from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
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
PROGNOZA_MIESIACE = [(2025, 12), (2026, 1), (2026, 2)]


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


def _load_meteo_z_txt() -> dict[tuple[int, int], tuple[float, float]]:
    opady = _parse_meteo_file(OPAD_PATH)
    tempy = _parse_meteo_file(TEMP_PATH)
    return {k: (opady[k], tempy[k]) for k in opady if k in tempy}


def _prognoza_grudzien_styczen_luty() -> list[dict] | None:
    if not OPAD_PATH.exists() or not TEMP_PATH.exists():
        return None
    meteo = _load_meteo_z_txt()
    df = lake.load_data(lake.get_data_path(LAKE_ID))
    if df.empty:
        return None
    model_path = lake.get_model_path(LAKE_ID)
    if not model_path.exists():
        return None
    model, feature_cols, lag_months, meteo_lag_months = lake.load_model(model_path)
    df["_ym"] = df[lake.COL_DATA].dt.year.astype(str) + "-" + df[lake.COL_DATA].dt.month.astype(str).str.zfill(2)
    hist = df[df["_ym"] <= "2025-11"].copy()
    if hist.empty:
        return None
    last_row = hist.iloc[-1]
    level = float(last_row[lake.COL_POZIOM])
    hist_tail = hist.tail(lag_months)
    last_changes = [float(hist_tail.iloc[i][lake.COL_ZMIANA]) for i in range(len(hist_tail))]
    last_poziomy = [float(hist_tail.iloc[i][lake.COL_POZIOM]) for i in range(len(hist_tail))]
    while len(last_changes) < lag_months:
        last_changes.insert(0, 0.0)
        last_poziomy.insert(0, level)
    meteo_tail = hist.tail(meteo_lag_months) if meteo_lag_months else []
    last_opady = [float(meteo_tail.iloc[i][lake.COL_OPAD]) for i in range(len(meteo_tail))] if meteo_lag_months else []
    last_temperatury = [float(meteo_tail.iloc[i][lake.COL_TEMPERATURA]) for i in range(len(meteo_tail))] if meteo_lag_months else []
    max_poziom, odplyw_m, przesaczanie_m = lake.get_drainage_params(LAKE_ID, df)
    results = []
    for year, month in PROGNOZA_MIESIACE:
        key = (year, month)
        if key not in meteo:
            break
        opad, temp = meteo[key]
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
    return results if results else None


def _plot_poziom_rzeczywisty_i_model(
    df: pd.DataFrame,
    eval_rows: list | None,
    out_path: Path,
    prognoza: list[dict] | None = None,
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
    if prognoza:
        last_date = pd.to_datetime(df[lake.COL_DATA].iloc[-1])
        last_level = float(df[lake.COL_POZIOM].iloc[-1])
        dates_prog = [last_date] + [pd.to_datetime(r["data"] + "-01") for r in prognoza]
        levels_prog = [last_level] + [float(r["poziom"]) for r in prognoza]
        ax.plot(dates_prog, levels_prog, color="#2ca02c", linewidth=1.5, marker="o", markersize=5, label="Prognoza (grudzień–luty)")
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


def _write_report(fig_filename: str, prognoza: list[dict] | None = None) -> str:
    lines = [
        "# Raport: Jezioro Niedzięgiel",
        "",
        "Raport dedykowany tylko dla Jeziora Niedzięgiel.",
        "",
        "## Poziom wody: rzeczywisty pomiar i model",
        "",
        "Niebieska linia: poziom z pliku `data/niedziegiel/data.csv` (pomiar na pierwszy dzień miesiąca). Przerywana pomarańczowa: wahania poziomu według modelu (scenariusz kumulatywny z prognozy zmiany miesięcznej). Zielona linia z punktami: prognoza poziomu na grudzień, styczeń i luty od ostatniego pomiaru (dane z plików opad/temp).",
        "",
        f"![Poziom wody – pomiar i model]({fig_filename})",
        "",
    ]
    if prognoza:
        lines.extend([
            "## Prognoza poziomu (grudzień, styczeń, luty)",
            "",
            "Wyliczenie od ostatniego rzeczywistego pomiaru (listopad 2025) z użyciem modelu bazowego Niedzięgiel i danych pogodowych z plików `data/niedziegiel/opad.txt` i `data/niedziegiel/temp.txt`.",
            "",
            "| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |",
            "|------|-----------|------------------|----------------------|-------------------|",
        ])
        for r in prognoza:
            lines.append(f"| {r['data']} | {r['opad']} | {r['temperatura']} | {r['zmiana_prognoza']} | {r['poziom']} |")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    df = lake.load_data(lake.get_data_path(LAKE_ID))
    eval_rows = None
    if lake.get_model_path(LAKE_ID).exists():
        _, _, eval_rows = run_evaluation(lake_id=LAKE_ID)
    prognoza = _prognoza_grudzien_styczen_luty()
    fig_path = FIGURES_DIR / "poziom_rzeczywisty.png"
    _plot_poziom_rzeczywisty_i_model(df, eval_rows, fig_path, prognoza=prognoza)
    print(f"Wykres zapisany: {fig_path}")
    content = _write_report("poziom_rzeczywisty.png", prognoza=prognoza)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(content, encoding="utf-8")
    print(f"Raport zapisany: {REPORT_PATH}")


if __name__ == "__main__":
    main()
