import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

import lake
from evaluate_predictions import run_evaluation

DOCS_DIR = Path(__file__).resolve().parent / "docs"


def _figs_dir(lake_id):
    return DOCS_DIR / f"figures_{lake_id}"


def _report_path(lake_id):
    return DOCS_DIR / f"raport_podsumowujacy_{lake_id}.md"


def _plot_wysokosci(rows, figs_dir, lake_name):
    dates = [np.datetime64(r["data"] + "-01") for r in rows]
    rzeczywista = [r["wysokosc_rzeczywista"] for r in rows]
    model = [r["wysokosc_model"] for r in rows]
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(dates, rzeczywista, label="Wysokość rzeczywista", color="#1f77b4", linewidth=1.2)
    ax.plot(dates, model, label="Wysokość scenariusz modelowy", color="#ff7f0e", linewidth=1.2, linestyle="--")
    ax.set_xlabel("Data")
    ax.set_ylabel("Wysokość (m)")
    ax.set_title(f"{lake_name} – wysokość wody: rzeczywista vs scenariusz modelowy")
    ax.legend(loc="best")
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(figs_dir / "wysokosc_rzeczywista_vs_model.png", dpi=150)
    plt.close()


def _plot_rozbieznosc(rows, figs_dir):
    dates = [np.datetime64(r["data"] + "-01") for r in rows]
    rozb = [r["rozbieznosc"] for r in rows]
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.fill_between(dates, 0, rozb, where=[x >= 0 for x in rozb], color="#1f77b4", alpha=0.6, label="Rzeczywistość > model")
    ax.fill_between(dates, 0, rozb, where=[x < 0 for x in rozb], color="#ff7f0e", alpha=0.6, label="Rzeczywistość < model")
    ax.axhline(y=0, color="black", linewidth=0.5)
    ax.set_xlabel("Data")
    ax.set_ylabel("Rozbieżność (m)")
    ax.set_title("Rozbieżność: wysokość rzeczywista − scenariusz modelowy")
    ax.legend(loc="best")
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(figs_dir / "rozbieznosc_w_czasie.png", dpi=150)
    plt.close()


def _plot_zmiana_fakt_vs_prognoza(rows, figs_dir):
    fakt = [r["zmiana_fakt"] for r in rows]
    prog = [r["zmiana_prognoza"] for r in rows]
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.scatter(fakt, prog, alpha=0.5, s=15, color="#2ca02c")
    lims = [min(min(fakt), min(prog)) - 0.02, max(max(fakt), max(prog)) + 0.02]
    ax.plot(lims, lims, "k--", linewidth=1, label="Idealna zgodność (y = x)")
    ax.set_xlabel("Zmiana faktyczna (m)")
    ax.set_ylabel("Zmiana prognozowana (m)")
    ax.set_title("Zmiana poziomu: faktyczna vs prognoza modelu")
    ax.legend()
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(figs_dir / "zmiana_fakt_vs_prognoza.png", dpi=150)
    plt.close()


def _plot_blad_miesieczny(rows, figs_dir):
    dates = [np.datetime64(r["data"] + "-01") for r in rows]
    blad = [r["błąd"] for r in rows]
    fig, ax = plt.subplots(figsize=(12, 4))
    colors = ["#d62728" if b >= 0 else "#1f77b4" for b in blad]
    ax.bar(dates, blad, width=20, color=colors, alpha=0.7, edgecolor="none")
    ax.axhline(y=0, color="black", linewidth=0.5)
    ax.set_xlabel("Data")
    ax.set_ylabel("Błąd miesięczny (m)")
    ax.set_title("Błąd prognozy zmiany poziomu w kolejnych miesiącach")
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.3, axis="y")
    fig.tight_layout()
    fig.savefig(figs_dir / "blad_miesieczny.png", dpi=150)
    plt.close()


