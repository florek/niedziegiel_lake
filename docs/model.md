# Model prognozy zmiany poziomu jezior (Budzisławskie, Koziegłowskie, Niedzięgiel, Ostrowskie, Powidzkie, Skulska Wieś, Suszewskie, Wilczyńskie)

## Cel

Model uczenia maszynowego służy do **prognozowania zmiany poziomu wybranego jeziora w danym miesiącu** (Zmiana) na podstawie:
- daty (sezonowość: miesiąc),
- opadu (Opad),
- temperatury (Temperatura),
- ostatnich zmian poziomu i poziomów (cechy opóźnione).

Obsługiwane jeziora: **Jezioro Budzisławskie** (`budzislawskie`), **Jezioro Koziegłowskie** (`kozieglowskie`), **Jezioro Niedzięgiel** (`niedziegiel`), **Jezioro Ostrowskie** (`ostrowskie`), **Jezioro Powidzkie** (`powidzkie`), **Jezioro Skulska Wieś** (`skulskawies`), **Jezioro Suszewskie** (`suszewskie`), **Jezioro Wilczyńskie** (`wilczynskie`). Dla każdego jeziora osobny plik danych i osobny wytrenowany model.

## Dane wejściowe

Pliki CSV w `data/`: `data/budzislawskie_data.csv`, `data/kozieglowskie_data.csv`, `data/niedziegiel_data.csv`, `data/ostrowskie_data.csv`, `data/powidzkie_data.csv`, `data/skulskawies_data.csv`, `data/suszewskie_data.csv`, `data/wilczynskie_data.csv`. Modele: `data/{id}_model.pkl`.

Kolumny: **Data** (pierwszy dzień miesiąca, dd.mm.yyyy), **Poziom** [m], **Zmiana** [m] (target), **Opad** [mm], **Temperatura** [°C]. Wartości dziesiętne z przecinkiem. Wiersze z #ERROR! lub brakami są pomijane. **Limit wysokości i strefa odpływu:** w scenariuszu modelowym poziom nie może przekraczać dopuszczalnego maksimum (`MAX_POZIOM_SPIETRZANIA_BY_LAKE`). Strefa odpływu (od której woda się przesącza) i miesięczne przesączanie są **obliczane z danych** per jezioro (`get_drainage_params(lake_id, df)`): szerokość strefy `odplyw_m` = 5% zakresu poziomów (min–max) z danych, ograniczone do 0,2–1,0 m; miesięczne przesączanie `przesaczanie_m` = średnia ujemna zmiana poziomu w miesiącach, gdy poziom końcowy był w strefie (max − odplyw_m, max]. Domyślne stałe: `ODPLYW_FRAC_RANGE`, `ODPLYW_M_MIN`, `ODPLYW_M_MAX`, `PRZESACZANIE_DEFAULT_M`. `apply_cap_and_drainage(poziom, max_poziom, odplyw_m, przesaczanie_m)` łączy limit z korektą w strefie.

## Algorytm

- **Wybór modelu:** przed zapisem trenowane są sześć kandydatów (scikit-learn): HistGradientBoosting (early stop, głębszy), GradientBoosting (reg, strong, legacy), Random Forest. Wybierany jest model z **najniższym MAE na zbiorze testowym**; dla każdego jeziora może to być inny typ.
- **Cechy:** month_sin, month_cos (cykliczny miesiąc), Opad, Temperatura; **opady i temperatury z opóźnieniem 1–N mies.** – dla każdego jeziora automatycznie testowane N z ciągu Fibonacciego (0, 1, 2, 3, 5, 8, 13 mies.), wybierane N z najlepszym MAE na teście (reakcja zlewni zależy od jeziora); oraz opóźnienia zmiany i poziomu (Niedzięgiel 3, Powidzkie 5 – `LAG_MONTHS_BY_LAKE`).
- **Podział:** temporalny, per jezioro. Niedzięgiel, Powidzkie: trening do 2013, test 2014–2023. Skulska Wieś: trening do 2015, test 2016–2023. Budzisławskie, Koziegłowskie, Ostrowskie, Suszewskie, Wilczyńskie (oddziaływanie leja depresji): trening do 2003-02 (luty 2003), test od 2003-03 (`TRAIN_END_YEAR_BY_LAKE`, `TRAIN_END_MONTH_BY_LAKE`).
- **Ewaluacja:** MAE i RMSE na zbiorze testowym (metryki w metrach).

## Użycie

Trening i zapis modelu (per jezioro):
```bash
python lake.py budzislawskie
python lake.py kozieglowskie
python lake.py niedziegiel
python lake.py powidzkie
python lake.py ostrowskie
python lake.py skulskawies
python lake.py suszewskie
python lake.py wilczynskie
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

## Raport ogólny

`python generate_summary_report.py` generuje `docs/raport_ogolny.md`: tabelę zbiorczą (jezioro, okres testowy, liczba miesięcy, MAE, RMSE) oraz linki do raportów szczegółowych per jezioro.

## Eksport do PDF

Raporty z `docs/` (np. `raport_ogolny.md`, `raport_podsumowujacy_niedziegiel.md`, `podsumowanie_ewaluacji_powidzkie.md`) można wyeksportować do PDF: `python md_to_pdf.py` (wszystkie `.md` z `docs/`) lub z podaniem konkretnych plików. Obrazy z katalogów `figures_{jezioro}/` są osadzane w PDF.
