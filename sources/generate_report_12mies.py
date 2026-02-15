import sys
from datetime import datetime
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import lake
from evaluate_predictions import run_evaluation

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
MONTH_NAMES = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12,
}
OKNO_HISTORII_LAT = 10
OKNO_REFERENCJA_MIESIACE = 12
HISTORIA_OD_ROKU = 1974
DATA_KONIEC_PROGNOZY = (2027, 1)
MIESIACE_DOPELNIENIA = (
    "stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca",
    "lipca", "sierpnia", "września", "października", "listopada", "grudnia",
)


def _data_referencyjna() -> tuple[int, int]:
    rok, mies = DATA_KONIEC_PROGNOZY
    mies -= 12
    if mies < 1:
        mies += 12
        rok -= 1
    return (rok, mies)


def _miesiace_symulacji() -> list[tuple[int, int]]:
    rok_ref, mies_ref = _data_referencyjna()
    mies_ref += 1
    if mies_ref > 12:
        mies_ref = 1
        rok_ref += 1
    out = []
    for _ in range(12):
        out.append((rok_ref, mies_ref))
        mies_ref += 1
        if mies_ref > 12:
            mies_ref = 1
            rok_ref += 1
    return out


TEMP_KLASY = ("zimny", "normalny", "ciepły")
OPAD_KLASY = ("suchy", "normalny", "wilgotny")
PERC_TEMP = {"zimny": 25, "normalny": 50, "ciepły": 75}
PERC_OPAD = {"suchy": 25, "normalny": 50, "wilgotny": 75}


def _monthly_percentiles(df: pd.DataFrame) -> dict[int, dict]:
    df = df.dropna(subset=[lake.COL_OPAD, lake.COL_TEMPERATURA])
    df["_month"] = df[lake.COL_DATA].dt.month
    out = {}
    for month in range(1, 13):
        sub = df[df["_month"] == month]
        if len(sub) < 5:
            out[month] = {"opad_25": 0.0, "opad_50": 0.0, "opad_75": 0.0, "temp_25": 0.0, "temp_50": 0.0, "temp_75": 0.0}
            continue
        opad = sub[lake.COL_OPAD].astype(float)
        temp = sub[lake.COL_TEMPERATURA].astype(float)
        out[month] = {
            "opad_25": float(np.percentile(opad, 25)),
            "opad_50": float(np.percentile(opad, 50)),
            "opad_75": float(np.percentile(opad, 75)),
            "temp_25": float(np.percentile(temp, 25)),
            "temp_50": float(np.percentile(temp, 50)),
            "temp_75": float(np.percentile(temp, 75)),
        }
    return out


def _get_variant_meteo(
    month_percentiles: dict[int, dict],
    temp_klasa: str,
    opad_klasa: str,
    months_sequence: list[tuple[int, int]],
) -> list[tuple[float, float]]:
    return [
        (
            month_percentiles[m][f"opad_{PERC_OPAD[opad_klasa]}"],
            month_percentiles[m][f"temp_{PERC_TEMP[temp_klasa]}"],
        )
        for _, m in months_sequence
    ]


def _dodaj_szanse_realizacji(df: pd.DataFrame, warianty: list[dict]) -> None:
    df_meteo = df.dropna(subset=[lake.COL_OPAD, lake.COL_TEMPERATURA]).sort_values(lake.COL_DATA)
    if len(df_meteo) < OKNO_REFERENCJA_MIESIACE:
        for v in warianty:
            v["szansa_pct"] = 100.0 / len(warianty) if warianty else 0.0
        return
    tail = df_meteo.tail(OKNO_REFERENCJA_MIESIACE)
    ref_opad = float(tail[lake.COL_OPAD].astype(float).mean())
    ref_temp = float(tail[lake.COL_TEMPERATURA].astype(float).mean())
    std_opad = float(tail[lake.COL_OPAD].astype(float).std()) or 1.0
    std_temp = float(tail[lake.COL_TEMPERATURA].astype(float).std()) or 1.0
    dists = []
    for v in warianty:
        o = v["suma_opadu"] / len(v["wyniki"])
        t = v["srednia_temp_roczna"]
        d = np.sqrt(((o - ref_opad) / std_opad) ** 2 + ((t - ref_temp) / std_temp) ** 2)
        dists.append(np.exp(-d))
    total = sum(dists)
    if total <= 0:
        total = 1.0
    for v, w in zip(warianty, dists):
        v["szansa_pct"] = round(100.0 * w / total, 1)


