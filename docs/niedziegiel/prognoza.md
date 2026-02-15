# Raport: Jezioro Niedzięgiel

Raport ewaluacji na następne 12 miesięcy dla Jezioro Niedzięgiel.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/niedziegiel/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Symulacje wariantów pogodowych (12 miesięcy do przodu)

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/niedziegiel/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykres: pełny zakres historii (od 1974) + 12 miesięcy symulacji.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa realizacji (%) |
|---------|------------------------|
| zimny, suchy | 10.2 |
| zimny, normalny | 13.8 |
| zimny, wilgotny | 7.3 |
| normalny, suchy | 10.8 |
| normalny, normalny | 16.0 |
| normalny, wilgotny | 7.6 |
| ciepły, suchy | 10.8 |
| ciepły, normalny | 15.8 |
| ciepły, wilgotny | 7.6 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów): **101.959 m n.p.m.** W stosunku do stanu na koniec stycznia 2026 (101.89 m n.p.m.): przybędzie +0.069 m (+6.9 cm).


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 28.8 | 0.4 | +3.6 cm | 101.926 |
| 2026-03 | 31.8 | 3.8 | +2.8 cm | 101.954 |
| 2026-04 | 25.9 | 8.6 | +0.7 cm | 101.961 |
| 2026-05 | 42.5 | 13.7 | -1.7 cm | 101.943 |
| 2026-06 | 53.1 | 17.2 | -2.7 cm | 101.916 |
| 2026-07 | 67.2 | 19.0 | -3.1 cm | 101.885 |
| 2026-08 | 53.1 | 18.5 | -3.2 cm | 101.853 |
| 2026-09 | 40.2 | 14.1 | -2.2 cm | 101.831 |
| 2026-10 | 29.0 | 9.3 | -0.7 cm | 101.824 |
| 2026-11 | 35.0 | 4.3 | +2.5 cm | 101.849 |
| 2026-12 | 36.9 | 1.0 | +4.8 cm | 101.897 |
| 2027-01 | 34.5 | -0.2 | +6.2 cm | 101.959 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 478.0 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.069 m (+6.9 cm)
- **Poziom na koniec stycznia 2027:** 101.959 m n.p.m.

### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | -2.1 | +3.5 cm | 101.925 |
| 2026-03 | 22.0 | 2.0 | +2.5 cm | 101.949 |
| 2026-04 | 15.9 | 7.7 | +1.4 cm | 101.963 |
| 2026-05 | 30.2 | 12.6 | -0.5 cm | 101.958 |
| 2026-06 | 36.6 | 16.0 | -2.2 cm | 101.936 |
| 2026-07 | 47.1 | 17.4 | -2.5 cm | 101.911 |
| 2026-08 | 37.2 | 17.4 | -2.8 cm | 101.883 |
| 2026-09 | 22.9 | 12.9 | -3.3 cm | 101.85 |
| 2026-10 | 18.0 | 8.1 | -1.5 cm | 101.835 |
| 2026-11 | 23.5 | 2.9 | +1.0 cm | 101.845 |
| 2026-12 | 26.2 | -0.4 | +3.6 cm | 101.881 |
| 2027-01 | 23.3 | -2.2 | +4.6 cm | 101.927 |

- **Szansa realizacji:** 10.2 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.037 m (+3.7 cm)
- **Poziom na koniec stycznia 2027:** 101.927 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | -2.1 | +3.6 cm | 101.927 |
| 2026-03 | 30.8 | 2.0 | +3.2 cm | 101.958 |
| 2026-04 | 28.2 | 7.7 | +2.1 cm | 101.979 |
| 2026-05 | 42.4 | 12.6 | -0.4 cm | 101.975 |
| 2026-06 | 55.5 | 16.0 | -1.0 cm | 101.965 |
| 2026-07 | 65.5 | 17.4 | -0.8 cm | 101.957 |
| 2026-08 | 52.7 | 17.4 | -0.8 cm | 101.949 |
| 2026-09 | 40.6 | 12.9 | -0.5 cm | 101.944 |
| 2026-10 | 29.0 | 8.1 | +0.3 cm | 101.947 |
| 2026-11 | 37.2 | 2.9 | +3.2 cm | 101.979 |
| 2026-12 | 39.2 | -0.4 | +5.1 cm | 102.029 |
| 2027-01 | 35.5 | -2.2 | +6.2 cm | 102.091 |

