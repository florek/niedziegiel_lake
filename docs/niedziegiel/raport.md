# Raport: Jezioro Niedzięgiel

Raport dedykowany tylko dla Jeziora Niedzięgiel.

## Poziom wody: rzeczywisty pomiar i model

Niebieska linia: poziom z pliku `data/niedziegiel/data.csv` (pomiar na pierwszy dzień miesiąca). Przerywana pomarańczowa: wahania poziomu według modelu (scenariusz kumulatywny z prognozy zmiany miesięcznej).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Symulacje wariantów pogodowych (12 miesięcy do przodu)

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/niedziegiel/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykres: pełny zakres historii (od 1974) + 12 miesięcy symulacji.

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

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona według szans realizacji wszystkich wariantów): **101.866 m n.p.m.** W stosunku do stanu na koniec stycznia 2026 (101.89 m n.p.m.): ubędzie 0.024 m.


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 28.8 | 0.4 | -0.0654 | 101.825 |
| 2026-03 | 31.8 | 3.8 | 0.0327 | 101.857 |
| 2026-04 | 25.9 | 8.6 | 0.0122 | 101.869 |
| 2026-05 | 42.5 | 13.7 | -0.0135 | 101.856 |
| 2026-06 | 53.1 | 17.2 | -0.0274 | 101.828 |
| 2026-07 | 67.2 | 19.0 | -0.034 | 101.794 |
| 2026-08 | 53.1 | 18.5 | -0.0355 | 101.759 |
| 2026-09 | 40.2 | 14.1 | -0.0256 | 101.733 |
| 2026-10 | 29.0 | 9.3 | -0.0045 | 101.729 |
| 2026-11 | 35.0 | 4.3 | 0.0269 | 101.756 |
| 2026-12 | 36.9 | 1.0 | 0.0485 | 101.804 |
| 2027-01 | 34.5 | -0.2 | 0.062 | 101.866 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 478.0 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.024 m
- **Poziom na koniec stycznia 2027:** 101.866 m n.p.m.

### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | -2.1 | 0.035 | 101.925 |
| 2026-03 | 22.0 | 2.0 | 0.035 | 101.96 |
| 2026-04 | 15.9 | 7.7 | 0.0317 | 101.992 |
| 2026-05 | 30.2 | 12.6 | 0.0114 | 102.003 |
| 2026-06 | 36.6 | 16.0 | -0.0193 | 101.984 |
| 2026-07 | 47.1 | 17.4 | -0.034 | 101.95 |
| 2026-08 | 37.2 | 17.4 | -0.0394 | 101.91 |
| 2026-09 | 22.9 | 12.9 | -0.0451 | 101.865 |
| 2026-10 | 18.0 | 8.1 | -0.0349 | 101.83 |
| 2026-11 | 23.5 | 2.9 | 0.0034 | 101.834 |
| 2026-12 | 26.2 | -0.4 | 0.034 | 101.868 |
| 2027-01 | 23.3 | -2.2 | 0.0433 | 101.911 |

- **Szansa realizacji:** 10.2 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.021 m
- **Poziom na koniec stycznia 2027:** 101.911 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | -2.1 | 0.0368 | 101.927 |
| 2026-03 | 30.8 | 2.0 | 0.0344 | 101.961 |
| 2026-04 | 28.2 | 7.7 | 0.0199 | 101.981 |
| 2026-05 | 42.4 | 12.6 | -0.004 | 101.977 |
| 2026-06 | 55.5 | 16.0 | -0.0114 | 101.966 |
| 2026-07 | 65.5 | 17.4 | -0.0131 | 101.953 |
| 2026-08 | 52.7 | 17.4 | -0.0108 | 101.942 |
| 2026-09 | 40.6 | 12.9 | -0.0088 | 101.933 |
| 2026-10 | 29.0 | 8.1 | 0.0029 | 101.936 |
| 2026-11 | 37.2 | 2.9 | 0.032 | 101.968 |
| 2026-12 | 39.2 | -0.4 | 0.0468 | 102.015 |
| 2027-01 | 35.5 | -2.2 | 0.0605 | 102.075 |

