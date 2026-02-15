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
| zimny, suchy | 12.3 | 94.505 | 94.451 |
| zimny, normalny | 16.1 | 94.552 | 94.765 |
| zimny, wilgotny | 6.7 | 94.6 | 95.206 |
| normalny, suchy | 11.9 | 94.454 | 94.396 |
| normalny, normalny | 15.2 | 94.493 | 94.589 |
| normalny, wilgotny | 6.6 | 94.544 | 94.953 |
| ciepły, suchy | 11.2 | 94.41 | 94.357 |
| ciepły, normalny | 13.7 | 94.441 | 94.568 |
| ciepły, wilgotny | 6.3 | 94.513 | 94.839 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (94.6849 m n.p.m.):
- **Model drenażowy:** 94.495 m n.p.m. – ubędzie 0.190 m (-19.0 cm)
- **Model naturalny (sprzed drenażu):** 94.63 m n.p.m. – ubędzie 0.055 m (-5.5 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.6 °C
- **Suma opadu (prognoza):** 487.0 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.190 m (-19.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.495 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.055 m (-5.5 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.63 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 12.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.180 m (-18.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.505 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.234 m (-23.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.451 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 16.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.133 m (-13.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.552 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.080 m (+8.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.765 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 6.7 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.085 m (-8.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.6 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.521 m (+52.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.206 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 11.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.231 m (-23.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.454 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.289 m (-28.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.396 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.192 m (-19.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.493 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.096 m (-9.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.589 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 6.6 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.141 m (-14.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.544 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.268 m (+26.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.953 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 11.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.275 m (-27.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.41 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.328 m (-32.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.357 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 13.7 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.244 m (-24.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.441 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.117 m (-11.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.568 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 6.3 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.172 m (-17.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.513 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.154 m (+15.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.839 m n.p.m.




*Wygenerowano: 2026-02-15 22:11*