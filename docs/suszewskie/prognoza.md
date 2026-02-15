# Raport: Jezioro Suszewskie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Suszewskie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/suszewskie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/suszewskie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

W niektórych miesiącach **model naturalny** może dawać prognozę gorszą (np. większy spadek poziomu lub mniejszy przyrost) niż model drenażowy – wynika to z tego, że był uczony tylko na danych sprzed drenażu i nie odzwierciedla aktualnego reżimu; model drenażowy jest dopasowany do okresu po zmianie reżimu.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 12.5 | 93.594 | 93.899 |
| zimny, normalny | 15.8 | 93.762 | 94.058 |
| zimny, wilgotny | 6.7 | 94.258 | 94.489 |
| normalny, suchy | 12.1 | 93.583 | 93.679 |
| normalny, normalny | 15.0 | 93.729 | 93.837 |
| normalny, wilgotny | 6.6 | 94.201 | 94.178 |
| ciepły, suchy | 11.3 | 93.517 | 93.452 |
| ciepły, normalny | 13.5 | 93.683 | 93.615 |
| ciepły, wilgotny | 6.4 | 93.974 | 93.886 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (93.7383 m n.p.m.):
- **Model drenażowy:** 93.752 m n.p.m. – przybędzie +0.014 m (+1.4 cm)
- **Model naturalny (sprzed drenażu):** 93.857 m n.p.m. – przybędzie +0.119 m (+11.9 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.6 °C
- **Suma opadu (prognoza):** 489.5 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.014 m (+1.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.752 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.119 m (+11.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.857 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 12.5 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 337.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.144 m (-14.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.594 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.161 m (+16.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.899 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 15.8 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 517.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.024 m (+2.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.762 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.320 m (+32.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.058 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 6.7 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 704.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.520 m (+52.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.258 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.751 m (+75.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.489 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 12.1 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 337.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.155 m (-15.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.583 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.059 m (-5.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.679 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 15.0 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 517.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.009 m (-0.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.729 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.099 m (+9.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.837 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 6.6 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 704.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.463 m (+46.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.201 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.440 m (+44.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.178 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 11.3 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 337.6 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.221 m (-22.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.517 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.286 m (-28.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.452 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 13.5 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 517.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.055 m (-5.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.683 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.123 m (-12.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.615 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 6.4 %
- **Średnia temperatura roczna (prognoza):** 11.0 °C
- **Suma opadu (prognoza):** 704.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.236 m (+23.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.974 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.148 m (+14.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.886 m n.p.m.




*Wygenerowano: 2026-02-15 21:15*