import sys
from pathlib import Path

import numpy as np

import lake

YEAR_MIN = 2000
YEAR_MAX = 2015
MONTH_END = 2


def main() -> None:
    year_step = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    years = list(range(YEAR_MIN, YEAR_MAX + 1, year_step))
    if years[-1] != YEAR_MAX:
        years.append(YEAR_MAX)
    results = []
    for lake_id in lake.LAKES:
        path = lake.get_data_path(lake_id)
        if not path.exists():
            results.append((lake_id, None, None, None))
            continue
        print(f"--- {lake.LAKES.get(lake_id, lake_id)} ---", flush=True)
        df = lake.load_data(path)
        best_mae = np.inf
        best_year = None
        best_month = None
        orig_year = lake.TRAIN_END_YEAR_BY_LAKE.get(lake_id)
        orig_month = lake.TRAIN_END_MONTH_BY_LAKE.get(lake_id)
        for year in years:
            lake.TRAIN_END_YEAR_BY_LAKE[lake_id] = year
            lake.TRAIN_END_MONTH_BY_LAKE[lake_id] = MONTH_END
            try:
                model, feat, metrics, lag_m, meteo_m = lake.train_model(
                    df=df,
                    path=path,
                    lake_id=lake_id,
                )
                mae = metrics.get("test_mae")
                if mae is not None and mae < best_mae:
                    best_mae = mae
                    best_year = year
                    best_month = MONTH_END
                    print(f"  {year}-{MONTH_END:02d} MAE={mae:.4f}", flush=True)
            except Exception:
                pass
        if orig_year is not None:
            lake.TRAIN_END_YEAR_BY_LAKE[lake_id] = orig_year
        if orig_month is not None:
            lake.TRAIN_END_MONTH_BY_LAKE[lake_id] = orig_month
        if best_year is not None:
            results.append((lake_id, best_year, best_month, round(best_mae, 4)))
        else:
            results.append((lake_id, None, None, None))
    print("Jezioro          | Optymalny koniec treningu | Test MAE (m)")
    print("-----------------|----------------------------|-------------")
    for lid, y, m, v in results:
        date_str = f"{y}-{m:02d}" if y and m else "–"
        mae_str = str(v) if v is not None else "–"
        print(f"{lid:16} | {date_str:26} | {mae_str}")


if __name__ == "__main__":
    main()
