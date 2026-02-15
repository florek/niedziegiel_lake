# Raport: Jezioro Skulska Wieś

Raport ewaluacji na następne 12 miesięcy dla Jezioro Skulska Wieś.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/skulskawies/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Symulacje wariantów pogodowych (12 miesięcy do przodu)

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/skulskawies/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykres: pełny zakres historii (od 1974) + 12 miesięcy symulacji.

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

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów): **86.018 m n.p.m.** W stosunku do stanu na koniec stycznia 2026 (85.758 m n.p.m.): przybędzie +0.260 m (+26.0 cm).


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.0 | 1.2 | +7.0 cm | 85.828 |
| 2026-03 | 33.4 | 4.2 | +8.3 cm | 85.91 |
| 2026-04 | 25.1 | 9.3 | +7.5 cm | 85.986 |
| 2026-05 | 46.0 | 13.9 | +2.8 cm | 86.014 |
| 2026-06 | 50.1 | 17.7 | -3.4 cm | 85.98 |
| 2026-07 | 69.9 | 19.7 | -4.4 cm | 85.936 |
| 2026-08 | 53.6 | 19.2 | -4.1 cm | 85.895 |
| 2026-09 | 40.3 | 14.8 | -2.3 cm | 85.872 |
| 2026-10 | 31.5 | 9.8 | +0.5 cm | 85.878 |
| 2026-11 | 34.6 | 4.7 | +2.7 cm | 85.905 |
| 2026-12 | 34.9 | 1.4 | +5.3 cm | 85.957 |
| 2027-01 | 38.4 | 0.0 | +6.1 cm | 86.018 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 491.7 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.260 m (+26.0 cm)
- **Poziom na koniec stycznia 2027:** 86.018 m n.p.m.

### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | -1.0 | +6.2 cm | 85.82 |
| 2026-03 | 22.8 | 3.0 | +6.9 cm | 85.889 |
| 2026-04 | 15.0 | 8.4 | +7.1 cm | 85.96 |
| 2026-05 | 34.0 | 12.8 | +5.7 cm | 86.017 |
| 2026-06 | 33.6 | 16.5 | -1.4 cm | 86.003 |
| 2026-07 | 53.9 | 18.8 | -4.1 cm | 85.962 |
| 2026-08 | 35.5 | 18.3 | -6.2 cm | 85.901 |
| 2026-09 | 22.7 | 13.7 | -5.5 cm | 85.845 |
| 2026-10 | 17.6 | 8.3 | -2.9 cm | 85.816 |
| 2026-11 | 21.8 | 3.6 | +1.7 cm | 85.833 |
| 2026-12 | 25.6 | -0.2 | +5.4 cm | 85.887 |
| 2027-01 | 28.6 | -1.9 | +5.9 cm | 85.946 |

- **Szansa realizacji:** 11.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.188 m (+18.8 cm)
- **Poziom na koniec stycznia 2027:** 85.946 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | -1.0 | +6.2 cm | 85.82 |
| 2026-03 | 33.9 | 3.0 | +6.8 cm | 85.888 |
| 2026-04 | 27.7 | 8.4 | +7.2 cm | 85.96 |
| 2026-05 | 46.4 | 12.8 | +5.6 cm | 86.015 |
| 2026-06 | 53.1 | 16.5 | -1.8 cm | 85.997 |
| 2026-07 | 66.7 | 18.8 | -4.9 cm | 85.948 |
| 2026-08 | 56.2 | 18.3 | -4.5 cm | 85.904 |
| 2026-09 | 43.3 | 13.7 | -0.7 cm | 85.897 |
| 2026-10 | 33.9 | 8.3 | +2.6 cm | 85.923 |
| 2026-11 | 38.8 | 3.6 | +4.7 cm | 85.97 |
| 2026-12 | 36.7 | -0.2 | +6.2 cm | 86.032 |
| 2027-01 | 39.8 | -1.9 | +4.0 cm | 86.072 |

