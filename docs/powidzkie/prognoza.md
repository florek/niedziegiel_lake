# Raport: Jezioro Powidzkie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Powidzkie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/powidzkie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Symulacje wariantów pogodowych (12 miesięcy do przodu)

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/powidzkie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykres: pełny zakres historii (od 1974) + 12 miesięcy symulacji.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa realizacji (%) |
|---------|------------------------|
| zimny, suchy | 10.2 |
| zimny, normalny | 13.7 |
| zimny, wilgotny | 7.3 |
| normalny, suchy | 10.8 |
| normalny, normalny | 16.0 |
| normalny, wilgotny | 7.6 |
| ciepły, suchy | 10.8 |
| ciepły, normalny | 15.9 |
| ciepły, wilgotny | 7.6 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów): **97.848 m n.p.m.** W stosunku do stanu na koniec stycznia 2026 (97.7681 m n.p.m.): przybędzie +0.080 m (+8.0 cm).


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 28.8 | 0.4 | +2.9 cm | 97.797 |
| 2026-03 | 31.8 | 3.8 | +2.5 cm | 97.822 |
| 2026-04 | 25.9 | 8.6 | +0.7 cm | 97.829 |
| 2026-05 | 42.5 | 13.7 | -1.4 cm | 97.815 |
| 2026-06 | 53.1 | 17.2 | -2.2 cm | 97.793 |
| 2026-07 | 67.2 | 19.0 | -3.1 cm | 97.763 |
| 2026-08 | 53.1 | 18.5 | -2.9 cm | 97.733 |
| 2026-09 | 40.2 | 14.1 | -0.9 cm | 97.725 |
| 2026-10 | 29.0 | 9.3 | +0.5 cm | 97.73 |
| 2026-11 | 35.0 | 4.3 | +3.2 cm | 97.761 |
| 2026-12 | 36.9 | 1.0 | +4.2 cm | 97.804 |
| 2027-01 | 34.5 | -0.2 | +4.4 cm | 97.848 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.2 °C
- **Suma opadu (prognoza):** 478.0 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.080 m (+8.0 cm)
- **Poziom na koniec stycznia 2027:** 97.848 m n.p.m.

### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | -2.1 | +2.9 cm | 97.798 |
| 2026-03 | 22.0 | 2.0 | +2.8 cm | 97.826 |
| 2026-04 | 15.9 | 7.7 | +1.8 cm | 97.843 |
| 2026-05 | 30.2 | 12.6 | +0.0 cm | 97.843 |
| 2026-06 | 36.6 | 16.0 | -2.5 cm | 97.818 |
| 2026-07 | 47.1 | 17.4 | -3.9 cm | 97.78 |
| 2026-08 | 37.2 | 17.4 | -3.9 cm | 97.74 |
| 2026-09 | 22.9 | 12.9 | -0.9 cm | 97.731 |
| 2026-10 | 18.0 | 8.1 | +0.1 cm | 97.732 |
| 2026-11 | 23.5 | 2.9 | +3.2 cm | 97.764 |
| 2026-12 | 26.2 | -0.4 | +3.9 cm | 97.804 |
| 2027-01 | 23.3 | -2.2 | +4.1 cm | 97.845 |

- **Szansa realizacji:** 10.2 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.077 m (+7.7 cm)
- **Poziom na koniec stycznia 2027:** 97.845 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | -2.1 | +3.0 cm | 97.798 |
| 2026-03 | 30.8 | 2.0 | +3.2 cm | 97.83 |
| 2026-04 | 28.2 | 7.7 | +1.5 cm | 97.845 |
| 2026-05 | 42.4 | 12.6 | +0.6 cm | 97.851 |
| 2026-06 | 55.5 | 16.0 | +0.2 cm | 97.854 |
| 2026-07 | 65.5 | 17.4 | -2.0 cm | 97.833 |
| 2026-08 | 52.7 | 17.4 | -2.5 cm | 97.809 |
| 2026-09 | 40.6 | 12.9 | -1.3 cm | 97.796 |
| 2026-10 | 29.0 | 8.1 | +0.6 cm | 97.802 |
| 2026-11 | 37.2 | 2.9 | +4.2 cm | 97.844 |
| 2026-12 | 39.2 | -0.4 | +4.7 cm | 97.891 |
| 2027-01 | 35.5 | -2.2 | +4.3 cm | 97.934 |

