import sys
from datetime import datetime
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

import lake
from evaluate_predictions import run_evaluation

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"


def _figs_dir(lake_id):
    return DOCS_DIR / lake_id


def _report_path(lake_id):
    return DOCS_DIR / lake_id / "raport_podsumowujacy.md"


def _train_start_label(lake_id):
    y = lake.TRAIN_START_YEAR_BY_LAKE.get(lake_id)
    m = lake.TRAIN_START_MONTH_BY_LAKE.get(lake_id)
    if y is None:
        return None
    return f"{y}-{m:02d}" if m is not None else str(y)


def _train_end_label(lake_id):
    y = lake.TRAIN_END_YEAR_BY_LAKE.get(lake_id, 2013)
    m = lake.TRAIN_END_MONTH_BY_LAKE.get(lake_id)
    return f"{y}-{m:02d}" if m is not None else f"roku {y}"


def _test_start_label(lake_id):
    y = lake.TRAIN_END_YEAR_BY_LAKE.get(lake_id, 2013)
    m = lake.TRAIN_END_MONTH_BY_LAKE.get(lake_id)
    if m is not None and m < 12:
        return f"{y}-{m + 1:02d}"
    return str(y + 1)


def _year_range_from_rows(rows):
    if not rows:
        return None, None
    years = [int(r["data"][:4]) for r in rows]
    return min(years), max(years)


def _train_end_natural_label(lake_id):
    y = lake.TRAIN_END_NATURAL_YEAR_BY_LAKE.get(lake_id)
    if y is None:
        return None
    m = lake.TRAIN_END_NATURAL_MONTH_BY_LAKE.get(lake_id)
    return f"{y}-{m:02d}" if m is not None else f"roku {y}"


def _train_range_table_cell(lake_id, rows, rows_natural):
    min_yr, _ = _year_range_from_rows(rows)
    part = "**Po drenażu:** uczony od {} do {}.".format(
        _train_start_label(lake_id),
        _train_end_label(lake_id),
    )
    if rows_natural and _train_end_natural_label(lake_id):
        part += " **Sprzed drenażu:** uczony od {} do {}.".format(
            min_yr,
            _train_end_natural_label(lake_id),
        )
    return part


def _plot_wysokosci(rows, figs_dir, lake_name, lake_id, rows_natural=None):
    dates = [np.datetime64(r["data"] + "-01") for r in rows]
    rzeczywista = np.array([float(r["wysokosc_rzeczywista"]) for r in rows])
    model = np.array([float(r["wysokosc_model"]) for r in rows])
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(dates, rzeczywista, label="Wysokość rzeczywista", color="#1f77b4", linewidth=1.2)
    if rows_natural:
        dates_nat = [np.datetime64(r["data"] + "-01") for r in rows_natural]
        natural = np.array([float(r["wysokosc_model"]) for r in rows_natural])
        ax.plot(dates_nat, natural, label="Model naturalny (sprzed drenażu)", color="#2ca02c", linewidth=1.2, linestyle=":")
    ax.set_xlabel("Data")
    ax.set_ylabel("Wysokość (m)")
    ax.set_title(f"{lake_name} – wysokość wody: rzeczywista vs scenariusze modelowe")
    ax.legend(loc="best")
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(figs_dir / "wysokosc_rzeczywista_vs_model.png", dpi=150)
    plt.close()


def _align_natural_by_date(rows, rows_natural):
    if not rows_natural:
        return None
    nat_by_date = {r["data"]: r for r in rows_natural}
    return nat_by_date


def _plot_rozbieznosc(rows, figs_dir, rows_natural=None):
    nat_by_date = _align_natural_by_date(rows, rows_natural)
    if nat_by_date is not None:
        dates = []
        rozb = []
        for r in rows:
            nat = nat_by_date.get(r["data"])
            if nat is not None:
                dates.append(np.datetime64(r["data"] + "-01"))
                rozb.append((r["wysokosc_rzeczywista"] - nat["wysokosc_model"]) * 100)
        if dates and rozb:
            title = "Rozbieżność: wysokość rzeczywista − scenariusz modelu naturalnego (sprzed drenażu)"
        else:
            dates = [np.datetime64(r["data"] + "-01") for r in rows]
            rozb = [r["rozbieznosc"] * 100 for r in rows]
            title = "Rozbieżność: wysokość rzeczywista − scenariusz modelowy (drenażowy)"
    else:
        dates = [np.datetime64(r["data"] + "-01") for r in rows]
        rozb = [r["rozbieznosc"] * 100 for r in rows]
        title = "Rozbieżność: wysokość rzeczywista − scenariusz modelowy (drenażowy)"
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.fill_between(dates, 0, rozb, where=[x >= 0 for x in rozb], color="#1f77b4", alpha=0.35, label="Rzeczywistość > model")
    ax.fill_between(dates, 0, rozb, where=[x < 0 for x in rozb], color="#ff7f0e", alpha=0.35, label="Rzeczywistość < model")
    ax.plot(dates, rozb, color="#1a1a1a", linewidth=1.2, zorder=2)
    ax.axhline(y=0, color="gray", linewidth=1, linestyle="-", zorder=1)
    y_min, y_max = min(rozb), max(rozb)
    margin = max(10, (y_max - y_min) * 0.05) if y_max > y_min else 10
    ax.set_ylim(y_min - margin, y_max + margin)
    ax.set_xlabel("Data")
    ax.set_ylabel("Rozbieżność (cm)")
    ax.set_title(title)
    ax.legend(loc="best")
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(figs_dir / "rozbieznosc_w_czasie.png", dpi=150)
    plt.close()


