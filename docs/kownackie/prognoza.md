# Raport: Jezioro Kownackie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Kownackie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska linia: poziom z pliku `data/kownackie/data.csv` (pomiar na pierwszy dzień miesiąca). Przerywana pomarańczowa: wahania poziomu według modelu (scenariusz kumulatywny z prognozy zmiany miesięcznej).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Symulacje wariantów pogodowych (12 miesięcy do przodu)

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/kownackie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykres: pełny zakres historii (od 1974) + 12 miesięcy symulacji.

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

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów): **93.156 m n.p.m.** W stosunku do stanu na koniec stycznia 2026 (93.2357 m n.p.m.): ubędzie 0.080 m (-8.0 cm).


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.0 | 1.2 | +3.2 cm | 93.268 |
| 2026-03 | 33.4 | 4.2 | +1.9 cm | 93.286 |
| 2026-04 | 25.1 | 9.3 | +3.7 cm | 93.323 |
| 2026-05 | 46.0 | 13.9 | +2.0 cm | 93.344 |
| 2026-06 | 50.1 | 17.7 | -0.1 cm | 93.342 |
| 2026-07 | 69.9 | 19.7 | -4.1 cm | 93.301 |
| 2026-08 | 53.6 | 19.2 | -4.9 cm | 93.252 |
| 2026-09 | 40.3 | 14.8 | -5.6 cm | 93.196 |
| 2026-10 | 31.5 | 9.8 | -6.2 cm | 93.133 |
| 2026-11 | 34.6 | 4.7 | -2.2 cm | 93.111 |
| 2026-12 | 34.9 | 1.4 | +1.1 cm | 93.123 |
| 2027-01 | 38.4 | 0.0 | +3.4 cm | 93.156 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 491.7 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.080 m (-8.0 cm)
- **Poziom na koniec stycznia 2027:** 93.156 m n.p.m.

### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | -1.0 | +3.2 cm | 93.267 |
| 2026-03 | 22.8 | 3.0 | +1.5 cm | 93.282 |
| 2026-04 | 15.0 | 8.4 | +2.6 cm | 93.308 |
| 2026-05 | 34.0 | 12.8 | +0.5 cm | 93.313 |
| 2026-06 | 33.6 | 16.5 | -1.9 cm | 93.294 |
| 2026-07 | 53.9 | 18.8 | -5.5 cm | 93.239 |
| 2026-08 | 35.5 | 18.3 | -5.9 cm | 93.18 |
| 2026-09 | 22.7 | 13.7 | -6.6 cm | 93.114 |
| 2026-10 | 17.6 | 8.3 | -6.7 cm | 93.047 |
| 2026-11 | 21.8 | 3.6 | -1.7 cm | 93.031 |
| 2026-12 | 25.6 | -0.2 | +0.3 cm | 93.033 |
| 2027-01 | 28.6 | -1.9 | +2.1 cm | 93.054 |

- **Szansa realizacji:** 11.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.182 m (-18.2 cm)
- **Poziom na koniec stycznia 2027:** 93.054 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | -1.0 | +3.3 cm | 93.268 |
| 2026-03 | 33.9 | 3.0 | +1.5 cm | 93.283 |
| 2026-04 | 27.7 | 8.4 | +6.8 cm | 93.351 |
| 2026-05 | 46.4 | 12.8 | +6.7 cm | 93.418 |
| 2026-06 | 53.1 | 16.5 | +7.4 cm | 93.492 |
| 2026-07 | 66.7 | 18.8 | -3.9 cm | 93.453 |
| 2026-08 | 56.2 | 18.3 | -5.2 cm | 93.401 |
| 2026-09 | 43.3 | 13.7 | -5.5 cm | 93.346 |
| 2026-10 | 33.9 | 8.3 | -5.9 cm | 93.287 |
| 2026-11 | 38.8 | 3.6 | -1.7 cm | 93.27 |
| 2026-12 | 36.7 | -0.2 | +2.9 cm | 93.298 |
| 2027-01 | 39.8 | -1.9 | +5.2 cm | 93.351 |

