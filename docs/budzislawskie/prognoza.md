# Raport: Jezioro Budzisławskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Budzisławskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska linia: poziom z pliku `data/budzislawskie/data.csv` (pomiar na pierwszy dzień miesiąca). Przerywana pomarańczowa: wahania poziomu według modelu (scenariusz kumulatywny z prognozy zmiany miesięcznej).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Symulacje wariantów pogodowych (12 miesięcy do przodu)

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/budzislawskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykres: pełny zakres historii (od 1974) + 12 miesięcy symulacji.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa realizacji (%) |
|---------|------------------------|
| zimny, suchy | 11.3 |
| zimny, normalny | 14.2 |
| zimny, wilgotny | 7.1 |
| normalny, suchy | 11.7 |
| normalny, normalny | 15.2 |
| normalny, wilgotny | 7.2 |
| ciepły, suchy | 11.5 |
| ciepły, normalny | 14.5 |
| ciepły, wilgotny | 7.2 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów): **96.023 m n.p.m.** W stosunku do stanu na koniec stycznia 2026 (96.0461 m n.p.m.): ubędzie 0.023 m (-2.3 cm).


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.0 | 1.2 | +2.8 cm | 96.074 |
| 2026-03 | 33.4 | 4.2 | +2.1 cm | 96.095 |
| 2026-04 | 25.1 | 9.3 | +0.9 cm | 96.104 |
| 2026-05 | 46.0 | 13.9 | -1.1 cm | 96.093 |
| 2026-06 | 50.1 | 17.7 | -3.7 cm | 96.056 |
| 2026-07 | 69.9 | 19.7 | -3.7 cm | 96.02 |
| 2026-08 | 53.6 | 19.2 | -3.1 cm | 95.989 |
| 2026-09 | 40.3 | 14.8 | -2.4 cm | 95.965 |
| 2026-10 | 31.5 | 9.8 | -1.0 cm | 95.955 |
| 2026-11 | 34.6 | 4.7 | +0.7 cm | 95.961 |
| 2026-12 | 34.9 | 1.4 | +2.1 cm | 95.982 |
| 2027-01 | 38.4 | 0.0 | +4.1 cm | 96.023 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 491.7 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.023 m (-2.3 cm)
- **Poziom na koniec stycznia 2027:** 96.023 m n.p.m.

### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | -1.0 | +2.7 cm | 96.073 |
| 2026-03 | 22.8 | 3.0 | +2.0 cm | 96.093 |
| 2026-04 | 15.0 | 8.4 | +1.0 cm | 96.103 |
| 2026-05 | 34.0 | 12.8 | -0.8 cm | 96.094 |
| 2026-06 | 33.6 | 16.5 | -3.6 cm | 96.059 |
| 2026-07 | 53.9 | 18.8 | -4.2 cm | 96.016 |
| 2026-08 | 35.5 | 18.3 | -3.6 cm | 95.981 |
| 2026-09 | 22.7 | 13.7 | -3.7 cm | 95.944 |
| 2026-10 | 17.6 | 8.3 | -1.3 cm | 95.932 |
| 2026-11 | 21.8 | 3.6 | +0.5 cm | 95.937 |
| 2026-12 | 25.6 | -0.2 | +2.2 cm | 95.958 |
| 2027-01 | 28.6 | -1.9 | +3.8 cm | 95.996 |

- **Szansa realizacji:** 11.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.050 m (-5.0 cm)
- **Poziom na koniec stycznia 2027:** 95.996 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | -1.0 | +2.7 cm | 96.073 |
| 2026-03 | 33.9 | 3.0 | +2.0 cm | 96.093 |
| 2026-04 | 27.7 | 8.4 | +1.0 cm | 96.103 |
| 2026-05 | 46.4 | 12.8 | -0.9 cm | 96.095 |
| 2026-06 | 53.1 | 16.5 | -3.1 cm | 96.063 |
| 2026-07 | 66.7 | 18.8 | -3.8 cm | 96.025 |
| 2026-08 | 56.2 | 18.3 | -3.4 cm | 95.992 |
| 2026-09 | 43.3 | 13.7 | -1.7 cm | 95.975 |
| 2026-10 | 33.9 | 8.3 | -0.7 cm | 95.967 |
| 2026-11 | 38.8 | 3.6 | +0.7 cm | 95.974 |
| 2026-12 | 36.7 | -0.2 | +2.1 cm | 95.995 |
| 2027-01 | 39.8 | -1.9 | +3.9 cm | 96.034 |

