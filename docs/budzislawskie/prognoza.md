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
| zimny, suchy | 12.3 | 95.822 | 96.066 |
| zimny, normalny | 16.1 | 95.833 | 96.091 |
| zimny, wilgotny | 6.7 | 95.875 | 96.172 |
| normalny, suchy | 11.9 | 95.662 | 96.048 |
| normalny, normalny | 15.2 | 95.698 | 96.073 |
| normalny, wilgotny | 6.6 | 95.875 | 96.157 |
| ciepły, suchy | 11.2 | 95.666 | 95.999 |
| ciepły, normalny | 13.7 | 95.725 | 96.029 |
| ciepły, wilgotny | 6.3 | 95.738 | 96.116 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (96.0461 m n.p.m.):
- **Model drenażowy:** 95.757 m n.p.m. – ubędzie 0.289 m (-28.9 cm)
- **Model naturalny (sprzed drenażu):** 96.073 m n.p.m. – przybędzie +0.027 m (+2.7 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.6 °C
- **Suma opadu (prognoza):** 487.0 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.289 m (-28.9 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.757 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.027 m (+2.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.073 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 12.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.224 m (-22.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.822 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.020 m (+2.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.066 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 16.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.213 m (-21.3 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.833 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.045 m (+4.5 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.091 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 6.7 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.171 m (-17.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.875 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.126 m (+12.6 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.172 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 11.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.384 m (-38.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.662 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.002 m (+0.2 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.048 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.348 m (-34.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.698 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.027 m (+2.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.073 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 6.6 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.171 m (-17.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.875 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.111 m (+11.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.157 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 11.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.380 m (-38.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.666 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.047 m (-4.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 95.999 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 13.7 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.321 m (-32.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.725 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.017 m (-1.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.029 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 6.3 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.308 m (-30.8 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 95.738 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.070 m (+7.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 96.116 m n.p.m.




*Wygenerowano: 2026-02-15 22:11*