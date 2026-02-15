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
| zimny, suchy | 12.3 | 92.942 | 93.149 |
| zimny, normalny | 16.1 | 93.019 | 93.249 |
| zimny, wilgotny | 6.7 | 93.235 | 93.34 |
| normalny, suchy | 11.9 | 92.784 | 93.075 |
| normalny, normalny | 15.2 | 92.902 | 93.196 |
| normalny, wilgotny | 6.6 | 93.046 | 93.271 |
| ciepły, suchy | 11.2 | 92.71 | 93.047 |
| ciepły, normalny | 13.7 | 92.824 | 93.172 |
| ciepły, wilgotny | 6.3 | 92.966 | 93.236 |

**Najbardziej prawdopodobny poziom na koniec stycznia 2027** (średnia ważona zmian miesięcznych według szans realizacji wszystkich wariantów). W stosunku do stanu na koniec stycznia 2026 (93.2357 m n.p.m.):
- **Model drenażowy:** 92.915 m n.p.m. – ubędzie 0.321 m (-32.1 cm)
- **Model naturalny (sprzed drenażu):** 93.182 m n.p.m. – ubędzie 0.054 m (-5.4 cm)


### najbardziej prawdopodobny

![Symulacja najbardziej prawdopodobny](symulacja_wariant_najbardziej_prawdopodobny.png)


- **Średnia ważona wszystkich wariantów (bez własnej szansy realizacji).**
- **Średnia temperatura roczna (prognoza):** 9.6 °C
- **Suma opadu (prognoza):** 487.0 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.321 m (-32.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.915 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.054 m (-5.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.182 m n.p.m.


### zimny, suchy

![Symulacja zimny, suchy](symulacja_wariant_zimny_suchy.png)


- **Szansa realizacji:** 12.3 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.294 m (-29.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.942 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.087 m (-8.7 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.149 m n.p.m.


### zimny, normalny

![Symulacja zimny, normalny](symulacja_wariant_zimny_normalny.png)


- **Szansa realizacji:** 16.1 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.217 m (-21.7 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.019 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.013 m (+1.3 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.249 m n.p.m.


### zimny, wilgotny

![Symulacja zimny, wilgotny](symulacja_wariant_zimny_wilgotny.png)


- **Szansa realizacji:** 6.7 %
- **Średnia temperatura roczna (prognoza):** 8.4 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.001 m (-0.1 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.235 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.104 m (+10.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.34 m n.p.m.


### normalny, suchy

![Symulacja normalny, suchy](symulacja_wariant_normalny_suchy.png)


- **Szansa realizacji:** 11.9 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.452 m (-45.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.784 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.161 m (-16.1 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.075 m n.p.m.


### normalny, normalny

![Symulacja normalny, normalny](symulacja_wariant_normalny_normalny.png)


- **Szansa realizacji:** 15.2 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.334 m (-33.4 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.902 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.040 m (-4.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.196 m n.p.m.


### normalny, wilgotny

![Symulacja normalny, wilgotny](symulacja_wariant_normalny_wilgotny.png)


- **Szansa realizacji:** 6.6 %
- **Średnia temperatura roczna (prognoza):** 9.7 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.190 m (-19.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 93.046 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.035 m (+3.5 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.271 m n.p.m.


### ciepły, suchy

![Symulacja ciepły, suchy](symulacja_wariant_cieply_suchy.png)


- **Szansa realizacji:** 11.2 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 336.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.526 m (-52.6 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.71 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.189 m (-18.9 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.047 m n.p.m.


### ciepły, normalny

![Symulacja ciepły, normalny](symulacja_wariant_cieply_normalny.png)


- **Szansa realizacji:** 13.7 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 510.9 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.412 m (-41.2 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.824 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): -0.064 m (-6.4 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.172 m n.p.m.


### ciepły, wilgotny

![Symulacja ciepły, wilgotny](symulacja_wariant_cieply_wilgotny.png)


- **Szansa realizacji:** 6.3 %
- **Średnia temperatura roczna (prognoza):** 10.9 °C
- **Suma opadu (prognoza):** 703.1 mm
- **Różnica poziomu wody (drenaż)** (koniec − start): -0.270 m (-27.0 cm)
- **Poziom na koniec stycznia 2027 (drenaż):** 92.966 m n.p.m.
- **Różnica poziomu wody (natural)** (koniec − start): +0.000 m (+0.0 cm)
- **Poziom na koniec stycznia 2027 (natural):** 93.236 m n.p.m.




*Wygenerowano: 2026-02-15 21:15*