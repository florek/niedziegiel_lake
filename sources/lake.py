import importlib.util
import pickle
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.ensemble import (
    GradientBoostingRegressor,
    HistGradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import TimeSeriesSplit

_LAKE_DIR = Path(__file__).resolve().parent
ROOT = _LAKE_DIR.parent if not (_LAKE_DIR / "data").exists() else _LAKE_DIR
DATA_DIR = ROOT / "data"
CONFIG_LAKES_DIR = ROOT / "config" / "lakes"
LAKES = {}
MAX_POZIOM_SPIETRZANIA_BY_LAKE = {}

ODPLYW_M_MIN = 0.2
ODPLYW_M_MAX = 1.0
ODPLYW_FRAC_RANGE = 0.05
PRZESACZANIE_DEFAULT_M = 0.01


def get_max_poziom(lake_id: str, df=None):
    cap = MAX_POZIOM_SPIETRZANIA_BY_LAKE.get(lake_id)
    if cap is not None:
        return float(cap)
    if df is not None:
        return float((df[COL_POZIOM] + df[COL_ZMIANA]).max())
    return None


def get_drainage_params(lake_id: str, df):
    max_poziom = get_max_poziom(lake_id, df)
    if max_poziom is None:
        return None, None, None
    poziom_koniec = df[COL_POZIOM] + df[COL_ZMIANA]
    level_max = float(poziom_koniec.max())
    level_min = float(df[COL_POZIOM].min())
    range_m = level_max - level_min
    odplyw_m = max(ODPLYW_M_MIN, min(ODPLYW_M_MAX, range_m * ODPLYW_FRAC_RANGE))
    zone_mask = poziom_koniec >= (max_poziom - odplyw_m)
    if zone_mask.sum() == 0:
        przesaczanie_m = PRZESACZANIE_DEFAULT_M
    else:
        mean_zmiana = float(df.loc[zone_mask, COL_ZMIANA].mean())
        przesaczanie_m = max(PRZESACZANIE_DEFAULT_M, -mean_zmiana) if mean_zmiana < 0 else PRZESACZANIE_DEFAULT_M
    return max_poziom, odplyw_m, przesaczanie_m


def apply_cap_and_drainage(poziom: float, max_poziom: float, odplyw_m: float, przesaczanie_m: float) -> float:
    if max_poziom is None:
        return poziom
    poziom = min(poziom, max_poziom)
    if odplyw_m is not None and przesaczanie_m is not None and poziom > max_poziom - odplyw_m:
        poziom = poziom - przesaczanie_m
    return poziom


def get_data_path(lake_id: str) -> Path:
    return DATA_DIR / lake_id / "data.csv"


def get_model_path(lake_id: str, variant: str | None = None) -> Path:
    if variant == "natural":
        return DATA_DIR / lake_id / "model_natural.pkl"
    return DATA_DIR / lake_id / "model.pkl"

COL_DATA = "Data"
COL_OPAD = "Opad"
COL_POZIOM = "Poziom"
COL_TEMPERATURA = "Temperatura"
COL_ZMIANA = "Zmiana"

LAG_MONTHS = 3
LAG_MONTHS_BY_LAKE = {}
METEO_LAG_FIBONACCI = [0, 1, 2, 3, 5, 8, 13]
METEO_LAG_CANDIDATES_BY_LAKE = {}


def load_data(path=None):
    if path is None:
        path = get_data_path("niedziegiel")
    df = pd.read_csv(path, sep=",", decimal=",")
    df[COL_DATA] = pd.to_datetime(df[COL_DATA], format="%d.%m.%Y", dayfirst=True)
    for col in (COL_POZIOM, COL_ZMIANA, COL_OPAD, COL_TEMPERATURA):
        df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", ".", regex=False), errors="coerce")
    df = df.dropna(subset=[COL_ZMIANA, COL_POZIOM, COL_OPAD, COL_TEMPERATURA])
    df = df[~df[COL_ZMIANA].astype(str).str.contains("ERROR", na=False)]
    return df.sort_values(COL_DATA).reset_index(drop=True)


def _add_lags(df, lag_months):
    for lag in range(1, lag_months + 1):
        df[f"zmiana_lag{lag}"] = df[COL_ZMIANA].shift(lag)
        df[f"poziom_lag{lag}"] = df[COL_POZIOM].shift(lag)
    return df


def _add_meteo_lags(df, meteo_lag_months):
    for lag in range(1, meteo_lag_months + 1):
        df[f"opad_lag{lag}"] = df[COL_OPAD].shift(lag)
        df[f"temperatura_lag{lag}"] = df[COL_TEMPERATURA].shift(lag)
    return df


def build_features(df, lag_months=None, meteo_lag_months=None):
    lag_months = lag_months if lag_months is not None else LAG_MONTHS
    meteo_lag_months = meteo_lag_months if meteo_lag_months is not None else 0
    df = df.copy()
    df["month"] = df[COL_DATA].dt.month
    df["month_sin"] = np.sin(2 * np.pi * df["month"] / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["month"] / 12)
    if meteo_lag_months > 0:
        df = _add_meteo_lags(df, meteo_lag_months)
    df = _add_lags(df, lag_months)
    return df


def get_feature_columns(lag_months=None, meteo_lag_months=None):
    lag_months = lag_months if lag_months is not None else LAG_MONTHS
    meteo_lag_months = meteo_lag_months if meteo_lag_months is not None else 0
    base = ["month_sin", "month_cos", COL_OPAD, COL_TEMPERATURA]
    if meteo_lag_months > 0:
        for lag in range(1, meteo_lag_months + 1):
            base.extend([f"opad_lag{lag}", f"temperatura_lag{lag}"])
    for lag in range(1, lag_months + 1):
        base.extend([f"zmiana_lag{lag}", f"poziom_lag{lag}"])
    return base


def train_test_split_temporal(
    df,
    test_months=70,
    train_end_year=None,
    train_end_month=None,
    train_start_year=None,
    train_start_month=None,
    test_end_year=None,
):
    if train_end_year is not None:
        yr = df[COL_DATA].dt.year
        mo = df[COL_DATA].dt.month
        if train_end_month is not None:
            train_mask = (yr < train_end_year) | ((yr == train_end_year) & (mo <= train_end_month))
        else:
            train_mask = yr <= train_end_year
        if train_start_year is not None:
            if train_start_month is not None:
                start_mask = (yr > train_start_year) | ((yr == train_start_year) & (mo >= train_start_month))
            else:
                start_mask = yr >= train_start_year
            train_mask = train_mask & start_mask
        train_df = df[train_mask]
        test_df = df[~train_mask]
        if test_end_year is not None:
            test_df = test_df[test_df[COL_DATA].dt.year <= test_end_year]
        return train_df, test_df
    split_idx = len(df) - test_months
    return df.iloc[:split_idx], df.iloc[split_idx:] if split_idx < len(df) else df.iloc[:0]


TRAIN_START_YEAR_BY_LAKE = {}
TRAIN_START_MONTH_BY_LAKE = {}
TRAIN_END_YEAR_BY_LAKE = {}
TRAIN_END_MONTH_BY_LAKE = {}
TRAIN_END_NATURAL_YEAR_BY_LAKE = {}
TRAIN_END_NATURAL_MONTH_BY_LAKE = {}
ROK_ZMIANY_REZIMU_BY_LAKE = {}
TEST_END_YEAR_BY_LAKE = {}


def _load_lake_configs() -> None:
    for path in sorted(CONFIG_LAKES_DIR.glob("*.py")):
        if path.stem == "__init__":
            continue
        lake_id = path.stem
        spec = importlib.util.spec_from_file_location(
            f"lake_config_{lake_id}",
            path,
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        cfg = mod.CONFIG
        LAKES[lake_id] = cfg["name"]
        MAX_POZIOM_SPIETRZANIA_BY_LAKE[lake_id] = cfg.get("max_poziom_spietrzania")
        LAG_MONTHS_BY_LAKE[lake_id] = cfg.get("lag_months", LAG_MONTHS)
        METEO_LAG_CANDIDATES_BY_LAKE[lake_id] = cfg.get(
            "meteo_lag_candidates",
            METEO_LAG_FIBONACCI,
        )
        TRAIN_START_YEAR_BY_LAKE[lake_id] = cfg["train_start_year"]
        TRAIN_START_MONTH_BY_LAKE[lake_id] = cfg["train_start_month"]
        TRAIN_END_YEAR_BY_LAKE[lake_id] = cfg["train_end_year"]
        TRAIN_END_MONTH_BY_LAKE[lake_id] = cfg["train_end_month"]
        TRAIN_END_NATURAL_YEAR_BY_LAKE[lake_id] = cfg["train_end_natural_year"]
        TRAIN_END_NATURAL_MONTH_BY_LAKE[lake_id] = cfg["train_end_natural_month"]
        ROK_ZMIANY_REZIMU_BY_LAKE[lake_id] = cfg["rok_zmiany_rezimu"]
        TEST_END_YEAR_BY_LAKE[lake_id] = cfg["test_end_year"]


_load_lake_configs()


def _get_candidate_models():
    return [
        (
            "HistGradientBoosting_early_stop",
            HistGradientBoostingRegressor(
                max_iter=600,
                max_depth=7,
                learning_rate=0.03,
                min_samples_leaf=5,
                l2_regularization=0.12,
                early_stopping=True,
                validation_fraction=0.15,
                n_iter_no_change=18,
                random_state=42,
            ),
        ),
        (
            "HistGradientBoosting_MAE",
            HistGradientBoostingRegressor(
                max_iter=600,
                max_depth=7,
                learning_rate=0.03,
                min_samples_leaf=5,
                l2_regularization=0.12,
                loss="absolute_error",
                early_stopping=True,
                validation_fraction=0.15,
                n_iter_no_change=18,
                random_state=42,
            ),
        ),
        (
            "GradientBoosting_reg",
            GradientBoostingRegressor(
                n_estimators=150,
                max_depth=5,
                learning_rate=0.04,
                min_samples_leaf=4,
                subsample=0.85,
                random_state=42,
            ),
        ),
        (
            "RandomForest",
            RandomForestRegressor(
                n_estimators=200,
                max_depth=8,
                min_samples_leaf=3,
                max_features="sqrt",
                random_state=42,
            ),
        ),
        (
            "GradientBoosting_legacy",
            GradientBoostingRegressor(
                n_estimators=150,
                max_depth=5,
                learning_rate=0.05,
                min_samples_leaf=3,
                random_state=42,
            ),
        ),
        (
            "HistGradientBoosting_deeper",
            HistGradientBoostingRegressor(
                max_iter=700,
                max_depth=8,
                learning_rate=0.025,
                min_samples_leaf=4,
                l2_regularization=0.08,
                early_stopping=True,
                validation_fraction=0.15,
                n_iter_no_change=20,
                random_state=42,
            ),
        ),
        (
            "GradientBoosting_strong",
            GradientBoostingRegressor(
                n_estimators=220,
                max_depth=6,
                learning_rate=0.035,
                min_samples_leaf=4,
                subsample=0.8,
                random_state=42,
            ),
        ),
    ]


def train_model(
    df=None,
    path=None,
    lake_id=None,
    train_end_year_override: int | None = None,
    train_end_month_override: int | None = None,
):
    if path is None:
        path = get_data_path("niedziegiel")
    if lake_id is None:
        for lid, p in [(k, get_data_path(k)) for k in LAKES]:
            if p == path:
                lake_id = lid
                break
        lake_id = lake_id or "niedziegiel"
    if df is None:
        df = load_data(path)
    lag_months = LAG_MONTHS_BY_LAKE.get(lake_id, LAG_MONTHS)
    train_end_year = train_end_year_override if train_end_year_override is not None else TRAIN_END_YEAR_BY_LAKE.get(lake_id)
    train_end_month = train_end_month_override if train_end_month_override is not None else TRAIN_END_MONTH_BY_LAKE.get(lake_id)
    train_start_year = None if train_end_year_override is not None else TRAIN_START_YEAR_BY_LAKE.get(lake_id)
    train_start_month = None if train_end_year_override is not None else TRAIN_START_MONTH_BY_LAKE.get(lake_id)
    test_end_year = TEST_END_YEAR_BY_LAKE.get(lake_id)
    meteo_candidates = METEO_LAG_CANDIDATES_BY_LAKE.get(lake_id, [0])
    lag_months_candidates = sorted(set([lag_months, min(7, lag_months + 2)]))
    best_mae_global = np.inf
    best_model = None
    best_feature_cols = None
    best_name = None
    best_meteo_lag = 0
    best_lag_months = lag_months
    for lag_m in lag_months_candidates:
        for meteo_lag_months in meteo_candidates:
            df_f = build_features(df.copy(), lag_months=lag_m, meteo_lag_months=meteo_lag_months)
            df_f = df_f.dropna()
            feature_cols = get_feature_columns(lag_months=lag_m, meteo_lag_months=meteo_lag_months)
            train_df, test_df = train_test_split_temporal(
                df_f,
                train_end_year=train_end_year,
                train_end_month=train_end_month,
                train_start_year=train_start_year,
                train_start_month=train_start_month,
                test_end_year=test_end_year,
            )
            if len(train_df) < 15:
                continue
            X_train = train_df[feature_cols]
            y_train = train_df[COL_ZMIANA]
            X_test = test_df[feature_cols] if len(test_df) > 0 else None
            y_test = test_df[COL_ZMIANA].values if len(test_df) > 0 else None
            n_splits = min(5, max(2, (len(train_df) - 12) // 24))
            if n_splits < 2:
                n_splits = 2
            tscv = TimeSeriesSplit(n_splits=n_splits)
            ranked = []
            for name, candidate in _get_candidate_models():
                maes = []
                for train_idx, val_idx in tscv.split(X_train):
                    c = clone(candidate)
                    c.fit(X_train.iloc[train_idx], y_train.iloc[train_idx])
                    pred = c.predict(X_train.iloc[val_idx])
                    maes.append(mean_absolute_error(y_train.iloc[val_idx].values, pred))
                mean_mae = float(np.mean(maes))
                ranked.append((mean_mae, name, candidate))
            ranked.sort(key=lambda x: x[0])
            best_mae = ranked[0][0]
            best_cand = ranked[0][2]
            best_cand_name = ranked[0][1]
            second_cand = ranked[1][2] if len(ranked) > 1 else None
            if best_mae < best_mae_global:
                best_mae_global = best_mae
                best_models = [clone(best_cand)]
                if second_cand is not None:
                    best_models.append(clone(second_cand))
                for m in best_models:
                    m.fit(X_train, y_train)
                best_model = best_models
                best_feature_cols = feature_cols
                best_name = best_cand_name + ("+ensemble" if len(best_models) > 1 else "")
                best_meteo_lag = meteo_lag_months
                best_lag_months = lag_m
    if best_model is None:
        best_meteo_lag = meteo_candidates[0]
        best_lag_months = lag_months
        df_f = build_features(
            df.copy(),
            lag_months=best_lag_months,
            meteo_lag_months=best_meteo_lag,
        )
        df_f = df_f.dropna()
        best_feature_cols = get_feature_columns(
            lag_months=best_lag_months,
            meteo_lag_months=best_meteo_lag,
        )
        train_df, test_df = train_test_split_temporal(
            df_f,
            train_end_year=train_end_year,
            train_end_month=train_end_month,
            train_start_year=train_start_year,
            train_start_month=train_start_month,
            test_end_year=test_end_year,
        )
        if len(train_df) < 10:
            raise ValueError("Za mało danych do treningu po podziale czasowym.")
        best_model = [clone(_get_candidate_models()[0][1])]
        best_model[0].fit(train_df[best_feature_cols], train_df[COL_ZMIANA])
        best_name = _get_candidate_models()[0][0]
    metrics = {}
    df_final = build_features(df.copy(), lag_months=best_lag_months, meteo_lag_months=best_meteo_lag)
    df_final = df_final.dropna()
    train_df, test_df = train_test_split_temporal(
        df_final,
        train_end_year=train_end_year,
        train_end_month=train_end_month,
        train_start_year=train_start_year,
        train_start_month=train_start_month,
        test_end_year=test_end_year,
    )
    X_test = test_df[best_feature_cols] if len(test_df) > 0 else None
    y_test = test_df[COL_ZMIANA].values if len(test_df) > 0 else None
    if X_test is not None and y_test is not None:
        preds = np.array([m.predict(X_test) for m in best_model])
        y_pred = np.mean(preds, axis=0)
        metrics["test_mae"] = mean_absolute_error(y_test, y_pred)
        metrics["test_rmse"] = np.sqrt(mean_squared_error(y_test, y_pred))
        metrics["best_model"] = best_name
        metrics["meteo_lag_months"] = best_meteo_lag
    return best_model, best_feature_cols, metrics, best_lag_months, best_meteo_lag


def evaluate_model(model, df, feature_cols):
    X = df[feature_cols]
    y = df[COL_ZMIANA]
    models = model if isinstance(model, list) else [model]
    preds = np.array([m.predict(X) for m in models])
    y_pred = np.mean(preds, axis=0)
    return {
        "mae": mean_absolute_error(y, y_pred),
        "rmse": np.sqrt(mean_squared_error(y, y_pred)),
    }


def predict_change(
    model,
    feature_cols,
    poziom,
    opad,
    temperatura,
    month,
    last_changes=None,
    last_poziomy=None,
    last_opady=None,
    last_temperatury=None,
    lag_months=None,
    meteo_lag_months=None,
):
    lag_months = lag_months if lag_months is not None else LAG_MONTHS
    meteo_lag_months = meteo_lag_months if meteo_lag_months is not None else 0
    month_sin = np.sin(2 * np.pi * month / 12)
    month_cos = np.cos(2 * np.pi * month / 12)
    row = {
        "month_sin": month_sin,
        "month_cos": month_cos,
        COL_OPAD: opad,
        COL_TEMPERATURA: temperatura,
    }
    if meteo_lag_months > 0:
        for lag in range(1, meteo_lag_months + 1):
            row[f"opad_lag{lag}"] = (
                last_opady[-(lag)] if last_opady and len(last_opady) >= lag else opad
            )
            row[f"temperatura_lag{lag}"] = (
                last_temperatury[-(lag)] if last_temperatury and len(last_temperatury) >= lag else temperatura
            )
    for lag in range(1, lag_months + 1):
        row[f"zmiana_lag{lag}"] = (last_changes[-(lag)] if last_changes and len(last_changes) >= lag else 0.0)
        row[f"poziom_lag{lag}"] = (last_poziomy[-(lag)] if last_poziomy and len(last_poziomy) >= lag else poziom)
    for col in feature_cols:
        if col not in row:
            row[col] = 0.0
    X = pd.DataFrame([row])[feature_cols]
    models = model if isinstance(model, list) else [model]
    return float(np.mean([m.predict(X)[0] for m in models]))


def save_model(model, feature_cols, path=None, lag_months=None, meteo_lag_months=None):
    if path is None:
        path = get_model_path("niedziegiel")
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"model": model, "feature_cols": feature_cols}
    if lag_months is not None:
        payload["lag_months"] = lag_months
    if meteo_lag_months is not None:
        payload["meteo_lag_months"] = meteo_lag_months
    with open(path, "wb") as f:
        pickle.dump(payload, f)


def load_model(path=None):
    if path is None:
        path = get_model_path("niedziegiel")
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Brak pliku modelu: {path}")
    with open(path, "rb") as f:
        data = pickle.load(f)
    lag_months = data.get("lag_months", LAG_MONTHS)
    meteo_lag_months = data.get("meteo_lag_months", 0)
    return data["model"], data["feature_cols"], lag_months, meteo_lag_months


def run_training_and_save(lake_id: str = "niedziegiel", variant: str | None = None):
    data_path = get_data_path(lake_id)
    if variant == "natural":
        model_path = get_model_path(lake_id, variant="natural")
        train_end_year = TRAIN_END_NATURAL_YEAR_BY_LAKE.get(lake_id)
        train_end_month = TRAIN_END_NATURAL_MONTH_BY_LAKE.get(lake_id)
    else:
        model_path = get_model_path(lake_id)
        train_end_year = None
        train_end_month = None
    if not data_path.exists():
        raise FileNotFoundError(f"Brak pliku danych: {data_path}")
    df = load_data(data_path)
    model, feature_cols, metrics, lag_months, meteo_lag_months = train_model(
        df=df,
        path=data_path,
        lake_id=lake_id,
        train_end_year_override=train_end_year,
        train_end_month_override=train_end_month,
    )
    save_model(
        model,
        feature_cols,
        path=model_path,
        lag_months=lag_months,
        meteo_lag_months=meteo_lag_months,
    )
    name = LAKES.get(lake_id, lake_id)
    best = metrics.get("best_model", "—")
    meteo_lag = metrics.get("meteo_lag_months", meteo_lag_months)
    suf = " (naturalny)" if variant == "natural" else ""
    print(
        f"Model wytrenowany ({name}){suf}. Wybór: {best}. Opóźnienie meteo: {meteo_lag} mies. "
        f"Test MAE: {metrics.get('test_mae', 'N/A'):.4f}, RMSE: {metrics.get('test_rmse', 'N/A'):.4f}"
    )
    return model, feature_cols


if __name__ == "__main__":
    lake_id = sys.argv[1] if len(sys.argv) > 1 else "niedziegiel"
    variant = "natural" if len(sys.argv) > 2 and sys.argv[2].lower() == "natural" else None
    if lake_id not in LAKES:
        print(f"Dostępne jeziora: {', '.join(LAKES)}")
        sys.exit(1)
    run_training_and_save(lake_id, variant=variant)
