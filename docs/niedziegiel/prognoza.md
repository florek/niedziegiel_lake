# Raport: Jezioro Niedzięgiel

Raport ewaluacji na następne 12 miesięcy dla Jezioro Niedzięgiel.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/niedziegiel/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/niedziegiel/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 10.2 | 101.91 | 101.974 |
| zimny, normalny | 13.8 | 101.911 | 102.093 |
| zimny, wilgotny | 7.3 | 101.912 | 102.191 |
| normalny, suchy | 10.8 | 101.94 | 101.894 |
| normalny, normalny | 16.0 | 101.914 | 102.005 |
| normalny, wilgotny | 7.6 | 101.906 | 102.241 |
| ciepły, suchy | 10.8 | 101.9 | 101.854 |
| ciepły, normalny | 15.8 | 101.922 | 101.919 |
| ciepły, wilgotny | 7.6 | 101.901 | 102.239 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (101.89 m n.p.m.):
- **Model drenażowy:** 101.914 m n.p.m. – przybędzie +0.024 m (+2.4 cm)
- **Model naturalny (sprzed drenażu):** 102.021 m n.p.m. – przybędzie +0.131 m (+13.1 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 28.8 | 0.4 | +4.8 cm | 101.938 | +3.8 cm | 101.928 |
| 2026-03 | 31.8 | 3.8 | +3.9 cm | 101.977 | +3.2 cm | 101.96 |
| 2026-04 | 25.9 | 8.6 | -2.5 cm | 101.952 | +0.8 cm | 101.968 |
| 2026-05 | 42.5 | 13.7 | -5.0 cm | 101.902 | -1.8 cm | 101.951 |
| 2026-06 | 53.1 | 17.2 | -6.1 cm | 101.841 | -2.6 cm | 101.925 |
| 2026-07 | 67.2 | 19.0 | -5.7 cm | 101.785 | -3.0 cm | 101.895 |
| 2026-08 | 53.1 | 18.5 | -2.9 cm | 101.756 | -2.7 cm | 101.868 |
| 2026-09 | 40.2 | 14.1 | +1.1 cm | 101.766 | -0.9 cm | 101.86 |
| 2026-10 | 29.0 | 9.3 | +5.2 cm | 101.819 | +1.4 cm | 101.873 |
| 2026-11 | 35.0 | 4.3 | +5.1 cm | 101.87 | +3.6 cm | 101.91 |
| 2026-12 | 36.9 | 1.0 | +3.2 cm | 101.902 | +5.1 cm | 101.96 |
| 2027-01 | 34.5 | -0.2 | +1.2 cm | 101.914 | +6.1 cm | 102.021 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 478.0 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.024 m (+2.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.914 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.131 m (+13.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 102.021 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 19.3 | -2.1 | +5.1 cm | 101.941 | +3.7 cm | 101.927 |
| 2026-03 | 22.0 | 2.0 | +4.5 cm | 101.986 | +3.4 cm | 101.961 |
| 2026-04 | 15.9 | 7.7 | -2.3 cm | 101.962 | +1.6 cm | 101.977 |
| 2026-05 | 30.2 | 12.6 | -4.7 cm | 101.916 | +0.1 cm | 101.978 |
| 2026-06 | 36.6 | 16.0 | -5.9 cm | 101.857 | -1.7 cm | 101.961 |
| 2026-07 | 47.1 | 17.4 | -5.2 cm | 101.805 | -3.0 cm | 101.931 |
| 2026-08 | 37.2 | 17.4 | -2.3 cm | 101.781 | -3.3 cm | 101.899 |
| 2026-09 | 22.9 | 12.9 | +2.8 cm | 101.81 | -1.8 cm | 101.88 |
| 2026-10 | 18.0 | 8.1 | +5.6 cm | 101.866 | -0.5 cm | 101.876 |
| 2026-11 | 23.5 | 2.9 | +4.1 cm | 101.907 | +2.1 cm | 101.897 |
| 2026-12 | 26.2 | -0.4 | +1.0 cm | 101.917 | +3.5 cm | 101.931 |
| 2027-01 | 23.3 | -2.2 | -0.8 cm | 101.91 | +4.2 cm | 101.974 |

- **Szansa realizacji:** 10.2 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.020 m (+2.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.91 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.084 m (+8.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.974 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 29.5 | -2.1 | +5.0 cm | 101.94 | +3.9 cm | 101.929 |
| 2026-03 | 30.8 | 2.0 | +4.4 cm | 101.984 | +3.5 cm | 101.965 |
| 2026-04 | 28.2 | 7.7 | -2.5 cm | 101.959 | +2.2 cm | 101.986 |
| 2026-05 | 42.4 | 12.6 | -5.8 cm | 101.901 | -0.7 cm | 101.98 |
| 2026-06 | 55.5 | 16.0 | -6.6 cm | 101.835 | -2.5 cm | 101.955 |
| 2026-07 | 65.5 | 17.4 | -6.2 cm | 101.774 | -1.4 cm | 101.941 |
| 2026-08 | 52.7 | 17.4 | -2.9 cm | 101.745 | -0.5 cm | 101.936 |
| 2026-09 | 40.6 | 12.9 | +0.9 cm | 101.754 | +0.1 cm | 101.936 |
| 2026-10 | 29.0 | 8.1 | +5.1 cm | 101.805 | +1.5 cm | 101.951 |
| 2026-11 | 37.2 | 2.9 | +5.0 cm | 101.855 | +3.3 cm | 101.984 |
| 2026-12 | 39.2 | -0.4 | +3.9 cm | 101.894 | +4.8 cm | 102.032 |
| 2027-01 | 35.5 | -2.2 | +1.7 cm | 101.911 | +6.1 cm | 102.093 |

- **Szansa realizacji:** 13.8 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.021 m (+2.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.911 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.203 m (+20.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 102.093 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 41.0 | -2.1 | +5.0 cm | 101.94 | +4.0 cm | 101.93 |
| 2026-03 | 47.6 | 2.0 | +4.5 cm | 101.985 | +3.3 cm | 101.963 |
| 2026-04 | 35.4 | 7.7 | -2.5 cm | 101.96 | +0.9 cm | 101.972 |
| 2026-05 | 60.2 | 12.6 | -5.1 cm | 101.909 | -1.5 cm | 101.957 |
| 2026-06 | 71.7 | 16.0 | -6.6 cm | 101.843 | -1.0 cm | 101.948 |
| 2026-07 | 99.5 | 17.4 | -5.8 cm | 101.786 | -0.3 cm | 101.945 |
| 2026-08 | 76.7 | 17.4 | -3.3 cm | 101.753 | +0.3 cm | 101.948 |
| 2026-09 | 64.1 | 12.9 | +0.1 cm | 101.753 | +1.5 cm | 101.963 |
| 2026-10 | 44.6 | 8.1 | +5.1 cm | 101.805 | +2.9 cm | 101.992 |
| 2026-11 | 47.0 | 2.9 | +5.1 cm | 101.856 | +5.0 cm | 102.042 |
| 2026-12 | 47.8 | -0.4 | +3.8 cm | 101.894 | +7.0 cm | 102.112 |
| 2027-01 | 48.5 | -2.2 | +1.8 cm | 101.912 | +7.8 cm | 102.191 |

- **Szansa realizacji:** 7.3 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.022 m (+2.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.912 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.301 m (+30.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 102.191 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 19.3 | -0.1 | +5.1 cm | 101.941 | +3.7 cm | 101.927 |
| 2026-03 | 22.0 | 4.2 | +3.6 cm | 101.976 | +3.1 cm | 101.958 |
| 2026-04 | 15.9 | 8.7 | -2.4 cm | 101.953 | +0.9 cm | 101.967 |
| 2026-05 | 30.2 | 13.8 | -4.4 cm | 101.908 | -1.8 cm | 101.95 |
| 2026-06 | 36.6 | 16.8 | -5.6 cm | 101.853 | -2.7 cm | 101.923 |
| 2026-07 | 47.1 | 19.5 | -5.3 cm | 101.8 | -4.4 cm | 101.879 |
| 2026-08 | 37.2 | 18.5 | -2.5 cm | 101.774 | -4.5 cm | 101.834 |
| 2026-09 | 22.9 | 13.9 | +0.7 cm | 101.781 | -2.6 cm | 101.807 |
| 2026-10 | 18.0 | 9.1 | +5.2 cm | 101.833 | -0.5 cm | 101.802 |
| 2026-11 | 23.5 | 4.5 | +5.3 cm | 101.885 | +1.7 cm | 101.819 |
| 2026-12 | 26.2 | 1.2 | +3.8 cm | 101.923 | +3.2 cm | 101.851 |
| 2027-01 | 23.3 | -0.2 | +1.7 cm | 101.94 | +4.3 cm | 101.894 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.050 m (+5.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.94 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.004 m (+0.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.894 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 29.5 | -0.1 | +5.0 cm | 101.94 | +3.9 cm | 101.929 |
| 2026-03 | 30.8 | 4.2 | +3.4 cm | 101.974 | +3.2 cm | 101.961 |
| 2026-04 | 28.2 | 8.7 | -3.1 cm | 101.943 | +0.4 cm | 101.966 |
| 2026-05 | 42.4 | 13.8 | -5.4 cm | 101.889 | -2.7 cm | 101.939 |
| 2026-06 | 55.5 | 16.8 | -5.7 cm | 101.832 | -3.2 cm | 101.907 |
| 2026-07 | 65.5 | 19.5 | -5.8 cm | 101.775 | -2.9 cm | 101.878 |
| 2026-08 | 52.7 | 18.5 | -3.1 cm | 101.743 | -1.9 cm | 101.858 |
| 2026-09 | 40.6 | 13.9 | +0.8 cm | 101.752 | -0.5 cm | 101.853 |
| 2026-10 | 29.0 | 9.1 | +5.1 cm | 101.803 | +1.4 cm | 101.867 |
| 2026-11 | 37.2 | 4.5 | +5.5 cm | 101.858 | +3.1 cm | 101.898 |
| 2026-12 | 39.2 | 1.2 | +3.9 cm | 101.897 | +4.8 cm | 101.946 |
| 2027-01 | 35.5 | -0.2 | +1.7 cm | 101.914 | +6.0 cm | 102.005 |

- **Szansa realizacji:** 16.0 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.024 m (+2.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.914 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.115 m (+11.5 cm)
- **Poziom na koniec stycznia 2027 (natural):** 102.005 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 41.0 | -0.1 | +5.0 cm | 101.94 | +4.0 cm | 101.93 |
| 2026-03 | 47.6 | 4.2 | +3.5 cm | 101.975 | +3.0 cm | 101.96 |
| 2026-04 | 35.4 | 8.7 | -2.5 cm | 101.951 | +0.1 cm | 101.961 |
| 2026-05 | 60.2 | 13.8 | -5.1 cm | 101.9 | -2.1 cm | 101.94 |
| 2026-06 | 71.7 | 16.8 | -6.6 cm | 101.834 | -1.7 cm | 101.923 |
| 2026-07 | 99.5 | 19.5 | -5.8 cm | 101.776 | -2.0 cm | 101.903 |
| 2026-08 | 76.7 | 18.5 | -3.3 cm | 101.743 | -0.6 cm | 101.897 |
| 2026-09 | 64.1 | 13.9 | +0.0 cm | 101.743 | +2.6 cm | 101.923 |
| 2026-10 | 44.6 | 9.1 | +5.1 cm | 101.795 | +4.7 cm | 101.97 |
| 2026-11 | 47.0 | 4.5 | +5.6 cm | 101.85 | +8.0 cm | 102.049 |
| 2026-12 | 47.8 | 1.2 | +3.8 cm | 101.889 | +9.5 cm | 102.144 |
| 2027-01 | 48.5 | -0.2 | +1.8 cm | 101.906 | +9.6 cm | 102.241 |

- **Szansa realizacji:** 7.6 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.016 m (+1.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.906 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.351 m (+35.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 102.241 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 19.3 | 3.1 | +4.4 cm | 101.934 | +3.6 cm | 101.926 |
| 2026-03 | 22.0 | 5.1 | +3.8 cm | 101.972 | +2.9 cm | 101.956 |
| 2026-04 | 15.9 | 9.4 | -2.1 cm | 101.951 | +0.8 cm | 101.963 |
| 2026-05 | 30.2 | 14.8 | -4.6 cm | 101.905 | -1.8 cm | 101.945 |
| 2026-06 | 36.6 | 18.8 | -5.9 cm | 101.846 | -3.1 cm | 101.914 |
| 2026-07 | 47.1 | 20.1 | -5.3 cm | 101.793 | -4.5 cm | 101.869 |
| 2026-08 | 37.2 | 19.4 | -2.3 cm | 101.77 | -5.8 cm | 101.811 |
| 2026-09 | 22.9 | 15.6 | +2.9 cm | 101.799 | -4.0 cm | 101.77 |
| 2026-10 | 18.0 | 10.6 | +5.7 cm | 101.856 | -0.4 cm | 101.766 |
| 2026-11 | 23.5 | 5.4 | +4.5 cm | 101.901 | +1.9 cm | 101.786 |
| 2026-12 | 26.2 | 2.2 | +0.9 cm | 101.91 | +2.9 cm | 101.814 |
| 2027-01 | 23.3 | 1.8 | -1.0 cm | 101.9 | +4.0 cm | 101.854 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.010 m (+1.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.9 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.036 m (-3.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.854 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 29.5 | 3.1 | +4.3 cm | 101.933 | +3.8 cm | 101.928 |
| 2026-03 | 30.8 | 5.1 | +3.7 cm | 101.97 | +3.0 cm | 101.958 |
| 2026-04 | 28.2 | 9.4 | -2.3 cm | 101.947 | +0.3 cm | 101.961 |
| 2026-05 | 42.4 | 14.8 | -4.7 cm | 101.901 | -2.7 cm | 101.934 |
| 2026-06 | 55.5 | 18.8 | -5.9 cm | 101.841 | -3.6 cm | 101.898 |
| 2026-07 | 65.5 | 20.1 | -5.8 cm | 101.784 | -4.5 cm | 101.852 |
| 2026-08 | 52.7 | 19.4 | -3.1 cm | 101.753 | -4.8 cm | 101.804 |
| 2026-09 | 40.6 | 15.6 | +0.8 cm | 101.761 | -2.8 cm | 101.776 |
| 2026-10 | 29.0 | 10.6 | +5.1 cm | 101.812 | +0.9 cm | 101.785 |
| 2026-11 | 37.2 | 5.4 | +5.5 cm | 101.867 | +3.1 cm | 101.815 |
| 2026-12 | 39.2 | 2.2 | +3.8 cm | 101.904 | +4.5 cm | 101.86 |
| 2027-01 | 35.5 | 1.8 | +1.7 cm | 101.922 | +5.9 cm | 101.919 |

- **Szansa realizacji:** 15.8 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.032 m (+3.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.922 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.029 m (+2.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.919 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 41.0 | 3.1 | +4.4 cm | 101.934 | +3.9 cm | 101.929 |
| 2026-03 | 47.6 | 5.1 | +3.8 cm | 101.971 | +2.9 cm | 101.957 |
| 2026-04 | 35.4 | 9.4 | -2.2 cm | 101.949 | -0.1 cm | 101.956 |
| 2026-05 | 60.2 | 14.8 | -5.3 cm | 101.897 | -2.0 cm | 101.936 |
| 2026-06 | 71.7 | 18.8 | -6.6 cm | 101.83 | -2.0 cm | 101.916 |
| 2026-07 | 99.5 | 20.1 | -5.8 cm | 101.773 | -2.2 cm | 101.894 |
| 2026-08 | 76.7 | 19.4 | -3.3 cm | 101.739 | -0.6 cm | 101.888 |
| 2026-09 | 64.1 | 15.6 | +0.0 cm | 101.74 | +2.9 cm | 101.916 |
| 2026-10 | 44.6 | 10.6 | +5.1 cm | 101.791 | +5.3 cm | 101.969 |
| 2026-11 | 47.0 | 5.4 | +5.5 cm | 101.846 | +8.1 cm | 102.05 |
| 2026-12 | 47.8 | 2.2 | +3.7 cm | 101.883 | +9.4 cm | 102.144 |
| 2027-01 | 48.5 | 1.8 | +1.8 cm | 101.901 | +9.5 cm | 102.239 |

- **Szansa realizacji:** 7.6 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.011 m (+1.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.901 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.349 m (+34.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 102.239 m n.p.m.




*Wygenerowano: 2026-02-15 15:44*