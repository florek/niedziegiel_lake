# Raport podsumowujący: prognoza zmiany poziomu Jezioro Budzisławskie

## 1. Cel projektu

Projekt ma na celu:
- zbudowanie **modelu uczenia maszynowego**, który na podstawie opadu i temperatury (oraz sezonowości i historii) prognozuje **miesięczną zmianę poziomu** Jezioro Budzisławskie;
- **ewaluację** prognoz względem rzeczywistych pomiarów.

---

## 2. Dane

- **Źródło:** plik `data/budzislawskie/data.csv`.
- **Zakres:** dane miesięczne (pierwszy dzień miesiąca).
- **Kolumny:** Data, Poziom (m), Zmiana (m), Opad (mm), Temperatura (°C).
- **Target:** Zmiana – miesięczna zmiana poziomu.
- Wiersze z błędami (#ERROR!) lub brakami są pomijane. Po usunięciu lagów (5 mies.) do analizy wchodzi **391** miesięcy.

---

## 3. Model

| Element | Opis |
|--------|------|
| Algorytm | Gradient Boosting (regresja), scikit-learn |
| Cechy wejściowe | Miesiąc (sin/cos), Opad, Temperatura, opad i temperatura z opóźnieniem 1–5 mies., 3 opóźnienia zmiany poziomu, 3 opóźnienia poziomu |
| Trening (od–do) | **Po drenażu:** uczony od 2011-01 do 2023-12. **Sprzed drenażu:** uczony od 1993 do 2002-12. |
| Wynik | Prognoza zmiany poziomu na dany miesiąc (cm) |

**Szczegóły – na czym uczony i testowany:**

- **Model drenażowy:** uczony na danych do 2023-12, testowany na danych od 2024 do 2025.

- **Model naturalny** (sprzed drenażu): uczony na danych do 2002-12, stosowany do porównań (wykresy rozbieżności, błąd miesięczny) na okresie od 1993 do 2025.

Model **nie** używa bieżącego poziomu – tylko opad, temperatura, sezon i historia.


---

## 4. Wyniki ewaluacji

- **MAE (średni błąd bezwzględny):** 3.23 cm
- **RMSE:** 5.05 cm
- **Liczba miesięcy:** 391

### 4.1. Wysokość wody: rzeczywista vs scenariusz modelowy

Scenariusz modelowy: start od poziomu na początek pierwszego miesiąca; w każdym miesiącu dodawana jest **prognozowana** zmiana (kumulatywnie).

![Wysokość rzeczywista vs model](wysokosc_rzeczywista_vs_model.png)

### 4.2. Rozbieżność w czasie

Rozbieżność = wysokość rzeczywista − wysokość w scenariuszu **modelu naturalnego (sprzed drenażu)**. Wartość dodatnia: jezioro wyżej niż przewidywał model naturalny; ujemna: niżej (np. efekt drenażu).

W **okresie treningowym** modelu naturalnego (na lewo od pionowej linii): średnia bezwzględna rozbieżność = **9.8 cm** (117 miesięcy). Linia pionowa = koniec treningu; po prawej = prognoza poza danymi treningowymi.

![Rozbieżność w czasie](rozbieznosc_w_czasie.png)

### 4.3. Zmiana poziomu: faktyczna vs prognoza (zbiór testowy)

Wykres obejmuje **tylko zbiór testowy** (dane, na których model nie był uczony). Punkty przy linii y = x oznaczają dobrą zgodność miesięcznych zmian.

![Zmiana faktyczna vs prognoza](zmiana_fakt_vs_prognoza.png)

### 4.4. Błąd miesięczny

Błąd = zmiana faktyczna − zmiana prognozowana w każdym miesiącu przez **model naturalny (sprzed drenażu)**.

![Błąd miesięczny](blad_miesieczny.png)

---

## 5. Podsumowanie

- Model prognozuje miesięczną zmianę poziomu Jezioro Budzisławskie z MAE ~3.23 cm.
- Scenariusz kumulatywny (wysokość z prognozowanej zmiany) jest porównywany z rzeczywistą wysokością; rozbieżność i błąd miesięczny opisują jakość prognoz.

Szczegóły techniczne: [model.md](../model.md), [podsumowanie_ewaluacji.md](podsumowanie_ewaluacji.md).

*Wygenerowano: 2026-02-17 19:20*
