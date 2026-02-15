# Raport: Jezioro Koziegłowskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Koziegłowskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/kozieglowskie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Symulacje wariantów pogodowych (12 miesięcy do przodu)

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/kozieglowskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykres: pełny zakres historii (od 1974) + 12 miesięcy symulacji.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa realizacji (%) |
|---------|------------------------|
| zimny, suchy | 11.7 |
| zimny, normalny | 14.3 |
| zimny, wilgotny | 6.8 |
| normalny, suchy | 12.1 |
| normalny, normalny | 15.2 |
| normalny, wilgotny | 6.9 |
| ciepły, suchy | 11.7 |
| ciepły, normalny | 14.4 |
| ciepły, wilgotny | 6.8 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów): **101.191 m n.p.m.** W stosunku do stanu na koniec stycznia 2026 (101.0031 m n.p.m.): przybędzie +0.188 m (+18.8 cm).


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.5 | 1.4 | +10.8 cm | 101.111 |
| 2026-03 | 32.8 | 4.4 | +10.7 cm | 101.218 |
| 2026-04 | 25.4 | 9.4 | +8.5 cm | 101.303 |
| 2026-05 | 49.0 | 14.0 | +5.6 cm | 101.359 |
| 2026-06 | 50.5 | 17.8 | -4.2 cm | 101.317 |
| 2026-07 | 69.7 | 19.7 | -5.8 cm | 101.259 |
| 2026-08 | 54.2 | 19.2 | -5.5 cm | 101.204 |
| 2026-09 | 37.1 | 14.9 | -5.4 cm | 101.15 |
| 2026-10 | 36.4 | 9.8 | -3.6 cm | 101.114 |
| 2026-11 | 33.4 | 4.8 | -0.8 cm | 101.106 |
| 2026-12 | 33.9 | 1.4 | +2.1 cm | 101.128 |
| 2027-01 | 38.2 | -0.1 | +6.4 cm | 101.191 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 495.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.188 m (+18.8 cm)
- **Poziom na koniec stycznia 2027:** 101.191 m n.p.m.

### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 26.0 | -0.9 | +10.8 cm | 101.111 |
| 2026-03 | 22.3 | 3.3 | +11.2 cm | 101.223 |
| 2026-04 | 15.2 | 8.4 | +8.8 cm | 101.311 |
| 2026-05 | 35.4 | 13.1 | +7.5 cm | 101.386 |
| 2026-06 | 34.1 | 16.5 | -3.8 cm | 101.348 |
| 2026-07 | 54.5 | 19.0 | -7.0 cm | 101.278 |
| 2026-08 | 34.2 | 18.3 | -6.6 cm | 101.212 |
| 2026-09 | 22.4 | 13.7 | -6.5 cm | 101.147 |
| 2026-10 | 22.7 | 8.5 | -3.9 cm | 101.108 |
| 2026-11 | 19.4 | 3.8 | -1.3 cm | 101.095 |
| 2026-12 | 24.8 | -0.2 | +3.3 cm | 101.128 |
| 2027-01 | 27.9 | -2.0 | +7.1 cm | 101.199 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 8.5 °C
- **Suma opadu (prognoza):** 338.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.196 m (+19.6 cm)
- **Poziom na koniec stycznia 2027:** 101.199 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.8 | -0.9 | +10.8 cm | 101.111 |
| 2026-03 | 33.6 | 3.3 | +11.2 cm | 101.222 |
| 2026-04 | 28.6 | 8.4 | +8.9 cm | 101.311 |
| 2026-05 | 47.6 | 13.1 | +7.9 cm | 101.39 |
| 2026-06 | 54.0 | 16.5 | -3.4 cm | 101.356 |
| 2026-07 | 67.5 | 19.0 | -5.6 cm | 101.3 |
| 2026-08 | 57.5 | 18.3 | -5.3 cm | 101.247 |
| 2026-09 | 40.6 | 13.7 | -3.2 cm | 101.214 |
| 2026-10 | 38.8 | 8.5 | +0.7 cm | 101.221 |
| 2026-11 | 38.4 | 3.8 | +1.0 cm | 101.231 |
| 2026-12 | 35.8 | -0.2 | +2.6 cm | 101.257 |
| 2027-01 | 40.0 | -2.0 | +5.3 cm | 101.31 |

