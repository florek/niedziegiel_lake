import sys
from pathlib import Path

import lake

DOCS_DIR = Path(__file__).resolve().parent / "docs"


def run_evaluation(lake_id="niedziegiel", data_path=None, model_path=None, output_path=None):
    if output_path is None:
        output_path = DOCS_DIR / f"podsumowanie_ewaluacji_{lake_id}.md"
    data_path = data_path or lake.get_data_path(lake_id)
    model_path = model_path or lake.get_model_path(lake_id)
    model, feature_cols, lag_months, meteo_lag_months = lake.load_model(model_path)
    df = lake.load_data(data_path)
    df = lake.build_features(
        df,
        lag_months=lag_months,
        meteo_lag_months=meteo_lag_months,
    )
    df = df.dropna()
    if len(df) == 0:
        raise ValueError("Brak wierszy z pełnymi cechami.")
    train_end_year = lake.TRAIN_END_YEAR_BY_LAKE.get(lake_id)
    train_end_month = lake.TRAIN_END_MONTH_BY_LAKE.get(lake_id)
    test_mask = None
    if train_end_year is not None:
        yr = df[lake.COL_DATA].dt.year
        mo = df[lake.COL_DATA].dt.month
        if train_end_month is not None:
            test_mask = (yr > train_end_year) | ((yr == train_end_year) & (mo > train_end_month))
        else:
            test_mask = yr > train_end_year
        test_end_year = lake.TEST_END_YEAR_BY_LAKE.get(lake_id)
        if test_end_year is not None:
            test_mask = test_mask & (df[lake.COL_DATA].dt.year <= test_end_year)
    X = df[feature_cols]
    y_true = df[lake.COL_ZMIANA]
    y_pred = model.predict(X)
    errors = y_true.values - y_pred
    if test_mask is not None:
        mae = (abs(errors[test_mask])).mean()
        rmse = (errors[test_mask] ** 2).mean() ** 0.5
        n_test = test_mask.sum()
    else:
        mae = (abs(errors)).mean()
        rmse = (errors ** 2).mean() ** 0.5
        n_test = len(df)
    poziom_rzeczywisty_koniec = (df[lake.COL_POZIOM] + df[lake.COL_ZMIANA]).values
    poziom_model_koniec = []
    poziom_prev = float(df.iloc[0][lake.COL_POZIOM])
    max_poziom = lake.get_max_poziom(lake_id, df)
    for i in range(len(df)):
        poziom_prev = poziom_prev + float(y_pred[i])
        if max_poziom is not None:
            poziom_prev = min(poziom_prev, max_poziom)
        poziom_model_koniec.append(poziom_prev)
    rows = []
    for i in range(len(df)):
        row = df.iloc[i]
        rows.append({
            "data": row[lake.COL_DATA].strftime("%Y-%m"),
            "opad": round(row[lake.COL_OPAD], 1),
            "temperatura": round(row[lake.COL_TEMPERATURA], 1),
            "zmiana_fakt": round(row[lake.COL_ZMIANA], 4),
            "zmiana_prognoza": round(float(y_pred[i]), 4),
            "błąd": round(float(errors[i]), 4),
            "wysokosc_rzeczywista": round(float(poziom_rzeczywisty_koniec[i]), 3),
            "wysokosc_model": round(poziom_model_koniec[i], 3),
        })
    for i in range(len(rows)):
        rows[i]["rozbieznosc"] = round(rows[i]["wysokosc_rzeczywista"] - rows[i]["wysokosc_model"], 3)
    lake_name = lake.LAKES.get(lake_id, lake_id)
    content = _build_md(rows, mae, rmse, n_test, len(rows), lake_name)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    print(f"Podsumowanie zapisane: {output_path}")
    return mae, rmse, rows


def _build_md(rows, mae, rmse, n_test, n_all, lake_name="Jezioro"):
    lines = [
        f"# Podsumowanie ewaluacji prognozy zmiany poziomu {lake_name}",
        "",
        f"Dla każdego miesiąca model otrzymuje opad i temperaturę (oraz cechy opóźnione z historii), wylicza prognozowaną zmianę poziomu {lake_name} i jest ona porównana z faktyczną zmianą.",
        "",
        "## Metryki",
        "",
        f"- **MAE (średni błąd bezwzględny):** {mae:.4f} m",
        f"- **RMSE (pierwiastek błędu średniokwadratowego):** {rmse:.4f} m",
        f"- **Liczba miesięcy (zbior testowy):** {n_test}",
        f"- **Liczba miesięcy (tabela / wykres):** {n_all}",
        "",
        "## Porównanie miesięczne",
        "",
        "| Data | Opad (mm) | Temperatura (°C) | Zmiana faktyczna (m) | Zmiana prognoza (m) | Błąd (m) | Wysokość rzeczywista (m) | Wysokość scenariusz modelowy (m) | Rozbieżność (m) |",
        "|------|-----------|------------------|----------------------|---------------------|----------|---------------------------|-----------------------------------|-----------------|",
    ]
    for r in rows:
        lines.append(f"| {r['data']} | {r['opad']} | {r['temperatura']} | {r['zmiana_fakt']} | {r['zmiana_prognoza']} | {r['błąd']} | {r['wysokosc_rzeczywista']} | {r['wysokosc_model']} | {r['rozbieznosc']} |")
    return "\n".join(lines)


if __name__ == "__main__":
    lake_id = sys.argv[1] if len(sys.argv) > 1 else None
    if lake_id and lake_id not in lake.LAKES:
        print(f"Dostępne jeziora: {', '.join(lake.LAKES)}")
        sys.exit(1)
    for lid in (lake.LAKES if lake_id is None else [lake_id]):
        if not lake.get_model_path(lid).exists():
            print(f"Pomijam {lid}: brak pliku modelu.")
            continue
        run_evaluation(lake_id=lid)