def _variant_to_filename(nazwa: str) -> str:
    t = nazwa.replace(", ", "_").replace(" ", "_").replace("ł", "l").replace("ó", "o").replace("ą", "a").replace("ę", "e").replace("ś", "s").replace("ć", "c").replace("ź", "z").replace("ż", "z")
    return t


def _run_simulation_for_meteo(
    model,
    feature_cols: list,
    lag_months: int,
    meteo_lag_months: int,
    level_start: float,
    last_changes: list,
    last_poziomy: list,
    last_opady: list,
    last_temperatury: list,
    max_poziom: float,
    odplyw_m: float,
    przesaczanie_m: float,
    meteo_sequence: list[tuple[float, float]],
    months_sequence: list[tuple[int, int]],
) -> list[dict]:
    level = level_start
    results = []
    for (opad, temp), (year, month) in zip(meteo_sequence, months_sequence):
        pred = lake.predict_change(
            model,
            feature_cols,
            level,
            opad,
            temp,
            month,
            last_changes=last_changes,
            last_poziomy=last_poziomy,
            last_opady=last_opady if last_opady else None,
            last_temperatury=last_temperatury if last_temperatury else None,
            lag_months=lag_months,
            meteo_lag_months=meteo_lag_months,
        )
        level = level + pred
        level = lake.apply_cap_and_drainage(level, max_poziom, odplyw_m, przesaczanie_m)
        results.append({
            "data": f"{year}-{month:02d}",
            "opad": opad,
            "temperatura": temp,
            "zmiana_prognoza": round(pred, 4),
            "poziom": round(level, 3),
        })
        last_changes = last_changes[1:] + [pred]
        last_poziomy = last_poziomy[1:] + [level]
        if meteo_lag_months:
            last_opady = (last_opady[1:] + [opad])[-meteo_lag_months:]
            last_temperatury = (last_temperatury[1:] + [temp])[-meteo_lag_months:]
    return results


def _data_ostatniego_pomiaru(df: pd.DataFrame) -> tuple[int, int] | None:
    df_poziom = df.dropna(subset=[lake.COL_POZIOM])
    if df_poziom.empty:
        return None
    ostatni = df_poziom.sort_values(lake.COL_DATA).iloc[-1]
    dt = ostatni[lake.COL_DATA]
    return (int(dt.year), int(dt.month))


def _symulacje_warianty(df: pd.DataFrame, lake_id: str, model_variant: str | None = None) -> list[dict] | None:
    if model_variant == "natural":
        model_path = lake.get_model_path(lake_id, "natural")
    else:
        model_path = lake.get_model_path(lake_id)
    if not model_path.exists():
        return None
    data_ost = _data_ostatniego_pomiaru(df)
    if data_ost is None:
        return None
    rok_ost, mies_ost = data_ost
    ym_ost = f"{rok_ost}-{mies_ost:02d}"
    model, feature_cols, lag_months, meteo_lag_months = lake.load_model(model_path)
    df["_ym"] = df[lake.COL_DATA].dt.year.astype(str) + "-" + df[lake.COL_DATA].dt.month.astype(str).str.zfill(2)
    hist = df[df["_ym"] <= ym_ost].copy()
    if hist.empty:
        return None
    last_row = hist.iloc[-1]
    level_start = float(last_row[lake.COL_POZIOM])
    hist_tail = hist.tail(lag_months)
    last_changes = [float(hist_tail.iloc[i][lake.COL_ZMIANA]) for i in range(len(hist_tail))]
    last_poziomy = [float(hist_tail.iloc[i][lake.COL_POZIOM]) for i in range(len(hist_tail))]
    while len(last_changes) < lag_months:
        last_changes.insert(0, 0.0)
        last_poziomy.insert(0, level_start)
    meteo_tail = hist.tail(meteo_lag_months) if meteo_lag_months else []
    last_opady = [float(meteo_tail.iloc[i][lake.COL_OPAD]) for i in range(len(meteo_tail))] if meteo_lag_months else []
    last_temperatury = [float(meteo_tail.iloc[i][lake.COL_TEMPERATURA]) for i in range(len(meteo_tail))] if meteo_lag_months else []
    max_poziom, odplyw_m, przesaczanie_m = lake.get_drainage_params(lake_id, df)
    month_percentiles = _monthly_percentiles(df)
    out = []
    for temp_klasa in TEMP_KLASY:
        for opad_klasa in OPAD_KLASY:
            nazwa = f"{temp_klasa}, {opad_klasa}"
            miesiace_sym = _miesiace_symulacji()
            meteo_seq = _get_variant_meteo(
                month_percentiles,
                temp_klasa,
                opad_klasa,
                miesiace_sym,
            )
            results = _run_simulation_for_meteo(
                model,
                feature_cols,
                lag_months,
                meteo_lag_months,
                level_start,
                list(last_changes),
                list(last_poziomy),
                list(last_opady),
                list(last_temperatury),
                max_poziom,
                odplyw_m,
                przesaczanie_m,
                meteo_seq,
                miesiace_sym,
            )
            if not results:
                continue
            poziom_koniec = results[-1]["poziom"]
            srednia_temp = float(np.mean([r["temperatura"] for r in results]))
            suma_opadu = sum(r["opad"] for r in results)
            roznica_poziomu = poziom_koniec - level_start
            out.append({
                "nazwa": nazwa,
                "temp_klasa": temp_klasa,
                "opad_klasa": opad_klasa,
                "wyniki": results,
                "poziom_koniec": poziom_koniec,
                "level_start": level_start,
                "srednia_temp_roczna": srednia_temp,
                "suma_opadu": suma_opadu,
                "roznica_poziomu": roznica_poziomu,
            })
    return out if out else None