def _plot_zmiana_fakt_vs_prognoza(rows, figs_dir):
    fakt = [r["zmiana_fakt"] * 100 for r in rows]
    prog = [r["zmiana_prognoza"] * 100 for r in rows]
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.scatter(fakt, prog, alpha=0.5, s=15, color="#2ca02c")
    lims = [min(min(fakt), min(prog)) - 2, max(max(fakt), max(prog)) + 2]
    ax.plot(lims, lims, "k--", linewidth=1, label="Idealna zgodność (y = x)")
    ax.set_xlabel("Zmiana faktyczna (cm)")
    ax.set_ylabel("Zmiana prognozowana (cm)")
    ax.set_title("Zmiana poziomu: faktyczna vs prognoza modelu")
    ax.legend()
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(figs_dir / "zmiana_fakt_vs_prognoza.png", dpi=150)
    plt.close()


def _plot_blad_miesieczny(rows, figs_dir, rows_natural=None):
    nat_by_date = _align_natural_by_date(rows, rows_natural)
    if nat_by_date is not None:
        dates = []
        blad = []
        for r in rows:
            nat = nat_by_date.get(r["data"])
            if nat is not None:
                dates.append(np.datetime64(r["data"] + "-01"))
                blad.append((r["zmiana_fakt"] - nat["zmiana_prognoza"]) * 100)
        if dates and blad:
            title = "Błąd prognozy zmiany poziomu (zmiana faktyczna − prognoza modelu naturalnego, sprzed drenażu)"
        else:
            dates = [np.datetime64(r["data"] + "-01") for r in rows]
            blad = [r["błąd"] * 100 for r in rows]
            title = "Błąd prognozy zmiany poziomu w kolejnych miesiącach"
    else:
        dates = [np.datetime64(r["data"] + "-01") for r in rows]
        blad = [r["błąd"] * 100 for r in rows]
        title = "Błąd prognozy zmiany poziomu w kolejnych miesiącach"
    fig, ax = plt.subplots(figsize=(12, 4))
    colors = ["#d62728" if b >= 0 else "#1f77b4" for b in blad]
    ax.bar(dates, blad, width=20, color=colors, alpha=0.7, edgecolor="none")
    ax.axhline(y=0, color="black", linewidth=0.5)
    ax.set_xlabel("Data")
    ax.set_ylabel("Błąd miesięczny (cm)")
    ax.set_title(title)
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.3, axis="y")
    fig.tight_layout()
    fig.savefig(figs_dir / "blad_miesieczny.png", dpi=150)
    plt.close()


