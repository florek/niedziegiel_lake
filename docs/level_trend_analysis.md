# Analiza trendu poziomu jeziora (twardy test 2000–2010 vs 2015+)

Skrypt `scripts/level_trend_analysis.py` wykonuje test, czy tempo spadku poziomu wody po 2015 roku jest większe niż w okresie 2000–2010.

## Wejście

- CSV z kolumnami: **date** (YYYY-MM-DD) lub **Data**, **level** (m n.p.m.) lub **Poziom**.
- Opcjonalnie: **lake** (gdy wiele jezior w jednym pliku), **Temperatura**, **Opad** (do korelacji z poziomem).

## Kroki analizy

1. Wczytanie danych, konwersja daty na `datetime`, sortowanie chronologiczne.
2. Zmienna ciągła: `year = rok + (day_of_year / 365.25)`.
3. Okresy: **2000–2010** oraz **2015–2023** (lub do końca danych).
4. Dla każdego okresu tempo trendu (m/rok):
   - **OLS** (regresja liniowa),
   - **Theil-Sen** (odporna),
   - **Bootstrap** (1000 prób, przedział ufności 95%).
5. Porównanie: różnica tempa (okres2 − okres1), pokrywanie się przedziałów 95% CI, istotność (test na różnicę).
6. Średnie miesięczne Δlevel w obu okresach (średnia i odchylenie std).
7. **Test Chow** – zmiana strukturalna (przełom).
8. **Mann-Kendall** – istotność trendu w każdym okresie.
9. **Korelacje**: poziom roczny vs temperatura roczna, poziom vs opad roczny (jeśli kolumny w CSV).

## Wyniki

Przy **--all-lakes** – dla każdego jeziora osobno:
- **reports/trend_analysis/&lt;lake_id&gt;/trend_results.csv** – tabela wyników (OLS, Theil-Sen, bootstrap, Chow, Mann-Kendall, korelacje).
- **reports/trend_analysis/&lt;lake_id&gt;/level_and_trends.png** – wykres: poziom w czasie, linie trendu 2000–2010 i 2015–2023, zaznaczone zakresy okresów.
- Raport tekstowy na stdout **per jezioro**: interpretacja hydrologiczna, czy tempo spadku przyspieszyło, czy zmiana jest istotna, czy wynik spójny z klimatem vs drenażem.

Bez **--all-lakes** – jeden plik wejściowy: wyniki w katalogu **--out-dir** (trend_results.csv, level_and_trends.png).

## Użycie

```bash
python scripts/level_trend_analysis.py --all-lakes
python scripts/level_trend_analysis.py data/budzislawskie/data_ext.csv --out-dir reports/trend_analysis/budzislawskie
```

- **--all-lakes** – analiza **dla każdego jeziora osobno** (Niedzięgiel, Powidzkie, Budzisławskie). Wyniki w `reports/trend_analysis/<lake_id>/` (trend_results.csv, level_and_trends.png) oraz raport na stdout per jezioro.
- **input** – pojedynczy plik CSV (używany gdy brak `--all-lakes`; domyślnie `data/budzislawskie/data_ext.csv`).
- **--date-col**, **--level-col** – nazwy kolumn (domyślnie Data, Poziom).
- **--lake-col**, **--lake** – filtr po jeziorze w pliku wielojeziorowym.
- **--period2-end** – koniec drugiego okresu (domyślnie 2023).
- **--out-dir** – katalog wyników; przy `--all-lakes` tworzone są podkatalogi `niedziegiel/`, `powidzkie/`, `budzislawskie/`.

## Interpretacja

- **Różnica tempa &lt; 0**: szybszy spadek w okresie 2015+ (bardziej ujemny slope).
- **Różnica tempa &gt; 0**: wolniejszy spadek (lub wzrost) w 2015+.
- **p &lt; 0,05** dla różnicy: zmiana tempa uznana za istotną statystycznie.
- **Test Chow (p &lt; 0,05)**: istotna zmiana struktury (przełom) w szeregu.
- Korelacja poziom–temperatura / poziom–opad wspiera interpretację w kierunku klimatu (bilans wodny, ETP).
