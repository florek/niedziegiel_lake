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

## Symulacje wariantów pogodowych (12 miesięcy do przodu)

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/niedziegiel/data.csv`. Symulacja: 12 miesięcy od lutego 2026 (styczeń 2026 to pomiar rzeczywisty) – luty 2026–styczeń 2027. Wykres: pełny zakres historii (od 1974) + 12 miesięcy symulacji.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa realizacji (%) |
|---------|------------------------|
| zimny, suchy | 10.2 |
| zimny, normalny | 13.8 |
| zimny, wilgotny | 7.3 |
| normalny, suchy | 10.8 |
| normalny, normalny | 16.0 |
| normalny, wilgotny | 7.6 |
| ciepły, suchy | 10.8 |
| ciepły, normalny | 15.8 |
| ciepły, wilgotny | 7.6 |


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | -2.1 | 0.0154 | 101.865 |
| 2026-03 | 22.0 | 2.0 | 0.0352 | 101.901 |
| 2026-04 | 15.9 | 7.7 | 0.0413 | 101.942 |
| 2026-05 | 30.2 | 12.6 | 0.0173 | 101.959 |
| 2026-06 | 36.6 | 16.0 | -0.0129 | 101.946 |
| 2026-07 | 47.1 | 17.4 | -0.0316 | 101.915 |
| 2026-08 | 37.2 | 17.4 | -0.0403 | 101.874 |
| 2026-09 | 22.9 | 12.9 | -0.0451 | 101.829 |
| 2026-10 | 18.0 | 8.1 | -0.0349 | 101.794 |
| 2026-11 | 23.5 | 2.9 | 0.0034 | 101.798 |
| 2026-12 | 26.2 | -0.4 | 0.034 | 101.832 |
| 2027-01 | 23.3 | -2.2 | 0.0433 | 101.875 |

- **Szansa realizacji:** 10.2 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.025 m
- **Poziom na koniec stycznia 2027:** 101.875 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | -2.1 | 0.0267 | 101.877 |
| 2026-03 | 30.8 | 2.0 | 0.0447 | 101.921 |
| 2026-04 | 28.2 | 7.7 | 0.0416 | 101.963 |
| 2026-05 | 42.4 | 12.6 | 0.0157 | 101.979 |
| 2026-06 | 55.5 | 16.0 | -0.0085 | 101.97 |
| 2026-07 | 65.5 | 17.4 | -0.0201 | 101.95 |
| 2026-08 | 52.7 | 17.4 | -0.0196 | 101.93 |
| 2026-09 | 40.6 | 12.9 | -0.0186 | 101.912 |
| 2026-10 | 29.0 | 8.1 | -0.0081 | 101.904 |
| 2026-11 | 37.2 | 2.9 | 0.0294 | 101.933 |
| 2026-12 | 39.2 | -0.4 | 0.0468 | 101.98 |
| 2027-01 | 35.5 | -2.2 | 0.0605 | 102.04 |

- **Szansa realizacji:** 13.8 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.190 m
- **Poziom na koniec stycznia 2027:** 102.04 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | -2.1 | 0.0327 | 101.883 |
| 2026-03 | 47.6 | 2.0 | 0.0456 | 101.928 |
| 2026-04 | 35.4 | 7.7 | 0.0553 | 101.984 |
| 2026-05 | 60.2 | 12.6 | 0.0476 | 102.031 |
| 2026-06 | 71.7 | 16.0 | 0.0428 | 102.074 |
| 2026-07 | 99.5 | 17.4 | 0.0132 | 102.087 |
| 2026-08 | 76.7 | 17.4 | -0.0194 | 102.068 |
| 2026-09 | 64.1 | 12.9 | -0.0162 | 102.052 |
| 2026-10 | 44.6 | 8.1 | -0.0018 | 102.05 |
| 2026-11 | 47.0 | 2.9 | 0.0356 | 102.086 |
| 2026-12 | 47.8 | -0.4 | 0.0697 | 102.155 |
| 2027-01 | 48.5 | -2.2 | 0.0908 | 102.246 |

- **Szansa realizacji:** 7.3 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.396 m
- **Poziom na koniec stycznia 2027:** 102.246 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | -0.1 | 0.0149 | 101.865 |
| 2026-03 | 22.0 | 4.2 | 0.0287 | 101.894 |
| 2026-04 | 15.9 | 8.7 | 0.0224 | 101.916 |
| 2026-05 | 30.2 | 13.8 | -0.0028 | 101.913 |
| 2026-06 | 36.6 | 16.8 | -0.0161 | 101.897 |
| 2026-07 | 47.1 | 19.5 | -0.0365 | 101.861 |
| 2026-08 | 37.2 | 18.5 | -0.0546 | 101.806 |
| 2026-09 | 22.9 | 13.9 | -0.0459 | 101.76 |
| 2026-10 | 18.0 | 9.1 | -0.0288 | 101.731 |
| 2026-11 | 23.5 | 4.5 | 0.0021 | 101.733 |
| 2026-12 | 26.2 | 1.2 | 0.0319 | 101.765 |
| 2027-01 | 23.3 | -0.2 | 0.0445 | 101.81 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.040 m
- **Poziom na koniec stycznia 2027:** 101.81 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | -0.1 | 0.0267 | 101.877 |
| 2026-03 | 30.8 | 4.2 | 0.0443 | 101.921 |
| 2026-04 | 28.2 | 8.7 | 0.0289 | 101.95 |
| 2026-05 | 42.4 | 13.8 | -0.0006 | 101.949 |
| 2026-06 | 55.5 | 16.8 | -0.0271 | 101.922 |
| 2026-07 | 65.5 | 19.5 | -0.0392 | 101.883 |
| 2026-08 | 52.7 | 18.5 | -0.0473 | 101.836 |
| 2026-09 | 40.6 | 13.9 | -0.0396 | 101.796 |
| 2026-10 | 29.0 | 9.1 | -0.02 | 101.776 |
| 2026-11 | 37.2 | 4.5 | 0.0233 | 101.8 |
| 2026-12 | 39.2 | 1.2 | 0.0432 | 101.843 |
| 2027-01 | 35.5 | -0.2 | 0.0533 | 101.896 |

- **Szansa realizacji:** 16.0 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.046 m
- **Poziom na koniec stycznia 2027:** 101.896 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | -0.1 | 0.0327 | 101.883 |
| 2026-03 | 47.6 | 4.2 | 0.0452 | 101.928 |
| 2026-04 | 35.4 | 8.7 | 0.0383 | 101.966 |
| 2026-05 | 60.2 | 13.8 | 0.0128 | 101.979 |
| 2026-06 | 71.7 | 16.8 | -0.0235 | 101.956 |
| 2026-07 | 99.5 | 19.5 | -0.0266 | 101.929 |
| 2026-08 | 76.7 | 18.5 | -0.0223 | 101.907 |
| 2026-09 | 64.1 | 13.9 | -0.0049 | 101.902 |
| 2026-10 | 44.6 | 9.1 | 0.011 | 101.913 |
| 2026-11 | 47.0 | 4.5 | 0.0416 | 101.954 |
| 2026-12 | 47.8 | 1.2 | 0.0698 | 102.024 |
| 2027-01 | 48.5 | -0.2 | 0.0908 | 102.115 |

- **Szansa realizacji:** 7.6 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.265 m
- **Poziom na koniec stycznia 2027:** 102.115 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | 3.1 | 0.0145 | 101.865 |
| 2026-03 | 22.0 | 5.1 | 0.0284 | 101.893 |
| 2026-04 | 15.9 | 9.4 | 0.0174 | 101.91 |
| 2026-05 | 30.2 | 14.8 | -0.0049 | 101.905 |
| 2026-06 | 36.6 | 18.8 | -0.023 | 101.882 |
| 2026-07 | 47.1 | 20.1 | -0.04 | 101.842 |
| 2026-08 | 37.2 | 19.4 | -0.0525 | 101.79 |
| 2026-09 | 22.9 | 15.6 | -0.045 | 101.745 |
| 2026-10 | 18.0 | 10.6 | -0.0182 | 101.727 |
| 2026-11 | 23.5 | 5.4 | 0.0096 | 101.736 |
| 2026-12 | 26.2 | 2.2 | 0.0349 | 101.771 |
| 2027-01 | 23.3 | 1.8 | 0.0414 | 101.813 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.037 m
- **Poziom na koniec stycznia 2027:** 101.813 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | 3.1 | 0.0263 | 101.876 |
| 2026-03 | 30.8 | 5.1 | 0.0441 | 101.92 |
| 2026-04 | 28.2 | 9.4 | 0.0249 | 101.945 |
| 2026-05 | 42.4 | 14.8 | -0.0091 | 101.936 |
| 2026-06 | 55.5 | 18.8 | -0.0253 | 101.911 |
| 2026-07 | 65.5 | 20.1 | -0.04 | 101.871 |
| 2026-08 | 52.7 | 19.4 | -0.0434 | 101.827 |
| 2026-09 | 40.6 | 15.6 | -0.033 | 101.794 |
| 2026-10 | 29.0 | 10.6 | 0.0012 | 101.796 |
| 2026-11 | 37.2 | 5.4 | 0.0327 | 101.828 |
| 2026-12 | 39.2 | 2.2 | 0.046 | 101.874 |
| 2027-01 | 35.5 | 1.8 | 0.0594 | 101.934 |

- **Szansa realizacji:** 15.8 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.084 m
- **Poziom na koniec stycznia 2027:** 101.934 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | 3.1 | 0.0321 | 101.882 |
| 2026-03 | 47.6 | 5.1 | 0.0453 | 101.927 |
| 2026-04 | 35.4 | 9.4 | 0.0355 | 101.963 |
| 2026-05 | 60.2 | 14.8 | 0.0108 | 101.974 |
| 2026-06 | 71.7 | 18.8 | -0.0279 | 101.946 |
| 2026-07 | 99.5 | 20.1 | -0.0327 | 101.913 |
| 2026-08 | 76.7 | 19.4 | -0.0216 | 101.891 |
| 2026-09 | 64.1 | 15.6 | -0.0026 | 101.889 |
| 2026-10 | 44.6 | 10.6 | 0.0216 | 101.91 |
| 2026-11 | 47.0 | 5.4 | 0.0447 | 101.955 |
| 2026-12 | 47.8 | 2.2 | 0.0696 | 102.025 |
| 2027-01 | 48.5 | 1.8 | 0.0904 | 102.115 |

- **Szansa realizacji:** 7.6 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.265 m
- **Poziom na koniec stycznia 2027:** 102.115 m n.p.m.

