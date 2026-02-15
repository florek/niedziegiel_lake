# Szacunek lat odbudowy poziomu po zaniku dodatkowego źródła drenażu

## Założenia (uproszczone)

- **Rozbieżność** = wysokość rzeczywista − wysokość w scenariuszu modelowym (klimat, sezon, lagi). Ujemna = jezioro poniżej scenariusza.
- Przy **zaniku dodatkowego drenażu** zakładamy, że poziom rzeczywisty dąży do scenariusza modelowego; szacujemy **ile lat** potrzeba na „zamknięcie” obecnej luki.
- **Scenariusz A (symmetric):** odbudowa z prędkością równą obserwowanemu tempu narastania rozjazdu (trend liniowy rozbieżności w czasie).
- **Scenariusz B (stałe tempo):** odbudowa z prędkością **5.0 cm/rok**.
- Wartości oparte na średniej rozbieżności z **ostatnich 12 miesięcy** i trendzie z pełnego szeregu ewaluacji. **Szacunek teoretyczny**, bez modelowania hydrologicznego odbudowy.
- **Projekcja odbudowy:** scenariusz modelowy przy **średnich warunkach z ostatnich 5 lat (sezonowość)**. Do 2/2026 poziom rzeczywisty – **trend z ostatnich 5 lat** rzeczywistych pomiarów; od 2/2026 **wznios wód gruntowych** (cm/rok z CSV lub 5 cm/rok). Wykres do momentu zrównania z modelem (koniec odbudowy).

---

## Wznios poziomu wód gruntowych – porównanie

Dwa wzniosy dla porównania (źródło: `data/zanik_drenazu.csv`): wznios bazowy oraz wznios po zalaniu kopalni.

| Jezioro | Wznios (cm/rok) | Wznios po zalaniu kopalni (cm/rok) |
|---------|-----------------|-------------------------------------|
| Jezioro Budzisławskie | — | — |
| Jezioro Koziegłowskie | — | — |
| Jezioro Kownackie | — | — |
| Jezioro Niedzięgiel | — | — |
| Jezioro Ostrowskie | — | — |
| Jezioro Powidzkie | — | — |
| Jezioro Skulska Wieś | — | — |
| Jezioro Suszewskie | — | — |
| Jezioro Wilczyńskie | — | — |

---

## Wyniki per jezioro

### Jezioro Budzisławskie

- **Średnia rozbieżność (ostatnie 12 miesięcy):** -200.2 cm
- **Trend rozbieżności:** -6.86 cm/rok
- **Szacunek odbudowy (scenariusz A, symmetric):** 29.2 lat
- **Szacunek odbudowy (scenariusz B, 5.0 cm/rok):** 40.0 lat

### Jezioro Koziegłowskie

- **Średnia rozbieżność (ostatnie 12 miesięcy):** -73.9 cm
- **Trend rozbieżności:** -4.20 cm/rok
- **Szacunek odbudowy (scenariusz A, symmetric):** 17.6 lat
- **Szacunek odbudowy (scenariusz B, 5.0 cm/rok):** 14.8 lat

### Jezioro Kownackie

- **Średnia rozbieżność (ostatnie 12 miesięcy):** -318.4 cm
- **Trend rozbieżności:** -11.10 cm/rok
- **Szacunek odbudowy (scenariusz A, symmetric):** 28.7 lat
- **Szacunek odbudowy (scenariusz B, 5.0 cm/rok):** 63.7 lat

### Jezioro Niedzięgiel

- **Średnia rozbieżność (ostatnie 12 miesięcy):** -96.7 cm
- **Trend rozbieżności:** -1.17 cm/rok
- **Szacunek odbudowy (scenariusz A, symmetric):** 82.6 lat
- **Szacunek odbudowy (scenariusz B, 5.0 cm/rok):** 19.3 lat

### Jezioro Ostrowskie

- **Średnia rozbieżność (ostatnie 12 miesięcy):** -342.1 cm
- **Trend rozbieżności:** -11.34 cm/rok
- **Szacunek odbudowy (scenariusz A, symmetric):** 30.2 lat
- **Szacunek odbudowy (scenariusz B, 5.0 cm/rok):** 68.4 lat

### Jezioro Powidzkie

- **Średnia rozbieżność (ostatnie 12 miesięcy):** -32.0 cm
- **Trend rozbieżności:** -0.74 cm/rok
- **Szacunek odbudowy (scenariusz A, symmetric):** 43.3 lat
- **Szacunek odbudowy (scenariusz B, 5.0 cm/rok):** 6.4 lat

### Jezioro Skulska Wieś

- **Średnia rozbieżność (ostatnie 12 miesięcy):** 2.1 cm
- **Trend rozbieżności:** 0.55 cm/rok
- **Szacunek odbudowy (scenariusz A):** —
- **Szacunek odbudowy (scenariusz B):** —

### Jezioro Suszewskie

- **Średnia rozbieżność (ostatnie 12 miesięcy):** -442.6 cm
- **Trend rozbieżności:** -15.93 cm/rok
- **Szacunek odbudowy (scenariusz A, symmetric):** 27.8 lat
- **Szacunek odbudowy (scenariusz B, 5.0 cm/rok):** 88.5 lat

### Jezioro Wilczyńskie

- **Średnia rozbieżność (ostatnie 12 miesięcy):** -495.9 cm
- **Trend rozbieżności:** -19.29 cm/rok
- **Szacunek odbudowy (scenariusz A, symmetric):** 25.7 lat
- **Szacunek odbudowy (scenariusz B, 5.0 cm/rok):** 99.2 lat

---

## Wykresy projekcji odbudowy

Średnia 5 lat z sezonowymi wahaniami (opad i temperatura per miesiąc); projekcja do 2070 lub do zrównania z modelem.

### Jezioro Budzisławskie

![Odbudowa budzislawskie](odbudowa/odbudowa_budzislawskie.png)

### Jezioro Koziegłowskie

![Odbudowa kozieglowskie](odbudowa/odbudowa_kozieglowskie.png)

### Jezioro Kownackie

![Odbudowa kownackie](odbudowa/odbudowa_kownackie.png)

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