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
FIGURES_DIR = DOCS_DIR / "niedziegiel"
REPORT_PATH = DOCS_DIR / "niedziegiel" / "raport.md"
LAKE_ID = "niedziegiel"
OPAD_PATH = DATA_DIR / "niedziegiel" / "opad.txt"
TEMP_PATH = DATA_DIR / "niedziegiel" / "temp.txt"
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


def _symulacje_warianty(df: pd.DataFrame) -> list[dict] | None:
    model_path = lake.get_model_path(LAKE_ID)
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
    max_poziom, odplyw_m, przesaczanie_m = lake.get_drainage_params(LAKE_ID, df)
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
    ax.plot(pd.to_datetime(sim_dates), sim_levels, color="#d62728", linewidth=1.5, marker="o", markersize=4, label="Symulacja (12 mies.)")
    ax.set_xlabel("Data")
    ax.set_ylabel("Wysokość (m n.p.m.)")
    ax.set_title(f"Jezioro Niedzięgiel – {nazwa}: pełny zakres od {HISTORIA_OD_ROKU} + 12 mies. symulacji")
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
) -> None:
    df = df.dropna(subset=[lake.COL_POZIOM])
    if df.empty:
        return
    dates = pd.to_datetime(df[lake.COL_DATA])
    poziom = df[lake.COL_POZIOM].astype(float)
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(dates, poziom, color="#1f77b4", linewidth=1.2, label="Poziom wody (rzeczywisty pomiar)")
    if eval_rows:
        dates_model = pd.to_datetime([r["data"] + "-01" for r in eval_rows])
        model_level = [float(r["wysokosc_model"]) for r in eval_rows]
        ax.plot(dates_model, model_level, color="#ff7f0e", linewidth=1.2, linestyle="--", label="Wahania według modelu")
    ax.set_xlabel("Data")
    ax.set_ylabel("Wysokość (m n.p.m.)")
    ax.set_title("Jezioro Niedzięgiel – poziom wody: rzeczywisty pomiar i scenariusz modelowy")
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
    warianty: list[dict] | None = None,
    wariant_najbardziej_prawdopodobny: dict | None = None,
    data_koniec_prognozy: tuple[int, int] = DATA_KONIEC_PROGNOZY,
    data_referencyjna: tuple[int, int] | None = None,
    level_na_data_referencyjna: float | None = None,
) -> str:
    if data_referencyjna is None:
        data_referencyjna = _data_referencyjna()
    lines = [
        "# Raport: Jezioro Niedzięgiel",
        "",
        "Raport dedykowany tylko dla Jeziora Niedzięgiel.",
        "",
        "## Poziom wody: rzeczywisty pomiar i model",
        "",
        "Niebieska linia: poziom z pliku `data/niedziegiel/data.csv` (pomiar na pierwszy dzień miesiąca). Przerywana pomarańczowa: wahania poziomu według modelu (scenariusz kumulatywny z prognozy zmiany miesięcznej).",
        "",
        f"![Poziom wody – pomiar i model]({fig_filename})",
        "",
    ]
    if warianty:
        lines.extend([
            "## Symulacje wariantów pogodowych (12 miesięcy do przodu)",
            "",
            f"Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/niedziegiel/data.csv`. Symulacja: 12 miesięcy do końca {_format_koniec_miesiaca(*data_koniec_prognozy)} (stan na koniec {_format_koniec_miesiaca(*data_referencyjna)} to pomiar rzeczywisty). Wykres: pełny zakres historii (od {HISTORIA_OD_ROKU}) + 12 miesięcy symulacji.",
            "",
            "**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):",
            "",
            "| Wariant | Szansa realizacji (%) |",
            "|---------|------------------------|",
        ])
        for v in warianty:
            if v.get("szansa_pct") is not None:
                lines.append(f"| {v['nazwa']} | {v['szansa_pct']} |")
        rok_kon, mies_kon = data_koniec_prognozy
        rok_ref, mies_ref = data_referencyjna
        poziom_wazony = sum(v["poziom_koniec"] * (v["szansa_pct"] / 100.0) for v in warianty if v.get("szansa_pct") is not None)
        level_ref = level_na_data_referencyjna if level_na_data_referencyjna is not None else warianty[0]["level_start"]
        roznica = poziom_wazony - level_ref
        roznica_txt = f"przybędzie {_format_zmiana_m_cm(roznica)}" if roznica >= 0 else f"ubędzie {-roznica:.3f} m ({roznica * 100:+.1f} cm)"
        txt_koniec = _format_koniec_miesiaca(rok_kon, mies_kon)
        txt_ref = _format_koniec_miesiaca(rok_ref, mies_ref)
        lines.extend([
            "",
            f"**Najbardziej prawdopodobny poziom na koniec {txt_koniec}** (średnia ważona według szans realizacji wszystkich wariantów): **{round(poziom_wazony, 3)} m n.p.m.** W stosunku do stanu na koniec {txt_ref} ({level_ref} m n.p.m.): {roznica_txt}.",
            "",
            "",
        ])
        warianty_do_sekcji = ([wariant_najbardziej_prawdopodobny] if wariant_najbardziej_prawdopodobny else []) + warianty
        for v in warianty_do_sekcji:
            nazwa = v["nazwa"]
            fname = f"symulacja_wariant_{_variant_to_filename(nazwa)}.png"
            lines.extend([
                f"### {nazwa}",
                "",
                f"![Symulacja {nazwa}]({fname})",
                "",
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
                f"- **Różnica poziomu wody** (koniec symulacji − start): {_format_zmiana_m_cm(v['roznica_poziomu'])}",
                f"- **Poziom na koniec {_format_koniec_miesiaca(*data_koniec_prognozy)}:** {v['poziom_koniec']} m n.p.m.",
                "",
            ])
        lines.append("")
    lines.append("")
    lines.append(f"*Wygenerowano: {datetime.now().strftime('%Y-%m-%d %H:%M')}*")
    return "\n".join(lines)


