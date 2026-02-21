from __future__ import annotations

import sys
from pathlib import Path

_root = Path(__file__).resolve().parents[1]
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

import pandas as pd

def main() -> None:
    bud_path = _root / "data" / "budzislawskie" / "data_ext.csv"
    nied_path = _root / "data" / "niedziegiel" / "data_ext.csv"
    bud = pd.read_csv(bud_path)
    bud.columns = [c.strip().lstrip("\ufeff") for c in bud.columns]
    bud["Data"] = pd.to_datetime(bud["Data"], format="%d.%m.%Y", dayfirst=True)
    nied = pd.read_csv(nied_path)
    nied["Data"] = pd.to_datetime(nied["Data"])
    ext_cols = ["Opad", "Temperatura", "Rezerwuar_sniegu", "Opad_efektywny", "Snow_add_mm", "Rain_part_mm", "Melt_mm"]
    merged = bud[["Data", "Poziom", "Zmiana"]].merge(
        nied[["Data"] + ext_cols],
        on="Data",
        how="left",
    )
    merged["Data"] = merged["Data"].dt.strftime("%Y-%m-%d")
    merged.to_csv(bud_path, index=False)

if __name__ == "__main__":
    main()
