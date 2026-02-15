# Prognoza zmiany poziomu jezior (Budzisławskie, Koziegłowskie, Niedzięgiel, Ostrowskie, Powidzkie, Skulska Wieś, Suszewskie, Wilczyńskie)

Projekt zawiera modele uczenia maszynowego do **prognozowania miesięcznej zmiany poziomu** wybranego jeziora na podstawie danych z pliku CSV (daty, poziom, opad, temperatura). Obsługiwane jeziora: **Jezioro Budzisławskie**, **Jezioro Koziegłowskie**, **Jezioro Niedzięgiel**, **Jezioro Ostrowskie**, **Jezioro Powidzkie**, **Jezioro Skulska Wieś**, **Jezioro Suszewskie**, **Jezioro Wilczyńskie**.

## Wymagania

- Python 3.10+
- Zależności: `pip install -r requirements.txt` (m.in. pandas, scikit-learn, numpy, matplotlib do raportu z wykresami).

## Struktura projektu

- **sources/** – kod Pythona (lake.py, evaluate_predictions.py, generate_report.py, generate_report_12mies.py, poziom_do_stycznia_2026.py, merge_*.py itd.).
- **data/** – dane per jezioro w podkatalogach:
  - **data/{id}/** – np. `data/niedziegiel/`: pliki `data.csv`, `model.pkl`, opcjonalnie `opad.txt`, `temp.txt`, `realny_pomiar.csv`.
  - **data/meteo.csv**, **data/zanik_drenazu.csv** – pliki współdzielone.
- **docs/** – raporty i wykresy per jezioro:
  - **docs/{id}/** – np. `docs/niedziegiel/`: raporty (prognoza.md z ewaluacją 12 mies., raport_podsumowujacy.md, podsumowanie_ewaluacji.md), wykresy PNG (poziom_rzeczywisty.png, symulacja_wariant_*.png).
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
5. Raport ewaluacji na 12 miesięcy: poziom rzeczywisty vs model, 9 wariantów pogodowych, symulacja do końca stycznia 2027, szanse realizacji. Dla jednego jeziora lub wszystkich:
   ```bash
   python sources/generate_report_12mies.py
   python sources/generate_report_12mies.py niedziegiel
   python sources/generate_report_12mies.py all
   ```
   Wynik per jezioro: `docs/{id}/prognoza.md`, `docs/{id}/poziom_rzeczywisty.png`, `docs/{id}/symulacja_wariant_*.png`, `docs/{id}/podsumowanie_ewaluacji.md`.
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
8. Symulacja poziomu do stycznia 2026 (warunki z `data/meteo.csv`): dla każdego jeziora od ostatniego miesiąca w `data/{id}/data.csv` do stycznia 2026 włącznie; wyliczone wiersze (Data, Poziom, Zmiana, Opad, Temperatura) są dopisywane do tego pliku.
   ```bash
   python sources/poziom_do_stycznia_2026.py
   ```
9. Szacunek lat odbudowy poziomu po zaniku dodatkowego drenażu:
   ```bash
   python sources/recovery_after_drainage_stop.py
   ```
   Wynik: `docs/szacunek_odbudowy_po_zaniku_drenazu.md`, `docs/{id}/zanik_drenazu.md`, wykresy w `docs/odbudowa/`.

Szczegóły modelu i API: [docs/model.md](docs/model.md).

## Wygenerowane raporty (linki)

Raporty i wykresy powstają po uruchomieniu skryptów z sekcji „Szybki start”. Poniżej linki z opisami.

| Opis | Plik |
|------|------|
| **Raport ogólny** – tabela zbiorcza dla wszystkich jezior z modelami | [docs/raport_ogolny.md](docs/raport_ogolny.md) |
| **Dokumentacja modelu** – opis modelu i API | [docs/model.md](docs/model.md) |
| **Raport ewaluacji 12 mies.** – poziom vs model, 9 wariantów pogodowych (każde jezioro: `docs/{id}/prognoza.md`) | [docs/niedziegiel/prognoza.md](docs/niedziegiel/prognoza.md) |
| **Szacunek odbudowy** – lat do odbudowy poziomu po zaniku dodatkowego drenażu (zbiorczo) | [docs/szacunek_odbudowy_po_zaniku_drenazu.md](docs/szacunek_odbudowy_po_zaniku_drenazu.md) |
| **Budzisławskie** – prognoza 12 mies. | [docs/budzislawskie/prognoza.md](docs/budzislawskie/prognoza.md) |
| **Budzisławskie** – raport z wykresami | [docs/budzislawskie/raport_podsumowujacy.md](docs/budzislawskie/raport_podsumowujacy.md) |
| **Budzisławskie** – podsumowanie ewaluacji | [docs/budzislawskie/podsumowanie_ewaluacji.md](docs/budzislawskie/podsumowanie_ewaluacji.md) |
| **Budzisławskie** – zanik drenażu | [docs/budzislawskie/zanik_drenazu.md](docs/budzislawskie/zanik_drenazu.md) |
| **Koziegłowskie** – prognoza 12 mies. | [docs/kozieglowskie/prognoza.md](docs/kozieglowskie/prognoza.md) |
| **Koziegłowskie** – raport z wykresami | [docs/kozieglowskie/raport_podsumowujacy.md](docs/kozieglowskie/raport_podsumowujacy.md) |
| **Koziegłowskie** – podsumowanie ewaluacji | [docs/kozieglowskie/podsumowanie_ewaluacji.md](docs/kozieglowskie/podsumowanie_ewaluacji.md) |
| **Koziegłowskie** – zanik drenażu | [docs/kozieglowskie/zanik_drenazu.md](docs/kozieglowskie/zanik_drenazu.md) |
| **Niedzięgiel** – prognoza 12 mies. | [docs/niedziegiel/prognoza.md](docs/niedziegiel/prognoza.md) |
| **Niedzięgiel** – raport podsumowujący (z wykresami) | [docs/niedziegiel/raport_podsumowujacy.md](docs/niedziegiel/raport_podsumowujacy.md) |
| **Niedzięgiel** – podsumowanie ewaluacji | [docs/niedziegiel/podsumowanie_ewaluacji.md](docs/niedziegiel/podsumowanie_ewaluacji.md) |
| **Niedzięgiel** – zanik drenażu | [docs/niedziegiel/zanik_drenazu.md](docs/niedziegiel/zanik_drenazu.md) |
| **Ostrowskie** – prognoza 12 mies. | [docs/ostrowskie/prognoza.md](docs/ostrowskie/prognoza.md) |
| **Ostrowskie** – raport z wykresami | [docs/ostrowskie/raport_podsumowujacy.md](docs/ostrowskie/raport_podsumowujacy.md) |
| **Ostrowskie** – podsumowanie ewaluacji | [docs/ostrowskie/podsumowanie_ewaluacji.md](docs/ostrowskie/podsumowanie_ewaluacji.md) |
| **Ostrowskie** – zanik drenażu | [docs/ostrowskie/zanik_drenazu.md](docs/ostrowskie/zanik_drenazu.md) |
| **Powidzkie** – prognoza 12 mies. | [docs/powidzkie/prognoza.md](docs/powidzkie/prognoza.md) |
| **Powidzkie** – raport z wykresami | [docs/powidzkie/raport_podsumowujacy.md](docs/powidzkie/raport_podsumowujacy.md) |
| **Powidzkie** – podsumowanie ewaluacji | [docs/powidzkie/podsumowanie_ewaluacji.md](docs/powidzkie/podsumowanie_ewaluacji.md) |
| **Powidzkie** – zanik drenażu | [docs/powidzkie/zanik_drenazu.md](docs/powidzkie/zanik_drenazu.md) |
| **Skulska Wieś** – prognoza 12 mies. | [docs/skulskawies/prognoza.md](docs/skulskawies/prognoza.md) |
| **Skulska Wieś** – raport z wykresami | [docs/skulskawies/raport_podsumowujacy.md](docs/skulskawies/raport_podsumowujacy.md) |
| **Skulska Wieś** – podsumowanie ewaluacji | [docs/skulskawies/podsumowanie_ewaluacji.md](docs/skulskawies/podsumowanie_ewaluacji.md) |
| **Skulska Wieś** – zanik drenażu | [docs/skulskawies/zanik_drenazu.md](docs/skulskawies/zanik_drenazu.md) |
| **Suszewskie** – prognoza 12 mies. | [docs/suszewskie/prognoza.md](docs/suszewskie/prognoza.md) |
| **Suszewskie** – raport z wykresami | [docs/suszewskie/raport_podsumowujacy.md](docs/suszewskie/raport_podsumowujacy.md) |
| **Suszewskie** – podsumowanie ewaluacji | [docs/suszewskie/podsumowanie_ewaluacji.md](docs/suszewskie/podsumowanie_ewaluacji.md) |
| **Suszewskie** – zanik drenażu | [docs/suszewskie/zanik_drenazu.md](docs/suszewskie/zanik_drenazu.md) |
| **Wilczyńskie** – prognoza 12 mies. | [docs/wilczynskie/prognoza.md](docs/wilczynskie/prognoza.md) |
| **Wilczyńskie** – raport z wykresami | [docs/wilczynskie/raport_podsumowujacy.md](docs/wilczynskie/raport_podsumowujacy.md) |
| **Wilczyńskie** – podsumowanie ewaluacji | [docs/wilczynskie/podsumowanie_ewaluacji.md](docs/wilczynskie/podsumowanie_ewaluacji.md) |
| **Wilczyńskie** – zanik drenażu | [docs/wilczynskie/zanik_drenazu.md](docs/wilczynskie/zanik_drenazu.md) |

Wykresy PNG (poziom, symulacje wariantów itd.) znajdują się w tych samych katalogach co raporty (np. `docs/niedziegiel/`).

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

