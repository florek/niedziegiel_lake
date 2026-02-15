# Raport: Jezioro Powidzkie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Powidzkie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska linia: poziom z pliku `data/powidzkie/data.csv` (pomiar na pierwszy dzień miesiąca). Przerywana pomarańczowa: wahania poziomu według modelu (scenariusz kumulatywny z prognozy zmiany miesięcznej).

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

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów): **97.844 m n.p.m.** W stosunku do stanu na koniec stycznia 2026 (97.7681 m n.p.m.): przybędzie +0.076 m (+7.6 cm).


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 28.8 | 0.4 | +2.9 cm | 97.797 |
| 2026-03 | 31.8 | 3.8 | +1.1 cm | 97.808 |
| 2026-04 | 25.9 | 8.6 | -1.6 cm | 97.792 |
| 2026-05 | 42.5 | 13.7 | -1.9 cm | 97.772 |
| 2026-06 | 53.1 | 17.2 | -1.7 cm | 97.756 |
| 2026-07 | 67.2 | 19.0 | -2.2 cm | 97.733 |
| 2026-08 | 53.1 | 18.5 | -2.4 cm | 97.71 |
| 2026-09 | 40.2 | 14.1 | -0.7 cm | 97.703 |
| 2026-10 | 29.0 | 9.3 | +1.1 cm | 97.714 |
| 2026-11 | 35.0 | 4.3 | +3.9 cm | 97.752 |
| 2026-12 | 36.9 | 1.0 | +4.5 cm | 97.798 |
| 2027-01 | 34.5 | -0.2 | +4.6 cm | 97.844 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.2 °C
- **Suma opadu (prognoza):** 478.0 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.076 m (+7.6 cm)
- **Poziom na koniec stycznia 2027:** 97.844 m n.p.m.

### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | -2.1 | +2.7 cm | 97.795 |
| 2026-03 | 22.0 | 2.0 | +2.0 cm | 97.815 |
| 2026-04 | 15.9 | 7.7 | -0.9 cm | 97.807 |
| 2026-05 | 30.2 | 12.6 | -1.9 cm | 97.788 |
| 2026-06 | 36.6 | 16.0 | -2.7 cm | 97.761 |
| 2026-07 | 47.1 | 17.4 | -3.7 cm | 97.723 |
| 2026-08 | 37.2 | 17.4 | -3.5 cm | 97.689 |
| 2026-09 | 22.9 | 12.9 | -0.8 cm | 97.68 |
| 2026-10 | 18.0 | 8.1 | +1.1 cm | 97.691 |
| 2026-11 | 23.5 | 2.9 | +3.9 cm | 97.73 |
| 2026-12 | 26.2 | -0.4 | +4.0 cm | 97.77 |
| 2027-01 | 23.3 | -2.2 | +3.9 cm | 97.809 |

- **Szansa realizacji:** 10.2 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.041 m (+4.1 cm)
- **Poziom na koniec stycznia 2027:** 97.809 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | -2.1 | +3.0 cm | 97.798 |
| 2026-03 | 30.8 | 2.0 | +2.2 cm | 97.82 |
| 2026-04 | 28.2 | 7.7 | -1.1 cm | 97.809 |
| 2026-05 | 42.4 | 12.6 | -1.3 cm | 97.796 |
| 2026-06 | 55.5 | 16.0 | -0.9 cm | 97.787 |
| 2026-07 | 65.5 | 17.4 | -1.5 cm | 97.772 |
| 2026-08 | 52.7 | 17.4 | -3.2 cm | 97.74 |
| 2026-09 | 40.6 | 12.9 | -1.2 cm | 97.729 |
| 2026-10 | 29.0 | 8.1 | +1.3 cm | 97.742 |
| 2026-11 | 37.2 | 2.9 | +4.7 cm | 97.789 |
| 2026-12 | 39.2 | -0.4 | +5.3 cm | 97.842 |
| 2027-01 | 35.5 | -2.2 | +4.6 cm | 97.888 |