def _parse_meteo_file(path: Path, value_idx: int = 1) -> dict[tuple[int, int], float]:
    out = {}
    for line in path.read_text(encoding="utf-8").strip().splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        head = parts[0].split()
        if len(head) < 2:
            continue
        month = MONTH_NAMES.get(head[0])
        if month is None:
            continue
        try:
            year = int(head[1])
            val = float(parts[value_idx].replace(",", ".").strip())
        except (ValueError, IndexError):
            continue
        out[(year, month)] = val
    return out


def _plot_wariant_symulacja(
    df: pd.DataFrame,
    data_referencyjna: tuple[int, int],
    level_na_data_referencyjna: float,
    wyniki: list[dict],
    out_path: Path,
    nazwa: str,
    nazwa_jeziora: str,
    wyniki_natural: list[dict] | None = None,
    level_na_data_referencyjna_natural: float | None = None,
) -> None:
    df_poziom = df.dropna(subset=[lake.COL_POZIOM]).copy()
    df_poziom = df_poziom.sort_values(lake.COL_DATA)
    if df_poziom.empty:
        return
    cutoff = pd.Timestamp(f"{HISTORIA_OD_ROKU}-01-01")
    hist = df_poziom[df_poziom[lake.COL_DATA] >= cutoff]
    hist_dates = pd.to_datetime(hist[lake.COL_DATA])
    hist_levels = hist[lake.COL_POZIOM].astype(float)
    rok_ref, mies_ref = data_referencyjna
    data_pierwsza_sym = f"{rok_ref}-{mies_ref:02d}-01"
    sim_dates = [data_pierwsza_sym] + [r["data"] + "-01" for r in wyniki]
    sim_levels = [level_na_data_referencyjna] + [float(r["poziom"]) for r in wyniki]
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(hist_dates, hist_levels, color="#1f77b4", linewidth=1.2, label=f"Historia (od {HISTORIA_OD_ROKU})")
    label_drain = "Symulacja model drenażowy (12 mies.)" if (wyniki_natural is not None) else "Symulacja (12 mies.)"
    ax.plot(pd.to_datetime(sim_dates), sim_levels, color="#d62728", linewidth=1.5, marker="o", markersize=4, label=label_drain)
    if wyniki_natural is not None and level_na_data_referencyjna_natural is not None:
        sim_dates_nat = [data_pierwsza_sym] + [r["data"] + "-01" for r in wyniki_natural]
        sim_levels_nat = [level_na_data_referencyjna_natural] + [float(r["poziom"]) for r in wyniki_natural]
        ax.plot(pd.to_datetime(sim_dates_nat), sim_levels_nat, color="#2ca02c", linewidth=1.5, marker="s", markersize=4, label="Symulacja model naturalny (12 mies.)")
    ax.set_xlabel("Data")
    ax.set_ylabel("Wysokość (m n.p.m.)")
    suffix = " (dwa modele)" if wyniki_natural else ""
    ax.set_title(f"{nazwa_jeziora} – {nazwa}: pełny zakres od {HISTORIA_OD_ROKU} + 12 mies. symulacji{suffix}")
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.legend(loc="best")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150)
    plt.close()


