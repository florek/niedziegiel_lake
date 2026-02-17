import sys
from datetime import datetime
from pathlib import Path

import lake
from evaluate_predictions import run_evaluation

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"


def _collect_metrics():
    results = []
    for lid in lake.LAKES:
        if not lake.get_model_path(lid).exists():
            continue
        try:
            mae, rmse, rows, _ = run_evaluation(lake_id=lid)
        except Exception as e:
            print(f"Pomijam {lid}: {e}")
            continue
        if not rows:
            continue
        lake_name = lake.LAKES.get(lid, lid)
        period_start = rows[0]["data"]
        period_end = rows[-1]["data"]
        results.append({
            "lake_id": lid,
            "lake_name": lake_name,
            "period_start": period_start,
            "period_end": period_end,
            "n": len(rows),
            "mae": mae,
            "rmse": rmse,
        })
    return results


def _write_summary_report(results):
    lines = [
        "# Raport ogólny – prognoza zmiany poziomu jezior",
        "",
        "Podsumowanie ewaluacji modeli dla wszystkich jezior. Metryki (MAE, RMSE) i okres dotyczą **zbioru testowego**.",
        "",
        "> Linki są względem katalogu `docs/` (działają w podglądzie na GitHubie).",
        "",
        "## Tabela zbiorcza",
        "",
        "| Jezioro | Okres testowy | Liczba miesięcy | MAE (cm) | RMSE (cm) | Raport szczegółowy |",
        "|---------|----------------|-----------------|----------|-----------|--------------------|",
    ]
    for r in results:
        link = f"[raport]({r['lake_id']}/raport_podsumowujacy.md)"
        lines.append(
            f"| {r['lake_name']} | {r['period_start']} – {r['period_end']} | {r['n']} | {r['mae'] * 100:.2f} | {r['rmse'] * 100:.2f} | {link} |"
        )
    lines.extend([
        "",
        "## Raporty per jezioro",
        "",
    ])
    for r in results:
        lines.append(f"- **{r['lake_name']}:** [raport z wykresami]({r['lake_id']}/raport_podsumowujacy.md), [podsumowanie ewaluacji]({r['lake_id']}/podsumowanie_ewaluacji.md)")
    lines.append("")
    lines.append(f"*Wygenerowano: {datetime.now().strftime('%Y-%m-%d %H:%M')}*")
    lines.append("")
    out_path = DOCS_DIR / "raport_ogolny.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Raport ogólny zapisany: {out_path}")


if __name__ == "__main__":
    results = _collect_metrics()
    if not results:
        print("Brak wytrenowanych modeli. Uruchom np. python sources/lake.py niedziegiel")
        sys.exit(1)
    _write_summary_report(results)
