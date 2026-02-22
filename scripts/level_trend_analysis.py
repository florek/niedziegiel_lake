from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as st
from sklearn.linear_model import TheilSenRegressor

ROOT = Path(__file__).resolve().parents[1]
PERIOD1 = (2000, 2010)
PERIOD2_START = 2015
PERIOD2_END = 2023
N_BOOT = 1000
CI = 0.95

LAKES = [
    ("niedziegiel", ROOT / "data" / "niedziegiel" / "data_ext.csv", "Niedziegiel"),
    ("powidzkie", ROOT / "data" / "powidzkie" / "data_ext.csv", "Powidzkie"),
    ("budzislawskie", ROOT / "data" / "budzislawskie" / "data_ext.csv", "Budzislawskie"),
    ("skulskie", ROOT / "data" / "skulskie" / "data_ext.csv", "Skulskie"),
]


def _normalize_columns(df: pd.DataFrame, date_col: str, level_col: str) -> pd.DataFrame:
    df = df.rename(columns={date_col: "date", level_col: "level"})
    for c in ["date", "level"]:
        if c not in df.columns:
            raise ValueError(f"Brak kolumny odpowiadającej {c}. Dostępne: {list(df.columns)}")
    return df


def _parse_level(ser: pd.Series) -> pd.Series:
    if pd.api.types.is_numeric_dtype(ser):
        return ser.astype(float)
    return pd.to_numeric(ser.astype(str).str.replace(",", ".", regex=False), errors="coerce")


def load_and_prepare(
    path: Path,
    date_col: str = "date",
    level_col: str = "level",
    lake_col: str | None = None,
    lake_filter: str | None = None,
) -> pd.DataFrame:
    raw = pd.read_csv(path)
    raw.columns = [c.strip().lstrip("\ufeff") for c in raw.columns]
    date_cand = date_col if date_col in raw.columns else ("Data" if "Data" in raw.columns else None)
    level_cand = level_col if level_col in raw.columns else ("Poziom" if "Poziom" in raw.columns else None)
    if date_cand is None or level_cand is None:
        raise ValueError(f"Oczekiwano kolumn date/Data i level/Poziom. Mam: {list(raw.columns)}")
    df = _normalize_columns(raw.copy(), date_cand, level_cand)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"]).sort_values("date")
    if lake_col and lake_col in raw.columns:
        df["lake"] = raw.loc[df.index, lake_col]
    df = df.reset_index(drop=True)
    df["level"] = _parse_level(df["level"])
    df = df.dropna(subset=["level"])
    if lake_col and lake_filter and "lake" in df.columns:
        df = df[df["lake"] == lake_filter].copy()
    df["year_cont"] = df["date"].dt.year + df["date"].dt.dayofyear / 365.25
    return df


def _trend_ols(y: np.ndarray, x: np.ndarray) -> tuple[float, float, float, float]:
    slope, intercept, r, p, se = st.linregress(x, y)
    return slope, intercept, se, p


def _trend_theilsen(y: np.ndarray, x: np.ndarray) -> float:
    x_ = x.reshape(-1, 1)
    m = TheilSenRegressor(random_state=42).fit(x_, y)
    return float(m.coef_[0])


def _trend_bootstrap(
    y: np.ndarray, x: np.ndarray, n_boot: int = N_BOOT, ci: float = CI
) -> tuple[float, float, float]:
    n = len(y)
    slopes = []
    for _ in range(n_boot):
        idx = np.random.choice(n, size=n, replace=True)
        xb, yb = x[idx], y[idx]
        s, _, _, _, _ = st.linregress(xb, yb)
        slopes.append(s)
    slopes = np.array(slopes)
    lo = np.percentile(slopes, (1 - ci) / 2 * 100)
    hi = np.percentile(slopes, (1 + ci) / 2 * 100)
    return float(np.median(slopes)), float(lo), float(hi)


def _monthly_delta(df: pd.DataFrame) -> pd.Series:
    df = df.sort_values("date")
    return df["level"].diff()


def _mann_kendall(y: np.ndarray) -> tuple[float, float]:
    n = len(y)
    s = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            s += np.sign(y[j] - y[i])
    var_s = (n * (n - 1) * (2 * n + 5)) / 18.0
    z = (s - 1) / np.sqrt(var_s) if s > 0 else (s + 1) / np.sqrt(var_s) if s < 0 else 0
    p = 2 * (1 - st.norm.cdf(abs(z)))
    return float(z), float(p)


