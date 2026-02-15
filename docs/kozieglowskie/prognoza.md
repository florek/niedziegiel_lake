# Raport: Jezioro Koziegłowskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Koziegłowskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/kozieglowskie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/kozieglowskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 11.7 | 100.903 | 101.212 |
| zimny, normalny | 14.3 | 101.1 | 101.297 |
| zimny, wilgotny | 6.8 | 101.234 | 101.377 |
| normalny, suchy | 12.1 | 100.887 | 101.176 |
| normalny, normalny | 15.2 | 101.092 | 101.202 |
| normalny, wilgotny | 6.9 | 101.227 | 101.304 |
| ciepły, suchy | 11.7 | 100.876 | 100.954 |
| ciepły, normalny | 14.4 | 101.103 | 101.114 |
| ciepły, wilgotny | 6.8 | 101.217 | 101.211 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (101.0031 m n.p.m.):
- **Model drenażowy:** 101.05 m n.p.m. – przybędzie +0.047 m (+4.7 cm)
- **Model naturalny (sprzed drenażu):** 101.191 m n.p.m. – przybędzie +0.188 m (+18.8 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.5 | 1.4 | +10.8 cm | 101.111 | +10.6 cm | 101.109 |
| 2026-03 | 32.8 | 4.4 | +11.0 cm | 101.221 | +10.3 cm | 101.212 |
| 2026-04 | 25.4 | 9.4 | +9.1 cm | 101.312 | +9.2 cm | 101.304 |
| 2026-05 | 49.0 | 14.0 | +3.4 cm | 101.346 | +6.0 cm | 101.364 |
| 2026-06 | 50.5 | 17.8 | -4.3 cm | 101.303 | -3.9 cm | 101.325 |
| 2026-07 | 69.7 | 19.7 | -7.4 cm | 101.229 | -6.0 cm | 101.265 |
| 2026-08 | 54.2 | 19.2 | -8.2 cm | 101.147 | -6.0 cm | 101.205 |
| 2026-09 | 37.1 | 14.9 | -6.9 cm | 101.078 | -5.3 cm | 101.152 |
| 2026-10 | 36.4 | 9.8 | -5.4 cm | 101.023 | -3.3 cm | 101.119 |
| 2026-11 | 33.4 | 4.8 | -2.0 cm | 101.003 | -1.8 cm | 101.101 |
| 2026-12 | 33.9 | 1.4 | +1.1 cm | 101.014 | +2.6 cm | 101.127 |
| 2027-01 | 38.2 | -0.1 | +3.6 cm | 101.05 | +6.4 cm | 101.191 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 495.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.047 m (+4.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.05 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.188 m (+18.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.191 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 26.0 | -0.9 | +10.8 cm | 101.111 | +10.6 cm | 101.109 |
| 2026-03 | 22.3 | 3.3 | +11.1 cm | 101.222 | +10.7 cm | 101.216 |
| 2026-04 | 15.2 | 8.4 | +8.1 cm | 101.302 | +9.1 cm | 101.306 |
| 2026-05 | 35.4 | 13.1 | +3.6 cm | 101.338 | +7.8 cm | 101.384 |
| 2026-06 | 34.1 | 16.5 | -5.3 cm | 101.285 | -3.9 cm | 101.345 |
| 2026-07 | 54.5 | 19.0 | -9.8 cm | 101.187 | -5.9 cm | 101.286 |
| 2026-08 | 34.2 | 18.3 | -10.5 cm | 101.082 | -7.3 cm | 101.214 |
| 2026-09 | 22.4 | 13.7 | -9.6 cm | 100.986 | -4.8 cm | 101.165 |
| 2026-10 | 22.7 | 8.5 | -8.3 cm | 100.903 | -2.4 cm | 101.142 |
| 2026-11 | 19.4 | 3.8 | -2.8 cm | 100.875 | -1.3 cm | 101.128 |
| 2026-12 | 24.8 | -0.2 | +0.4 cm | 100.879 | +2.4 cm | 101.153 |
| 2027-01 | 27.9 | -2.0 | +2.4 cm | 100.903 | +5.9 cm | 101.212 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 8.5 °C
- **Suma opadu (prognoza):** 338.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.100 m (-10.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.903 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.209 m (+20.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.212 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.8 | -0.9 | +10.8 cm | 101.111 | +10.6 cm | 101.109 |
| 2026-03 | 33.6 | 3.3 | +11.2 cm | 101.223 | +10.6 cm | 101.215 |
| 2026-04 | 28.6 | 8.4 | +9.7 cm | 101.319 | +9.2 cm | 101.308 |
| 2026-05 | 47.6 | 13.1 | +5.1 cm | 101.37 | +8.4 cm | 101.392 |
| 2026-06 | 54.0 | 16.5 | -4.2 cm | 101.328 | -2.7 cm | 101.364 |
| 2026-07 | 67.5 | 19.0 | -8.0 cm | 101.248 | -6.3 cm | 101.302 |
| 2026-08 | 57.5 | 18.3 | -9.6 cm | 101.152 | -5.7 cm | 101.245 |
| 2026-09 | 40.6 | 13.7 | -6.7 cm | 101.085 | -4.2 cm | 101.203 |
| 2026-10 | 38.8 | 8.5 | -5.5 cm | 101.03 | +1.1 cm | 101.214 |
| 2026-11 | 38.4 | 3.8 | -0.9 cm | 101.022 | +0.3 cm | 101.217 |
| 2026-12 | 35.8 | -0.2 | +3.0 cm | 101.051 | +2.9 cm | 101.246 |
| 2027-01 | 40.0 | -2.0 | +4.9 cm | 101.1 | +5.1 cm | 101.297 |

- **Szansa realizacji:** 14.3 %
- **Średnia temperatura roczna (prognoza):** 8.5 °C
- **Suma opadu (prognoza):** 517.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.097 m (+9.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.1 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.294 m (+29.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.297 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 48.8 | -0.9 | +10.8 cm | 101.111 | +11.0 cm | 101.113 |
| 2026-03 | 49.5 | 3.3 | +11.2 cm | 101.223 | +11.1 cm | 101.224 |
| 2026-04 | 36.4 | 8.4 | +9.6 cm | 101.319 | +9.3 cm | 101.317 |
| 2026-05 | 75.4 | 13.1 | +4.2 cm | 101.361 | +8.8 cm | 101.406 |
| 2026-06 | 71.7 | 16.5 | -2.8 cm | 101.333 | -2.6 cm | 101.379 |
| 2026-07 | 101.3 | 19.0 | -4.6 cm | 101.287 | -6.3 cm | 101.316 |
| 2026-08 | 81.8 | 18.3 | -6.4 cm | 101.223 | -5.7 cm | 101.259 |
| 2026-09 | 55.0 | 13.7 | -3.8 cm | 101.185 | -1.9 cm | 101.24 |
| 2026-10 | 55.2 | 8.5 | -3.0 cm | 101.154 | +2.8 cm | 101.268 |
| 2026-11 | 46.9 | 3.8 | +1.1 cm | 101.166 | +2.2 cm | 101.29 |
| 2026-12 | 46.0 | -0.2 | +3.1 cm | 101.197 | +3.2 cm | 101.322 |
| 2027-01 | 52.5 | -2.0 | +3.8 cm | 101.234 | +5.4 cm | 101.377 |

- **Szansa realizacji:** 6.8 %
- **Średnia temperatura roczna (prognoza):** 8.5 °C
- **Suma opadu (prognoza):** 720.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.231 m (+23.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.234 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.374 m (+37.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.377 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 26.0 | 1.0 | +10.8 cm | 101.111 | +10.7 cm | 101.11 |
| 2026-03 | 22.3 | 4.3 | +11.1 cm | 101.222 | +10.2 cm | 101.212 |
| 2026-04 | 15.2 | 9.1 | +8.0 cm | 101.302 | +9.1 cm | 101.303 |
| 2026-05 | 35.4 | 13.8 | +2.0 cm | 101.322 | +6.5 cm | 101.368 |
| 2026-06 | 34.1 | 18.0 | -5.4 cm | 101.268 | -3.9 cm | 101.329 |
| 2026-07 | 54.5 | 19.8 | -9.9 cm | 101.17 | -5.8 cm | 101.271 |
| 2026-08 | 34.2 | 19.3 | -9.4 cm | 101.076 | -7.2 cm | 101.199 |
| 2026-09 | 22.4 | 14.9 | -9.2 cm | 100.983 | -6.2 cm | 101.137 |
| 2026-10 | 22.7 | 9.8 | -8.0 cm | 100.904 | -5.5 cm | 101.083 |
| 2026-11 | 19.4 | 5.0 | -3.5 cm | 100.868 | -2.7 cm | 101.056 |
| 2026-12 | 24.8 | 1.7 | -0.7 cm | 100.862 | +4.0 cm | 101.096 |
| 2027-01 | 27.9 | -0.1 | +2.5 cm | 100.887 | +8.0 cm | 101.176 |

- **Szansa realizacji:** 12.1 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 338.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.116 m (-11.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.887 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.173 m (+17.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.176 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.8 | 1.0 | +10.8 cm | 101.111 | +10.7 cm | 101.11 |
| 2026-03 | 33.6 | 4.3 | +11.2 cm | 101.223 | +10.2 cm | 101.212 |
| 2026-04 | 28.6 | 9.1 | +9.6 cm | 101.319 | +9.2 cm | 101.304 |
| 2026-05 | 47.6 | 13.8 | +3.6 cm | 101.354 | +7.1 cm | 101.376 |
| 2026-06 | 54.0 | 18.0 | -4.4 cm | 101.311 | -2.7 cm | 101.348 |
| 2026-07 | 67.5 | 19.8 | -8.0 cm | 101.23 | -6.3 cm | 101.286 |
| 2026-08 | 57.5 | 19.3 | -8.3 cm | 101.147 | -5.4 cm | 101.232 |
| 2026-09 | 40.6 | 14.9 | -6.4 cm | 101.084 | -5.8 cm | 101.173 |
| 2026-10 | 38.8 | 9.8 | -4.2 cm | 101.042 | -4.6 cm | 101.127 |
| 2026-11 | 38.4 | 5.0 | -1.7 cm | 101.025 | -2.4 cm | 101.103 |
| 2026-12 | 35.8 | 1.7 | +1.6 cm | 101.041 | +2.5 cm | 101.128 |
| 2027-01 | 40.0 | -0.1 | +5.1 cm | 101.092 | +7.4 cm | 101.202 |

- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 517.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.089 m (+8.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.092 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.199 m (+19.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.202 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 48.8 | 1.0 | +10.8 cm | 101.111 | +11.1 cm | 101.114 |
| 2026-03 | 49.5 | 4.3 | +11.2 cm | 101.223 | +10.8 cm | 101.222 |
| 2026-04 | 36.4 | 9.1 | +9.6 cm | 101.318 | +9.3 cm | 101.315 |
| 2026-05 | 75.4 | 13.8 | +2.6 cm | 101.345 | +7.5 cm | 101.39 |
| 2026-06 | 71.7 | 18.0 | -2.9 cm | 101.316 | -2.7 cm | 101.363 |
| 2026-07 | 101.3 | 19.8 | -4.7 cm | 101.269 | -6.3 cm | 101.3 |
| 2026-08 | 81.8 | 19.3 | -5.1 cm | 101.218 | -5.7 cm | 101.243 |
| 2026-09 | 55.0 | 14.9 | -3.7 cm | 101.181 | -3.6 cm | 101.207 |
| 2026-10 | 55.2 | 9.8 | -3.0 cm | 101.15 | +0.8 cm | 101.216 |
| 2026-11 | 46.9 | 5.0 | +0.6 cm | 101.156 | +0.9 cm | 101.224 |
| 2026-12 | 46.0 | 1.7 | +3.2 cm | 101.187 | +3.0 cm | 101.254 |
| 2027-01 | 52.5 | -0.1 | +3.9 cm | 101.227 | +5.0 cm | 101.304 |

- **Szansa realizacji:** 6.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 720.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.224 m (+22.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.227 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.301 m (+30.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.304 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 26.0 | 4.0 | +10.8 cm | 101.111 | +10.4 cm | 101.107 |
| 2026-03 | 22.3 | 5.6 | +10.8 cm | 101.219 | +9.8 cm | 101.205 |
| 2026-04 | 15.2 | 10.6 | +8.1 cm | 101.3 | +9.1 cm | 101.295 |
| 2026-05 | 35.4 | 15.1 | +2.1 cm | 101.321 | +2.3 cm | 101.318 |
| 2026-06 | 34.1 | 19.0 | -5.2 cm | 101.268 | -7.0 cm | 101.248 |
| 2026-07 | 54.5 | 20.4 | -8.2 cm | 101.187 | -5.9 cm | 101.189 |
| 2026-08 | 34.2 | 20.0 | -9.0 cm | 101.096 | -7.2 cm | 101.117 |
| 2026-09 | 22.4 | 16.1 | -9.0 cm | 101.007 | -7.6 cm | 101.041 |
| 2026-10 | 22.7 | 11.3 | -8.1 cm | 100.926 | -9.2 cm | 100.949 |
| 2026-11 | 19.4 | 5.8 | -4.9 cm | 100.877 | -4.8 cm | 100.901 |
| 2026-12 | 24.8 | 2.7 | -1.6 cm | 100.861 | -0.3 cm | 100.898 |
| 2027-01 | 27.9 | 1.9 | +1.5 cm | 100.876 | +5.6 cm | 100.954 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 338.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.127 m (-12.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.876 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.049 m (-4.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 100.954 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.8 | 4.0 | +10.8 cm | 101.111 | +10.4 cm | 101.107 |
| 2026-03 | 33.6 | 5.6 | +10.9 cm | 101.22 | +9.7 cm | 101.204 |
| 2026-04 | 28.6 | 10.6 | +9.7 cm | 101.317 | +9.2 cm | 101.297 |
| 2026-05 | 47.6 | 15.1 | +3.6 cm | 101.353 | +2.9 cm | 101.326 |
| 2026-06 | 54.0 | 19.0 | -4.0 cm | 101.314 | -4.7 cm | 101.279 |
| 2026-07 | 67.5 | 20.4 | -5.9 cm | 101.255 | -5.7 cm | 101.223 |
| 2026-08 | 57.5 | 20.0 | -7.0 cm | 101.184 | -5.0 cm | 101.173 |
| 2026-09 | 40.6 | 16.1 | -6.3 cm | 101.121 | -6.7 cm | 101.106 |
| 2026-10 | 38.8 | 11.3 | -3.8 cm | 101.083 | -6.2 cm | 101.044 |
| 2026-11 | 38.4 | 5.8 | -2.9 cm | 101.054 | -3.7 cm | 101.007 |
| 2026-12 | 35.8 | 2.7 | +0.4 cm | 101.058 | +3.3 cm | 101.04 |
| 2027-01 | 40.0 | 1.9 | +4.5 cm | 101.103 | +7.4 cm | 101.114 |

- **Szansa realizacji:** 14.4 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 517.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.100 m (+10.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.103 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.111 m (+11.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.114 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 48.8 | 4.0 | +10.8 cm | 101.111 | +10.8 cm | 101.111 |
| 2026-03 | 49.5 | 5.6 | +10.9 cm | 101.221 | +10.3 cm | 101.214 |
| 2026-04 | 36.4 | 10.6 | +9.6 cm | 101.317 | +9.3 cm | 101.307 |
| 2026-05 | 75.4 | 15.1 | +2.7 cm | 101.344 | +3.3 cm | 101.34 |
| 2026-06 | 71.7 | 19.0 | -2.7 cm | 101.318 | -4.7 cm | 101.294 |
| 2026-07 | 101.3 | 20.4 | -3.3 cm | 101.285 | -5.8 cm | 101.236 |
| 2026-08 | 81.8 | 20.0 | -4.5 cm | 101.239 | -5.2 cm | 101.184 |
| 2026-09 | 55.0 | 16.1 | -4.4 cm | 101.195 | -4.3 cm | 101.141 |
| 2026-10 | 55.2 | 11.3 | -2.7 cm | 101.168 | -1.4 cm | 101.127 |
| 2026-11 | 46.9 | 5.8 | -0.4 cm | 101.164 | -1.4 cm | 101.113 |
| 2026-12 | 46.0 | 2.7 | +1.8 cm | 101.181 | +2.6 cm | 101.139 |
| 2027-01 | 52.5 | 1.9 | +3.6 cm | 101.217 | +7.1 cm | 101.211 |

- **Szansa realizacji:** 6.8 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 720.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.214 m (+21.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.217 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.208 m (+20.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.211 m n.p.m.




*Wygenerowano: 2026-02-15 15:44*