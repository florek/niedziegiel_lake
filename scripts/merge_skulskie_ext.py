from __future__ import annotations

import sys
from pathlib import Path

_root = Path(__file__).resolve().parents[1]
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

import pandas as pd

MONTH_ABBR = {
    "sty": 1,
    "lut": 2,
    "mar": 3,
    "kwi": 4,
    "maj": 5,
    "cze": 6,
    "lip": 7,
    "sie": 8,
    "wrz": 9,
    "paz": 10,
    "paź": 10,
    "lis": 11,
    "gru": 12,
}
EXT_COLS = ["Opad", "Temperatura", "Rezerwuar_sniegu", "Opad_efektywny", "Snow_add_mm", "Rain_part_mm", "Melt_mm"]


def main() -> None:
    skul_path = _root / "data" / "skulskie" / "data.csv"
    nied_path = _root / "data" / "niedziegiel" / "data_ext.csv"
    out_path = _root / "data" / "skulskie" / "data_ext.csv"
    raw = pd.read_csv(skul_path, sep="\t", header=None, names=["mies_rok", "col1", "poziom", "col3"])
    raw["poziom"] = pd.to_numeric(raw["poziom"].astype(str).str.replace(",", ".", regex=False), errors="coerce")
    raw = raw.dropna(subset=["poziom"])
    def parse_mies_rok(s: str) -> tuple[int, int]:
        s = s.strip()
        for abbr, m in MONTH_ABBR.items():
            if s.lower().startswith(abbr):
                rest = s[len(abbr):].lstrip("-")
                y = int(rest)
                if y < 100:
                    y = 1900 + y if y >= 90 else 2000 + y
                return m, y
        raise ValueError(f"Nie rozpoznano mies_rok: {s!r}")
    rows = []
    for _, r in raw.iterrows():
        m, y = parse_mies_rok(r["mies_rok"])
        rows.append({"Data": f"{y}-{m:02d}-01", "Poziom": r["poziom"]})
    df = pd.DataFrame(rows)
    df["Data"] = pd.to_datetime(df["Data"])
    df["Zmiana"] = df["Poziom"].diff().fillna(0).round(4)
    df["Poziom"] = df["Poziom"].round(2)
    nied = pd.read_csv(nied_path)
    nied.columns = [c.strip().lstrip("\ufeff") for c in nied.columns]
    nied["Data"] = pd.to_datetime(nied["Data"])
    merged = df[["Data", "Poziom", "Zmiana"]].merge(
        nied[["Data"] + EXT_COLS],
        on="Data",
        how="left",
    )
    merged["Data"] = merged["Data"].dt.strftime("%Y-%m-%d")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    merged.to_csv(out_path, index=False)
    print(f"Zapisano {len(merged)} wierszy -> {out_path}")


if __name__ == "__main__":
    main()