- **Szansa realizacji:** 13.7 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.120 m (+12.0 cm)
- **Poziom na koniec stycznia 2027:** 97.888 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | -2.1 | +3.2 cm | 97.8 |
| 2026-03 | 47.6 | 2.0 | +1.6 cm | 97.816 |
| 2026-04 | 35.4 | 7.7 | -1.1 cm | 97.804 |
| 2026-05 | 60.2 | 12.6 | -0.1 cm | 97.803 |
| 2026-06 | 71.7 | 16.0 | -0.6 cm | 97.797 |
| 2026-07 | 99.5 | 17.4 | -1.3 cm | 97.784 |
| 2026-08 | 76.7 | 17.4 | -1.7 cm | 97.767 |
| 2026-09 | 64.1 | 12.9 | -0.0 cm | 97.767 |
| 2026-10 | 44.6 | 8.1 | +1.5 cm | 97.782 |
| 2026-11 | 47.0 | 2.9 | +4.3 cm | 97.826 |
| 2026-12 | 47.8 | -0.4 | +4.5 cm | 97.871 |
| 2027-01 | 48.5 | -2.2 | +5.6 cm | 97.927 |

- **Szansa realizacji:** 7.3 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.159 m (+15.9 cm)
- **Poziom na koniec stycznia 2027:** 97.927 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | -0.1 | +2.7 cm | 97.795 |
| 2026-03 | 22.0 | 4.2 | +0.8 cm | 97.803 |
| 2026-04 | 15.9 | 8.7 | -1.2 cm | 97.792 |
| 2026-05 | 30.2 | 13.8 | -1.8 cm | 97.774 |
| 2026-06 | 36.6 | 16.8 | -2.4 cm | 97.75 |
| 2026-07 | 47.1 | 19.5 | -3.8 cm | 97.713 |
| 2026-08 | 37.2 | 18.5 | -3.0 cm | 97.683 |
| 2026-09 | 22.9 | 13.9 | -1.0 cm | 97.673 |
| 2026-10 | 18.0 | 9.1 | +0.4 cm | 97.677 |
| 2026-11 | 23.5 | 4.5 | +2.7 cm | 97.705 |
| 2026-12 | 26.2 | 1.2 | +4.0 cm | 97.745 |
| 2027-01 | 23.3 | -0.2 | +3.9 cm | 97.784 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.016 m (+1.6 cm)
- **Poziom na koniec stycznia 2027:** 97.784 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | -0.1 | +3.0 cm | 97.798 |
| 2026-03 | 30.8 | 4.2 | +0.9 cm | 97.807 |
| 2026-04 | 28.2 | 8.7 | -1.5 cm | 97.792 |
| 2026-05 | 42.4 | 13.8 | -2.4 cm | 97.767 |
| 2026-06 | 55.5 | 16.8 | -1.7 cm | 97.75 |
| 2026-07 | 65.5 | 19.5 | -1.9 cm | 97.731 |
| 2026-08 | 52.7 | 18.5 | -2.9 cm | 97.702 |
| 2026-09 | 40.6 | 13.9 | -1.2 cm | 97.69 |
| 2026-10 | 29.0 | 9.1 | +1.0 cm | 97.7 |
| 2026-11 | 37.2 | 4.5 | +4.2 cm | 97.742 |
| 2026-12 | 39.2 | 1.2 | +4.5 cm | 97.787 |
| 2027-01 | 35.5 | -0.2 | +5.2 cm | 97.839 |

- **Szansa realizacji:** 16.0 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.071 m (+7.1 cm)
- **Poziom na koniec stycznia 2027:** 97.839 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | -0.1 | +3.2 cm | 97.8 |
| 2026-03 | 47.6 | 4.2 | +0.2 cm | 97.801 |
| 2026-04 | 35.4 | 8.7 | -2.0 cm | 97.781 |
| 2026-05 | 60.2 | 13.8 | -1.2 cm | 97.77 |
| 2026-06 | 71.7 | 16.8 | -1.0 cm | 97.759 |
| 2026-07 | 99.5 | 19.5 | -1.4 cm | 97.746 |
| 2026-08 | 76.7 | 18.5 | -1.3 cm | 97.733 |
| 2026-09 | 64.1 | 13.9 | +0.1 cm | 97.734 |
| 2026-10 | 44.6 | 9.1 | +1.1 cm | 97.746 |
| 2026-11 | 47.0 | 4.5 | +3.4 cm | 97.78 |
| 2026-12 | 47.8 | 1.2 | +4.4 cm | 97.824 |
| 2027-01 | 48.5 | -0.2 | +3.9 cm | 97.862 |

