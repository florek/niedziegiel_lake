# Raport: Jezioro Skulska Wieś

Raport ewaluacji na następne 12 miesięcy dla Jezioro Skulska Wieś.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/skulskawies/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/skulskawies/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 11.3 | 85.718 | 86.056 |
| zimny, normalny | 14.2 | 85.978 | 86.094 |
| zimny, wilgotny | 7.1 | 86.189 | 86.08 |
| normalny, suchy | 11.7 | 85.478 | 85.911 |
| normalny, normalny | 15.2 | 85.811 | 86.089 |
| normalny, wilgotny | 7.2 | 86.164 | 86.088 |
| ciepły, suchy | 11.5 | 85.4 | 85.985 |
| ciepły, normalny | 14.5 | 85.749 | 86.028 |
| ciepły, wilgotny | 7.2 | 86.133 | 86.094 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (85.758 m n.p.m.):
- **Model drenażowy:** 85.805 m n.p.m. – przybędzie +0.047 m (+4.7 cm)
- **Model naturalny (sprzed drenażu):** 86.044 m n.p.m. – przybędzie +0.286 m (+28.6 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.0 | 1.2 | +6.2 cm | 85.82 | +6.4 cm | 85.822 |
| 2026-03 | 33.4 | 4.2 | +7.0 cm | 85.89 | +7.0 cm | 85.893 |
| 2026-04 | 25.1 | 9.3 | +5.5 cm | 85.945 | +7.1 cm | 85.964 |
| 2026-05 | 46.0 | 13.9 | -1.1 cm | 85.934 | +2.7 cm | 85.991 |
| 2026-06 | 50.1 | 17.7 | -5.9 cm | 85.875 | -2.6 cm | 85.965 |
| 2026-07 | 69.9 | 19.7 | -7.6 cm | 85.799 | -2.1 cm | 85.944 |
| 2026-08 | 53.6 | 19.2 | -7.4 cm | 85.726 | -1.1 cm | 85.933 |
| 2026-09 | 40.3 | 14.8 | -4.8 cm | 85.677 | -1.9 cm | 85.914 |
| 2026-10 | 31.5 | 9.8 | -2.4 cm | 85.653 | -0.2 cm | 85.912 |
| 2026-11 | 34.6 | 4.7 | +1.6 cm | 85.669 | +2.3 cm | 85.935 |
| 2026-12 | 34.9 | 1.4 | +5.8 cm | 85.726 | +4.9 cm | 85.984 |
| 2027-01 | 38.4 | 0.0 | +7.8 cm | 85.805 | +6.0 cm | 86.044 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 491.7 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.047 m (+4.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.805 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.286 m (+28.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.044 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | -1.0 | +6.3 cm | 85.822 | +5.9 cm | 85.817 |
| 2026-03 | 22.8 | 3.0 | +7.0 cm | 85.892 | +6.6 cm | 85.884 |
| 2026-04 | 15.0 | 8.4 | +4.9 cm | 85.941 | +7.4 cm | 85.957 |
| 2026-05 | 34.0 | 12.8 | -0.9 cm | 85.932 | +5.4 cm | 86.011 |
| 2026-06 | 33.6 | 16.5 | -6.5 cm | 85.867 | -1.2 cm | 85.999 |
| 2026-07 | 53.9 | 18.8 | -8.0 cm | 85.788 | -3.1 cm | 85.968 |
| 2026-08 | 35.5 | 18.3 | -7.5 cm | 85.713 | -1.8 cm | 85.95 |
| 2026-09 | 22.7 | 13.7 | -4.8 cm | 85.665 | +1.3 cm | 85.963 |
| 2026-10 | 17.6 | 8.3 | -5.0 cm | 85.615 | +1.2 cm | 85.976 |
| 2026-11 | 21.8 | 3.6 | -1.3 cm | 85.602 | +2.5 cm | 86.0 |
| 2026-12 | 25.6 | -0.2 | +4.2 cm | 85.644 | +2.9 cm | 86.029 |
| 2027-01 | 28.6 | -1.9 | +7.3 cm | 85.718 | +2.8 cm | 86.056 |

- **Szansa realizacji:** 11.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.040 m (-4.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.718 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.298 m (+29.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.056 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | -1.0 | +6.5 cm | 85.823 | +6.1 cm | 85.819 |
| 2026-03 | 33.9 | 3.0 | +7.5 cm | 85.898 | +6.8 cm | 85.887 |
| 2026-04 | 27.7 | 8.4 | +7.0 cm | 85.968 | +8.1 cm | 85.968 |
| 2026-05 | 46.4 | 12.8 | -0.3 cm | 85.965 | +5.7 cm | 86.025 |
| 2026-06 | 53.1 | 16.5 | -5.1 cm | 85.913 | -1.8 cm | 86.008 |
| 2026-07 | 66.7 | 18.8 | -7.1 cm | 85.842 | -3.8 cm | 85.97 |
| 2026-08 | 56.2 | 18.3 | -6.7 cm | 85.776 | -3.1 cm | 85.939 |
| 2026-09 | 43.3 | 13.7 | -3.2 cm | 85.744 | -0.2 cm | 85.938 |
| 2026-10 | 33.9 | 8.3 | -1.3 cm | 85.731 | +1.2 cm | 85.95 |
| 2026-11 | 38.8 | 3.6 | +4.8 cm | 85.779 | +3.2 cm | 85.982 |
| 2026-12 | 36.7 | -0.2 | +8.9 cm | 85.868 | +6.4 cm | 86.047 |
| 2027-01 | 39.8 | -1.9 | +11.1 cm | 85.978 | +4.8 cm | 86.094 |

- **Szansa realizacji:** 14.2 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.220 m (+22.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.978 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.336 m (+33.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.094 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | -1.0 | +6.6 cm | 85.824 | +6.9 cm | 85.827 |
| 2026-03 | 49.5 | 3.0 | +8.8 cm | 85.912 | +8.4 cm | 85.912 |
| 2026-04 | 36.1 | 8.4 | +8.4 cm | 85.996 | +9.6 cm | 86.007 |
| 2026-05 | 64.7 | 12.8 | +2.1 cm | 86.017 | +5.3 cm | 86.06 |
| 2026-06 | 70.6 | 16.5 | -4.0 cm | 85.976 | -3.5 cm | 86.026 |
| 2026-07 | 102.3 | 18.8 | -5.9 cm | 85.917 | -4.1 cm | 85.985 |
| 2026-08 | 77.4 | 18.3 | -4.6 cm | 85.872 | -2.6 cm | 85.959 |
| 2026-09 | 62.5 | 13.7 | +0.5 cm | 85.877 | +1.0 cm | 85.969 |
| 2026-10 | 49.0 | 8.3 | +6.4 cm | 85.941 | +1.9 cm | 85.988 |
| 2026-11 | 46.6 | 3.6 | +9.1 cm | 86.032 | +3.2 cm | 86.02 |
| 2026-12 | 46.4 | -0.2 | +8.9 cm | 86.121 | +3.1 cm | 86.051 |
| 2027-01 | 51.6 | -1.9 | +6.8 cm | 86.189 | +2.9 cm | 86.08 |

- **Szansa realizacji:** 7.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.431 m (+43.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 86.189 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.322 m (+32.2 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.08 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | 0.8 | +6.3 cm | 85.822 | +7.3 cm | 85.831 |
| 2026-03 | 22.8 | 4.3 | +6.0 cm | 85.881 | +8.0 cm | 85.911 |
| 2026-04 | 15.0 | 9.1 | +4.5 cm | 85.926 | +8.8 cm | 85.999 |
| 2026-05 | 34.0 | 13.7 | -1.2 cm | 85.914 | +3.3 cm | 86.032 |
| 2026-06 | 33.6 | 17.8 | -6.4 cm | 85.85 | -4.6 cm | 85.985 |
| 2026-07 | 53.9 | 19.8 | -8.1 cm | 85.768 | -5.4 cm | 85.931 |
| 2026-08 | 35.5 | 19.3 | -8.9 cm | 85.679 | -3.8 cm | 85.894 |
| 2026-09 | 22.7 | 14.7 | -9.0 cm | 85.589 | -5.4 cm | 85.84 |
| 2026-10 | 17.6 | 9.8 | -8.5 cm | 85.503 | -3.9 cm | 85.801 |
| 2026-11 | 21.8 | 4.8 | -4.6 cm | 85.458 | -0.4 cm | 85.797 |
| 2026-12 | 25.6 | 1.8 | -0.9 cm | 85.448 | +3.8 cm | 85.835 |
| 2027-01 | 28.6 | 0.1 | +3.0 cm | 85.478 | +7.6 cm | 85.911 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.280 m (-28.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.478 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.153 m (+15.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 85.911 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | 0.8 | +6.5 cm | 85.823 | +7.5 cm | 85.833 |
| 2026-03 | 33.9 | 4.3 | +6.4 cm | 85.886 | +9.3 cm | 85.926 |
| 2026-04 | 27.7 | 9.1 | +5.1 cm | 85.937 | +9.2 cm | 86.019 |
| 2026-05 | 46.4 | 13.7 | -1.2 cm | 85.925 | +2.8 cm | 86.047 |
| 2026-06 | 53.1 | 17.8 | -5.0 cm | 85.875 | -4.8 cm | 85.999 |
| 2026-07 | 66.7 | 19.8 | -7.8 cm | 85.798 | -4.3 cm | 85.957 |
| 2026-08 | 56.2 | 19.3 | -7.6 cm | 85.722 | -2.8 cm | 85.929 |
| 2026-09 | 43.3 | 14.7 | -4.1 cm | 85.682 | -2.7 cm | 85.901 |
| 2026-10 | 33.9 | 9.8 | -2.5 cm | 85.656 | -0.1 cm | 85.901 |
| 2026-11 | 38.8 | 4.8 | +0.9 cm | 85.666 | +4.0 cm | 85.941 |
| 2026-12 | 36.7 | 1.8 | +6.3 cm | 85.729 | +6.3 cm | 86.003 |
| 2027-01 | 39.8 | 0.1 | +8.3 cm | 85.811 | +8.6 cm | 86.089 |

- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.053 m (+5.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.811 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.331 m (+33.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.089 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | 0.8 | +6.6 cm | 85.824 | +8.1 cm | 85.839 |
| 2026-03 | 49.5 | 4.3 | +7.2 cm | 85.897 | +9.7 cm | 85.937 |
| 2026-04 | 36.1 | 9.1 | +6.8 cm | 85.964 | +9.1 cm | 86.027 |
| 2026-05 | 64.7 | 13.7 | +0.2 cm | 85.967 | +2.5 cm | 86.053 |
| 2026-06 | 70.6 | 17.8 | -4.0 cm | 85.927 | -4.5 cm | 86.008 |
| 2026-07 | 102.3 | 19.8 | -6.5 cm | 85.862 | -2.1 cm | 85.987 |
| 2026-08 | 77.4 | 19.3 | -5.4 cm | 85.807 | +0.7 cm | 85.994 |
| 2026-09 | 62.5 | 14.7 | -0.0 cm | 85.807 | -2.8 cm | 85.966 |
| 2026-10 | 49.0 | 9.8 | +6.0 cm | 85.867 | -0.5 cm | 85.961 |
| 2026-11 | 46.6 | 4.8 | +8.8 cm | 85.955 | +1.6 cm | 85.978 |
| 2026-12 | 46.4 | 1.8 | +10.9 cm | 86.064 | +5.3 cm | 86.031 |
| 2027-01 | 51.6 | 0.1 | +10.0 cm | 86.164 | +5.8 cm | 86.088 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.406 m (+40.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 86.164 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.330 m (+33.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.088 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | 3.8 | +5.5 cm | 85.813 | +5.3 cm | 85.811 |
| 2026-03 | 22.8 | 5.4 | +6.5 cm | 85.878 | +4.5 cm | 85.856 |
| 2026-04 | 15.0 | 10.4 | +3.9 cm | 85.918 | +3.4 cm | 85.89 |
| 2026-05 | 34.0 | 15.1 | -2.5 cm | 85.893 | -0.9 cm | 85.881 |
| 2026-06 | 33.6 | 18.9 | -8.3 cm | 85.809 | -1.0 cm | 85.871 |
| 2026-07 | 53.9 | 20.4 | -8.9 cm | 85.72 | +2.1 cm | 85.893 |
| 2026-08 | 35.5 | 20.0 | -11.0 cm | 85.61 | +1.0 cm | 85.902 |
| 2026-09 | 22.7 | 16.0 | -10.7 cm | 85.502 | -2.8 cm | 85.875 |
| 2026-10 | 17.6 | 11.2 | -9.2 cm | 85.41 | -1.6 cm | 85.859 |
| 2026-11 | 21.8 | 5.7 | -4.8 cm | 85.362 | +1.6 cm | 85.875 |
| 2026-12 | 25.6 | 2.6 | +0.0 cm | 85.362 | +4.5 cm | 85.919 |
| 2027-01 | 28.6 | 1.9 | +3.9 cm | 85.4 | +6.6 cm | 85.985 |

- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.358 m (-35.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.4 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.227 m (+22.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 85.985 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | 3.8 | +5.7 cm | 85.815 | +5.2 cm | 85.81 |
| 2026-03 | 33.9 | 5.4 | +7.1 cm | 85.885 | +4.5 cm | 85.855 |
| 2026-04 | 27.7 | 10.4 | +4.4 cm | 85.929 | +2.9 cm | 85.885 |
| 2026-05 | 46.4 | 15.1 | -2.5 cm | 85.904 | -0.3 cm | 85.882 |
| 2026-06 | 53.1 | 18.9 | -7.3 cm | 85.831 | -0.7 cm | 85.875 |
| 2026-07 | 66.7 | 20.4 | -8.4 cm | 85.747 | +1.3 cm | 85.888 |
| 2026-08 | 56.2 | 20.0 | -7.0 cm | 85.677 | +2.0 cm | 85.907 |
| 2026-09 | 43.3 | 16.0 | -5.7 cm | 85.619 | -2.1 cm | 85.887 |
| 2026-10 | 33.9 | 11.2 | -2.8 cm | 85.592 | +0.4 cm | 85.891 |
| 2026-11 | 38.8 | 5.7 | +0.5 cm | 85.597 | +2.3 cm | 85.914 |
| 2026-12 | 36.7 | 2.6 | +6.3 cm | 85.661 | +4.9 cm | 85.962 |
| 2027-01 | 39.8 | 1.9 | +8.9 cm | 85.749 | +6.6 cm | 86.028 |

- **Szansa realizacji:** 14.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.009 m (-0.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.749 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.270 m (+27.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.028 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | 3.8 | +5.6 cm | 85.814 | +5.7 cm | 85.815 |
| 2026-03 | 49.5 | 5.4 | +7.6 cm | 85.89 | +7.1 cm | 85.887 |
| 2026-04 | 36.1 | 10.4 | +6.8 cm | 85.958 | +8.3 cm | 85.97 |
| 2026-05 | 64.7 | 15.1 | -1.5 cm | 85.943 | +0.1 cm | 85.971 |
| 2026-06 | 70.6 | 18.9 | -4.1 cm | 85.902 | -1.9 cm | 85.952 |
| 2026-07 | 102.3 | 20.4 | -6.1 cm | 85.841 | +1.3 cm | 85.965 |
| 2026-08 | 77.4 | 20.0 | -5.5 cm | 85.787 | +1.7 cm | 85.982 |
| 2026-09 | 62.5 | 16.0 | -1.9 cm | 85.767 | -3.5 cm | 85.947 |
| 2026-10 | 49.0 | 11.2 | +4.0 cm | 85.808 | +0.1 cm | 85.948 |
| 2026-11 | 46.6 | 5.7 | +8.6 cm | 85.894 | +2.1 cm | 85.969 |
| 2026-12 | 46.4 | 2.6 | +11.3 cm | 86.007 | +5.6 cm | 86.025 |
| 2027-01 | 51.6 | 1.9 | +12.7 cm | 86.133 | +7.0 cm | 86.094 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.375 m (+37.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 86.133 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.336 m (+33.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.094 m n.p.m.




*Wygenerowano: 2026-02-15 15:45*