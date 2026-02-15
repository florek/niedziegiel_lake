# Raport: Jezioro Niedzięgiel

Raport dedykowany tylko dla Jeziora Niedzięgiel.

## Poziom wody: rzeczywisty pomiar i model

Niebieska linia: poziom z pliku `data/niedziegiel/data.csv` (pomiar na pierwszy dzień miesiąca). Przerywana pomarańczowa: wahania poziomu według modelu (scenariusz kumulatywny z prognozy zmiany miesięcznej). Zielona linia z punktami: prognoza poziomu na grudzień, styczeń i luty od ostatniego pomiaru (dane z plików opad/temp).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza poziomu (grudzień, styczeń, luty)

Wyliczenie od ostatniego rzeczywistego pomiaru (listopad 2025) z użyciem modelu bazowego Niedzięgiel i danych pogodowych z plików `data/niedziegiel/opad.txt` i `data/niedziegiel/temp.txt`.

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2025-12 | 13.0 | 2.4 | 0.0134 | 101.863 |
| 2026-01 | 17.3 | -2.9 | 0.0288 | 101.892 |
| 2026-02 | 9.9 | -2.5 | 0.0337 | 101.926 |
