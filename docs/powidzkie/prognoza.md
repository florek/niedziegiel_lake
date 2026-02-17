# Raport: Jezioro Powidzkie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Powidzkie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/powidzkie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/powidzkie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

W niektórych miesiącach **model naturalny** może dawać prognozę gorszą (np. większy spadek poziomu lub mniejszy przyrost) niż model drenażowy – wynika to z tego, że był uczony tylko na danych sprzed drenażu i nie odzwierciedla aktualnego reżimu; model drenażowy jest dopasowany do okresu po zmianie reżimu.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 3.9 | 97.381 | 97.135 |
| zimny, normalny | 8.2 | 97.504 | 97.304 |
| zimny, wilgotny | 11.7 | 97.656 | 97.497 |
| normalny, suchy | 4.9 | 97.348 | 97.094 |
| normalny, normalny | 11.0 | 97.481 | 97.256 |
| normalny, wilgotny | 16.7 | 97.635 | 97.461 |
| ciepły, suchy | 5.9 | 97.324 | 96.986 |
| ciepły, normalny | 14.3 | 97.46 | 97.144 |
| ciepły, wilgotny | 23.4 | 97.633 | 97.362 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (97.39 m n.p.m.):
- **Model drenażowy:** 97.542 m n.p.m. – przybędzie +0.152 m (+15.2 cm)
- **Model naturalny (sprzed drenażu):** 97.302 m n.p.m. – ubędzie 0.088 m (-8.8 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.4 °C
- **Suma opadu (prognoza):** 565.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.152 m (+15.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.542 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.088 m (-8.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.302 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 3.9 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 324.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.009 m (-0.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.381 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.255 m (-25.5 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.135 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 8.2 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.114 m (+11.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.504 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.086 m (-8.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.304 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 684.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.266 m (+26.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.656 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.107 m (+10.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.497 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 4.9 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 324.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.042 m (-4.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.348 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.296 m (-29.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.094 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 11.0 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.091 m (+9.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.481 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.134 m (-13.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.256 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 16.7 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 684.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.245 m (+24.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.635 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.071 m (+7.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.461 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 5.9 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 324.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.066 m (-6.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.324 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.404 m (-40.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.986 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 14.3 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.070 m (+7.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.46 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.246 m (-24.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.144 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 23.4 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 684.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.243 m (+24.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.633 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.028 m (-2.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.362 m n.p.m.




*Wygenerowano: 2026-02-17 19:21*