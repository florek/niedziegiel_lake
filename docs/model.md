# Model prognozy zmiany poziomu jezior (Budzisławskie, Koziegłowskie, Kownackie, Niedzięgiel, Ostrowskie, Powidzkie, Skulska Wieś, Suszewskie, Wilczyńskie)

## Cel

Model uczenia maszynowego służy do **prognozowania zmiany poziomu wybranego jeziora w danym miesiącu** (Zmiana) na podstawie:
- daty (sezonowość: miesiąc),
- opadu (Opad),
- temperatury (Temperatura),
- ostatnich zmian poziomu i poziomów (cechy opóźnione).

Obsługiwane jeziora: **Jezioro Budzisławskie** (`budzislawskie`), **Jezioro Koziegłowskie** (`kozieglowskie`), **Jezioro Kownackie** (`kownackie`), **Jezioro Niedzięgiel** (`niedziegiel`), **Jezioro Ostrowskie** (`ostrowskie`), **Jezioro Powidzkie** (`powidzkie`), **Jezioro Skulska Wieś** (`skulskawies`), **Jezioro Suszewskie** (`suszewskie`), **Jezioro Wilczyńskie** (`wilczynskie`). Dla każdego jeziora osobny plik danych i osobny wytrenowany model.

## Dane wejściowe

Dane i modele per jezioro w katalogach `data/{id}/`: plik `data.csv`, model `model.pkl`. Np. `data/niedziegiel/data.csv`, `data/niedziegiel/model.pkl`.

Kolumny: **Data** (pierwszy dzień miesiąca, dd.mm.yyyy), **Poziom** [m], **Zmiana** [m] (target), **Opad** [mm], **Temperatura** [°C]. Wartości dziesiętne z przecinkiem. Wiersze z #ERROR! lub brakami są pomijane. **Limit wysokości i strefa odpływu:** w scenariuszu modelowym poziom nie może przekraczać dopuszczalnego maksimum (`MAX_POZIOM_SPIETRZANIA_BY_LAKE`). Strefa odpływu (od której woda się przesącza) i miesięczne przesączanie są **obliczane z danych** per jezioro (`get_drainage_params(lake_id, df)`): szerokość strefy `odplyw_m` = 5% zakresu poziomów (min–max) z danych, ograniczone do 0,2–1,0 m; miesięczne przesączanie `przesaczanie_m` = średnia ujemna zmiana poziomu w miesiącach, gdy poziom końcowy był w strefie (max − odplyw_m, max]. Domyślne stałe: `ODPLYW_FRAC_RANGE`, `ODPLYW_M_MIN`, `ODPLYW_M_MAX`, `PRZESACZANIE_DEFAULT_M`. `apply_cap_and_drainage(poziom, max_poziom, odplyw_m, przesaczanie_m)` łączy limit z korektą w strefie.

## Algorytm

- **Wybór modelu:** przed zapisem trenowane są sześć kandydatów (scikit-learn): HistGradientBoosting (early stop, głębszy), GradientBoosting (reg, strong, legacy), Random Forest. Wybierany jest model z **najniższym MAE na zbiorze testowym**; dla każdego jeziora może to być inny typ.
- **Cechy:** month_sin, month_cos (cykliczny miesiąc), Opad, Temperatura; **opady i temperatury z opóźnieniem 1–N mies.** – dla każdego jeziora automatycznie testowane N z ciągu Fibonacciego (0, 1, 2, 3, 5, 8, 13 mies.), wybierane N z najlepszym MAE na teście (reakcja zlewni zależy od jeziora); oraz opóźnienia zmiany i poziomu (Niedzięgiel 3, Powidzkie 5 – `LAG_MONTHS_BY_LAKE`).
- **Podział:** temporalny, per jezioro. Dwa warianty modelu: (1) **po zmianie reżimu** – trening do daty optymalnej (skan 2000–2015), zapis w `data/{id}/model.pkl`; (2) **naturalny** – trening do końca roku przed pojawieniem się drenażu (`TRAIN_END_NATURAL_*`), zapis w `data/{id}/model_natural.pkl`. Rok pojawienia się drenażu (trening naturalny do końca roku poprzedniego): Budzisławskie 2003→2002-12, Koziegłowskie 2003→2002-12 (test do 2003), Kownackie 2003→2002-12, Niedzięgiel 2019→2018-12, Ostrowskie 2004→2003-12, Powidzkie 2018→2017-12, Skulska Wieś 2012→2011-12 (test do 2012), Suszewskie 2003→2002-12, Wilczyńskie 2003→2002-12. Trening naturalny: `python sources/lake.py {id} natural`. Na wykresach: niebieski = pomiar, pomarańczowy = model po reżimie, zielony = model naturalny.
- **Ewaluacja:** MAE i RMSE na zbiorze testowym (metryki w metrach).