- **Szansa realizacji:** 14.3 %
- **Średnia temperatura roczna (prognoza):** 8.5 °C
- **Suma opadu (prognoza):** 517.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.307 m (+30.7 cm)
- **Poziom na koniec stycznia 2027:** 101.31 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 48.8 | -0.9 | +11.2 cm | 101.115 |
| 2026-03 | 49.5 | 3.3 | +11.6 cm | 101.231 |
| 2026-04 | 36.4 | 8.4 | +8.8 cm | 101.319 |
| 2026-05 | 75.4 | 13.1 | +8.3 cm | 101.402 |
| 2026-06 | 71.7 | 16.5 | -2.8 cm | 101.374 |
| 2026-07 | 101.3 | 19.0 | -5.4 cm | 101.32 |
| 2026-08 | 81.8 | 18.3 | -3.9 cm | 101.28 |
| 2026-09 | 55.0 | 13.7 | -1.9 cm | 101.262 |
| 2026-10 | 55.2 | 8.5 | +1.5 cm | 101.277 |
| 2026-11 | 46.9 | 3.8 | +1.4 cm | 101.291 |
| 2026-12 | 46.0 | -0.2 | +2.8 cm | 101.319 |
| 2027-01 | 52.5 | -2.0 | +5.9 cm | 101.378 |

- **Szansa realizacji:** 6.8 %
- **Średnia temperatura roczna (prognoza):** 8.5 °C
- **Suma opadu (prognoza):** 720.6 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.375 m (+37.5 cm)
- **Poziom na koniec stycznia 2027:** 101.378 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 26.0 | 1.0 | +10.8 cm | 101.112 |
| 2026-03 | 22.3 | 4.3 | +11.0 cm | 101.221 |
| 2026-04 | 15.2 | 9.1 | +8.3 cm | 101.304 |
| 2026-05 | 35.4 | 13.8 | +6.5 cm | 101.369 |
| 2026-06 | 34.1 | 18.0 | -3.6 cm | 101.333 |
| 2026-07 | 54.5 | 19.8 | -6.6 cm | 101.266 |
| 2026-08 | 34.2 | 19.3 | -6.7 cm | 101.199 |
| 2026-09 | 22.4 | 14.9 | -7.8 cm | 101.121 |
| 2026-10 | 22.7 | 9.8 | -8.6 cm | 101.035 |
| 2026-11 | 19.4 | 5.0 | -5.1 cm | 100.984 |
| 2026-12 | 24.8 | 1.7 | +0.6 cm | 100.99 |
| 2027-01 | 27.9 | -0.1 | +6.0 cm | 101.05 |

- **Szansa realizacji:** 12.1 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 338.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.047 m (+4.7 cm)
- **Poziom na koniec stycznia 2027:** 101.05 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.8 | 1.0 | +10.8 cm | 101.111 |
| 2026-03 | 33.6 | 4.3 | +10.9 cm | 101.22 |
| 2026-04 | 28.6 | 9.1 | +8.4 cm | 101.304 |
| 2026-05 | 47.6 | 13.8 | +6.9 cm | 101.372 |
| 2026-06 | 54.0 | 18.0 | -3.4 cm | 101.339 |
| 2026-07 | 67.5 | 19.8 | -5.3 cm | 101.285 |
| 2026-08 | 57.5 | 19.3 | -5.4 cm | 101.232 |
| 2026-09 | 40.6 | 14.9 | -5.0 cm | 101.182 |
| 2026-10 | 38.8 | 9.8 | -3.0 cm | 101.151 |
| 2026-11 | 38.4 | 5.0 | +0.4 cm | 101.155 |
| 2026-12 | 35.8 | 1.7 | +2.6 cm | 101.181 |
| 2027-01 | 40.0 | -0.1 | +7.1 cm | 101.252 |

- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 517.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.249 m (+24.9 cm)
- **Poziom na koniec stycznia 2027:** 101.252 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 48.8 | 1.0 | +11.2 cm | 101.115 |
| 2026-03 | 49.5 | 4.3 | +11.3 cm | 101.228 |
| 2026-04 | 36.4 | 9.1 | +8.3 cm | 101.311 |
| 2026-05 | 75.4 | 13.8 | +7.3 cm | 101.384 |
| 2026-06 | 71.7 | 18.0 | -2.7 cm | 101.358 |
| 2026-07 | 101.3 | 19.8 | -5.1 cm | 101.307 |
| 2026-08 | 81.8 | 19.3 | -4.1 cm | 101.265 |
| 2026-09 | 55.0 | 14.9 | -4.2 cm | 101.223 |
| 2026-10 | 55.2 | 9.8 | -1.9 cm | 101.204 |
| 2026-11 | 46.9 | 5.0 | +0.9 cm | 101.213 |
| 2026-12 | 46.0 | 1.7 | +2.8 cm | 101.241 |
| 2027-01 | 52.5 | -0.1 | +5.5 cm | 101.296 |

- **Szansa realizacji:** 6.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 720.6 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.293 m (+29.3 cm)
- **Poziom na koniec stycznia 2027:** 101.296 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 26.0 | 4.0 | +10.6 cm | 101.109 |
| 2026-03 | 22.3 | 5.6 | +9.9 cm | 101.208 |
| 2026-04 | 15.2 | 10.6 | +8.3 cm | 101.291 |
| 2026-05 | 35.4 | 15.1 | +1.8 cm | 101.31 |
| 2026-06 | 34.1 | 19.0 | -6.4 cm | 101.246 |
| 2026-07 | 54.5 | 20.4 | -6.5 cm | 101.18 |
| 2026-08 | 34.2 | 20.0 | -6.5 cm | 101.115 |
| 2026-09 | 22.4 | 16.1 | -8.1 cm | 101.034 |
| 2026-10 | 22.7 | 11.3 | -8.4 cm | 100.95 |
| 2026-11 | 19.4 | 5.8 | -4.9 cm | 100.902 |
| 2026-12 | 24.8 | 2.7 | -0.7 cm | 100.895 |
| 2027-01 | 27.9 | 1.9 | +5.8 cm | 100.953 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 338.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.050 m (-5.0 cm)
- **Poziom na koniec stycznia 2027:** 100.953 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.8 | 4.0 | +10.6 cm | 101.109 |
| 2026-03 | 33.6 | 5.6 | +9.8 cm | 101.207 |
| 2026-04 | 28.6 | 10.6 | +8.4 cm | 101.291 |
| 2026-05 | 47.6 | 15.1 | +2.1 cm | 101.312 |
| 2026-06 | 54.0 | 19.0 | -6.3 cm | 101.249 |
| 2026-07 | 67.5 | 20.4 | -5.2 cm | 101.197 |
| 2026-08 | 57.5 | 20.0 | -5.1 cm | 101.146 |
| 2026-09 | 40.6 | 16.1 | -5.5 cm | 101.091 |
| 2026-10 | 38.8 | 11.3 | -3.4 cm | 101.057 |
| 2026-11 | 38.4 | 5.8 | +1.2 cm | 101.069 |
| 2026-12 | 35.8 | 2.7 | +2.9 cm | 101.097 |
| 2027-01 | 40.0 | 1.9 | +7.2 cm | 101.169 |

- **Szansa realizacji:** 14.4 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 517.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.166 m (+16.6 cm)
- **Poziom na koniec stycznia 2027:** 101.169 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 48.8 | 4.0 | +11.0 cm | 101.113 |
| 2026-03 | 49.5 | 5.6 | +10.2 cm | 101.215 |
| 2026-04 | 36.4 | 10.6 | +8.3 cm | 101.298 |
| 2026-05 | 75.4 | 15.1 | +2.5 cm | 101.324 |
| 2026-06 | 71.7 | 19.0 | -4.3 cm | 101.28 |
| 2026-07 | 101.3 | 20.4 | -4.9 cm | 101.231 |
| 2026-08 | 81.8 | 20.0 | -4.2 cm | 101.19 |
| 2026-09 | 55.0 | 16.1 | -5.0 cm | 101.14 |
| 2026-10 | 55.2 | 11.3 | -3.1 cm | 101.11 |
| 2026-11 | 46.9 | 5.8 | +0.3 cm | 101.112 |
| 2026-12 | 46.0 | 2.7 | +2.7 cm | 101.139 |
| 2027-01 | 52.5 | 1.9 | +7.3 cm | 101.212 |

- **Szansa realizacji:** 6.8 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 720.6 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.209 m (+20.9 cm)
- **Poziom na koniec stycznia 2027:** 101.212 m n.p.m.



*Wygenerowano: 2026-02-15 14:10*