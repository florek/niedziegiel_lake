# Prognoza zmiany poziomu jezior (Budzisławskie, Koziegłowskie, Niedzięgiel, Ostrowskie, Powidzkie, Skulska Wieś, Suszewskie, Wilczyńskie)

Projekt zawiera modele uczenia maszynowego do **prognozowania miesięcznej zmiany poziomu** wybranego jeziora na podstawie danych z pliku CSV (daty, poziom, opad, temperatura). Obsługiwane jeziora: **Jezioro Budzisławskie**, **Jezioro Koziegłowskie**, **Jezioro Niedzięgiel**, **Jezioro Ostrowskie**, **Jezioro Powidzkie**, **Jezioro Skulska Wieś**, **Jezioro Suszewskie**, **Jezioro Wilczyńskie**.

## Wymagania

- Python 3.10+
- Zależności: `pip install -r requirements.txt` (m.in. pandas, scikit-learn, numpy, matplotlib do raportu z wykresami).

## Dane i modele per jezioro

Nazwy plików są spójne: `data/{id}_data.csv`, `data/{id}_model.pkl`.

- **Budzisławskie:** `data/budzislawskie_data.csv`, `data/budzislawskie_model.pkl` (trening do lutego 2003, lej depresji)
- **Koziegłowskie:** `data/kozieglowskie_data.csv`, `data/kozieglowskie_model.pkl` (trening do lutego 2003, lej depresji)
- **Niedzięgiel:** `data/niedziegiel_data.csv`, `data/niedziegiel_model.pkl`
- **Ostrowskie:** `data/ostrowskie_data.csv`, `data/ostrowskie_model.pkl` (trening do lutego 2003, lej depresji)
- **Powidzkie:** `data/powidzkie_data.csv`, `data/powidzkie_model.pkl`
- **Skulska Wieś:** `data/skulskawies_data.csv`, `data/skulskawies_model.pkl` (trening do 2015, test 2016–2023)
- **Suszewskie:** `data/suszewskie_data.csv`, `data/suszewskie_model.pkl` (trening do lutego 2003, lej depresji)
- **Wilczyńskie:** `data/wilczynskie_data.csv`, `data/wilczynskie_model.pkl` (trening do lutego 2003, lej depresji)

Format CSV: nagłówki Data, Poziom, Zmiana, Opad, Temperatura; dziesiętne z przecinkiem. W scenariuszu modelowym poziom jeziora nie może przekraczać **maks. spiętrzenia (dopuszczony stan)** – wartości w `lake.MAX_POZIOM_SPIETRZANIA_BY_LAKE` na podstawie historycznego maksimum z pomiarów (odpływy na pewnych rzędnych). Jeśli masz jeszcze pliki `data.csv` lub `model.pkl`, przemianuj je na `niedziegiel_data.csv` i `niedziegiel_model.pkl`.

## Szybki start

1. Umieść dane w `data/{jezioro}_data.csv` (np. `niedziegiel_data.csv`, `powidzkie_data.csv`).
2. Wytrenuj i zapisz model dla wybranego jeziora (automatyczny wybór najlepszego modelu spośród kilku kandydatów):
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
   Bez argumentu domyślnie: `niedziegiel`. Modele zapisują się w `data/{jezioro}_model.pkl`. Dla Budzisławskiego trening kończy się w lutym 2003 (anomalie w danych później).
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
5. **Raport ogólny** (tabela zbiorcza dla wszystkich jezior z modelami):
   ```bash
   python generate_summary_report.py
   ```
   Wynik: `docs/raport_ogolny.md` (MAE, RMSE, okres testowy, linki do raportów szczegółowych).
6. **Eksport raportów do PDF:**
   ```bash
   python md_to_pdf.py
   ```
   Konwertuje wszystkie `.md` z `docs/` na PDF (obrazy z odpowiednich `figures_*`).
7. **Szacunek lat odbudowy poziomu po zaniku dodatkowego drenażu** (analiza osobna, uproszczona):
   ```bash
   python recovery_after_drainage_stop.py
   ```
   Wynik: `docs/szacunek_odbudowy_po_zaniku_drenazu.md`, pliki per jezioro `docs/zanik_drenazu_{jezioro}.md` oraz wykresy projekcji odbudowy (średnia 5 lat, do 2070) w `docs/figures_odbudowa/odbudowa_{jezioro}.png`.

