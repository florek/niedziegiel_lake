# Raport: Jezioro Wilczyńskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Wilczyńskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/wilczynskie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/wilczynskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 11.3 | 93.975 | 93.978 |
| zimny, normalny | 14.2 | 94.097 | 94.315 |
| zimny, wilgotny | 7.1 | 94.458 | 94.541 |
| normalny, suchy | 11.7 | 93.867 | 93.784 |
| normalny, normalny | 15.2 | 93.996 | 94.01 |
| normalny, wilgotny | 7.2 | 94.234 | 94.322 |
| ciepły, suchy | 11.5 | 93.812 | 93.765 |
| ciepły, normalny | 14.5 | 93.901 | 93.965 |
| ciepły, wilgotny | 7.2 | 94.129 | 94.27 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (94.0036 m n.p.m.):
- **Model drenażowy:** 94.017 m n.p.m. – przybędzie +0.013 m (+1.3 cm)
- **Model naturalny (sprzed drenażu):** 94.067 m n.p.m. – przybędzie +0.063 m (+6.3 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.0 | 1.2 | +8.1 cm | 94.084 | +8.4 cm | 94.087 |
| 2026-03 | 33.4 | 4.2 | +8.2 cm | 94.166 | +8.4 cm | 94.171 |
| 2026-04 | 25.1 | 9.3 | +5.3 cm | 94.219 | +8.0 cm | 94.251 |
| 2026-05 | 46.0 | 13.9 | +1.9 cm | 94.238 | +5.6 cm | 94.307 |
| 2026-06 | 50.1 | 17.7 | -1.4 cm | 94.224 | -2.7 cm | 94.28 |
| 2026-07 | 69.9 | 19.7 | -5.7 cm | 94.167 | -4.9 cm | 94.231 |
| 2026-08 | 53.6 | 19.2 | -6.2 cm | 94.105 | -6.2 cm | 94.169 |
| 2026-09 | 40.3 | 14.8 | -6.4 cm | 94.042 | -5.1 cm | 94.118 |
| 2026-10 | 31.5 | 9.8 | -4.6 cm | 93.995 | -4.6 cm | 94.072 |
| 2026-11 | 34.6 | 4.7 | -2.3 cm | 93.972 | -3.0 cm | 94.042 |
| 2026-12 | 34.9 | 1.4 | +1.9 cm | 93.992 | -0.9 cm | 94.033 |
| 2027-01 | 38.4 | 0.0 | +2.5 cm | 94.017 | +3.4 cm | 94.067 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 491.7 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.013 m (+1.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.017 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.063 m (+6.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.067 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | -1.0 | +8.2 cm | 94.086 | +8.1 cm | 94.084 |
| 2026-03 | 22.8 | 3.0 | +8.1 cm | 94.168 | +8.3 cm | 94.168 |
| 2026-04 | 15.0 | 8.4 | +4.6 cm | 94.213 | +6.9 cm | 94.236 |
| 2026-05 | 34.0 | 12.8 | +1.9 cm | 94.232 | +6.0 cm | 94.296 |
| 2026-06 | 33.6 | 16.5 | -1.7 cm | 94.215 | -0.2 cm | 94.295 |
| 2026-07 | 53.9 | 18.8 | -5.0 cm | 94.165 | -5.5 cm | 94.239 |
| 2026-08 | 35.5 | 18.3 | -5.5 cm | 94.11 | -7.9 cm | 94.161 |
| 2026-09 | 22.7 | 13.7 | -6.4 cm | 94.045 | -7.4 cm | 94.087 |
| 2026-10 | 17.6 | 8.3 | -4.2 cm | 94.004 | -7.4 cm | 94.013 |
| 2026-11 | 21.8 | 3.6 | -2.6 cm | 93.977 | -5.3 cm | 93.96 |
| 2026-12 | 25.6 | -0.2 | -0.2 cm | 93.975 | -0.7 cm | 93.952 |
| 2027-01 | 28.6 | -1.9 | -0.1 cm | 93.975 | +2.6 cm | 93.978 |

- **Szansa realizacji:** 11.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.029 m (-2.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.975 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.026 m (-2.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.978 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | -1.0 | +8.3 cm | 94.087 | +8.0 cm | 94.084 |
| 2026-03 | 33.9 | 3.0 | +8.8 cm | 94.175 | +8.4 cm | 94.168 |
| 2026-04 | 27.7 | 8.4 | +5.0 cm | 94.225 | +7.0 cm | 94.238 |
| 2026-05 | 46.4 | 12.8 | +1.9 cm | 94.245 | +8.1 cm | 94.319 |
| 2026-06 | 53.1 | 16.5 | -1.1 cm | 94.233 | +2.4 cm | 94.344 |
| 2026-07 | 66.7 | 18.8 | -4.0 cm | 94.194 | -2.2 cm | 94.322 |
| 2026-08 | 56.2 | 18.3 | -3.5 cm | 94.158 | -3.9 cm | 94.283 |
| 2026-09 | 43.3 | 13.7 | -4.7 cm | 94.111 | -2.9 cm | 94.253 |
| 2026-10 | 33.9 | 8.3 | -3.5 cm | 94.076 | -2.5 cm | 94.228 |
| 2026-11 | 38.8 | 3.6 | -2.5 cm | 94.051 | +0.3 cm | 94.231 |
| 2026-12 | 36.7 | -0.2 | +1.8 cm | 94.069 | +2.1 cm | 94.253 |
| 2027-01 | 39.8 | -1.9 | +2.8 cm | 94.097 | +6.2 cm | 94.315 |

- **Szansa realizacji:** 14.2 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.093 m (+9.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.097 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.311 m (+31.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.315 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | -1.0 | +8.2 cm | 94.086 | +9.6 cm | 94.1 |
| 2026-03 | 49.5 | 3.0 | +9.9 cm | 94.185 | +10.0 cm | 94.2 |
| 2026-04 | 36.1 | 8.4 | +6.8 cm | 94.253 | +11.7 cm | 94.317 |
| 2026-05 | 64.7 | 12.8 | +3.9 cm | 94.291 | +11.9 cm | 94.436 |
| 2026-06 | 70.6 | 16.5 | +3.4 cm | 94.325 | +3.7 cm | 94.474 |
| 2026-07 | 102.3 | 18.8 | -1.1 cm | 94.314 | -1.2 cm | 94.461 |
| 2026-08 | 77.4 | 18.3 | -1.6 cm | 94.298 | -4.0 cm | 94.422 |
| 2026-09 | 62.5 | 13.7 | -1.1 cm | 94.287 | -2.8 cm | 94.394 |
| 2026-10 | 49.0 | 8.3 | +0.4 cm | 94.291 | -1.8 cm | 94.376 |
| 2026-11 | 46.6 | 3.6 | +2.5 cm | 94.316 | +1.3 cm | 94.389 |
| 2026-12 | 46.4 | -0.2 | +5.6 cm | 94.373 | +6.0 cm | 94.449 |
| 2027-01 | 51.6 | -1.9 | +8.5 cm | 94.458 | +9.2 cm | 94.541 |

- **Szansa realizacji:** 7.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.454 m (+45.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.458 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.537 m (+53.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.541 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | 0.8 | +8.4 cm | 94.087 | +8.1 cm | 94.084 |
| 2026-03 | 22.8 | 4.3 | +7.1 cm | 94.158 | +8.1 cm | 94.166 |
| 2026-04 | 15.0 | 9.1 | +4.8 cm | 94.207 | +6.7 cm | 94.233 |
| 2026-05 | 34.0 | 13.7 | +1.2 cm | 94.219 | +3.8 cm | 94.271 |
| 2026-06 | 33.6 | 17.8 | -2.0 cm | 94.199 | -5.4 cm | 94.216 |
| 2026-07 | 53.9 | 19.8 | -6.7 cm | 94.133 | -7.8 cm | 94.139 |
| 2026-08 | 35.5 | 19.3 | -8.2 cm | 94.05 | -8.9 cm | 94.049 |
| 2026-09 | 22.7 | 14.7 | -7.8 cm | 93.973 | -7.1 cm | 93.978 |
| 2026-10 | 17.6 | 9.8 | -5.9 cm | 93.914 | -7.3 cm | 93.905 |
| 2026-11 | 21.8 | 4.8 | -3.5 cm | 93.88 | -5.9 cm | 93.846 |
| 2026-12 | 25.6 | 1.8 | +0.9 cm | 93.889 | -5.5 cm | 93.791 |
| 2027-01 | 28.6 | 0.1 | -2.1 cm | 93.867 | -0.7 cm | 93.784 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.137 m (-13.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.867 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.220 m (-22.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.784 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | 0.8 | +8.5 cm | 94.088 | +8.0 cm | 94.084 |
| 2026-03 | 33.9 | 4.3 | +8.0 cm | 94.168 | +8.2 cm | 94.166 |
| 2026-04 | 27.7 | 9.1 | +5.2 cm | 94.22 | +6.9 cm | 94.235 |
| 2026-05 | 46.4 | 13.7 | +1.4 cm | 94.234 | +6.1 cm | 94.296 |
| 2026-06 | 53.1 | 17.8 | -1.7 cm | 94.217 | -5.2 cm | 94.244 |
| 2026-07 | 66.7 | 19.8 | -6.6 cm | 94.152 | -5.7 cm | 94.187 |
| 2026-08 | 56.2 | 19.3 | -6.4 cm | 94.087 | -6.4 cm | 94.124 |
| 2026-09 | 43.3 | 14.7 | -6.8 cm | 94.019 | -5.6 cm | 94.067 |
| 2026-10 | 33.9 | 9.8 | -5.4 cm | 93.965 | -4.5 cm | 94.022 |
| 2026-11 | 38.8 | 4.8 | -3.3 cm | 93.933 | -3.3 cm | 93.989 |
| 2026-12 | 36.7 | 1.8 | +2.9 cm | 93.962 | -1.6 cm | 93.973 |
| 2027-01 | 39.8 | 0.1 | +3.4 cm | 93.996 | +3.7 cm | 94.01 |

- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.008 m (-0.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.996 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.006 m (+0.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.01 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | 0.8 | +8.3 cm | 94.087 | +9.6 cm | 94.1 |
| 2026-03 | 49.5 | 4.3 | +8.9 cm | 94.176 | +9.8 cm | 94.198 |
| 2026-04 | 36.1 | 9.1 | +7.0 cm | 94.246 | +11.6 cm | 94.314 |
| 2026-05 | 64.7 | 13.7 | +3.4 cm | 94.28 | +7.7 cm | 94.391 |
| 2026-06 | 70.6 | 17.8 | +0.9 cm | 94.29 | -2.7 cm | 94.364 |
| 2026-07 | 102.3 | 19.8 | -4.0 cm | 94.25 | -2.5 cm | 94.339 |
| 2026-08 | 77.4 | 19.3 | -5.7 cm | 94.193 | -3.9 cm | 94.3 |
| 2026-09 | 62.5 | 14.7 | -4.0 cm | 94.153 | -2.1 cm | 94.279 |
| 2026-10 | 49.0 | 9.8 | -3.5 cm | 94.118 | -1.9 cm | 94.261 |
| 2026-11 | 46.6 | 4.8 | -0.7 cm | 94.111 | -0.8 cm | 94.253 |
| 2026-12 | 46.4 | 1.8 | +5.0 cm | 94.162 | +1.6 cm | 94.269 |
| 2027-01 | 51.6 | 0.1 | +7.2 cm | 94.234 | +5.3 cm | 94.322 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.230 m (+23.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.234 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.318 m (+31.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.322 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | 3.8 | +7.6 cm | 94.079 | +8.1 cm | 94.084 |
| 2026-03 | 22.8 | 5.4 | +7.1 cm | 94.15 | +7.6 cm | 94.16 |
| 2026-04 | 15.0 | 10.4 | +4.5 cm | 94.195 | +7.0 cm | 94.23 |
| 2026-05 | 34.0 | 15.1 | +1.4 cm | 94.209 | +2.3 cm | 94.253 |
| 2026-06 | 33.6 | 18.9 | -3.7 cm | 94.172 | -5.5 cm | 94.198 |
| 2026-07 | 53.9 | 20.4 | -8.2 cm | 94.089 | -7.8 cm | 94.12 |
| 2026-08 | 35.5 | 20.0 | -9.2 cm | 93.997 | -8.9 cm | 94.031 |
| 2026-09 | 22.7 | 16.0 | -9.3 cm | 93.904 | -7.1 cm | 93.96 |
| 2026-10 | 17.6 | 11.2 | -6.2 cm | 93.842 | -7.3 cm | 93.886 |
| 2026-11 | 21.8 | 5.7 | -2.4 cm | 93.818 | -6.0 cm | 93.826 |
| 2026-12 | 25.6 | 2.6 | -0.5 cm | 93.813 | -5.5 cm | 93.771 |
| 2027-01 | 28.6 | 1.9 | -0.0 cm | 93.812 | -0.6 cm | 93.765 |

- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.192 m (-19.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.812 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.239 m (-23.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.765 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | 3.8 | +7.7 cm | 94.08 | +8.0 cm | 94.084 |
| 2026-03 | 33.9 | 5.4 | +8.0 cm | 94.16 | +7.7 cm | 94.16 |
| 2026-04 | 27.7 | 10.4 | +4.9 cm | 94.208 | +7.2 cm | 94.233 |
| 2026-05 | 46.4 | 15.1 | +1.0 cm | 94.218 | +3.2 cm | 94.265 |
| 2026-06 | 53.1 | 18.9 | -3.5 cm | 94.183 | -5.3 cm | 94.212 |
| 2026-07 | 66.7 | 20.4 | -8.0 cm | 94.103 | -5.7 cm | 94.154 |
| 2026-08 | 56.2 | 20.0 | -7.2 cm | 94.031 | -6.3 cm | 94.091 |
| 2026-09 | 43.3 | 16.0 | -8.1 cm | 93.95 | -5.6 cm | 94.035 |
| 2026-10 | 33.9 | 11.2 | -5.9 cm | 93.891 | -4.6 cm | 93.989 |
| 2026-11 | 38.8 | 5.7 | -3.1 cm | 93.86 | -3.5 cm | 93.954 |
| 2026-12 | 36.7 | 2.6 | +1.7 cm | 93.877 | -1.6 cm | 93.938 |
| 2027-01 | 39.8 | 1.9 | +2.3 cm | 93.901 | +2.8 cm | 93.965 |

- **Szansa realizacji:** 14.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.103 m (-10.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.901 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.039 m (-3.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.965 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | 3.8 | +7.5 cm | 94.078 | +9.6 cm | 94.1 |
| 2026-03 | 49.5 | 5.4 | +8.9 cm | 94.168 | +9.2 cm | 94.192 |
| 2026-04 | 36.1 | 10.4 | +6.6 cm | 94.234 | +11.6 cm | 94.308 |
| 2026-05 | 64.7 | 15.1 | +3.5 cm | 94.269 | +4.4 cm | 94.352 |
| 2026-06 | 70.6 | 18.9 | +1.1 cm | 94.279 | -4.2 cm | 94.31 |
| 2026-07 | 102.3 | 20.4 | -4.0 cm | 94.239 | -2.5 cm | 94.285 |
| 2026-08 | 77.4 | 20.0 | -7.1 cm | 94.169 | -3.4 cm | 94.251 |
| 2026-09 | 62.5 | 16.0 | -5.8 cm | 94.111 | -2.7 cm | 94.224 |
| 2026-10 | 49.0 | 11.2 | -5.2 cm | 94.059 | -1.6 cm | 94.208 |
| 2026-11 | 46.6 | 5.7 | -2.1 cm | 94.038 | -0.9 cm | 94.198 |
| 2026-12 | 46.4 | 2.6 | +3.2 cm | 94.069 | +1.7 cm | 94.216 |
| 2027-01 | 51.6 | 1.9 | +6.0 cm | 94.129 | +5.4 cm | 94.27 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.125 m (+12.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.129 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.266 m (+26.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.27 m n.p.m.




*Wygenerowano: 2026-02-15 15:45*