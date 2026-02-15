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
| zimny, suchy | 8.0 |
| zimny, normalny | 12.7 |
| zimny, wilgotny | 10.1 |
| normalny, suchy | 8.5 |
| normalny, normalny | 14.6 |
| normalny, wilgotny | 10.8 |
| ciepły, suchy | 8.6 |
| ciepły, normalny | 15.6 |
| ciepły, wilgotny | 11.1 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów): **93.388 m n.p.m.** W stosunku do stanu na koniec stycznia 2026 (93.45 m n.p.m.): ubędzie 0.062 m (-6.2 cm).


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 36.2 | 1.2 | +0.3 cm | 93.453 |
| 2026-03 | 38.7 | 4.1 | +3.2 cm | 93.484 |
| 2026-04 | 26.9 | 9.1 | +4.1 cm | 93.525 |
| 2026-05 | 52.6 | 13.9 | +2.4 cm | 93.549 |
| 2026-06 | 51.4 | 17.6 | +0.5 cm | 93.554 |
| 2026-07 | 74.0 | 19.7 | -3.9 cm | 93.515 |
| 2026-08 | 59.6 | 19.2 | -4.9 cm | 93.466 |
| 2026-09 | 43.8 | 14.6 | -5.4 cm | 93.412 |
| 2026-10 | 35.8 | 9.8 | -5.8 cm | 93.354 |
| 2026-11 | 36.8 | 4.8 | -1.8 cm | 93.336 |
| 2026-12 | 37.3 | 1.3 | +1.5 cm | 93.351 |
| 2027-01 | 40.7 | 0.0 | +3.7 cm | 93.388 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.6 °C
- **Suma opadu (prognoza):** 533.8 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.062 m (-6.2 cm)
- **Poziom na koniec stycznia 2027:** 93.388 m n.p.m.

### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 26.4 | -1.1 | +0.1 cm | 93.451 |
| 2026-03 | 25.8 | 2.9 | +2.5 cm | 93.475 |
| 2026-04 | 14.3 | 8.3 | +2.9 cm | 93.504 |
| 2026-05 | 33.8 | 12.9 | +0.9 cm | 93.513 |
| 2026-06 | 32.7 | 16.4 | -2.1 cm | 93.492 |
| 2026-07 | 52.1 | 18.7 | -5.5 cm | 93.438 |
| 2026-08 | 34.6 | 18.2 | -5.9 cm | 93.378 |
| 2026-09 | 22.5 | 13.6 | -6.7 cm | 93.311 |
| 2026-10 | 17.1 | 8.2 | -5.6 cm | 93.255 |
| 2026-11 | 20.3 | 3.5 | -1.3 cm | 93.241 |
| 2026-12 | 25.8 | -0.2 | +0.2 cm | 93.243 |
| 2027-01 | 29.0 | -1.9 | +1.7 cm | 93.26 |

- **Szansa realizacji:** 8.0 %
- **Średnia temperatura roczna (prognoza):** 8.3 °C
- **Suma opadu (prognoza):** 334.5 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.190 m (-19.0 cm)
- **Poziom na koniec stycznia 2027:** 93.26 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | -1.1 | +0.2 cm | 93.452 |
| 2026-03 | 37.7 | 2.9 | +3.1 cm | 93.483 |
| 2026-04 | 27.7 | 8.3 | +6.9 cm | 93.552 |
| 2026-05 | 48.9 | 12.9 | +6.5 cm | 93.617 |
| 2026-06 | 49.9 | 16.4 | +1.8 cm | 93.634 |
| 2026-07 | 65.4 | 18.7 | -3.9 cm | 93.595 |
| 2026-08 | 58.8 | 18.2 | -5.3 cm | 93.542 |
| 2026-09 | 41.0 | 13.6 | -4.7 cm | 93.496 |
| 2026-10 | 33.9 | 8.2 | -6.7 cm | 93.429 |
| 2026-11 | 38.8 | 3.5 | -1.3 cm | 93.416 |
| 2026-12 | 37.6 | -0.2 | +3.0 cm | 93.446 |
| 2027-01 | 40.0 | -1.9 | +5.2 cm | 93.498 |

