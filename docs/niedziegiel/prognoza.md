# Raport: Jezioro Niedzięgiel

Raport ewaluacji na następne 12 miesięcy dla Jezioro Niedzięgiel.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/niedziegiel/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/niedziegiel/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

W niektórych miesiącach **model naturalny** może dawać prognozę gorszą (np. większy spadek poziomu lub mniejszy przyrost) niż model drenażowy – wynika to z tego, że był uczony tylko na danych sprzed drenażu i nie odzwierciedla aktualnego reżimu; model drenażowy jest dopasowany do okresu po zmianie reżimu.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 3.9 | 101.735 | 101.654 |
| zimny, normalny | 8.2 | 101.762 | 101.807 |
| zimny, wilgotny | 11.7 | 101.819 | 102.001 |
| normalny, suchy | 4.9 | 101.727 | 101.597 |
| normalny, normalny | 11.0 | 101.754 | 101.729 |
| normalny, wilgotny | 16.7 | 101.809 | 101.923 |
| ciepły, suchy | 5.9 | 101.717 | 101.479 |
| ciepły, normalny | 14.3 | 101.741 | 101.601 |
| ciepły, wilgotny | 23.4 | 101.795 | 101.81 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (101.84 m n.p.m.):
- **Model drenażowy:** 101.775 m n.p.m. – ubędzie 0.065 m (-6.5 cm)
- **Model naturalny (sprzed drenażu):** 101.776 m n.p.m. – ubędzie 0.064 m (-6.4 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.4 °C
- **Suma opadu (prognoza):** 565.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.065 m (-6.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.775 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.064 m (-6.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.776 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 3.9 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 324.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.105 m (-10.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.735 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.186 m (-18.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.654 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 8.2 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.078 m (-7.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.762 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.033 m (-3.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.807 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 684.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.021 m (-2.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.819 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.161 m (+16.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 102.001 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 4.9 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 324.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.113 m (-11.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.727 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.243 m (-24.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.597 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 11.0 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.086 m (-8.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.754 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.111 m (-11.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.729 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 16.7 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 684.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.031 m (-3.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.809 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.083 m (+8.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.923 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 5.9 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 324.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.123 m (-12.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.717 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.361 m (-36.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.479 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 14.3 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.099 m (-9.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.741 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.239 m (-23.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.601 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 23.4 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 684.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.045 m (-4.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.795 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.030 m (-3.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.81 m n.p.m.




*Wygenerowano: 2026-02-17 19:21*