def _write_report(rows, mae, rmse, n, lake_id, lake_name, rows_natural=None):
    figs_dir = _figs_dir(lake_id)
    figs_dir.mkdir(parents=True, exist_ok=True)
    _plot_wysokosci(rows, figs_dir, lake_name, lake_id, rows_natural=rows_natural)
    _plot_rozbieznosc(rows, figs_dir, rows_natural=rows_natural)
    _plot_zmiana_fakt_vs_prognoza(rows, figs_dir)
    _plot_blad_miesieczny(rows, figs_dir, rows_natural=rows_natural)
    model_path = lake.get_model_path(lake_id)
    if model_path.exists():
        _, _, lag_m, meteo_m = lake.load_model(model_path)
    else:
        lag_m = lake.LAG_MONTHS_BY_LAKE.get(lake_id, lake.LAG_MONTHS)
        meteo_m = 0
    lag_effective = max(lag_m, meteo_m)
    cechy_text = (
        f"Miesiąc (sin/cos), Opad, Temperatura"
        + (f", opad i temperatura z opóźnieniem 1–{meteo_m} mies." if meteo_m > 0 else "")
        + f", {lag_m} opóźnienia zmiany poziomu, {lag_m} opóźnienia poziomu"
    )
    sections = [
        f"# Raport podsumowujący: prognoza zmiany poziomu {lake_name}",
        "",
        "## 1. Cel projektu",
        "",
        "Projekt ma na celu:",
        f"- zbudowanie **modelu uczenia maszynowego**, który na podstawie opadu i temperatury (oraz sezonowości i historii) prognozuje **miesięczną zmianę poziomu** {lake_name};",
        "- **ewaluację** prognoz względem rzeczywistych pomiarów.",
        "",
        "---",
        "",
        "## 2. Dane",
        "",
        f"- **Źródło:** plik `data/{lake_id}/data.csv`.",
        "- **Zakres:** dane miesięczne (pierwszy dzień miesiąca).",
        "- **Kolumny:** Data, Poziom (m), Zmiana (m), Opad (mm), Temperatura (°C).",
        "- **Target:** Zmiana – miesięczna zmiana poziomu.",
        "- Wiersze z błędami (#ERROR!) lub brakami są pomijane. Po usunięciu lagów ({} mies.) do analizy wchodzi **{}** miesięcy.".format(
            lag_effective,
            n,
        ),
        "",
        "---",
        "",
        "## 3. Model",
        "",
        "| Element | Opis |",
        "|--------|------|",
        "| Algorytm | Gradient Boosting (regresja), scikit-learn |",
        "| Cechy wejściowe | {} |".format(cechy_text),
        "| Trening (od–do) | {} |".format(_train_range_table_cell(lake_id, rows, rows_natural)),
        "| Wynik | Prognoza zmiany poziomu na dany miesiąc (cm) |",
        "",
        "Model **nie** używa bieżącego poziomu – tylko opad, temperatura, sezon i historia.",
        "",
    ]
    sections += [
        "",
        "---",
        "",
        "## 4. Wyniki ewaluacji",
        "",
        "- **MAE (średni błąd bezwzględny):** {:.2f} cm".format(mae * 100),
        "- **RMSE:** {:.2f} cm".format(rmse * 100),
        "- **Liczba miesięcy:** {}".format(n),
        "",
        "### 4.1. Wysokość wody: rzeczywista vs scenariusz modelowy",
        "",
        "Scenariusz modelowy: start od poziomu na początek pierwszego miesiąca; w każdym miesiącu dodawana jest **prognozowana** zmiana (kumulatywnie).",
        "",
        "![Wysokość rzeczywista vs model](wysokosc_rzeczywista_vs_model.png)",
        "",
        "### 4.2. Rozbieżność w czasie",
        "",
        "Rozbieżność = wysokość rzeczywista − wysokość w scenariuszu "
        + ("**modelu naturalnego (sprzed drenażu)**. Wartość dodatnia: jezioro wyżej niż przewidywał model naturalny; ujemna: niżej (np. efekt drenażu)." if rows_natural else "modelowym. Wartość dodatnia: jezioro wyżej niż przewidywał model; ujemna: niżej."),
        "",
        "![Rozbieżność w czasie](rozbieznosc_w_czasie.png)",
        "",
        "### 4.3. Zmiana poziomu: faktyczna vs prognoza",
        "",
        "Punkty przy linii y = x oznaczają dobrą zgodność miesięcznych zmian.",
        "",
        "![Zmiana faktyczna vs prognoza](zmiana_fakt_vs_prognoza.png)",
        "",
        "### 4.4. Błąd miesięczny",
        "",
        "Błąd = zmiana faktyczna − zmiana prognozowana w każdym miesiącu "
        + ("przez **model naturalny (sprzed drenażu)**." if rows_natural else "."),
        "",
        "![Błąd miesięczny](blad_miesieczny.png)",
        "",
        "---",
        "",
        "## 5. Podsumowanie",
        "",
        "- Model prognozuje miesięczną zmianę poziomu {} z MAE ~{:.2f} cm.".format(lake_name, mae * 100),
        "- Scenariusz kumulatywny (wysokość z prognozowanej zmiany) jest porównywany z rzeczywistą wysokością; rozbieżność i błąd miesięczny opisują jakość prognoz.",
        "",
        "Szczegóły techniczne: [model.md](../model.md), [podsumowanie_ewaluacji.md](podsumowanie_ewaluacji.md).",
        "",
        f"*Wygenerowano: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        "",
    ]
    report_path = _report_path(lake_id)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(sections), encoding="utf-8")
    print(f"Raport zapisany: {report_path}")


def run(lake_id="niedziegiel"):
    mae, rmse, rows = run_evaluation(lake_id=lake_id)
    if rows is None or len(rows) == 0:
        raise ValueError("Brak danych do raportu.")
    rows_natural = None
    natural_path = lake.get_model_path(lake_id, "natural")
    if natural_path.exists():
        _, _, rows_natural = run_evaluation(
            lake_id=lake_id,
            model_path=natural_path,
            output_path=_figs_dir(lake_id) / "podsumowanie_ewaluacji_natural.md",
        )
    lake_name = lake.LAKES.get(lake_id, lake_id)
    _write_report(rows, mae, rmse, len(rows), lake_id, lake_name, rows_natural=rows_natural)


if __name__ == "__main__":
    lake_id = sys.argv[1] if len(sys.argv) > 1 else None
    if lake_id and lake_id not in lake.LAKES:
        print(f"Dostępne jeziora: {', '.join(lake.LAKES)}")
        sys.exit(1)
    for lid in (lake.LAKES if lake_id is None else [lake_id]):
        if not lake.get_model_path(lid).exists():
            print(f"Pomijam {lid}: brak pliku modelu.")
            continue
        run(lake_id=lid)