def _write_report(rows, mae, rmse, n, lake_id, lake_name):
    figs_dir = _figs_dir(lake_id)
    figs_dir.mkdir(parents=True, exist_ok=True)
    _plot_wysokosci(rows, figs_dir, lake_name)
    _plot_rozbieznosc(rows, figs_dir)
    _plot_zmiana_fakt_vs_prognoza(rows, figs_dir)
    _plot_blad_miesieczny(rows, figs_dir)
    figs_ref = f"figures_{lake_id}"
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
        f"- **Źródło:** plik `data/{lake_id}_data.csv`.",
        "- **Zakres:** dane miesięczne (pierwszy dzień miesiąca).",
        "- **Kolumny:** Data, Poziom (m), Zmiana (m), Opad (mm), Temperatura (°C).",
        "- **Target:** Zmiana – miesięczna zmiana poziomu.",
        "- Wiersze z błędami (#ERROR!) lub brakami są pomijane. Po usunięciu lagów (3 miesiące) do analizy wchodzi **{}** miesięcy.".format(n),
        "",
        "---",
        "",
        "## 3. Model",
        "",
        "| Element | Opis |",
        "|--------|------|",
        "| Algorytm | Gradient Boosting (regresja), scikit-learn |",
        "| Cechy wejściowe | Miesiąc (sin/cos), Opad, Temperatura, 3 opóźnienia zmiany poziomu, 3 opóźnienia poziomu |",
        "| Trening | Podział czasowy: ostatnie 70 miesięcy = zbiór testowy |",
        "| Wynik | Prognoza zmiany poziomu na dany miesiąc (m) |",
        "",
        "Model **nie** używa bieżącego poziomu – tylko opad, temperatura, sezon i historia.",
        "",
        "---",
        "",
        "## 4. Wyniki ewaluacji",
        "",
        "- **MAE (średni błąd bezwzględny):** {:.4f} m (~{:.2f} cm)".format(mae, mae * 100),
        "- **RMSE:** {:.4f} m".format(rmse),
        "- **Liczba miesięcy:** {}".format(n),
        "",
        "### 4.1. Wysokość wody: rzeczywista vs scenariusz modelowy",
        "",
        "Scenariusz modelowy: start od poziomu na początek pierwszego miesiąca; w każdym miesiącu dodawana jest **prognozowana** zmiana (kumulatywnie).",
        "",
        "![Wysokość rzeczywista vs model]({}/wysokosc_rzeczywista_vs_model.png)".format(figs_ref),
        "",
        "### 4.2. Rozbieżność w czasie",
        "",
        "Rozbieżność = wysokość rzeczywista − wysokość w scenariuszu modelowym. Wartość dodatnia: jezioro wyżej niż przewidywał model; ujemna: niżej.",
        "",
        "![Rozbieżność w czasie]({}/rozbieznosc_w_czasie.png)".format(figs_ref),
        "",
        "### 4.3. Zmiana poziomu: faktyczna vs prognoza",
        "",
        "Punkty przy linii y = x oznaczają dobrą zgodność miesięcznych zmian.",
        "",
        "![Zmiana faktyczna vs prognoza]({}/zmiana_fakt_vs_prognoza.png)".format(figs_ref),
        "",
        "### 4.4. Błąd miesięczny",
        "",
        "Błąd = zmiana faktyczna − zmiana prognozowana w każdym miesiącu.",
        "",
        "![Błąd miesięczny]({}/blad_miesieczny.png)".format(figs_ref),
        "",
        "---",
        "",
        "## 5. Podsumowanie",
        "",
        "- Model prognozuje miesięczną zmianę poziomu {} z MAE ~{:.2f} cm.".format(lake_name, mae * 100),
        "- Scenariusz kumulatywny (wysokość z prognozowanej zmiany) jest porównywany z rzeczywistą wysokością; rozbieżność i błąd miesięczny opisują jakość prognoz.",
        "",
        "Szczegóły techniczne: [model.md](model.md), [podsumowanie_ewaluacji_{}.md](podsumowanie_ewaluacji_{}.md).".format(lake_id, lake_id),
        "",
    ])
    report_path = _report_path(lake_id)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(sections), encoding="utf-8")
    print(f"Raport zapisany: {report_path}")


def run(lake_id="niedziegiel"):
    mae, rmse, rows = run_evaluation(lake_id=lake_id)
    if rows is None or len(rows) == 0:
        raise ValueError("Brak danych do raportu.")
    lake_name = lake.LAKES.get(lake_id, lake_id)
    _write_report(rows, mae, rmse, len(rows), lake_id, lake_name)


if __name__ == "__main__":
    lake_id = sys.argv[1] if len(sys.argv) > 1 else None
    if lake_id and lake_id not in lake.LAKES:
        print(f"Dostępne jeziora: {', '.join(lake.LAKES)}")
        sys.exit(1)
    for lid in (lake.LAKES if lake_id is None else [lake_id]):
        run(lake_id=lid)
