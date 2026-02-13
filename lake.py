import pickle
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import (
    GradientBoostingRegressor,
    HistGradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.metrics import mean_absolute_error, mean_squared_error

DATA_DIR = Path(__file__).resolve().parent / "data"
LAKES = {"niedziegiel": "Jezioro Niedzięgiel", "powidzkie": "Jezioro Powidzkie"}


def get_data_path(lake_id: str) -> Path:
    return DATA_DIR / f"{lake_id}_data.csv"


def get_model_path(lake_id: str) -> Path:
    return DATA_DIR / f"{lake_id}_model.pkl"

COL_DATA = "Data"
COL_OPAD = "Opad"
COL_POZIOM = "Poziom"
COL_TEMPERATURA = "Temperatura"
COL_ZMIANA = "Zmiana"

LAG_MONTHS = 3


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


def _add_lags(df):
    for lag in range(1, LAG_MONTHS + 1):
        df[f"zmiana_lag{lag}"] = df[COL_ZMIANA].shift(lag)
        df[f"poziom_lag{lag}"] = df[COL_POZIOM].shift(lag)
    return df


def build_features(df):
    df = df.copy()
    df["month"] = df[COL_DATA].dt.month
    df["month_sin"] = np.sin(2 * np.pi * df["month"] / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["month"] / 12)
    df = _add_lags(df)
    return df


def get_feature_columns():
    base = ["month_sin", "month_cos", COL_OPAD, COL_TEMPERATURA]
    lags = []
    for lag in range(1, LAG_MONTHS + 1):
        lags.extend([f"zmiana_lag{lag}", f"poziom_lag{lag}"])
    return base + lags


def train_test_split_temporal(df, test_months=70, train_end_year=None, test_end_year=None):
    if train_end_year is not None:
        train_df = df[df[COL_DATA].dt.year <= train_end_year]
        test_df = df[df[COL_DATA].dt.year > train_end_year]
        if test_end_year is not None:
            test_df = test_df[test_df[COL_DATA].dt.year <= test_end_year]
        return train_df, test_df
    split_idx = len(df) - test_months
    return df.iloc[:split_idx], df.iloc[split_idx:] if split_idx < len(df) else df.iloc[:0]


TRAIN_END_YEAR_BY_LAKE = {"niedziegiel": 2010, "powidzkie": 2010}
TEST_END_YEAR_BY_LAKE = {"niedziegiel": 2023, "powidzkie": 2023}


def _get_candidate_models():
    return [
        (
            "HistGradientBoosting_early_stop",
            HistGradientBoostingRegressor(
                max_iter=200,
                max_depth=5,
                learning_rate=0.05,
                min_samples_leaf=10,
                l2_regularization=0.2,
                early_stopping=True,
                validation_fraction=0.15,
                n_iter_no_change=12,
                random_state=42,
            ),
        ),
        (
            "GradientBoosting_reg",
            GradientBoostingRegressor(
                n_estimators=80,
                max_depth=3,
                learning_rate=0.06,
                min_samples_leaf=8,
                subsample=0.85,
                random_state=42,
            ),
        ),
        (
            "RandomForest",
            RandomForestRegressor(
                n_estimators=120,
                max_depth=6,
                min_samples_leaf=5,
                max_features="sqrt",
                random_state=42,
            ),
        ),
        (
            "GradientBoosting_legacy",
            GradientBoostingRegressor(
                n_estimators=100,
                max_depth=4,
                learning_rate=0.08,
                min_samples_leaf=3,
                random_state=42,
            ),
        ),
    ]


def train_model(df=None, path=None, lake_id=None):
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
    df = build_features(df)
    df = df.dropna()
    feature_cols = get_feature_columns()
    train_end_year = TRAIN_END_YEAR_BY_LAKE.get(lake_id)
    test_end_year = TEST_END_YEAR_BY_LAKE.get(lake_id)
    train_df, test_df = train_test_split_temporal(
        df,
        train_end_year=train_end_year,
        test_end_year=test_end_year,
    )
    if len(train_df) < 10:
        raise ValueError("Za mało danych do treningu po podziale czasowym.")
    X_train = train_df[feature_cols]
    y_train = train_df[COL_ZMIANA]
    X_test = test_df[feature_cols] if len(test_df) > 0 else None
    y_test = test_df[COL_ZMIANA].values if len(test_df) > 0 else None
    best_mae = np.inf
    best_model = None
    best_name = None
    for name, candidate in _get_candidate_models():
        candidate.fit(X_train, y_train)
        if X_test is not None and y_test is not None:
            pred = candidate.predict(X_test)
            mae = mean_absolute_error(y_test, pred)
            if mae < best_mae:
                best_mae = mae
                best_model = candidate
                best_name = name
    if best_model is not None:
        model = best_model
    else:
        model = _get_candidate_models()[0][1]
        model.fit(X_train, y_train)
    metrics = {}
    if X_test is not None and y_test is not None:
        y_pred = model.predict(X_test)
        metrics["test_mae"] = mean_absolute_error(y_test, y_pred)
        metrics["test_rmse"] = np.sqrt(mean_squared_error(y_test, y_pred))
        metrics["best_model"] = best_name
    return model, feature_cols, metrics


def evaluate_model(model, df, feature_cols):
    X = df[feature_cols]
    y = df[COL_ZMIANA]
    y_pred = model.predict(X)
    return {
        "mae": mean_absolute_error(y, y_pred),
        "rmse": np.sqrt(mean_squared_error(y, y_pred)),
    }


def predict_change(model, feature_cols, poziom, opad, temperatura, month, last_changes=None, last_poziomy=None):
    month_sin = np.sin(2 * np.pi * month / 12)
    month_cos = np.cos(2 * np.pi * month / 12)
    row = {
        "month_sin": month_sin,
        "month_cos": month_cos,
        COL_OPAD: opad,
        COL_TEMPERATURA: temperatura,
    }
    for lag in range(1, LAG_MONTHS + 1):
        row[f"zmiana_lag{lag}"] = (last_changes[-(lag)] if last_changes and len(last_changes) >= lag else 0.0)
        row[f"poziom_lag{lag}"] = (last_poziomy[-(lag)] if last_poziomy and len(last_poziomy) >= lag else poziom)
    X = pd.DataFrame([row])[feature_cols]
    return float(model.predict(X)[0])


def save_model(model, feature_cols, path=None):
    if path is None:
        path = get_model_path("niedziegiel")
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump({"model": model, "feature_cols": feature_cols}, f)


def load_model(path=None):
    if path is None:
        path = get_model_path("niedziegiel")
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Brak pliku modelu: {path}")
    with open(path, "rb") as f:
        data = pickle.load(f)
    return data["model"], data["feature_cols"]


def run_training_and_save(lake_id: str = "niedziegiel"):
    data_path = get_data_path(lake_id)
    model_path = get_model_path(lake_id)
    if not data_path.exists():
        raise FileNotFoundError(f"Brak pliku danych: {data_path}")
    df = load_data(data_path)
    model, feature_cols, metrics = train_model(df=df, path=data_path, lake_id=lake_id)
    save_model(model, feature_cols, path=model_path)
    name = LAKES.get(lake_id, lake_id)
    best = metrics.get("best_model", "—")
    print(f"Model wytrenowany ({name}). Wybór: {best}. Test MAE: {metrics.get('test_mae', 'N/A'):.4f}, RMSE: {metrics.get('test_rmse', 'N/A'):.4f}")
    return model, feature_cols


if __name__ == "__main__":
    lake_id = sys.argv[1] if len(sys.argv) > 1 else "niedziegiel"
    if lake_id not in LAKES:
        print(f"Dostępne jeziora: {', '.join(LAKES)}")
        sys.exit(1)
    run_training_and_save(lake_id)
