# Raport: Jezioro Koziegłowskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Koziegłowskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/kozieglowskie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/kozieglowskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

W niektórych miesiącach **model naturalny** może dawać prognozę gorszą (np. większy spadek poziomu lub mniejszy przyrost) niż model drenażowy – wynika to z tego, że był uczony tylko na danych sprzed drenażu i nie odzwierciedla aktualnego reżimu; model drenażowy jest dopasowany do okresu po zmianie reżimu.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 6.4 | 100.656 | 100.964 |
| zimny, normalny | 8.1 | 100.739 | 101.217 |
| zimny, wilgotny | 8.2 | 100.84 | 101.286 |
| normalny, suchy | 9.0 | 100.607 | 100.939 |
| normalny, normalny | 11.7 | 100.712 | 101.167 |
| normalny, wilgotny | 11.9 | 100.807 | 101.231 |
| ciepły, suchy | 12.0 | 100.574 | 100.931 |
| ciepły, normalny | 16.2 | 100.666 | 101.177 |
| ciepły, wilgotny | 16.5 | 100.775 | 101.246 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (100.68 m n.p.m.):
- **Model drenażowy:** 100.71 m n.p.m. – przybędzie +0.030 m (+3.0 cm)
- **Model naturalny (sprzed drenażu):** 101.141 m n.p.m. – przybędzie +0.461 m (+46.1 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 10.0 °C
- **Suma opadu (prognoza):** 546.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.030 m (+3.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.71 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.461 m (+46.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.141 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 6.4 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 337.4 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.024 m (-2.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.656 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.284 m (+28.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 100.964 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 8.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 522.8 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.059 m (+5.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.739 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.537 m (+53.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.217 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 8.2 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 727.5 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.160 m (+16.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.84 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.606 m (+60.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.286 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 9.0 %
- **Średnia temperatura roczna (prognoza):** 9.8 °C
- **Suma opadu (prognoza):** 337.4 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.073 m (-7.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.607 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.259 m (+25.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 100.939 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 9.8 °C
- **Suma opadu (prognoza):** 522.8 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.032 m (+3.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.712 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.487 m (+48.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.167 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 11.9 %
- **Średnia temperatura roczna (prognoza):** 9.8 °C
- **Suma opadu (prognoza):** 727.5 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.127 m (+12.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.807 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.551 m (+55.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.231 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 12.0 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 337.4 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.106 m (-10.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.574 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.251 m (+25.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 100.931 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 16.2 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 522.8 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.014 m (-1.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.666 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.497 m (+49.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.177 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 16.5 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 727.5 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.095 m (+9.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.775 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.566 m (+56.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.246 m n.p.m.




*Wygenerowano: 2026-02-17 19:21*