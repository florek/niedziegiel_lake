# Raport: Jezioro Wilczyńskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Wilczyńskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/wilczynskie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Symulacje wariantów pogodowych (12 miesięcy do przodu)

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/wilczynskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykres: pełny zakres historii (od 1974) + 12 miesięcy symulacji.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa realizacji (%) |
|---------|------------------------|
| zimny, suchy | 11.3 |
| zimny, normalny | 14.2 |
| zimny, wilgotny | 7.1 |
| normalny, suchy | 11.7 |
| normalny, normalny | 15.2 |
| normalny, wilgotny | 7.2 |
| ciepły, suchy | 11.5 |
| ciepły, normalny | 14.5 |
| ciepły, wilgotny | 7.2 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów): **93.893 m n.p.m.** W stosunku do stanu na koniec stycznia 2026 (94.0036 m n.p.m.): ubędzie 0.111 m (-11.1 cm).


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.0 | 1.2 | +9.7 cm | 94.101 |
| 2026-03 | 33.4 | 4.2 | +6.9 cm | 94.169 |
| 2026-04 | 25.1 | 9.3 | +6.1 cm | 94.23 |
| 2026-05 | 46.0 | 13.9 | +3.2 cm | 94.262 |
| 2026-06 | 50.1 | 17.7 | -1.7 cm | 94.246 |
| 2026-07 | 69.9 | 19.7 | -5.8 cm | 94.188 |
| 2026-08 | 53.6 | 19.2 | -7.0 cm | 94.119 |
| 2026-09 | 40.3 | 14.8 | -8.0 cm | 94.039 |
| 2026-10 | 31.5 | 9.8 | -6.8 cm | 93.971 |
| 2026-11 | 34.6 | 4.7 | -5.1 cm | 93.92 |
| 2026-12 | 34.9 | 1.4 | -2.8 cm | 93.892 |
| 2027-01 | 38.4 | 0.0 | +0.1 cm | 93.893 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 491.7 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.111 m (-11.1 cm)
- **Poziom na koniec stycznia 2027:** 93.893 m n.p.m.

### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | -1.0 | +9.1 cm | 94.095 |
| 2026-03 | 22.8 | 3.0 | +7.3 cm | 94.168 |
| 2026-04 | 15.0 | 8.4 | +7.1 cm | 94.239 |
| 2026-05 | 34.0 | 12.8 | +5.6 cm | 94.295 |
| 2026-06 | 33.6 | 16.5 | +1.5 cm | 94.31 |
| 2026-07 | 53.9 | 18.8 | -7.7 cm | 94.233 |
| 2026-08 | 35.5 | 18.3 | -8.7 cm | 94.146 |
| 2026-09 | 22.7 | 13.7 | -10.4 cm | 94.042 |
| 2026-10 | 17.6 | 8.3 | -8.8 cm | 93.955 |
| 2026-11 | 21.8 | 3.6 | -7.0 cm | 93.885 |
| 2026-12 | 25.6 | -0.2 | -5.0 cm | 93.835 |
| 2027-01 | 28.6 | -1.9 | -2.6 cm | 93.809 |

- **Szansa realizacji:** 11.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.195 m (-19.5 cm)
- **Poziom na koniec stycznia 2027:** 93.809 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | -1.0 | +9.1 cm | 94.095 |
| 2026-03 | 33.9 | 3.0 | +7.4 cm | 94.169 |
| 2026-04 | 27.7 | 8.4 | +7.9 cm | 94.248 |
| 2026-05 | 46.4 | 12.8 | +6.7 cm | 94.314 |
| 2026-06 | 53.1 | 16.5 | +4.1 cm | 94.355 |
| 2026-07 | 66.7 | 18.8 | -4.1 cm | 94.314 |
| 2026-08 | 56.2 | 18.3 | -5.5 cm | 94.259 |
| 2026-09 | 43.3 | 13.7 | -7.1 cm | 94.188 |
| 2026-10 | 33.9 | 8.3 | -5.8 cm | 94.13 |
| 2026-11 | 38.8 | 3.6 | -4.2 cm | 94.088 |
| 2026-12 | 36.7 | -0.2 | -1.2 cm | 94.076 |
| 2027-01 | 39.8 | -1.9 | +0.8 cm | 94.084 |