def _plot_poziom_rzeczywisty_i_model(
    df: pd.DataFrame,
    eval_rows: list | None,
    out_path: Path,
    nazwa_jeziora: str,
    lake_id: str,
    eval_rows_natural: list | None = None,
) -> None:
    df = df.dropna(subset=[lake.COL_POZIOM])
    if df.empty:
        return
    dates = pd.to_datetime(df[lake.COL_DATA])
    poziom = df[lake.COL_POZIOM].astype(float)
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(dates, poziom, color="#1f77b4", linewidth=1.2, label="Poziom wody (rzeczywisty pomiar)")
    if eval_rows_natural:
        dates_nat = pd.to_datetime([r["data"] + "-01" for r in eval_rows_natural])
        natural_level = [float(r["wysokosc_model"]) for r in eval_rows_natural]
        ax.plot(dates_nat, natural_level, color="#2ca02c", linewidth=1.2, linestyle=":", label="Model naturalny (sprzed drenażu)")
    ax.set_xlabel("Data")
    ax.set_ylabel("Wysokość (m n.p.m.)")
    ax.set_title(f"{nazwa_jeziora} – poziom wody: rzeczywisty pomiar i scenariusze modelowe")
    ax.legend(loc="best")
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150)
    plt.close()


def _format_koniec_miesiaca(rok: int, miesiac: int) -> str:
    return f"{MIESIACE_DOPELNIENIA[miesiac - 1]} {rok}"


def _format_zmiana_m_cm(roznica_m: float) -> str:
    cm = roznica_m * 100
    return f"{roznica_m:+.3f} m ({cm:+.1f} cm)"


def _format_zmiana_cm(zmiana_m: float) -> str:
    return f"{zmiana_m * 100:+.1f} cm"


