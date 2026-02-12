# Model prognozy zmiany poziomu Jeziora Niedzięgiel

## Cel

Model uczenia maszynowego służy do **prognozowania zmiany poziomu Jeziora Niedzięgiel w danym miesiącu** (Zmiana) na podstawie:
- daty (sezonowość: miesiąc),
- opadu (Opad),
- temperatury (Temperatura),
- opcjonalnie: ostatnich zmian poziomu Jeziora Niedzięgiel i poziomów (cechy opóźnione).

## Dane wejściowe

Plik `data/data.csv`:
- **Data** – pierwszy dzień miesiąca (dd.mm.yyyy),
- **Poziom** – poziom Jeziora Niedzięgiel [m],
- **Zmiana** – zmiana poziomu Jeziora Niedzięgiel w danym miesiącu [m] (target),
- **Opad** – opad [mm],
- **Temperatura** – temperatura [°C].

Wartości dziesiętne w pliku używają przecinka. Wiersze z błędami (#ERROR!) lub pustymi wartościami są pomijane.

## Algorytm

- **Model:** `GradientBoostingRegressor` (scikit-learn).
- **Cechy:** month_sin, month_cos (cykliczny miesiąc), Opad, Temperatura oraz 3 opóźnienia (lag 1–3) dla Zmiana i Poziom (bez bieżącego poziomu).
- **Podział:** temporalny – ostatnie 70 miesięcy jako zbiór testowy, reszta jako treningowy.
- **Ewaluacja:** MAE i RMSE na zbiorze testowym (metryki w metrach).

## Użycie

Trening i zapis modelu:
```bash
python lake.py
```

W kodzie:
- `load_data()` – wczytanie i czyszczenie CSV,
- `train_model(df)` – trening, zwraca model, listę cech i słownik z `test_mae`, `test_rmse`,
- `predict_change(model, feature_cols, poziom, opad, temperatura, month, last_changes=..., last_poziomy=...)` – prognoza zmiany na jeden miesiąc,
- `save_model()` / `load_model()` – zapis/odczyt modelu do/z `data/model.pkl`.

## Wyniki (przykładowe)

Na zbiorze testowym (70 ostatnich miesięcy) typowe wartości:
- **Test MAE:** ~0,023 m,
- **Test RMSE:** ~0,028 m.

Interpretacja: średni błąd prognozy zmiany poziomu Jeziora Niedzięgiel to ok. 2,3 cm w wartości bezwzględnej.
