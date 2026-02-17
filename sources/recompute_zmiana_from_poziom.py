import sys
from pathlib import Path

import pandas as pd

import lake

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"


def _to_num(ser):
    return pd.to_numeric(ser.astype(str).str.replace(",", ".", regex=False), errors="coerce")


def _process_file(path: Path) -> tuple[int, int]:
    df = pd.read_csv(path, sep=",", decimal=",", encoding="utf-8")
    df[lake.COL_DATA] = pd.to_datetime(df[lake.COL_DATA], format="%d.%m.%Y", dayfirst=True)
    df = df.sort_values(lake.COL_DATA).reset_index(drop=True)
    df[lake.COL_POZIOM] = _to_num(df[lake.COL_POZIOM])
    df = df.dropna(subset=[lake.COL_POZIOM])
    if len(df) < 2:
        return 0, 0
    zmiana_old = df[lake.COL_ZMIANA].copy()
    if lake.COL_ZMIANA in df.columns:
        df[lake.COL_ZMIANA] = df[lake.COL_POZIOM].diff().round(4)
        df.loc[df.index[0], lake.COL_ZMIANA] = 0.0
    try:
        zmiana_old_num = _to_num(zmiana_old)
        diff_count = (abs(zmiana_old_num - df[lake.COL_ZMIANA]) > 1e-6).sum()
    except Exception:
        diff_count = len(df)
    for col in (lake.COL_OPAD, lake.COL_TEMPERATURA):
        if col in df.columns:
            df[col] = _to_num(df[col])
    df[lake.COL_POZIOM] = df[lake.COL_POZIOM].round(2)
    df[lake.COL_ZMIANA] = df[lake.COL_ZMIANA].round(4)
    df[lake.COL_DATA] = df[lake.COL_DATA].dt.strftime("%d.%m.%Y")
    df.to_csv(path, index=False, encoding="utf-8", sep=",", decimal=",")
    return len(df), int(diff_count)


def main():
    lake_ids = sys.argv[1:] if len(sys.argv) > 1 else list(lake.LAKES.keys())
    for lake_id in lake_ids:
        if lake_id not in lake.LAKES:
            print(f"Nieznane jezioro: {lake_id}", file=sys.stderr)
            continue
        path = DATA_DIR / lake_id / "data.csv"
        if not path.exists():
            print(f"Pomijam {lake_id}: brak data.csv")
            continue
        try:
            n_rows, n_diff = _process_file(path)
            print(f"{lake_id}: {n_rows} wierszy, Zmiana przeliczona z Poziom (zmienionych: {n_diff})")
        except Exception as e:
            print(f"{lake_id}: błąd – {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