- **Szansa realizacji:** 14.2 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.314 m (+31.4 cm)
- **Poziom na koniec stycznia 2027:** 86.072 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | -1.0 | +6.2 cm | 85.82 |
| 2026-03 | 49.5 | 3.0 | +6.7 cm | 85.887 |
| 2026-04 | 36.1 | 8.4 | +7.3 cm | 85.96 |
| 2026-05 | 64.7 | 12.8 | +5.3 cm | 86.014 |
| 2026-06 | 70.6 | 16.5 | -1.9 cm | 85.994 |
| 2026-07 | 102.3 | 18.8 | -2.1 cm | 85.974 |
| 2026-08 | 77.4 | 18.3 | -2.8 cm | 85.946 |
| 2026-09 | 62.5 | 13.7 | -1.7 cm | 85.929 |
| 2026-10 | 49.0 | 8.3 | +0.6 cm | 85.934 |
| 2026-11 | 46.6 | 3.6 | +4.6 cm | 85.98 |
| 2026-12 | 46.4 | -0.2 | +6.7 cm | 86.047 |
| 2027-01 | 51.6 | -1.9 | +5.5 cm | 86.102 |

- **Szansa realizacji:** 7.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.344 m (+34.4 cm)
- **Poziom na koniec stycznia 2027:** 86.102 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | 0.8 | +7.9 cm | 85.837 |
| 2026-03 | 22.8 | 4.3 | +9.6 cm | 85.933 |
| 2026-04 | 15.0 | 9.1 | +8.4 cm | 86.017 |
| 2026-05 | 34.0 | 13.7 | +2.7 cm | 86.044 |
| 2026-06 | 33.6 | 17.8 | -3.8 cm | 86.006 |
| 2026-07 | 53.9 | 19.8 | -6.8 cm | 85.937 |
| 2026-08 | 35.5 | 19.3 | -8.9 cm | 85.848 |
| 2026-09 | 22.7 | 14.7 | -8.0 cm | 85.768 |
| 2026-10 | 17.6 | 9.8 | -5.7 cm | 85.711 |
| 2026-11 | 21.8 | 4.8 | -2.7 cm | 85.684 |
| 2026-12 | 25.6 | 1.8 | +3.8 cm | 85.721 |
| 2027-01 | 28.6 | 0.1 | +7.9 cm | 85.801 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.043 m (+4.3 cm)
- **Poziom na koniec stycznia 2027:** 85.801 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | 0.8 | +7.9 cm | 85.837 |
| 2026-03 | 33.9 | 4.3 | +9.5 cm | 85.932 |
| 2026-04 | 27.7 | 9.1 | +8.6 cm | 86.017 |
| 2026-05 | 46.4 | 13.7 | +3.0 cm | 86.047 |
| 2026-06 | 53.1 | 17.8 | -4.2 cm | 86.005 |
| 2026-07 | 66.7 | 19.8 | -6.3 cm | 85.942 |
| 2026-08 | 56.2 | 19.3 | -5.3 cm | 85.889 |
| 2026-09 | 43.3 | 14.7 | -1.8 cm | 85.872 |
| 2026-10 | 33.9 | 9.8 | +3.0 cm | 85.902 |
| 2026-11 | 38.8 | 4.8 | +4.0 cm | 85.942 |
| 2026-12 | 36.7 | 1.8 | +5.9 cm | 86.0 |
| 2027-01 | 39.8 | 0.1 | +6.8 cm | 86.068 |

- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.310 m (+31.0 cm)
- **Poziom na koniec stycznia 2027:** 86.068 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | 0.8 | +7.8 cm | 85.836 |
| 2026-03 | 49.5 | 4.3 | +9.2 cm | 85.928 |
| 2026-04 | 36.1 | 9.1 | +8.7 cm | 86.015 |
| 2026-05 | 64.7 | 13.7 | +2.8 cm | 86.043 |
| 2026-06 | 70.6 | 17.8 | -4.3 cm | 86.0 |
| 2026-07 | 102.3 | 19.8 | -3.8 cm | 85.962 |
| 2026-08 | 77.4 | 19.3 | -3.3 cm | 85.929 |
| 2026-09 | 62.5 | 14.7 | -1.5 cm | 85.914 |
| 2026-10 | 49.0 | 9.8 | +2.1 cm | 85.936 |
| 2026-11 | 46.6 | 4.8 | +4.7 cm | 85.983 |
| 2026-12 | 46.4 | 1.8 | +6.0 cm | 86.043 |
| 2027-01 | 51.6 | 0.1 | +5.6 cm | 86.099 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.341 m (+34.1 cm)
- **Poziom na koniec stycznia 2027:** 86.099 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | 3.8 | +6.9 cm | 85.827 |
| 2026-03 | 22.8 | 5.4 | +8.6 cm | 85.913 |
| 2026-04 | 15.0 | 10.4 | +6.8 cm | 85.981 |
| 2026-05 | 34.0 | 15.1 | +0.3 cm | 85.984 |
| 2026-06 | 33.6 | 18.9 | -4.2 cm | 85.942 |
| 2026-07 | 53.9 | 20.4 | -3.5 cm | 85.906 |
| 2026-08 | 35.5 | 20.0 | -3.4 cm | 85.873 |
| 2026-09 | 22.7 | 16.0 | -1.7 cm | 85.856 |
| 2026-10 | 17.6 | 11.2 | +2.1 cm | 85.877 |
| 2026-11 | 21.8 | 5.7 | +3.3 cm | 85.91 |
| 2026-12 | 25.6 | 2.6 | +4.9 cm | 85.959 |
| 2027-01 | 28.6 | 1.9 | +6.3 cm | 86.022 |

- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.264 m (+26.4 cm)
- **Poziom na koniec stycznia 2027:** 86.022 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | 3.8 | +6.8 cm | 85.826 |
| 2026-03 | 33.9 | 5.4 | +8.5 cm | 85.911 |
| 2026-04 | 27.7 | 10.4 | +7.0 cm | 85.981 |
| 2026-05 | 46.4 | 15.1 | -0.1 cm | 85.98 |
| 2026-06 | 53.1 | 18.9 | -4.5 cm | 85.936 |
| 2026-07 | 66.7 | 20.4 | -3.8 cm | 85.898 |
| 2026-08 | 56.2 | 20.0 | -1.6 cm | 85.882 |
| 2026-09 | 43.3 | 16.0 | +0.4 cm | 85.886 |
| 2026-10 | 33.9 | 11.2 | +1.9 cm | 85.904 |
| 2026-11 | 38.8 | 5.7 | +3.0 cm | 85.934 |
| 2026-12 | 36.7 | 2.6 | +4.8 cm | 85.982 |
| 2027-01 | 39.8 | 1.9 | +6.0 cm | 86.041 |

- **Szansa realizacji:** 14.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.283 m (+28.3 cm)
- **Poziom na koniec stycznia 2027:** 86.041 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | 3.8 | +6.7 cm | 85.825 |
| 2026-03 | 49.5 | 5.4 | +8.4 cm | 85.909 |
| 2026-04 | 36.1 | 10.4 | +6.8 cm | 85.977 |
| 2026-05 | 64.7 | 15.1 | -0.2 cm | 85.975 |
| 2026-06 | 70.6 | 18.9 | -4.6 cm | 85.929 |
| 2026-07 | 102.3 | 20.4 | -1.0 cm | 85.919 |
| 2026-08 | 77.4 | 20.0 | +2.2 cm | 85.942 |
| 2026-09 | 62.5 | 16.0 | +0.1 cm | 85.943 |
| 2026-10 | 49.0 | 11.2 | -0.0 cm | 85.943 |
| 2026-11 | 46.6 | 5.7 | +0.7 cm | 85.95 |
| 2026-12 | 46.4 | 2.6 | +4.1 cm | 85.991 |
| 2027-01 | 51.6 | 1.9 | +7.3 cm | 86.064 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.306 m (+30.6 cm)
- **Poziom na koniec stycznia 2027:** 86.064 m n.p.m.



*Wygenerowano: 2026-02-15 14:10*