- **Szansa realizacji:** 12.7 %
- **Średnia temperatura roczna (prognoza):** 8.3 °C
- **Suma opadu (prognoza):** 514.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.048 m (+4.8 cm)
- **Poziom na koniec stycznia 2027:** 93.498 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.3 | -1.1 | +0.6 cm | 93.456 |
| 2026-03 | 50.2 | 2.9 | +3.9 cm | 93.495 |
| 2026-04 | 35.5 | 8.3 | +7.4 cm | 93.569 |
| 2026-05 | 72.4 | 12.9 | +7.1 cm | 93.64 |
| 2026-06 | 68.1 | 16.4 | +9.8 cm | 93.738 |
| 2026-07 | 102.7 | 18.7 | -2.4 cm | 93.715 |
| 2026-08 | 80.3 | 18.2 | -5.1 cm | 93.664 |
| 2026-09 | 64.3 | 13.6 | -5.9 cm | 93.605 |
| 2026-10 | 52.8 | 8.2 | -4.2 cm | 93.563 |
| 2026-11 | 46.8 | 3.5 | +0.6 cm | 93.569 |
| 2026-12 | 46.0 | -0.2 | +4.1 cm | 93.61 |
| 2027-01 | 50.8 | -1.9 | +5.7 cm | 93.667 |

- **Szansa realizacji:** 10.1 %
- **Średnia temperatura roczna (prognoza):** 8.3 °C
- **Suma opadu (prognoza):** 716.5 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.217 m (+21.7 cm)
- **Poziom na koniec stycznia 2027:** 93.667 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 26.4 | 0.8 | +0.1 cm | 93.451 |
| 2026-03 | 25.8 | 4.2 | +2.7 cm | 93.478 |
| 2026-04 | 14.3 | 9.1 | +2.7 cm | 93.505 |
| 2026-05 | 33.8 | 13.7 | -0.1 cm | 93.504 |
| 2026-06 | 32.7 | 17.3 | -2.8 cm | 93.476 |
| 2026-07 | 52.1 | 19.8 | -6.3 cm | 93.413 |
| 2026-08 | 34.6 | 19.3 | -5.6 cm | 93.358 |
| 2026-09 | 22.5 | 14.3 | -6.6 cm | 93.292 |
| 2026-10 | 17.1 | 9.8 | -5.5 cm | 93.237 |
| 2026-11 | 20.3 | 5.0 | -2.2 cm | 93.215 |
| 2026-12 | 25.8 | 1.7 | -0.0 cm | 93.215 |
| 2027-01 | 29.0 | -0.1 | +1.4 cm | 93.229 |

- **Szansa realizacji:** 8.5 %
- **Średnia temperatura roczna (prognoza):** 9.6 °C
- **Suma opadu (prognoza):** 334.5 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.221 m (-22.1 cm)
- **Poziom na koniec stycznia 2027:** 93.229 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | 0.8 | +0.2 cm | 93.452 |
| 2026-03 | 37.7 | 4.2 | +3.3 cm | 93.485 |
| 2026-04 | 27.7 | 9.1 | +3.7 cm | 93.522 |
| 2026-05 | 48.9 | 13.7 | +0.8 cm | 93.53 |
| 2026-06 | 49.9 | 17.3 | -1.1 cm | 93.519 |
| 2026-07 | 65.4 | 19.8 | -4.0 cm | 93.479 |
| 2026-08 | 58.8 | 19.3 | -4.2 cm | 93.437 |
| 2026-09 | 41.0 | 14.3 | -4.6 cm | 93.391 |
| 2026-10 | 33.9 | 9.8 | -6.7 cm | 93.324 |
| 2026-11 | 38.8 | 5.0 | -2.7 cm | 93.297 |
| 2026-12 | 37.6 | 1.7 | +2.5 cm | 93.322 |
| 2027-01 | 40.0 | -0.1 | +4.7 cm | 93.369 |