- **Szansa realizacji:** 13.7 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.166 m (+16.6 cm)
- **Poziom na koniec stycznia 2027:** 97.934 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | -2.1 | +3.0 cm | 97.798 |
| 2026-03 | 47.6 | 2.0 | +3.1 cm | 97.829 |
| 2026-04 | 35.4 | 7.7 | +1.7 cm | 97.846 |
| 2026-05 | 60.2 | 12.6 | +0.2 cm | 97.848 |
| 2026-06 | 71.7 | 16.0 | -1.6 cm | 97.832 |
| 2026-07 | 99.5 | 17.4 | -2.6 cm | 97.806 |
| 2026-08 | 76.7 | 17.4 | -2.3 cm | 97.783 |
| 2026-09 | 64.1 | 12.9 | -0.6 cm | 97.777 |
| 2026-10 | 44.6 | 8.1 | +0.6 cm | 97.783 |
| 2026-11 | 47.0 | 2.9 | +3.8 cm | 97.82 |
| 2026-12 | 47.8 | -0.4 | +4.5 cm | 97.865 |
| 2027-01 | 48.5 | -2.2 | +4.2 cm | 97.907 |

- **Szansa realizacji:** 7.3 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.139 m (+13.9 cm)
- **Poziom na koniec stycznia 2027:** 97.907 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | -0.1 | +2.9 cm | 97.798 |
| 2026-03 | 22.0 | 4.2 | +2.0 cm | 97.818 |
| 2026-04 | 15.9 | 8.7 | +0.1 cm | 97.818 |
| 2026-05 | 30.2 | 13.8 | -2.8 cm | 97.79 |
| 2026-06 | 36.6 | 16.8 | -3.5 cm | 97.755 |
| 2026-07 | 47.1 | 19.5 | -4.6 cm | 97.709 |
| 2026-08 | 37.2 | 18.5 | -3.9 cm | 97.67 |
| 2026-09 | 22.9 | 13.9 | -1.2 cm | 97.659 |
| 2026-10 | 18.0 | 9.1 | +0.2 cm | 97.661 |
| 2026-11 | 23.5 | 4.5 | +3.0 cm | 97.69 |
| 2026-12 | 26.2 | 1.2 | +3.9 cm | 97.73 |
| 2027-01 | 23.3 | -0.2 | +4.2 cm | 97.771 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.003 m (+0.3 cm)
- **Poziom na koniec stycznia 2027:** 97.771 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | -0.1 | +3.0 cm | 97.798 |
| 2026-03 | 30.8 | 4.2 | +2.4 cm | 97.822 |
| 2026-04 | 28.2 | 8.7 | +0.2 cm | 97.825 |
| 2026-05 | 42.4 | 13.8 | -2.5 cm | 97.8 |
| 2026-06 | 55.5 | 16.8 | -2.4 cm | 97.776 |
| 2026-07 | 65.5 | 19.5 | -2.6 cm | 97.75 |
| 2026-08 | 52.7 | 18.5 | -2.5 cm | 97.724 |
| 2026-09 | 40.6 | 13.9 | -1.1 cm | 97.714 |
| 2026-10 | 29.0 | 9.1 | +0.5 cm | 97.719 |
| 2026-11 | 37.2 | 4.5 | +2.9 cm | 97.748 |
| 2026-12 | 39.2 | 1.2 | +4.2 cm | 97.79 |
| 2027-01 | 35.5 | -0.2 | +4.4 cm | 97.834 |

- **Szansa realizacji:** 16.0 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.066 m (+6.6 cm)
- **Poziom na koniec stycznia 2027:** 97.834 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | -0.1 | +3.0 cm | 97.798 |
| 2026-03 | 47.6 | 4.2 | +2.3 cm | 97.821 |
| 2026-04 | 35.4 | 8.7 | +0.4 cm | 97.826 |
| 2026-05 | 60.2 | 13.8 | -1.9 cm | 97.806 |
| 2026-06 | 71.7 | 16.8 | -2.5 cm | 97.781 |
| 2026-07 | 99.5 | 19.5 | -2.8 cm | 97.753 |
| 2026-08 | 76.7 | 18.5 | -2.4 cm | 97.729 |
| 2026-09 | 64.1 | 13.9 | -0.4 cm | 97.726 |
| 2026-10 | 44.6 | 9.1 | +0.0 cm | 97.726 |
| 2026-11 | 47.0 | 4.5 | +2.0 cm | 97.746 |
| 2026-12 | 47.8 | 1.2 | +3.9 cm | 97.785 |
| 2027-01 | 48.5 | -0.2 | +4.4 cm | 97.829 |

