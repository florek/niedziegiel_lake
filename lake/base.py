from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from lake.config import LakeConstraints, LakeRegressionConfig


def _project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _to_float_series(s: pd.Series) -> pd.Series:
    if not pd.api.types.is_numeric_dtype(s):
        s = s.astype(str).str.replace(",", ".", regex=False)
        s = s.replace({"nan": np.nan, "None": np.nan, "": np.nan})
    return pd.to_numeric(s, errors="coerce")


def _add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["month"] = df["Data"].dt.month.astype(int)
    df["month_sin"] = np.sin(2 * np.pi * df["month"] / 12.0)
    df["month_cos"] = np.cos(2 * np.pi * df["month"] / 12.0)
    return df


def _add_lags(df: pd.DataFrame, cols: list[str], lags: list[int]) -> pd.DataFrame:
    df = df.copy()
    for c in cols:
        for l in lags:
            df[f"{c}_lag{l}"] = df[c].shift(l)
    return df


def _compute_max_level(df_raw: pd.DataFrame, cfg: LakeConstraints) -> float:
    if cfg.max_level_mode == "fixed":
        return float(cfg.max_level_fixed + cfg.max_level_margin)
    hist_max = _to_float_series(df_raw["Poziom"]).dropna().max()
    return float(hist_max + cfg.max_level_margin)


def _apply_constraints(
    level_pred_next: float,
    max_level: float,
    cfg: LakeConstraints,
) -> float:
    level = float(level_pred_next)
    if level > cfg.spillway_level:
        excess = level - cfg.spillway_level
        outflow = cfg.outflow_k * (excess ** cfg.outflow_exp)
        level = level - outflow
    level = min(level, float(max_level))
    if cfg.min_level_fixed is not None:
        level = max(level, float(cfg.min_level_fixed))
    return level


