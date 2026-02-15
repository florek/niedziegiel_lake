from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

import lake

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
LAKE_ID = "niedziegiel_zaklocony"
OPAD_PATH = DATA_DIR / "niedziegiel" / "opad.txt"
TEMP_PATH = DATA_DIR / "niedziegiel" / "temp.txt"
REPORT_PATH = DOCS_DIR / "niedziegiel" / "symulacja_rezim_zaklocony.md"
FIGURE_PATH = DOCS_DIR / "niedziegiel" / "symulacja_rezim_zaklocony.png"
DODATKOWY_ODCIAG_M_NA_MIESIAC = 0.015

MONTH_NAMES = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12,
}


def _parse_meteo_file(path: Path) -> list[tuple[int, int, float]]:
    lines = path.read_text(encoding="utf-8").strip().splitlines()
    out = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) < 3:
            continue
        month_name, year_s, value_s = parts[0], parts[1], parts[2]
        month = MONTH_NAMES.get(month_name)
        if month is None:
            continue
        try:
            year = int(year_s)
            value = float(value_s.replace(",", "."))
        except ValueError:
            continue
        out.append((year, month, value))
    return out


def load_scenario(opad_path: Path, temp_path: Path) -> list[dict]:
    opad_rows = _parse_meteo_file(opad_path)
    temp_rows = _parse_meteo_file(temp_path)
    if len(opad_rows) != len(temp_rows):
        raise ValueError("Różna liczba wierszy w plikach opad i temperatura.")
    scenario = []
    for (yr, mo, opad), (yr2, mo2, temp) in zip(opad_rows, temp_rows):
        if (yr, mo) != (yr2, mo2):
            raise ValueError(f"Niezgodność dat: opad {yr}-{mo}, temp {yr2}-{mo2}")
        scenario.append({"year": yr, "month": mo, "opad": opad, "temperatura": temp})
    return scenario


def _override_with_observed_meteo(scenario: list[dict], df: pd.DataFrame) -> None:
    df["_ym"] = df[lake.COL_DATA].dt.year.astype(str) + "-" + df[lake.COL_DATA].dt.month.astype(str).str.zfill(2)
    lookup = df.set_index("_ym")
    for row in scenario:
        ym = f"{row['year']}-{row['month']:02d}"
        if ym in lookup.index:
            r = lookup.loc[ym]
            row["opad"] = float(r[lake.COL_OPAD])
            row["temperatura"] = float(r[lake.COL_TEMPERATURA])
            row["_meteo_zrodlo"] = "CSV"
        else:
            row["_meteo_zrodlo"] = "txt"


def _get_initial_state_from_observed(scenario_start_ym: str):
    df = lake.load_data(lake.get_data_path(LAKE_ID))
    df["_ym"] = df[lake.COL_DATA].dt.year.astype(str) + "-" + df[lake.COL_DATA].dt.month.astype(str).str.zfill(2)
    hist = df[df["_ym"] < scenario_start_ym].copy()
    if hist.empty:
        return None, None, None, None, None, None, None, None, None, None
    model, feature_cols, lag_months, meteo_lag_months = lake.load_model(lake.get_model_path(LAKE_ID))
    last_row = hist.iloc[-1]
    level = float(last_row[lake.COL_POZIOM]) + float(last_row[lake.COL_ZMIANA])
    hist_tail = hist.tail(lag_months)
    last_changes = [float(hist_tail.iloc[i][lake.COL_ZMIANA]) for i in range(len(hist_tail))]
    last_poziomy = [
        float(hist_tail.iloc[i][lake.COL_POZIOM]) + float(hist_tail.iloc[i][lake.COL_ZMIANA])
        for i in range(len(hist_tail))
    ]
    while len(last_changes) < lag_months:
        last_changes.insert(0, 0.0)
        last_poziomy.insert(0, level)
    meteo_tail = hist.tail(meteo_lag_months) if meteo_lag_months else []
    last_opady = [float(meteo_tail.iloc[i][lake.COL_OPAD]) for i in range(len(meteo_tail))] if meteo_lag_months else []
    last_temperatury = [float(meteo_tail.iloc[i][lake.COL_TEMPERATURA]) for i in range(len(meteo_tail))] if meteo_lag_months else []
    return (
        model,
        feature_cols,
        lag_months,
        meteo_lag_months,
        level,
        last_changes,
        last_poziomy,
        last_opady,
        last_temperatury,
        df,
    )


