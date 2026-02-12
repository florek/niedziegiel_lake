from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

import lake
from evaluate_predictions import _find_break_month, run_evaluation

FIGS_DIR = Path(__file__).resolve().parent / "docs" / "figures"
REPORT_PATH = Path(__file__).resolve().parent / "docs" / "raport_podsumowujacy.md"


def _ensure_figures_dir():
    FIGS_DIR.mkdir(parents=True, exist_ok=True)


def _plot_wysokosci(rows, break_month, break_idx):
    dates = [np.datetime64(r["data"] + "-01") for r in rows]
    rzeczywista = [r["wysokosc_rzeczywista"] for r in rows]
    model = [r["wysokosc_model"] for r in rows]
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(dates, rzeczywista, label="Wysokość rzeczywista", color="#1f77b4", linewidth=1.2)
    ax.plot(dates, model, label="Wysokość scenariusz modelowy", color="#ff7f0e", linewidth=1.2, linestyle="--")
    if break_idx is not None:
        ax.axvline(x=dates[break_idx], color="red", linestyle=":", linewidth=1.5, label=f"Moment rozjazdu ({break_month})")
    ax.set_xlabel("Data")
    ax.set_ylabel("Wysokość (m)")
    ax.set_title("Jezioro Niedzięgiel – wysokość wody: rzeczywista vs scenariusz modelowy")
    ax.legend(loc="best")
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIGS_DIR / "wysokosc_rzeczywista_vs_model.png", dpi=150)
    plt.close()


def _plot_rozbieznosc(rows, break_month, break_idx):
    dates = [np.datetime64(r["data"] + "-01") for r in rows]
    rozb = [r["rozbieznosc"] for r in rows]
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.fill_between(dates, 0, rozb, where=[x >= 0 for x in rozb], color="#1f77b4", alpha=0.6, label="Rzeczywistość > model")
    ax.fill_between(dates, 0, rozb, where=[x < 0 for x in rozb], color="#ff7f0e", alpha=0.6, label="Rzeczywistość < model")
    if break_idx is not None:
        ax.axvline(x=dates[break_idx], color="red", linestyle=":", linewidth=1.5, label=f"Moment rozjazdu ({break_month})")
    ax.axhline(y=0, color="black", linewidth=0.5)
    ax.set_xlabel("Data")
    ax.set_ylabel("Rozbieżność (m)")
    ax.set_title("Rozbieżność: wysokość rzeczywista − scenariusz modelowy")
    ax.legend(loc="best")
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIGS_DIR / "rozbieznosc_w_czasie.png", dpi=150)
    plt.close()


def _plot_zmiana_fakt_vs_prognoza(rows):
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
    fig.savefig(FIGS_DIR / "zmiana_fakt_vs_prognoza.png", dpi=150)
    plt.close()


def _plot_blad_miesieczny(rows, break_month, break_idx):
    dates = [np.datetime64(r["data"] + "-01") for r in rows]
    blad = [r["błąd"] for r in rows]
    fig, ax = plt.subplots(figsize=(12, 4))
    colors = ["#d62728" if b >= 0 else "#1f77b4" for b in blad]
    ax.bar(dates, blad, width=20, color=colors, alpha=0.7, edgecolor="none")
    if break_idx is not None:
        ax.axvline(x=dates[break_idx], color="red", linestyle=":", linewidth=1.5, label=f"Moment rozjazdu ({break_month})")
    ax.axhline(y=0, color="black", linewidth=0.5)
    ax.set_xlabel("Data")
    ax.set_ylabel("Błąd miesięczny (m)")
    ax.set_title("Błąd prognozy zmiany poziomu w kolejnych miesiącach")
    if break_idx is not None:
        ax.legend()
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.3, axis="y")
    fig.tight_layout()
    fig.savefig(FIGS_DIR / "blad_miesieczny.png", dpi=150)
    plt.close()