Szczegóły modelu i API: [docs/model.md](docs/model.md).

## Struktura

- `lake.py` – konfiguracja jezior (`LAKES`), ścieżki `get_data_path(lake_id)`, `get_model_path(lake_id)`, wczytywanie danych, budowa cech, trening, zapis/odczyt modelu, `predict_change(...)`.
- `merge_niedziegiel_data.py` – łączy `data/meteo.csv` (opad, temperatura) z `data/niedziel_realny_pomiar.csv` (poziom), dodaje kolumnę Zmiana i zapisuje `data/niedziegiel_data.csv`.
- `merge_budzislawskie_data.py` – łączy `data/meteo.csv` z `data/budzislawskie_realny_pomiar.csv`, zapisuje `data/budzislawskie_data.csv`.
- `merge_kozieglowskie_data.py` – łączy `data/meteo.csv` z `data/kozieglowskie_realny_pomiar.csv`, zapisuje `data/kozieglowskie_data.csv`.
- `merge_suszewskie_data.py` – łączy `data/meteo.csv` z `data/suszewskie_realny_pomiar.csv`, zapisuje `data/suszewskie_data.csv`.
- `merge_ostrowskie_data.py` – łączy `data/meteo.csv` z `data/ostrowskie_realny_pomiar.csv`, zapisuje `data/ostrowskie_data.csv`.
- `merge_wilczynskie_data.py` – łączy `data/meteo.csv` z `data/wilczynskie_realny_pomiar.csv`, zapisuje `data/wilczynskie_data.csv`.
- `merge_powidzkie_data.py` – łączy `data/meteo.csv` z `data/powidzkie_realny_pomiar.csv` (poziom), dodaje kolumnę Zmiana i zapisuje `data/powidzkie_data.csv`.
- `merge_skulskawies_data.py` – łączy `data/meteo.csv` z `data/skulskawies_realny_pomiar.csv` lub `data/skuska_wies_realny_pomiar.csv` (poziom), zapisuje `data/skulskawies_data.csv`.
- `evaluate_predictions.py` – ewaluacja per jezioro, podsumowania w `docs/podsumowanie_ewaluacji_{jezioro}.md`.
- `generate_report.py` – raporty z wykresami: `docs/raport_podsumowujacy_{jezioro}.md`, `docs/figures_{jezioro}/*.png`.
- `generate_summary_report.py` – raport ogólny: `docs/raport_ogolny.md` (tabela zbiorcza wszystkich jezior).
- `recovery_after_drainage_stop.py` – szacunek lat odbudowy po zaniku drenażu (średnia pogoda 5 lat, projekcja do 2070): `docs/szacunek_odbudowy_po_zaniku_drenazu.md`, `docs/zanik_drenazu_{jezioro}.md`, `docs/figures_odbudowa/odbudowa_{jezioro}.png`.
- `md_to_pdf.py` – konwersja Markdown → PDF (fpdf2, markdown).
- `data/{jezioro}_data.csv` – dane miesięczne (Data, Poziom, Zmiana, Opad, Temperatura). Budzisławskie: `python merge_budzislawskie_data.py`. Koziegłowskie: `python merge_kozieglowskie_data.py`. Niedzięgiel: `python merge_niedziegiel_data.py`. Powidzkie: `python merge_powidzkie_data.py`. Ostrowskie: `python merge_ostrowskie_data.py`. Skulska Wieś: `python merge_skulskawies_data.py`. Suszewskie: `python merge_suszewskie_data.py`. Wilczyńskie: `python merge_wilczynskie_data.py` (wszystkie łączą `meteo.csv` z odpowiednim plikiem pomiaru).
- `data/{jezioro}_model.pkl` – wytrenowany model.
- `docs/model.md` – opis modelu i użycia.
- `docs/raport_ogolny.md` – raport zbiorczy (tabela MAE/RMSE, linki do raportów).
- `docs/raport_podsumowujacy_*.md`, `docs/podsumowanie_ewaluacji_*.md`, `docs/figures_*/` – raporty i wykresy per jezioro.
