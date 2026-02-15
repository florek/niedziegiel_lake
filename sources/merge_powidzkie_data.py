import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
LAKE_ID = "powidzkie"
METEO_PATH = DATA_DIR / "meteo.csv"
REALNY_PATH = DATA_DIR / LAKE_ID / "realny_pomiar.csv"
OUTPUT_PATH = DATA_DIR / LAKE_ID / "data.csv"


def norm_poziom(s):
    s = str(s).strip().replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


meteo_by_key = {}
with METEO_PATH.open(encoding="utf-8") as f:
    r = csv.reader(f)
    next(r)
    for row in r:
        if len(row) < 3:
            continue
        datestr = row[0].strip()
        parts = datestr.split("-")
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
with REALNY_PATH.open(encoding="utf-8") as f:
    r = csv.reader(f)
    next(r)
    for row in r:
        if len(row) < 2:
            continue
        datestr = row[0].strip()
        parts = datestr.split("-")
        if len(parts) != 2:
            continue
        year, month = int(parts[0]), int(parts[1])
        poziom = norm_poziom(row[1])
        if poziom is None:
            continue
        rows.append((year, month, poziom))

rows.sort(key=lambda x: (x[0], x[1]))
out = [["Data", "Poziom", "Zmiana", "Opad", "Temperatura"]]
prev_poziom = None
for year, month, poziom in rows:
    data_str = f"01.{month:02d}.{year}"
    poziom_str = f"{poziom:.2f}".replace(".", ",")
    if prev_poziom is not None:
        zmiana = poziom - prev_poziom
        zmiana_str = f"{zmiana:.2f}".replace(".", ",")
    else:
        zmiana_str = "0"
    opad, temp = meteo_by_key.get((year, month), ("", ""))
    opad_str = str(opad).replace(".", ",") if opad != "" else ""
    temp_str = str(temp).replace(".", ",") if temp != "" else ""
    out.append([data_str, poziom_str, zmiana_str, opad_str, temp_str])
    prev_poziom = poziom

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(out)
print(len(out) - 1, "wierszy")
