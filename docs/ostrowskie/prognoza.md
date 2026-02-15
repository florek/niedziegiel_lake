# Raport: Jezioro Ostrowskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Ostrowskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/ostrowskie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/ostrowskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 11.3 | 94.505 | 94.451 |
| zimny, normalny | 14.2 | 94.552 | 94.765 |
| zimny, wilgotny | 7.1 | 94.6 | 95.206 |
| normalny, suchy | 11.7 | 94.454 | 94.396 |
| normalny, normalny | 15.2 | 94.493 | 94.589 |
| normalny, wilgotny | 7.2 | 94.544 | 94.953 |
| ciepły, suchy | 11.5 | 94.41 | 94.357 |
| ciepły, normalny | 14.5 | 94.441 | 94.568 |
| ciepły, wilgotny | 7.2 | 94.513 | 94.839 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (94.6849 m n.p.m.):
- **Model drenażowy:** 94.494 m n.p.m. – ubędzie 0.191 m (-19.1 cm)
- **Model naturalny (sprzed drenażu):** 94.634 m n.p.m. – ubędzie 0.051 m (-5.1 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.0 | 1.2 | +2.0 cm | 94.705 | +0.8 cm | 94.692 |
| 2026-03 | 33.4 | 4.2 | +1.9 cm | 94.724 | +1.8 cm | 94.71 |
| 2026-04 | 25.1 | 9.3 | +1.1 cm | 94.735 | +2.1 cm | 94.731 |
| 2026-05 | 46.0 | 13.9 | -0.5 cm | 94.731 | +2.9 cm | 94.76 |
| 2026-06 | 50.1 | 17.7 | -2.4 cm | 94.706 | +1.2 cm | 94.772 |
| 2026-07 | 69.9 | 19.7 | -3.5 cm | 94.672 | -0.7 cm | 94.766 |
| 2026-08 | 53.6 | 19.2 | -3.8 cm | 94.634 | -3.0 cm | 94.736 |
| 2026-09 | 40.3 | 14.8 | -4.1 cm | 94.593 | -3.8 cm | 94.698 |
| 2026-10 | 31.5 | 9.8 | -4.3 cm | 94.55 | -3.4 cm | 94.664 |
| 2026-11 | 34.6 | 4.7 | -3.6 cm | 94.513 | -2.6 cm | 94.638 |
| 2026-12 | 34.9 | 1.4 | -2.5 cm | 94.488 | -1.6 cm | 94.622 |
| 2027-01 | 38.4 | 0.0 | +0.6 cm | 94.494 | +1.2 cm | 94.634 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 491.7 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.191 m (-19.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.494 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.051 m (-5.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.634 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | -1.0 | +2.2 cm | 94.707 | +0.6 cm | 94.691 |
| 2026-03 | 22.8 | 3.0 | +2.1 cm | 94.728 | +1.0 cm | 94.701 |
| 2026-04 | 15.0 | 8.4 | +0.9 cm | 94.737 | +1.2 cm | 94.713 |
| 2026-05 | 34.0 | 12.8 | -0.6 cm | 94.731 | +0.4 cm | 94.716 |
| 2026-06 | 33.6 | 16.5 | -2.5 cm | 94.706 | -1.4 cm | 94.703 |
| 2026-07 | 53.9 | 18.8 | -3.3 cm | 94.674 | -3.1 cm | 94.672 |
| 2026-08 | 35.5 | 18.3 | -3.6 cm | 94.638 | -4.7 cm | 94.624 |
| 2026-09 | 22.7 | 13.7 | -4.0 cm | 94.598 | -4.5 cm | 94.579 |
| 2026-10 | 17.6 | 8.3 | -4.1 cm | 94.557 | -4.4 cm | 94.535 |
| 2026-11 | 21.8 | 3.6 | -3.5 cm | 94.522 | -4.6 cm | 94.489 |
| 2026-12 | 25.6 | -0.2 | -2.3 cm | 94.498 | -2.9 cm | 94.46 |
| 2027-01 | 28.6 | -1.9 | +0.6 cm | 94.505 | -0.9 cm | 94.451 |

- **Szansa realizacji:** 11.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.180 m (-18.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.505 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.234 m (-23.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.451 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | -1.0 | +2.1 cm | 94.706 | +0.7 cm | 94.692 |
| 2026-03 | 33.9 | 3.0 | +2.3 cm | 94.729 | +1.4 cm | 94.705 |
| 2026-04 | 27.7 | 8.4 | +1.8 cm | 94.747 | +2.7 cm | 94.732 |
| 2026-05 | 46.4 | 12.8 | -0.2 cm | 94.744 | +4.2 cm | 94.774 |
| 2026-06 | 53.1 | 16.5 | -2.0 cm | 94.724 | +4.6 cm | 94.821 |
| 2026-07 | 66.7 | 18.8 | -3.1 cm | 94.693 | +2.3 cm | 94.843 |
| 2026-08 | 56.2 | 18.3 | -3.2 cm | 94.661 | -2.3 cm | 94.82 |
| 2026-09 | 43.3 | 13.7 | -3.6 cm | 94.625 | -3.5 cm | 94.785 |
| 2026-10 | 33.9 | 8.3 | -3.8 cm | 94.587 | -3.3 cm | 94.753 |
| 2026-11 | 38.8 | 3.6 | -3.4 cm | 94.553 | -1.3 cm | 94.74 |
| 2026-12 | 36.7 | -0.2 | -1.6 cm | 94.536 | +0.0 cm | 94.74 |
| 2027-01 | 39.8 | -1.9 | +1.5 cm | 94.552 | +2.6 cm | 94.765 |

- **Szansa realizacji:** 14.2 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.133 m (-13.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.552 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.080 m (+8.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.765 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | -1.0 | +1.9 cm | 94.704 | +1.5 cm | 94.7 |
| 2026-03 | 49.5 | 3.0 | +2.3 cm | 94.728 | +3.7 cm | 94.737 |
| 2026-04 | 36.1 | 8.4 | +2.3 cm | 94.751 | +6.5 cm | 94.803 |
| 2026-05 | 64.7 | 12.8 | +0.9 cm | 94.759 | +11.6 cm | 94.919 |
| 2026-06 | 70.6 | 16.5 | -1.7 cm | 94.743 | +11.6 cm | 95.035 |
| 2026-07 | 102.3 | 18.8 | -3.2 cm | 94.711 | +7.7 cm | 95.112 |
| 2026-08 | 77.4 | 18.3 | -3.1 cm | 94.68 | +5.4 cm | 95.165 |
| 2026-09 | 62.5 | 13.7 | -3.0 cm | 94.65 | +1.3 cm | 95.178 |
| 2026-10 | 49.0 | 8.3 | -3.2 cm | 94.618 | -1.4 cm | 95.164 |
| 2026-11 | 46.6 | 3.6 | -2.7 cm | 94.592 | -1.6 cm | 95.148 |
| 2026-12 | 46.4 | -0.2 | -1.2 cm | 94.579 | +0.9 cm | 95.157 |
| 2027-01 | 51.6 | -1.9 | +2.1 cm | 94.6 | +5.0 cm | 95.206 |

- **Szansa realizacji:** 7.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.085 m (-8.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.6 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.521 m (+52.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.206 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | 0.8 | +2.0 cm | 94.705 | +0.5 cm | 94.69 |
| 2026-03 | 22.8 | 4.3 | +1.8 cm | 94.723 | +1.3 cm | 94.703 |
| 2026-04 | 15.0 | 9.1 | +0.4 cm | 94.727 | +0.6 cm | 94.709 |
| 2026-05 | 34.0 | 13.7 | -1.0 cm | 94.717 | -0.2 cm | 94.706 |
| 2026-06 | 33.6 | 17.8 | -2.9 cm | 94.688 | -2.3 cm | 94.683 |
| 2026-07 | 53.9 | 19.8 | -3.7 cm | 94.651 | -3.4 cm | 94.649 |
| 2026-08 | 35.5 | 19.3 | -4.2 cm | 94.609 | -5.4 cm | 94.595 |
| 2026-09 | 22.7 | 14.7 | -4.5 cm | 94.564 | -5.0 cm | 94.546 |
| 2026-10 | 17.6 | 9.8 | -4.4 cm | 94.521 | -4.7 cm | 94.499 |
| 2026-11 | 21.8 | 4.8 | -3.8 cm | 94.483 | -4.8 cm | 94.451 |
| 2026-12 | 25.6 | 1.8 | -2.8 cm | 94.455 | -3.9 cm | 94.412 |
| 2027-01 | 28.6 | 0.1 | -0.1 cm | 94.454 | -1.6 cm | 94.396 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.231 m (-23.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.454 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.289 m (-28.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.396 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | 0.8 | +1.9 cm | 94.704 | +0.6 cm | 94.691 |
| 2026-03 | 33.9 | 4.3 | +2.0 cm | 94.724 | +1.6 cm | 94.707 |
| 2026-04 | 27.7 | 9.1 | +1.2 cm | 94.736 | +1.8 cm | 94.724 |
| 2026-05 | 46.4 | 13.7 | -0.7 cm | 94.729 | +1.5 cm | 94.739 |
| 2026-06 | 53.1 | 17.8 | -2.3 cm | 94.706 | -0.5 cm | 94.734 |
| 2026-07 | 66.7 | 19.8 | -3.5 cm | 94.671 | -2.5 cm | 94.71 |
| 2026-08 | 56.2 | 19.3 | -3.7 cm | 94.634 | -3.6 cm | 94.674 |
| 2026-09 | 43.3 | 14.7 | -4.3 cm | 94.59 | -4.8 cm | 94.626 |
| 2026-10 | 33.9 | 9.8 | -4.1 cm | 94.549 | -3.2 cm | 94.594 |
| 2026-11 | 38.8 | 4.8 | -3.6 cm | 94.513 | -1.6 cm | 94.579 |
| 2026-12 | 36.7 | 1.8 | -2.8 cm | 94.486 | -0.9 cm | 94.569 |
| 2027-01 | 39.8 | 0.1 | +0.8 cm | 94.493 | +2.0 cm | 94.589 |

- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.192 m (-19.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.493 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.096 m (-9.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.589 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | 0.8 | +1.7 cm | 94.702 | +1.5 cm | 94.7 |
| 2026-03 | 49.5 | 4.3 | +2.0 cm | 94.722 | +3.9 cm | 94.739 |
| 2026-04 | 36.1 | 9.1 | +1.9 cm | 94.741 | +5.2 cm | 94.791 |
| 2026-05 | 64.7 | 13.7 | +0.6 cm | 94.747 | +7.4 cm | 94.865 |
| 2026-06 | 70.6 | 17.8 | -2.1 cm | 94.726 | +6.5 cm | 94.931 |
| 2026-07 | 102.3 | 19.8 | -3.6 cm | 94.69 | +5.6 cm | 94.987 |
| 2026-08 | 77.4 | 19.3 | -3.6 cm | 94.654 | -0.7 cm | 94.98 |
| 2026-09 | 62.5 | 14.7 | -3.7 cm | 94.617 | -2.8 cm | 94.952 |
| 2026-10 | 49.0 | 9.8 | -3.7 cm | 94.58 | -2.6 cm | 94.927 |
| 2026-11 | 46.6 | 4.8 | -3.0 cm | 94.549 | -1.0 cm | 94.916 |
| 2026-12 | 46.4 | 1.8 | -1.9 cm | 94.531 | -0.1 cm | 94.915 |
| 2027-01 | 51.6 | 0.1 | +1.3 cm | 94.544 | +3.8 cm | 94.953 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.141 m (-14.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.544 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.268 m (+26.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.953 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | 3.8 | +2.0 cm | 94.705 | +0.5 cm | 94.69 |
| 2026-03 | 22.8 | 5.4 | +1.5 cm | 94.72 | +0.4 cm | 94.694 |
| 2026-04 | 15.0 | 10.4 | +0.1 cm | 94.72 | -0.4 cm | 94.689 |
| 2026-05 | 34.0 | 15.1 | -1.2 cm | 94.708 | -0.5 cm | 94.684 |
| 2026-06 | 33.6 | 18.9 | -3.1 cm | 94.678 | -2.9 cm | 94.655 |
| 2026-07 | 53.9 | 20.4 | -3.6 cm | 94.641 | -3.6 cm | 94.619 |
| 2026-08 | 35.5 | 20.0 | -4.4 cm | 94.597 | -5.5 cm | 94.563 |
| 2026-09 | 22.7 | 16.0 | -4.6 cm | 94.551 | -5.1 cm | 94.513 |
| 2026-10 | 17.6 | 11.2 | -5.4 cm | 94.497 | -4.7 cm | 94.465 |
| 2026-11 | 21.8 | 5.7 | -4.5 cm | 94.452 | -4.9 cm | 94.417 |
| 2026-12 | 25.6 | 2.6 | -3.4 cm | 94.418 | -4.2 cm | 94.374 |
| 2027-01 | 28.6 | 1.9 | -0.8 cm | 94.41 | -1.8 cm | 94.357 |

- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.275 m (-27.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.41 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.328 m (-32.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.357 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | 3.8 | +1.9 cm | 94.704 | +0.5 cm | 94.69 |
| 2026-03 | 33.9 | 5.4 | +1.8 cm | 94.721 | +1.4 cm | 94.704 |
| 2026-04 | 27.7 | 10.4 | +0.8 cm | 94.73 | +1.3 cm | 94.717 |
| 2026-05 | 46.4 | 15.1 | -0.9 cm | 94.721 | +1.4 cm | 94.73 |
| 2026-06 | 53.1 | 18.9 | -2.6 cm | 94.695 | -1.6 cm | 94.714 |
| 2026-07 | 66.7 | 20.4 | -3.6 cm | 94.659 | -3.0 cm | 94.684 |
| 2026-08 | 56.2 | 20.0 | -4.2 cm | 94.617 | -3.2 cm | 94.652 |
| 2026-09 | 43.3 | 16.0 | -4.6 cm | 94.571 | -3.7 cm | 94.615 |
| 2026-10 | 33.9 | 11.2 | -5.4 cm | 94.517 | -3.0 cm | 94.585 |
| 2026-11 | 38.8 | 5.7 | -4.3 cm | 94.474 | -1.7 cm | 94.567 |
| 2026-12 | 36.7 | 2.6 | -3.3 cm | 94.441 | -1.4 cm | 94.553 |
| 2027-01 | 39.8 | 1.9 | +0.0 cm | 94.441 | +1.5 cm | 94.568 |

- **Szansa realizacji:** 14.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.244 m (-24.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.441 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.117 m (-11.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.568 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | 3.8 | +1.7 cm | 94.702 | +1.4 cm | 94.699 |
| 2026-03 | 49.5 | 5.4 | +1.8 cm | 94.72 | +3.4 cm | 94.733 |
| 2026-04 | 36.1 | 10.4 | +1.6 cm | 94.737 | +4.3 cm | 94.776 |
| 2026-05 | 64.7 | 15.1 | +0.3 cm | 94.74 | +7.3 cm | 94.85 |
| 2026-06 | 70.6 | 18.9 | -2.5 cm | 94.715 | +4.9 cm | 94.899 |
| 2026-07 | 102.3 | 20.4 | -3.6 cm | 94.679 | +0.9 cm | 94.908 |
| 2026-08 | 77.4 | 20.0 | -3.8 cm | 94.641 | -2.6 cm | 94.881 |
| 2026-09 | 62.5 | 16.0 | -3.9 cm | 94.603 | -3.1 cm | 94.85 |
| 2026-10 | 49.0 | 11.2 | -4.0 cm | 94.562 | -2.4 cm | 94.827 |
| 2026-11 | 46.6 | 5.7 | -3.2 cm | 94.53 | -1.4 cm | 94.813 |
| 2026-12 | 46.4 | 2.6 | -2.2 cm | 94.508 | -0.6 cm | 94.807 |
| 2027-01 | 51.6 | 1.9 | +0.5 cm | 94.513 | +3.2 cm | 94.839 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.172 m (-17.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.513 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.154 m (+15.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.839 m n.p.m.




*Wygenerowano: 2026-02-15 15:45*