def _chow_test(
    y: np.ndarray, x: np.ndarray, break_idx: int
) -> tuple[float, float, int, int]:
    n, k = len(y), 2
    if break_idx < k or n - break_idx < k:
        return float("nan"), float("nan"), 1, 1
    x1, y1 = x[:break_idx], y[:break_idx]
    x2, y2 = x[break_idx:], y[break_idx:]
    s1, i1, _, _, _ = st.linregress(x1, y1)
    s2, i2, _, _, _ = st.linregress(x2, y2)
    pred1 = s1 * x1 + i1
    pred2 = s2 * x2 + i2
    rss1 = np.sum((y1 - pred1) ** 2)
    rss2 = np.sum((y2 - pred2) ** 2)
    rss_pooled = rss1 + rss2
    s_pool, i_pool, _, _, _ = st.linregress(x, y)
    rss_full = np.sum((y - (s_pool * x + i_pool)) ** 2)
    num = (rss_full - rss_pooled) / k
    den = rss_pooled / (n - 2 * k)
    f_stat = num / den if den > 0 else float("nan")
    p_val = 1 - st.f.cdf(f_stat, k, n - 2 * k) if np.isfinite(f_stat) else float("nan")
    return float(f_stat), float(p_val), break_idx, n - break_idx


def run_period_analysis(df: pd.DataFrame, year_lo: int, year_hi: int) -> dict:
    sub = df[(df["date"].dt.year >= year_lo) & (df["date"].dt.year <= year_hi)].copy()
    if len(sub) < 10:
        return {"n": len(sub), "slope_ols": np.nan, "slope_ts": np.nan, "slope_boot": np.nan, "ci_lo": np.nan, "ci_hi": np.nan, "p_ols": np.nan}
    x = sub["year_cont"].values
    y = sub["level"].values
    slope_ols, intercept_ols, se_ols, p_ols = _trend_ols(y, x)
    slope_ts = _trend_theilsen(y, x)
    slope_boot, ci_lo, ci_hi = _trend_bootstrap(y, x, n_boot=N_BOOT, ci=CI)
    delta = _monthly_delta(sub)
    delta_valid = delta.dropna()
    return {
        "n": len(sub),
        "slope_ols": slope_ols,
        "slope_ts": slope_ts,
        "slope_boot": slope_boot,
        "ci_lo": ci_lo,
        "ci_hi": ci_hi,
        "se_ols": se_ols,
        "p_ols": p_ols,
        "mean_delta": float(delta_valid.mean()) if len(delta_valid) else np.nan,
        "std_delta": float(delta_valid.std()) if len(delta_valid) > 1 else np.nan,
        "mk_z": _mann_kendall(y)[0],
        "mk_p": _mann_kendall(y)[1],
    }


def run_comparison(res1: dict, res2: dict) -> dict:
    diff_ols = res2["slope_ols"] - res1["slope_ols"]
    diff_ts = res2["slope_ts"] - res1["slope_ts"]
    overlap = not (res2["ci_hi"] < res1["ci_lo"] or res2["ci_lo"] > res1["ci_hi"])
    se_diff = np.sqrt(res1["se_ols"] ** 2 + res2["se_ols"] ** 2) if np.isfinite(res1["se_ols"]) and np.isfinite(res2["se_ols"]) else np.nan
    z_diff = diff_ols / se_diff if se_diff and se_diff > 0 else np.nan
    p_diff = 2 * (1 - st.norm.cdf(abs(z_diff))) if np.isfinite(z_diff) else np.nan
    return {
        "diff_ols_m_per_yr": diff_ols,
        "diff_theilsen_m_per_yr": diff_ts,
        "ci_overlap": overlap,
        "p_diff": p_diff,
        "significant_005": p_diff < 0.05 if np.isfinite(p_diff) else False,
    }


def run_chow(df: pd.DataFrame, break_year: float = 2012.5) -> dict:
    df = df.sort_values("date")
    x = df["year_cont"].values
    y = df["level"].values
    break_idx = int(np.searchsorted(x, break_year))
    f_stat, p_val, n1, n2 = _chow_test(y, x, break_idx)
    return {"chow_f": f_stat, "chow_p": p_val, "n_before": n1, "n_after": n2}


