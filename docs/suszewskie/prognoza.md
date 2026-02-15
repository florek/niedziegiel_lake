# Raport: Jezioro Suszewskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Suszewskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/suszewskie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/suszewskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 11.5 | 93.594 | 93.899 |
| zimny, normalny | 14.1 | 93.762 | 94.058 |
| zimny, wilgotny | 7.1 | 94.258 | 94.489 |
| normalny, suchy | 11.9 | 93.583 | 93.679 |
| normalny, normalny | 15.0 | 93.729 | 93.837 |
| normalny, wilgotny | 7.3 | 94.201 | 94.178 |
| ciepły, suchy | 11.6 | 93.517 | 93.452 |
| ciepły, normalny | 14.3 | 93.683 | 93.615 |
| ciepły, wilgotny | 7.2 | 93.974 | 93.886 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (93.7383 m n.p.m.):
- **Model drenażowy:** 93.759 m n.p.m. – przybędzie +0.021 m (+2.1 cm)
- **Model naturalny (sprzed drenażu):** 93.855 m n.p.m. – przybędzie +0.117 m (+11.7 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.3 | 1.3 | +13.9 cm | 93.877 | +3.6 cm | 93.774 |
| 2026-03 | 34.2 | 4.4 | +18.1 cm | 94.058 | +13.3 cm | 93.907 |
| 2026-04 | 25.7 | 9.3 | +13.3 cm | 94.191 | +18.8 cm | 94.095 |
| 2026-05 | 47.7 | 13.8 | +6.4 cm | 94.255 | +12.0 cm | 94.214 |
| 2026-06 | 50.3 | 17.8 | -2.6 cm | 94.229 | +0.5 cm | 94.219 |
| 2026-07 | 68.4 | 19.9 | -10.3 cm | 94.127 | -4.8 cm | 94.172 |
| 2026-08 | 54.3 | 19.2 | -10.8 cm | 94.019 | -8.2 cm | 94.089 |
| 2026-09 | 38.8 | 14.9 | -10.2 cm | 93.917 | -9.0 cm | 94.0 |
| 2026-10 | 33.6 | 9.8 | -9.1 cm | 93.826 | -9.6 cm | 93.904 |
| 2026-11 | 34.2 | 4.7 | -6.2 cm | 93.764 | -6.4 cm | 93.84 |
| 2026-12 | 35.3 | 1.4 | -2.7 cm | 93.737 | -2.6 cm | 93.814 |
| 2027-01 | 38.3 | -0.1 | +2.2 cm | 93.759 | +4.2 cm | 93.855 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 495.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.021 m (+2.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.759 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.117 m (+11.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.855 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | -1.1 | +13.3 cm | 93.872 | +3.6 cm | 93.774 |
| 2026-03 | 22.6 | 3.2 | +17.1 cm | 94.042 | +12.8 cm | 93.902 |
| 2026-04 | 15.6 | 8.3 | +12.2 cm | 94.165 | +20.1 cm | 94.103 |
| 2026-05 | 34.9 | 12.8 | +6.6 cm | 94.231 | +16.3 cm | 94.266 |
| 2026-06 | 33.1 | 16.5 | -4.2 cm | 94.189 | +3.5 cm | 94.301 |
| 2026-07 | 53.0 | 19.3 | -9.9 cm | 94.09 | -4.4 cm | 94.257 |
| 2026-08 | 35.1 | 18.4 | -11.4 cm | 93.976 | -7.9 cm | 94.177 |
| 2026-09 | 22.6 | 13.7 | -12.1 cm | 93.855 | -10.6 cm | 94.071 |
| 2026-10 | 20.1 | 8.4 | -10.1 cm | 93.754 | -10.9 cm | 93.962 |
| 2026-11 | 21.2 | 3.5 | -7.1 cm | 93.683 | -8.1 cm | 93.882 |
| 2026-12 | 25.4 | -0.2 | -4.7 cm | 93.636 | -2.0 cm | 93.861 |
| 2027-01 | 28.2 | -2.0 | -4.2 cm | 93.594 | +3.8 cm | 93.899 |

- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 337.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.144 m (-14.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.594 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.161 m (+16.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.899 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.8 | -1.1 | +13.8 cm | 93.876 | +3.6 cm | 93.774 |
| 2026-03 | 35.8 | 3.2 | +18.1 cm | 94.057 | +13.6 cm | 93.911 |
| 2026-04 | 28.6 | 8.3 | +13.3 cm | 94.19 | +20.2 cm | 94.113 |
| 2026-05 | 47.6 | 12.8 | +8.6 cm | 94.275 | +17.1 cm | 94.284 |
| 2026-06 | 54.0 | 16.5 | -0.4 cm | 94.271 | +3.2 cm | 94.316 |
| 2026-07 | 66.1 | 19.3 | -8.3 cm | 94.188 | -3.8 cm | 94.278 |
| 2026-08 | 57.5 | 18.4 | -10.1 cm | 94.088 | -5.9 cm | 94.219 |
| 2026-09 | 42.1 | 13.7 | -10.2 cm | 93.986 | -8.4 cm | 94.135 |
| 2026-10 | 35.9 | 8.4 | -9.3 cm | 93.893 | -8.9 cm | 94.046 |
| 2026-11 | 38.4 | 3.5 | -7.3 cm | 93.82 | -5.0 cm | 93.997 |
| 2026-12 | 37.6 | -0.2 | -3.6 cm | 93.784 | +0.2 cm | 93.998 |
| 2027-01 | 39.5 | -2.0 | -2.2 cm | 93.762 | +6.0 cm | 94.058 |

- **Szansa realizacji:** 14.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 517.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.024 m (+2.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.762 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.320 m (+32.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.058 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 47.2 | -1.1 | +14.9 cm | 93.887 | +3.6 cm | 93.774 |
| 2026-03 | 49.9 | 3.2 | +20.0 cm | 94.087 | +14.3 cm | 93.918 |
| 2026-04 | 36.2 | 8.3 | +15.1 cm | 94.238 | +20.6 cm | 94.124 |
| 2026-05 | 68.5 | 12.8 | +8.7 cm | 94.325 | +19.6 cm | 94.32 |
| 2026-06 | 71.0 | 16.5 | -0.6 cm | 94.319 | +7.7 cm | 94.397 |
| 2026-07 | 97.8 | 19.3 | -8.3 cm | 94.236 | -2.3 cm | 94.374 |
| 2026-08 | 78.9 | 18.4 | -9.9 cm | 94.137 | -5.0 cm | 94.324 |
| 2026-09 | 58.4 | 13.7 | -6.7 cm | 94.07 | -6.3 cm | 94.262 |
| 2026-10 | 51.1 | 8.4 | -5.9 cm | 94.011 | -6.7 cm | 94.195 |
| 2026-11 | 46.8 | 3.5 | -2.7 cm | 93.984 | -1.0 cm | 94.184 |
| 2026-12 | 46.7 | -0.2 | +4.2 cm | 94.026 | +10.7 cm | 94.291 |
| 2027-01 | 52.4 | -2.0 | +23.2 cm | 94.258 | +19.8 cm | 94.489 |

- **Szansa realizacji:** 7.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 704.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.520 m (+52.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.258 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.751 m (+75.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.489 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | 1.0 | +13.3 cm | 93.872 | +3.6 cm | 93.774 |
| 2026-03 | 22.6 | 4.3 | +17.1 cm | 94.042 | +12.9 cm | 93.904 |
| 2026-04 | 15.6 | 9.1 | +12.2 cm | 94.165 | +19.4 cm | 94.098 |
| 2026-05 | 34.9 | 13.6 | +5.0 cm | 94.215 | +13.6 cm | 94.234 |
| 2026-06 | 33.1 | 17.9 | -4.2 cm | 94.173 | +0.0 cm | 94.234 |
| 2026-07 | 53.0 | 19.8 | -10.5 cm | 94.067 | -5.2 cm | 94.183 |
| 2026-08 | 35.1 | 19.3 | -10.8 cm | 93.959 | -10.6 cm | 94.077 |
| 2026-09 | 22.6 | 14.8 | -12.4 cm | 93.835 | -10.9 cm | 93.968 |
| 2026-10 | 20.1 | 9.8 | -10.3 cm | 93.731 | -11.3 cm | 93.855 |
| 2026-11 | 21.2 | 4.9 | -6.9 cm | 93.663 | -9.4 cm | 93.761 |
| 2026-12 | 25.4 | 1.8 | -4.8 cm | 93.614 | -7.3 cm | 93.688 |
| 2027-01 | 28.2 | -0.1 | -3.1 cm | 93.583 | -0.9 cm | 93.679 |

- **Szansa realizacji:** 11.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 337.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.155 m (-15.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.583 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.059 m (-5.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.679 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.8 | 1.0 | +13.8 cm | 93.876 | +3.6 cm | 93.774 |
| 2026-03 | 35.8 | 4.3 | +18.1 cm | 94.057 | +13.8 cm | 93.912 |
| 2026-04 | 28.6 | 9.1 | +13.3 cm | 94.19 | +19.6 cm | 94.108 |
| 2026-05 | 47.6 | 13.6 | +6.8 cm | 94.257 | +14.3 cm | 94.251 |
| 2026-06 | 54.0 | 17.9 | -1.9 cm | 94.238 | +0.1 cm | 94.252 |
| 2026-07 | 66.1 | 19.8 | -9.2 cm | 94.146 | -4.4 cm | 94.208 |
| 2026-08 | 57.5 | 19.3 | -9.5 cm | 94.051 | -6.9 cm | 94.139 |
| 2026-09 | 42.1 | 14.8 | -10.5 cm | 93.945 | -8.8 cm | 94.051 |
| 2026-10 | 35.9 | 9.8 | -9.5 cm | 93.85 | -8.9 cm | 93.962 |
| 2026-11 | 38.4 | 4.9 | -7.3 cm | 93.777 | -7.0 cm | 93.892 |
| 2026-12 | 37.6 | 1.8 | -3.8 cm | 93.739 | -6.3 cm | 93.829 |
| 2027-01 | 39.5 | -0.1 | -1.1 cm | 93.729 | +0.9 cm | 93.837 |

- **Szansa realizacji:** 15.0 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 517.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.009 m (-0.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.729 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.099 m (+9.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.837 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 47.2 | 1.0 | +14.9 cm | 93.887 | +3.6 cm | 93.774 |
| 2026-03 | 49.9 | 4.3 | +20.0 cm | 94.087 | +14.5 cm | 93.919 |
| 2026-04 | 36.2 | 9.1 | +15.1 cm | 94.238 | +20.0 cm | 94.119 |
| 2026-05 | 68.5 | 13.6 | +6.9 cm | 94.306 | +15.3 cm | 94.272 |
| 2026-06 | 71.0 | 17.9 | -2.1 cm | 94.286 | +1.1 cm | 94.283 |
| 2026-07 | 97.8 | 19.8 | -9.0 cm | 94.195 | -4.0 cm | 94.243 |
| 2026-08 | 78.9 | 19.3 | -9.3 cm | 94.102 | -7.8 cm | 94.165 |
| 2026-09 | 58.4 | 14.8 | -7.5 cm | 94.027 | -6.7 cm | 94.098 |
| 2026-10 | 51.1 | 9.8 | -6.2 cm | 93.966 | -7.0 cm | 94.028 |
| 2026-11 | 46.8 | 4.9 | -3.0 cm | 93.935 | -3.2 cm | 93.996 |
| 2026-12 | 46.7 | 1.8 | +3.7 cm | 93.972 | +4.8 cm | 94.044 |
| 2027-01 | 52.4 | -0.1 | +22.9 cm | 94.201 | +13.5 cm | 94.178 |

- **Szansa realizacji:** 7.3 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 704.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.463 m (+46.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.201 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.440 m (+44.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.178 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | 3.8 | +13.3 cm | 93.872 | +3.5 cm | 93.773 |
| 2026-03 | 22.6 | 5.5 | +17.1 cm | 94.042 | +12.1 cm | 93.895 |
| 2026-04 | 15.6 | 10.5 | +12.2 cm | 94.165 | +16.2 cm | 94.057 |
| 2026-05 | 34.9 | 15.0 | +4.0 cm | 94.205 | +3.9 cm | 94.095 |
| 2026-06 | 33.1 | 18.9 | -4.8 cm | 94.157 | -4.2 cm | 94.053 |
| 2026-07 | 53.0 | 20.4 | -13.6 cm | 94.021 | -7.5 cm | 93.978 |
| 2026-08 | 35.1 | 20.0 | -13.5 cm | 93.887 | -11.2 cm | 93.866 |
| 2026-09 | 22.6 | 16.1 | -11.9 cm | 93.768 | -10.9 cm | 93.757 |
| 2026-10 | 20.1 | 11.2 | -10.3 cm | 93.665 | -12.1 cm | 93.636 |
| 2026-11 | 21.2 | 5.7 | -6.8 cm | 93.596 | -9.2 cm | 93.544 |
| 2026-12 | 25.4 | 2.6 | -4.8 cm | 93.548 | -8.0 cm | 93.464 |
| 2027-01 | 28.2 | 1.9 | -3.1 cm | 93.517 | -1.1 cm | 93.452 |

- **Szansa realizacji:** 11.6 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 337.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.221 m (-22.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.517 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.286 m (-28.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.452 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.8 | 3.8 | +13.8 cm | 93.876 | +3.5 cm | 93.773 |
| 2026-03 | 35.8 | 5.5 | +18.1 cm | 94.057 | +12.8 cm | 93.901 |
| 2026-04 | 28.6 | 10.5 | +13.3 cm | 94.19 | +16.4 cm | 94.065 |
| 2026-05 | 47.6 | 15.0 | +5.8 cm | 94.247 | +4.1 cm | 94.106 |
| 2026-06 | 54.0 | 18.9 | -2.5 cm | 94.222 | -2.5 cm | 94.081 |
| 2026-07 | 66.1 | 20.4 | -11.7 cm | 94.106 | -5.3 cm | 94.028 |
| 2026-08 | 57.5 | 20.0 | -11.1 cm | 93.995 | -8.9 cm | 93.939 |
| 2026-09 | 42.1 | 16.1 | -10.0 cm | 93.895 | -8.8 cm | 93.851 |
| 2026-10 | 35.9 | 11.2 | -9.9 cm | 93.796 | -9.7 cm | 93.754 |
| 2026-11 | 38.4 | 5.7 | -6.7 cm | 93.729 | -6.8 cm | 93.686 |
| 2026-12 | 37.6 | 2.6 | -3.8 cm | 93.691 | -7.4 cm | 93.612 |
| 2027-01 | 39.5 | 1.9 | -0.8 cm | 93.683 | +0.3 cm | 93.615 |

- **Szansa realizacji:** 14.3 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 517.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.055 m (-5.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.683 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.123 m (-12.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.615 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 47.2 | 3.8 | +14.9 cm | 93.887 | +3.5 cm | 93.773 |
| 2026-03 | 49.9 | 5.5 | +20.0 cm | 94.087 | +13.5 cm | 93.908 |
| 2026-04 | 36.2 | 10.5 | +15.1 cm | 94.238 | +16.8 cm | 94.076 |
| 2026-05 | 68.5 | 15.0 | +5.9 cm | 94.296 | +5.1 cm | 94.127 |
| 2026-06 | 71.0 | 18.9 | -2.5 cm | 94.272 | -1.6 cm | 94.111 |
| 2026-07 | 97.8 | 20.4 | -11.7 cm | 94.155 | -5.5 cm | 94.057 |
| 2026-08 | 78.9 | 20.0 | -10.9 cm | 94.046 | -9.8 cm | 93.959 |
| 2026-09 | 58.4 | 16.1 | -6.9 cm | 93.977 | -6.7 cm | 93.891 |
| 2026-10 | 51.1 | 11.2 | -6.6 cm | 93.911 | -8.4 cm | 93.807 |
| 2026-11 | 46.8 | 5.7 | -3.9 cm | 93.873 | -3.2 cm | 93.775 |
| 2026-12 | 46.7 | 2.6 | -0.0 cm | 93.873 | +3.5 cm | 93.81 |
| 2027-01 | 52.4 | 1.9 | +10.1 cm | 93.974 | +7.6 cm | 93.886 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 704.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.236 m (+23.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.974 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.148 m (+14.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.886 m n.p.m.




*Wygenerowano: 2026-02-15 15:45*