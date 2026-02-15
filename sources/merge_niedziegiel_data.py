import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
LAKE_ID = "niedziegiel"
METEO_PATH = DATA_DIR / "meteo.csv"
REALNY_PATH = DATA_DIR / LAKE_ID / "realny_pomiar.csv"
OUTPUT_PATH = DATA_DIR / LAKE_ID / "data.csv"


def _norm_poziom(s):
    s = str(s).strip().replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def _parse_data(data_str):
    parts = data_str.strip().split(".")
    if len(parts) != 3:
        return None
    try:
        day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        return (year, month)
    except ValueError:
        return None


realny_by_key = {}
with REALNY_PATH.open(encoding="utf-8") as f:
    r = csv.reader(f)
    next(r)
    for row in r:
        if len(row) < 2:
            continue
        parts = row[0].strip().split("-")
        if len(parts) != 2:
            continue
        try:
            year, month = int(parts[0]), int(parts[1])
        except ValueError:
            continue
        poziom = _norm_poziom(row[1])
        if poziom is None:
            continue
        realny_by_key[(year, month)] = poziom

meteo_by_key = {}
with METEO_PATH.open(encoding="utf-8") as f:
    r = csv.reader(f)
    next(r)
    for row in r:
        if len(row) < 3:
            continue
        parts = row[0].strip().split("-")
        if len(parts) != 2:
            continue
        month, year = int(parts[0]), int(parts[1])
        try:
            opad = float(str(row[1]).replace(",", "."))
        except (ValueError, TypeError):
            opad = ""
        try:
            temp = float(str(row[2]).replace(",", "."))
        except (ValueError, TypeError):
            temp = ""
        meteo_by_key[(year, month)] = (opad, temp)

rows = []
with OUTPUT_PATH.open(encoding="utf-8") as f:
    r = csv.reader(f)
    header = next(r)
    for row in r:
        if len(row) < 2:
            continue
        data_str = row[0].strip()
        key = _parse_data(data_str)
        if key is None:
            continue
        year, month = key
        poziom = realny_by_key.get((year, month))
        if poziom is None:
            poziom = _norm_poziom(row[1])
        if poziom is None:
            continue
        opad, temp = meteo_by_key.get((year, month), (row[3] if len(row) > 3 else "", row[4] if len(row) > 4 else ""))
        if opad == "" and len(row) > 3 and row[3].strip():
            try:
                opad = float(str(row[3]).replace(",", "."))
            except (ValueError, TypeError):
                pass
        if temp == "" and len(row) > 4 and row[4].strip():
            try:
                temp = float(str(row[4]).replace(",", "."))
            except (ValueError, TypeError):
                pass
        rows.append((data_str, poziom, opad, temp))

out = [["Data", "Poziom", "Zmiana", "Opad", "Temperatura"]]
prev_poziom = None
for data_str, poziom, opad, temp in rows:
    poziom_str = f"{poziom:.2f}".replace(".", ",")
    if prev_poziom is not None:
        zmiana = poziom - prev_poziom
        zmiana_str = f"{zmiana:.2f}".replace(".", ",")
    else:
        zmiana_str = "0"
    opad_str = str(opad).replace(".", ",") if opad != "" else ""
    temp_str = str(temp).replace(".", ",") if temp != "" else ""
    out.append([data_str, poziom_str, zmiana_str, opad_str, temp_str])
    prev_poziom = poziom

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(out)
print(len(out) - 1, "wierszy")
