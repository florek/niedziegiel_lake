from __future__ import annotations

import argparse
import sys
from dataclasses import replace
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

_root = Path(__file__).resolve().parents[1]
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from lake.base import LakeRegressionModel
from lake.budzislawskie import BUDZISLAWSKIE_CONFIG
from lake.config import LakeRegressionConfig
from lake.niedziegiel import NIEDZIEGIEL_CONFIG
from lake.powidzkie import POWIDZKIE_CONFIG
from lake.skulskie import SKULSKIE_CONFIG

LAKES: list[tuple[str, LakeRegressionConfig, str]] = [
    ("niedziegiel", NIEDZIEGIEL_CONFIG, "Niedzięgiel"),
    ("powidzkie", POWIDZKIE_CONFIG, "Powidzkie"),
    ("budzislawskie", BUDZISLAWSKIE_CONFIG, "Budzisławskie"),
    ("skulskie", SKULSKIE_CONFIG, "Skulskie"),
]

YEARS_AFTER_START = 10
YEARS_BEFORE_END = 3
DEFAULT_EVAL_MONTHS = 24


def _load_data(config: LakeRegressionConfig) -> pd.DataFrame:
    data_path = _root / config.data_path if not Path(config.data_path).is_absolute() else Path(config.data_path)
    if not data_path.exists():
        raise FileNotFoundError(f"Brak pliku: {data_path}")
    df = pd.read_csv(data_path)
    df.columns = [c.strip().lstrip("\ufeff") for c in df.columns]
    date_col = next((c for c in df.columns if c == "Data"), None)
    if date_col is None:
        raise ValueError("Brak kolumny Data w CSV.")
    df["Data"] = pd.to_datetime(df["Data"].astype(str).str.strip(), errors="coerce")
    df = df.dropna(subset=["Data"]).sort_values("Data")
    return df


def _data_date_range(config: LakeRegressionConfig) -> tuple[pd.Timestamp, pd.Timestamp]:
    df = _load_data(config)
    return df["Data"].min(), df["Data"].max()


def _yearly_mean_level(config: LakeRegressionConfig) -> pd.DataFrame:
    df = _load_data(config)
    if "Poziom" not in df.columns:
        return pd.DataFrame(columns=["rok", "poziom"])
    s = df["Poziom"].astype(str).str.replace(",", ".", regex=False)
    s = pd.to_numeric(s, errors="coerce")
    df = df.assign(rok=df["Data"].dt.year, poziom=s)
    return df.groupby("rok", as_index=False)["poziom"].mean()