class LakeRegressionModel:
    def __init__(self, config: LakeRegressionConfig) -> None:
        self.config = config
        self._root = _project_root()
        self._model_path = self._root / "ml_models" / config.lake_id / "model.joblib"
        self._reports_dir = self._root / "reports" / config.lake_id
        self._df_raw: Optional[pd.DataFrame] = None
        self._df_prepared: Optional[pd.DataFrame] = None
        self._train_df: Optional[pd.DataFrame] = None
        self._test_df: Optional[pd.DataFrame] = None
        self._model: Optional[HistGradientBoostingRegressor] = None
        self._feature_cols: Optional[list[str]] = None
        self._max_level: Optional[float] = None

    def _data_path(self) -> Path:
        p = Path(self.config.data_path)
        if not p.is_absolute():
            p = self._root / p
        return p

    def load_data(self) -> pd.DataFrame:
        path = self._data_path()
        if not path.exists():
            raise FileNotFoundError(f"Brak pliku danych: {path}")
        self._df_raw = pd.read_csv(path)
        self._df_raw.columns = [
            c.strip().lstrip("\ufeff") for c in self._df_raw.columns
        ]
        if self._df_raw.columns.duplicated().any():
            self._df_raw = self._df_raw.loc[:, ~self._df_raw.columns.duplicated()]
        return self._df_raw

    def prepare_dataset(self, df: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        raw = df if df is not None else self._df_raw
        if raw is None:
            raise RuntimeError("Brak danych. Wywołaj load_data() lub przekaż DataFrame.")
        df = raw.copy()
        date_col = None
        for c in df.columns:
            if c.strip().lstrip("\ufeff") == "Data":
                date_col = c
                break
        if date_col is None:
            raise ValueError(f"Brak kolumny 'Data'. Mam: {list(df.columns)}")
        if date_col != "Data":
            df = df.rename(columns={date_col: "Data"})
        if isinstance(df["Data"], pd.DataFrame):
            df["Data"] = df["Data"].iloc[:, 0]
        raw_dates = df["Data"].astype(str).str.strip()
        df["Data"] = pd.to_datetime(raw_dates, errors="coerce")
        still_na = df["Data"].isna()
        if still_na.any():
            df.loc[still_na, "Data"] = pd.to_datetime(
                raw_dates[still_na], format="%d.%m.%Y", dayfirst=True, errors="coerce"
            )
        df = df.dropna(subset=["Data"]).sort_values("Data").reset_index(drop=True)
        for c in df.columns:
            if c.strip().lstrip("\ufeff") == "Data" or pd.api.types.is_datetime64_any_dtype(df[c]):
                continue
            df[c] = _to_float_series(df[c])
        if self.config.target_col not in df.columns:
            raise ValueError(f"Brak kolumny '{self.config.target_col}'. Mam: {list(df.columns)}")
        if self.config.level_col not in df.columns:
            raise ValueError(f"Brak kolumny '{self.config.level_col}'. Mam: {list(df.columns)}")
        missing = [c for c in self.config.base_features if c not in df.columns]
        if missing:
            raise ValueError(f"Brakuje kolumn w CSV: {missing}. Mam: {list(df.columns)}")
        df = _add_time_features(df)
        lag_cols = [c for c in self.config.lag_columns if c in df.columns]
        df = _add_lags(df, cols=lag_cols, lags=self.config.lags)
        df["y_next"] = df[self.config.target_col].shift(-1)
        df["y_date"] = df["Data"].shift(-1)
        df = df.dropna(subset=["y_next", "y_date"]).reset_index(drop=True)
        self._df_prepared = df
        return df

    def _split(self, df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        train_end_dt = pd.to_datetime(self.config.train_end)
        train_df = df[df["y_date"] <= train_end_dt].copy()
        test_df = df[df["y_date"] > train_end_dt].copy()
        if len(train_df) < self.config.min_train_rows:
            n = len(df)
            split_idx = int(n * 0.8)
            if split_idx < self.config.min_train_rows:
                split_idx = self.config.min_train_rows
            if split_idx >= n:
                raise ValueError(
                    f"Za mało danych treningowych po cięciu: {len(train_df)} wierszy. "
                    f"Zakres y_date: {df['y_date'].min()} – {df['y_date'].max()}. "
                    f"train_end={self.config.train_end}. Ustaw train_end w zakresie danych "
                    f"lub dodaj dane historyczne."
                )
            train_df = df.iloc[:split_idx].copy()
            test_df = df.iloc[split_idx:].copy()
        if len(test_df) == 0:
            raise ValueError("Test ma 0 wierszy. Sprawdź train_end albo zakres danych.")
        return train_df, test_df

    def _get_feature_columns(self, df: pd.DataFrame) -> list[str]:
        base = [c for c in self.config.base_features if c in df.columns]
        feature_cols = base + ["month_sin", "month_cos"]
        for c in df.columns:
            if c.endswith("_lag1") or c.endswith("_lag2") or c.endswith("_lag3"):
                feature_cols.append(c)
        seen = set()
        return [c for c in feature_cols if not (c in seen or seen.add(c))]

    def _prepare_features_only(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        date_col = None
        for c in df.columns:
            if c.strip().lstrip("\ufeff") == "Data":
                date_col = c
                break
        if date_col is None:
            raise ValueError("Brak kolumny 'Data'.")
        if date_col != "Data":
            df = df.rename(columns={date_col: "Data"})
        if isinstance(df["Data"], pd.DataFrame):
            df["Data"] = df["Data"].iloc[:, 0]
        raw_dates = df["Data"].astype(str).str.strip()
        df["Data"] = pd.to_datetime(raw_dates, errors="coerce")
        still_na = df["Data"].isna()
        if still_na.any():
            df.loc[still_na, "Data"] = pd.to_datetime(
                raw_dates[still_na], format="%d.%m.%Y", dayfirst=True, errors="coerce"
            )
        df = df.dropna(subset=["Data"]).sort_values("Data").reset_index(drop=True)
        for c in df.columns:
            if c.strip().lstrip("\ufeff") == "Data" or pd.api.types.is_datetime64_any_dtype(df[c]):
                continue
            df[c] = _to_float_series(df[c])
        df = _add_time_features(df)
        lag_cols = [c for c in self.config.lag_columns if c in df.columns]
        df = _add_lags(df, cols=lag_cols, lags=self.config.lags)
        return df

    def _build_feature_matrix(
        self, df: pd.DataFrame, feature_cols: Optional[list[str]] = None
    ) -> tuple[pd.DataFrame, pd.Series]:
        if feature_cols is None:
            feature_cols = self._get_feature_columns(df)
        X = df[feature_cols].copy()
        y = df["y_next"].copy()
        return X, y

    def train(self, mode: str = "full") -> dict[str, float]:
        if self._df_raw is None:
            self.load_data()
        df = self.prepare_dataset()
        self._train_df, self._test_df = self._split(df)
        feature_cols = self._get_feature_columns(self._train_df)
        X_train, y_train = self._build_feature_matrix(self._train_df, feature_cols)
        self._feature_cols = feature_cols
        self._model = HistGradientBoostingRegressor(**self.config.model_kwargs)
        self._model.fit(X_train, y_train)
        if self.config.constraints is not None and self._df_raw is not None:
            self._max_level = _compute_max_level(
                self._df_raw, self.config.constraints
            )
        self._model_path.parent.mkdir(parents=True, exist_ok=True)
        last_level: Optional[float] = None
        if self.config.target_col != self.config.level_col:
            last_level = float(
                self._train_df.iloc[-1][self.config.level_col]
                + self._train_df.iloc[-1]["y_next"]
            )
        artifact = {
            "model": self._model,
            "feature_cols": self._feature_cols,
            "train_end": self.config.train_end,
            "target": f"{self.config.target_col}(t+1)",
            "target_col": self.config.target_col,
            "level_col": self.config.level_col,
            "last_level": last_level,
            "constraints": self.config.constraints,
            "max_level": self._max_level,
            "data_columns": list(self._df_raw.columns) if self._df_raw is not None else [],
        }
        joblib.dump(artifact, self._model_path)
        pred_train = self._model.predict(X_train)
        rmse = float(np.sqrt(mean_squared_error(y_train.values, pred_train)))
        mae = float(mean_absolute_error(y_train.values, pred_train))
        r2 = float(r2_score(y_train.values, pred_train))
        return {"rmse": rmse, "mae": mae, "r2": r2}

    def predict(
        self,
        horizon_months: int = 12,
        future_features_df: Optional[pd.DataFrame] = None,
    ) -> np.ndarray:
        if self._model is None or self._feature_cols is None:
            artifact_path = self._model_path
            if not artifact_path.exists():
                raise RuntimeError(
                    f"Model nie wytrenowany i brak pliku: {artifact_path}"
                )
            artifact = joblib.load(artifact_path)
            self._model = artifact["model"]
            self._feature_cols = artifact["feature_cols"]
            self._max_level = artifact.get("max_level")
        target_col = self.config.target_col
        level_col = self.config.level_col
        last_level = None
        if self._model_path.exists():
            art = joblib.load(self._model_path)
            target_col = art.get("target_col", target_col)
            level_col = art.get("level_col", level_col)
            last_level = art.get("last_level")
        def _to_levels(raw: np.ndarray) -> np.ndarray:
            if target_col == level_col or last_level is None:
                return raw
            levels = last_level + np.cumsum(raw.astype(float))
            if self.config.constraints is not None and self._max_level is not None:
                levels = np.array(
                    [
                        _apply_constraints(
                            float(L), self._max_level, self.config.constraints
                        )
                        for L in levels
                    ],
                    dtype=float,
                )
            return levels
        if future_features_df is not None:
            prep = self._prepare_features_only(future_features_df)
            cols = [c for c in self._feature_cols if c in prep.columns]
            if len(cols) != len(self._feature_cols):
                raise ValueError(
                    f"future_features_df nie ma wszystkich cech. Brakuje: "
                    f"{set(self._feature_cols) - set(cols)}"
                )
            X = prep[self._feature_cols].dropna()
            if len(X) == 0:
                raise ValueError("Po przygotowaniu cech brak kompletnych wierszy.")
            pred = self._model.predict(X)
            pred = _to_levels(pred) if target_col != level_col else pred
            if target_col == level_col and self.config.constraints is not None and self._max_level is not None:
                pred = np.array(
                    [
                        _apply_constraints(
                            p, self._max_level, self.config.constraints
                        )
                        for p in pred
                    ],
                    dtype=float,
                )
            return pred[:horizon_months] if len(pred) > horizon_months else pred
        if self._test_df is None:
            if self._df_raw is None:
                self.load_data()
            self.prepare_dataset()
            self._train_df, self._test_df = self._split(self._df_prepared)
        if last_level is None and target_col != level_col:
            last_level = float(
                self._train_df.iloc[-1][level_col] + self._train_df.iloc[-1]["y_next"]
            )
        X_test, _ = self._build_feature_matrix(self._test_df)
        pred = self._model.predict(X_test)
        pred = _to_levels(pred) if target_col != level_col else pred
        if target_col == level_col and self.config.constraints is not None and self._max_level is not None:
            pred = np.array(
                [
                    _apply_constraints(
                        p, self._max_level, self.config.constraints
                    )
                    for p in pred
                ],
                dtype=float,
            )
        return pred[:horizon_months] if len(pred) > horizon_months else pred

    def evaluate(self, horizon_months: int = 24) -> dict[str, float]:
        if self._test_df is None:
            if self._df_raw is None:
                self.load_data()
            self.prepare_dataset()
            self._train_df, self._test_df = self._split(self._df_prepared)
        subset = self._test_df.head(horizon_months)
        if len(subset) == 0:
            return {"rmse": float("nan"), "mae": float("nan"), "r2": float("nan")}
        X, y = self._build_feature_matrix(subset)
        if self._model is None:
            artifact = joblib.load(self._model_path)
            self._model = artifact["model"]
            self._feature_cols = artifact["feature_cols"]
            self._max_level = artifact.get("max_level")
        pred = self._model.predict(X)
        target_col = self.config.target_col
        level_col = self.config.level_col
        if self._model_path.exists():
            art = joblib.load(self._model_path)
            target_col = art.get("target_col", target_col)
            level_col = art.get("level_col", level_col)
        if target_col == level_col and self.config.constraints is not None and self._max_level is not None:
            pred = np.array(
                [
                    _apply_constraints(
                        p, self._max_level, self.config.constraints
                    )
                    for p in pred
                ],
                dtype=float,
            )
        return {
            "rmse": float(np.sqrt(mean_squared_error(y.values, pred))),
            "mae": float(mean_absolute_error(y.values, pred)),
            "r2": float(r2_score(y.values, pred)),
        }

    def get_future_data(self, horizon_months: int = 12) -> pd.DataFrame:
        if self._df_raw is None:
            self.load_data()
        df = self.prepare_dataset()
        last = df.iloc[-1:].copy()
        if horizon_months <= 1:
            return last
        last_date = last["Data"].iloc[0]
        rows = [last]
        for i in range(1, horizon_months):
            next_date = last_date + pd.DateOffset(months=i)
            row = last.iloc[0].to_dict()
            row["Data"] = next_date
            rows.append(pd.DataFrame([row]))
        out = pd.concat(rows, ignore_index=True)
        out["y_date"] = out["Data"] + pd.DateOffset(months=1)
        out["y_next_poziom"] = np.nan
        return out

    def _save_full_history_chart(self) -> None:
        if self._df_prepared is None:
            if self._df_raw is None:
                self.load_data()
            self.prepare_dataset()
        if self._model is None or self._feature_cols is None:
            if not self._model_path.exists():
                return
            artifact = joblib.load(self._model_path)
            self._model = artifact["model"]
            self._feature_cols = artifact["feature_cols"]
            self._max_level = artifact.get("max_level")
        df = self._df_prepared
        X, y = self._build_feature_matrix(df)
        valid = X.notna().all(axis=1)
        if valid.sum() == 0:
            return
        X_valid = X.loc[valid]
        y_valid = y.loc[valid]
        dates_valid = df.loc[valid, "y_date"]
        pred = self._model.predict(X_valid)
        target_col = self.config.target_col
        level_col = self.config.level_col
        if self._model_path.exists():
            art = joblib.load(self._model_path)
            target_col = art.get("target_col", target_col)
            level_col = art.get("level_col", level_col)
        if target_col != level_col:
            y_plot = (df.loc[valid, level_col] + df.loc[valid, "y_next"]).values
            first_idx = X_valid.index[0]
            initial_level = float(df.loc[first_idx, level_col])
            pred_levels = initial_level + np.cumsum(pred.astype(float))
            if self.config.constraints is not None and self._max_level is not None:
                pred_levels = np.array(
                    [
                        _apply_constraints(
                            float(L), self._max_level, self.config.constraints
                        )
                        for L in pred_levels
                    ],
                    dtype=float,
                )
            pred = pred_levels
        else:
            y_plot = y_valid.values
            if self.config.constraints is not None and self._max_level is not None:
                pred = np.array(
                    [
                        _apply_constraints(
                            p, self._max_level, self.config.constraints
                        )
                        for p in pred
                    ],
                    dtype=float,
                )
        train_end_dt = pd.to_datetime(self.config.train_end)
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.plot(dates_valid, y_plot, label="Rzeczywisty", color="tab:blue", alpha=0.9)
        ax.plot(dates_valid, pred, label="Model", color="tab:orange", alpha=0.9)
        ax.axvline(x=train_end_dt, color="gray", linestyle="--", linewidth=1.5, label="Koniec treningu")
        ax.set_xlabel("Data")
        ax.set_ylabel("Poziom [m]")
        ax.set_title(f"{self.config.name}: poziom rzeczywisty vs model (cała oś czasu)")
        ax.legend(loc="best")
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        self._reports_dir.mkdir(parents=True, exist_ok=True)
        path = self._reports_dir / "poziom_rzeczywisty_vs_model.png"
        fig.savefig(path, dpi=150)
        plt.close(fig)

    def generate_report(
        self,
        horizon_months: int = 12,
        future_features_df: Optional[pd.DataFrame] = None,
        save_png: bool = True,
        save_csv: bool = True,
    ) -> None:
        self._reports_dir.mkdir(parents=True, exist_ok=True)
        if save_png:
            self._save_full_history_chart()
        pred = self.predict(
            horizon_months=horizon_months,
            future_features_df=future_features_df,
        )
        if future_features_df is not None:
            prep = self._prepare_features_only(future_features_df)
            dates = (prep["Data"] + pd.DateOffset(months=1)).values[: len(pred)]
            out = pd.DataFrame({
                "y_date": dates,
                "pred_next_poziom": pred,
            })
        else:
            if self._test_df is None:
                if self._df_raw is None:
                    self.load_data()
                self.prepare_dataset()
                self._train_df, self._test_df = self._split(self._df_prepared)
            test_sub = self._test_df.head(horizon_months)
            if len(test_sub) == 0:
                return
            if self.config.target_col != self.config.level_col:
                real_level = (test_sub[self.config.level_col] + test_sub["y_next"]).values
            else:
                real_level = test_sub["y_next"].values
            out = pd.DataFrame({
                "y_date": test_sub["y_date"].values,
                "y_next_poziom": real_level,
                "pred_next_poziom": pred[: len(test_sub)],
            })
        if save_csv:
            csv_path = self._reports_dir / "predictions.csv"
            out.to_csv(csv_path, index=False)
        if save_png and len(out) > 0:
            fig, ax = plt.subplots(figsize=(12, 5))
            if "y_next_poziom" in out.columns:
                ax.plot(out["y_date"], out["y_next_poziom"], label="Rzeczywisty", color="tab:blue", alpha=0.9)
            ax.plot(out["y_date"], out["pred_next_poziom"], label="Predykcja", color="tab:orange", alpha=0.9)
            ax.set_xlabel("Data")
            ax.set_ylabel("Poziom [m]")
            ax.set_title(f"{self.config.name}: poziom rzeczywisty vs predykowany")
            ax.legend(loc="best")
            ax.grid(True, alpha=0.3)
            fig.tight_layout()
            png_path = self._reports_dir / "historia_prognoza.png"
            fig.savefig(png_path, dpi=150)
            plt.close(fig)