def _write_report(
    fig_filename: str,
    nazwa_jeziora: str,
    lake_id: str,
    warianty: list[dict] | None = None,
    wariant_najbardziej_prawdopodobny: dict | None = None,
    warianty_natural: list[dict] | None = None,
    wariant_najbardziej_prawdopodobny_natural: dict | None = None,
    data_koniec_prognozy: tuple[int, int] = DATA_KONIEC_PROGNOZY,
    data_referencyjna: tuple[int, int] | None = None,
    level_na_data_referencyjna: float | None = None,
) -> str:
    if data_referencyjna is None:
        data_referencyjna = _data_referencyjna()
    lines = [
        f"# Raport: {nazwa_jeziora}",
        "",
        f"Raport ewaluacji na następne 12 miesięcy dla {nazwa_jeziora}.",
        "",
        "## Poziom wody: rzeczywisty pomiar i model",
        "",
        f"Niebieska: poziom z `data/{lake_id}/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).",
        "",
        f"![Poziom wody – pomiar i model]({fig_filename})",
        "",
    ]
    if warianty:
        lines.extend([
            "## Prognoza 12 mies.",
            "",
            f"Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/{lake_id}/data.csv`. Symulacja: 12 miesięcy do końca {_format_koniec_miesiaca(*data_koniec_prognozy)} (stan na koniec {_format_koniec_miesiaca(*data_referencyjna)} to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.",
            "",
            "**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):",
            "",
        ])
        if warianty_natural:
            lines.append("| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |")
            lines.append("|---------|------------|-----------------------------|------------------------------|")
            nat_by_nazwa = {v["nazwa"]: v for v in warianty_natural}
            for v in warianty:
                if v.get("szansa_pct") is not None:
                    vn = nat_by_nazwa.get(v["nazwa"])
                    pn = round(vn["poziom_koniec"], 3) if vn else "—"
                    lines.append(f"| {v['nazwa']} | {v['szansa_pct']} | {round(v['poziom_koniec'], 3)} | {pn} |")
        else:
            lines.append("| Wariant | Szansa realizacji (%) |")
            lines.append("|---------|------------------------|")
            for v in warianty:
                if v.get("szansa_pct") is not None:
                    lines.append(f"| {v['nazwa']} | {v['szansa_pct']} |")
        rok_kon, mies_kon = data_koniec_prognozy
        rok_ref, mies_ref = data_referencyjna
        level_ref = level_na_data_referencyjna if level_na_data_referencyjna is not None else warianty[0]["level_start"]
        if wariant_najbardziej_prawdopodobny:
            poziom_wazony = wariant_najbardziej_prawdopodobny["poziom_koniec"]
        else:
            poziom_wazony = sum(v["poziom_koniec"] * (v["szansa_pct"] / 100.0) for v in warianty if v.get("szansa_pct") is not None)
        roznica = poziom_wazony - level_ref
        roznica_txt = f"przybędzie {_format_zmiana_m_cm(roznica)}" if roznica >= 0 else f"ubędzie {-roznica:.3f} m ({roznica * 100:+.1f} cm)"
        txt_koniec = _format_koniec_miesiaca(rok_kon, mies_kon)
        txt_ref = _format_koniec_miesiaca(rok_ref, mies_ref)
        level_ref_nat = level_na_data_referencyjna if level_na_data_referencyjna is not None else (warianty_natural[0]["level_start"] if warianty_natural else level_ref)
        if wariant_najbardziej_prawdopodobny_natural is not None:
            poziom_wazony_nat = wariant_najbardziej_prawdopodobny_natural["poziom_koniec"]
            roznica_nat = poziom_wazony_nat - level_ref_nat
            roznica_txt_nat = f"przybędzie {_format_zmiana_m_cm(roznica_nat)}" if roznica_nat >= 0 else f"ubędzie {-roznica_nat:.3f} m ({roznica_nat * 100:+.1f} cm)"
        else:
            poziom_wazony_nat = roznica_txt_nat = None
        lines.append("")
        lines.append(f"**Najbardziej prawdopodobny poziom na koniec {txt_koniec}** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec {txt_ref} ({level_ref} m n.p.m.):")
        lines.append(f"- **Model drenażowy:** {round(poziom_wazony, 3)} m n.p.m. – {roznica_txt}")
        if poziom_wazony_nat is not None and roznica_txt_nat:
            lines.append(f"- **Model naturalny (sprzed drenażu):** {round(poziom_wazony_nat, 3)} m n.p.m. – {roznica_txt_nat}")
        lines.extend(["", ""])
        nat_by_nazwa = {}
        if warianty_natural:
            for v in ([wariant_najbardziej_prawdopodobny_natural] if wariant_najbardziej_prawdopodobny_natural else []) + warianty_natural:
                nat_by_nazwa[v["nazwa"]] = v
        warianty_do_sekcji = ([wariant_najbardziej_prawdopodobny] if wariant_najbardziej_prawdopodobny else []) + warianty
        for v in warianty_do_sekcji:
            nazwa = v["nazwa"]
            fname = f"symulacja_wariant_{_variant_to_filename(nazwa)}.png"
            v_nat = nat_by_nazwa.get(nazwa)
            lines.extend([f"### {nazwa}", "", f"![Symulacja {nazwa}]({fname})", ""])
            if v_nat and len(v_nat["wyniki"]) == len(v["wyniki"]):
                lines.extend([
                    "| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |",
                    "|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|",
                ])
                for r, rn in zip(v["wyniki"], v_nat["wyniki"]):
                    lines.append(f"| {r['data']} | {round(r['opad'], 1)} | {round(r['temperatura'], 1)} | {_format_zmiana_cm(r['zmiana_prognoza'])} | {r['poziom']} | {_format_zmiana_cm(rn['zmiana_prognoza'])} | {rn['poziom']} |")
            else:
                lines.extend([
                    "| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |",
                    "|------|-----------|------------------|----------------------|-------------------|",
                ])
                for r in v["wyniki"]:
                    lines.append(f"| {r['data']} | {round(r['opad'], 1)} | {round(r['temperatura'], 1)} | {_format_zmiana_cm(r['zmiana_prognoza'])} | {r['poziom']} |")
            szansa_line = "- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**" if v.get("czy_srednia_wazona") else f"- **Szansa realizacji:** {v['szansa_pct']} %"
            lines.extend([
                "",
                szansa_line,
                f"- **Średnia temperatura roczna (prognoza):** {round(v['srednia_temp_roczna'], 1)} °C",
                f"- **Suma opadu (prognoza):** {round(v['suma_opadu'], 1)} mm",
                f"- **Różnica poziomu wody (drenaż)** (koniec − start): {_format_zmiana_m_cm(v['roznica_poziomu'])}",
                f"- **Poziom na koniec {_format_koniec_miesiaca(*data_koniec_prognozy)} (drenaż):** {round(v['poziom_koniec'], 3)} m n.p.m.",
            ])
            if v_nat:
                lines.append(f"- **Różnica poziomu wody (natural)** (koniec − start): {_format_zmiana_m_cm(v_nat['roznica_poziomu'])}")
                lines.append(f"- **Poziom na koniec {_format_koniec_miesiaca(*data_koniec_prognozy)} (natural):** {round(v_nat['poziom_koniec'], 3)} m n.p.m.")
            lines.extend(["", ""])
        lines.append("")
    lines.append("")
    lines.append(f"*Wygenerowano: {datetime.now().strftime('%Y-%m-%d %H:%M')}*")
    return "\n".join(lines)


