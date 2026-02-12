# Raport podsumowujący: prognoza zmiany poziomu Jezioro Niedzięgiel

## 1. Cel projektu

Projekt ma na celu:
- zbudowanie **modelu uczenia maszynowego**, który na podstawie opadu i temperatury (oraz sezonowości i historii) prognozuje **miesięczną zmianę poziomu** Jezioro Niedzięgiel;
- **ewaluację** prognoz względem rzeczywistych pomiarów.

---

## 2. Dane

- **Źródło:** plik `data/niedziegiel_data.csv`.
- **Zakres:** dane miesięczne (pierwszy dzień miesiąca).
- **Kolumny:** Data, Poziom (m), Zmiana (m), Opad (mm), Temperatura (°C).
- **Target:** Zmiana – miesięczna zmiana poziomu.
- Wiersze z błędami (#ERROR!) lub brakami są pomijane. Po usunięciu lagów (3 miesiące) do analizy wchodzi **343** miesięcy.

---

## 3. Model

| Element | Opis |
|--------|------|
| Algorytm | Gradient Boosting (regresja), scikit-learn |
| Cechy wejściowe | Miesiąc (sin/cos), Opad, Temperatura, 3 opóźnienia zmiany poziomu, 3 opóźnienia poziomu |
| Trening | Podział czasowy: ostatnie 70 miesięcy = zbiór testowy |
| Wynik | Prognoza zmiany poziomu na dany miesiąc (m) |

Model **nie** używa bieżącego poziomu – tylko opad, temperatura, sezon i historia.

---

## 4. Wyniki ewaluacji

- **MAE (średni błąd bezwzględny):** 0.0111 m (~1.11 cm)
- **RMSE:** 0.0157 m
- **Liczba miesięcy:** 343

### 4.1. Wysokość wody: rzeczywista vs scenariusz modelowy

Scenariusz modelowy: start od poziomu na początek pierwszego miesiąca; w każdym miesiącu dodawana jest **prognozowana** zmiana (kumulatywnie).

![Wysokość rzeczywista vs model](figures_niedziegiel/wysokosc_rzeczywista_vs_model.png)

### 4.2. Rozbieżność w czasie

Rozbieżność = wysokość rzeczywista − wysokość w scenariuszu modelowym. Wartość dodatnia: jezioro wyżej niż przewidywał model; ujemna: niżej.

![Rozbieżność w czasie](figures_niedziegiel/rozbieznosc_w_czasie.png)

### 4.3. Zmiana poziomu: faktyczna vs prognoza

Punkty przy linii y = x oznaczają dobrą zgodność miesięcznych zmian.

![Zmiana faktyczna vs prognoza](figures_niedziegiel/zmiana_fakt_vs_prognoza.png)

### 4.4. Błąd miesięczny

Błąd = zmiana faktyczna − zmiana prognozowana w każdym miesiącu.

![Błąd miesięczny](figures_niedziegiel/blad_miesieczny.png)

---

## 5. Podsumowanie

- Model prognozuje miesięczną zmianę poziomu Jezioro Niedzięgiel z MAE ~1.11 cm.
- Scenariusz kumulatywny (wysokość z prognozowanej zmiany) jest porównywany z rzeczywistą wysokością; rozbieżność i błąd miesięczny opisują jakość prognoz.

Szczegóły techniczne: [model.md](model.md), [podsumowanie_ewaluacji_niedziegiel.md](podsumowanie_ewaluacji_niedziegiel.md).
