# Raport: Jezioro Budzisławskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Budzisławskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/budzislawskie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/budzislawskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

W niektórych miesiącach **model naturalny** może dawać prognozę gorszą (np. większy spadek poziomu lub mniejszy przyrost) niż model drenażowy – wynika to z tego, że był uczony tylko na danych sprzed drenażu i nie odzwierciedla aktualnego reżimu; model drenażowy jest dopasowany do okresu po zmianie reżimu.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 4.0 | 95.133 | 95.291 |
| zimny, normalny | 8.9 | 95.237 | 95.32 |
| zimny, wilgotny | 11.7 | 95.385 | 95.408 |
| normalny, suchy | 4.9 | 95.089 | 95.237 |
| normalny, normalny | 11.7 | 95.182 | 95.269 |
| normalny, wilgotny | 16.1 | 95.351 | 95.359 |
| ciepły, suchy | 5.8 | 95.007 | 95.193 |
| ciepły, normalny | 15.0 | 95.104 | 95.213 |
| ciepły, wilgotny | 22.0 | 95.295 | 95.294 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (95.29 m n.p.m.):
- **Model drenażowy:** 95.234 m n.p.m. – ubędzie 0.056 m (-5.6 cm)
- **Model naturalny (sprzed drenażu):** 95.296 m n.p.m. – przybędzie +0.006 m (+0.6 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.9 °C
- **Suma opadu (prognoza):** 582.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.056 m (-5.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.234 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.006 m (+0.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.296 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 4.0 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 338.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.157 m (-15.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.133 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.001 m (+0.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.291 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 8.9 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 511.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.053 m (-5.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.237 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.030 m (+3.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.32 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 704.4 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.095 m (+9.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.385 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.118 m (+11.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.408 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 4.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 338.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.201 m (-20.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.089 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.053 m (-5.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.237 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 11.7 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 511.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.108 m (-10.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.182 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.021 m (-2.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.269 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 16.1 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 704.4 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.061 m (+6.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.351 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.069 m (+6.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.359 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 5.8 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 338.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.283 m (-28.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.007 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.097 m (-9.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.193 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 15.0 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 511.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.186 m (-18.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.104 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.077 m (-7.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.213 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 22.0 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 704.4 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.005 m (+0.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.295 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.004 m (+0.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.294 m n.p.m.




*Wygenerowano: 2026-02-17 19:20*