def run_climate_correlations(df: pd.DataFrame) -> dict:
    out = {"corr_level_temp": (np.nan, np.nan), "corr_level_opad": (np.nan, np.nan)}
    work = df.copy()
    if "Temperatura" in work.columns:
        t = pd.to_numeric(work["Temperatura"].astype(str).str.replace(",", ".", regex=False), errors="coerce")
        work = work.assign(temp=t)
        by_yr = work.groupby(work["date"].dt.year).agg(level_mean=("level", "mean"), temp_mean=("temp", "mean")).dropna()
        if len(by_yr) >= 5:
            r_t, p_t = st.pearsonr(by_yr["level_mean"], by_yr["temp_mean"])
            out["corr_level_temp"] = (float(r_t), float(p_t))
    if "Opad" in df.columns:
        o = pd.to_numeric(df["Opad"].astype(str).str.replace(",", ".", regex=False), errors="coerce")
        work = df.assign(opad=o)
        by_yr = work.groupby(work["date"].dt.year).agg(level_mean=("level", "mean"), opad_sum=("opad", "sum")).dropna()
        if len(by_yr) >= 5:
            r_o, p_o = st.pearsonr(by_yr["level_mean"], by_yr["opad_sum"])
            out["corr_level_opad"] = (float(r_o), float(p_o))
    return out


def build_results_table(
    res1: dict, res2: dict, comp: dict, chow: dict, climate: dict, period2_end: int
) -> pd.DataFrame:
    rows = [
        {"metoda": "OLS (m/rok)", "2000–2010": res1["slope_ols"], "2015–" + str(period2_end): res2["slope_ols"]},
        {"metoda": "Theil-Sen (m/rok)", "2000–2010": res1["slope_ts"], "2015–" + str(period2_end): res2["slope_ts"]},
        {"metoda": "Bootstrap mediana (m/rok)", "2000–2010": res1["slope_boot"], "2015–" + str(period2_end): res2["slope_boot"]},
        {"metoda": "Bootstrap 95% CI dolna", "2000–2010": res1["ci_lo"], "2015–" + str(period2_end): res2["ci_lo"]},
        {"metoda": "Bootstrap 95% CI górna", "2000–2010": res1["ci_hi"], "2015–" + str(period2_end): res2["ci_hi"]},
        {"metoda": "Śr. mies. Δlevel (m)", "2000–2010": res1["mean_delta"], "2015–" + str(period2_end): res2["mean_delta"]},
        {"metoda": "Odch. std. Δlevel (m)", "2000–2010": res1["std_delta"], "2015–" + str(period2_end): res2["std_delta"]},
        {"metoda": "Mann-Kendall p", "2000–2010": res1["mk_p"], "2015–" + str(period2_end): res2["mk_p"]},
        {"metoda": "Różnica tempa (okres2-okres1) m/rok", "2000–2010": None, "2015–" + str(period2_end): comp["diff_ols_m_per_yr"]},
        {"metoda": "Przedziały 95% CI pokrywają się", "2000–2010": comp["ci_overlap"], "2015–" + str(period2_end): None},
        {"metoda": "Różnica istotna (p<0,05)", "2000–2010": comp["significant_005"], "2015–" + str(period2_end): None},
        {"metoda": "Chow F (zmiana struktury)", "2000–2010": chow["chow_f"], "2015–" + str(period2_end): None},
        {"metoda": "Chow p", "2000–2010": chow["chow_p"], "2015–" + str(period2_end): None},
    ]
    return pd.DataFrame(rows)


