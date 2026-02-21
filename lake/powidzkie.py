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

POWIDZKIE_CONFIG = LakeRegressionConfig(
    lake_id="powidzkie",
    name="Powidzkie",
    data_path="data/powidzkie/data_ext.csv",
    train_end="2015-01-01",
    base_features=BASE_FEATURES,
    lag_columns=LAG_COLUMNS,
    lags=[1, 2, 3, 6],
    constraints=LakeConstraints(
        spillway_level=98.60,
        outflow_k=0.6,
        outflow_exp=1.2,
        max_level_mode="history",
        max_level_fixed=99.00,
        max_level_margin=0.00,
        min_level_fixed=None,
    ),
)


class Powidzkie(LakeRegressionModel):
    def __init__(self) -> None:
        super().__init__(POWIDZKIE_CONFIG)