def run_simulation(
    lake_id: str,
    scenario: list[dict],
    model,
    feature_cols: list,
    lag_months: int,
    meteo_lag_months: int,
    level_start: float,
    last_changes: list,
    last_poziomy: list,
    last_opady: list,
    last_temperatury: list,
    df: pd.DataFrame,
) -> list[dict]:
    max_poziom, odplyw_m, przesaczanie_m = lake.get_drainage_params(lake_id, df)
    level = level_start
    results = []
    for row in scenario:
        pred = lake.predict_change(
            model,
            feature_cols,
            level,
            row["opad"],
            row["temperatura"],
            row["month"],
            last_changes=last_changes,
            last_poziomy=last_poziomy,
            last_opady=last_opady if last_opady else None,
            last_temperatury=last_temperatury if last_temperatury else None,
            lag_months=lag_months,
            meteo_lag_months=meteo_lag_months,
        )
        level = level + pred
        level = lake.apply_cap_and_drainage(level, max_poziom, odplyw_m, przesaczanie_m)
        level = level - DODATKOWY_ODCIAG_M_NA_MIESIAC
        data_ym = f"{row['year']}-{row['month']:02d}"
        results.append({
            "data": data_ym,
            "opad": row["opad"],
            "temperatura": row["temperatura"],
            "zmiana_prognoza": round(pred, 4),
            "wysokosc_symulowana": round(level, 3),
        })
        last_changes = last_changes[1:] + [pred]
        last_poziomy = last_poziomy[1:] + [level]
        if meteo_lag_months:
            last_opady = (last_opady[1:] + [row["opad"]])[-meteo_lag_months:]
            last_temperatury = (last_temperatury[1:] + [row["temperatura"]])[-meteo_lag_months:]
    return results


def _write_report(results: list[dict], scenario_start: str, scenario_end: str, dodatkowy_odciag: float = 0.0) -> str:
    lines = [
        "# Symulacja poziomu Jeziora Niedzięgiel przy zakłóconym reżimie opadu i temperatury",
        "",
        "## Źródło scenariusza",
        "",
        f"- **Opad:** `data/niedziegiel/opad.txt`",
        f"- **Temperatura:** `data/niedziegiel/temp.txt`",
        f"- **Okres:** {scenario_start} – {scenario_end}",
        "",
        "## Metoda",
        "",
        "Stan początkowy: **rzeczywisty poziom wody** z pomiarów (koniec ostatniego miesiąca przed scenariuszem) oraz ostatnie zmiany/poziomy/opady/temperatury z danych obserwowanych. Dla miesięcy, na które są dane w `data/niedziegiel/data.csv`, używany jest **opad i temperatura z CSV** (pomiary); dla pozostałych miesięcy – wartości z plików txt.",
        "",
    ]
    if dodatkowy_odciag > 0:
        lines.extend([
            f"- **Dodatkowy odciąg (wartość „ciągnąca wodę”):** {dodatkowy_odciag * 100:.1f} cm/mies. – odejmowany co miesiąc od poziomu, aby odzwierciedlić silniejszy w rzeczywistości drenaż/odpływ niż ten ujęty w modelu.",
            "",
        ])
    lines.extend([
        "## Wyniki symulacji",
        "",
        "| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Wysokość symulowana (m) |",
        "|------|-----------|------------------|----------------------|--------------------------|",
    ])
    for r in results:
        zm_cm = r["zmiana_prognoza"] * 100
        lines.append(
            f"| {r['data']} | {r['opad']} | {r['temperatura']} | {zm_cm:+.1f} | {r['wysokosc_symulowana']} |"
        )
    lines.extend([
        "",
        "## Wykres",
        "",
        "![Symulacja przy zakłóconym reżimie](symulacja_rezim_zaklocony.png)",
        "",
        "## Rozbieżność z rzeczywistością / odciąg",
        "",
        "**W listopadzie 2025 rzeczywisty poziom wody wynosił ok. 101,8 m.** Model może być **zbyt optymistyczny** – nie ujmuje w pełni wartości „ciągnącej wodę” (dodatkowy drenaż, odpływ podziemny itd.), która w rzeczywistości jest większa. W skrypcie można ustawić stały **dodatkowy odciąg** (zmienna `DODATKOWY_ODCIAG_M_NA_MIESIAC`, w m/mies.) – odejmowany co miesiąc od poziomu; przy ok. 1,5 cm/mies. symulacja zbliża się do obserwowanego 101,8 m w XI 2025.",
        "",
        "## Uwagi",
        "",
        "Symulacja ma charakter teoretyczny. Poziom początkowy to rzeczywisty pomiar (koniec lipca 2023); skala wysokości (ok. 102–103 m) odpowiada Jezioru Niedzięgiel.",
        "",
    ])
    return "\n".join(lines)