- **Szansa realizacji:** 7.6 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.061 m (+6.1 cm)
- **Poziom na koniec stycznia 2027:** 97.829 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | 3.1 | +2.8 cm | 97.796 |
| 2026-03 | 22.0 | 5.1 | +2.0 cm | 97.816 |
| 2026-04 | 15.9 | 9.4 | +0.1 cm | 97.817 |
| 2026-05 | 30.2 | 14.8 | -2.6 cm | 97.791 |
| 2026-06 | 36.6 | 18.8 | -3.6 cm | 97.755 |
| 2026-07 | 47.1 | 20.1 | -4.5 cm | 97.711 |
| 2026-08 | 37.2 | 19.4 | -3.7 cm | 97.674 |
| 2026-09 | 22.9 | 15.6 | -1.1 cm | 97.663 |
| 2026-10 | 18.0 | 10.6 | +0.6 cm | 97.669 |
| 2026-11 | 23.5 | 5.4 | +3.3 cm | 97.703 |
| 2026-12 | 26.2 | 2.2 | +3.9 cm | 97.742 |
| 2027-01 | 23.3 | 1.8 | +4.2 cm | 97.784 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.016 m (+1.6 cm)
- **Poziom na koniec stycznia 2027:** 97.784 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | 3.1 | +2.9 cm | 97.797 |
| 2026-03 | 30.8 | 5.1 | +2.4 cm | 97.82 |
| 2026-04 | 28.2 | 9.4 | +0.3 cm | 97.823 |
| 2026-05 | 42.4 | 14.8 | -2.3 cm | 97.8 |
| 2026-06 | 55.5 | 18.8 | -2.2 cm | 97.778 |
| 2026-07 | 65.5 | 20.1 | -2.6 cm | 97.752 |
| 2026-08 | 52.7 | 19.4 | -2.7 cm | 97.725 |
| 2026-09 | 40.6 | 15.6 | -0.7 cm | 97.718 |
| 2026-10 | 29.0 | 10.6 | +0.9 cm | 97.727 |
| 2026-11 | 37.2 | 5.4 | +3.5 cm | 97.763 |
| 2026-12 | 39.2 | 2.2 | +4.7 cm | 97.81 |
| 2027-01 | 35.5 | 1.8 | +5.1 cm | 97.861 |

- **Szansa realizacji:** 15.9 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.093 m (+9.3 cm)
- **Poziom na koniec stycznia 2027:** 97.861 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | 3.1 | +2.9 cm | 97.797 |
| 2026-03 | 47.6 | 5.1 | +2.2 cm | 97.819 |
| 2026-04 | 35.4 | 9.4 | +0.5 cm | 97.824 |
| 2026-05 | 60.2 | 14.8 | -0.2 cm | 97.823 |
| 2026-06 | 71.7 | 18.8 | -1.8 cm | 97.804 |
| 2026-07 | 99.5 | 20.1 | -2.5 cm | 97.779 |
| 2026-08 | 76.7 | 19.4 | -2.4 cm | 97.755 |
| 2026-09 | 64.1 | 15.6 | -0.2 cm | 97.754 |
| 2026-10 | 44.6 | 10.6 | +0.4 cm | 97.758 |
| 2026-11 | 47.0 | 5.4 | +1.9 cm | 97.777 |
| 2026-12 | 47.8 | 2.2 | +3.9 cm | 97.815 |
| 2027-01 | 48.5 | 1.8 | +4.6 cm | 97.861 |

- **Szansa realizacji:** 7.6 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.093 m (+9.3 cm)
- **Poziom na koniec stycznia 2027:** 97.861 m n.p.m.



*Wygenerowano: 2026-02-15 15:00*