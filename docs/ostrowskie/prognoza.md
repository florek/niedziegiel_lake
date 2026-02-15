# Raport: Jezioro Ostrowskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Ostrowskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/ostrowskie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Symulacje wariantów pogodowych (12 miesięcy do przodu)

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/ostrowskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykres: pełny zakres historii (od 1974) + 12 miesięcy symulacji.

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

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów): **94.487 m n.p.m.** W stosunku do stanu na koniec stycznia 2026 (94.6849 m n.p.m.): ubędzie 0.198 m (-19.8 cm).


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.0 | 1.2 | +1.9 cm | 94.704 |
| 2026-03 | 33.4 | 4.2 | +2.4 cm | 94.728 |
| 2026-04 | 25.1 | 9.3 | +1.3 cm | 94.741 |
| 2026-05 | 46.0 | 13.9 | +1.3 cm | 94.754 |
| 2026-06 | 50.1 | 17.7 | -0.8 cm | 94.746 |
| 2026-07 | 69.9 | 19.7 | -3.1 cm | 94.715 |
| 2026-08 | 53.6 | 19.2 | -5.1 cm | 94.664 |
| 2026-09 | 40.3 | 14.8 | -5.4 cm | 94.61 |
| 2026-10 | 31.5 | 9.8 | -5.2 cm | 94.558 |
| 2026-11 | 34.6 | 4.7 | -5.1 cm | 94.508 |
| 2026-12 | 34.9 | 1.4 | -2.3 cm | 94.485 |
| 2027-01 | 38.4 | 0.0 | +0.2 cm | 94.487 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 491.7 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.198 m (-19.8 cm)
- **Poziom na koniec stycznia 2027:** 94.487 m n.p.m.

### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | -1.0 | +1.6 cm | 94.701 |
| 2026-03 | 22.8 | 3.0 | +2.3 cm | 94.724 |
| 2026-04 | 15.0 | 8.4 | +2.3 cm | 94.747 |
| 2026-05 | 34.0 | 12.8 | +1.1 cm | 94.758 |
| 2026-06 | 33.6 | 16.5 | -1.1 cm | 94.747 |
| 2026-07 | 53.9 | 18.8 | -1.8 cm | 94.729 |
| 2026-08 | 35.5 | 18.3 | -4.9 cm | 94.68 |
| 2026-09 | 22.7 | 13.7 | -7.0 cm | 94.61 |
| 2026-10 | 17.6 | 8.3 | -6.9 cm | 94.542 |
| 2026-11 | 21.8 | 3.6 | -7.2 cm | 94.47 |
| 2026-12 | 25.6 | -0.2 | -2.9 cm | 94.441 |
| 2027-01 | 28.6 | -1.9 | -0.2 cm | 94.439 |

- **Szansa realizacji:** 11.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.246 m (-24.6 cm)
- **Poziom na koniec stycznia 2027:** 94.439 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | -1.0 | +1.8 cm | 94.703 |
| 2026-03 | 33.9 | 3.0 | +2.6 cm | 94.729 |
| 2026-04 | 27.7 | 8.4 | +2.8 cm | 94.757 |
| 2026-05 | 46.4 | 12.8 | +2.5 cm | 94.782 |
| 2026-06 | 53.1 | 16.5 | +2.2 cm | 94.804 |
| 2026-07 | 66.7 | 18.8 | -1.3 cm | 94.791 |
| 2026-08 | 56.2 | 18.3 | -4.0 cm | 94.751 |
| 2026-09 | 43.3 | 13.7 | -4.3 cm | 94.708 |
| 2026-10 | 33.9 | 8.3 | -4.0 cm | 94.667 |
| 2026-11 | 38.8 | 3.6 | -4.7 cm | 94.62 |
| 2026-12 | 36.7 | -0.2 | -0.8 cm | 94.612 |
| 2027-01 | 39.8 | -1.9 | +0.9 cm | 94.621 |

