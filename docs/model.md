# Model prognozy zmiany poziomu jezior (Niedzięgiel, Powidzkie)

## Cel

Model uczenia maszynowego służy do **prognozowania zmiany poziomu wybranego jeziora w danym miesiącu** (Zmiana) na podstawie:
- daty (sezonowość: miesiąc),
- opadu (Opad),
- temperatury (Temperatura),
- ostatnich zmian poziomu i poziomów (cechy opóźnione).

Obsługiwane jeziora: **Jezioro Niedzięgiel** (`niedziegiel`), **Jezioro Powidzkie** (`powidzkie`). Dla każdego jeziora osobny plik danych i osobny wytrenowany model.

## Dane wejściowe

Pliki CSV w `data/`: `data/niedziegiel_data.csv`, `data/powidzkie_data.csv`. Modele: `data/niedziegiel_model.pkl`, `data/powidzkie_model.pkl`.

Kolumny: **Data** (pierwszy dzień miesiąca, dd.mm.yyyy), **Poziom** [m], **Zmiana** [m] (target), **Opad** [mm], **Temperatura** [°C]. Wartości dziesiętne z przecinkiem. Wiersze z #ERROR! lub brakami są pomijane.

## Algorytm

- **Wybór modelu:** przed zapisem trenowane są sześć kandydatów (scikit-learn): HistGradientBoosting (early stop, głębszy), GradientBoosting (reg, strong, legacy), Random Forest. Wybierany jest model z **najniższym MAE na zbiorze testowym**; dla każdego jeziora może to być inny typ.
- **Cechy:** month_sin, month_cos (cykliczny miesiąc), Opad, Temperatura; opcjonalnie **opady i temperatury z opóźnieniem 1–N mies.** (dla Powidzkiego automatycznie testowane N ∈ {0, 6, 12}, wybierane N z najlepszym MAE na teście – typowo 12 mies., zgodnie z rocznym opóźnieniem reakcji jeziora); oraz opóźnienia zmiany i poziomu (Niedzięgiel 3, Powidzkie 5 – `LAG_MONTHS_BY_LAKE`).
- **Podział:** temporalny – trening do roku 2013 włącznie, test 2014–2023 (obie jeziora).
- **Ewaluacja:** MAE i RMSE na zbiorze testowym (metryki w metrach).

## Użycie

Trening i zapis modelu (per jezioro):
```bash
python lake.py niedziegiel
python lake.py powidzkie
```

W kodzie:
- `lake.LAKES` – słownik id → nazwa jeziora.
- `lake.get_data_path(lake_id)`, `lake.get_model_path(lake_id)` – ścieżki do pliku CSV i modelu.
- `load_data(path=...)` – wczytanie i czyszczenie CSV.
- `train_model(df=..., path=...)` – trening, zwraca model, listę cech, metryki, lag_months, meteo_lag_months.
- `predict_change(model, feature_cols, poziom, opad, temperatura, month, last_changes=..., last_poziomy=..., last_opady=..., last_temperatury=..., lag_months=..., meteo_lag_months=...)` – prognoza zmiany na jeden miesiąc (przy meteo_lag > 0 podaj listy ostatnich opadów i temperatur).
- `save_model(..., lag_months=..., meteo_lag_months=...)` / `load_model(path=...)` – zapis/odczyt modelu (`data/{lake_id}_model.pkl`); load zwraca model, feature_cols, lag_months, meteo_lag_months.

## Wyniki (przykładowe)

Na zbiorze testowym (70 ostatnich miesięcy) typowe wartości to rzędu kilku centymetrów MAE (średni błąd bezwzględny prognozy zmiany poziomu).

## Eksport do PDF

Raporty z `docs/` (np. `raport_podsumowujacy_niedziegiel.md`, `podsumowanie_ewaluacji_powidzkie.md`) można wyeksportować do PDF: `python md_to_pdf.py` (wszystkie `.md` z `docs/`) lub z podaniem konkretnych plików. Obrazy z katalogów `figures_{jezioro}/` są osadzane w PDF.