def _plot_results(results: list[dict], out_path: Path) -> None:
    if not results:
        return
    dates = [r["data"] + "-01" for r in results]
    levels = [r["wysokosc_symulowana"] for r in results]
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(
        pd.to_datetime(dates),
        levels,
        color="#1f77b4",
        linewidth=1.2,
        label="Wysokość symulowana",
    )
    ax.set_xlabel("Data")
    ax.set_ylabel("Wysokość (m)")
    ax.set_title("Jezioro Niedzięgiel – symulacja przy zakłóconym reżimie (opad i temperatura ze scenariusza)")
    ax.xaxis.set_major_locator(mdates.YearLocator(1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150)
    plt.close()


def main() -> None:
    if not OPAD_PATH.exists() or not TEMP_PATH.exists():
        raise FileNotFoundError("Brak plików opad.txt lub temp.txt w data/niedziegiel/")
    model_path = lake.get_model_path(LAKE_ID)
    if not model_path.exists():
        print("Brak modelu reżimu zakłóconego – trening (2018–2024)...")
        lake.run_training_and_save(LAKE_ID)
    scenario = load_scenario(OPAD_PATH, TEMP_PATH)
    if not scenario:
        raise ValueError("Scenariusz jest pusty.")
    df_csv = lake.load_data(lake.get_data_path(LAKE_ID))
    _override_with_observed_meteo(scenario, df_csv)
    scenario_start_ym = f"{scenario[0]['year']}-{scenario[0]['month']:02d}"
    scenario_end_ym = f"{scenario[-1]['year']}-{scenario[-1]['month']:02d}"
    init = _get_initial_state_from_observed(scenario_start_ym)
    if init[0] is None:
        raise ValueError(
            "Brak stanu początkowego (dane historyczne muszą się kończyć przed początkiem scenariusza)."
        )
    (
        model,
        feature_cols,
        lag_months,
        meteo_lag_months,
        level_start,
        last_changes,
        last_poziomy,
        last_opady,
        last_temperatury,
        df,
    ) = init
    results = run_simulation(
        lake_id=LAKE_ID,
        scenario=scenario,
        model=model,
        feature_cols=feature_cols,
        lag_months=lag_months,
        meteo_lag_months=meteo_lag_months,
        level_start=level_start,
        last_changes=last_changes,
        last_poziomy=last_poziomy,
        last_opady=last_opady,
        last_temperatury=last_temperatury,
        df=df,
    )
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    report_content = _write_report(
        results,
        scenario_start_ym,
        scenario_end_ym,
        dodatkowy_odciag=DODATKOWY_ODCIAG_M_NA_MIESIAC,
    )
    REPORT_PATH.write_text(report_content, encoding="utf-8")
    print(f"Raport zapisany: {REPORT_PATH}")
    _plot_results(results, FIGURE_PATH)
    print(f"Wykres zapisany: {FIGURE_PATH}")


if __name__ == "__main__":
    main()
