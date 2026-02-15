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
| zimny, suchy | 10.9 | 101.91 | 101.974 |
| zimny, normalny | 17.1 | 101.911 | 102.093 |
| zimny, wilgotny | 6.9 | 101.912 | 102.191 |
| normalny, suchy | 10.8 | 101.94 | 101.894 |
| normalny, normalny | 16.4 | 101.914 | 102.005 |
| normalny, wilgotny | 6.8 | 101.906 | 102.241 |
| ciepły, suchy | 10.2 | 101.9 | 101.854 |
| ciepły, normalny | 14.4 | 101.922 | 101.919 |
| ciepły, wilgotny | 6.6 | 101.901 | 102.239 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (101.89 m n.p.m.):
- **Model drenażowy:** 101.914 m n.p.m. – przybędzie +0.024 m (+2.4 cm)
- **Model naturalny (sprzed drenażu):** 102.021 m n.p.m. – przybędzie +0.131 m (+13.1 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 474.5 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.024 m (+2.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.914 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.131 m (+13.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 102.021 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 10.9 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.020 m (+2.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.91 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.084 m (+8.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.974 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 17.1 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.021 m (+2.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.911 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.203 m (+20.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 102.093 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 6.9 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.022 m (+2.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.912 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.301 m (+30.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 102.191 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.050 m (+5.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.94 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.004 m (+0.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.894 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 16.4 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.024 m (+2.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.914 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.115 m (+11.5 cm)
- **Poziom na koniec stycznia 2027 (natural):** 102.005 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 6.8 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.016 m (+1.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.906 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.351 m (+35.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 102.241 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 10.2 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.010 m (+1.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.9 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.036 m (-3.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.854 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 14.4 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.032 m (+3.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.922 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.029 m (+2.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 101.919 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 6.6 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.011 m (+1.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 101.901 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.349 m (+34.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 102.239 m n.p.m.




*Wygenerowano: 2026-02-15 22:27*