# Raport: Jezioro Suszewskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Suszewskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/suszewskie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Symulacje wariantów pogodowych (12 miesięcy do przodu)

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/suszewskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykres: pełny zakres historii (od 1974) + 12 miesięcy symulacji.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa realizacji (%) |
|---------|------------------------|
| zimny, suchy | 11.5 |
| zimny, normalny | 14.1 |
| zimny, wilgotny | 7.1 |
| normalny, suchy | 11.9 |
| normalny, normalny | 15.0 |
| normalny, wilgotny | 7.3 |
| ciepły, suchy | 11.6 |
| ciepły, normalny | 14.3 |
| ciepły, wilgotny | 7.2 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów): **94.168 m n.p.m.** W stosunku do stanu na koniec stycznia 2026 (93.7383 m n.p.m.): przybędzie +0.430 m (+43.0 cm).


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.3 | 1.3 | +6.5 cm | 93.803 |
| 2026-03 | 34.2 | 4.4 | +17.0 cm | 93.973 |
| 2026-04 | 25.7 | 9.3 | +16.6 cm | 94.139 |
| 2026-05 | 47.7 | 13.8 | +16.6 cm | 94.305 |
| 2026-06 | 50.3 | 17.8 | +8.9 cm | 94.394 |
| 2026-07 | 68.4 | 19.9 | +1.3 cm | 94.407 |
| 2026-08 | 54.3 | 19.2 | -6.9 cm | 94.338 |
| 2026-09 | 38.8 | 14.9 | -9.4 cm | 94.244 |
| 2026-10 | 33.6 | 9.8 | -8.1 cm | 94.163 |
| 2026-11 | 34.2 | 4.7 | -4.8 cm | 94.116 |
| 2026-12 | 35.3 | 1.4 | -0.0 cm | 94.115 |
| 2027-01 | 38.3 | -0.1 | +5.3 cm | 94.168 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 495.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.430 m (+43.0 cm)
- **Poziom na koniec stycznia 2027:** 94.168 m n.p.m.

### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | -1.1 | +5.1 cm | 93.789 |
| 2026-03 | 22.6 | 3.2 | +14.2 cm | 93.932 |
| 2026-04 | 15.6 | 8.3 | +15.4 cm | 94.086 |
| 2026-05 | 34.9 | 12.8 | +15.4 cm | 94.24 |
| 2026-06 | 33.1 | 16.5 | +7.9 cm | 94.32 |
| 2026-07 | 53.0 | 19.3 | +3.3 cm | 94.353 |
| 2026-08 | 35.1 | 18.4 | -7.1 cm | 94.282 |
| 2026-09 | 22.6 | 13.7 | -11.8 cm | 94.164 |
| 2026-10 | 20.1 | 8.4 | -11.3 cm | 94.051 |
| 2026-11 | 21.2 | 3.5 | -7.5 cm | 93.976 |
| 2026-12 | 25.4 | -0.2 | -4.7 cm | 93.928 |
| 2027-01 | 28.2 | -2.0 | -3.5 cm | 93.894 |

- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 337.6 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.156 m (+15.6 cm)
- **Poziom na koniec stycznia 2027:** 93.894 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.8 | -1.1 | +5.3 cm | 93.791 |
| 2026-03 | 35.8 | 3.2 | +14.2 cm | 93.934 |
| 2026-04 | 28.6 | 8.3 | +15.4 cm | 94.087 |
| 2026-05 | 47.6 | 12.8 | +15.1 cm | 94.238 |
| 2026-06 | 54.0 | 16.5 | +6.9 cm | 94.308 |
| 2026-07 | 66.1 | 19.3 | -1.4 cm | 94.293 |
| 2026-08 | 57.5 | 18.4 | -9.4 cm | 94.2 |
| 2026-09 | 42.1 | 13.7 | -10.4 cm | 94.096 |
| 2026-10 | 35.9 | 8.4 | -10.6 cm | 93.99 |
| 2026-11 | 38.4 | 3.5 | -6.0 cm | 93.93 |
| 2026-12 | 37.6 | -0.2 | -3.9 cm | 93.89 |
| 2027-01 | 39.5 | -2.0 | +1.7 cm | 93.908 |