- **Szansa realizacji:** 14.2 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.080 m (+8.0 cm)
- **Poziom na koniec stycznia 2027:** 94.084 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | -1.0 | +10.7 cm | 94.11 |
| 2026-03 | 49.5 | 3.0 | +10.0 cm | 94.211 |
| 2026-04 | 36.1 | 8.4 | +10.4 cm | 94.315 |
| 2026-05 | 64.7 | 12.8 | +7.5 cm | 94.39 |
| 2026-06 | 70.6 | 16.5 | +9.1 cm | 94.481 |
| 2026-07 | 102.3 | 18.8 | +2.3 cm | 94.503 |
| 2026-08 | 77.4 | 18.3 | -1.7 cm | 94.486 |
| 2026-09 | 62.5 | 13.7 | -2.9 cm | 94.457 |
| 2026-10 | 49.0 | 8.3 | -2.6 cm | 94.431 |
| 2026-11 | 46.6 | 3.6 | -0.4 cm | 94.428 |
| 2026-12 | 46.4 | -0.2 | +2.9 cm | 94.457 |
| 2027-01 | 51.6 | -1.9 | +7.0 cm | 94.528 |

- **Szansa realizacji:** 7.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.524 m (+52.4 cm)
- **Poziom na koniec stycznia 2027:** 94.528 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | 0.8 | +9.7 cm | 94.1 |
| 2026-03 | 22.8 | 4.3 | +6.3 cm | 94.163 |
| 2026-04 | 15.0 | 9.1 | +5.2 cm | 94.215 |
| 2026-05 | 34.0 | 13.7 | -0.3 cm | 94.212 |
| 2026-06 | 33.6 | 17.8 | -5.9 cm | 94.153 |
| 2026-07 | 53.9 | 19.8 | -8.1 cm | 94.073 |
| 2026-08 | 35.5 | 19.3 | -9.1 cm | 93.981 |
| 2026-09 | 22.7 | 14.7 | -10.8 cm | 93.873 |
| 2026-10 | 17.6 | 9.8 | -10.1 cm | 93.773 |
| 2026-11 | 21.8 | 4.8 | -8.3 cm | 93.69 |
| 2026-12 | 25.6 | 1.8 | -5.8 cm | 93.632 |
| 2027-01 | 28.6 | 0.1 | -2.8 cm | 93.605 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.399 m (-39.9 cm)
- **Poziom na koniec stycznia 2027:** 93.605 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | 0.8 | +9.7 cm | 94.101 |
| 2026-03 | 33.9 | 4.3 | +6.2 cm | 94.163 |
| 2026-04 | 27.7 | 9.1 | +6.1 cm | 94.224 |
| 2026-05 | 46.4 | 13.7 | +5.1 cm | 94.275 |
| 2026-06 | 53.1 | 17.8 | -4.9 cm | 94.226 |
| 2026-07 | 66.7 | 19.8 | -7.5 cm | 94.151 |
| 2026-08 | 56.2 | 19.3 | -7.8 cm | 94.072 |
| 2026-09 | 43.3 | 14.7 | -8.3 cm | 93.989 |
| 2026-10 | 33.9 | 9.8 | -6.9 cm | 93.92 |
| 2026-11 | 38.8 | 4.8 | -4.8 cm | 93.872 |
| 2026-12 | 36.7 | 1.8 | -2.8 cm | 93.844 |
| 2027-01 | 39.8 | 0.1 | -0.1 cm | 93.843 |

- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.161 m (-16.1 cm)
- **Poziom na koniec stycznia 2027:** 93.843 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | 0.8 | +11.3 cm | 94.116 |
| 2026-03 | 49.5 | 4.3 | +8.8 cm | 94.205 |
| 2026-04 | 36.1 | 9.1 | +9.2 cm | 94.297 |
| 2026-05 | 64.7 | 13.7 | +7.4 cm | 94.371 |
| 2026-06 | 70.6 | 17.8 | +4.4 cm | 94.414 |
| 2026-07 | 102.3 | 19.8 | -1.1 cm | 94.403 |
| 2026-08 | 77.4 | 19.3 | -3.5 cm | 94.368 |
| 2026-09 | 62.5 | 14.7 | -4.0 cm | 94.328 |
| 2026-10 | 49.0 | 9.8 | -4.3 cm | 94.285 |
| 2026-11 | 46.6 | 4.8 | -2.8 cm | 94.257 |
| 2026-12 | 46.4 | 1.8 | -0.3 cm | 94.255 |
| 2027-01 | 51.6 | 0.1 | +2.9 cm | 94.283 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.279 m (+27.9 cm)
- **Poziom na koniec stycznia 2027:** 94.283 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | 3.8 | +9.3 cm | 94.096 |
| 2026-03 | 22.8 | 5.4 | +5.3 cm | 94.15 |
| 2026-04 | 15.0 | 10.4 | +1.8 cm | 94.167 |
| 2026-05 | 34.0 | 15.1 | -3.3 cm | 94.134 |
| 2026-06 | 33.6 | 18.9 | -8.1 cm | 94.054 |
| 2026-07 | 53.9 | 20.4 | -8.8 cm | 93.966 |
| 2026-08 | 35.5 | 20.0 | -9.8 cm | 93.868 |
| 2026-09 | 22.7 | 16.0 | -11.4 cm | 93.754 |
| 2026-10 | 17.6 | 11.2 | -9.5 cm | 93.659 |
| 2026-11 | 21.8 | 5.7 | -7.6 cm | 93.583 |
| 2026-12 | 25.6 | 2.6 | -5.8 cm | 93.525 |
| 2027-01 | 28.6 | 1.9 | -2.9 cm | 93.496 |

- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.508 m (-50.8 cm)
- **Poziom na koniec stycznia 2027:** 93.496 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | 3.8 | +9.3 cm | 94.097 |
| 2026-03 | 33.9 | 5.4 | +5.4 cm | 94.15 |
| 2026-04 | 27.7 | 10.4 | +3.0 cm | 94.181 |
| 2026-05 | 46.4 | 15.1 | -1.9 cm | 94.162 |
| 2026-06 | 53.1 | 18.9 | -7.3 cm | 94.089 |
| 2026-07 | 66.7 | 20.4 | -7.9 cm | 94.01 |
| 2026-08 | 56.2 | 20.0 | -8.1 cm | 93.93 |
| 2026-09 | 43.3 | 16.0 | -7.8 cm | 93.852 |
| 2026-10 | 33.9 | 11.2 | -6.5 cm | 93.787 |
| 2026-11 | 38.8 | 5.7 | -4.7 cm | 93.741 |
| 2026-12 | 36.7 | 2.6 | -3.0 cm | 93.711 |
| 2027-01 | 39.8 | 1.9 | +0.0 cm | 93.711 |

- **Szansa realizacji:** 14.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.293 m (-29.3 cm)
- **Poziom na koniec stycznia 2027:** 93.711 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | 3.8 | +10.8 cm | 94.112 |
| 2026-03 | 49.5 | 5.4 | +7.9 cm | 94.191 |
| 2026-04 | 36.1 | 10.4 | +8.7 cm | 94.278 |
| 2026-05 | 64.7 | 15.1 | +6.5 cm | 94.343 |
| 2026-06 | 70.6 | 18.9 | +0.8 cm | 94.351 |
| 2026-07 | 102.3 | 20.4 | -2.0 cm | 94.331 |
| 2026-08 | 77.4 | 20.0 | -3.7 cm | 94.294 |
| 2026-09 | 62.5 | 16.0 | -4.4 cm | 94.25 |
| 2026-10 | 49.0 | 11.2 | -3.9 cm | 94.212 |
| 2026-11 | 46.6 | 5.7 | -3.0 cm | 94.182 |
| 2026-12 | 46.4 | 2.6 | -0.6 cm | 94.176 |
| 2027-01 | 51.6 | 1.9 | +3.0 cm | 94.206 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.202 m (+20.2 cm)
- **Poziom na koniec stycznia 2027:** 94.206 m n.p.m.



*Wygenerowano: 2026-02-15 15:00*