## Użycie

Trening i zapis modelu (per jezioro), z katalogu głównego projektu:
```bash
python sources/lake.py budzislawskie
python sources/lake.py kozieglowskie
python sources/lake.py niedziegiel
python sources/lake.py powidzkie
python sources/lake.py ostrowskie
python sources/lake.py skulskawies
python sources/lake.py suszewskie
python sources/lake.py wilczynskie
```

W kodzie:
- `lake.LAKES` – słownik id → nazwa jeziora.
- `lake.get_data_path(lake_id)`, `lake.get_model_path(lake_id)` – ścieżki do pliku CSV i modelu.
- `load_data(path=...)` – wczytanie i czyszczenie CSV.
- `train_model(df=..., path=...)` – trening, zwraca model, listę cech, metryki, lag_months, meteo_lag_months.
- `predict_change(model, feature_cols, poziom, opad, temperatura, month, last_changes=..., last_poziomy=..., last_opady=..., last_temperatury=..., lag_months=..., meteo_lag_months=...)` – prognoza zmiany na jeden miesiąc (przy meteo_lag > 0 podaj listy ostatnich opadów i temperatur).
- `save_model(..., lag_months=..., meteo_lag_months=...)` / `load_model(path=...)` – zapis/odczyt modelu (`data/{lake_id}/model.pkl`); load zwraca model, feature_cols, lag_months, meteo_lag_months.

## Wyniki (przykładowe)

Na zbiorze testowym (70 ostatnich miesięcy) typowe wartości to rzędu kilku centymetrów MAE (średni błąd bezwzględny prognozy zmiany poziomu).

## Prognoza poziomu do stycznia 2026 (meteo.csv)

Skrypt `sources/poziom_do_stycznia_2026.py` dla każdego jeziora z modelem i danymi uruchamia symulację od miesiąca następującego po ostatnim wpisie w `data/{id}/data.csv` do stycznia 2026 włącznie, używając warunków z `data/meteo.csv`. Wyliczone wiersze (Data, Poziom, Zmiana, Opad, Temperatura) są dopisywane do `data/{id}/data.csv`. Uruchomienie: `python sources/poziom_do_stycznia_2026.py`.

## Raport ewaluacji na 12 miesięcy

`python sources/generate_report_12mies.py` (bez argumentu: Niedzięgiel; z argumentem: `all` lub id jeziora) generuje per jezioro: `docs/{id}/prognoza.md`, `docs/{id}/szanse_odbudowy.md` (opisowa ocena szans na odbudowę na podstawie prognozy 12 mies.), wykres poziomu i symulacje 9 wariantów pogodowych do końca stycznia 2027 oraz `docs/{id}/podsumowanie_ewaluacji.md`.

## Raport ogólny

`python sources/generate_summary_report.py` generuje `docs/raport_ogolny.md`: tabelę zbiorczą (jezioro, okres testowy, liczba miesięcy, MAE, RMSE) oraz linki do raportów szczegółowych per jezioro (`docs/{id}/raport_podsumowujacy.md`, `docs/{id}/podsumowanie_ewaluacji.md`).

## Eksport do PDF

Raporty z `docs/` (np. `raport_ogolny.md`, `docs/niedziegiel/raport_podsumowujacy.md`, `docs/powidzkie/podsumowanie_ewaluacji.md`) można wyeksportować do PDF: `python md_to_pdf.py` (wszystkie `.md` z `docs/`) lub z podaniem konkretnych plików. Obrazy z katalogów `docs/{jezioro}/` i `docs/odbudowa/` są osadzane w PDF.
