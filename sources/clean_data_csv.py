import csv
import sys
from pathlib import Path

import lake

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"


def _norm_val(s):
    if s is None or str(s).strip() == "":
        return None
    try:
        return float(str(s).strip().replace(",", "."))
    except ValueError:
        return None


def _parse_data(s):
    s = str(s).strip()
    parts = s.split(".")
    if len(parts) != 3:
        return None
    try:
        d, m, y = int(parts[0]), int(parts[1]), int(parts[2])
        if 1 <= m <= 12 and y > 1900:
            return f"{d:02d}.{m:02d}.{y}"
    except (ValueError, TypeError):
        pass
    return None


def _row_complete(row):
    if len(row) < 5:
        return False
    data_str = _parse_data(row[0])
    if data_str is None:
        return False
    poziom = _norm_val(row[1])
    zmiana = _norm_val(row[2])
    opad = _norm_val(row[3])
    temp = _norm_val(row[4])
    if poziom is None or zmiana is None or opad is None or temp is None:
        return False
    if "ERROR" in str(row[2]).upper():
        return False
    return True


def _clean_file(path: Path) -> int:
    rows_in = []
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.reader(f)
        header = next(r)
        rows_in = list(r)
    if header != ["Data", "Poziom", "Zmiana", "Opad", "Temperatura"]:
        return 0
    kept = [row for row in rows_in if _row_complete(row)]
    removed = len(rows_in) - len(kept)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(kept)
    return removed


def main():
    lake_ids = sys.argv[1:] if len(sys.argv) > 1 else list(lake.LAKES)
    for lake_id in lake_ids:
        if lake_id not in lake.LAKES:
            print(f"Nieznane jezioro: {lake_id}", file=sys.stderr)
            continue
        path = DATA_DIR / lake_id / "data.csv"
        if not path.exists():
            print(f"Pomijam {lake_id}: brak data.csv")
            continue
        removed = _clean_file(path)
        if removed > 0:
            print(f"{lake_id}: usunięto {removed} niekompletnych wierszy")
        else:
            print(f"{lake_id}: plik kompletny, bez zmian")


if __name__ == "__main__":
    main()