- **Szansa realizacji:** 13.8 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.185 m
- **Poziom na koniec stycznia 2027:** 102.075 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | -2.1 | 0.0375 | 101.928 |
| 2026-03 | 47.6 | 2.0 | 0.0313 | 101.959 |
| 2026-04 | 35.4 | 7.7 | 0.0183 | 101.977 |
| 2026-05 | 60.2 | 12.6 | -0.0015 | 101.976 |
| 2026-06 | 71.7 | 16.0 | -0.0117 | 101.964 |
| 2026-07 | 99.5 | 17.4 | -0.0093 | 101.955 |
| 2026-08 | 76.7 | 17.4 | -0.0036 | 101.951 |
| 2026-09 | 64.1 | 12.9 | 0.0063 | 101.957 |
| 2026-10 | 44.6 | 8.1 | 0.0153 | 101.973 |
| 2026-11 | 47.0 | 2.9 | 0.0403 | 102.013 |
| 2026-12 | 47.8 | -0.4 | 0.0697 | 102.083 |
| 2027-01 | 48.5 | -2.2 | 0.0908 | 102.174 |

- **Szansa realizacji:** 7.3 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.284 m
- **Poziom na koniec stycznia 2027:** 102.174 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | -0.1 | 0.0353 | 101.925 |
| 2026-03 | 22.0 | 4.2 | 0.0338 | 101.959 |
| 2026-04 | 15.9 | 8.7 | 0.0118 | 101.971 |
| 2026-05 | 30.2 | 13.8 | -0.0154 | 101.956 |
| 2026-06 | 36.6 | 16.8 | -0.0321 | 101.923 |
| 2026-07 | 47.1 | 19.5 | -0.0451 | 101.878 |
| 2026-08 | 37.2 | 18.5 | -0.0571 | 101.821 |
| 2026-09 | 22.9 | 13.9 | -0.0499 | 101.771 |
| 2026-10 | 18.0 | 9.1 | -0.0217 | 101.75 |
| 2026-11 | 23.5 | 4.5 | 0.0118 | 101.761 |
| 2026-12 | 26.2 | 1.2 | 0.0359 | 101.797 |
| 2027-01 | 23.3 | -0.2 | 0.0501 | 101.847 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.043 m
- **Poziom na koniec stycznia 2027:** 101.847 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | -0.1 | 0.037 | 101.927 |
| 2026-03 | 30.8 | 4.2 | 0.0332 | 101.96 |
| 2026-04 | 28.2 | 8.7 | 0.01 | 101.97 |
| 2026-05 | 42.4 | 13.8 | -0.0175 | 101.953 |
| 2026-06 | 55.5 | 16.8 | -0.0283 | 101.924 |
| 2026-07 | 65.5 | 19.5 | -0.0357 | 101.889 |
| 2026-08 | 52.7 | 18.5 | -0.0455 | 101.843 |
| 2026-09 | 40.6 | 13.9 | -0.0396 | 101.804 |
| 2026-10 | 29.0 | 9.1 | -0.02 | 101.784 |
| 2026-11 | 37.2 | 4.5 | 0.0233 | 101.807 |
| 2026-12 | 39.2 | 1.2 | 0.0432 | 101.85 |
| 2027-01 | 35.5 | -0.2 | 0.0533 | 101.903 |

- **Szansa realizacji:** 16.0 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.013 m
- **Poziom na koniec stycznia 2027:** 101.903 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | -0.1 | 0.0378 | 101.928 |
| 2026-03 | 47.6 | 4.2 | 0.03 | 101.958 |
| 2026-04 | 35.4 | 8.7 | 0.0088 | 101.967 |
| 2026-05 | 60.2 | 13.8 | -0.0138 | 101.953 |
| 2026-06 | 71.7 | 16.8 | -0.0201 | 101.933 |
| 2026-07 | 99.5 | 19.5 | -0.0168 | 101.916 |
| 2026-08 | 76.7 | 18.5 | -0.0146 | 101.901 |
| 2026-09 | 64.1 | 13.9 | 0.0065 | 101.908 |
| 2026-10 | 44.6 | 9.1 | 0.017 | 101.925 |
| 2026-11 | 47.0 | 4.5 | 0.0443 | 101.969 |
| 2026-12 | 47.8 | 1.2 | 0.0698 | 102.039 |
| 2027-01 | 48.5 | -0.2 | 0.0908 | 102.13 |

