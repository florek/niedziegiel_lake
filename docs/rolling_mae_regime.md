# Analiza MAE z przesuwanym końcem treningu (wykrywanie zmiany reżimu)

Skrypt `commands/rolling_mae_regime.py` trenuje modele z końcem treningu przesuwanym co rok i zapisuje MAE w tabelach oraz na wykresie, aby wspomóc wykrywanie punktu przełamania / zmiany reżimu wodnego.

## Zakres treningu

- **Początek treningu:** zawsze początek historii (pierwsza data w CSV).
- **Koniec treningu:** od **10 lat po początku historii** do **3 lata przed końcem historii**, krok roczny (np. 2002, 2003, …, 2022).
- Dla każdego takiego końca treningu model jest trenowany, a zbiór testowy to **tylko kolejne 24 miesiące** (można zmienić przez `--eval-months`).

## Wyniki

W katalogu `reports/<lake_id>/` powstają:

- **rolling_mae.csv** – tabela: `train_end`, `rok`, `mae`, `mae_spadki`, `mae_przyrosty`, `rmse`, `r2` dla każdego roku (MAE ogólne, MAE tylko dla miesięcy ze spadkiem poziomu, MAE tylko dla miesięcy z przyrostem).
- **rolling_mae_summary.csv** – jedna wiersz: `min_mae`, `max_mae`, `mean_mae`, `rok_min_mae`, `rok_max_mae`.
- **rolling_mae.png** – wykres: MAE w postaci skumulowanego słupka (spadki + przyrosty), poziom jeziora jako linia; MAE ogólne pominięte na wykresie (jest sumą składowych), pozostaje w CSV.

## Użycie

```bash
python commands/rolling_mae_regime.py --lake budzislawskie
python commands/rolling_mae_regime.py --lake niedziegiel --eval-months 24
python commands/rolling_mae_regime.py
```

- `--lake` – wybór jeziora (`niedziegiel`, `powidzkie`, `budzislawskie`); brak = wszystkie.
- `--eval-months` – zbiór testowy: tylko kolejne N miesięcy po treningu (domyślnie 24).

## Interpretacja (zmiana reżimu)

- Wzrost MAE przy przesuwaniu końca treningu w przód może wskazywać na **zmianę reżimu**: model uczy się na starym reżimie, a ewaluacja trafia w okres o innej dynamice.
- Lokalne maksimum MAE na wykresie to kandydat na **punkt przełamania**.
- Tabela podsumowania (`rolling_mae_summary.csv`) podaje rok z najwyższym i najniższym MAE.
