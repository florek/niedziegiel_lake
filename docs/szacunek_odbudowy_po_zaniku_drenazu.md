# Szacunek lat odbudowy poziomu po zaniku dodatkowego źródła drenażu

## Założenia (uproszczone)

- **Rozbieżność** = wysokość rzeczywista − wysokość w scenariuszu modelowym (klimat, sezon, lagi). Ujemna = jezioro poniżej scenariusza.
- Przy **zaniku dodatkowego drenażu** zakładamy, że poziom rzeczywisty dąży do scenariusza modelowego; szacujemy **ile lat** potrzeba na „zamknięcie” obecnej luki.
- **Scenariusz A (symmetric):** odbudowa z prędkością równą obserwowanemu tempu narastania rozjazdu (trend liniowy rozbieżności w czasie).
- **Scenariusz B (stałe tempo):** odbudowa z prędkością **5.0 cm/rok**.
- Wartości oparte na średniej rozbieżności z **ostatnich 12 miesięcy** i trendzie z pełnego szeregu ewaluacji. **Szacunek teoretyczny**, bez modelowania hydrologicznego odbudowy.
- **Projekcja odbudowy:** scenariusz modelowy przy **meteo z ostatnich 15 lat** (sekwencja miesięczna, bez harmonijki). Do 2/2026 poziom rzeczywisty – **trend z ostatnich 5 lat**; od 2/2026 **wznios wód gruntowych** (cm/rok z CSV lub 5 cm/rok). Wykres: tylko odbudowa do scenariusza naturalnego (bez scenariusza drenażowego).

---

## Wznios poziomu wód gruntowych – porównanie

Dwa wzniosy dla porównania (źródło: `data/zanik_drenazu.csv`): wznios bazowy oraz wznios po zalaniu kopalni.

| Jezioro | Wznios (cm/rok) | Wznios po zalaniu kopalni (cm/rok) |
|---------|-----------------|-------------------------------------|
| Jezioro Budzisławskie | — | — |
| Jezioro Kownackie | — | — |
| Jezioro Koziegłowskie | — | — |
| Jezioro Niedzięgiel | — | — |
| Jezioro Ostrowskie | — | — |
| Jezioro Powidzkie | — | — |
| Jezioro Skulska Wieś | — | — |
| Jezioro Suszewskie | — | — |
| Jezioro Wilczyńskie | — | — |

---

## Wyniki per jezioro

### Jezioro Budzisławskie

- **Średnia rozbieżność (ostatnie 12 miesięcy):** 218.8 cm
- **Trend rozbieżności:** 5.40 cm/rok
- **Szacunek odbudowy (scenariusz A):** —
- **Szacunek odbudowy (scenariusz B):** —

### Jezioro Kownackie

- **Średnia rozbieżność (ostatnie 12 miesięcy):** 707.0 cm
- **Trend rozbieżności:** 22.12 cm/rok
- **Szacunek odbudowy (scenariusz A):** —
- **Szacunek odbudowy (scenariusz B):** —

### Jezioro Koziegłowskie

- **Średnia rozbieżność (ostatnie 12 miesięcy):** 294.5 cm
- **Trend rozbieżności:** 9.87 cm/rok
- **Szacunek odbudowy (scenariusz A):** —
- **Szacunek odbudowy (scenariusz B):** —

### Jezioro Niedzięgiel

- **Średnia rozbieżność (ostatnie 12 miesięcy):** 535.1 cm
- **Trend rozbieżności:** 12.79 cm/rok
- **Szacunek odbudowy (scenariusz A):** —
- **Szacunek odbudowy (scenariusz B):** —

### Jezioro Ostrowskie

- **Średnia rozbieżność (ostatnie 12 miesięcy):** 352.1 cm
- **Trend rozbieżności:** 10.43 cm/rok
- **Szacunek odbudowy (scenariusz A):** —
- **Szacunek odbudowy (scenariusz B):** —

### Jezioro Powidzkie

- **Średnia rozbieżność (ostatnie 12 miesięcy):** 451.3 cm
- **Trend rozbieżności:** 9.70 cm/rok
- **Szacunek odbudowy (scenariusz A):** —
- **Szacunek odbudowy (scenariusz B):** —

### Jezioro Skulska Wieś

- **Średnia rozbieżność (ostatnie 12 miesięcy):** 73.2 cm
- **Trend rozbieżności:** 2.41 cm/rok
- **Szacunek odbudowy (scenariusz A):** —
- **Szacunek odbudowy (scenariusz B):** —

### Jezioro Suszewskie

- **Średnia rozbieżność (ostatnie 12 miesięcy):** 1262.7 cm
- **Trend rozbieżności:** 39.81 cm/rok
- **Szacunek odbudowy (scenariusz A):** —
- **Szacunek odbudowy (scenariusz B):** —

### Jezioro Wilczyńskie

- **Średnia rozbieżność (ostatnie 12 miesięcy):** 342.6 cm
- **Trend rozbieżności:** 8.35 cm/rok
- **Szacunek odbudowy (scenariusz A):** —
- **Szacunek odbudowy (scenariusz B):** —

---

## Wykresy projekcji odbudowy

Dla każdego jeziora: **odbudowa do scenariusza naturalnego** (meteo z ostatnich 15 lat, wznios wód gruntowych). Wykres bez scenariusza drenażowego – kontekst to odbudowa po zaniku drenażu.

### Jezioro Budzisławskie

![Odbudowa budzislawskie](odbudowa/odbudowa_budzislawskie.png)

### Jezioro Kownackie

![Odbudowa kownackie](odbudowa/odbudowa_kownackie.png)

### Jezioro Koziegłowskie

![Odbudowa kozieglowskie](odbudowa/odbudowa_kozieglowskie.png)

### Jezioro Niedzięgiel

![Odbudowa niedziegiel](odbudowa/odbudowa_niedziegiel.png)

### Jezioro Ostrowskie

![Odbudowa ostrowskie](odbudowa/odbudowa_ostrowskie.png)

### Jezioro Powidzkie

![Odbudowa powidzkie](odbudowa/odbudowa_powidzkie.png)

### Jezioro Skulska Wieś

![Odbudowa skulskawies](odbudowa/odbudowa_skulskawies.png)

### Jezioro Suszewskie

![Odbudowa suszewskie](odbudowa/odbudowa_suszewskie.png)

### Jezioro Wilczyńskie

![Odbudowa wilczynskie](odbudowa/odbudowa_wilczynskie.png)

---

## Uwagi

- Analiza **całkowicie osobna** od wnioskowania o istnieniu czynnika drenującego; służy tylko do zgrubnego szacunku czasu odbudowy.
- Rzeczywista odbudowa zależy od zatrzymania drenażu, warunków klimatycznych i bilansu wód podziemnych; powyższe wartości mają charakter orientacyjny.