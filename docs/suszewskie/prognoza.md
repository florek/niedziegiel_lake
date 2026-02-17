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
| zimny, suchy | 6.4 | 93.037 | 93.983 |
| zimny, normalny | 8.1 | 93.593 | 94.063 |
| zimny, wilgotny | 8.3 | 94.079 | 94.106 |
| normalny, suchy | 8.9 | 92.917 | 93.951 |
| normalny, normalny | 11.5 | 93.331 | 94.03 |
| normalny, wilgotny | 11.9 | 95.696 | 94.064 |
| ciepły, suchy | 12.0 | 92.915 | 93.95 |
| ciepły, normalny | 16.2 | 93.316 | 94.034 |
| ciepły, wilgotny | 16.7 | 93.551 | 94.073 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (93.59 m n.p.m.):
- **Model drenażowy:** 93.624 m n.p.m. – przybędzie +0.034 m (+3.4 cm)
- **Model naturalny (sprzed drenażu):** 94.031 m n.p.m. – przybędzie +0.441 m (+44.1 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 10.0 °C
- **Suma opadu (prognoza):** 539.3 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.034 m (+3.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.624 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.441 m (+44.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.031 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 6.4 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 334.3 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.553 m (-55.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.037 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.393 m (+39.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.983 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 8.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 515.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.003 m (+0.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.593 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.473 m (+47.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.063 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 8.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 714.4 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.489 m (+48.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 94.079 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.516 m (+51.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.106 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 8.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 334.3 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.673 m (-67.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.917 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.361 m (+36.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.951 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 515.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.259 m (-25.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.331 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.440 m (+44.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.03 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 11.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 714.4 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +2.106 m (+210.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.696 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.474 m (+47.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.064 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 12.0 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 334.3 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.675 m (-67.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.915 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.360 m (+36.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.95 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 16.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 515.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.274 m (-27.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.316 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.444 m (+44.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.034 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 16.7 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 714.4 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.039 m (-3.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.551 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.483 m (+48.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.073 m n.p.m.




*Wygenerowano: 2026-02-17 19:21*