import sys
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


def _compute_drenaz_rows(rows, rows_natural):
    by_date = {r["data"]: r["wysokosc_rzeczywista"] for r in rows}
    by_date_nat = {r["data"]: r["wysokosc_model"] for r in rows_natural}
    common = sorted(set(by_date) & set(by_date_nat))
    out = []
    prev_drenaz = None
    for data in common:
        drenaz_cm = (by_date_nat[data] - by_date[data]) * 100
        przyrost = None
        if prev_drenaz is not None:
            przyrost = drenaz_cm - prev_drenaz
        prev_drenaz = drenaz_cm
        out.append({
            "data": data,
            "drenaz_cm": round(drenaz_cm, 1),
            "przyrost_cm": round(przyrost, 1) if przyrost is not None else None,
        })
    return out


def _yearly_sums(drenaz_rows):
    by_year = {}
    for r in drenaz_rows:
        if r["przyrost_cm"] is None:
            continue
        year = int(r["data"][:4])
        by_year.setdefault(year, []).append(r["przyrost_cm"])
    out = []
    for year in sorted(by_year):
        vals = by_year[year]
        out.append({"year": year, "suma_przyrost_cm": round(sum(vals), 1)})
    return out


def _write_table(drenaz_rows, lake_id, lake_name):
    figs_dir = _figs_dir(lake_id)
    figs_dir.mkdir(parents=True, exist_ok=True)
    path = figs_dir / "drenaz_miesieczny.md"
    yearly = _yearly_sums(drenaz_rows)
    lines = [
        f"# Drenaż – {lake_name}",
        "",
        "Drenaż = poziom z modelu naturalnego (bez drenażu) − poziom rzeczywisty. Przyrost = o ile wzrósł drenaż względem poprzedniego miesiąca.",
        "",
        "![Suma przyrostu drenażu wg roku](drenaz_miesieczny.png)",
        "",
        "## Suma przyrostu drenażu wg roku",
        "",
        "Tabela: **suma przyrostu dla każdego roku** (cm/rok), bez wierszy miesięcznych.",
        "",
        "| Rok | Suma przyrostu (cm/rok) |",
        "|-----|-------------------------|",
    ]
    for r in (yearly or []):
        lines.append(f"| {r['year']} | {r['suma_przyrost_cm']:+.1f} |")
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Tabela zapisana: {path}")


def _plot_drenaz(drenaz_rows, lake_id, lake_name):
    if not drenaz_rows:
        return
    figs_dir = _figs_dir(lake_id)
    figs_dir.mkdir(parents=True, exist_ok=True)
    yearly = _yearly_sums(drenaz_rows)
    if not yearly:
        return
    years = [r["year"] for r in yearly]
    sumy = [r["suma_przyrost_cm"] for r in yearly]
    colors = ["#d62728" if s > 0 else "#2ca02c" if s < 0 else "gray" for s in sumy]
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(years, sumy, color=colors, alpha=0.7, edgecolor="none")
    ax.set_ylabel("Suma przyrostu drenażu (cm/rok)")
    ax.set_xlabel("Rok")
    ax.set_title(f"{lake_name} – suma przyrostu drenażu w roku")
    ax.axhline(y=0, color="black", linewidth=0.5)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    out_path = figs_dir / "drenaz_miesieczny.png"
    fig.savefig(str(out_path), dpi=150)
    plt.close()
    print(f"Wykres zapisany: {out_path}")


def run_lake(lake_id):
    natural_path = lake.get_model_path(lake_id, "natural")
    if not natural_path.exists():
        print(f"Pomijam {lake_id}: brak modelu naturalnego.")
        return
    mae, rmse, rows, _ = run_evaluation(lake_id=lake_id)
    _, _, rows_natural, _ = run_evaluation(
        lake_id=lake_id,
        model_path=natural_path,
        output_path=_figs_dir(lake_id) / "podsumowanie_ewaluacji_natural.md",
    )
    if not rows or not rows_natural:
        print(f"Pomijam {lake_id}: brak danych.")
        return
    drenaz_rows = _compute_drenaz_rows(rows, rows_natural)
    if not drenaz_rows:
        print(f"Pomijam {lake_id}: brak wspólnych dat (drenaż).")
        return
    lake_name = lake.LAKES.get(lake_id, lake_id)
    _write_table(drenaz_rows, lake_id, lake_name)
    _plot_drenaz(drenaz_rows, lake_id, lake_name)


def run_all():
    for lake_id in lake.LAKES:
        run_lake(lake_id)


if __name__ == "__main__":
    lake_id = sys.argv[1] if len(sys.argv) > 1 else None
    if lake_id and lake_id not in lake.LAKES:
        print(f"Dostępne jeziora: {', '.join(lake.LAKES)}")
        sys.exit(1)
    if lake_id:
        run_lake(lake_id)
    else:
        run_all()
