# Raport podsumowujący: prognoza zmiany poziomu Jezioro Niedzięgiel

## 1. Cel projektu

Projekt ma na celu:
- zbudowanie **modelu uczenia maszynowego**, który na podstawie opadu i temperatury (oraz sezonowości i historii) prognozuje **miesięczną zmianę poziomu** Jezioro Niedzięgiel;
- **ewaluację** prognoz względem rzeczywistych pomiarów.

---

## 2. Dane

- **Źródło:** plik `data/niedziegiel/data.csv`.
- **Zakres:** dane miesięczne (pierwszy dzień miesiąca).
- **Kolumny:** Data, Poziom (m), Zmiana (m), Opad (mm), Temperatura (°C).
- **Target:** Zmiana – miesięczna zmiana poziomu.
- Wiersze z błędami (#ERROR!) lub brakami są pomijane. Po usunięciu lagów (3 mies.) do analizy wchodzi **598** miesięcy.

---

## 3. Model

| Element | Opis |
|--------|------|
| Algorytm | Gradient Boosting (regresja), scikit-learn |
| Cechy wejściowe | Miesiąc (sin/cos), Opad, Temperatura, 3 opóźnienia zmiany poziomu, 3 opóźnienia poziomu |
| Trening (od–do) | **Po drenażu:** uczony od 2018-01 do 2023-12. **Sprzed drenażu:** uczony od 1976 do 2018-12. |
| Wynik | Prognoza zmiany poziomu na dany miesiąc (cm) |

Model **nie** używa bieżącego poziomu – tylko opad, temperatura, sezon i historia.


---

## 4. Wyniki ewaluacji

- **MAE (średni błąd bezwzględny):** nan cm
- **RMSE:** nan cm
- **Liczba miesięcy:** 598

### 4.1. Wysokość wody: rzeczywista vs scenariusz modelowy

Scenariusz modelowy: start od poziomu na początek pierwszego miesiąca; w każdym miesiącu dodawana jest **prognozowana** zmiana (kumulatywnie).

![Wysokość rzeczywista vs model](wysokosc_rzeczywista_vs_model.png)

### 4.2. Rozbieżność w czasie

Rozbieżność = wysokość rzeczywista − wysokość w scenariuszu **modelu naturalnego (sprzed drenażu)**. Wartość dodatnia: jezioro wyżej niż przewidywał model naturalny; ujemna: niżej (np. efekt drenażu).

![Rozbieżność w czasie](rozbieznosc_w_czasie.png)

### 4.3. Zmiana poziomu: faktyczna vs prognoza

Punkty przy linii y = x oznaczają dobrą zgodność miesięcznych zmian.

![Zmiana faktyczna vs prognoza](zmiana_fakt_vs_prognoza.png)

### 4.4. Błąd miesięczny

Błąd = zmiana faktyczna − zmiana prognozowana w każdym miesiącu przez **model naturalny (sprzed drenażu)**.

![Błąd miesięczny](blad_miesieczny.png)

---

## 5. Podsumowanie

- Model prognozuje miesięczną zmianę poziomu Jezioro Niedzięgiel z MAE ~nan cm.
- Scenariusz kumulatywny (wysokość z prognozowanej zmiany) jest porównywany z rzeczywistą wysokością; rozbieżność i błąd miesięczny opisują jakość prognoz.

Szczegóły techniczne: [model.md](../model.md), [podsumowanie_ewaluacji.md](podsumowanie_ewaluacji.md).

*Wygenerowano: 2026-02-15 16:13*
