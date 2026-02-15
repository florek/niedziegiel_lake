# Raport podsumowujący: prognoza zmiany poziomu Jezioro Powidzkie

## 1. Cel projektu

Projekt ma na celu:
- zbudowanie **modelu uczenia maszynowego**, który na podstawie opadu i temperatury (oraz sezonowości i historii) prognozuje **miesięczną zmianę poziomu** Jezioro Powidzkie;
- **ewaluację** prognoz względem rzeczywistych pomiarów.

---

## 2. Dane

- **Źródło:** plik `data/powidzkie/data.csv`.
- **Zakres:** dane miesięczne (pierwszy dzień miesiąca).
- **Kolumny:** Data, Poziom (m), Zmiana (m), Opad (mm), Temperatura (°C).
- **Target:** Zmiana – miesięczna zmiana poziomu.
- Wiersze z błędami (#ERROR!) lub brakami są pomijane. Po usunięciu lagów (5 mies.) do analizy wchodzi **570** miesięcy.

---

## 3. Model

| Element | Opis |
|--------|------|
| Algorytm | Gradient Boosting (regresja), scikit-learn |
| Cechy wejściowe | Miesiąc (sin/cos), Opad, Temperatura, opad i temperatura z opóźnieniem 1–3 mies., 5 opóźnienia zmiany poziomu, 5 opóźnienia poziomu |
| Trening | Podział czasowy: trening do roku 2013, test od 2014 do 2023 |
| Wynik | Prognoza zmiany poziomu na dany miesiąc (cm) |

Model **nie** używa bieżącego poziomu – tylko opad, temperatura, sezon i historia.

---

## 4. Wyniki ewaluacji

- **MAE (średni błąd bezwzględny):** 1.76 cm
- **RMSE:** 2.23 cm
- **Liczba miesięcy:** 570

### 4.1. Wysokość wody: rzeczywista vs scenariusz modelowy

Scenariusz modelowy: start od poziomu na początek pierwszego miesiąca; w każdym miesiącu dodawana jest **prognozowana** zmiana (kumulatywnie).

![Wysokość rzeczywista vs model](wysokosc_rzeczywista_vs_model.png)

### 4.2. Rozbieżność w czasie

Rozbieżność = wysokość rzeczywista − wysokość w scenariuszu modelowym. Wartość dodatnia: jezioro wyżej niż przewidywał model; ujemna: niżej.

![Rozbieżność w czasie](rozbieznosc_w_czasie.png)

### 4.3. Zmiana poziomu: faktyczna vs prognoza

Punkty przy linii y = x oznaczają dobrą zgodność miesięcznych zmian.

![Zmiana faktyczna vs prognoza](zmiana_fakt_vs_prognoza.png)

### 4.4. Błąd miesięczny

Błąd = zmiana faktyczna − zmiana prognozowana w każdym miesiącu.

![Błąd miesięczny](blad_miesieczny.png)

---

## 5. Podsumowanie

- Model prognozuje miesięczną zmianę poziomu Jezioro Powidzkie z MAE ~1.76 cm.
- Scenariusz kumulatywny (wysokość z prognozowanej zmiany) jest porównywany z rzeczywistą wysokością; rozbieżność i błąd miesięczny opisują jakość prognoz.

Szczegóły techniczne: [model.md](../model.md), [podsumowanie_ewaluacji.md](podsumowanie_ewaluacji.md).

*Wygenerowano: 2026-02-15 11:28*
