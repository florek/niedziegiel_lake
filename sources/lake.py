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

_LAKE_DIR = Path(__file__).resolve().parent
ROOT = _LAKE_DIR.parent if not (_LAKE_DIR / "data").exists() else _LAKE_DIR
DATA_DIR = ROOT / "data"
LAKES = {
    "budzislawskie": "Jezioro Budzisławskie",
    "kozieglowskie": "Jezioro Koziegłowskie",
    "kownackie": "Jezioro Kownackie",
    "niedziegiel": "Jezioro Niedzięgiel",
    "ostrowskie": "Jezioro Ostrowskie",
    "powidzkie": "Jezioro Powidzkie",
    "skulskawies": "Jezioro Skulska Wieś",
    "suszewskie": "Jezioro Suszewskie",
    "wilczynskie": "Jezioro Wilczyńskie",
}


MAX_POZIOM_SPIETRZANIA_BY_LAKE = {
    "budzislawskie": 99.02,
    "kozieglowskie": 101.91,
    "kownackie": 97.50,
    "niedziegiel": 103.80,
    "ostrowskie": 98.66,
    "powidzkie": 98.79,
    "skulskawies": 86.49,
    "suszewskie": 98.94,
    "wilczynskie": 99.15,
}

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


def get_model_path(lake_id: str) -> Path:
    return DATA_DIR / lake_id / "model.pkl"

COL_DATA = "Data"
COL_OPAD = "Opad"
COL_POZIOM = "Poziom"
COL_TEMPERATURA = "Temperatura"
COL_ZMIANA = "Zmiana"

LAG_MONTHS = 3
LAG_MONTHS_BY_LAKE = {"budzislawskie": 3, "kozieglowskie": 3, "kownackie": 3, "niedziegiel": 3, "ostrowskie": 3, "powidzkie": 5, "skulskawies": 3, "suszewskie": 3, "wilczynskie": 3}
METEO_LAG_FIBONACCI = [0, 1, 2, 3, 5, 8, 13]
METEO_LAG_CANDIDATES_BY_LAKE = {
    "budzislawskie": METEO_LAG_FIBONACCI,
    "kozieglowskie": METEO_LAG_FIBONACCI,
    "kownackie": METEO_LAG_FIBONACCI,
    "niedziegiel": METEO_LAG_FIBONACCI,
    "ostrowskie": METEO_LAG_FIBONACCI,
    "powidzkie": METEO_LAG_FIBONACCI,
    "skulskawies": METEO_LAG_FIBONACCI,
    "suszewskie": METEO_LAG_FIBONACCI,
    "wilczynskie": METEO_LAG_FIBONACCI,
}


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
    test_end_year=None,
):
    if train_end_year is not None:
        yr = df[COL_DATA].dt.year
        mo = df[COL_DATA].dt.month
        if train_end_month is not None:
            train_mask = (yr < train_end_year) | ((yr == train_end_year) & (mo <= train_end_month))
        else:
            train_mask = yr <= train_end_year
        train_df = df[train_mask]
        test_df = df[~train_mask]
        if test_end_year is not None:
            test_df = test_df[test_df[COL_DATA].dt.year <= test_end_year]
        return train_df, test_df
    split_idx = len(df) - test_months
    return df.iloc[:split_idx], df.iloc[split_idx:] if split_idx < len(df) else df.iloc[:0]


