# Raport: Jezioro Skulska Wieś

Raport ewaluacji na następne 12 miesięcy dla Jezioro Skulska Wieś.

## Poziom wody: rzeczywisty pomiar i model

Niebieska linia: poziom z pliku `data/skulskawies/data.csv` (pomiar na pierwszy dzień miesiąca). Przerywana pomarańczowa: wahania poziomu według modelu (scenariusz kumulatywny z prognozy zmiany miesięcznej).

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

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów): **85.708 m n.p.m.** W stosunku do stanu na koniec stycznia 2026 (85.758 m n.p.m.): ubędzie 0.050 m (-5.0 cm).


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.0 | 1.2 | +4.1 cm | 85.799 |
| 2026-03 | 33.4 | 4.2 | +5.6 cm | 85.855 |
| 2026-04 | 25.1 | 9.3 | +4.9 cm | 85.904 |
| 2026-05 | 46.0 | 13.9 | +0.0 cm | 85.904 |
| 2026-06 | 50.1 | 17.7 | -5.5 cm | 85.849 |
| 2026-07 | 69.9 | 19.7 | -6.4 cm | 85.784 |
| 2026-08 | 53.6 | 19.2 | -6.2 cm | 85.723 |
| 2026-09 | 40.3 | 14.8 | -7.2 cm | 85.651 |
| 2026-10 | 31.5 | 9.8 | -3.5 cm | 85.617 |
| 2026-11 | 34.6 | 4.7 | -0.8 cm | 85.609 |
| 2026-12 | 34.9 | 1.4 | +3.4 cm | 85.643 |
| 2027-01 | 38.4 | 0.0 | +6.5 cm | 85.708 |

- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 491.7 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.050 m (-5.0 cm)
- **Poziom na koniec stycznia 2027:** 85.708 m n.p.m.

### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | -1.0 | +3.8 cm | 85.796 |
| 2026-03 | 22.8 | 3.0 | +5.5 cm | 85.851 |
| 2026-04 | 15.0 | 8.4 | +4.9 cm | 85.9 |
| 2026-05 | 34.0 | 12.8 | +2.2 cm | 85.922 |
| 2026-06 | 33.6 | 16.5 | -5.0 cm | 85.872 |
| 2026-07 | 53.9 | 18.8 | -8.4 cm | 85.789 |
| 2026-08 | 35.5 | 18.3 | -8.8 cm | 85.701 |
| 2026-09 | 22.7 | 13.7 | -10.4 cm | 85.597 |
| 2026-10 | 17.6 | 8.3 | -7.8 cm | 85.519 |
| 2026-11 | 21.8 | 3.6 | -5.8 cm | 85.461 |
| 2026-12 | 25.6 | -0.2 | +0.1 cm | 85.462 |
| 2027-01 | 28.6 | -1.9 | +5.3 cm | 85.515 |

- **Szansa realizacji:** 11.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.243 m (-24.3 cm)
- **Poziom na koniec stycznia 2027:** 85.515 m n.p.m.

### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | -1.0 | +3.9 cm | 85.797 |
| 2026-03 | 33.9 | 3.0 | +5.5 cm | 85.852 |
| 2026-04 | 27.7 | 8.4 | +5.4 cm | 85.906 |
| 2026-05 | 46.4 | 12.8 | +3.3 cm | 85.939 |
| 2026-06 | 53.1 | 16.5 | -4.3 cm | 85.896 |
| 2026-07 | 66.7 | 18.8 | -5.8 cm | 85.838 |
| 2026-08 | 56.2 | 18.3 | -5.9 cm | 85.779 |
| 2026-09 | 43.3 | 13.7 | -3.5 cm | 85.744 |
| 2026-10 | 33.9 | 8.3 | +1.5 cm | 85.759 |
| 2026-11 | 38.8 | 3.6 | +2.9 cm | 85.788 |
| 2026-12 | 36.7 | -0.2 | +6.2 cm | 85.85 |
| 2027-01 | 39.8 | -1.9 | +6.9 cm | 85.919 |

- **Szansa realizacji:** 14.2 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.161 m (+16.1 cm)
- **Poziom na koniec stycznia 2027:** 85.919 m n.p.m.

### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | -1.0 | +4.7 cm | 85.805 |
| 2026-03 | 49.5 | 3.0 | +7.0 cm | 85.875 |
| 2026-04 | 36.1 | 8.4 | +7.1 cm | 85.946 |
| 2026-05 | 64.7 | 12.8 | +4.1 cm | 85.987 |
| 2026-06 | 70.6 | 16.5 | -3.4 cm | 85.953 |
| 2026-07 | 102.3 | 18.8 | -2.4 cm | 85.929 |
| 2026-08 | 77.4 | 18.3 | +0.0 cm | 85.929 |
| 2026-09 | 62.5 | 13.7 | -0.4 cm | 85.925 |
| 2026-10 | 49.0 | 8.3 | +2.7 cm | 85.952 |
| 2026-11 | 46.6 | 3.6 | +5.7 cm | 86.009 |
| 2026-12 | 46.4 | -0.2 | +8.3 cm | 86.092 |
| 2027-01 | 51.6 | -1.9 | +8.7 cm | 86.179 |

- **Szansa realizacji:** 7.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.421 m (+42.1 cm)
- **Poziom na koniec stycznia 2027:** 86.179 m n.p.m.

### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | 0.8 | +4.2 cm | 85.8 |
| 2026-03 | 22.8 | 4.3 | +5.2 cm | 85.852 |
| 2026-04 | 15.0 | 9.1 | +4.9 cm | 85.901 |
| 2026-05 | 34.0 | 13.7 | -0.2 cm | 85.899 |
| 2026-06 | 33.6 | 17.8 | -5.8 cm | 85.84 |
| 2026-07 | 53.9 | 19.8 | -8.4 cm | 85.757 |
| 2026-08 | 35.5 | 19.3 | -8.8 cm | 85.669 |
| 2026-09 | 22.7 | 14.7 | -12.4 cm | 85.545 |
| 2026-10 | 17.6 | 9.8 | -8.2 cm | 85.463 |
| 2026-11 | 21.8 | 4.8 | -7.1 cm | 85.392 |
| 2026-12 | 25.6 | 1.8 | -2.1 cm | 85.372 |
| 2027-01 | 28.6 | 0.1 | +4.7 cm | 85.418 |

- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.340 m (-34.0 cm)
- **Poziom na koniec stycznia 2027:** 85.418 m n.p.m.

### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | 0.8 | +4.2 cm | 85.8 |
| 2026-03 | 33.9 | 4.3 | +5.3 cm | 85.854 |
| 2026-04 | 27.7 | 9.1 | +4.9 cm | 85.903 |
| 2026-05 | 46.4 | 13.7 | +0.9 cm | 85.912 |
| 2026-06 | 53.1 | 17.8 | -5.4 cm | 85.858 |
| 2026-07 | 66.7 | 19.8 | -6.6 cm | 85.792 |
| 2026-08 | 56.2 | 19.3 | -7.0 cm | 85.721 |
| 2026-09 | 43.3 | 14.7 | -7.0 cm | 85.651 |
| 2026-10 | 33.9 | 9.8 | -4.3 cm | 85.608 |
| 2026-11 | 38.8 | 4.8 | +0.8 cm | 85.616 |
| 2026-12 | 36.7 | 1.8 | +4.5 cm | 85.661 |
| 2027-01 | 39.8 | 0.1 | +7.1 cm | 85.732 |

- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.026 m (-2.6 cm)
- **Poziom na koniec stycznia 2027:** 85.732 m n.p.m.

### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | 0.8 | +5.0 cm | 85.808 |
| 2026-03 | 49.5 | 4.3 | +6.8 cm | 85.876 |
| 2026-04 | 36.1 | 9.1 | +6.8 cm | 85.944 |
| 2026-05 | 64.7 | 13.7 | +1.0 cm | 85.954 |
| 2026-06 | 70.6 | 17.8 | -4.5 cm | 85.909 |
| 2026-07 | 102.3 | 19.8 | -3.1 cm | 85.878 |
| 2026-08 | 77.4 | 19.3 | -0.5 cm | 85.873 |
| 2026-09 | 62.5 | 14.7 | -2.7 cm | 85.846 |
| 2026-10 | 49.0 | 9.8 | +2.1 cm | 85.866 |
| 2026-11 | 46.6 | 4.8 | +5.5 cm | 85.922 |
| 2026-12 | 46.4 | 1.8 | +7.1 cm | 85.992 |
| 2027-01 | 51.6 | 0.1 | +8.8 cm | 86.08 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.322 m (+32.2 cm)
- **Poziom na koniec stycznia 2027:** 86.08 m n.p.m.

### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 25.8 | 3.8 | +3.7 cm | 85.795 |
| 2026-03 | 22.8 | 5.4 | +5.1 cm | 85.846 |
| 2026-04 | 15.0 | 10.4 | +3.3 cm | 85.879 |
| 2026-05 | 34.0 | 15.1 | -4.0 cm | 85.839 |
| 2026-06 | 33.6 | 18.9 | -7.9 cm | 85.76 |
| 2026-07 | 53.9 | 20.4 | -8.9 cm | 85.67 |
| 2026-08 | 35.5 | 20.0 | -11.0 cm | 85.561 |
| 2026-09 | 22.7 | 16.0 | -11.7 cm | 85.444 |
| 2026-10 | 17.6 | 11.2 | -7.9 cm | 85.365 |
| 2026-11 | 21.8 | 5.7 | -6.3 cm | 85.302 |
| 2026-12 | 25.6 | 2.6 | -0.2 cm | 85.3 |
| 2027-01 | 28.6 | 1.9 | +4.7 cm | 85.347 |

- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.411 m (-41.1 cm)
- **Poziom na koniec stycznia 2027:** 85.347 m n.p.m.

### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 34.4 | 3.8 | +3.8 cm | 85.796 |
| 2026-03 | 33.9 | 5.4 | +5.1 cm | 85.847 |
| 2026-04 | 27.7 | 10.4 | +3.4 cm | 85.881 |
| 2026-05 | 46.4 | 15.1 | -3.8 cm | 85.843 |
| 2026-06 | 53.1 | 18.9 | -7.0 cm | 85.772 |
| 2026-07 | 66.7 | 20.4 | -7.2 cm | 85.7 |
| 2026-08 | 56.2 | 20.0 | -6.6 cm | 85.634 |
| 2026-09 | 43.3 | 16.0 | -7.7 cm | 85.557 |
| 2026-10 | 33.9 | 11.2 | -5.0 cm | 85.507 |
| 2026-11 | 38.8 | 5.7 | -1.8 cm | 85.488 |
| 2026-12 | 36.7 | 2.6 | +3.8 cm | 85.526 |
| 2027-01 | 39.8 | 1.9 | +6.5 cm | 85.592 |

- **Szansa realizacji:** 14.5 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody** (koniec symulacji − start): -0.166 m (-16.6 cm)
- **Poziom na koniec stycznia 2027:** 85.592 m n.p.m.

### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)

| Data | Opad (mm) | Temperatura (°C) | Zmiana prognoza (cm) | Poziom (m n.p.m.) |
|------|-----------|------------------|----------------------|-------------------|
| 2026-02 | 46.4 | 3.8 | +4.3 cm | 85.801 |
| 2026-03 | 49.5 | 5.4 | +6.6 cm | 85.868 |
| 2026-04 | 36.1 | 10.4 | +5.2 cm | 85.919 |
| 2026-05 | 64.7 | 15.1 | -2.2 cm | 85.898 |
| 2026-06 | 70.6 | 18.9 | -5.0 cm | 85.848 |
| 2026-07 | 102.3 | 20.4 | -2.9 cm | 85.819 |
| 2026-08 | 77.4 | 20.0 | +0.1 cm | 85.821 |
| 2026-09 | 62.5 | 16.0 | -3.9 cm | 85.782 |
| 2026-10 | 49.0 | 11.2 | +1.4 cm | 85.796 |
| 2026-11 | 46.6 | 5.7 | +5.1 cm | 85.848 |
| 2026-12 | 46.4 | 2.6 | +6.5 cm | 85.913 |
| 2027-01 | 51.6 | 1.9 | +8.2 cm | 85.995 |

- **Szansa realizacji:** 7.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody** (koniec symulacji − start): +0.237 m (+23.7 cm)
- **Poziom na koniec stycznia 2027:** 85.995 m n.p.m.



*Wygenerowano: 2026-02-15 12:16*