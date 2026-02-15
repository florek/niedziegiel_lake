# Raport: Jezioro Wilczyńskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Wilczyńskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/wilczynskie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/wilczynskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

W niektórych miesiącach **model naturalny** może dawać prognozę gorszą (np. większy spadek poziomu lub mniejszy przyrost) niż model drenażowy – wynika to z tego, że był uczony tylko na danych sprzed drenażu i nie odzwierciedla aktualnego reżimu; model drenażowy jest dopasowany do okresu po zmianie reżimu.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 12.3 | 93.975 | 93.978 |
| zimny, normalny | 16.1 | 94.097 | 94.315 |
| zimny, wilgotny | 6.7 | 94.458 | 94.541 |
| normalny, suchy | 11.9 | 93.867 | 93.784 |
| normalny, normalny | 15.2 | 93.996 | 94.01 |
| normalny, wilgotny | 6.6 | 94.234 | 94.322 |
| ciepły, suchy | 11.2 | 93.812 | 93.765 |
| ciepły, normalny | 13.7 | 93.901 | 93.965 |
| ciepły, wilgotny | 6.3 | 94.129 | 94.27 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (94.0036 m n.p.m.):
- **Model drenażowy:** 94.016 m n.p.m. – przybędzie +0.012 m (+1.2 cm)
- **Model naturalny (sprzed drenażu):** 94.067 m n.p.m. – przybędzie +0.063 m (+6.3 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.6 °C
- **Suma opadu (prognoza):** 487.0 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.012 m (+1.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.016 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.063 m (+6.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.067 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 12.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.029 m (-2.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.975 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.026 m (-2.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.978 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 16.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.093 m (+9.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.097 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.311 m (+31.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.315 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 6.7 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.454 m (+45.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.458 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.537 m (+53.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.541 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 11.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.137 m (-13.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.867 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.220 m (-22.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.784 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.008 m (-0.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.996 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.006 m (+0.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.01 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 6.6 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.230 m (+23.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.234 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.318 m (+31.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.322 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 11.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.192 m (-19.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.812 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.239 m (-23.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.765 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 13.7 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.103 m (-10.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.901 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.039 m (-3.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.965 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 6.3 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.125 m (+12.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.129 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.266 m (+26.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.27 m n.p.m.




*Wygenerowano: 2026-02-15 22:11*