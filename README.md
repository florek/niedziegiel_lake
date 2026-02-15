# Prognoza zmiany poziomu jezior (Budzisławskie, Koziegłowskie, Niedzięgiel, Ostrowskie, Powidzkie, Skulska Wieś, Suszewskie, Wilczyńskie)

Projekt zawiera modele uczenia maszynowego do **prognozowania miesięcznej zmiany poziomu** wybranego jeziora na podstawie danych z pliku CSV (daty, poziom, opad, temperatura). Obsługiwane jeziora: **Jezioro Budzisławskie**, **Jezioro Koziegłowskie**, **Jezioro Niedzięgiel**, **Jezioro Ostrowskie**, **Jezioro Powidzkie**, **Jezioro Skulska Wieś**, **Jezioro Suszewskie**, **Jezioro Wilczyńskie**.

## Wymagania

- Python 3.10+
- Zależności: `pip install -r requirements.txt` (m.in. pandas, scikit-learn, numpy, matplotlib do raportu z wykresami).

## Struktura projektu

- **sources/** – kod Pythona (lake.py, evaluate_predictions.py, generate_report.py, merge_*.py itd.).
- **data/** – dane per jezioro w podkatalogach:
  - **data/{id}/** – np. `data/niedziegiel/`: pliki `data.csv`, `model.pkl`, opcjonalnie `opad.txt`, `temp.txt`, `realny_pomiar.csv`.
  - **data/meteo.csv**, **data/zanik_drenazu.csv** – pliki współdzielone.
- **docs/** – raporty i wykresy per jezioro:
  - **docs/{id}/** – np. `docs/niedziegiel/`: raporty (raport.md, raport_podsumowujacy.md, podsumowanie_ewaluacji.md), wykresy PNG.
  - **docs/odbudowa/** – wykresy projekcji odbudowy.
  - **docs/raport_ogolny.md**, **docs/szacunek_odbudowy_po_zaniku_drenazu.md** – raporty zbiorcze.

Dane i modele per jezioro: `data/niedziegiel/data.csv`, `data/niedziegiel/model.pkl` itd. Format CSV: nagłówki Data, Poziom, Zmiana, Opad, Temperatura; dziesiętne z przecinkiem. Limit wysokości (max spiętrzenia) w `lake.MAX_POZIOM_SPIETRZANIA_BY_LAKE`.

## Szybki start

Uruchamiaj skrypty z **katalogu głównego projektu** (gdzie są katalogi `data/`, `docs/`, `sources/`).

1. Umieść dane w `data/{jezioro}/data.csv` (np. wygeneruj: `python sources/merge_niedziegiel_data.py`).
2. Wytrenuj i zapisz model dla wybranego jeziora:
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
   Modele zapisują się w `data/{jezioro}/model.pkl`.
3. Ewaluacja (jedno jezioro lub wszystkie):
   ```bash
   python sources/evaluate_predictions.py
   python sources/evaluate_predictions.py powidzkie
   ```
   Wynik: `docs/{id}/podsumowanie_ewaluacji.md`.
4. Pełny raport z wykresami (jedno jezioro lub wszystkie):
   ```bash
   python sources/generate_report.py
   python sources/generate_report.py powidzkie
   ```
   Wynik: `docs/{id}/raport_podsumowujacy.md` oraz wykresy w `docs/{id}/`.
5. Raport tylko dla Niedzięgła (wykres poziomu z rzeczywistego pomiaru, prognoza grudzień–luty):
   ```bash
   python sources/generate_report_niedziegiel.py
   ```
   Wynik: `docs/niedziegiel/raport.md`, wykres `docs/niedziegiel/poziom_rzeczywisty.png`.
6. Raport ogólny (tabela zbiorcza dla wszystkich jezior z modelami):
   ```bash
   python sources/generate_summary_report.py
   ```
   Wynik: `docs/raport_ogolny.md`.
7. Eksport raportów do PDF (jeśli masz md_to_pdf.py):
   ```bash
   python md_to_pdf.py
   ```
   Obrazy z `docs/{jezioro}/` i `docs/odbudowa/` są osadzane w PDF.
8. Szacunek lat odbudowy poziomu po zaniku dodatkowego drenażu:
   ```bash
   python sources/recovery_after_drainage_stop.py
   ```
   Wynik: `docs/szacunek_odbudowy_po_zaniku_drenazu.md`, `docs/{id}/zanik_drenazu.md`, wykresy w `docs/odbudowa/`.

Szczegóły modelu i API: [docs/model.md](docs/model.md).

## Merge danych (realny pomiar + meteo → data.csv)

Dla każdego jeziora: `data/{id}/realny_pomiar.csv` oraz wspólny `data/meteo.csv` → `data/{id}/data.csv`:

```bash
python sources/merge_niedziegiel_data.py
python sources/merge_powidzkie_data.py
python sources/merge_budzislawskie_data.py
python sources/merge_kozieglowskie_data.py
python sources/merge_ostrowskie_data.py
python sources/merge_skulskawies_data.py
python sources/merge_suszewskie_data.py
python sources/merge_wilczynskie_data.py
```

## Symulacja reżimu zakłóconego (Niedzięgiel)

Scenariusz opad/temperatura z plików `data/niedziegiel/opad.txt` i `data/niedziegiel/temp.txt`:

```bash
python sources/simulate_disturbed_regime.py
```

Wynik: `docs/niedziegiel/symulacja_rezim_zaklocony.md`, wykres w `docs/niedziegiel/`.