- **Szansa realizacji:** 7.6 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.094 m (+9.4 cm)
- **Poziom na koniec stycznia 2027:** 97.862 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 19.3 | 3.1 | +2.6 cm | 97.794 |
| 2026-03 | 22.0 | 5.1 | +0.7 cm | 97.801 |
| 2026-04 | 15.9 | 9.4 | -1.8 cm | 97.783 |
| 2026-05 | 30.2 | 14.8 | -3.3 cm | 97.75 |
| 2026-06 | 36.6 | 18.8 | -2.5 cm | 97.725 |
| 2026-07 | 47.1 | 20.1 | -3.3 cm | 97.692 |
| 2026-08 | 37.2 | 19.4 | -2.0 cm | 97.672 |
| 2026-09 | 22.9 | 15.6 | -1.1 cm | 97.661 |
| 2026-10 | 18.0 | 10.6 | +0.7 cm | 97.668 |
| 2026-11 | 23.5 | 5.4 | +3.5 cm | 97.703 |
| 2026-12 | 26.2 | 2.2 | +4.3 cm | 97.746 |
| 2027-01 | 23.3 | 1.8 | +3.9 cm | 97.785 |

- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.017 m (+1.7 cm)
- **Poziom na koniec stycznia 2027:** 97.785 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 29.5 | 3.1 | +2.8 cm | 97.797 |
| 2026-03 | 30.8 | 5.1 | +0.8 cm | 97.805 |
| 2026-04 | 28.2 | 9.4 | -2.3 cm | 97.782 |
| 2026-05 | 42.4 | 14.8 | -2.7 cm | 97.755 |
| 2026-06 | 55.5 | 18.8 | -1.9 cm | 97.736 |
| 2026-07 | 65.5 | 20.1 | -1.6 cm | 97.72 |
| 2026-08 | 52.7 | 19.4 | -1.8 cm | 97.702 |
| 2026-09 | 40.6 | 15.6 | -1.0 cm | 97.692 |
| 2026-10 | 29.0 | 10.6 | +1.3 cm | 97.704 |
| 2026-11 | 37.2 | 5.4 | +4.2 cm | 97.746 |
| 2026-12 | 39.2 | 2.2 | +4.8 cm | 97.794 |
| 2027-01 | 35.5 | 1.8 | +5.1 cm | 97.845 |

- **Szansa realizacji:** 15.9 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.077 m (+7.7 cm)
- **Poziom na koniec stycznia 2027:** 97.845 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 41.0 | 3.1 | +3.0 cm | 97.798 |
| 2026-03 | 47.6 | 5.1 | +0.2 cm | 97.8 |
| 2026-04 | 35.4 | 9.4 | -2.6 cm | 97.774 |
| 2026-05 | 60.2 | 14.8 | -1.4 cm | 97.76 |
| 2026-06 | 71.7 | 18.8 | -1.0 cm | 97.75 |
| 2026-07 | 99.5 | 20.1 | -1.2 cm | 97.737 |
| 2026-08 | 76.7 | 19.4 | -0.5 cm | 97.732 |
| 2026-09 | 64.1 | 15.6 | +1.0 cm | 97.742 |
| 2026-10 | 44.6 | 10.6 | +1.8 cm | 97.76 |
| 2026-11 | 47.0 | 5.4 | +3.5 cm | 97.795 |
| 2026-12 | 47.8 | 2.2 | +4.7 cm | 97.842 |
| 2027-01 | 48.5 | 1.8 | +4.6 cm | 97.888 |

- **Szansa realizacji:** 7.6 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.120 m (+12.0 cm)
- **Poziom na koniec stycznia 2027:** 97.888 m n.p.m.



*Wygenerowano: 2026-02-15 12:03*