- **Szansa realizacji:** 14.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 517.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.170 m (+17.0 cm)
- **Poziom na koniec stycznia 2027:** 93.908 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 47.2 | -1.1 | +5.1 cm | 93.79 |
| 2026-03 | 49.9 | 3.2 | +18.4 cm | 93.974 |
| 2026-04 | 36.2 | 8.3 | +18.1 cm | 94.155 |
| 2026-05 | 68.5 | 12.8 | +25.5 cm | 94.41 |
| 2026-06 | 71.0 | 16.5 | +22.7 cm | 94.637 |
| 2026-07 | 97.8 | 19.3 | +12.4 cm | 94.761 |
| 2026-08 | 78.9 | 18.4 | +4.9 cm | 94.81 |
| 2026-09 | 58.4 | 13.7 | +8.7 cm | 94.898 |
| 2026-10 | 51.1 | 8.4 | +22.2 cm | 95.119 |
| 2026-11 | 46.8 | 3.5 | +28.2 cm | 95.401 |
| 2026-12 | 46.7 | -0.2 | +38.8 cm | 95.789 |
| 2027-01 | 52.4 | -2.0 | +42.4 cm | 96.213 |

- **Szansa realizacji:** 7.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 704.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +2.475 m (+247.5 cm)
- **Poziom na koniec stycznia 2027:** 96.213 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | 1.0 | +7.6 cm | 93.814 |
| 2026-03 | 22.6 | 4.3 | +19.3 cm | 94.007 |
| 2026-04 | 15.6 | 9.1 | +18.1 cm | 94.188 |
| 2026-05 | 34.9 | 13.6 | +19.2 cm | 94.38 |
| 2026-06 | 33.1 | 17.9 | +7.7 cm | 94.457 |
| 2026-07 | 53.0 | 19.8 | +3.8 cm | 94.495 |
| 2026-08 | 35.1 | 19.3 | -6.8 cm | 94.427 |
| 2026-09 | 22.6 | 14.8 | -11.7 cm | 94.31 |
| 2026-10 | 20.1 | 9.8 | -11.0 cm | 94.199 |
| 2026-11 | 21.2 | 4.9 | -7.5 cm | 94.124 |
| 2026-12 | 25.4 | 1.8 | -3.4 cm | 94.091 |
| 2027-01 | 28.2 | -0.1 | +1.3 cm | 94.104 |

- **Szansa realizacji:** 11.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 337.6 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.366 m (+36.6 cm)
- **Poziom na koniec stycznia 2027:** 94.104 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.8 | 1.0 | +8.3 cm | 93.821 |
| 2026-03 | 35.8 | 4.3 | +19.1 cm | 94.012 |
| 2026-04 | 28.6 | 9.1 | +18.0 cm | 94.192 |
| 2026-05 | 47.6 | 13.6 | +18.3 cm | 94.375 |
| 2026-06 | 54.0 | 17.9 | +7.2 cm | 94.447 |
| 2026-07 | 66.1 | 19.8 | -1.1 cm | 94.436 |
| 2026-08 | 57.5 | 19.3 | -9.2 cm | 94.344 |
| 2026-09 | 42.1 | 14.8 | -10.4 cm | 94.241 |
| 2026-10 | 35.9 | 9.8 | -10.4 cm | 94.137 |
| 2026-11 | 38.4 | 4.9 | -5.7 cm | 94.08 |
| 2026-12 | 37.6 | 1.8 | -2.4 cm | 94.056 |
| 2027-01 | 39.5 | -0.1 | +5.5 cm | 94.111 |

- **Szansa realizacji:** 15.0 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 517.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.373 m (+37.3 cm)
- **Poziom na koniec stycznia 2027:** 94.111 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 47.2 | 1.0 | +8.8 cm | 93.826 |
| 2026-03 | 49.9 | 4.3 | +23.4 cm | 94.06 |
| 2026-04 | 36.2 | 9.1 | +20.8 cm | 94.269 |
| 2026-05 | 68.5 | 13.6 | +27.6 cm | 94.545 |
| 2026-06 | 71.0 | 17.9 | +19.5 cm | 94.74 |
| 2026-07 | 97.8 | 19.8 | +6.6 cm | 94.805 |
| 2026-08 | 78.9 | 19.3 | -3.3 cm | 94.772 |
| 2026-09 | 58.4 | 14.8 | -5.8 cm | 94.715 |
| 2026-10 | 51.1 | 9.8 | -8.0 cm | 94.635 |
| 2026-11 | 46.8 | 4.9 | -2.6 cm | 94.609 |
| 2026-12 | 46.7 | 1.8 | +1.8 cm | 94.627 |
| 2027-01 | 52.4 | -0.1 | +9.0 cm | 94.717 |

