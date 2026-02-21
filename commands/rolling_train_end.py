from __future__ import annotations

import argparse
import sys
from dataclasses import replace
from pathlib import Path

_root = Path(__file__).resolve().parents[1]
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from lake.base import LakeRegressionModel
from lake.config import LakeRegressionConfig
from lake.budzislawskie import BUDZISLAWSKIE_CONFIG
from lake.niedziegiel import NIEDZIEGIEL_CONFIG
from lake.powidzkie import POWIDZKIE_CONFIG

TRAIN_END_YEAR_FIRST = 2024
TRAIN_END_YEAR_LAST = 1990
BUDZISLAWSKIE_YEAR_LAST = 2002

LAKES = [
    ("niedziegiel", NIEDZIEGIEL_CONFIG, "Niedzięgiel", TRAIN_END_YEAR_LAST),
    ("powidzkie", POWIDZKIE_CONFIG, "Powidzkie", TRAIN_END_YEAR_LAST),
    ("budzislawskie", BUDZISLAWSKIE_CONFIG, "Budzisławskie", BUDZISLAWSKIE_YEAR_LAST),
]


def _run_variants_for_config(
    base_config: LakeRegressionConfig,
    label: str,
    year_last: int = TRAIN_END_YEAR_LAST,
) -> None:
    for year in range(TRAIN_END_YEAR_FIRST, year_last - 1, -1):
        train_end = f"{year}-12-01"
        config = replace(base_config, train_end=train_end)
        model = LakeRegressionModel(config)
        model.load_data()
        model.train(mode="full")
        train_start = 1976 if year_last == TRAIN_END_YEAR_LAST else 1992
        chart_path = model._reports_dir / f"train_{train_start}_{year}.png"
        model._save_full_history_chart(save_path=chart_path)
        print(f"{label}: train {train_start}–{year}, test od {year + 1} → {chart_path.name}")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Warianty treningu: koniec treningu 2024→1990 (lub 2002 dla Budzisławskiego).")
    parser.add_argument(
        "--lake",
        choices=[lake_id for lake_id, *_ in LAKES],
        default=None,
        help="Jedno jezioro (niedziegiel, powidzkie, budzislawskie). Bez argumentu: wszystkie.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    lakes = [t for t in LAKES if args.lake is None or t[0] == args.lake]
    print(
        f"Warianty: trening 1976–(rok) / 1992–(rok), test do 2025. "
        f"Ostatni rok treningu od {TRAIN_END_YEAR_FIRST} do {TRAIN_END_YEAR_LAST} (Budzisławskie: {BUDZISLAWSKIE_YEAR_LAST}).\n"
    )
    for lake_id, config, label, year_last in lakes:
        _run_variants_for_config(config, label, year_last=year_last)


if __name__ == "__main__":
    main()