def _wariant_najbardziej_prawdopodobny(
    warianty: list[dict],
    level_na_data_ref: float,
) -> dict:
    level_prev = level_na_data_ref
    wyniki = []
    for i in range(12):
        poziom_i = sum(v["wyniki"][i]["poziom"] * (v["szansa_pct"] / 100.0) for v in warianty)
        opad_i = sum(v["wyniki"][i]["opad"] * (v["szansa_pct"] / 100.0) for v in warianty)
        temp_i = sum(v["wyniki"][i]["temperatura"] * (v["szansa_pct"] / 100.0) for v in warianty)
        zmiana_i = poziom_i - level_prev
        level_prev = poziom_i
        wyniki.append({
            "data": warianty[0]["wyniki"][i]["data"],
            "opad": opad_i,
            "temperatura": temp_i,
            "zmiana_prognoza": round(zmiana_i, 4),
            "poziom": round(poziom_i, 3),
        })
    poziom_koniec = wyniki[-1]["poziom"]
    return {
        "nazwa": "najbardziej prawdopodobny",
        "wyniki": wyniki,
        "poziom_koniec": poziom_koniec,
        "level_start": level_na_data_ref,
        "srednia_temp_roczna": sum(r["temperatura"] for r in wyniki) / 12,
        "suma_opadu": sum(r["opad"] for r in wyniki),
        "roznica_poziomu": poziom_koniec - level_na_data_ref,
        "szansa_pct": None,
        "czy_srednia_wazona": True,
    }


def _level_na_koniec_miesiaca(df: pd.DataFrame, rok: int, miesiac: int) -> float | None:
    df_poziom = df.dropna(subset=[lake.COL_POZIOM])
    wiersze = df_poziom[(df_poziom[lake.COL_DATA].dt.year == rok) & (df_poziom[lake.COL_DATA].dt.month == miesiac)]
    if wiersze.empty:
        return None
    return float(wiersze.iloc[0][lake.COL_POZIOM])


def main() -> None:
    df = lake.load_data(lake.get_data_path(LAKE_ID))
    eval_rows = None
    if lake.get_model_path(LAKE_ID).exists():
        _, _, eval_rows = run_evaluation(lake_id=LAKE_ID)
    fig_path = FIGURES_DIR / "poziom_rzeczywisty.png"
    _plot_poziom_rzeczywisty_i_model(df, eval_rows, fig_path)
    print(f"Wykres zapisany: {fig_path}")
    warianty = _symulacje_warianty(df)
    data_ref = _data_referencyjna()
    level_na_data_ref = _level_na_koniec_miesiaca(df, data_ref[0], data_ref[1])
    wariant_np = None
    if warianty:
        _dodaj_szanse_realizacji(df, warianty)
        level_na_data_ref_plot = level_na_data_ref if level_na_data_ref is not None else warianty[0]["level_start"]
        wariant_np = _wariant_najbardziej_prawdopodobny(warianty, level_na_data_ref_plot)
        for v in [wariant_np] + warianty:
            path_wariant = FIGURES_DIR / f"symulacja_wariant_{_variant_to_filename(v['nazwa'])}.png"
            _plot_wariant_symulacja(
                df=df,
                data_referencyjna=data_ref,
                level_na_data_referencyjna=level_na_data_ref_plot,
                wyniki=v["wyniki"],
                out_path=path_wariant,
                nazwa=v["nazwa"],
            )
            print(f"Wykres wariantu zapisany: {path_wariant}")
    content = _write_report(
        "poziom_rzeczywisty.png",
        warianty=warianty,
        wariant_najbardziej_prawdopodobny=wariant_np,
        data_referencyjna=data_ref,
        level_na_data_referencyjna=level_na_data_ref,
    )
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(content, encoding="utf-8")
    print(f"Raport zapisany: {REPORT_PATH}")


if __name__ == "__main__":
    main()