- **Szansa realizacji:** 13.8 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.201 m (+20.1 cm)
- **Poziom na koniec stycznia 2027:** 102.091 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | -2.1 | +3.8 cm | 101.928 |
| 2026-03 | 47.6 | 2.0 | +3.1 cm | 101.959 |
| 2026-04 | 35.4 | 7.7 | +1.8 cm | 101.977 |
| 2026-05 | 60.2 | 12.6 | -0.4 cm | 101.973 |
| 2026-06 | 71.7 | 16.0 | -1.1 cm | 101.963 |
| 2026-07 | 99.5 | 17.4 | -0.8 cm | 101.955 |
| 2026-08 | 76.7 | 17.4 | +0.0 cm | 101.955 |
| 2026-09 | 64.1 | 12.9 | +0.9 cm | 101.964 |
| 2026-10 | 44.6 | 8.1 | +0.6 cm | 101.971 |
| 2026-11 | 47.0 | 2.9 | +3.6 cm | 102.007 |
| 2026-12 | 47.8 | -0.4 | +6.7 cm | 102.074 |
| 2027-01 | 48.5 | -2.2 | +9.3 cm | 102.167 |

- **Szansa realizacji:** 7.3 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.277 m (+27.7 cm)
- **Poziom na koniec stycznia 2027:** 102.167 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | -0.1 | +3.5 cm | 101.925 |
| 2026-03 | 22.0 | 4.2 | +2.3 cm | 101.948 |
| 2026-04 | 15.9 | 8.7 | +0.2 cm | 101.95 |
| 2026-05 | 30.2 | 13.8 | -1.7 cm | 101.934 |
| 2026-06 | 36.6 | 16.8 | -3.0 cm | 101.904 |
| 2026-07 | 47.1 | 19.5 | -4.5 cm | 101.859 |
| 2026-08 | 37.2 | 18.5 | -6.0 cm | 101.799 |
| 2026-09 | 22.9 | 13.9 | -4.6 cm | 101.753 |
| 2026-10 | 18.0 | 9.1 | -2.4 cm | 101.729 |
| 2026-11 | 23.5 | 4.5 | +1.6 cm | 101.745 |
| 2026-12 | 26.2 | 1.2 | +3.8 cm | 101.783 |
| 2027-01 | 23.3 | -0.2 | +4.5 cm | 101.828 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.062 m (-6.2 cm)
- **Poziom na koniec stycznia 2027:** 101.828 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | -0.1 | +3.6 cm | 101.927 |
| 2026-03 | 30.8 | 4.2 | +3.0 cm | 101.957 |
| 2026-04 | 28.2 | 8.7 | +0.4 cm | 101.961 |
| 2026-05 | 42.4 | 13.8 | -2.6 cm | 101.934 |
| 2026-06 | 55.5 | 16.8 | -3.7 cm | 101.898 |
| 2026-07 | 65.5 | 19.5 | -4.4 cm | 101.854 |
| 2026-08 | 52.7 | 18.5 | -3.9 cm | 101.815 |
| 2026-09 | 40.6 | 13.9 | -3.0 cm | 101.785 |
| 2026-10 | 29.0 | 9.1 | -1.1 cm | 101.773 |
| 2026-11 | 37.2 | 4.5 | +2.7 cm | 101.801 |
| 2026-12 | 39.2 | 1.2 | +4.9 cm | 101.85 |
| 2027-01 | 35.5 | -0.2 | +6.2 cm | 101.911 |

- **Szansa realizacji:** 16.0 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.021 m (+2.1 cm)
- **Poziom na koniec stycznia 2027:** 101.911 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | -0.1 | +3.8 cm | 101.928 |
| 2026-03 | 47.6 | 4.2 | +2.9 cm | 101.957 |
| 2026-04 | 35.4 | 8.7 | -0.0 cm | 101.957 |
| 2026-05 | 60.2 | 13.8 | -2.5 cm | 101.932 |
| 2026-06 | 71.7 | 16.8 | -1.9 cm | 101.913 |
| 2026-07 | 99.5 | 19.5 | -1.5 cm | 101.898 |
| 2026-08 | 76.7 | 18.5 | +0.0 cm | 101.898 |
| 2026-09 | 64.1 | 13.9 | +1.0 cm | 101.908 |
| 2026-10 | 44.6 | 9.1 | +0.4 cm | 101.912 |
| 2026-11 | 47.0 | 4.5 | +3.0 cm | 101.942 |
| 2026-12 | 47.8 | 1.2 | +5.5 cm | 101.997 |
| 2027-01 | 48.5 | -0.2 | +7.1 cm | 102.068 |

