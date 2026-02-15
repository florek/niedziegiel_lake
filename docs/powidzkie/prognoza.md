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
| zimny, suchy | 10.9 | 97.716 | 97.798 |
| zimny, normalny | 17.0 | 97.71 | 97.831 |
| zimny, wilgotny | 6.9 | 97.686 | 97.879 |
| normalny, suchy | 10.8 | 97.714 | 97.786 |
| normalny, normalny | 16.4 | 97.709 | 97.816 |
| normalny, wilgotny | 6.8 | 97.667 | 97.842 |
| ciepły, suchy | 10.2 | 97.682 | 97.794 |
| ciepły, normalny | 14.4 | 97.679 | 97.816 |
| ciepły, wilgotny | 6.6 | 97.657 | 97.844 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (97.7681 m n.p.m.):
- **Model drenażowy:** 97.695 m n.p.m. – ubędzie 0.073 m (-7.3 cm)
- **Model naturalny (sprzed drenażu):** 97.819 m n.p.m. – przybędzie +0.051 m (+5.1 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 474.0 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.073 m (-7.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.695 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.051 m (+5.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.819 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 10.9 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.052 m (-5.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.716 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.030 m (+3.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.798 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 17.0 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.058 m (-5.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.71 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.063 m (+6.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.831 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 6.9 %
- **Średnia temperatura roczna (prognoza):** 7.7 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.082 m (-8.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.686 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.111 m (+11.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.879 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 10.8 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.054 m (-5.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.714 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.018 m (+1.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.786 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 16.4 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.059 m (-5.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.709 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.048 m (+4.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.816 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 6.8 %
- **Średnia temperatura roczna (prognoza):** 9.1 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.101 m (-10.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.667 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.074 m (+7.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.842 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 10.2 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 322.2 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.086 m (-8.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.682 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.026 m (+2.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.794 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 14.4 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 486.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.089 m (-8.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.679 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.048 m (+4.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.816 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 6.6 %
- **Średnia temperatura roczna (prognoza):** 10.5 °C
- **Suma opadu (prognoza):** 683.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.111 m (-11.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 97.657 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.076 m (+7.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 97.844 m n.p.m.




*Wygenerowano: 2026-02-15 21:15*