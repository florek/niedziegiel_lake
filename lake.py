import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

DATA_PATH = Path(__file__).resolve().parent / "data" / "data.csv"
MODEL_PATH = Path(__file__).resolve().parent / "data" / "model.pkl"

COL_DATA = "Data"
COL_OPAD = "Opad"
COL_POZIOM = "Poziom"
COL_TEMPERATURA = "Temperatura"
COL_ZMIANA = "Zmiana"

LAG_MONTHS = 3


def load_data(path=DATA_PATH):
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


def train_test_split_temporal(df, test_months=70):
    split_idx = len(df) - test_months
    return df.iloc[:split_idx], df.iloc[split_idx:] if split_idx < len(df) else df.iloc[:0]


def train_model(df=None, path=DATA_PATH):
    if df is None:
        df = load_data(path)
    df = build_features(df)
    df = df.dropna()
    feature_cols = get_feature_columns()
    train_df, test_df = train_test_split_temporal(df, test_months=70)
    if len(train_df) < 10:
        raise ValueError("Za mało danych do treningu po podziale czasowym.")
    X_train = train_df[feature_cols]
    y_train = train_df[COL_ZMIANA]
    model = GradientBoostingRegressor(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.08,
        min_samples_leaf=3,
        random_state=42,
    )
    model.fit(X_train, y_train)
    metrics = {}
    if len(test_df) > 0:
        X_test = test_df[feature_cols]
        y_test = test_df[COL_ZMIANA]
        y_pred = model.predict(X_test)
        metrics["test_mae"] = mean_absolute_error(y_test, y_pred)
        metrics["test_rmse"] = np.sqrt(mean_squared_error(y_test, y_pred))
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


def save_model(model, feature_cols, path=MODEL_PATH):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump({"model": model, "feature_cols": feature_cols}, f)


def load_model(path=MODEL_PATH):
    with open(path, "rb") as f:
        data = pickle.load(f)
    return data["model"], data["feature_cols"]


def run_training_and_save():
    df = load_data()
    model, feature_cols, metrics = train_model(df=df)
    save_model(model, feature_cols)
    print(f"Model wytrenowany. Test MAE: {metrics.get('test_mae', 'N/A'):.4f}, RMSE: {metrics.get('test_rmse', 'N/A'):.4f}")
    return model, feature_cols


if __name__ == "__main__":
    run_training_and_save()