TRAIN_END_YEAR_BY_LAKE = {"budzislawskie": 2003, "kozieglowskie": 2003, "kownackie": 2003, "niedziegiel": 2013, "ostrowskie": 2003, "powidzkie": 2013, "skulskawies": 2015, "suszewskie": 2003, "wilczynskie": 2003}
TRAIN_END_MONTH_BY_LAKE = {"budzislawskie": 2, "kozieglowskie": 2, "kownackie": 2, "niedziegiel": None, "ostrowskie": 2, "powidzkie": None, "skulskawies": None, "suszewskie": 2, "wilczynskie": 2}
TEST_END_YEAR_BY_LAKE = {"budzislawskie": 2023, "kozieglowskie": 2023, "kownackie": 2023, "niedziegiel": 2023, "ostrowskie": 2023, "powidzkie": 2023, "skulskawies": 2023, "suszewskie": 2023, "wilczynskie": 2023}


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
        (
            "HistGradientBoosting_deeper",
            HistGradientBoostingRegressor(
                max_iter=300,
                max_depth=6,
                learning_rate=0.04,
                min_samples_leaf=6,
                l2_regularization=0.15,
                early_stopping=True,
                validation_fraction=0.15,
                n_iter_no_change=15,
                random_state=42,
            ),
        ),
        (
            "GradientBoosting_strong",
            GradientBoostingRegressor(
                n_estimators=150,
                max_depth=5,
                learning_rate=0.05,
                min_samples_leaf=6,
                subsample=0.8,
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
    lag_months = LAG_MONTHS_BY_LAKE.get(lake_id, LAG_MONTHS)
    train_end_year = TRAIN_END_YEAR_BY_LAKE.get(lake_id)
    train_end_month = TRAIN_END_MONTH_BY_LAKE.get(lake_id)
    test_end_year = TEST_END_YEAR_BY_LAKE.get(lake_id)
    meteo_candidates = METEO_LAG_CANDIDATES_BY_LAKE.get(lake_id, [0])
    best_mae_global = np.inf
    best_model = None
    best_feature_cols = None
    best_name = None
    best_meteo_lag = 0
    for meteo_lag_months in meteo_candidates:
        df_f = build_features(df.copy(), lag_months=lag_months, meteo_lag_months=meteo_lag_months)
        df_f = df_f.dropna()
        feature_cols = get_feature_columns(lag_months=lag_months, meteo_lag_months=meteo_lag_months)
        train_df, test_df = train_test_split_temporal(
            df_f,
            train_end_year=train_end_year,
            train_end_month=train_end_month,
            test_end_year=test_end_year,
        )
        if len(train_df) < 10:
            continue
        X_train = train_df[feature_cols]
        y_train = train_df[COL_ZMIANA]
        X_test = test_df[feature_cols] if len(test_df) > 0 else None
        y_test = test_df[COL_ZMIANA].values if len(test_df) > 0 else None
        best_mae = np.inf
        best_cand = None
        best_cand_name = None
        for name, candidate in _get_candidate_models():
            candidate.fit(X_train, y_train)
            if X_test is not None and y_test is not None:
                pred = candidate.predict(X_test)
                mae = mean_absolute_error(y_test, pred)
                if mae < best_mae:
                    best_mae = mae
                    best_cand = candidate
                    best_cand_name = name
        if best_cand is not None and best_mae < best_mae_global:
            best_mae_global = best_mae
            best_model = best_cand
            best_feature_cols = feature_cols
            best_name = best_cand_name
            best_meteo_lag = meteo_lag_months
    if best_model is None:
        best_meteo_lag = meteo_candidates[0]
        df_f = build_features(
            df.copy(),
            lag_months=lag_months,
            meteo_lag_months=best_meteo_lag,
        )
        df_f = df_f.dropna()
        best_feature_cols = get_feature_columns(
            lag_months=lag_months,
            meteo_lag_months=best_meteo_lag,
        )
        train_df, test_df = train_test_split_temporal(
            df_f,
            train_end_year=train_end_year,
            train_end_month=train_end_month,
            test_end_year=test_end_year,
        )
        if len(train_df) < 10:
            raise ValueError("Za mało danych do treningu po podziale czasowym.")
        best_model = _get_candidate_models()[0][1]
        best_model.fit(train_df[best_feature_cols], train_df[COL_ZMIANA])
        best_name = _get_candidate_models()[0][0]
    metrics = {}
    df_final = build_features(df.copy(), lag_months=lag_months, meteo_lag_months=best_meteo_lag)
    df_final = df_final.dropna()
    train_df, test_df = train_test_split_temporal(
        df_final,
        train_end_year=train_end_year,
        train_end_month=train_end_month,
        test_end_year=test_end_year,
    )
    X_test = test_df[best_feature_cols] if len(test_df) > 0 else None
    y_test = test_df[COL_ZMIANA].values if len(test_df) > 0 else None
    if X_test is not None and y_test is not None:
        y_pred = best_model.predict(X_test)
        metrics["test_mae"] = mean_absolute_error(y_test, y_pred)
        metrics["test_rmse"] = np.sqrt(mean_squared_error(y_test, y_pred))
        metrics["best_model"] = best_name
        metrics["meteo_lag_months"] = best_meteo_lag
    return best_model, best_feature_cols, metrics, lag_months, best_meteo_lag


def evaluate_model(model, df, feature_cols):
    X = df[feature_cols]
    y = df[COL_ZMIANA]
    y_pred = model.predict(X)
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
    X = pd.DataFrame([row])[feature_cols]
    return float(model.predict(X)[0])


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


def run_training_and_save(lake_id: str = "niedziegiel"):
    data_path = get_data_path(lake_id)
    model_path = get_model_path(lake_id)
    if not data_path.exists():
        raise FileNotFoundError(f"Brak pliku danych: {data_path}")
    df = load_data(data_path)
    model, feature_cols, metrics, lag_months, meteo_lag_months = train_model(
        df=df,
        path=data_path,
        lake_id=lake_id,
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
    print(
        f"Model wytrenowany ({name}). Wybór: {best}. Opóźnienie meteo: {meteo_lag} mies. "
        f"Test MAE: {metrics.get('test_mae', 'N/A'):.4f}, RMSE: {metrics.get('test_rmse', 'N/A'):.4f}"
    )
    return model, feature_cols


if __name__ == "__main__":
    lake_id = sys.argv[1] if len(sys.argv) > 1 else "niedziegiel"
    if lake_id not in LAKES:
        print(f"Dostępne jeziora: {', '.join(LAKES)}")
        sys.exit(1)
    run_training_and_save(lake_id)
