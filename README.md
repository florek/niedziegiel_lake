# Prognoza zmiany poziomu Jeziora Niedzięgiel

Projekt zawiera model uczenia maszynowego do **prognozowania miesięcznej zmiany poziomu Jeziora Niedzięgiel** na podstawie danych z pliku `data/data.csv` (daty, poziom, opad, temperatura).

## Wymagania

- Python 3.10+
- Zależności: `pip install -r requirements.txt` (m.in. pandas, scikit-learn, numpy, matplotlib do raportu z wykresami).

## Szybki start

1. Umieść dane w `data/data.csv` (nagłówki: Data, Poziom, Zmiana, Opad, Temperatura; dziesiętne z przecinkiem).
2. Wytrenuj i zapisz model:
   ```bash
   python lake.py
   ```
3. Model zapisuje się w `data/model.pkl`. Do prognoz w kodzie użyj `lake.load_model()` i `lake.predict_change(...)`.
4. Ewaluacja: dla każdego miesiąca model dostaje opad i temperaturę, wylicza prognozę zmiany i porównuje z faktyczną. Podsumowanie w MD:
   ```bash
   python evaluate_predictions.py
   ```
   Wynik: `docs/podsumowanie_ewaluacji.md` (metryki MAE/RMSE oraz tabela miesięczna).
5. **Pełny raport z wykresami** – cel analizy, dane, model, wyniki, moment rozjazdu z modelem, wykresy (wysokość rzeczywista vs model, rozbieżność w czasie, zmiana fakt vs prognoza, błąd miesięczny):
   ```bash
   python generate_report.py
   ```
   Wynik: `docs/raport_podsumowujacy.md` oraz wykresy w `docs/figures/`.

Szczegóły modelu i API: [docs/model.md](docs/model.md). **Raport podsumowujący (z wykresami):** [docs/raport_podsumowujacy.md](docs/raport_podsumowujacy.md).

## Struktura

- `lake.py` – wczytywanie danych, budowa cech, trening (GradientBoostingRegressor), ewaluacja, zapis/odczyt modelu i funkcja `predict_change`.
- `evaluate_predictions.py` – ewaluacja: prognozy vs faktyczna zmiana poziomu Jeziora Niedzięgiel, podsumowanie w `docs/podsumowanie_ewaluacji.md`.
- `generate_report.py` – generowanie pełnego raportu z wykresami: `docs/raport_podsumowujacy.md`, `docs/figures/*.png`.
- `data/data.csv` – dane miesięczne (Data, Poziom, Zmiana, Opad, Temperatura).
- `data/model.pkl` – wytrenowany model (po uruchomieniu `python lake.py`).
- `docs/model.md` – opis modelu i użycia.
- `docs/raport_podsumowujacy.md` – raport podsumowujący z wykresami (cel, dane, model, wyniki, moment rozjazdu).
- `docs/figures/` – wykresy PNG do raportu.
