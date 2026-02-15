from pathlib import Path

import pandas as pd

import lake

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
METEO_PATH = DATA_DIR / "meteo.csv"
TARGET_YEAR = 2026
TARGET_MONTH = 1


def _load_meteo_dict(path: Path) -> dict[tuple[int, int], tuple[float, float]]:
    df = pd.read_csv(path, sep=",", decimal=".", encoding="utf-8")
    col_data = [c for c in df.columns if "data" in c.lower() or c.strip() == ""]
    col_data = col_data[0] if col_data else df.columns[0]
    col_opad = "opad" if "opad" in [c.lower() for c in df.columns] else df.columns[1]
    col_temp = "temperatura" if "temperatura" in [c.lower() for c in df.columns] else df.columns[2]
    out = {}
    for _, row in df.iterrows():
        raw = str(row[col_data]).strip()
        if not raw or raw.startswith("data"):
            continue
        part = raw.split("-")
        if len(part) != 2:
            continue
        try:
            month = int(part[0])
            year = int(part[1])
            opad = float(row[col_opad])
            temp = float(row[col_temp])
        except (ValueError, TypeError):
            continue
        out[(year, month)] = (opad, temp)
    return out


def _data_ostatniego_pomiaru(df: pd.DataFrame) -> tuple[int, int] | None:
    df_poziom = df.dropna(subset=[lake.COL_POZIOM])
    if df_poziom.empty:
        return None
    ostatni = df_poziom.sort_values(lake.COL_DATA).iloc[-1]
    dt = ostatni[lake.COL_DATA]
    return (int(dt.year), int(dt.month))


def _months_from_to(start_year: int, start_month: int, end_year: int, end_month: int) -> list[tuple[int, int]]:
    out = []
    y, m = start_year, start_month
    while (y, m) <= (end_year, end_month):
        out.append((y, m))
        m += 1
        if m > 12:
            m = 1
            y += 1
    return out


def _fmt_num(val: float) -> str:
    s = f"{val:.4f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _run_simulation_and_return_rows(
    lake_id: str,
    meteo_dict: dict[tuple[int, int], tuple[float, float]],
) -> list[dict] | None:
    data_path = lake.get_data_path(lake_id)
    model_path = lake.get_model_path(lake_id)
    if not data_path.exists() or not model_path.exists():
        return None
    df = lake.load_data(data_path)
    data_ost = _data_ostatniego_pomiaru(df)
    if data_ost is None:
        return None
    rok_ost, mies_ost = data_ost
    next_m = mies_ost + 1
    next_y = rok_ost if next_m <= 12 else rok_ost + 1
    if next_m > 12:
        next_m = 1
    months_sequence = _months_from_to(next_y, next_m, TARGET_YEAR, TARGET_MONTH)
    if not months_sequence:
        return []
    meteo_sequence = [meteo_dict.get((y, m)) for (y, m) in months_sequence]
    if any(x is None for x in meteo_sequence):
        return None
    model, feature_cols, lag_months, meteo_lag_months = lake.load_model(model_path)
    df["_ym"] = df[lake.COL_DATA].dt.year.astype(str) + "-" + df[lake.COL_DATA].dt.month.astype(str).str.zfill(2)
    ym_ost = f"{rok_ost}-{mies_ost:02d}"
    hist = df[df["_ym"] <= ym_ost].copy()
    if hist.empty:
        return None
    last_row = hist.iloc[-1]
    level = float(last_row[lake.COL_POZIOM])
    hist_tail = hist.tail(lag_months)
    last_changes = [float(hist_tail.iloc[i][lake.COL_ZMIANA]) for i in range(len(hist_tail))]
    last_poziomy = [float(hist_tail.iloc[i][lake.COL_POZIOM]) for i in range(len(hist_tail))]
    while len(last_changes) < lag_months:
        last_changes.insert(0, 0.0)
        last_poziomy.insert(0, level)
    meteo_tail = hist.tail(meteo_lag_months) if meteo_lag_months else []
    last_opady = [float(meteo_tail.iloc[i][lake.COL_OPAD]) for i in range(len(meteo_tail))] if meteo_lag_months else []
    last_temperatury = [float(meteo_tail.iloc[i][lake.COL_TEMPERATURA]) for i in range(len(meteo_tail))] if meteo_lag_months else []
    max_poziom, odplyw_m, przesaczanie_m = lake.get_drainage_params(lake_id, df)
    new_rows = []
    for (opad, temp), (year, month) in zip(meteo_sequence, months_sequence):
        pred = lake.predict_change(
            model,
            feature_cols,
            level,
            opad,
            temp,
            month,
            last_changes=last_changes,
            last_poziomy=last_poziomy,
            last_opady=last_opady if last_opady else None,
            last_temperatury=last_temperatury if last_temperatury else None,
            lag_months=lag_months,
            meteo_lag_months=meteo_lag_months,
        )
        poziom_start = level
        level = level + pred
        level = lake.apply_cap_and_drainage(level, max_poziom, odplyw_m, przesaczanie_m)
        new_rows.append({
            "data_str": f"01.{month:02d}.{year}",
            "poziom": poziom_start,
            "zmiana": pred,
            "opad": opad,
            "temperatura": temp,
        })
        last_changes = last_changes[1:] + [pred]
        last_poziomy = last_poziomy[1:] + [level]
        if meteo_lag_months:
            last_opady = (last_opady[1:] + [opad])[-meteo_lag_months:]
            last_temperatury = (last_temperatury[1:] + [temp])[-meteo_lag_months:]
    return new_rows


def _append_rows_to_data_csv(data_path: Path, new_rows: list[dict]) -> None:
    lines = data_path.read_text(encoding="utf-8").rstrip().splitlines()
    while lines and not lines[-1].strip():
        lines.pop()
    for row in new_rows:
        data_str = row["data_str"]
        line = f'{data_str},"{_fmt_num(row["poziom"])}","{_fmt_num(row["zmiana"])}","{_fmt_num(row["opad"])}","{_fmt_num(row["temperatura"])}"'
        lines.append(line)
    data_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    meteo_dict = _load_meteo_dict(METEO_PATH)
    if (TARGET_YEAR, TARGET_MONTH) not in meteo_dict:
        print(f"Brak danych meteo dla {TARGET_MONTH:02d}-{TARGET_YEAR} w {METEO_PATH}")
        return
    for lake_id in lake.LAKES:
        data_path = lake.get_data_path(lake_id)
        new_rows = _run_simulation_and_return_rows(lake_id, meteo_dict)
        nazwa = lake.LAKES.get(lake_id, lake_id)
        if new_rows is None:
            print(f"{nazwa}: brak modelu/danych lub brak meteo – pominięto")
            continue
        if not new_rows:
            print(f"{nazwa}: dane do {TARGET_MONTH:02d}.{TARGET_YEAR} już w pliku – bez dopisywania")
            continue
        _append_rows_to_data_csv(data_path, new_rows)
        miesiace = " – ".join(r["data_str"] for r in new_rows)
        print(f"{nazwa}: dopisano {len(new_rows)} miesięcy ({miesiace}) do {data_path}")


if __name__ == "__main__":
    main()