def _run_rolling_mae(
    config: LakeRegressionConfig,
    label: str,
    eval_months: int,
    reports_dir: Path,
) -> pd.DataFrame:
    first_ts, last_ts = _data_date_range(config)
    first_year = first_ts.year
    last_year = last_ts.year
    start_year = first_year + YEARS_AFTER_START
    end_year = last_year - YEARS_BEFORE_END
    if start_year > end_year:
        raise ValueError(
            f"Zakres treningu pusty: start_year={start_year} (początek+{YEARS_AFTER_START}), "
            f"end_year={end_year} (koniec-{YEARS_BEFORE_END}). "
            f"Dane: {first_year}–{last_year}."
        )
    rows: list[dict] = []
    for year in range(start_year, end_year + 1):
        train_end = f"{year}-12-01"
        cfg = replace(config, train_end=train_end)
        model = LakeRegressionModel(cfg)
        model.load_data()
        model.train(mode="full")
        metrics = model.evaluate_breakdown(horizon_months=eval_months)
        rows.append({
            "train_end": train_end,
            "rok": year,
            "mae": round(metrics["mae"], 4),
            "mae_spadki": round(metrics["mae_drops"], 4) if not pd.isna(metrics["mae_drops"]) else None,
            "mae_przyrosty": round(metrics["mae_rises"], 4) if not pd.isna(metrics["mae_rises"]) else None,
            "rmse": round(metrics["rmse"], 4),
            "r2": round(metrics["r2"], 4),
        })
    df = pd.DataFrame(rows)
    reports_dir.mkdir(parents=True, exist_ok=True)
    csv_path = reports_dir / "rolling_mae.csv"
    df.to_csv(csv_path, index=False)
    summary = pd.DataFrame([{
        "min_mae": df["mae"].min(),
        "max_mae": df["mae"].max(),
        "mean_mae": round(df["mae"].mean(), 4),
        "rok_min_mae": int(df.loc[df["mae"].idxmin(), "rok"]),
        "rok_max_mae": int(df.loc[df["mae"].idxmax(), "rok"]),
    }])
    summary_path = reports_dir / "rolling_mae_summary.csv"
    summary.to_csv(summary_path, index=False)
    level_df = _yearly_mean_level(config)
    fig, ax = plt.subplots(figsize=(12, 5))
    spadki = df["mae_spadki"].fillna(0).values
    przyrosty = df["mae_przyrosty"].fillna(0).values
    width = 0.6
    ax.bar(
        df["rok"] - width / 2,
        spadki,
        width=width,
        label="MAE (spadki)",
        color="tab:red",
    )
    ax.bar(
        df["rok"] - width / 2,
        przyrosty,
        width=width,
        bottom=spadki,
        label="MAE (przyrosty)",
        color="tab:green",
    )
    ax.set_xlabel("Koniec treningu (rok)")
    ax.set_ylabel("MAE (m)")
    ax2 = ax.twinx()
    if len(level_df) > 0:
        ax2.plot(
            level_df["rok"],
            level_df["poziom"],
            color="tab:orange",
            alpha=0.8,
            linewidth=2,
            label="Rzeczywisty poziom (śr. roczna)",
        )
    ax2.set_ylabel("Poziom (m)", color="tab:orange")
    ax2.tick_params(axis="y", labelcolor="tab:orange")
    ax.set_title(
        f"{label}: MAE (spadki + przyrosty) na {eval_months} miesiącach po treningu "
        f"(wykrywanie zmiany reżimu)"
    )
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc="best")
    ax.grid(True, alpha=0.3, axis="y")
    fig.tight_layout()
    png_path = reports_dir / "rolling_mae.png"
    fig.savefig(png_path, dpi=150)
    plt.close(fig)
    return df


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Trening z przesuwanym końcem treningu: od 10 lat po początku do 3 lat przed końcem; MAE w tabeli i na wykresie (wykrywanie zmiany reżimu)."
    )
    parser.add_argument(
        "--lake",
        choices=[lake_id for lake_id, *_ in LAKES],
        default=None,
        help="Jedno jezioro; bez argumentu: wszystkie.",
    )
    parser.add_argument(
        "--eval-months",
        type=int,
        default=DEFAULT_EVAL_MONTHS,
        help=f"Zbiór testowy: tylko kolejne N miesięcy po treningu (domyślnie {DEFAULT_EVAL_MONTHS}).",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    lakes = [t for t in LAKES if args.lake is None or t[0] == args.lake]
    for lake_id, config, label in lakes:
        reports_dir = _root / "reports" / lake_id
        df = _run_rolling_mae(
            config=config,
            label=label,
            eval_months=args.eval_months,
            reports_dir=reports_dir,
        )
        csv_path = reports_dir / "rolling_mae.csv"
        png_path = reports_dir / "rolling_mae.png"
        print(f"\n{label} – MAE dla przesuwającego się końca treningu (ewaluacja: {args.eval_months} mies.):")
        print(df.to_string(index=False))
        summary_path = reports_dir / "rolling_mae_summary.csv"
        if summary_path.exists():
            summary = pd.read_csv(summary_path)
            print("Podsumowanie:", summary.to_string(index=False))
        print(f"Zapis: {csv_path}, {summary_path}, {png_path}")


if __name__ == "__main__":
    main()
