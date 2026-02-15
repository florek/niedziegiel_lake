# Raport: Jezioro Koziegłowskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Koziegłowskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska linia: poziom z pliku `data/kozieglowskie/data.csv` (pomiar na pierwszy dzień miesiąca). Przerywana pomarańczowa: wahania poziomu według modelu (scenariusz kumulatywny z prognozy zmiany miesięcznej).

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

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów): **101.196 m n.p.m.** W stosunku do stanu na koniec stycznia 2026 (101.0031 m n.p.m.): przybędzie +0.193 m (+19.3 cm).


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.5 | 1.4 | +10.9 cm | 101.112 |
| 2026-03 | 32.8 | 4.4 | +10.7 cm | 101.219 |
| 2026-04 | 25.4 | 9.4 | +7.8 cm | 101.297 |
| 2026-05 | 49.0 | 14.0 | +4.8 cm | 101.345 |
| 2026-06 | 50.5 | 17.8 | -4.6 cm | 101.299 |
| 2026-07 | 69.7 | 19.7 | -5.8 cm | 101.241 |
| 2026-08 | 54.2 | 19.2 | -5.5 cm | 101.186 |
| 2026-09 | 37.1 | 14.9 | -5.7 cm | 101.129 |
| 2026-10 | 36.4 | 9.8 | -3.8 cm | 101.092 |
| 2026-11 | 33.4 | 4.8 | -1.0 cm | 101.082 |
| 2026-12 | 33.9 | 1.4 | +3.4 cm | 101.116 |
| 2027-01 | 38.2 | -0.1 | +8.0 cm | 101.196 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 495.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.193 m (+19.3 cm)
- **Poziom na koniec stycznia 2027:** 101.196 m n.p.m.

### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 26.0 | -0.9 | +10.9 cm | 101.112 |
| 2026-03 | 22.3 | 3.3 | +10.4 cm | 101.217 |
| 2026-04 | 15.2 | 8.4 | +10.0 cm | 101.317 |
| 2026-05 | 35.4 | 13.1 | +7.2 cm | 101.389 |
| 2026-06 | 34.1 | 16.5 | -4.4 cm | 101.345 |
| 2026-07 | 54.5 | 19.0 | -6.6 cm | 101.279 |
| 2026-08 | 34.2 | 18.3 | -6.9 cm | 101.21 |
| 2026-09 | 22.4 | 13.7 | -7.0 cm | 101.14 |
| 2026-10 | 22.7 | 8.5 | -4.1 cm | 101.1 |
| 2026-11 | 19.4 | 3.8 | -1.8 cm | 101.082 |
| 2026-12 | 24.8 | -0.2 | +3.3 cm | 101.115 |
| 2027-01 | 27.9 | -2.0 | +8.5 cm | 101.2 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 8.5 °C
- **Suma opadu (prognoza):** 338.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.197 m (+19.7 cm)
- **Poziom na koniec stycznia 2027:** 101.2 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.8 | -0.9 | +11.0 cm | 101.113 |
| 2026-03 | 33.6 | 3.3 | +11.2 cm | 101.225 |
| 2026-04 | 28.6 | 8.4 | +10.9 cm | 101.334 |
| 2026-05 | 47.6 | 13.1 | +7.4 cm | 101.408 |
| 2026-06 | 54.0 | 16.5 | -4.6 cm | 101.362 |
| 2026-07 | 67.5 | 19.0 | -5.8 cm | 101.304 |
| 2026-08 | 57.5 | 18.3 | -5.6 cm | 101.248 |
| 2026-09 | 40.6 | 13.7 | -4.6 cm | 101.202 |
| 2026-10 | 38.8 | 8.5 | -0.8 cm | 101.193 |
| 2026-11 | 38.4 | 3.8 | +1.4 cm | 101.208 |
| 2026-12 | 35.8 | -0.2 | +3.9 cm | 101.247 |
| 2027-01 | 40.0 | -2.0 | +6.0 cm | 101.307 |

