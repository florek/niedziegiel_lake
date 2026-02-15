# Raport: Jezioro Budzisławskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Budzisławskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/budzislawskie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/budzislawskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 11.3 | 95.822 | 96.066 |
| zimny, normalny | 14.2 | 95.833 | 96.091 |
| zimny, wilgotny | 7.1 | 95.875 | 96.172 |
| normalny, suchy | 11.7 | 95.662 | 96.048 |
| normalny, normalny | 15.2 | 95.698 | 96.073 |
| normalny, wilgotny | 7.2 | 95.875 | 96.157 |
| ciepły, suchy | 11.5 | 95.666 | 95.999 |
| ciepły, normalny | 14.5 | 95.725 | 96.029 |
| ciepły, wilgotny | 7.2 | 95.738 | 96.116 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (96.0461 m n.p.m.):
- **Model drenażowy:** 95.756 m n.p.m. – ubędzie 0.290 m (-29.0 cm)
- **Model naturalny (sprzed drenażu):** 96.073 m n.p.m. – przybędzie +0.027 m (+2.7 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.0 | 1.2 | +3.7 cm | 96.083 | +3.5 cm | 96.081 |
| 2026-03 | 33.4 | 4.2 | +2.0 cm | 96.103 | +3.0 cm | 96.111 |
| 2026-04 | 25.1 | 9.3 | -1.0 cm | 96.092 | +1.6 cm | 96.127 |
| 2026-05 | 46.0 | 13.9 | -4.4 cm | 96.048 | +0.0 cm | 96.127 |
| 2026-06 | 50.1 | 17.7 | -5.7 cm | 95.991 | -2.9 cm | 96.098 |
| 2026-07 | 69.9 | 19.7 | -6.5 cm | 95.927 | -3.0 cm | 96.068 |
| 2026-08 | 53.6 | 19.2 | -6.4 cm | 95.863 | -3.0 cm | 96.038 |
| 2026-09 | 40.3 | 14.8 | -4.2 cm | 95.821 | -2.0 cm | 96.018 |
| 2026-10 | 31.5 | 9.8 | -4.0 cm | 95.781 | -0.8 cm | 96.01 |
| 2026-11 | 34.6 | 4.7 | -2.8 cm | 95.753 | +0.5 cm | 96.015 |
| 2026-12 | 34.9 | 1.4 | -0.6 cm | 95.747 | +1.9 cm | 96.034 |
| 2027-01 | 38.4 | 0.0 | +0.9 cm | 95.756 | +3.9 cm | 96.073 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 491.7 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.290 m (-29.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.756 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.027 m (+2.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.073 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | -1.0 | +3.7 cm | 96.083 | +3.2 cm | 96.078 |
| 2026-03 | 22.8 | 3.0 | +2.3 cm | 96.106 | +2.7 cm | 96.106 |
| 2026-04 | 15.0 | 8.4 | -1.0 cm | 96.096 | +1.9 cm | 96.125 |
| 2026-05 | 34.0 | 12.8 | -4.2 cm | 96.054 | +0.9 cm | 96.134 |
| 2026-06 | 33.6 | 16.5 | -5.4 cm | 95.999 | -2.4 cm | 96.111 |
| 2026-07 | 53.9 | 18.8 | -5.7 cm | 95.942 | -3.4 cm | 96.076 |
| 2026-08 | 35.5 | 18.3 | -6.4 cm | 95.878 | -3.4 cm | 96.042 |
| 2026-09 | 22.7 | 13.7 | -3.6 cm | 95.842 | -2.1 cm | 96.021 |
| 2026-10 | 17.6 | 8.3 | -3.0 cm | 95.811 | -0.7 cm | 96.014 |
| 2026-11 | 21.8 | 3.6 | -1.0 cm | 95.802 | +0.1 cm | 96.015 |
| 2026-12 | 25.6 | -0.2 | +0.3 cm | 95.804 | +1.8 cm | 96.033 |
| 2027-01 | 28.6 | -1.9 | +1.8 cm | 95.822 | +3.3 cm | 96.066 |

- **Szansa realizacji:** 11.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.224 m (-22.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.822 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.020 m (+2.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.066 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | -1.0 | +3.6 cm | 96.082 | +3.3 cm | 96.079 |
| 2026-03 | 33.9 | 3.0 | +2.1 cm | 96.103 | +2.7 cm | 96.106 |
| 2026-04 | 27.7 | 8.4 | -1.2 cm | 96.091 | +1.9 cm | 96.125 |
| 2026-05 | 46.4 | 12.8 | -3.9 cm | 96.051 | +1.0 cm | 96.135 |
| 2026-06 | 53.1 | 16.5 | -5.1 cm | 96.0 | -2.2 cm | 96.113 |
| 2026-07 | 66.7 | 18.8 | -5.7 cm | 95.944 | -2.7 cm | 96.087 |
| 2026-08 | 56.2 | 18.3 | -6.1 cm | 95.882 | -3.3 cm | 96.054 |
| 2026-09 | 43.3 | 13.7 | -3.5 cm | 95.847 | -2.0 cm | 96.034 |
| 2026-10 | 33.9 | 8.3 | -3.2 cm | 95.815 | -0.7 cm | 96.027 |
| 2026-11 | 38.8 | 3.6 | -0.7 cm | 95.808 | +0.3 cm | 96.03 |
| 2026-12 | 36.7 | -0.2 | +0.4 cm | 95.812 | +1.9 cm | 96.049 |
| 2027-01 | 39.8 | -1.9 | +2.1 cm | 95.833 | +4.2 cm | 96.091 |

- **Szansa realizacji:** 14.2 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.213 m (-21.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.833 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.045 m (+4.5 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.091 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | -1.0 | +3.9 cm | 96.085 | +4.4 cm | 96.09 |
| 2026-03 | 49.5 | 3.0 | +2.4 cm | 96.109 | +4.2 cm | 96.132 |
| 2026-04 | 36.1 | 8.4 | -1.2 cm | 96.097 | +2.3 cm | 96.155 |
| 2026-05 | 64.7 | 12.8 | -3.7 cm | 96.06 | +1.1 cm | 96.166 |
| 2026-06 | 70.6 | 16.5 | -5.1 cm | 96.009 | -1.8 cm | 96.148 |
| 2026-07 | 102.3 | 18.8 | -5.5 cm | 95.954 | -2.5 cm | 96.123 |
| 2026-08 | 77.4 | 18.3 | -5.4 cm | 95.9 | -2.4 cm | 96.1 |
| 2026-09 | 62.5 | 13.7 | -3.8 cm | 95.862 | -1.0 cm | 96.089 |
| 2026-10 | 49.0 | 8.3 | -3.1 cm | 95.831 | +0.2 cm | 96.091 |
| 2026-11 | 46.6 | 3.6 | -0.4 cm | 95.828 | +1.3 cm | 96.104 |
| 2026-12 | 46.4 | -0.2 | +2.3 cm | 95.851 | +2.3 cm | 96.127 |
| 2027-01 | 51.6 | -1.9 | +2.4 cm | 95.875 | +4.5 cm | 96.172 |

- **Szansa realizacji:** 7.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.171 m (-17.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.875 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.126 m (+12.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.172 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | 0.8 | +3.6 cm | 96.082 | +3.2 cm | 96.078 |
| 2026-03 | 22.8 | 4.3 | +1.9 cm | 96.101 | +2.7 cm | 96.106 |
| 2026-04 | 15.0 | 9.1 | -0.9 cm | 96.092 | +1.9 cm | 96.125 |
| 2026-05 | 34.0 | 13.7 | -5.1 cm | 96.042 | +0.3 cm | 96.127 |
| 2026-06 | 33.6 | 17.8 | -6.8 cm | 95.974 | -3.3 cm | 96.094 |
| 2026-07 | 53.9 | 19.8 | -7.5 cm | 95.899 | -3.4 cm | 96.06 |
| 2026-08 | 35.5 | 19.3 | -6.6 cm | 95.833 | -3.3 cm | 96.027 |
| 2026-09 | 22.7 | 14.7 | -5.0 cm | 95.783 | -2.1 cm | 96.006 |
| 2026-10 | 17.6 | 9.8 | -5.1 cm | 95.732 | -1.0 cm | 95.996 |
| 2026-11 | 21.8 | 4.8 | -4.7 cm | 95.685 | +0.1 cm | 95.997 |
| 2026-12 | 25.6 | 1.8 | -2.0 cm | 95.665 | +1.8 cm | 96.015 |
| 2027-01 | 28.6 | 0.1 | -0.3 cm | 95.662 | +3.3 cm | 96.048 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.384 m (-38.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.662 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.002 m (+0.2 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.048 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | 0.8 | +3.5 cm | 96.081 | +3.3 cm | 96.079 |
| 2026-03 | 33.9 | 4.3 | +1.7 cm | 96.098 | +2.7 cm | 96.106 |
| 2026-04 | 27.7 | 9.1 | -1.1 cm | 96.087 | +1.9 cm | 96.125 |
| 2026-05 | 46.4 | 13.7 | -4.6 cm | 96.041 | +0.4 cm | 96.129 |
| 2026-06 | 53.1 | 17.8 | -6.5 cm | 95.977 | -3.2 cm | 96.097 |
| 2026-07 | 66.7 | 19.8 | -7.2 cm | 95.904 | -2.7 cm | 96.07 |
| 2026-08 | 56.2 | 19.3 | -6.5 cm | 95.839 | -3.1 cm | 96.039 |
| 2026-09 | 43.3 | 14.7 | -3.5 cm | 95.804 | -2.0 cm | 96.019 |
| 2026-10 | 33.9 | 9.8 | -5.1 cm | 95.753 | -1.0 cm | 96.009 |
| 2026-11 | 38.8 | 4.8 | -3.5 cm | 95.718 | +0.3 cm | 96.012 |
| 2026-12 | 36.7 | 1.8 | -1.7 cm | 95.701 | +1.9 cm | 96.031 |
| 2027-01 | 39.8 | 0.1 | -0.3 cm | 95.698 | +4.2 cm | 96.073 |

- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.348 m (-34.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.698 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.027 m (+2.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.073 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | 0.8 | +3.8 cm | 96.084 | +4.4 cm | 96.09 |
| 2026-03 | 49.5 | 4.3 | +2.1 cm | 96.105 | +4.2 cm | 96.132 |
| 2026-04 | 36.1 | 9.1 | -1.1 cm | 96.094 | +2.3 cm | 96.155 |
| 2026-05 | 64.7 | 13.7 | -4.4 cm | 96.05 | +0.5 cm | 96.16 |
| 2026-06 | 70.6 | 17.8 | -5.1 cm | 96.0 | -2.4 cm | 96.136 |
| 2026-07 | 102.3 | 19.8 | -6.3 cm | 95.937 | -2.5 cm | 96.111 |
| 2026-08 | 77.4 | 19.3 | -6.2 cm | 95.875 | -2.3 cm | 96.088 |
| 2026-09 | 62.5 | 14.7 | -3.5 cm | 95.84 | -1.1 cm | 96.077 |
| 2026-10 | 49.0 | 9.8 | -1.4 cm | 95.826 | -0.1 cm | 96.076 |
| 2026-11 | 46.6 | 4.8 | -0.0 cm | 95.826 | +1.3 cm | 96.089 |
| 2026-12 | 46.4 | 1.8 | +2.3 cm | 95.848 | +2.2 cm | 96.111 |
| 2027-01 | 51.6 | 0.1 | +2.6 cm | 95.875 | +4.5 cm | 96.157 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.171 m (-17.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.875 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.111 m (+11.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.157 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | 3.8 | +3.8 cm | 96.084 | +3.1 cm | 96.077 |
| 2026-03 | 22.8 | 5.4 | +1.8 cm | 96.102 | +2.7 cm | 96.105 |
| 2026-04 | 15.0 | 10.4 | -0.8 cm | 96.094 | +0.8 cm | 96.112 |
| 2026-05 | 34.0 | 15.1 | -4.7 cm | 96.047 | -1.5 cm | 96.098 |
| 2026-06 | 33.6 | 18.9 | -6.8 cm | 95.979 | -3.7 cm | 96.061 |
| 2026-07 | 53.9 | 20.4 | -7.3 cm | 95.906 | -3.9 cm | 96.022 |
| 2026-08 | 35.5 | 20.0 | -6.8 cm | 95.837 | -3.5 cm | 95.988 |
| 2026-09 | 22.7 | 16.0 | -5.5 cm | 95.783 | -2.5 cm | 95.963 |
| 2026-10 | 17.6 | 11.2 | -5.1 cm | 95.732 | -1.4 cm | 95.948 |
| 2026-11 | 21.8 | 5.7 | -4.7 cm | 95.685 | +0.2 cm | 95.951 |
| 2026-12 | 25.6 | 2.6 | -1.8 cm | 95.667 | +1.7 cm | 95.968 |
| 2027-01 | 28.6 | 1.9 | -0.1 cm | 95.666 | +3.1 cm | 95.999 |

- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.380 m (-38.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.666 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.047 m (-4.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.999 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | 3.8 | +3.7 cm | 96.083 | +3.1 cm | 96.077 |
| 2026-03 | 33.9 | 5.4 | +1.6 cm | 96.099 | +2.7 cm | 96.105 |
| 2026-04 | 27.7 | 10.4 | -1.0 cm | 96.089 | +0.8 cm | 96.112 |
| 2026-05 | 46.4 | 15.1 | -4.4 cm | 96.045 | -1.3 cm | 96.099 |
| 2026-06 | 53.1 | 18.9 | -5.1 cm | 95.994 | -3.5 cm | 96.064 |
| 2026-07 | 66.7 | 20.4 | -6.1 cm | 95.933 | -3.2 cm | 96.032 |
| 2026-08 | 56.2 | 20.0 | -6.6 cm | 95.867 | -2.8 cm | 96.003 |
| 2026-09 | 43.3 | 16.0 | -4.6 cm | 95.821 | -2.4 cm | 95.979 |
| 2026-10 | 33.9 | 11.2 | -4.5 cm | 95.777 | -1.2 cm | 95.968 |
| 2026-11 | 38.8 | 5.7 | -4.3 cm | 95.733 | +0.3 cm | 95.971 |
| 2026-12 | 36.7 | 2.6 | -1.4 cm | 95.719 | +1.8 cm | 95.988 |
| 2027-01 | 39.8 | 1.9 | +0.6 cm | 95.725 | +4.1 cm | 96.029 |

- **Szansa realizacji:** 14.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.321 m (-32.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.725 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.017 m (-1.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.029 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | 3.8 | +4.0 cm | 96.086 | +4.2 cm | 96.088 |
| 2026-03 | 49.5 | 5.4 | +2.0 cm | 96.107 | +4.2 cm | 96.13 |
| 2026-04 | 36.1 | 10.4 | -1.0 cm | 96.097 | +0.8 cm | 96.138 |
| 2026-05 | 64.7 | 15.1 | -4.2 cm | 96.055 | -1.0 cm | 96.128 |
| 2026-06 | 70.6 | 18.9 | -5.0 cm | 96.005 | -2.8 cm | 96.1 |
| 2026-07 | 102.3 | 20.4 | -6.1 cm | 95.944 | -2.5 cm | 96.075 |
| 2026-08 | 77.4 | 20.0 | -6.7 cm | 95.877 | -1.9 cm | 96.056 |
| 2026-09 | 62.5 | 16.0 | -4.5 cm | 95.831 | -1.4 cm | 96.042 |
| 2026-10 | 49.0 | 11.2 | -4.3 cm | 95.788 | -0.3 cm | 96.039 |
| 2026-11 | 46.6 | 5.7 | -4.2 cm | 95.746 | +1.3 cm | 96.052 |
| 2026-12 | 46.4 | 2.6 | -1.3 cm | 95.733 | +2.0 cm | 96.073 |
| 2027-01 | 51.6 | 1.9 | +0.5 cm | 95.738 | +4.3 cm | 96.116 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.308 m (-30.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.738 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.070 m (+7.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.116 m n.p.m.




*Wygenerowano: 2026-02-15 15:44*