def _build_szanse_odbudowy_opis(
    nazwa_jeziora: str,
    lake_id: str,
    warianty: list[dict],
    wariant_najbardziej_prawdopodobny: dict | None,
    level_ref: float,
    data_referencyjna: tuple[int, int],
    data_koniec_prognozy: tuple[int, int],
    warianty_natural: list[dict] | None = None,
    wariant_najbardziej_prawdopodobny_natural: dict | None = None,
) -> str:
    rok_kon, mies_kon = data_koniec_prognozy
    rok_ref, mies_ref = data_referencyjna
    txt_ref = _format_koniec_miesiaca(rok_ref, mies_ref)
    txt_koniec = _format_koniec_miesiaca(rok_kon, mies_kon)
    if wariant_najbardziej_prawdopodobny:
        poziom_wazony = wariant_najbardziej_prawdopodobny["poziom_koniec"]
    else:
        poziom_wazony = sum(
            v["poziom_koniec"] * (v["szansa_pct"] / 100.0)
            for v in warianty
            if v.get("szansa_pct") is not None
        )
    roznica_m = poziom_wazony - level_ref
    roznica_cm = roznica_m * 100
    warianty_bez_np = [v for v in warianty if not v.get("czy_srednia_wazona")]
    if warianty_bez_np:
        zmiany_cm = [v["roznica_poziomu"] * 100 for v in warianty_bez_np]
        min_cm = min(zmiany_cm)
        max_cm = max(zmiany_cm)
    else:
        min_cm = max_cm = roznica_cm
    max_szansa = max((v.get("szansa_pct") or 0) for v in warianty) if warianty else 0
    if wariant_najbardziej_prawdopodobny_natural is not None:
        poziom_wazony_nat = wariant_najbardziej_prawdopodobny_natural["poziom_koniec"]
        roznica_nat_cm = (poziom_wazony_nat - level_ref) * 100
    else:
        poziom_wazony_nat = roznica_nat_cm = None
    lines = [
        f"# Szanse na odbudowę – {nazwa_jeziora}",
        "",
        "Opisowa ocena szans na odbudowę poziomu wody w perspektywie **kolejnych 12 miesięcy**, na podstawie prognozy z symulacji wariantów pogodowych (opad i temperatura z percentyli historycznych) oraz szacowanych szans realizacji każdego wariantu (zgodność z ostatnimi 12 miesiącami pomiarowymi).",
        "",
        f"**Stan odniesienia:** koniec {txt_ref} – poziom {level_ref:.3f} m n.p.m.",
        "",
    ]
    if poziom_wazony_nat is not None and roznica_nat_cm is not None:
        lines.extend([
            "**Porównanie prognoz** (najbardziej prawdopodobny scenariusz, średnia ważona):",
            "",
            "| Model | Poziom koniec (m n.p.m.) | Zmiana (cm) |",
            "|-------|-------------------------------------|-------------|",
            f"| Drenażowy (po zmianie reżimu) | {poziom_wazony:.3f} | {roznica_cm:+.1f} |",
            f"| Naturalny (sprzed drenażu) | {poziom_wazony_nat:.3f} | {roznica_nat_cm:+.1f} |",
            "",
        ])
    lines.extend([
        f"**Prognoza na koniec {txt_koniec}** (model drenażowy): poziom **{poziom_wazony:.3f} m n.p.m.**, czyli **{'wzrost' if roznica_cm >= 0 else 'spadek'} o {abs(roznica_cm):.1f} cm** w stosunku do stanu odniesienia.",
        "",
        f"W zależności od warunków pogodowych w nadchodzącym roku prognozowana zmiana poziomu w 12 miesięcy (model drenażowy) mieści się w zakresie od **{min_cm:+.1f} cm** do **{max_cm:+.1f} cm**. Najwyższą szansę realizacji ({max_szansa:.1f}%) ma jeden z wariantów pogodowych; szczegóły wszystkich wariantów i szans – w raporcie [Prognoza 12 mies.](#docs-{lake_id}-prognoza).",
        "",
    ])
    if roznica_cm >= 5:
        sent = "prognoza **modelu drenażowego** wskazuje na **możliwy przyrost** poziomu w ciągu roku; sprzyja to odbudowie, o ile utrzyma się tendencja i nie nasili się drenaż."
    elif roznica_cm >= 0:
        sent = "prognoza **modelu drenażowego** wskazuje na **stabilizację lub niewielki przyrost** poziomu w ciągu roku; szanse na odbudowę w tej perspektywie są umiarkowane."
    elif roznica_cm >= -10:
        sent = "prognoza **modelu drenażowego** wskazuje na **niewielki spadek** poziomu w ciągu roku; szanse na odbudowę w perspektywie 12 miesięcy są ograniczone bez zatrzymania drenażu."
    else:
        sent = "prognoza **modelu drenażowego** wskazuje na **spadek** poziomu w ciągu roku; szanse na odbudowę w perspektywie roku są niskie – istotna odbudowa wymagałaby zatrzymania drenażu i korzystnych warunków."
    lines.append("**Szanse na odbudowę w perspektywie roku (model drenażowy):** " + sent)
    if poziom_wazony_nat is not None and roznica_nat_cm is not None:
        if roznica_nat_cm >= 5:
            sent_nat = "prognoza **modelu naturalnego** (sprzed drenażu) wskazuje na **możliwy przyrost** poziomu w ciągu roku."
        elif roznica_nat_cm >= 0:
            sent_nat = "prognoza **modelu naturalnego** wskazuje na **stabilizację lub niewielki przyrost** poziomu w ciągu roku."
        elif roznica_nat_cm >= -10:
            sent_nat = "prognoza **modelu naturalnego** wskazuje na **niewielki spadek** poziomu w ciągu roku."
        else:
            sent_nat = "prognoza **modelu naturalnego** wskazuje na **spadek** poziomu w ciągu roku."
        lines.extend(["", "**Szanse na odbudowę w perspektywie roku (model naturalny):** " + sent_nat])
    lines.extend([
        "",
        f"Szacunki długoterminowej odbudowy (lata do zamknięcia luki po ewentualnym zaniku drenażu) – patrz [Zanik drenażu](#docs-{lake_id}-zanik-drenazu).",
        "",
        f"*Wygenerowano: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
    ])
    return "\n".join(lines)