- **Szansa realizacji:** 7.6 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.178 m (+17.8 cm)
- **Poziom na koniec stycznia 2027:** 102.068 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | 3.1 | +3.5 cm | 101.925 |
| 2026-03 | 22.0 | 5.1 | +2.3 cm | 101.948 |
| 2026-04 | 15.9 | 9.4 | -0.1 cm | 101.947 |
| 2026-05 | 30.2 | 14.8 | -2.1 cm | 101.927 |
| 2026-06 | 36.6 | 18.8 | -3.5 cm | 101.892 |
| 2026-07 | 47.1 | 20.1 | -5.7 cm | 101.835 |
| 2026-08 | 37.2 | 19.4 | -7.2 cm | 101.763 |
| 2026-09 | 22.9 | 15.6 | -5.5 cm | 101.708 |
| 2026-10 | 18.0 | 10.6 | -2.7 cm | 101.68 |
| 2026-11 | 23.5 | 5.4 | +0.8 cm | 101.689 |
| 2026-12 | 26.2 | 2.2 | +3.2 cm | 101.721 |
| 2027-01 | 23.3 | 1.8 | +4.0 cm | 101.761 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.129 m (-12.9 cm)
- **Poziom na koniec stycznia 2027:** 101.761 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | 3.1 | +3.7 cm | 101.927 |
| 2026-03 | 30.8 | 5.1 | +3.0 cm | 101.957 |
| 2026-04 | 28.2 | 9.4 | +0.1 cm | 101.958 |
| 2026-05 | 42.4 | 14.8 | -2.6 cm | 101.932 |
| 2026-06 | 55.5 | 18.8 | -4.2 cm | 101.89 |
| 2026-07 | 65.5 | 20.1 | -4.4 cm | 101.846 |
| 2026-08 | 52.7 | 19.4 | -4.0 cm | 101.807 |
| 2026-09 | 40.6 | 15.6 | -2.9 cm | 101.778 |
| 2026-10 | 29.0 | 10.6 | -0.6 cm | 101.772 |
| 2026-11 | 37.2 | 5.4 | +3.0 cm | 101.802 |
| 2026-12 | 39.2 | 2.2 | +4.8 cm | 101.85 |
| 2027-01 | 35.5 | 1.8 | +6.5 cm | 101.915 |

- **Szansa realizacji:** 15.8 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.025 m (+2.5 cm)
- **Poziom na koniec stycznia 2027:** 101.915 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | 3.1 | +3.8 cm | 101.928 |
| 2026-03 | 47.6 | 5.1 | +2.9 cm | 101.957 |
| 2026-04 | 35.4 | 9.4 | -0.3 cm | 101.954 |
| 2026-05 | 60.2 | 14.8 | -2.4 cm | 101.93 |
| 2026-06 | 71.7 | 18.8 | -2.3 cm | 101.907 |
| 2026-07 | 99.5 | 20.1 | -1.5 cm | 101.892 |
| 2026-08 | 76.7 | 19.4 | -1.2 cm | 101.88 |
| 2026-09 | 64.1 | 15.6 | +0.7 cm | 101.887 |
| 2026-10 | 44.6 | 10.6 | +1.8 cm | 101.905 |
| 2026-11 | 47.0 | 5.4 | +4.4 cm | 101.949 |
| 2026-12 | 47.8 | 2.2 | +6.7 cm | 102.016 |
| 2027-01 | 48.5 | 1.8 | +9.4 cm | 102.11 |

- **Szansa realizacji:** 7.6 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.220 m (+22.0 cm)
- **Poziom na koniec stycznia 2027:** 102.11 m n.p.m.



*Wygenerowano: 2026-02-15 13:45*