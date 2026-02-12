# Prognoza zmiany poziomu jezior (Niedzięgiel, Powidzkie)

Projekt zawiera modele uczenia maszynowego do **prognozowania miesięcznej zmiany poziomu** wybranego jeziora na podstawie danych z pliku CSV (daty, poziom, opad, temperatura). Obsługiwane jeziora: **Jezioro Niedzięgiel**, **Jezioro Powidzkie**.

## Wymagania

- Python 3.10+
- Zależności: `pip install -r requirements.txt` (m.in. pandas, scikit-learn, numpy, matplotlib do raportu z wykresami).

## Dane i modele per jezioro

Nazwy plików są spójne: `data/{id}_data.csv`, `data/{id}_model.pkl`.

- **Niedzięgiel:** `data/niedziegiel_data.csv`, `data/niedziegiel_model.pkl`
- **Powidzkie:** `data/powidzkie_data.csv`, `data/powidzkie_model.pkl`

Format CSV: nagłówki Data, Poziom, Zmiana, Opad, Temperatura; dziesiętne z przecinkiem. Jeśli masz jeszcze pliki `data.csv` lub `model.pkl`, przemianuj je na `niedziegiel_data.csv` i `niedziegiel_model.pkl`.

## Szybki start

1. Umieść dane w `data/{jezioro}_data.csv` (np. `niedziegiel_data.csv`, `powidzkie_data.csv`).
2. Wytrenuj i zapisz model dla wybranego jeziora:
   ```bash
   python lake.py niedziegiel
   python lake.py powidzkie
   ```
   Bez argumentu domyślnie: `niedziegiel`. Modele zapisują się w `data/niedziegiel_model.pkl` i `data/powidzkie_model.pkl`.
3. Ewaluacja (jedno jezioro lub oba):
   ```bash
   python evaluate_predictions.py
   python evaluate_predictions.py powidzkie
   ```
   Wynik: `docs/podsumowanie_ewaluacji_niedziegiel.md`, `docs/podsumowanie_ewaluacji_powidzkie.md`.
4. **Pełny raport z wykresami** (jedno jezioro lub oba):
   ```bash
   python generate_report.py
   python generate_report.py powidzkie
   ```
   Wynik: `docs/raport_podsumowujacy_{jezioro}.md` oraz wykresy w `docs/figures_{jezioro}/`.
5. **Eksport raportów do PDF:**
   ```bash
   python md_to_pdf.py
   ```
   Konwertuje wszystkie `.md` z `docs/` na PDF (obrazy z odpowiednich `figures_*`).

Szczegóły modelu i API: [docs/model.md](docs/model.md).

## Struktura

- `lake.py` – konfiguracja jezior (`LAKES`), ścieżki `get_data_path(lake_id)`, `get_model_path(lake_id)`, wczytywanie danych, budowa cech, trening, zapis/odczyt modelu, `predict_change(...)`.
- `evaluate_predictions.py` – ewaluacja per jezioro, podsumowania w `docs/podsumowanie_ewaluacji_{jezioro}.md`.
- `generate_report.py` – raporty z wykresami: `docs/raport_podsumowujacy_{jezioro}.md`, `docs/figures_{jezioro}/*.png`.
- `md_to_pdf.py` – konwersja Markdown → PDF (fpdf2, markdown).
- `data/{jezioro}_data.csv` – dane miesięczne.
- `data/{jezioro}_model.pkl` – wytrenowany model.
- `docs/model.md` – opis modelu i użycia.
- `docs/raport_podsumowujacy_*.md`, `docs/podsumowanie_ewaluacji_*.md`, `docs/figures_*/` – raporty i wykresy per jezioro.