def _wariant_najbardziej_prawdopodobny(
    warianty: list[dict],
    level_start_symulacji: float,
    level_ref_do_porownania: float,
) -> dict:
    poziom_akt = level_start_symulacji
    wyniki = []
    for i in range(12):
        zmiana_i = sum(v["wyniki"][i]["zmiana_prognoza"] * (v["szansa_pct"] / 100.0) for v in warianty)
        opad_i = sum(v["wyniki"][i]["opad"] * (v["szansa_pct"] / 100.0) for v in warianty)
        temp_i = sum(v["wyniki"][i]["temperatura"] * (v["szansa_pct"] / 100.0) for v in warianty)
        poziom_akt = poziom_akt + zmiana_i
        wyniki.append({
            "data": warianty[0]["wyniki"][i]["data"],
            "opad": opad_i,
            "temperatura": temp_i,
            "zmiana_prognoza": round(zmiana_i, 4),
            "poziom": round(poziom_akt, 3),
        })
    poziom_koniec = round(poziom_akt, 3)
    return {
        "nazwa": "najbardziej prawdopodobny",
        "wyniki": wyniki,
        "poziom_koniec": poziom_koniec,
        "level_start": level_ref_do_porownania,
        "srednia_temp_roczna": sum(r["temperatura"] for r in wyniki) / 12,
        "suma_opadu": sum(r["opad"] for r in wyniki),
        "roznica_poziomu": poziom_koniec - level_ref_do_porownania,
        "szansa_pct": None,
        "czy_srednia_wazona": True,
    }


def _level_na_koniec_miesiaca(df: pd.DataFrame, rok: int, miesiac: int) -> float | None:
    df_poziom = df.dropna(subset=[lake.COL_POZIOM])
    wiersze = df_poziom[(df_poziom[lake.COL_DATA].dt.year == rok) & (df_poziom[lake.COL_DATA].dt.month == miesiac)]
    if wiersze.empty:
        return None
    return float(wiersze.iloc[0][lake.COL_POZIOM])


