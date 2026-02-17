from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import lake
from evaluate_predictions import run_evaluation

_RECOVERY_DIR = Path(__file__).resolve().parent
ROOT = _RECOVERY_DIR.parent if not (_RECOVERY_DIR / "data").exists() else _RECOVERY_DIR
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
FIGURES_ODBUDOWA_DIR = DOCS_DIR / "odbudowa"
OUTPUT_PATH = DOCS_DIR / "szacunek_odbudowy_po_zaniku_drenazu.md"
ZANIK_DRENAZU_CSV = DATA_DIR / "zanik_drenazu.csv"
RECOVERY_RATE_FIXED_CM_PER_YEAR = 5.0
AVG_METEO_YEARS = 5
PROJEKCJA_METEO_YEARS = 15
PROJECTION_END_YEAR = 2060
PROJECTION_MAX_YEAR = 2060
RECOVERY_START_YEAR = 2026
RECOVERY_START_MONTH = 2
MIESIACE_NAZWA = ("styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień")


def _load_wznios_by_lake() -> dict[str, dict]:
    if not ZANIK_DRENAZU_CSV.exists():
        return {}
    df = pd.read_csv(ZANIK_DRENAZU_CSV, encoding="utf-8")
    if "Jezioro" not in df.columns or "Fibo_cm_na_rok" not in df.columns or "Fibo_cm_na_rok_po_zalaniu" not in df.columns:
        return {}
    return {
        str(row["Jezioro"]).strip(): {
            "wznios_cm_rok": float(row["Fibo_cm_na_rok"]) if pd.notna(row.get("Fibo_cm_na_rok")) else None,
            "wznios_po_zalaniu_cm_rok": float(row["Fibo_cm_na_rok_po_zalaniu"]) if pd.notna(row.get("Fibo_cm_na_rok_po_zalaniu")) else None,
        }
        for _, row in df.iterrows()
    }


def _decimal_year(ym: str) -> float:
    y, m = int(ym[:4]), int(ym[5:7])
    return y + (m - 0.5) / 12.0


def _trend_cm_per_year(dates: list, values_m: list) -> float | None:
    if len(dates) < 2 or len(values_m) < 2:
        return None
    x = np.array([_decimal_year(d) for d in dates], dtype=float)
    y = np.array(values_m, dtype=float)
    slope = np.polyfit(x, y, 1)[0]
    return float(slope * 100.0)


def _mean_last_n_months(rows: list, n: int = 12) -> float | None:
    if not rows or n <= 0:
        return None
    take = rows[-n:]
    divergences = [r["rozbieznosc"] for r in take]
    return float(np.mean(divergences))


def _avg_meteo_last_n_years(df: pd.DataFrame, n: int) -> dict[int, tuple[float, float]]:
    cutoff_year = df[lake.COL_DATA].dt.year.max() - n + 1
    df = df[df[lake.COL_DATA].dt.year >= cutoff_year]
    if df.empty:
        return {m: (0.0, 0.0) for m in range(1, 13)}
    by_month = df.groupby(df[lake.COL_DATA].dt.month).agg(
        {lake.COL_OPAD: "mean", lake.COL_TEMPERATURA: "mean"}
    )
    result = {}
    for month in range(1, 13):
        if month in by_month.index:
            result[month] = (float(by_month.loc[month, lake.COL_OPAD]), float(by_month.loc[month, lake.COL_TEMPERATURA]))
        else:
            result[month] = (float(df[lake.COL_OPAD].mean()), float(df[lake.COL_TEMPERATURA].mean()))
    return result


def _meteo_sequence_last_n_years(df: pd.DataFrame, n: int) -> list[tuple[float, float]]:
    df_meteo = df.dropna(subset=[lake.COL_OPAD, lake.COL_TEMPERATURA]).sort_values(lake.COL_DATA)
    if df_meteo.empty:
        return []
    tail = df_meteo.tail(n * 12)
    return [
        (float(row[lake.COL_OPAD]), float(row[lake.COL_TEMPERATURA]))
        for _, row in tail.iterrows()
    ]


