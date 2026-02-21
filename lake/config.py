from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class LakeConstraints:
    spillway_level: float = 103.40
    outflow_k: float = 0.6
    outflow_exp: float = 1.2
    max_level_mode: str = "history"
    max_level_fixed: float = 104.00
    max_level_margin: float = 0.00
    min_level_fixed: float | None = None


@dataclass
class LakeRegressionConfig:
    lake_id: str
    name: str
    data_path: str
    train_end: str
    base_features: list[str]
    lag_columns: list[str]
    lags: list[int] = field(default_factory=lambda: [1, 2, 3])
    model_kwargs: dict = field(default_factory=dict)
    constraints: LakeConstraints | None = None
    min_train_rows: int = 24
    target_col: str = "Zmiana"
    level_col: str = "Poziom"

    def __post_init__(self) -> None:
        if not self.model_kwargs:
            self.model_kwargs = {
                "loss": "squared_error",
                "learning_rate": 0.05,
                "max_depth": 6,
                "max_iter": 2000,
                "min_samples_leaf": 10,
                "l2_regularization": 1e-3,
                "random_state": 42,
            }