- **Szansa realizacji:** 7.3 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 704.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.979 m (+97.9 cm)
- **Poziom na koniec stycznia 2027:** 94.717 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | 3.8 | +5.5 cm | 93.793 |
| 2026-03 | 22.6 | 5.5 | +14.3 cm | 93.936 |
| 2026-04 | 15.6 | 10.5 | +14.6 cm | 94.082 |
| 2026-05 | 34.9 | 15.0 | +10.7 cm | 94.189 |
| 2026-06 | 33.1 | 18.9 | +6.6 cm | 94.255 |
| 2026-07 | 53.0 | 20.4 | -3.1 cm | 94.223 |
| 2026-08 | 35.1 | 20.0 | -9.4 cm | 94.129 |
| 2026-09 | 22.6 | 16.1 | -13.0 cm | 93.999 |
| 2026-10 | 20.1 | 11.2 | -11.0 cm | 93.889 |
| 2026-11 | 21.2 | 5.7 | -10.4 cm | 93.785 |
| 2026-12 | 25.4 | 2.6 | -4.2 cm | 93.743 |
| 2027-01 | 28.2 | 1.9 | +0.8 cm | 93.75 |

- **Szansa realizacji:** 11.6 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 337.6 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.012 m (+1.2 cm)
- **Poziom na koniec stycznia 2027:** 93.75 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.8 | 3.8 | +6.2 cm | 93.801 |
| 2026-03 | 35.8 | 5.5 | +14.5 cm | 93.945 |
| 2026-04 | 28.6 | 10.5 | +14.2 cm | 94.087 |
| 2026-05 | 47.6 | 15.0 | +9.0 cm | 94.177 |
| 2026-06 | 54.0 | 18.9 | +4.7 cm | 94.224 |
| 2026-07 | 66.1 | 20.4 | -3.4 cm | 94.19 |
| 2026-08 | 57.5 | 20.0 | -8.8 cm | 94.102 |
| 2026-09 | 42.1 | 16.1 | -11.1 cm | 93.991 |
| 2026-10 | 35.9 | 11.2 | -10.0 cm | 93.891 |
| 2026-11 | 38.4 | 5.7 | -9.2 cm | 93.799 |
| 2026-12 | 37.6 | 2.6 | -3.0 cm | 93.768 |
| 2027-01 | 39.5 | 1.9 | +3.1 cm | 93.799 |

- **Szansa realizacji:** 14.3 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 517.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.061 m (+6.1 cm)
- **Poziom na koniec stycznia 2027:** 93.799 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 47.2 | 3.8 | +6.8 cm | 93.806 |
| 2026-03 | 49.9 | 5.5 | +19.8 cm | 94.005 |
| 2026-04 | 36.2 | 10.5 | +17.8 cm | 94.182 |
| 2026-05 | 68.5 | 15.0 | +18.1 cm | 94.364 |
| 2026-06 | 71.0 | 18.9 | +8.0 cm | 94.444 |
| 2026-07 | 97.8 | 20.4 | +4.5 cm | 94.489 |
| 2026-08 | 78.9 | 20.0 | -4.5 cm | 94.444 |
| 2026-09 | 58.4 | 16.1 | -10.8 cm | 94.335 |
| 2026-10 | 51.1 | 11.2 | -9.4 cm | 94.241 |
| 2026-11 | 46.8 | 5.7 | -7.9 cm | 94.162 |
| 2026-12 | 46.7 | 2.6 | -2.2 cm | 94.14 |
| 2027-01 | 52.4 | 1.9 | +3.7 cm | 94.177 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 704.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.439 m (+43.9 cm)
- **Poziom na koniec stycznia 2027:** 94.177 m n.p.m.



*Wygenerowano: 2026-02-15 13:45*