- **Szansa realizacji:** 14.3 %
- **Średnia temperatura roczna (prognoza):** 8.5 °C
- **Suma opadu (prognoza):** 517.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.304 m (+30.4 cm)
- **Poziom na koniec stycznia 2027:** 101.307 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 48.8 | -0.9 | +10.7 cm | 101.11 |
| 2026-03 | 49.5 | 3.3 | +11.2 cm | 101.222 |
| 2026-04 | 36.4 | 8.4 | +10.8 cm | 101.33 |
| 2026-05 | 75.4 | 13.1 | +8.4 cm | 101.414 |
| 2026-06 | 71.7 | 16.5 | -4.0 cm | 101.374 |
| 2026-07 | 101.3 | 19.0 | -5.9 cm | 101.315 |
| 2026-08 | 81.8 | 18.3 | -5.4 cm | 101.261 |
| 2026-09 | 55.0 | 13.7 | -1.4 cm | 101.247 |
| 2026-10 | 55.2 | 8.5 | +3.2 cm | 101.28 |
| 2026-11 | 46.9 | 3.8 | +3.5 cm | 101.315 |
| 2026-12 | 46.0 | -0.2 | +4.8 cm | 101.363 |
| 2027-01 | 52.5 | -2.0 | +7.5 cm | 101.438 |

- **Szansa realizacji:** 6.8 %
- **Średnia temperatura roczna (prognoza):** 8.5 °C
- **Suma opadu (prognoza):** 720.6 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.435 m (+43.5 cm)
- **Poziom na koniec stycznia 2027:** 101.438 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 26.0 | 1.0 | +11.2 cm | 101.115 |
| 2026-03 | 22.3 | 4.3 | +10.4 cm | 101.22 |
| 2026-04 | 15.2 | 9.1 | +5.8 cm | 101.278 |
| 2026-05 | 35.4 | 13.8 | +3.8 cm | 101.316 |
| 2026-06 | 34.1 | 18.0 | -4.5 cm | 101.27 |
| 2026-07 | 54.5 | 19.8 | -6.0 cm | 101.211 |
| 2026-08 | 34.2 | 19.3 | -6.3 cm | 101.147 |
| 2026-09 | 22.4 | 14.9 | -6.2 cm | 101.086 |
| 2026-10 | 22.7 | 9.8 | -5.5 cm | 101.031 |
| 2026-11 | 19.4 | 5.0 | -0.5 cm | 101.025 |
| 2026-12 | 24.8 | 1.7 | +4.4 cm | 101.069 |
| 2027-01 | 27.9 | -0.1 | +8.5 cm | 101.154 |

- **Szansa realizacji:** 12.1 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 338.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.151 m (+15.1 cm)
- **Poziom na koniec stycznia 2027:** 101.154 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.8 | 1.0 | +11.3 cm | 101.116 |
| 2026-03 | 33.6 | 4.3 | +11.2 cm | 101.228 |
| 2026-04 | 28.6 | 9.1 | +6.7 cm | 101.295 |
| 2026-05 | 47.6 | 13.8 | +4.0 cm | 101.335 |
| 2026-06 | 54.0 | 18.0 | -4.9 cm | 101.286 |
| 2026-07 | 67.5 | 19.8 | -5.3 cm | 101.232 |
| 2026-08 | 57.5 | 19.3 | -4.5 cm | 101.187 |
| 2026-09 | 40.6 | 14.9 | -5.5 cm | 101.132 |
| 2026-10 | 38.8 | 9.8 | -4.7 cm | 101.085 |
| 2026-11 | 38.4 | 5.0 | -1.3 cm | 101.072 |
| 2026-12 | 35.8 | 1.7 | +4.3 cm | 101.115 |
| 2027-01 | 40.0 | -0.1 | +8.6 cm | 101.201 |

- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 517.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.198 m (+19.8 cm)
- **Poziom na koniec stycznia 2027:** 101.201 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 48.8 | 1.0 | +11.0 cm | 101.113 |
| 2026-03 | 49.5 | 4.3 | +11.2 cm | 101.225 |
| 2026-04 | 36.4 | 9.1 | +6.6 cm | 101.291 |
| 2026-05 | 75.4 | 13.8 | +5.0 cm | 101.34 |
| 2026-06 | 71.7 | 18.0 | -4.0 cm | 101.301 |
| 2026-07 | 101.3 | 19.8 | -5.4 cm | 101.246 |
| 2026-08 | 81.8 | 19.3 | -4.9 cm | 101.197 |
| 2026-09 | 55.0 | 14.9 | -3.4 cm | 101.164 |
| 2026-10 | 55.2 | 9.8 | -0.3 cm | 101.16 |
| 2026-11 | 46.9 | 5.0 | +1.0 cm | 101.171 |
| 2026-12 | 46.0 | 1.7 | +3.8 cm | 101.209 |
| 2027-01 | 52.5 | -0.1 | +8.1 cm | 101.29 |