def run_report_for_lake(lake_id: str) -> None:
    figures_dir = DOCS_DIR / lake_id
    report_path = figures_dir / "prognoza.md"
    nazwa_jeziora = lake.LAKES.get(lake_id, lake_id)
    df = lake.load_data(lake.get_data_path(lake_id))
    eval_rows = None
    if lake.get_model_path(lake_id).exists():
        _, _, eval_rows = run_evaluation(lake_id=lake_id)
    eval_rows_natural = None
    natural_path = lake.get_model_path(lake_id, "natural")
    if not natural_path.exists() and lake.get_model_path(lake_id).exists():
        print(f"Brak modelu naturalnego dla {lake_id}, trening...")
        lake.run_training_and_save(lake_id, variant="natural")
    if natural_path.exists():
        _, _, eval_rows_natural = run_evaluation(
            lake_id=lake_id,
            model_path=natural_path,
            output_path=figures_dir / "podsumowanie_ewaluacji_natural.md",
        )
    fig_path = figures_dir / "poziom_rzeczywisty.png"
    _plot_poziom_rzeczywisty_i_model(
        df,
        eval_rows,
        fig_path,
        nazwa_jeziora=nazwa_jeziora,
        lake_id=lake_id,
        eval_rows_natural=eval_rows_natural,
    )
    print(f"Wykres zapisany: {fig_path}")
    warianty = _symulacje_warianty(df, lake_id)
    data_ref = _data_referencyjna()
    level_na_data_ref = _level_na_koniec_miesiaca(df, data_ref[0], data_ref[1])
    wariant_np = None
    if warianty:
        _dodaj_szanse_realizacji(df, warianty)
        level_na_data_ref_plot = level_na_data_ref if level_na_data_ref is not None else warianty[0]["level_start"]
        wariant_np = _wariant_najbardziej_prawdopodobny(
            warianty,
            level_start_symulacji=warianty[0]["level_start"],
            level_ref_do_porownania=level_na_data_ref if level_na_data_ref is not None else warianty[0]["level_start"],
        )
    natural_by_nazwa = {}
    if natural_path.exists():
        warianty_natural = _symulacje_warianty(df, lake_id, model_variant="natural")
    else:
        warianty_natural = None
    wariant_np_natural = None
    if warianty_natural:
        _dodaj_szanse_realizacji(df, warianty_natural)
        level_ref_nat = level_na_data_ref if level_na_data_ref is not None else warianty_natural[0]["level_start"]
        wariant_np_natural = _wariant_najbardziej_prawdopodobny(
            warianty_natural,
            level_start_symulacji=warianty_natural[0]["level_start"],
            level_ref_do_porownania=level_ref_nat,
        )
        for v in [wariant_np_natural] + warianty_natural:
            natural_by_nazwa[v["nazwa"]] = v["wyniki"]
    if warianty:
        for v in [wariant_np] + warianty:
            wyniki_nat = natural_by_nazwa.get(v["nazwa"])
            path_wariant = figures_dir / f"symulacja_wariant_{_variant_to_filename(v['nazwa'])}.png"
            _plot_wariant_symulacja(
                df=df,
                data_referencyjna=data_ref,
                level_na_data_referencyjna=level_na_data_ref_plot,
                wyniki=v["wyniki"],
                out_path=path_wariant,
                nazwa=v["nazwa"],
                nazwa_jeziora=nazwa_jeziora,
                wyniki_natural=wyniki_nat,
                level_na_data_referencyjna_natural=level_na_data_ref_plot if wyniki_nat else None,
            )
            print(f"Wykres wariantu zapisany: {path_wariant}")
    content = _write_report(
        "poziom_rzeczywisty.png",
        nazwa_jeziora=nazwa_jeziora,
        lake_id=lake_id,
        warianty=warianty,
        wariant_najbardziej_prawdopodobny=wariant_np,
        warianty_natural=warianty_natural,
        wariant_najbardziej_prawdopodobny_natural=wariant_np_natural,
        data_referencyjna=data_ref,
        level_na_data_referencyjna=level_na_data_ref,
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(content, encoding="utf-8")
    print(f"Raport zapisany: {report_path}")
    if warianty:
        level_ref = level_na_data_ref if level_na_data_ref is not None else warianty[0]["level_start"]
        szanse_content = _build_szanse_odbudowy_opis(
            nazwa_jeziora=nazwa_jeziora,
            lake_id=lake_id,
            warianty=warianty,
            wariant_najbardziej_prawdopodobny=wariant_np,
            level_ref=level_ref,
            data_referencyjna=data_ref,
            data_koniec_prognozy=DATA_KONIEC_PROGNOZY,
            warianty_natural=warianty_natural,
            wariant_najbardziej_prawdopodobny_natural=wariant_np_natural,
        )
        szanse_path = figures_dir / "szanse_odbudowy.md"
        szanse_path.write_text(szanse_content, encoding="utf-8")
        print(f"Szanse na odbudowę zapisane: {szanse_path}")


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1].lower() == "all":
        for lid in lake.LAKES:
            if not lake.get_model_path(lid).exists():
                print(f"Pomijam {lid}: brak modelu.")
                continue
            print(f"\n--- {lake.LAKES.get(lid, lid)} ---")
            run_report_for_lake(lid)
        return
    lake_id = sys.argv[1] if len(sys.argv) > 1 else "niedziegiel"
    if lake_id not in lake.LAKES:
        print(f"Dostępne jeziora: {', '.join(lake.LAKES)}")
        sys.exit(1)
    if not lake.get_model_path(lake_id).exists():
        print(f"Brak modelu dla {lake_id}: {lake.get_model_path(lake_id)}")
        sys.exit(1)
    run_report_for_lake(lake_id)


if __name__ == "__main__":
    main()