def plot_level_and_trends(
    df: pd.DataFrame,
    res1: dict,
    res2: dict,
    period2_end: int,
    out_path: Path,
    title: str = "Poziom jeziora i trendy",
) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df["date"], df["level"], color="tab:blue", alpha=0.7, label="Poziom (m n.p.m.)")
    p1 = df[(df["date"].dt.year >= PERIOD1[0]) & (df["date"].dt.year <= PERIOD1[1])]
    p2 = df[(df["date"].dt.year >= PERIOD2_START) & (df["date"].dt.year <= period2_end)]
    if len(p1) > 0:
        x1 = p1["year_cont"].values
        y1 = p1["level"].values
        s1, i1 = res1["slope_ols"], st.linregress(x1, y1)[1]
        t1 = i1 + s1 * x1
        ax.plot(p1["date"], t1, color="tab:green", linestyle="--", linewidth=2, label=f"Trend 2000–2010 ({s1:.4f} m/rok)")
    if len(p2) > 0:
        x2 = p2["year_cont"].values
        y2 = p2["level"].values
        s2, i2 = res2["slope_ols"], st.linregress(x2, y2)[1]
        t2 = i2 + s2 * x2
        ax.plot(p2["date"], t2, color="tab:red", linestyle="--", linewidth=2, label=f"Trend 2015–{period2_end} ({s2:.4f} m/rok)")
    ax.axvspan(
        pd.Timestamp(f"{PERIOD1[0]}-01-01"),
        pd.Timestamp(f"{PERIOD1[1]}-12-31"),
        alpha=0.15,
        color="green",
    )
    ax.axvspan(
        pd.Timestamp(f"{PERIOD2_START}-01-01"),
        pd.Timestamp(f"{period2_end}-12-31"),
        alpha=0.15,
        color="red",
    )
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.set_xlabel("Data")
    ax.set_ylabel("Poziom (m n.p.m.)")
    ax.set_title(title)
    ax.legend(loc="best")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def print_report(
    res1: dict,
    res2: dict,
    comp: dict,
    chow: dict,
    climate: dict,
    period2_end: int,
    table_path: Path | None,
) -> None:
    print("\n" + "=" * 60)
    print("RAPORT: Test tempa spadku poziomu wody")
    print("=" * 60)
    print(f"\nOkres 1: {PERIOD1[0]}-{PERIOD1[1]}  |  Okres 2: {PERIOD2_START}-{period2_end}")
    print(f"\nTempo trendu (m/rok):")
    print(f"  2000-2010:  OLS {res1['slope_ols']:.4f}  |  Theil-Sen {res1['slope_ts']:.4f}  |  Bootstrap [{res1['ci_lo']:.4f}, {res1['ci_hi']:.4f}]")
    print(f"  2015-{period2_end}:  OLS {res2['slope_ols']:.4f}  |  Theil-Sen {res2['slope_ts']:.4f}  |  Bootstrap [{res2['ci_lo']:.4f}, {res2['ci_hi']:.4f}]")
    print(f"\nRoznica tempa (okres2 - okres1): {comp['diff_ols_m_per_yr']:.4f} m/rok  (p = {comp['p_diff']:.4f})")
    print(f"Przedzialy 95% CI pokrywaja sie: {comp['ci_overlap']}. Roznica istotna (p<0.05): {comp['significant_005']}.")
    print(f"\nSrednie miesieczne dlevel: 2000-2010: {res1['mean_delta']:.4f} m (std {res1['std_delta']:.4f}); 2015-{period2_end}: {res2['mean_delta']:.4f} m (std {res2['std_delta']:.4f}).")
    print(f"\nTest Chow (zmiana struktury): F = {chow['chow_f']:.3f}, p = {chow['chow_p']:.4f}.")
    print(f"Mann-Kendall (trend): 2000-2010 p = {res1['mk_p']:.4f}; 2015-{period2_end} p = {res2['mk_p']:.4f}.")
    r_t, p_t = climate["corr_level_temp"]
    r_o, p_o = climate["corr_level_opad"]
    print(f"\nKorelacja poziom-temperatura roczna: r = {r_t:.3f}, p = {p_t:.4f}.")
    print(f"Korelacja poziom-opad roczny: r = {r_o:.3f}, p = {p_o:.4f}.")
    print("\n--- INTERPRETACJA HYDROLOGICZNA ---")
    if comp["diff_ols_m_per_yr"] < 0:
        print("Tempo spadku poziomu w okresie 2015+ jest wieksze (bardziej ujemne) niz w 2000-2010.")
    else:
        print("Tempo spadku poziomu w okresie 2015+ jest mniejsze niz w 2000-2010 (lub wystepuje wzrost).")
    if comp["significant_005"]:
        print("Roznica tempa jest istotna statystycznie (p<0.05) - twardy test pozytywny.")
    else:
        print("Roznica tempa nie jest istotna statystycznie przy alpha=0.05 - na tych danych nie mozna odrzucic rownosci trendow.")
    if np.isfinite(chow["chow_p"]) and chow["chow_p"] < 0.05:
        print("Test Chow wskazuje na istotna zmiane strukturalna (przelom) w szeregu poziomu.")
    if np.isfinite(p_t) and p_t < 0.05:
        print("Poziom koreluje z temperatura roczna - spojne z wplywem klimatu (ewapotranspiracja, topnienie).")
    if np.isfinite(p_o) and p_o < 0.05:
        print("Poziom koreluje z opadem rocznym - spojne z bilansem wodnym / klimatem.")
    print("Wnioski: Przyspieszenie spadku po 2015, jesli istotne, moze wynikac z klimatu (susze, wyzsza ETP) lub z drenazu/regulacji; korelacje z temp/opadem wspieraja role klimatu.")
    print("=" * 60)
    if table_path:
        print(f"\nTabela zapisana: {table_path}")