def _write_report(rows, mae, rmse, break_month, break_info, n):
    break_idx = next((i for i, r in enumerate(rows) if r["data"] == break_month), None) if break_month else None
    _ensure_figures_dir()
    _plot_wysokosci(rows, break_month, break_idx)
    _plot_rozbieznosc(rows, break_month, break_idx)
    _plot_zmiana_fakt_vs_prognoza(rows)
    _plot_blad_miesieczny(rows, break_month, break_idx)
    sections = [
        "# Raport podsumowujący: prognoza zmiany poziomu Jeziora Niedzięgiel",
        "",
        "## 1. Cel projektu",
        "",
        "Projekt ma na celu:",
        "- zbudowanie **modelu uczenia maszynowego**, który na podstawie opadu i temperatury (oraz sezonowości i historii) prognozuje **miesięczną zmianę poziomu** Jeziora Niedzięgiel;",
        "- **ewaluację** prognoz względem rzeczywistych pomiarów;",
        "- **wykrycie momentu**, od którego jezioro przestało reagować zgodnie z modelem (poziom rzeczywisty trwale odbiega od scenariusza opartego na prognozach).",
        "",
        "Teza: do pewnego momentu zachowanie poziomu jeziora da się wyjaśnić opadem i temperaturą; od pewnego momentu ta zależność została przerwana (np. zmiana odpływu, regulacja, użytkowanie).",
        "",
        "---",
        "",
        "## 2. Dane",
        "",
        "- **Źródło:** plik `data/data.csv`.",
        "- **Zakres:** dane miesięczne (pierwszy dzień miesiąca), od 1997 r.",
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
        "![Wysokość rzeczywista vs model](figures/wysokosc_rzeczywista_vs_model.png)",
        "",
        "### 4.2. Rozbieżność w czasie",
        "",
        "Rozbieżność = wysokość rzeczywista − wysokość w scenariuszu modelowym. Wartość dodatnia: jezioro wyżej niż przewidywał model; ujemna: niżej.",
        "",
        "![Rozbieżność w czasie](figures/rozbieznosc_w_czasie.png)",
        "",
        "### 4.3. Zmiana poziomu: faktyczna vs prognoza",
        "",
        "Punkty przy linii y = x oznaczają dobrą zgodność miesięcznych zmian.",
        "",
        "![Zmiana faktyczna vs prognoza](figures/zmiana_fakt_vs_prognoza.png)",
        "",
        "### 4.4. Błąd miesięczny",
        "",
        "Błąd = zmiana faktyczna − zmiana prognozowana w każdym miesiącu.",
        "",
        "![Błąd miesięczny](figures/blad_miesieczny.png)",
        "",
        "---",
        "",
        "## 5. Moment rozjazdu z modelem",
        "",
        ]
    if break_month and break_info:
        sections.extend([
            "**Wykryty moment:** od miesiąca **{}** poziom rzeczywisty trwale odbiega od scenariusza modelowego.".format(break_month),
            "",
            "- Rozbieżność w tym miesiącu: **{:+.3f} m** ({}).".format(break_info["rozbieznosc_w_momentcie"], break_info["kierunek"]),
            "",
            "**Interpretacja:** do tego momentu reakcja Jeziora Niedzięgiel na opad i temperaturę była zgodna z modelem; od miesiąca {} coś zmieniło zachowanie poziomu (np. zmiana odpływu, użytkowanie, regulacja).".format(break_month),
            "",
        ])
    else:
        sections.append("Nie wykryto wyraźnego, trwałego momentu rozjazdu (przyjęte progi: rozbieżność > 10 cm, utrzymanie > 6 miesięcy).")
        sections.append("")
    sections.extend([
        "---",
        "",
        "## 6. Podsumowanie",
        "",
        "- Model prognozuje miesięczną zmianę poziomu Jeziora Niedzięgiel z MAE ~{:.2f} cm.".format(mae * 100),
        "- Scenariusz „gdyby tylko opad i temperatura” (model) początkowo dobrze opisuje rzeczywistość; od pewnego momentu następuje **trwały rozjazd**.",
        "- Zidentyfikowany moment rozjazdu pozwala zawęzić w czasie poszukiwania przyczyn zmiany zachowania jeziora (dane hydrologiczne, zmiany w zagospodarowaniu, regulacje).",
        "",
        "Szczegóły techniczne: [model.md](model.md), [podsumowanie_ewaluacji.md](podsumowanie_ewaluacji.md).",
        "",
    ])
    report_path = Path(REPORT_PATH)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(sections), encoding="utf-8")
    print(f"Raport zapisany: {report_path}")


def run():
    mae, rmse, rows = run_evaluation()
    if rows is None or len(rows) == 0:
        raise ValueError("Brak danych do raportu.")
    break_month, break_info = _find_break_month(rows)
    _write_report(rows, mae, rmse, break_month, break_info, len(rows))


if __name__ == "__main__":
    run()
