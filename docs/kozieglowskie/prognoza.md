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
| zimny, suchy | 12.8 | 100.903 | 101.212 |
| zimny, normalny | 16.1 | 101.1 | 101.297 |
| zimny, wilgotny | 6.3 | 101.234 | 101.377 |
| normalny, suchy | 12.3 | 100.887 | 101.176 |
| normalny, normalny | 15.2 | 101.092 | 101.202 |
| normalny, wilgotny | 6.2 | 101.227 | 101.304 |
| ciepły, suchy | 11.5 | 100.876 | 100.954 |
| ciepły, normalny | 13.7 | 101.103 | 101.114 |
| ciepły, wilgotny | 6.0 | 101.217 | 101.211 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (101.0031 m n.p.m.):
- **Model drenażowy:** 101.046 m n.p.m. – przybędzie +0.043 m (+4.3 cm)
- **Model naturalny (sprzed drenażu):** 101.193 m n.p.m. – przybędzie +0.190 m (+19.0 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 490.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.043 m (+4.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.046 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.190 m (+19.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.193 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 12.8 %
- **Średnia temperatura roczna (prognoza):** 8.5 °C
- **Suma opadu (prognoza):** 338.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.100 m (-10.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.903 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.209 m (+20.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.212 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 16.1 %
- **Średnia temperatura roczna (prognoza):** 8.5 °C
- **Suma opadu (prognoza):** 517.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.097 m (+9.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.1 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.294 m (+29.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.297 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 6.3 %
- **Średnia temperatura roczna (prognoza):** 8.5 °C
- **Suma opadu (prognoza):** 720.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.231 m (+23.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.234 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.374 m (+37.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.377 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 12.3 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 338.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.116 m (-11.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.887 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.173 m (+17.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.176 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 517.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.089 m (+8.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.092 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.199 m (+19.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.202 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 6.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 720.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.224 m (+22.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.227 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.301 m (+30.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.304 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 338.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.127 m (-12.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 100.876 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.049 m (-4.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 100.954 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 13.7 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 517.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.100 m (+10.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.103 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.111 m (+11.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.114 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 6.0 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 720.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.214 m (+21.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.217 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.208 m (+20.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.211 m n.p.m.




*Wygenerowano: 2026-02-15 22:11*