- **Szansa realizacji:** 6.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 720.6 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.287 m (+28.7 cm)
- **Poziom na koniec stycznia 2027:** 101.29 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 26.0 | 4.0 | +10.5 cm | 101.109 |
| 2026-03 | 22.3 | 5.6 | +9.9 cm | 101.208 |
| 2026-04 | 15.2 | 10.6 | +5.8 cm | 101.266 |
| 2026-05 | 35.4 | 15.1 | +2.6 cm | 101.292 |
| 2026-06 | 34.1 | 19.0 | -4.8 cm | 101.244 |
| 2026-07 | 54.5 | 20.4 | -6.3 cm | 101.181 |
| 2026-08 | 34.2 | 20.0 | -6.6 cm | 101.115 |
| 2026-09 | 22.4 | 16.1 | -8.0 cm | 101.035 |
| 2026-10 | 22.7 | 11.3 | -8.7 cm | 100.949 |
| 2026-11 | 19.4 | 5.8 | -4.2 cm | 100.907 |
| 2026-12 | 24.8 | 2.7 | +0.7 cm | 100.913 |
| 2027-01 | 27.9 | 1.9 | +7.0 cm | 100.984 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 338.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.019 m (-1.9 cm)
- **Poziom na koniec stycznia 2027:** 100.984 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.8 | 4.0 | +10.6 cm | 101.109 |
| 2026-03 | 33.6 | 5.6 | +10.7 cm | 101.216 |
| 2026-04 | 28.6 | 10.6 | +6.8 cm | 101.284 |
| 2026-05 | 47.6 | 15.1 | +2.7 cm | 101.311 |
| 2026-06 | 54.0 | 19.0 | -5.0 cm | 101.262 |
| 2026-07 | 67.5 | 20.4 | -5.5 cm | 101.207 |
| 2026-08 | 57.5 | 20.0 | -4.5 cm | 101.162 |
| 2026-09 | 40.6 | 16.1 | -7.0 cm | 101.092 |
| 2026-10 | 38.8 | 11.3 | -6.1 cm | 101.031 |
| 2026-11 | 38.4 | 5.8 | -3.2 cm | 100.999 |
| 2026-12 | 35.8 | 2.7 | +2.8 cm | 101.027 |
| 2027-01 | 40.0 | 1.9 | +9.0 cm | 101.117 |

- **Szansa realizacji:** 14.4 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 517.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.114 m (+11.4 cm)
- **Poziom na koniec stycznia 2027:** 101.117 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 48.8 | 4.0 | +10.2 cm | 101.105 |
| 2026-03 | 49.5 | 5.6 | +10.6 cm | 101.212 |
| 2026-04 | 36.4 | 10.6 | +6.7 cm | 101.279 |
| 2026-05 | 75.4 | 15.1 | +3.1 cm | 101.31 |
| 2026-06 | 71.7 | 19.0 | -4.4 cm | 101.266 |
| 2026-07 | 101.3 | 20.4 | -5.5 cm | 101.211 |
| 2026-08 | 81.8 | 20.0 | -4.4 cm | 101.167 |
| 2026-09 | 55.0 | 16.1 | -4.5 cm | 101.122 |
| 2026-10 | 55.2 | 11.3 | -1.3 cm | 101.109 |
| 2026-11 | 46.9 | 5.8 | -0.9 cm | 101.099 |
| 2026-12 | 46.0 | 2.7 | +3.4 cm | 101.133 |
| 2027-01 | 52.5 | 1.9 | +9.1 cm | 101.224 |

- **Szansa realizacji:** 6.8 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 720.6 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.221 m (+22.1 cm)
- **Poziom na koniec stycznia 2027:** 101.224 m n.p.m.



*Wygenerowano: 2026-02-15 12:03*