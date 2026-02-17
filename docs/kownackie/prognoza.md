# Raport: Jezioro Kownackie

Raport ewaluacji na następne 12 miesięcy dla Jezioro Kownackie.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/kownackie/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/kownackie/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

W niektórych miesiącach **model naturalny** może dawać prognozę gorszą (np. większy spadek poziomu lub mniejszy przyrost) niż model drenażowy – wynika to z tego, że był uczony tylko na danych sprzed drenażu i nie odzwierciedla aktualnego reżimu; model drenażowy jest dopasowany do okresu po zmianie reżimu.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 6.4 | 92.917 | 93.072 |
| zimny, normalny | 8.0 | 93.007 | 93.237 |
| zimny, wilgotny | 8.3 | 93.109 | 93.434 |
| normalny, suchy | 8.9 | 92.868 | 93.066 |
| normalny, normalny | 11.5 | 92.964 | 93.218 |
| normalny, wilgotny | 11.9 | 93.057 | 93.403 |
| ciepły, suchy | 12.1 | 92.849 | 93.026 |
| ciepły, normalny | 16.1 | 92.951 | 93.148 |
| ciepły, wilgotny | 16.8 | 93.05 | 93.324 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (93.25 m n.p.m.):
- **Model drenażowy:** 92.978 m n.p.m. – ubędzie 0.272 m (-27.2 cm)
- **Model naturalny (sprzed drenażu):** 93.22 m n.p.m. – ubędzie 0.030 m (-3.0 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.9 °C
- **Suma opadu (prognoza):** 538.3 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.272 m (-27.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.978 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.030 m (-3.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.22 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 6.4 %
- **Średnia temperatura roczna (prognoza):** 8.3 °C
- **Suma opadu (prognoza):** 336.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.333 m (-33.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.917 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.178 m (-17.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.072 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 8.0 %
- **Średnia temperatura roczna (prognoza):** 8.3 °C
- **Suma opadu (prognoza):** 511.5 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.243 m (-24.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.007 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.013 m (-1.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.237 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 8.3 %
- **Średnia temperatura roczna (prognoza):** 8.3 °C
- **Suma opadu (prognoza):** 713.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.141 m (-14.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.109 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.184 m (+18.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.434 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 8.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.382 m (-38.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.868 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.184 m (-18.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.066 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 511.5 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.286 m (-28.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.964 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.032 m (-3.2 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.218 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 11.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 713.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.193 m (-19.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.057 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.153 m (+15.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.403 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 12.1 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.401 m (-40.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.849 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.224 m (-22.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.026 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 16.1 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 511.5 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.299 m (-29.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.951 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.102 m (-10.2 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.148 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 16.8 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 713.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.200 m (-20.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.05 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.074 m (+7.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.324 m n.p.m.




*Wygenerowano: 2026-02-17 19:21*