- **Szansa realizacji:** 14.6 %
- **Średnia temperatura roczna (prognoza):** 9.6 °C
- **Suma opadu (prognoza):** 514.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.081 m (-8.1 cm)
- **Poziom na koniec stycznia 2027:** 93.369 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.3 | 0.8 | +0.6 cm | 93.456 |
| 2026-03 | 50.2 | 4.2 | +4.2 cm | 93.498 |
| 2026-04 | 35.5 | 9.1 | +4.3 cm | 93.541 |
| 2026-05 | 72.4 | 13.7 | +2.3 cm | 93.564 |
| 2026-06 | 68.1 | 17.3 | +1.2 cm | 93.576 |
| 2026-07 | 102.7 | 19.8 | -3.1 cm | 93.545 |
| 2026-08 | 80.3 | 19.3 | -4.8 cm | 93.497 |
| 2026-09 | 64.3 | 14.3 | -5.4 cm | 93.444 |
| 2026-10 | 52.8 | 9.8 | -4.1 cm | 93.402 |
| 2026-11 | 46.8 | 5.0 | -0.9 cm | 93.393 |
| 2026-12 | 46.0 | 1.7 | +3.2 cm | 93.426 |
| 2027-01 | 50.8 | -0.1 | +4.8 cm | 93.474 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 9.6 °C
- **Suma opadu (prognoza):** 716.5 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.024 m (+2.4 cm)
- **Poziom na koniec stycznia 2027:** 93.474 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 26.4 | 3.6 | -0.0 cm | 93.45 |
| 2026-03 | 25.8 | 5.0 | +2.3 cm | 93.473 |
| 2026-04 | 14.3 | 9.8 | +2.3 cm | 93.496 |
| 2026-05 | 33.8 | 15.1 | +0.3 cm | 93.499 |
| 2026-06 | 32.7 | 18.9 | -3.3 cm | 93.466 |
| 2026-07 | 52.1 | 20.4 | -6.3 cm | 93.403 |
| 2026-08 | 34.6 | 19.9 | -5.6 cm | 93.347 |
| 2026-09 | 22.5 | 15.9 | -6.6 cm | 93.281 |
| 2026-10 | 17.1 | 11.2 | -6.2 cm | 93.219 |
| 2026-11 | 20.3 | 5.7 | -2.9 cm | 93.19 |
| 2026-12 | 25.8 | 2.4 | -0.4 cm | 93.187 |
| 2027-01 | 29.0 | 1.9 | +1.3 cm | 93.199 |

- **Szansa realizacji:** 8.6 %
- **Średnia temperatura roczna (prognoza):** 10.8 °C
- **Suma opadu (prognoza):** 334.5 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.251 m (-25.1 cm)
- **Poziom na koniec stycznia 2027:** 93.199 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | 3.6 | +0.1 cm | 93.451 |
| 2026-03 | 37.7 | 5.0 | +2.9 cm | 93.48 |
| 2026-04 | 27.7 | 9.8 | +2.8 cm | 93.508 |
| 2026-05 | 48.9 | 15.1 | +0.7 cm | 93.516 |
| 2026-06 | 49.9 | 18.9 | -0.9 cm | 93.507 |
| 2026-07 | 65.4 | 20.4 | -2.9 cm | 93.478 |
| 2026-08 | 58.8 | 19.9 | -4.1 cm | 93.437 |
| 2026-09 | 41.0 | 15.9 | -4.5 cm | 93.391 |
| 2026-10 | 33.9 | 11.2 | -7.4 cm | 93.318 |
| 2026-11 | 38.8 | 5.7 | -3.4 cm | 93.284 |
| 2026-12 | 37.6 | 2.4 | -0.4 cm | 93.28 |
| 2027-01 | 40.0 | 1.9 | +3.4 cm | 93.314 |

- **Szansa realizacji:** 15.6 %
- **Średnia temperatura roczna (prognoza):** 10.8 °C
- **Suma opadu (prognoza):** 514.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.136 m (-13.6 cm)
- **Poziom na koniec stycznia 2027:** 93.314 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.3 | 3.6 | +0.4 cm | 93.454 |
| 2026-03 | 50.2 | 5.0 | +3.3 cm | 93.487 |
| 2026-04 | 35.5 | 9.8 | +3.3 cm | 93.52 |
| 2026-05 | 72.4 | 15.1 | +2.3 cm | 93.544 |
| 2026-06 | 68.1 | 18.9 | +1.3 cm | 93.556 |
| 2026-07 | 102.7 | 20.4 | -2.1 cm | 93.535 |
| 2026-08 | 80.3 | 19.9 | -4.8 cm | 93.487 |
| 2026-09 | 64.3 | 15.9 | -5.6 cm | 93.431 |
| 2026-10 | 52.8 | 11.2 | -4.7 cm | 93.385 |
| 2026-11 | 46.8 | 5.7 | -1.0 cm | 93.374 |
| 2026-12 | 46.0 | 2.4 | +0.3 cm | 93.377 |
| 2027-01 | 50.8 | 1.9 | +3.5 cm | 93.412 |

- **Szansa realizacji:** 11.1 %
- **Średnia temperatura roczna (prognoza):** 10.8 °C
- **Suma opadu (prognoza):** 716.5 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.038 m (-3.8 cm)
- **Poziom na koniec stycznia 2027:** 93.412 m n.p.m.



*Wygenerowano: 2026-02-15 12:19*