def run_one_lake(
    input_path: Path,
    lake_id: str,
    label: str,
    out_dir: Path,
    period2_end_arg: int,
    date_col: str,
    level_col: str,
) -> None:
    df = load_and_prepare(input_path, date_col=date_col, level_col=level_col)
    period2_end = min(period2_end_arg, int(df["date"].dt.year.max()))
    res1 = run_period_analysis(df, PERIOD1[0], PERIOD1[1])
    res2 = run_period_analysis(df, PERIOD2_START, period2_end)
    comp = run_comparison(res1, res2)
    chow = run_chow(df)
    climate = run_climate_correlations(df)
    table = build_results_table(res1, res2, comp, chow, climate, period2_end)
    out_dir.mkdir(parents=True, exist_ok=True)
    table_path = out_dir / "trend_results.csv"
    table.to_csv(table_path, index=False)
    plot_level_and_trends(
        df,
        res1,
        res2,
        period2_end,
        out_dir / "level_and_trends.png",
        title=f"{label}: poziom i trendy (2000-2010, 2015-{period2_end})",
    )
    print(f"\n>>> JEZIORO: {label} ({lake_id}) <<<")
    print_report(res1, res2, comp, chow, climate, period2_end, table_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Analiza trendu poziomu jeziora: 2000-2010 vs 2015+")
    parser.add_argument("input", type=Path, nargs="?", default=None, help="Sciezka do CSV; pomijana przy --all-lakes")
    parser.add_argument("--all-lakes", action="store_true", help="Uruchom analize dla kazdego jeziora osobno (Niedziegiel, Powidzkie, Budzislawskie)")
    parser.add_argument("--date-col", default="Data", help="Kolumna daty")
    parser.add_argument("--level-col", default="Poziom", help="Kolumna poziomu")
    parser.add_argument("--lake-col", default=None, help="Opcjonalna kolumna jeziora")
    parser.add_argument("--lake", default=None, help="Filtr wartosci jeziora")
    parser.add_argument("--period2-end", type=int, default=PERIOD2_END, help=f"Koniec okresu 2 (domyslnie {PERIOD2_END})")
    parser.add_argument("--out-dir", type=Path, default=ROOT / "reports" / "trend_analysis", help="Katalog wynikow (przy --all-lakes: podkatalog per jezioro)")
    args = parser.parse_args()
    if args.all_lakes:
        for lake_id, data_path, label in LAKES:
            if not data_path.exists():
                print(f"Pomijam {label}: brak pliku {data_path}", file=sys.stderr)
                continue
            lake_out = args.out_dir / lake_id
            run_one_lake(
                input_path=data_path,
                lake_id=lake_id,
                label=label,
                out_dir=lake_out,
                period2_end_arg=args.period2_end,
                date_col=args.date_col,
                level_col=args.level_col,
            )
        return
    input_path = args.input or (ROOT / "data" / "budzislawskie" / "data_ext.csv")
    if not input_path.exists():
        print(f"Brak pliku: {input_path}", file=sys.stderr)
        sys.exit(1)
    run_one_lake(
        input_path=input_path,
        lake_id="single",
        label="Poziom jeziora",
        out_dir=args.out_dir,
        period2_end_arg=args.period2_end,
        date_col=args.date_col,
        level_col=args.level_col,
    )


if __name__ == "__main__":
    main()
