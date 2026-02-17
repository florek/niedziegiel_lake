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
| zimny, suchy | 12.3 | 85.789 | 85.863 |
| zimny, normalny | 16.1 | 85.858 | 86.048 |
| zimny, wilgotny | 6.7 | 86.073 | 86.142 |
| normalny, suchy | 11.9 | 85.758 | 85.738 |
| normalny, normalny | 15.2 | 85.771 | 85.959 |
| normalny, wilgotny | 6.6 | 85.962 | 86.119 |
| ciepły, suchy | 11.2 | 85.649 | 85.698 |
| ciepły, normalny | 13.7 | 85.796 | 85.869 |
| ciepły, wilgotny | 6.3 | 85.92 | 86.065 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (85.76 m n.p.m.):
- **Model drenażowy:** 85.818 m n.p.m. – przybędzie +0.058 m (+5.8 cm)
- **Model naturalny (sprzed drenażu):** 85.923 m n.p.m. – przybędzie +0.163 m (+16.3 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.6 °C
- **Suma opadu (prognoza):** 487.0 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.058 m (+5.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.818 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.163 m (+16.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 85.923 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 12.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.029 m (+2.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.789 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.103 m (+10.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 85.863 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 16.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.098 m (+9.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.858 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.288 m (+28.8 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.048 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 6.7 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.313 m (+31.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 86.073 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.382 m (+38.2 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.142 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 11.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.002 m (-0.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.758 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.022 m (-2.2 cm)
- **Poziom na koniec stycznia 2027 (natural):** 85.738 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.011 m (+1.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.771 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.199 m (+19.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 85.959 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 6.6 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.202 m (+20.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.962 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.359 m (+35.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.119 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 11.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.111 m (-11.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.649 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.062 m (-6.2 cm)
- **Poziom na koniec stycznia 2027 (natural):** 85.698 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 13.7 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.036 m (+3.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.796 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.109 m (+10.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 85.869 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 6.3 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): +0.160 m (+16.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 85.92 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.305 m (+30.5 cm)
- **Poziom na koniec stycznia 2027 (natural):** 86.065 m n.p.m.




*Wygenerowano: 2026-02-17 19:21*