- **Szansa realizacji:** 14.2 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.064 m (-6.4 cm)
- **Poziom na koniec stycznia 2027:** 94.621 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | -1.0 | +2.1 cm | 94.706 |
| 2026-03 | 49.5 | 3.0 | +3.1 cm | 94.737 |
| 2026-04 | 36.1 | 8.4 | +2.7 cm | 94.764 |
| 2026-05 | 64.7 | 12.8 | +5.1 cm | 94.815 |
| 2026-06 | 70.6 | 16.5 | +3.7 cm | 94.852 |
| 2026-07 | 102.3 | 18.8 | -0.3 cm | 94.849 |
| 2026-08 | 77.4 | 18.3 | -2.9 cm | 94.82 |
| 2026-09 | 62.5 | 13.7 | -2.4 cm | 94.796 |
| 2026-10 | 49.0 | 8.3 | -1.4 cm | 94.782 |
| 2026-11 | 46.6 | 3.6 | -0.4 cm | 94.778 |
| 2026-12 | 46.4 | -0.2 | +1.3 cm | 94.791 |
| 2027-01 | 51.6 | -1.9 | +3.5 cm | 94.825 |

- **Szansa realizacji:** 7.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.140 m (+14.0 cm)
- **Poziom na koniec stycznia 2027:** 94.825 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | 0.8 | +1.6 cm | 94.701 |
| 2026-03 | 22.8 | 4.3 | +2.1 cm | 94.722 |
| 2026-04 | 15.0 | 9.1 | +0.5 cm | 94.727 |
| 2026-05 | 34.0 | 13.7 | +0.8 cm | 94.736 |
| 2026-06 | 33.6 | 17.8 | -2.3 cm | 94.713 |
| 2026-07 | 53.9 | 19.8 | -4.4 cm | 94.669 |
| 2026-08 | 35.5 | 19.3 | -7.2 cm | 94.597 |
| 2026-09 | 22.7 | 14.7 | -7.3 cm | 94.524 |
| 2026-10 | 17.6 | 9.8 | -7.4 cm | 94.45 |
| 2026-11 | 21.8 | 4.8 | -7.2 cm | 94.378 |
| 2026-12 | 25.6 | 1.8 | -4.6 cm | 94.332 |
| 2027-01 | 28.6 | 0.1 | -1.9 cm | 94.313 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.372 m (-37.2 cm)
- **Poziom na koniec stycznia 2027:** 94.313 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | 0.8 | +1.9 cm | 94.704 |
| 2026-03 | 33.9 | 4.3 | +2.3 cm | 94.727 |
| 2026-04 | 27.7 | 9.1 | +0.5 cm | 94.732 |
| 2026-05 | 46.4 | 13.7 | +1.2 cm | 94.744 |
| 2026-06 | 53.1 | 17.8 | -1.7 cm | 94.727 |
| 2026-07 | 66.7 | 19.8 | -3.8 cm | 94.689 |
| 2026-08 | 56.2 | 19.3 | -5.5 cm | 94.634 |
| 2026-09 | 43.3 | 14.7 | -4.7 cm | 94.587 |
| 2026-10 | 33.9 | 9.8 | -4.9 cm | 94.538 |
| 2026-11 | 38.8 | 4.8 | -5.2 cm | 94.487 |
| 2026-12 | 36.7 | 1.8 | -3.0 cm | 94.457 |
| 2027-01 | 39.8 | 0.1 | +0.2 cm | 94.458 |

- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.227 m (-22.7 cm)
- **Poziom na koniec stycznia 2027:** 94.458 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | 0.8 | +2.1 cm | 94.706 |
| 2026-03 | 49.5 | 4.3 | +2.9 cm | 94.735 |
| 2026-04 | 36.1 | 9.1 | +1.4 cm | 94.75 |
| 2026-05 | 64.7 | 13.7 | +2.2 cm | 94.772 |
| 2026-06 | 70.6 | 17.8 | -1.1 cm | 94.761 |
| 2026-07 | 102.3 | 19.8 | -2.2 cm | 94.739 |
| 2026-08 | 77.4 | 19.3 | -3.4 cm | 94.705 |
| 2026-09 | 62.5 | 14.7 | -3.0 cm | 94.676 |
| 2026-10 | 49.0 | 9.8 | -2.2 cm | 94.653 |
| 2026-11 | 46.6 | 4.8 | -0.9 cm | 94.644 |
| 2026-12 | 46.4 | 1.8 | +0.4 cm | 94.648 |
| 2027-01 | 51.6 | 0.1 | +1.6 cm | 94.665 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.020 m (-2.0 cm)
- **Poziom na koniec stycznia 2027:** 94.665 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | 3.8 | +1.7 cm | 94.702 |
| 2026-03 | 22.8 | 5.4 | +2.0 cm | 94.722 |
| 2026-04 | 15.0 | 10.4 | +0.6 cm | 94.728 |
| 2026-05 | 34.0 | 15.1 | -0.5 cm | 94.722 |
| 2026-06 | 33.6 | 18.9 | -2.3 cm | 94.699 |
| 2026-07 | 53.9 | 20.4 | -5.1 cm | 94.649 |
| 2026-08 | 35.5 | 20.0 | -7.1 cm | 94.578 |
| 2026-09 | 22.7 | 16.0 | -8.4 cm | 94.494 |
| 2026-10 | 17.6 | 11.2 | -8.0 cm | 94.414 |
| 2026-11 | 21.8 | 5.7 | -7.5 cm | 94.339 |
| 2026-12 | 25.6 | 2.6 | -4.6 cm | 94.293 |
| 2027-01 | 28.6 | 1.9 | -1.9 cm | 94.274 |

- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.411 m (-41.1 cm)
- **Poziom na koniec stycznia 2027:** 94.274 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | 3.8 | +2.0 cm | 94.705 |
| 2026-03 | 33.9 | 5.4 | +2.2 cm | 94.727 |
| 2026-04 | 27.7 | 10.4 | +0.5 cm | 94.732 |
| 2026-05 | 46.4 | 15.1 | +0.1 cm | 94.733 |
| 2026-06 | 53.1 | 18.9 | -1.8 cm | 94.715 |
| 2026-07 | 66.7 | 20.4 | -4.5 cm | 94.671 |
| 2026-08 | 56.2 | 20.0 | -5.5 cm | 94.616 |
| 2026-09 | 43.3 | 16.0 | -5.4 cm | 94.562 |
| 2026-10 | 33.9 | 11.2 | -5.3 cm | 94.509 |
| 2026-11 | 38.8 | 5.7 | -5.4 cm | 94.455 |
| 2026-12 | 36.7 | 2.6 | -3.0 cm | 94.425 |
| 2027-01 | 39.8 | 1.9 | +0.2 cm | 94.427 |

- **Szansa realizacji:** 14.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.258 m (-25.8 cm)
- **Poziom na koniec stycznia 2027:** 94.427 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | 3.8 | +2.2 cm | 94.707 |
| 2026-03 | 49.5 | 5.4 | +2.8 cm | 94.735 |
| 2026-04 | 36.1 | 10.4 | +1.5 cm | 94.75 |
| 2026-05 | 64.7 | 15.1 | +0.8 cm | 94.758 |
| 2026-06 | 70.6 | 18.9 | -1.4 cm | 94.744 |
| 2026-07 | 102.3 | 20.4 | -2.9 cm | 94.715 |
| 2026-08 | 77.4 | 20.0 | -3.4 cm | 94.681 |
| 2026-09 | 62.5 | 16.0 | -3.8 cm | 94.643 |
| 2026-10 | 49.0 | 11.2 | -4.6 cm | 94.597 |
| 2026-11 | 46.6 | 5.7 | -2.9 cm | 94.568 |
| 2026-12 | 46.4 | 2.6 | +0.4 cm | 94.572 |
| 2027-01 | 51.6 | 1.9 | +1.5 cm | 94.587 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.098 m (-9.8 cm)
- **Poziom na koniec stycznia 2027:** 94.587 m n.p.m.



*Wygenerowano: 2026-02-15 14:10*