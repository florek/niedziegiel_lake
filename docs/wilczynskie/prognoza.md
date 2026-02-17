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
| zimny, suchy | 6.4 | 92.774 | 92.789 |
| zimny, normalny | 8.0 | 93.031 | 93.218 |
| zimny, wilgotny | 8.3 | 93.392 | 94.151 |
| normalny, suchy | 8.9 | 92.628 | 92.751 |
| normalny, normalny | 11.5 | 92.858 | 93.206 |
| normalny, wilgotny | 11.9 | 93.137 | 93.975 |
| ciepły, suchy | 12.1 | 92.595 | 92.63 |
| ciepły, normalny | 16.1 | 92.836 | 93.086 |
| ciepły, wilgotny | 16.8 | 93.087 | 93.572 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (93.18 m n.p.m.):
- **Model drenażowy:** 92.927 m n.p.m. – ubędzie 0.253 m (-25.3 cm)
- **Model naturalny (sprzed drenażu):** 93.282 m n.p.m. – przybędzie +0.102 m (+10.2 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.9 °C
- **Suma opadu (prognoza):** 538.3 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.253 m (-25.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.927 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.102 m (+10.2 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.282 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 6.4 %
- **Średnia temperatura roczna (prognoza):** 8.3 °C
- **Suma opadu (prognoza):** 336.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.406 m (-40.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.774 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.391 m (-39.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 92.789 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 8.0 %
- **Średnia temperatura roczna (prognoza):** 8.3 °C
- **Suma opadu (prognoza):** 511.5 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.149 m (-14.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.031 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.038 m (+3.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.218 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 8.3 %
- **Średnia temperatura roczna (prognoza):** 8.3 °C
- **Suma opadu (prognoza):** 713.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.212 m (+21.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.392 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.971 m (+97.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 94.151 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 8.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.552 m (-55.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.628 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.429 m (-42.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 92.751 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 11.5 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 511.5 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.322 m (-32.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.858 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.026 m (+2.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.206 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 11.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 713.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.043 m (-4.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.137 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.795 m (+79.5 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.975 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 12.1 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.585 m (-58.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.595 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.550 m (-55.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 92.63 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 16.1 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 511.5 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.344 m (-34.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.836 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.094 m (-9.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.086 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 16.8 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 713.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.093 m (-9.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.087 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.392 m (+39.2 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.572 m n.p.m.




*Wygenerowano: 2026-02-17 19:21*