- **Szansa realizacji:** 14.2 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.115 m (+11.5 cm)
- **Poziom na koniec stycznia 2027:** 93.351 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | -1.0 | +3.4 cm | 93.269 |
| 2026-03 | 49.5 | 3.0 | +1.5 cm | 93.285 |
| 2026-04 | 36.1 | 8.4 | +7.3 cm | 93.357 |
| 2026-05 | 64.7 | 12.8 | +7.3 cm | 93.43 |
| 2026-06 | 70.6 | 16.5 | +9.6 cm | 93.527 |
| 2026-07 | 102.3 | 18.8 | -2.4 cm | 93.502 |
| 2026-08 | 77.4 | 18.3 | -5.1 cm | 93.452 |
| 2026-09 | 62.5 | 13.7 | -6.1 cm | 93.391 |
| 2026-10 | 49.0 | 8.3 | -5.0 cm | 93.341 |
| 2026-11 | 46.6 | 3.6 | -0.4 cm | 93.337 |
| 2026-12 | 46.4 | -0.2 | +3.3 cm | 93.37 |
| 2027-01 | 51.6 | -1.9 | +5.4 cm | 93.424 |

- **Szansa realizacji:** 7.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.188 m (+18.8 cm)
- **Poziom na koniec stycznia 2027:** 93.424 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | 0.8 | +3.2 cm | 93.267 |
| 2026-03 | 22.8 | 4.3 | +2.2 cm | 93.289 |
| 2026-04 | 15.0 | 9.1 | +2.3 cm | 93.312 |
| 2026-05 | 34.0 | 13.7 | -0.2 cm | 93.31 |
| 2026-06 | 33.6 | 17.8 | -2.6 cm | 93.283 |
| 2026-07 | 53.9 | 19.8 | -6.2 cm | 93.222 |
| 2026-08 | 35.5 | 19.3 | -5.5 cm | 93.167 |
| 2026-09 | 22.7 | 14.7 | -6.5 cm | 93.102 |
| 2026-10 | 17.6 | 9.8 | -7.2 cm | 93.031 |
| 2026-11 | 21.8 | 4.8 | -2.5 cm | 93.006 |
| 2026-12 | 25.6 | 1.8 | -0.2 cm | 93.004 |
| 2027-01 | 28.6 | 0.1 | +1.6 cm | 93.02 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.216 m (-21.6 cm)
- **Poziom na koniec stycznia 2027:** 93.02 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | 0.8 | +3.3 cm | 93.268 |
| 2026-03 | 33.9 | 4.3 | +2.2 cm | 93.29 |
| 2026-04 | 27.7 | 9.1 | +3.3 cm | 93.324 |
| 2026-05 | 46.4 | 13.7 | +0.8 cm | 93.332 |
| 2026-06 | 53.1 | 17.8 | -0.7 cm | 93.325 |
| 2026-07 | 66.7 | 19.8 | -3.1 cm | 93.294 |
| 2026-08 | 56.2 | 19.3 | -4.0 cm | 93.254 |
| 2026-09 | 43.3 | 14.7 | -4.5 cm | 93.209 |
| 2026-10 | 33.9 | 9.8 | -5.9 cm | 93.149 |
| 2026-11 | 38.8 | 4.8 | -2.7 cm | 93.122 |
| 2026-12 | 36.7 | 1.8 | +2.4 cm | 93.146 |
| 2027-01 | 39.8 | 0.1 | +3.8 cm | 93.184 |

- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.052 m (-5.2 cm)
- **Poziom na koniec stycznia 2027:** 93.184 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | 0.8 | +3.4 cm | 93.269 |
| 2026-03 | 49.5 | 4.3 | +2.3 cm | 93.292 |
| 2026-04 | 36.1 | 9.1 | +3.9 cm | 93.331 |
| 2026-05 | 64.7 | 13.7 | +2.5 cm | 93.356 |
| 2026-06 | 70.6 | 17.8 | +1.7 cm | 93.373 |
| 2026-07 | 102.3 | 19.8 | -3.1 cm | 93.342 |
| 2026-08 | 77.4 | 19.3 | -4.8 cm | 93.295 |
| 2026-09 | 62.5 | 14.7 | -5.6 cm | 93.239 |
| 2026-10 | 49.0 | 9.8 | -4.9 cm | 93.19 |
| 2026-11 | 46.6 | 4.8 | -1.4 cm | 93.176 |
| 2026-12 | 46.4 | 1.8 | +2.8 cm | 93.204 |
| 2027-01 | 51.6 | 0.1 | +4.8 cm | 93.252 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.016 m (+1.6 cm)
- **Poziom na koniec stycznia 2027:** 93.252 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | 3.8 | +3.0 cm | 93.266 |
| 2026-03 | 22.8 | 5.4 | +1.9 cm | 93.284 |
| 2026-04 | 15.0 | 10.4 | +2.2 cm | 93.306 |
| 2026-05 | 34.0 | 15.1 | -0.5 cm | 93.301 |
| 2026-06 | 33.6 | 18.9 | -5.3 cm | 93.248 |
| 2026-07 | 53.9 | 20.4 | -6.2 cm | 93.187 |
| 2026-08 | 35.5 | 20.0 | -5.5 cm | 93.131 |
| 2026-09 | 22.7 | 16.0 | -6.5 cm | 93.067 |
| 2026-10 | 17.6 | 11.2 | -7.7 cm | 92.989 |
| 2026-11 | 21.8 | 5.7 | -3.1 cm | 92.958 |
| 2026-12 | 25.6 | 2.6 | -0.4 cm | 92.954 |
| 2027-01 | 28.6 | 1.9 | +1.5 cm | 92.969 |

- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.267 m (-26.7 cm)
- **Poziom na koniec stycznia 2027:** 92.969 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | 3.8 | +3.1 cm | 93.267 |
| 2026-03 | 33.9 | 5.4 | +2.0 cm | 93.286 |
| 2026-04 | 27.7 | 10.4 | +2.6 cm | 93.313 |
| 2026-05 | 46.4 | 15.1 | +0.8 cm | 93.321 |
| 2026-06 | 53.1 | 18.9 | -4.4 cm | 93.277 |
| 2026-07 | 66.7 | 20.4 | -3.4 cm | 93.243 |
| 2026-08 | 56.2 | 20.0 | -3.9 cm | 93.205 |
| 2026-09 | 43.3 | 16.0 | -4.4 cm | 93.16 |
| 2026-10 | 33.9 | 11.2 | -6.5 cm | 93.096 |
| 2026-11 | 38.8 | 5.7 | -3.2 cm | 93.064 |
| 2026-12 | 36.7 | 2.6 | -0.4 cm | 93.059 |
| 2027-01 | 39.8 | 1.9 | +3.3 cm | 93.092 |

- **Szansa realizacji:** 14.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.144 m (-14.4 cm)
- **Poziom na koniec stycznia 2027:** 93.092 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | 3.8 | +3.1 cm | 93.267 |
| 2026-03 | 49.5 | 5.4 | +2.2 cm | 93.289 |
| 2026-04 | 36.1 | 10.4 | +3.2 cm | 93.321 |
| 2026-05 | 64.7 | 15.1 | +2.3 cm | 93.344 |
| 2026-06 | 70.6 | 18.9 | -1.7 cm | 93.327 |
| 2026-07 | 102.3 | 20.4 | -2.4 cm | 93.303 |
| 2026-08 | 77.4 | 20.0 | -4.8 cm | 93.256 |
| 2026-09 | 62.5 | 16.0 | -5.8 cm | 93.198 |
| 2026-10 | 49.0 | 11.2 | -5.5 cm | 93.142 |
| 2026-11 | 46.6 | 5.7 | -1.6 cm | 93.126 |
| 2026-12 | 46.4 | 2.6 | +0.2 cm | 93.128 |
| 2027-01 | 51.6 | 1.9 | +3.5 cm | 93.164 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.072 m (-7.2 cm)
- **Poziom na koniec stycznia 2027:** 93.164 m n.p.m.



*Wygenerowano: 2026-02-15 12:22*