- **Szansa realizacji:** 14.2 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.012 m (-1.2 cm)
- **Poziom na koniec stycznia 2027:** 96.034 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | -1.0 | +3.3 cm | 96.079 |
| 2026-03 | 49.5 | 3.0 | +2.6 cm | 96.105 |
| 2026-04 | 36.1 | 8.4 | +1.0 cm | 96.115 |
| 2026-05 | 64.7 | 12.8 | -1.0 cm | 96.105 |
| 2026-06 | 70.6 | 16.5 | -3.0 cm | 96.075 |
| 2026-07 | 102.3 | 18.8 | -2.4 cm | 96.051 |
| 2026-08 | 77.4 | 18.3 | -1.7 cm | 96.034 |
| 2026-09 | 62.5 | 13.7 | -1.7 cm | 96.017 |
| 2026-10 | 49.0 | 8.3 | -0.6 cm | 96.011 |
| 2026-11 | 46.6 | 3.6 | +1.0 cm | 96.021 |
| 2026-12 | 46.4 | -0.2 | +2.2 cm | 96.043 |
| 2027-01 | 51.6 | -1.9 | +4.3 cm | 96.086 |

- **Szansa realizacji:** 7.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.040 m (+4.0 cm)
- **Poziom na koniec stycznia 2027:** 96.086 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | 0.8 | +2.7 cm | 96.073 |
| 2026-03 | 22.8 | 4.3 | +2.0 cm | 96.093 |
| 2026-04 | 15.0 | 9.1 | +1.0 cm | 96.103 |
| 2026-05 | 34.0 | 13.7 | -1.0 cm | 96.092 |
| 2026-06 | 33.6 | 17.8 | -4.2 cm | 96.05 |
| 2026-07 | 53.9 | 19.8 | -4.2 cm | 96.008 |
| 2026-08 | 35.5 | 19.3 | -3.6 cm | 95.972 |
| 2026-09 | 22.7 | 14.7 | -3.7 cm | 95.936 |
| 2026-10 | 17.6 | 9.8 | -1.3 cm | 95.922 |
| 2026-11 | 21.8 | 4.8 | +0.5 cm | 95.928 |
| 2026-12 | 25.6 | 1.8 | +2.1 cm | 95.949 |
| 2027-01 | 28.6 | 0.1 | +4.0 cm | 95.989 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.057 m (-5.7 cm)
- **Poziom na koniec stycznia 2027:** 95.989 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | 0.8 | +2.7 cm | 96.073 |
| 2026-03 | 33.9 | 4.3 | +2.0 cm | 96.093 |
| 2026-04 | 27.7 | 9.1 | +1.0 cm | 96.103 |
| 2026-05 | 46.4 | 13.7 | -1.0 cm | 96.093 |
| 2026-06 | 53.1 | 17.8 | -3.8 cm | 96.055 |
| 2026-07 | 66.7 | 19.8 | -3.9 cm | 96.017 |
| 2026-08 | 56.2 | 19.3 | -3.4 cm | 95.983 |
| 2026-09 | 43.3 | 14.7 | -1.8 cm | 95.965 |
| 2026-10 | 33.9 | 9.8 | -0.8 cm | 95.958 |
| 2026-11 | 38.8 | 4.8 | +0.7 cm | 95.965 |
| 2026-12 | 36.7 | 1.8 | +2.0 cm | 95.985 |
| 2027-01 | 39.8 | 0.1 | +4.2 cm | 96.027 |

- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.019 m (-1.9 cm)
- **Poziom na koniec stycznia 2027:** 96.027 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | 0.8 | +3.3 cm | 96.079 |
| 2026-03 | 49.5 | 4.3 | +2.6 cm | 96.105 |
| 2026-04 | 36.1 | 9.1 | +1.0 cm | 96.115 |
| 2026-05 | 64.7 | 13.7 | -1.1 cm | 96.104 |
| 2026-06 | 70.6 | 17.8 | -3.7 cm | 96.066 |
| 2026-07 | 102.3 | 19.8 | -2.5 cm | 96.041 |
| 2026-08 | 77.4 | 19.3 | -1.7 cm | 96.024 |
| 2026-09 | 62.5 | 14.7 | -1.8 cm | 96.007 |
| 2026-10 | 49.0 | 9.8 | -0.6 cm | 96.0 |
| 2026-11 | 46.6 | 4.8 | +1.0 cm | 96.01 |
| 2026-12 | 46.4 | 1.8 | +2.2 cm | 96.032 |
| 2027-01 | 51.6 | 0.1 | +4.6 cm | 96.078 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.032 m (+3.2 cm)
- **Poziom na koniec stycznia 2027:** 96.078 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | 3.8 | +2.6 cm | 96.072 |
| 2026-03 | 22.8 | 5.4 | +1.9 cm | 96.092 |
| 2026-04 | 15.0 | 10.4 | +0.7 cm | 96.099 |
| 2026-05 | 34.0 | 15.1 | -1.3 cm | 96.086 |
| 2026-06 | 33.6 | 18.9 | -4.3 cm | 96.043 |
| 2026-07 | 53.9 | 20.4 | -4.2 cm | 96.001 |
| 2026-08 | 35.5 | 20.0 | -3.6 cm | 95.965 |
| 2026-09 | 22.7 | 16.0 | -3.7 cm | 95.928 |
| 2026-10 | 17.6 | 11.2 | -1.7 cm | 95.912 |
| 2026-11 | 21.8 | 5.7 | +0.2 cm | 95.914 |
| 2026-12 | 25.6 | 2.6 | +1.9 cm | 95.933 |
| 2027-01 | 28.6 | 1.9 | +4.0 cm | 95.972 |

- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.074 m (-7.4 cm)
- **Poziom na koniec stycznia 2027:** 95.972 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | 3.8 | +2.6 cm | 96.072 |
| 2026-03 | 33.9 | 5.4 | +1.9 cm | 96.092 |
| 2026-04 | 27.7 | 10.4 | +0.8 cm | 96.099 |
| 2026-05 | 46.4 | 15.1 | -1.2 cm | 96.087 |
| 2026-06 | 53.1 | 18.9 | -3.8 cm | 96.049 |
| 2026-07 | 66.7 | 20.4 | -3.9 cm | 96.01 |
| 2026-08 | 56.2 | 20.0 | -3.4 cm | 95.976 |
| 2026-09 | 43.3 | 16.0 | -1.8 cm | 95.959 |
| 2026-10 | 33.9 | 11.2 | -1.0 cm | 95.949 |
| 2026-11 | 38.8 | 5.7 | +0.7 cm | 95.956 |
| 2026-12 | 36.7 | 2.6 | +2.0 cm | 95.976 |
| 2027-01 | 39.8 | 1.9 | +4.1 cm | 96.017 |

- **Szansa realizacji:** 14.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.029 m (-2.9 cm)
- **Poziom na koniec stycznia 2027:** 96.017 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | 3.8 | +3.2 cm | 96.078 |
| 2026-03 | 49.5 | 5.4 | +2.5 cm | 96.103 |
| 2026-04 | 36.1 | 10.4 | +0.7 cm | 96.11 |
| 2026-05 | 64.7 | 15.1 | -1.4 cm | 96.096 |
| 2026-06 | 70.6 | 18.9 | -3.7 cm | 96.059 |
| 2026-07 | 102.3 | 20.4 | -2.5 cm | 96.035 |
| 2026-08 | 77.4 | 20.0 | -1.7 cm | 96.017 |
| 2026-09 | 62.5 | 16.0 | -1.8 cm | 96.0 |
| 2026-10 | 49.0 | 11.2 | -0.8 cm | 95.992 |
| 2026-11 | 46.6 | 5.7 | +0.9 cm | 96.001 |
| 2026-12 | 46.4 | 2.6 | +2.1 cm | 96.022 |
| 2027-01 | 51.6 | 1.9 | +4.6 cm | 96.068 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.022 m (+2.2 cm)
- **Poziom na koniec stycznia 2027:** 96.068 m n.p.m.



*Wygenerowano: 2026-02-15 12:15*