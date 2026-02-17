# Raport: Jezioro Ostrowskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Ostrowskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/ostrowskie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/ostrowskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

W niektórych miesiącach **model naturalny** może dawać prognozę gorszą (np. większy spadek poziomu lub mniejszy przyrost) niż model drenażowy – wynika to z tego, że był uczony tylko na danych sprzed drenażu i nie odzwierciedla aktualnego reżimu; model drenażowy jest dopasowany do okresu po zmianie reżimu.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 12.3 | 94.418 | 94.62 |
| zimny, normalny | 16.1 | 94.596 | 94.824 |
| zimny, wilgotny | 6.7 | 94.707 | 95.25 |
| normalny, suchy | 11.9 | 94.39 | 94.523 |
| normalny, normalny | 15.2 | 94.552 | 94.67 |
| normalny, wilgotny | 6.6 | 94.674 | 95.135 |
| ciepły, suchy | 11.2 | 94.341 | 94.433 |
| ciepły, normalny | 13.7 | 94.463 | 94.625 |
| ciepły, wilgotny | 6.3 | 94.613 | 94.76 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (94.68 m n.p.m.):
- **Model drenażowy:** 94.51 m n.p.m. – ubędzie 0.170 m (-17.0 cm)
- **Model naturalny (sprzed drenażu):** 94.713 m n.p.m. – przybędzie +0.033 m (+3.3 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.6 °C
- **Suma opadu (prognoza):** 487.0 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.170 m (-17.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.51 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.033 m (+3.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.713 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 12.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.262 m (-26.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.418 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.060 m (-6.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.62 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 16.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.084 m (-8.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.596 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.144 m (+14.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.824 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 6.7 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.027 m (+2.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.707 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.570 m (+57.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.25 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 11.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.290 m (-29.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.39 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.157 m (-15.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.523 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.128 m (-12.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.552 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.010 m (-1.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.67 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 6.6 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.006 m (-0.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.674 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.455 m (+45.5 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.135 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 11.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.339 m (-33.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.341 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.247 m (-24.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.433 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 13.7 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.217 m (-21.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.463 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.055 m (-5.5 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.625 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 6.3 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.067 m (-6.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.613 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.080 m (+8.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.76 m n.p.m.




*Wygenerowano: 2026-02-17 19:21*