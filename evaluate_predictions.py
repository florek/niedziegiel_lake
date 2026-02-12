from pathlib import Path

import lake

SUMMARY_PATH = Path(__file__).resolve().parent / "docs" / "podsumowanie_ewaluacji.md"


def run_evaluation(data_path=None, model_path=None, output_path=SUMMARY_PATH):
    model, feature_cols = lake.load_model(model_path or lake.MODEL_PATH)
    df = lake.load_data(data_path or lake.DATA_PATH)
    df = lake.build_features(df)
    df = df.dropna()
    if len(df) == 0:
        raise ValueError("Brak wierszy z pełnymi cechami.")
    X = df[feature_cols]
    y_true = df[lake.COL_ZMIANA]
    y_pred = model.predict(X)
    errors = y_true.values - y_pred
    mae = (abs(errors)).mean()
    rmse = (errors ** 2).mean() ** 0.5
    poziom_rzeczywisty_koniec = (df[lake.COL_POZIOM] + df[lake.COL_ZMIANA]).values
    poziom_model_koniec = []
    poziom_prev = float(df.iloc[0][lake.COL_POZIOM])
    for i in range(len(df)):
        poziom_prev = poziom_prev + float(y_pred[i])
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
    break_month, break_info = _find_break_month(rows)
    content = _build_md(rows, mae, rmse, len(rows), break_month, break_info)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    print(f"Podsumowanie zapisane: {output_path}")
    return mae, rmse, rows


def _find_break_month(rows, threshold_drift=0.1, threshold_stay=0.05, min_months_stay=6):
    n = len(rows)
    for i in range(n):
        if abs(rows[i]["rozbieznosc"]) <= threshold_drift:
            continue
        stay_ok = True
        for j in range(i + 1, min(i + min_months_stay + 1, n)):
            if abs(rows[j]["rozbieznosc"]) < threshold_stay:
                stay_ok = False
                break
        if stay_ok and (i + min_months_stay < n or n - i >= 2):
            return rows[i]["data"], {
                "rozbieznosc_w_momentcie": rows[i]["rozbieznosc"],
                "kierunek": "rzeczywistość powyżej modelu" if rows[i]["rozbieznosc"] > 0 else "rzeczywistość poniżej modelu",
            }
    for i in range(n):
        if abs(rows[i]["rozbieznosc"]) > threshold_stay:
            return rows[i]["data"], {
                "rozbieznosc_w_momentcie": rows[i]["rozbieznosc"],
                "kierunek": "rzeczywistość powyżej modelu" if rows[i]["rozbieznosc"] > 0 else "rzeczywistość poniżej modelu",
            }
    return None, {}


def _build_md(rows, mae, rmse, n, break_month=None, break_info=None):
    lines = [
        "# Podsumowanie ewaluacji prognozy zmiany poziomu Jeziora Niedzięgiel",
        "",
        "Dla każdego miesiąca model otrzymuje opad i temperaturę (oraz cechy opóźnione z historii), wylicza prognozowaną zmianę poziomu Jeziora Niedzięgiel i jest ona porównana z faktyczną zmianą.",
        "",
        "## Cel analizy",
        "",
        "Do pewnego momentu Jezioro Niedzięgiel reaguje zgodnie z modelem (opad + temperatura + sezon → zmiana poziomu). Szukamy **momentu, od którego ta zależność została przerwana** – gdy poziom rzeczywisty trwale rozjechał się z prognozą modelu.",
        "",
        "## Moment rozjazdu z modelem",
        "",
    ]
    if break_month and break_info:
        lines.append(f"**Od miesiąca {break_month}** poziom rzeczywisty trwale odbiega od scenariusza modelowego.")
        lines.append(f"- Rozbieżność w tym miesiącu: **{break_info['rozbieznosc_w_momentcie']:+.3f} m** ({break_info['kierunek']}).")
        lines.append("")
        lines.append("Interpretacja: do tego momentu reakcja Jeziora Niedzięgiel na opad i temperaturę była zgodna z modelem; od tego miesiąca coś zmieniło zachowanie poziomu (np. zmiana odpływu, użytkowanie, regulacja).")
    else:
        lines.append("Nie wykryto wyraźnego, trwałego momentu rozjazdu (rozbieżność nie przekracza przyjętych progów lub często wraca do wartości bliskich modelowi).")
    lines.extend([
        "",
        "## Metryki",
        "",
        f"- **MAE (średni błąd bezwzględny):** {mae:.4f} m",
        f"- **RMSE (pierwiastek błędu średniokwadratowego):** {rmse:.4f} m",
        f"- **Liczba miesięcy:** {n}",
        "",
        "## Porównanie miesięczne",
        "",
        "| Data | Opad (mm) | Temperatura (°C) | Zmiana faktyczna (m) | Zmiana prognoza (m) | Błąd (m) | Wysokość rzeczywista (m) | Wysokość scenariusz modelowy (m) | Rozbieżność (m) |",
        "|------|-----------|------------------|----------------------|---------------------|----------|---------------------------|-----------------------------------|-----------------|",
    ])
    for r in rows:
        lines.append(f"| {r['data']} | {r['opad']} | {r['temperatura']} | {r['zmiana_fakt']} | {r['zmiana_prognoza']} | {r['błąd']} | {r['wysokosc_rzeczywista']} | {r['wysokosc_model']} | {r['rozbieznosc']} |")
    return "\n".join(lines)


if __name__ == "__main__":
    run_evaluation()
