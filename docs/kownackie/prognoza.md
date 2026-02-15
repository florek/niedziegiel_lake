# Raport: Jezioro Kownackie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Kownackie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/kownackie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/kownackie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 11.3 | 92.942 | 93.149 |
| zimny, normalny | 14.2 | 93.019 | 93.249 |
| zimny, wilgotny | 7.1 | 93.235 | 93.34 |
| normalny, suchy | 11.7 | 92.784 | 93.075 |
| normalny, normalny | 15.2 | 92.902 | 93.196 |
| normalny, wilgotny | 7.2 | 93.046 | 93.271 |
| ciepły, suchy | 11.5 | 92.71 | 93.047 |
| ciepły, normalny | 14.5 | 92.824 | 93.172 |
| ciepły, wilgotny | 7.2 | 92.966 | 93.236 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (93.2357 m n.p.m.):
- **Model drenażowy:** 92.915 m n.p.m. – ubędzie 0.321 m (-32.1 cm)
- **Model naturalny (sprzed drenażu):** 93.182 m n.p.m. – ubędzie 0.054 m (-5.4 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.0 | 1.2 | +0.5 cm | 93.241 | +3.1 cm | 93.266 |
| 2026-03 | 33.4 | 4.2 | +0.6 cm | 93.246 | +3.4 cm | 93.301 |
| 2026-04 | 25.1 | 9.3 | -1.1 cm | 93.235 | +2.6 cm | 93.327 |
| 2026-05 | 46.0 | 13.9 | -3.2 cm | 93.203 | +2.4 cm | 93.351 |
| 2026-06 | 50.1 | 17.7 | -3.9 cm | 93.164 | -2.2 cm | 93.329 |
| 2026-07 | 69.9 | 19.7 | -4.6 cm | 93.118 | -3.8 cm | 93.291 |
| 2026-08 | 53.6 | 19.2 | -5.6 cm | 93.062 | -4.3 cm | 93.248 |
| 2026-09 | 40.3 | 14.8 | -5.3 cm | 93.009 | -5.6 cm | 93.192 |
| 2026-10 | 31.5 | 9.8 | -4.7 cm | 92.962 | -4.7 cm | 93.145 |
| 2026-11 | 34.6 | 4.7 | -3.7 cm | 92.925 | -1.5 cm | 93.13 |
| 2026-12 | 34.9 | 1.4 | -1.6 cm | 92.909 | +0.9 cm | 93.139 |
| 2027-01 | 38.4 | 0.0 | +0.6 cm | 92.915 | +4.3 cm | 93.182 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 491.7 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.321 m (-32.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.915 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.054 m (-5.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.182 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | -1.0 | +1.2 cm | 93.248 | +3.0 cm | 93.266 |
| 2026-03 | 22.8 | 3.0 | +0.3 cm | 93.251 | +3.4 cm | 93.3 |
| 2026-04 | 15.0 | 8.4 | -1.8 cm | 93.233 | +2.5 cm | 93.326 |
| 2026-05 | 34.0 | 12.8 | -3.4 cm | 93.199 | +1.9 cm | 93.345 |
| 2026-06 | 33.6 | 16.5 | -3.9 cm | 93.16 | +0.0 cm | 93.345 |
| 2026-07 | 53.9 | 18.8 | -4.0 cm | 93.121 | -5.3 cm | 93.292 |
| 2026-08 | 35.5 | 18.3 | -4.3 cm | 93.077 | -5.5 cm | 93.238 |
| 2026-09 | 22.7 | 13.7 | -4.8 cm | 93.029 | -7.1 cm | 93.166 |
| 2026-10 | 17.6 | 8.3 | -4.9 cm | 92.98 | -5.4 cm | 93.112 |
| 2026-11 | 21.8 | 3.6 | -3.4 cm | 92.946 | -1.8 cm | 93.094 |
| 2026-12 | 25.6 | -0.2 | -0.9 cm | 92.937 | +0.6 cm | 93.1 |
| 2027-01 | 28.6 | -1.9 | +0.5 cm | 92.942 | +4.9 cm | 93.149 |

- **Szansa realizacji:** 11.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.294 m (-29.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.942 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.087 m (-8.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.149 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | -1.0 | +1.2 cm | 93.248 | +2.9 cm | 93.265 |
| 2026-03 | 33.9 | 3.0 | +0.9 cm | 93.257 | +3.4 cm | 93.299 |
| 2026-04 | 27.7 | 8.4 | -0.6 cm | 93.251 | +2.9 cm | 93.328 |
| 2026-05 | 46.4 | 12.8 | -1.5 cm | 93.236 | +2.3 cm | 93.351 |
| 2026-06 | 53.1 | 16.5 | -3.3 cm | 93.203 | +0.5 cm | 93.355 |
| 2026-07 | 66.7 | 18.8 | -4.0 cm | 93.162 | -2.3 cm | 93.332 |
| 2026-08 | 56.2 | 18.3 | -4.6 cm | 93.117 | -4.2 cm | 93.29 |
| 2026-09 | 43.3 | 13.7 | -5.1 cm | 93.066 | -6.2 cm | 93.228 |
| 2026-10 | 33.9 | 8.3 | -3.7 cm | 93.029 | -3.7 cm | 93.191 |
| 2026-11 | 38.8 | 3.6 | -2.5 cm | 93.004 | -1.5 cm | 93.176 |
| 2026-12 | 36.7 | -0.2 | -0.2 cm | 93.002 | +1.4 cm | 93.19 |
| 2027-01 | 39.8 | -1.9 | +1.7 cm | 93.019 | +5.9 cm | 93.249 |

- **Szansa realizacji:** 14.2 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.217 m (-21.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.019 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.013 m (+1.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.249 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | -1.0 | +1.4 cm | 93.25 | +2.9 cm | 93.265 |
| 2026-03 | 49.5 | 3.0 | +1.9 cm | 93.269 | +3.5 cm | 93.3 |
| 2026-04 | 36.1 | 8.4 | +1.6 cm | 93.286 | +3.1 cm | 93.331 |
| 2026-05 | 64.7 | 12.8 | -0.4 cm | 93.282 | +4.2 cm | 93.374 |
| 2026-06 | 70.6 | 16.5 | -3.3 cm | 93.249 | +2.9 cm | 93.402 |
| 2026-07 | 102.3 | 18.8 | -3.8 cm | 93.211 | +0.3 cm | 93.405 |
| 2026-08 | 77.4 | 18.3 | -3.9 cm | 93.172 | -4.2 cm | 93.363 |
| 2026-09 | 62.5 | 13.7 | -4.0 cm | 93.131 | -4.9 cm | 93.315 |
| 2026-10 | 49.0 | 8.3 | -2.7 cm | 93.104 | -3.5 cm | 93.279 |
| 2026-11 | 46.6 | 3.6 | +3.9 cm | 93.143 | -0.5 cm | 93.274 |
| 2026-12 | 46.4 | -0.2 | +3.8 cm | 93.181 | +1.3 cm | 93.286 |
| 2027-01 | 51.6 | -1.9 | +5.4 cm | 93.235 | +5.3 cm | 93.34 |

- **Szansa realizacji:** 7.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.001 m (-0.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.235 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.104 m (+10.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.34 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | 0.8 | -0.1 cm | 93.234 | +2.9 cm | 93.265 |
| 2026-03 | 22.8 | 4.3 | -0.0 cm | 93.234 | +4.0 cm | 93.305 |
| 2026-04 | 15.0 | 9.1 | -3.0 cm | 93.204 | +2.4 cm | 93.329 |
| 2026-05 | 34.0 | 13.7 | -4.9 cm | 93.154 | +1.6 cm | 93.345 |
| 2026-06 | 33.6 | 17.8 | -4.9 cm | 93.106 | -3.8 cm | 93.306 |
| 2026-07 | 53.9 | 19.8 | -5.2 cm | 93.054 | -5.9 cm | 93.248 |
| 2026-08 | 35.5 | 19.3 | -6.8 cm | 92.986 | -4.7 cm | 93.201 |
| 2026-09 | 22.7 | 14.7 | -5.0 cm | 92.937 | -6.6 cm | 93.135 |
| 2026-10 | 17.6 | 9.8 | -5.1 cm | 92.885 | -6.1 cm | 93.074 |
| 2026-11 | 21.8 | 4.8 | -6.0 cm | 92.825 | -2.5 cm | 93.05 |
| 2026-12 | 25.6 | 1.8 | -3.6 cm | 92.789 | +0.1 cm | 93.05 |
| 2027-01 | 28.6 | 0.1 | -0.4 cm | 92.784 | +2.5 cm | 93.075 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.452 m (-45.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.784 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.161 m (-16.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.075 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | 0.8 | +0.0 cm | 93.236 | +2.8 cm | 93.264 |
| 2026-03 | 33.9 | 4.3 | +0.6 cm | 93.242 | +4.0 cm | 93.304 |
| 2026-04 | 27.7 | 9.1 | -1.5 cm | 93.227 | +2.7 cm | 93.331 |
| 2026-05 | 46.4 | 13.7 | -2.6 cm | 93.201 | +1.9 cm | 93.351 |
| 2026-06 | 53.1 | 17.8 | -3.6 cm | 93.165 | -3.1 cm | 93.319 |
| 2026-07 | 66.7 | 19.8 | -4.2 cm | 93.123 | -4.1 cm | 93.278 |
| 2026-08 | 56.2 | 19.3 | -5.8 cm | 93.065 | -3.7 cm | 93.241 |
| 2026-09 | 43.3 | 14.7 | -5.1 cm | 93.014 | -5.3 cm | 93.189 |
| 2026-10 | 33.9 | 9.8 | -4.8 cm | 92.967 | -4.3 cm | 93.146 |
| 2026-11 | 38.8 | 4.8 | -4.4 cm | 92.923 | -1.5 cm | 93.131 |
| 2026-12 | 36.7 | 1.8 | -2.7 cm | 92.896 | +1.4 cm | 93.145 |
| 2027-01 | 39.8 | 0.1 | +0.6 cm | 92.902 | +5.1 cm | 93.196 |

- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.334 m (-33.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.902 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.040 m (-4.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.196 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | 0.8 | +0.2 cm | 93.238 | +2.8 cm | 93.264 |
| 2026-03 | 49.5 | 4.3 | +1.6 cm | 93.254 | +4.2 cm | 93.305 |
| 2026-04 | 36.1 | 9.1 | +1.5 cm | 93.269 | +3.0 cm | 93.335 |
| 2026-05 | 64.7 | 13.7 | -2.0 cm | 93.249 | +3.7 cm | 93.372 |
| 2026-06 | 70.6 | 17.8 | -3.5 cm | 93.214 | -1.5 cm | 93.357 |
| 2026-07 | 102.3 | 19.8 | -4.0 cm | 93.174 | -1.3 cm | 93.344 |
| 2026-08 | 77.4 | 19.3 | -4.7 cm | 93.128 | -3.6 cm | 93.308 |
| 2026-09 | 62.5 | 14.7 | -4.5 cm | 93.082 | -4.4 cm | 93.264 |
| 2026-10 | 49.0 | 9.8 | -4.3 cm | 93.039 | -4.3 cm | 93.221 |
| 2026-11 | 46.6 | 4.8 | -3.1 cm | 93.008 | -0.7 cm | 93.214 |
| 2026-12 | 46.4 | 1.8 | +0.5 cm | 93.013 | +1.2 cm | 93.226 |
| 2027-01 | 51.6 | 0.1 | +3.3 cm | 93.046 | +4.5 cm | 93.271 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.190 m (-19.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.046 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.035 m (+3.5 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.271 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 25.8 | 3.8 | +0.0 cm | 93.236 | +3.5 cm | 93.27 |
| 2026-03 | 22.8 | 5.4 | -0.7 cm | 93.229 | +2.7 cm | 93.297 |
| 2026-04 | 15.0 | 10.4 | -3.0 cm | 93.199 | +2.1 cm | 93.318 |
| 2026-05 | 34.0 | 15.1 | -6.6 cm | 93.133 | +1.8 cm | 93.336 |
| 2026-06 | 33.6 | 18.9 | -5.0 cm | 93.082 | -5.7 cm | 93.28 |
| 2026-07 | 53.9 | 20.4 | -5.6 cm | 93.026 | -6.3 cm | 93.217 |
| 2026-08 | 35.5 | 20.0 | -6.8 cm | 92.958 | -4.7 cm | 93.17 |
| 2026-09 | 22.7 | 16.0 | -6.2 cm | 92.896 | -5.9 cm | 93.111 |
| 2026-10 | 17.6 | 11.2 | -5.9 cm | 92.837 | -6.1 cm | 93.05 |
| 2026-11 | 21.8 | 5.7 | -6.4 cm | 92.773 | -2.0 cm | 93.03 |
| 2026-12 | 25.6 | 2.6 | -3.7 cm | 92.736 | -0.2 cm | 93.027 |
| 2027-01 | 28.6 | 1.9 | -2.6 cm | 92.71 | +2.0 cm | 93.047 |

- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.526 m (-52.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.71 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.189 m (-18.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.047 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 34.4 | 3.8 | +0.2 cm | 93.238 | +3.3 cm | 93.269 |
| 2026-03 | 33.9 | 5.4 | +0.3 cm | 93.241 | +2.8 cm | 93.297 |
| 2026-04 | 27.7 | 10.4 | -1.5 cm | 93.226 | +2.4 cm | 93.321 |
| 2026-05 | 46.4 | 15.1 | -3.6 cm | 93.19 | +2.2 cm | 93.343 |
| 2026-06 | 53.1 | 18.9 | -3.8 cm | 93.152 | -4.2 cm | 93.301 |
| 2026-07 | 66.7 | 20.4 | -5.1 cm | 93.101 | -4.5 cm | 93.256 |
| 2026-08 | 56.2 | 20.0 | -6.9 cm | 93.032 | -3.6 cm | 93.22 |
| 2026-09 | 43.3 | 16.0 | -6.7 cm | 92.966 | -4.9 cm | 93.171 |
| 2026-10 | 33.9 | 11.2 | -5.2 cm | 92.914 | -4.3 cm | 93.128 |
| 2026-11 | 38.8 | 5.7 | -4.6 cm | 92.868 | -1.5 cm | 93.114 |
| 2026-12 | 36.7 | 2.6 | -3.0 cm | 92.838 | +1.3 cm | 93.127 |
| 2027-01 | 39.8 | 1.9 | -1.4 cm | 92.824 | +4.5 cm | 93.172 |

- **Szansa realizacji:** 14.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.412 m (-41.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.824 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.064 m (-6.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.172 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temp. (°C) | Zmiana drenaż (cm) | Poziom drenaż (m) | Zmiana natural (cm) | Poziom natural (m) |
|------|-----------|------------|---------------------|-------------------|----------------------|--------------------|
| 2026-02 | 46.4 | 3.8 | +0.4 cm | 93.24 | +3.3 cm | 93.269 |
| 2026-03 | 49.5 | 5.4 | +1.5 cm | 93.255 | +2.9 cm | 93.298 |
| 2026-04 | 36.1 | 10.4 | +1.5 cm | 93.27 | +2.8 cm | 93.326 |
| 2026-05 | 64.7 | 15.1 | -3.0 cm | 93.24 | +3.9 cm | 93.365 |
| 2026-06 | 70.6 | 18.9 | -3.9 cm | 93.201 | -2.5 cm | 93.34 |
| 2026-07 | 102.3 | 20.4 | -4.8 cm | 93.153 | -1.6 cm | 93.324 |
| 2026-08 | 77.4 | 20.0 | -5.8 cm | 93.095 | -5.1 cm | 93.274 |
| 2026-09 | 62.5 | 16.0 | -5.7 cm | 93.038 | -3.8 cm | 93.235 |
| 2026-10 | 49.0 | 11.2 | -4.8 cm | 92.99 | -4.3 cm | 93.192 |
| 2026-11 | 46.6 | 5.7 | -3.6 cm | 92.954 | -0.7 cm | 93.184 |
| 2026-12 | 46.4 | 2.6 | -0.7 cm | 92.947 | +1.1 cm | 93.196 |
| 2027-01 | 51.6 | 1.9 | +1.9 cm | 92.966 | +4.0 cm | 93.236 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.270 m (-27.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.966 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.000 m (+0.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.236 m n.p.m.




*Wygenerowano: 2026-02-15 15:44*