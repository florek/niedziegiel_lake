# Raport: Jezioro Skulska Wieś

Raport ewaluacji na następne 12 miesięcy dla Jezioro Skulska Wieś.

## Poziom wody: rzeczywisty pomiar i model

Niebieska: poziom z `data/skulskawies/data.csv`. Pomarańczowa przerywana: model po zmianie reżimu (trening do daty optymalnej po drenażu). Zielona kropkowana: model naturalny (trening do końca roku przed pojawieniem się drenażu).

![Poziom wody – pomiar i model](poziom_rzeczywisty.png)

## Prognoza 12 mies.

Dla każdego wariantu (temperatura: zimny/normalny/ciepły × opad: suchy/normalny/wilgotny) opad i temperatura z percentyli historycznych w `data/skulskawies/data.csv`. Symulacja: 12 miesięcy do końca stycznia 2027 (stan na koniec stycznia 2026 to pomiar rzeczywisty). Wykresy i tabele: oba modele (drenażowy i naturalny – sprzed drenażu) na wspólnych wykresach i w jednej tabeli na wariant.

W niektórych miesiącach **model naturalny** może dawać prognozę gorszą (np. większy spadek poziomu lub mniejszy przyrost) niż model drenażowy – wynika to z tego, że był uczony tylko na danych sprzed drenażu i nie odzwierciedla aktualnego reżimu; model drenażowy jest dopasowany do okresu po zmianie reżimu.

**Szansa realizacji** (na podstawie zgodności z ostatnimi 12 miesiącami pomiarowymi – średni opad i temperatura):

| Wariant | Szansa (%) | Poziom koniec – drenaż (m) | Poziom koniec – natural (m) |
|---------|------------|-----------------------------|------------------------------|
| zimny, suchy | 12.3 | 85.718 | 86.056 |
| zimny, normalny | 16.1 | 85.978 | 86.094 |
| zimny, wilgotny | 6.7 | 86.189 | 86.08 |
| normalny, suchy | 11.9 | 85.478 | 85.911 |
| normalny, normalny | 15.2 | 85.811 | 86.089 |
| normalny, wilgotny | 6.6 | 86.164 | 86.088 |
| ciepły, suchy | 11.2 | 85.4 | 85.985 |
| ciepły, normalny | 13.7 | 85.749 | 86.028 |
| ciepły, wilgotny | 6.3 | 86.133 | 86.094 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (85.758 m n.p.m.):
- **Model drenażowy:** 85.802 m n.p.m. – przybędzie +0.044 m (+4.4 cm)
- **Model naturalny (sprzed drenażu):** 86.044 m n.p.m. – przybędzie +0.286 m (+28.6 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.6 °C
- **Suma opadu (prognoza):** 487.0 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.044 m (+4.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.802 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.286 m (+28.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.044 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 12.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.040 m (-4.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.718 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.298 m (+29.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.056 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 16.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.220 m (+22.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.978 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.336 m (+33.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.094 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 6.7 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.431 m (+43.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 86.189 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.322 m (+32.2 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.08 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 11.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.280 m (-28.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.478 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.153 m (+15.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 85.911 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.053 m (+5.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.811 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.331 m (+33.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.089 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 6.6 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.406 m (+40.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 86.164 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.330 m (+33.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.088 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 11.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.358 m (-35.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.4 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.227 m (+22.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 85.985 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 13.7 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.009 m (-0.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.749 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.270 m (+27.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.028 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 6.3 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.375 m (+37.5 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 86.133 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.336 m (+33.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.094 m n.p.m.




*Wygenerowano: 2026-02-15 22:11*