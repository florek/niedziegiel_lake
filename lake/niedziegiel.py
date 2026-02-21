from __future__ import annotations

from lake.base import LakeRegressionModel
from lake.config import LakeConstraints, LakeRegressionConfig

BASE_FEATURES = [
    "Zmiana",
    "Opad",
    "Temperatura",
    "Rezerwuar_sniegu",
    "Opad_efektywny",
    "Snow_add_mm",
    "Rain_part_mm",
    "Melt_mm",
]

LAG_COLUMNS = [
    "Opad_efektywny",
    "Opad",
    "Temperatura",
    "Melt_mm",
    "Rezerwuar_sniegu",
    "Zmiana",
]

NIEDZIEGIEL_CONFIG = LakeRegressionConfig(
    lake_id="niedziegiel",
    name="Niedzięgiel",
    data_path="data/niedziegiel/data_ext.csv",
    train_end="2017-12-01",
    base_features=BASE_FEATURES,
    lag_columns=LAG_COLUMNS,
    lags=[1, 2, 3, 6],
    constraints=LakeConstraints(
        spillway_level=103.60,
        outflow_k=0.6,
        outflow_exp=1.2,
        max_level_mode="history",
        max_level_fixed=104.00,
        max_level_margin=0.00,
        min_level_fixed=None,
    ),
)


class Niedziegiel(LakeRegressionModel):
    def __init__(self) -> None:
        super().__init__(NIEDZIEGIEL_CONFIG)


def _main() -> None:
    model = Niedziegiel()
    model.load_data()
    metrics = model.train(mode="full")
    print("TRAIN:", metrics)
    future = model.get_future_data()
    pred = model.predict(horizon_months=12, future_features_df=future)
    model.generate_report(
        horizon_months=12,
        future_features_df=future,
        save_png=True,
        save_csv=True,
    )
    eval_metrics = model.evaluate(horizon_months=24)
    print("EVAL (24 m):", eval_metrics)


if __name__ == "__main__":
    _main()