- **Szansa realizacji:** 7.6 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.240 m
- **Poziom na koniec stycznia 2027:** 102.13 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | 3.1 | 0.0353 | 101.925 |
| 2026-03 | 22.0 | 5.1 | 0.033 | 101.958 |
| 2026-04 | 15.9 | 9.4 | 0.0044 | 101.963 |
| 2026-05 | 30.2 | 14.8 | -0.0245 | 101.938 |
| 2026-06 | 36.6 | 18.8 | -0.037 | 101.901 |
| 2026-07 | 47.1 | 20.1 | -0.0594 | 101.842 |
| 2026-08 | 37.2 | 19.4 | -0.0614 | 101.78 |
| 2026-09 | 22.9 | 15.6 | -0.0423 | 101.738 |
| 2026-10 | 18.0 | 10.6 | -0.0074 | 101.731 |
| 2026-11 | 23.5 | 5.4 | 0.015 | 101.746 |
| 2026-12 | 26.2 | 2.2 | 0.0364 | 101.782 |
| 2027-01 | 23.3 | 1.8 | 0.0471 | 101.829 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.061 m
- **Poziom na koniec stycznia 2027:** 101.829 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | 3.1 | 0.037 | 101.927 |
| 2026-03 | 30.8 | 5.1 | 0.0324 | 101.959 |
| 2026-04 | 28.2 | 9.4 | 0.0027 | 101.962 |
| 2026-05 | 42.4 | 14.8 | -0.0263 | 101.936 |
| 2026-06 | 55.5 | 18.8 | -0.0449 | 101.891 |
| 2026-07 | 65.5 | 20.1 | -0.0515 | 101.839 |
| 2026-08 | 52.7 | 19.4 | -0.046 | 101.793 |
| 2026-09 | 40.6 | 15.6 | -0.0334 | 101.76 |
| 2026-10 | 29.0 | 10.6 | 0.0034 | 101.763 |
| 2026-11 | 37.2 | 5.4 | 0.0327 | 101.796 |
| 2026-12 | 39.2 | 2.2 | 0.046 | 101.842 |
| 2027-01 | 35.5 | 1.8 | 0.0594 | 101.901 |

- **Szansa realizacji:** 15.8 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.011 m
- **Poziom na koniec stycznia 2027:** 101.901 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (m) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | 3.1 | 0.0375 | 101.927 |
| 2026-03 | 47.6 | 5.1 | 0.0295 | 101.957 |
| 2026-04 | 35.4 | 9.4 | 0.0028 | 101.96 |
| 2026-05 | 60.2 | 14.8 | -0.0223 | 101.937 |
| 2026-06 | 71.7 | 18.8 | -0.0301 | 101.907 |
| 2026-07 | 99.5 | 20.1 | -0.0229 | 101.884 |
| 2026-08 | 76.7 | 19.4 | -0.0133 | 101.871 |
| 2026-09 | 64.1 | 15.6 | 0.0088 | 101.88 |
| 2026-10 | 44.6 | 10.6 | 0.0255 | 101.905 |
| 2026-11 | 47.0 | 5.4 | 0.0533 | 101.959 |
| 2026-12 | 47.8 | 2.2 | 0.0828 | 102.041 |
| 2027-01 | 48.5 | 1.8 | 0.099 | 102.14 |

- **Szansa realizacji:** 7.6 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.250 m
- **Poziom na koniec stycznia 2027:** 102.14 m n.p.m.



*Wygenerowano: 2026-02-15 11:21*