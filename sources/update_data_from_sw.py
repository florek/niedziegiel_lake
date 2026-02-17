import csv
import re
import sys
from pathlib import Path

import pandas as pd

import lake

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
EXCEL_PATH = DATA_DIR / "Jeziora Paweł Florczak.xlsx"
SHEET_NAME = "SW"
METEO_PATH = DATA_DIR / "meteo.csv"

PL_REPLACE = str.maketrans("ęóąśłżźćńĘÓĄŚŁŻŹĆŃ", "eoaslzzcnEOASLZZCN")


def _col_to_lake_id(col_name: str) -> str | None:
    s = str(col_name).strip().lower().translate(PL_REPLACE)
    s = re.sub(r"^jezioro\s+", "", s, flags=re.I)
    s = re.sub(r"\s+", "", s)
    for lid in lake.LAKES:
        name = lake.LAKES[lid].lower().translate(PL_REPLACE)
        canon = re.sub(r"^jezioro\s+", "", name, flags=re.I).replace(" ", "")
        if s == canon or s == lid:
            return lid
    return None


def _parse_excel_date(val) -> tuple[int, int] | None:
    if pd.isna(val):
        return None
    if hasattr(val, "year") and hasattr(val, "month"):
        return int(val.year), int(val.month)
    s = str(val).strip()
    for sep in ["-", ".", "/"]:
        parts = s.split(sep)
        if len(parts) >= 2:
            try:
                a, b = int(parts[0]), int(parts[1])
                if a > 1000:
                    return (a, b)
                if b > 1000:
                    return (b, a)
            except ValueError:
                pass
    return None


def _get_sw_sheet_name() -> str:
    xl = pd.ExcelFile(EXCEL_PATH)
    for name in xl.sheet_names:
        if name.strip().upper() == "SW" or "SW" in name.upper():
            return name
    return xl.sheet_names[0] if xl.sheet_names else "SW"


def _load_sw_by_lake() -> dict[str, list[tuple[int, int, float]]]:
    sheet = _get_sw_sheet_name()
    df = pd.read_excel(EXCEL_PATH, sheet_name=sheet, header=0)
    if df.empty or len(df.columns) < 2:
        return {}
    col0 = df.columns[0]
    lake_cols = {}
    for c in df.columns[1:]:
        lid = _col_to_lake_id(c)
        if lid is not None:
            lake_cols[c] = lid
    by_lake: dict[str, list[tuple[int, int, float]]] = {lid: [] for lid in lake.LAKES}
    for _, row in df.iterrows():
        key = _parse_excel_date(row[col0])
        if key is None:
            continue
        year, month = key
        for col, lid in lake_cols.items():
            try:
                v = row[col]
                if pd.isna(v):
                    continue
                poziom = float(str(v).replace(",", ".").strip())
            except (ValueError, TypeError):
                continue
            by_lake[lid].append((year, month, poziom))
    for lid in by_lake:
        by_lake[lid].sort(key=lambda x: (x[0], x[1]))
    return by_lake


def _load_meteo() -> dict[tuple[int, int], tuple[float | str, float | str]]:
    out = {}
    with METEO_PATH.open(encoding="utf-8") as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if len(row) < 3:
                continue
            parts = row[0].strip().split("-")
            if len(parts) != 2:
                continue
            try:
                month, year = int(parts[0]), int(parts[1])
            except ValueError:
                continue
            try:
                opad = float(str(row[1]).replace(",", "."))
            except (ValueError, TypeError):
                opad = ""
            try:
                temp = float(str(row[2]).replace(",", "."))
            except (ValueError, TypeError):
                temp = ""
            out[(year, month)] = (opad, temp)
    return out


def _write_data_csv(lake_id: str, rows: list[tuple[int, int, float]], meteo: dict) -> None:
    out_path = DATA_DIR / lake_id / "data.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out = [["Data", "Poziom", "Zmiana", "Opad", "Temperatura"]]
    prev_poziom = None
    for year, month, poziom in rows:
        data_str = f"01.{month:02d}.{year}"
        opad, temp = meteo.get((year, month), ("", ""))
        if prev_poziom is not None:
            zmiana = poziom - prev_poziom
            zmiana_str = f"{zmiana:.2f}".replace(".", ",")
        else:
            zmiana_str = "0"
        poziom_str = f"{poziom:.2f}".replace(".", ",")
        opad_str = str(opad).replace(".", ",") if opad != "" else ""
        temp_str = str(temp).replace(".", ",") if temp != "" else ""
        out.append([data_str, poziom_str, zmiana_str, opad_str, temp_str])
        prev_poziom = poziom
    with out_path.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(out)
    print(f"{lake_id}: {len(out) - 1} wierszy (tylko daty z SW)")


def main() -> None:
    if not EXCEL_PATH.exists():
        print(f"Brak pliku: {EXCEL_PATH}", file=sys.stderr)
        sys.exit(1)
    if not METEO_PATH.exists():
        print(f"Brak pliku: {METEO_PATH}", file=sys.stderr)
        sys.exit(1)
    by_lake = _load_sw_by_lake()
    meteo = _load_meteo()
    lake_ids = sys.argv[1:] if len(sys.argv) > 1 else list(lake.LAKES)
    for lid in lake_ids:
        if lid not in lake.LAKES:
            print(f"Nieznane jezioro: {lid}", file=sys.stderr)
            continue
        rows = by_lake.get(lid, [])
        if not rows:
            print(f"Pomijam {lid}: brak danych w arkuszu SW.")
            continue
        _write_data_csv(lid, rows, meteo)


if __name__ == "__main__":
    main()