def _project_recovery(
    lake_id: str,
    rows: list,
    df: pd.DataFrame,
    model,
    feature_cols: list,
    lag_months: int,
    meteo_lag_months: int,
    avg_meteo: dict[int, tuple[float, float]],
    recovery_cm_per_year: float = RECOVERY_RATE_FIXED_CM_PER_YEAR,
    meteo_sequence: list[tuple[float, float]] | None = None,
) -> tuple[list[str], list[float], list[float], list[str], list[float], list[float], bool, str | None]:
    if not rows or lag_months <= 0:
        return [], [], [], [], [], [], False, None
    recovery_m_per_month = (recovery_cm_per_year / 100.0) / 12.0
    last_d = rows[-1]["data"]
    year, month = int(last_d[:4]), int(last_d[5:7])
    level_model = float(rows[-1]["wysokosc_model"])
    level_actual_start = float(rows[-1]["wysokosc_rzeczywista"])
    last_5y = rows[-AVG_METEO_YEARS * 12 :]
    if len(last_5y) >= 2:
        x_t = np.array([_decimal_year(r["data"]) for r in last_5y], dtype=float)
        y_actual = np.array([float(r["wysokosc_rzeczywista"]) for r in last_5y], dtype=float)
        slope_actual_m_per_year = float(np.polyfit(x_t, y_actual, 1)[0])
    else:
        slope_actual_m_per_year = 0.0
    t_last = _decimal_year(last_d)
    gap_remaining = 0.0
    recovery_started = False
    had_positive_gap = False
    last_changes = [r["zmiana_prognoza"] for r in rows[-lag_months:]]
    last_poziomy = [float(rows[-1 - k]["wysokosc_model"]) for k in range(1, lag_months + 1) if len(rows) > k]
    while len(last_poziomy) < lag_months:
        last_poziomy.insert(0, level_model)
    last_opady = [r["opad"] for r in rows[-meteo_lag_months:]] if meteo_lag_months else []
    last_temperatury = [r["temperatura"] for r in rows[-meteo_lag_months:]] if meteo_lag_months else []
    max_poziom, odplyw_m, przesaczanie_m = lake.get_drainage_params(lake_id, df)
    hist_len = min(PROJEKCJA_METEO_YEARS * 12, len(rows))
    dates_hist = [r["data"] for r in rows[-hist_len:]]
    model_hist = [float(r["wysokosc_model"]) for r in rows[-hist_len:]]
    actual_hist = [float(r["wysokosc_rzeczywista"]) for r in rows[-hist_len:]]
    dates_proj, model_proj, actual_proj = [], [], []
    proj_month_idx = 0
    while year < PROJECTION_MAX_YEAR:
        month = month + 1
        if month > 12:
            month, year = 1, year + 1
        if year >= PROJECTION_MAX_YEAR:
            break
        if meteo_sequence and len(meteo_sequence) > 0:
            opad, temp = meteo_sequence[proj_month_idx % len(meteo_sequence)]
        else:
            opad, temp = avg_meteo.get(month, (float(np.mean([r["opad"] for r in rows[-60:]])), float(np.mean([r["temperatura"] for r in rows[-60:]]))))
        proj_month_idx += 1
        pred = lake.predict_change(
            model,
            feature_cols,
            level_model,
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
        level_model = level_model + pred
        level_model = lake.apply_cap_and_drainage(level_model, max_poziom, odplyw_m, przesaczanie_m)
        t_proj = year + (month - 0.5) / 12.0
        level_actual_trend = level_actual_start + slope_actual_m_per_year * (t_proj - t_last)
        if year < RECOVERY_START_YEAR or (year == RECOVERY_START_YEAR and month < RECOVERY_START_MONTH):
            level_actual = level_actual_trend
        else:
            if not recovery_started:
                recovery_started = True
                gap_remaining = max(0.0, level_model - level_actual_trend)
                had_positive_gap = gap_remaining > 0
            if gap_remaining > 0:
                gap_remaining = max(0.0, gap_remaining - recovery_m_per_month)
                level_actual = level_model - gap_remaining
            else:
                level_actual = level_actual_trend
        dates_proj.append(f"{year}-{month:02d}")
        model_proj.append(level_model)
        actual_proj.append(level_actual)
        last_changes = last_changes[1:] + [pred]
        last_poziomy = last_poziomy[1:] + [level_model]
        if meteo_lag_months:
            last_opady = (last_opady[1:] + [opad])[-meteo_lag_months:]
            last_temperatury = (last_temperatury[1:] + [temp])[-meteo_lag_months:]
        if recovery_started and had_positive_gap and level_actual >= level_model - 1e-6:
            convergence_ym = dates_proj[-1] if dates_proj else None
            return dates_hist, model_hist, actual_hist, dates_proj, model_proj, actual_proj, had_positive_gap, convergence_ym
    return dates_hist, model_hist, actual_hist, dates_proj, model_proj, actual_proj, had_positive_gap, None


def _plot_recovery(
    lake_name: str,
    dates_hist: list[str],
    model_hist: list[float],
    actual_hist: list[float],
    dates_proj: list[str],
    model_proj: list[float],
    actual_proj: list[float],
    out_path: Path,
    model_hist_nat: list[float] | None = None,
    dates_proj_nat: list[str] | None = None,
    model_proj_nat: list[float] | None = None,
    actual_proj_nat: list[float] | None = None,
    had_positive_gap_drain: bool = True,
    had_positive_gap_nat: bool = True,
    odbudowa_tylko_natural: bool = False,
):
    fig, ax = plt.subplots(figsize=(12, 5))
    tylko_natural = odbudowa_tylko_natural and model_hist_nat is not None and dates_proj_nat and model_proj_nat is not None and actual_proj_nat is not None
    if dates_hist:
        d_hist = [np.datetime64(d + "-01") for d in dates_hist]
        ax.plot(d_hist, actual_hist, label="Poziom rzeczywisty (historia)", color="#1f77b4", linewidth=1.2)
        if not tylko_natural:
            ax.plot(d_hist, model_hist, label="Scenariusz model drenażowy (historia)", color="#ff7f0e", linewidth=1.2, linestyle="--")
        if model_hist_nat is not None and len(model_hist_nat) == len(dates_hist):
            ax.plot(d_hist, model_hist_nat, label="Scenariusz model naturalny (historia)", color="#9467bd", linewidth=1.2, linestyle=":")
    if not tylko_natural and dates_proj:
        d_proj = [np.datetime64(d + "-01") for d in dates_proj]
        ax.plot(d_proj, model_proj, label="Model drenażowy – projekcja", color="#d62728", linewidth=1.2, linestyle="--")
        label_drain = "Odbudowa do modelu drenażowego" if had_positive_gap_drain else "Rzeczywisty – projekcja trendu (powyżej scenariusza drenażowego)"
        ax.plot(d_proj, actual_proj, label=label_drain, color="#2ca02c", linewidth=1.5, linestyle="-" if had_positive_gap_drain else ":")
    if dates_proj_nat and model_proj_nat is not None and actual_proj_nat is not None:
        d_proj_nat = [np.datetime64(d + "-01") for d in dates_proj_nat]
        ax.plot(d_proj_nat, model_proj_nat, label="Model naturalny – projekcja", color="#8c564b", linewidth=1.2, linestyle=":")
        label_nat = "Odbudowa do modelu naturalnego" if had_positive_gap_nat else "Rzeczywisty – projekcja trendu (powyżej scenariusza naturalnego)"
        ax.plot(d_proj_nat, actual_proj_nat, label=label_nat, color="#e377c2", linewidth=1.5, linestyle="-" if had_positive_gap_nat else ":")
    ax.set_xlabel("Data")
    ax.set_ylabel("Wysokość (m)")
    title = f"{lake_name} – odbudowa do scenariusza naturalnego (meteo 15 lat, wznios wód gruntowych)" if tylko_natural else f"{lake_name} – odbudowa: porównanie scenariusza drenażowego i naturalnego (do zrównania z modelem)"
    ax.set_title(title)
    ax.legend(loc="best")
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close()


def _result_from_rows(lake_id: str, rows: list) -> dict | None:
    if not rows:
        return None
    dates = [r["data"] for r in rows]
    divergences_m = [r["rozbieznosc"] for r in rows]
    trend_cm = _trend_cm_per_year(dates, divergences_m)
    mean_last_m = _mean_last_n_months(rows, 12)
    if mean_last_m is None:
        return None
    result = {
        "lake_id": lake_id,
        "lake_name": lake.LAKES.get(lake_id, lake_id),
        "n_months": len(rows),
        "mean_divergence_last_12m_m": mean_last_m,
        "trend_cm_per_year": trend_cm,
    }
    if trend_cm is not None and trend_cm < -0.01:
        gap_m = abs(mean_last_m)
        years_symmetric = (gap_m * 100.0) / abs(trend_cm) if trend_cm != 0 else None
        years_fixed_rate = (gap_m * 100.0) / RECOVERY_RATE_FIXED_CM_PER_YEAR
        result["recovery_years_symmetric"] = round(years_symmetric, 1) if years_symmetric is not None else None
        result["recovery_years_at_5cm"] = round(years_fixed_rate, 1)
    else:
        result["recovery_years_symmetric"] = None
        result["recovery_years_at_5cm"] = round((abs(mean_last_m) * 100.0) / RECOVERY_RATE_FIXED_CM_PER_YEAR, 1) if mean_last_m < 0 else None
    return result


def _get_lake_result_and_data(lake_id: str):
    if not lake.get_model_path(lake_id).exists():
        return None, None, None, None, None, None, None, None, None, None, None, None
    tmp_dir = DOCS_DIR / ".eval_tmp"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    out = tmp_dir / f"{lake_id}_eval.md"
    _, _, rows, _ = run_evaluation(
        lake_id=lake_id,
        output_path=out,
    )
    if not rows:
        return None, None, None, None, None, None, None, None, None, None, None, None
    result = _result_from_rows(lake_id, rows)
    if result is None:
        return None, None, None, None, None, None, None, None, None, None, None, None
    model, feature_cols, lag_months, meteo_lag_months = lake.load_model(lake.get_model_path(lake_id))
    df = lake.load_data(lake.get_data_path(lake_id))
    natural_path = lake.get_model_path(lake_id, "natural")
    rows_nat, model_nat, feature_cols_nat, lag_months_nat, meteo_lag_months_nat = None, None, None, None, None
    if natural_path.exists():
        out_nat = tmp_dir / f"{lake_id}_eval_nat.md"
        _, _, rows_nat, _ = run_evaluation(
            lake_id=lake_id,
            model_path=natural_path,
            output_path=out_nat,
        )
        if rows_nat:
            model_nat, feature_cols_nat, lag_months_nat, meteo_lag_months_nat = lake.load_model(natural_path)
    return result, rows, model, feature_cols, lag_months, meteo_lag_months, df, rows_nat, model_nat, feature_cols_nat, lag_months_nat, meteo_lag_months_nat


def build_report(results: list[dict], wznios_by_lake: dict[str, dict]) -> str:
    lines = [
        "# Szacunek lat odbudowy poziomu po zaniku dodatkowego źródła drenażu",
        "",
        "## Założenia (uproszczone)",
        "",
        "- **Rozbieżność** = wysokość rzeczywista − wysokość w scenariuszu modelowym (klimat, sezon, lagi). Ujemna = jezioro poniżej scenariusza.",
        "- Przy **zaniku dodatkowego drenażu** zakładamy, że poziom rzeczywisty dąży do scenariusza modelowego; szacujemy **ile lat** potrzeba na „zamknięcie” obecnej luki.",
        "- **Scenariusz A (symmetric):** odbudowa z prędkością równą obserwowanemu tempu narastania rozjazdu (trend liniowy rozbieżności w czasie).",
        f"- **Scenariusz B (stałe tempo):** odbudowa z prędkością **{RECOVERY_RATE_FIXED_CM_PER_YEAR} cm/rok**.",
        "- Wartości oparte na średniej rozbieżności z **ostatnich 12 miesięcy** i trendzie z pełnego szeregu ewaluacji. **Szacunek teoretyczny**, bez modelowania hydrologicznego odbudowy.",
        f"- **Projekcja odbudowy:** scenariusz modelowy przy **meteo z ostatnich {PROJEKCJA_METEO_YEARS} lat** (sekwencja miesięczna, bez harmonijki). Do {RECOVERY_START_MONTH}/{RECOVERY_START_YEAR} poziom rzeczywisty – **trend z ostatnich 5 lat**; od {RECOVERY_START_MONTH}/{RECOVERY_START_YEAR} **wznios wód gruntowych** (cm/rok z CSV lub 5 cm/rok). Wykres: tylko odbudowa do scenariusza naturalnego (bez scenariusza drenażowego).",
        "",
        "---",
        "",
        "## Wznios poziomu wód gruntowych – porównanie",
        "",
        "Dwa wzniosy dla porównania (źródło: `data/zanik_drenazu.csv`): wznios bazowy oraz wznios po zalaniu kopalni.",
        "",
        "| Jezioro | Wznios (cm/rok) | Wznios po zalaniu kopalni (cm/rok) |",
        "|---------|-----------------|-------------------------------------|",
    ]
    for r in results:
        name = r["lake_name"]
        short = name.replace("Jezioro ", "").strip()
        wznios = wznios_by_lake.get(short, {})
        w1 = wznios.get("wznios_cm_rok")
        w2 = wznios.get("wznios_po_zalaniu_cm_rok")
        w1_s = f"{w1:.1f}" if w1 is not None else "—"
        w2_s = f"{w2:.1f}" if w2 is not None else "—"
        lines.append(f"| {name} | {w1_s} | {w2_s} |")
    lines.extend([
        "",
        "---",
        "",
        "## Wyniki per jezioro",
        "",
    ])
    for r in results:
        name = r["lake_name"]
        lid = r["lake_id"]
        mean_m = r["mean_divergence_last_12m_m"]
        trend = r.get("trend_cm_per_year")
        ys_sym = r.get("recovery_years_symmetric")
        ys_5 = r.get("recovery_years_at_5cm")
        lines.append(f"### {name}")
        lines.append("")
        lines.append(f"- **Średnia rozbieżność (ostatnie 12 miesięcy):** {mean_m * 100:.1f} cm")
        lines.append(f"- **Trend rozbieżności:** {trend:.2f} cm/rok" if trend is not None else "- **Trend rozbieżności:** —")
        lines.append(f"- **Szacunek odbudowy (scenariusz A, symmetric):** {ys_sym} lat" if ys_sym is not None else "- **Szacunek odbudowy (scenariusz A):** —")
        lines.append(f"- **Szacunek odbudowy (scenariusz B, {RECOVERY_RATE_FIXED_CM_PER_YEAR} cm/rok):** {ys_5} lat" if ys_5 is not None else "- **Szacunek odbudowy (scenariusz B):** —")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Wykresy projekcji odbudowy")
    lines.append("")
    lines.append(f"Dla każdego jeziora: **odbudowa do scenariusza naturalnego** (meteo z ostatnich {PROJEKCJA_METEO_YEARS} lat, wznios wód gruntowych). Wykres bez scenariusza drenażowego – kontekst to odbudowa po zaniku drenażu.")
    lines.append("")
    for r in results:
        lines.append(f"### {r['lake_name']}")
        lines.append("")
        lines.append(f"![Odbudowa {r['lake_id']}](odbudowa/odbudowa_{r['lake_id']}.png)")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Uwagi")
    lines.append("")
    lines.append("- Analiza **całkowicie osobna** od wnioskowania o istnieniu czynnika drenującego; służy tylko do zgrubnego szacunku czasu odbudowy.")
    lines.append("- Rzeczywista odbudowa zależy od zatrzymania drenażu, warunków klimatycznych i bilansu wód podziemnych; powyższe wartości mają charakter orientacyjny.")
    return "\n".join(lines)


def _build_single_lake_report(r: dict, wznios_row: dict | None = None) -> str:
    name = r["lake_name"]
    lid = r["lake_id"]
    mean_m = r["mean_divergence_last_12m_m"]
    trend = r.get("trend_cm_per_year")
    ys_sym = r.get("recovery_years_symmetric")
    ys_5 = r.get("recovery_years_at_5cm")
    lines = [
        f"# Zanik drenażu — {name}",
        "",
        "- **Rozbieżność** = wysokość rzeczywista − wysokość w scenariuszu modelowym. Ujemna = jezioro poniżej scenariusza.",
        "- Przy zaniku dodatkowego drenażu szacuje się lata do zamknięcia luki (szacunek teoretyczny).",
        f"- Projekcja: wznios wód gruntowych (cm/rok), start odbudowy od {RECOVERY_START_MONTH}/{RECOVERY_START_YEAR}. Wykres do uzyskania stanu (zrównania z modelem), maks. do {PROJECTION_MAX_YEAR}.",
        "",
    ]
    if wznios_row:
        w1 = wznios_row.get("wznios_cm_rok")
        w2 = wznios_row.get("wznios_po_zalaniu_cm_rok")
        lines.extend([
            "## Wznios poziomu wód gruntowych (porównanie)",
            "",
            f"- **Wznios (cm/rok):** {w1:.1f}" if w1 is not None else "- **Wznios (cm/rok):** —",
            f"- **Wznios po zalaniu kopalni (cm/rok):** {w2:.1f}" if w2 is not None else "- **Wznios po zalaniu kopalni (cm/rok):** —",
            "",
        ])
    lines.extend([
        "## Wyniki",
        "",
        f"- **Średnia rozbieżność (ostatnie 12 miesięcy):** {mean_m * 100:.1f} cm",
        f"- **Trend rozbieżności:** {trend:.2f} cm/rok" if trend is not None else "- **Trend rozbieżności:** —",
        f"- **Szacunek odbudowy (scenariusz A, symmetric):** {ys_sym} lat" if ys_sym is not None else "- **Szacunek odbudowy (scenariusz A):** —",
        f"- **Szacunek odbudowy (scenariusz B, {RECOVERY_RATE_FIXED_CM_PER_YEAR} cm/rok):** {ys_5} lat" if ys_5 is not None else "- **Szacunek odbudowy (scenariusz B):** —",
        "",
    ])
    conv_ym = r.get("convergence_ym")
    wznios_cm = r.get("wznios_cm_rok")
    if conv_ym and wznios_cm is not None:
        try:
            y, m = int(conv_ym[:4]), int(conv_ym[5:7])
            mies = MIESIACE_NAZWA[m - 1] if 1 <= m <= 12 else conv_ym
            lines.append(f"- **Odbudowa (zrównanie z modelem naturalnym)** nastąpi w **{mies} {y}** przy wzniosie wód gruntowych **{wznios_cm:.1f} cm/rok** i meteo z ostatnich {PROJEKCJA_METEO_YEARS} lat.")
        except (ValueError, IndexError):
            lines.append(f"- **Odbudowa (zrównanie z modelem naturalnym)** nastąpi w **{conv_ym}** przy wzniosie wód gruntowych **{wznios_cm:.1f} cm/rok** i meteo z ostatnich {PROJEKCJA_METEO_YEARS} lat.")
    elif conv_ym:
        lines.append(f"- **Odbudowa (zrównanie z modelem naturalnym)** nastąpi w **{conv_ym}** przy meteo z ostatnich {PROJEKCJA_METEO_YEARS} lat.")
    else:
        wznios_txt = f"{wznios_cm:.1f} cm/rok" if wznios_cm is not None else "5 cm/rok"
        lines.append(f"- Do roku {PROJECTION_MAX_YEAR} zrównanie z modelem naturalnym **nie następuje** przy wzniosie {wznios_txt} i meteo z ostatnich {PROJEKCJA_METEO_YEARS} lat.")
    lines.extend([
        "",
        f"## Wykres projekcji odbudowy",
        "",
        f"Na wykresie: poziom rzeczywisty (historia), scenariusz naturalny (historia + projekcja) oraz odbudowa do scenariusza naturalnego (meteo {PROJEKCJA_METEO_YEARS} lat, wznios wód gruntowych). Bez scenariusza drenażowego – kontekst to odbudowa po zaniku drenażu. Gdy poziom rzeczywisty jest powyżej scenariusza, rysowana jest projekcja trendu (brak luki).",
        "",
        f"![Odbudowa – porównanie drenaż / naturalny](../odbudowa/odbudowa_{lid}.png)",
    ])
    return "\n".join(lines)


def main():
    wznios_by_lake = _load_wznios_by_lake()
    results = []
    for lake_id in lake.LAKES:
        result, rows, model, feature_cols, lag_months, meteo_lag_months, df, rows_nat, model_nat, feature_cols_nat, lag_months_nat, meteo_lag_months_nat = _get_lake_result_and_data(lake_id)
        if result is None:
            continue
        results.append(result)
        avg_meteo = _avg_meteo_last_n_years(df, AVG_METEO_YEARS)
        meteo_seq_15 = _meteo_sequence_last_n_years(df, PROJEKCJA_METEO_YEARS)
        short = result["lake_name"].replace("Jezioro ", "").strip()
        wznios_row = wznios_by_lake.get(short)
        recovery_cm = float(wznios_row["wznios_cm_rok"]) if wznios_row and wznios_row.get("wznios_cm_rok") is not None else RECOVERY_RATE_FIXED_CM_PER_YEAR
        dates_hist, model_hist, actual_hist, dates_proj, model_proj, actual_proj, had_gap_drain, _ = _project_recovery(
            lake_id=lake_id,
            rows=rows,
            df=df,
            model=model,
            feature_cols=feature_cols,
            lag_months=lag_months,
            meteo_lag_months=meteo_lag_months,
            avg_meteo=avg_meteo,
            recovery_cm_per_year=recovery_cm,
            meteo_sequence=meteo_seq_15 if meteo_seq_15 else None,
        )
        model_hist_nat = None
        dates_proj_nat, model_proj_nat, actual_proj_nat = None, None, None
        had_gap_nat = True
        convergence_ym = None
        hist_len = min(PROJEKCJA_METEO_YEARS * 12, len(rows))
        if rows_nat is not None and model_nat is not None and len(rows_nat) >= hist_len:
            model_hist_nat = [float(r["wysokosc_model"]) for r in rows_nat[-hist_len:]]
            _, _, _, dates_proj_nat, model_proj_nat, actual_proj_nat, had_gap_nat, convergence_ym = _project_recovery(
                lake_id=lake_id,
                rows=rows_nat,
                df=df,
                model=model_nat,
                feature_cols=feature_cols_nat,
                lag_months=lag_months_nat,
                meteo_lag_months=meteo_lag_months_nat,
                avg_meteo=avg_meteo,
                recovery_cm_per_year=recovery_cm,
                meteo_sequence=meteo_seq_15 if meteo_seq_15 else None,
            )
            if len(model_hist_nat) != len(dates_hist):
                model_hist_nat = None
            if not dates_proj_nat:
                dates_proj_nat, model_proj_nat, actual_proj_nat = None, None, None
        result["convergence_ym"] = convergence_ym
        result["wznios_cm_rok"] = recovery_cm
        FIGURES_ODBUDOWA_DIR.mkdir(parents=True, exist_ok=True)
        _plot_recovery(
            lake_name=result["lake_name"],
            dates_hist=dates_hist,
            model_hist=model_hist,
            actual_hist=actual_hist,
            dates_proj=dates_proj,
            model_proj=model_proj,
            actual_proj=actual_proj,
            out_path=FIGURES_ODBUDOWA_DIR / f"odbudowa_{lake_id}.png",
            model_hist_nat=model_hist_nat,
            dates_proj_nat=dates_proj_nat,
            model_proj_nat=model_proj_nat,
            actual_proj_nat=actual_proj_nat,
            had_positive_gap_drain=had_gap_drain,
            had_positive_gap_nat=had_gap_nat,
            odbudowa_tylko_natural=(model_hist_nat is not None and dates_proj_nat is not None),
        )
        print(f"Wykres: {FIGURES_ODBUDOWA_DIR / f'odbudowa_{lake_id}.png'}")
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    content = build_report(results, wznios_by_lake)
    OUTPUT_PATH.write_text(content, encoding="utf-8")
    print(f"Raport zapisany: {OUTPUT_PATH}")
    for r in results:
        short = r["lake_name"].replace("Jezioro ", "").strip()
        wznios_row = wznios_by_lake.get(short)
        path = DOCS_DIR / r["lake_id"] / "zanik_drenazu.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(_build_single_lake_report(r, wznios_row), encoding="utf-8")
        print(f"Zapisano: {path}")


if __name__ == "__main__":
    main()
