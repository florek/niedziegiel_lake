# Raport: Jezioro Powidzkie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Powidzkie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/powidzkie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/powidzkie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 10.2 | 97.716 | 97.798 |
| zimny, normalny | 13.7 | 97.71 | 97.831 |
| zimny, wilgotny | 7.3 | 97.686 | 97.879 |
| normalny, suchy | 10.8 | 97.714 | 97.786 |
| normalny, normalny | 16.0 | 97.709 | 97.816 |
| normalny, wilgotny | 7.6 | 97.667 | 97.842 |
| ciepły, suchy | 10.8 | 97.682 | 97.794 |
| ciepły, normalny | 15.9 | 97.679 | 97.816 |
| ciepły, wilgotny | 7.6 | 97.657 | 97.844 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (97.7681 m n.p.m.):
- **Model drenażowy:** 97.694 m n.p.m. – ubędzie 0.074 m (-7.4 cm)
- **Model naturalny (sprzed drenażu):** 97.819 m n.p.m. – przybędzie +0.051 m (+5.1 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 28.8 | 0.4 | +1.9 cm | 97.787 | +3.6 cm | 97.804 |
| 2026-03 | 31.8 | 3.8 | -1.3 cm | 97.774 | +0.8 cm | 97.812 |
| 2026-04 | 25.9 | 8.6 | -3.8 cm | 97.737 | -1.0 cm | 97.802 |
| 2026-05 | 42.5 | 13.7 | -5.4 cm | 97.682 | -2.1 cm | 97.781 |
| 2026-06 | 53.1 | 17.2 | -5.9 cm | 97.623 | -2.3 cm | 97.758 |
| 2026-07 | 67.2 | 19.0 | -5.5 cm | 97.569 | -2.4 cm | 97.734 |
| 2026-08 | 53.1 | 18.5 | -2.6 cm | 97.542 | -2.1 cm | 97.713 |
| 2026-09 | 40.2 | 14.1 | -0.9 cm | 97.533 | -1.5 cm | 97.698 |
| 2026-10 | 29.0 | 9.3 | +2.4 cm | 97.557 | +0.6 cm | 97.704 |
| 2026-11 | 35.0 | 4.3 | +4.4 cm | 97.601 | +3.0 cm | 97.735 |
| 2026-12 | 36.9 | 1.0 | +5.2 cm | 97.653 | +3.9 cm | 97.773 |
| 2027-01 | 34.5 | -0.2 | +4.1 cm | 97.694 | +4.6 cm | 97.819 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.2 °C
- **Suma opadu (prognoza):** 478.0 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.074 m (-7.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.694 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.051 m (+5.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.819 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 19.3 | -2.1 | +2.2 cm | 97.79 | +3.6 cm | 97.805 |
| 2026-03 | 22.0 | 2.0 | -0.7 cm | 97.782 | +1.5 cm | 97.82 |
| 2026-04 | 15.9 | 7.7 | -3.0 cm | 97.753 | -0.4 cm | 97.816 |
| 2026-05 | 30.2 | 12.6 | -5.1 cm | 97.701 | -2.1 cm | 97.795 |
| 2026-06 | 36.6 | 16.0 | -5.9 cm | 97.642 | -2.4 cm | 97.771 |
| 2026-07 | 47.1 | 17.4 | -5.6 cm | 97.585 | -2.8 cm | 97.743 |
| 2026-08 | 37.2 | 17.4 | -2.6 cm | 97.559 | -2.6 cm | 97.718 |
| 2026-09 | 22.9 | 12.9 | -1.0 cm | 97.548 | -1.5 cm | 97.703 |
| 2026-10 | 18.0 | 8.1 | +2.6 cm | 97.574 | -0.5 cm | 97.697 |
| 2026-11 | 23.5 | 2.9 | +4.6 cm | 97.62 | +2.6 cm | 97.724 |
| 2026-12 | 26.2 | -0.4 | +5.3 cm | 97.673 | +3.5 cm | 97.759 |
| 2027-01 | 23.3 | -2.2 | +4.2 cm | 97.716 | +3.9 cm | 97.798 |

- **Szansa realizacji:** 10.2 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.052 m (-5.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.716 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.030 m (+3.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.798 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 29.5 | -2.1 | +2.2 cm | 97.79 | +3.7 cm | 97.805 |
| 2026-03 | 30.8 | 2.0 | -0.7 cm | 97.782 | +1.3 cm | 97.818 |
| 2026-04 | 28.2 | 7.7 | -3.0 cm | 97.752 | -0.6 cm | 97.812 |
| 2026-05 | 42.4 | 12.6 | -5.2 cm | 97.699 | -1.8 cm | 97.794 |
| 2026-06 | 55.5 | 16.0 | -6.0 cm | 97.64 | -1.8 cm | 97.776 |
| 2026-07 | 65.5 | 17.4 | -5.6 cm | 97.583 | -2.1 cm | 97.754 |
| 2026-08 | 52.7 | 17.4 | -2.6 cm | 97.557 | -2.3 cm | 97.731 |
| 2026-09 | 40.6 | 12.9 | -0.9 cm | 97.547 | -1.9 cm | 97.712 |
| 2026-10 | 29.0 | 8.1 | +2.5 cm | 97.572 | -0.3 cm | 97.708 |
| 2026-11 | 37.2 | 2.9 | +4.5 cm | 97.617 | +3.2 cm | 97.741 |
| 2026-12 | 39.2 | -0.4 | +5.2 cm | 97.669 | +4.1 cm | 97.782 |
| 2027-01 | 35.5 | -2.2 | +4.1 cm | 97.71 | +4.9 cm | 97.831 |

- **Szansa realizacji:** 13.7 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.058 m (-5.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.71 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.063 m (+6.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.831 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 41.0 | -2.1 | +1.7 cm | 97.785 | +3.8 cm | 97.806 |
| 2026-03 | 47.6 | 2.0 | -1.4 cm | 97.771 | +1.1 cm | 97.817 |
| 2026-04 | 35.4 | 7.7 | -3.2 cm | 97.739 | -0.5 cm | 97.811 |
| 2026-05 | 60.2 | 12.6 | -5.2 cm | 97.687 | -1.7 cm | 97.794 |
| 2026-06 | 71.7 | 16.0 | -6.0 cm | 97.627 | -2.5 cm | 97.769 |
| 2026-07 | 99.5 | 17.4 | -5.6 cm | 97.571 | -2.4 cm | 97.745 |
| 2026-08 | 76.7 | 17.4 | -2.6 cm | 97.544 | -1.7 cm | 97.728 |
| 2026-09 | 64.1 | 12.9 | -1.0 cm | 97.534 | -1.2 cm | 97.716 |
| 2026-10 | 44.6 | 8.1 | +1.9 cm | 97.553 | +0.8 cm | 97.724 |
| 2026-11 | 47.0 | 2.9 | +4.2 cm | 97.594 | +4.0 cm | 97.764 |
| 2026-12 | 47.8 | -0.4 | +5.2 cm | 97.646 | +5.0 cm | 97.814 |
| 2027-01 | 48.5 | -2.2 | +4.0 cm | 97.686 | +6.5 cm | 97.879 |

- **Szansa realizacji:** 7.3 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.082 m (-8.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.686 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.111 m (+11.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.879 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 19.3 | -0.1 | +2.2 cm | 97.79 | +3.6 cm | 97.804 |
| 2026-03 | 22.0 | 4.2 | -1.1 cm | 97.779 | +0.9 cm | 97.813 |
| 2026-04 | 15.9 | 8.7 | -3.0 cm | 97.75 | -0.9 cm | 97.804 |
| 2026-05 | 30.2 | 13.8 | -5.0 cm | 97.7 | -1.9 cm | 97.784 |
| 2026-06 | 36.6 | 16.8 | -5.9 cm | 97.641 | -2.5 cm | 97.759 |
| 2026-07 | 47.1 | 19.5 | -5.6 cm | 97.584 | -2.8 cm | 97.731 |
| 2026-08 | 37.2 | 18.5 | -2.6 cm | 97.558 | -2.4 cm | 97.708 |
| 2026-09 | 22.9 | 13.9 | -1.0 cm | 97.547 | -1.6 cm | 97.692 |
| 2026-10 | 18.0 | 9.1 | +2.6 cm | 97.573 | -0.0 cm | 97.691 |
| 2026-11 | 23.5 | 4.5 | +4.6 cm | 97.619 | +2.3 cm | 97.715 |
| 2026-12 | 26.2 | 1.2 | +5.3 cm | 97.672 | +3.1 cm | 97.746 |
| 2027-01 | 23.3 | -0.2 | +4.2 cm | 97.714 | +4.1 cm | 97.786 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.054 m (-5.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.714 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.018 m (+1.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.786 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 29.5 | -0.1 | +2.2 cm | 97.79 | +3.7 cm | 97.805 |
| 2026-03 | 30.8 | 4.2 | -1.1 cm | 97.779 | +0.7 cm | 97.812 |
| 2026-04 | 28.2 | 8.7 | -3.0 cm | 97.749 | -1.0 cm | 97.802 |
| 2026-05 | 42.4 | 13.8 | -5.1 cm | 97.698 | -1.9 cm | 97.783 |
| 2026-06 | 55.5 | 16.8 | -6.0 cm | 97.639 | -2.1 cm | 97.762 |
| 2026-07 | 65.5 | 19.5 | -5.6 cm | 97.582 | -2.1 cm | 97.741 |
| 2026-08 | 52.7 | 18.5 | -2.6 cm | 97.556 | -2.1 cm | 97.719 |
| 2026-09 | 40.6 | 13.9 | -0.9 cm | 97.546 | -1.8 cm | 97.702 |
| 2026-10 | 29.0 | 9.1 | +2.5 cm | 97.571 | +0.2 cm | 97.703 |
| 2026-11 | 37.2 | 4.5 | +4.5 cm | 97.616 | +2.7 cm | 97.73 |
| 2026-12 | 39.2 | 1.2 | +5.2 cm | 97.668 | +3.9 cm | 97.769 |
| 2027-01 | 35.5 | -0.2 | +4.1 cm | 97.709 | +4.6 cm | 97.816 |

- **Szansa realizacji:** 16.0 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.059 m (-5.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.709 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.048 m (+4.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.816 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 41.0 | -0.1 | +1.7 cm | 97.785 | +3.7 cm | 97.805 |
| 2026-03 | 47.6 | 4.2 | -1.7 cm | 97.768 | +0.5 cm | 97.81 |
| 2026-04 | 35.4 | 8.7 | -4.8 cm | 97.72 | -1.1 cm | 97.799 |
| 2026-05 | 60.2 | 13.8 | -5.9 cm | 97.661 | -1.9 cm | 97.78 |
| 2026-06 | 71.7 | 16.8 | -5.9 cm | 97.602 | -2.8 cm | 97.752 |
| 2026-07 | 99.5 | 19.5 | -5.2 cm | 97.55 | -2.4 cm | 97.728 |
| 2026-08 | 76.7 | 18.5 | -2.6 cm | 97.523 | -1.7 cm | 97.712 |
| 2026-09 | 64.1 | 13.9 | -0.8 cm | 97.515 | -1.2 cm | 97.7 |
| 2026-10 | 44.6 | 9.1 | +1.9 cm | 97.534 | +1.2 cm | 97.712 |
| 2026-11 | 47.0 | 4.5 | +4.2 cm | 97.575 | +3.5 cm | 97.747 |
| 2026-12 | 47.8 | 1.2 | +5.2 cm | 97.627 | +4.2 cm | 97.79 |
| 2027-01 | 48.5 | -0.2 | +4.0 cm | 97.667 | +5.3 cm | 97.842 |

- **Szansa realizacji:** 7.6 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.101 m (-10.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.667 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.074 m (+7.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.842 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 19.3 | 3.1 | +1.8 cm | 97.786 | +3.4 cm | 97.802 |
| 2026-03 | 22.0 | 5.1 | -1.6 cm | 97.77 | +0.2 cm | 97.805 |
| 2026-04 | 15.9 | 9.4 | -4.8 cm | 97.722 | -1.5 cm | 97.79 |
| 2026-05 | 30.2 | 14.8 | -5.9 cm | 97.663 | -2.1 cm | 97.769 |
| 2026-06 | 36.6 | 18.8 | -5.8 cm | 97.604 | -2.5 cm | 97.744 |
| 2026-07 | 47.1 | 20.1 | -5.3 cm | 97.552 | -2.8 cm | 97.716 |
| 2026-08 | 37.2 | 19.4 | -2.5 cm | 97.526 | -2.1 cm | 97.695 |
| 2026-09 | 22.9 | 15.6 | -0.9 cm | 97.517 | -1.5 cm | 97.68 |
| 2026-10 | 18.0 | 10.6 | +2.6 cm | 97.542 | +1.2 cm | 97.692 |
| 2026-11 | 23.5 | 5.4 | +4.5 cm | 97.587 | +2.9 cm | 97.722 |
| 2026-12 | 26.2 | 2.2 | +5.2 cm | 97.639 | +3.4 cm | 97.756 |
| 2027-01 | 23.3 | 1.8 | +4.2 cm | 97.682 | +3.8 cm | 97.794 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.086 m (-8.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.682 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.026 m (+2.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.794 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 29.5 | 3.1 | +1.8 cm | 97.786 | +3.5 cm | 97.803 |
| 2026-03 | 30.8 | 5.1 | -1.6 cm | 97.77 | +0.4 cm | 97.807 |
| 2026-04 | 28.2 | 9.4 | -4.8 cm | 97.722 | -1.6 cm | 97.791 |
| 2026-05 | 42.4 | 14.8 | -5.9 cm | 97.663 | -2.8 cm | 97.763 |
| 2026-06 | 55.5 | 18.8 | -5.9 cm | 97.604 | -2.2 cm | 97.741 |
| 2026-07 | 65.5 | 20.1 | -5.3 cm | 97.551 | -2.0 cm | 97.721 |
| 2026-08 | 52.7 | 19.4 | -2.6 cm | 97.525 | -2.0 cm | 97.701 |
| 2026-09 | 40.6 | 15.6 | -0.8 cm | 97.517 | -1.6 cm | 97.686 |
| 2026-10 | 29.0 | 10.6 | +2.5 cm | 97.542 | +1.5 cm | 97.701 |
| 2026-11 | 37.2 | 5.4 | +4.4 cm | 97.586 | +3.3 cm | 97.733 |
| 2026-12 | 39.2 | 2.2 | +5.2 cm | 97.638 | +3.9 cm | 97.772 |
| 2027-01 | 35.5 | 1.8 | +4.1 cm | 97.679 | +4.4 cm | 97.816 |

- **Szansa realizacji:** 15.9 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.089 m (-8.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.679 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.048 m (+4.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.816 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 41.0 | 3.1 | +1.3 cm | 97.781 | +3.5 cm | 97.803 |
| 2026-03 | 47.6 | 5.1 | -2.1 cm | 97.76 | +0.2 cm | 97.805 |
| 2026-04 | 35.4 | 9.4 | -4.6 cm | 97.714 | -1.2 cm | 97.793 |
| 2026-05 | 60.2 | 14.8 | -5.9 cm | 97.654 | -2.1 cm | 97.772 |
| 2026-06 | 71.7 | 18.8 | -5.9 cm | 97.596 | -2.7 cm | 97.744 |
| 2026-07 | 99.5 | 20.1 | -5.3 cm | 97.542 | -2.2 cm | 97.722 |
| 2026-08 | 76.7 | 19.4 | -2.7 cm | 97.515 | -1.6 cm | 97.706 |
| 2026-09 | 64.1 | 15.6 | -0.8 cm | 97.507 | -0.8 cm | 97.699 |
| 2026-10 | 44.6 | 10.6 | +1.9 cm | 97.526 | +2.0 cm | 97.719 |
| 2026-11 | 47.0 | 5.4 | +4.1 cm | 97.566 | +3.5 cm | 97.754 |
| 2026-12 | 47.8 | 2.2 | +5.1 cm | 97.617 | +4.2 cm | 97.796 |
| 2027-01 | 48.5 | 1.8 | +4.0 cm | 97.657 | +4.9 cm | 97.844 |

- **Szansa realizacji:** 7.6 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.111 m (-11.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.657 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.076 m (+7.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.844 m n.p.m.




*Wygenerowano: 2026-02-15 15:45*