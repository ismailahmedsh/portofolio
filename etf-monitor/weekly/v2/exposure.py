"""Exposure view X per the approved spec (pillars v2), one function used live and point-in-time in REC04.
World reference (ELG07): Ken French Developed market + RF until 2008-02, ACWI 2008-03 to 2008-05, then VT (dividend-adjusted)."""
import numpy as np, pandas as pd
from sklearn.covariance import LedoitWolf

STRESS = [("2007-10-31", "2009-03-31"), ("2020-02-29", "2020-03-31"), ("2022-01-31", "2022-12-31")]
B_PRIORS = {"FAC01": 1.5, "FAC02": 1.5, "FAC03": 1.0, "FAC04": 1.0, "EXR08": -0.01}  # % a year per unit: unestimated priors
ERP = 4.0

def tanh_score(x, ref, k, d=1, one_sided=False):
    if x is None or ref is None or pd.isna(x) or pd.isna(ref): return np.nan
    z = d * (x - ref) / k
    return 50 - 50 * np.tanh(max(0.0, -z)) if one_sided else 50 + 50 * np.tanh(z)

def fam_score(scores, weights):
    have = {k: w for k, w in weights.items() if k in scores and not pd.isna(scores[k])}
    if not have: return np.nan, 0.0
    m = sum(scores[k] * w for k, w in have.items()) / sum(have.values()); c = sum(have.values()) / sum(weights.values())
    return 50 + c * (m - 50), c

def factors(french):
    f = french["Developed_5_Factors"].copy(); f.index = f.index + pd.offsets.MonthEnd(0)
    w = french["Developed_Mom_Factor"].copy(); w.index = w.index + pd.offsets.MonthEnd(0)
    f["WML"] = w.iloc[:, 0]
    return f

def world_reference(mret, f):
    """Monthly USD total return of the single declared world reference."""
    kf = (f["Mkt-RF"] + f["RF"])
    w = kf.copy()
    if "ACWI" in mret: w = w.where(~((w.index >= "2008-03-31") & (w.index <= "2008-05-31")), mret["ACWI"].reindex(w.index))
    vt = mret["VT"].dropna(); w = pd.concat([w.loc[:vt.index[0] - pd.offsets.MonthEnd(1)], vt]).sort_index()
    return w[~w.index.duplicated(keep="last")]

def splice_test(line, proxy):
    j = pd.concat([line, proxy], axis=1).dropna()
    if len(j) < 24: return False, len(j), np.nan, np.nan
    corr = j.corr().iloc[0, 1]; gap = ((1 + j.iloc[:, 0]).prod() ** (12 / len(j)) - (1 + j.iloc[:, 1]).prod() ** (12 / len(j))) * 1e4
    return bool(corr >= 0.98 and abs(gap) <= 50), len(j), float(corr), float(gap)

def spliced(line, proxy):
    ok, n, c, g = splice_test(line, proxy)
    if not ok: return line.dropna(), {"used": False, "overlap": n, "corr": c, "gap_bps": g}
    first = line.first_valid_index()
    return pd.concat([proxy.loc[:first - pd.offsets.MonthEnd(1)], line.loc[first:]]).dropna(), {"used": True, "overlap": n, "corr": round(c, 4), "gap_bps": round(g, 1)}

def _nw_tstats(X, y, coef, lags=3):
    e = y - X @ coef; n = len(y); XtXi = np.linalg.inv(X.T @ X)
    S = (X * e[:, None]).T @ (X * e[:, None])
    for l in range(1, lags + 1):
        w = 1 - l / (lags + 1); G = (X[l:] * e[l:, None]).T @ (X[:-l] * e[:-l, None]); S += w * (G + G.T)
    V = XtXi @ S @ XtXi; return coef / np.sqrt(np.maximum(np.diag(V), 1e-18))

def raw_measures(r, world, f, dt):
    """Pillar inputs for one exposure (monthly USD returns r) at decision date dt, using only data up to dt
    (Ken French factors and the world reference lagged 1 month for the regressions)."""
    r = r.loc[:dt].dropna(); W = world.loc[:dt]; out = {"months": len(r)}
    if len(r) < 36: return out
    lag = dt - pd.offsets.MonthEnd(1)
    ff = f.loc[:lag].copy()
    cma_b = np.polyfit(ff["HML"], ff["CMA"], 1)[0]  # expanding-window orthogonalisation, point-in-time
    ff["CMAp"] = ff["CMA"] - cma_b * ff["HML"]
    # FAC05: univariate 120-month beta on world excess returns, Ledoit-Wolf shrunk, release-lagged
    j = pd.concat([r.loc[:lag], W.loc[:lag]], axis=1).dropna().iloc[-120:]
    rf = f["RF"].reindex(j.index).fillna(0)
    if len(j) >= 36:
        ex = np.column_stack([j.iloc[:, 0] - rf, j.iloc[:, 1] - rf]); lw = LedoitWolf().fit(ex)
        b_ols = float(np.cov(ex.T)[0, 1] / np.cov(ex.T)[1, 1])
        out["FAC05"] = (1 - lw.shrinkage_) * b_ols + lw.shrinkage_ * 1.0  # Ledoit-Wolf intensity applied toward beta 1 (world = 1 exactly)
    # FAC01-04: 60-month Newey-West regression on Mkt-RF, SMB, HML, RMW, CMAp, WML, loadings shrunk by min(1, |t|/2)
    k = ff[["Mkt-RF", "SMB", "HML", "RMW", "CMAp", "WML", "RF"]].join(r.rename("y"), how="inner").dropna().iloc[-60:]
    if len(k) >= 36:
        X = np.column_stack([np.ones(len(k)), k[["Mkt-RF", "SMB", "HML", "RMW", "CMAp", "WML"]].values]); y = (k["y"] - k["RF"]).values
        coef = np.linalg.lstsq(X, y, rcond=None)[0]; t = _nw_tstats(X, y, coef); sh = np.minimum(1, np.abs(t) / 2) * coef
        out.update(FAC01=sh[3], FAC02=sh[4], FAC03=sh[5], FAC04=sh[2] if coef[4] >= 0 else 0.0, alpha=coef[0] * 12 * 100, alpha_t=t[0])
    # RSK01 components on the full expanding window (at least 120 months)
    jj = pd.concat([r, W], axis=1).dropna()
    if len(jj) >= 120:
        nav = (1 + jj).cumprod(); dd = (nav / nav.cummax() - 1).min() * 100
        out["DD_excess"] = float(dd.iloc[0] - dd.iloc[1])  # raw excess max drawdown, negative = deeper than the world
        def longest_uw(n):
            peak = n.cummax(); uw = (n < peak).astype(int); best = cur = 0
            for x in uw: cur = cur + 1 if x else 0; best = max(best, cur)
            return best
        out["RSK02"] = float(longest_uw(nav.iloc[:, 0]) - longest_uw(nav.iloc[:, 1]))
        if "FAC05" in out:
            sf = []
            for a, b in STRESS:
                if pd.Timestamp(b) + pd.offsets.MonthEnd(1) > dt: continue  # window must have ended at least 1 month before dt
                x = jj.loc[a:b]
                if len(x) == 0: continue
                s = ((1 + x.iloc[:, 0]).prod() - 1 - out["FAC05"] * ((1 + x.iloc[:, 1]).prod() - 1)) * 100
                sf.append(min(s, 0.0))  # only shortfalls count
            out["RSK04"] = float(np.mean(sf)) if sf else np.nan
        up, dn = jj[jj.iloc[:, 1] > 0], jj[jj.iloc[:, 1] < 0]
        out["RSK03"] = float(np.cov(dn.iloc[:, 0], dn.iloc[:, 1])[0, 1] / dn.iloc[:, 1].var() - np.cov(up.iloc[:, 0], up.iloc[:, 1])[0, 1] / up.iloc[:, 1].var())
        q = jj.iloc[:, 0].quantile(.05); out["RSK05"] = float(-jj.iloc[:, 0][jj.iloc[:, 0] <= q].mean() / jj.iloc[:, 0].std())
    # EXR08: months -60 to -13, relative to the world reference
    jr = pd.concat([r, W], axis=1).dropna()
    if len(jr) >= 60:
        win = jr.iloc[-60:-12]; out["EXR08"] = float(((1 + win.iloc[:, 0]).prod() - (1 + win.iloc[:, 1]).prod()) * 100)
    return out

def score(e, w):
    """Scores of exposure e against the world reference's own measures w (world = 50 on every pillar)."""
    s = {c: tanh_score(e.get(c), w.get(c), 0.2, 1) for c in ["FAC01", "FAC02", "FAC03", "FAC04"]}
    sub = [tanh_score(e.get("DD_excess"), 0.0, 10, 1, True), tanh_score(e.get("RSK02"), 0.0, 24, -1, True), tanh_score(e.get("RSK04"), w.get("RSK04", 0.0), 5, 1, True)]
    sub = [x for x in sub if not pd.isna(x)]
    s["RSK01"] = float(np.mean(sub)) if sub else np.nan
    s["RSK03"] = tanh_score(e.get("RSK03"), w.get("RSK03"), 0.2, -1, True)
    s["RSK05"] = tanh_score(e.get("RSK05"), w.get("RSK05"), 0.5, -1, True)
    s["EXR08"] = tanh_score(e.get("EXR08"), 0.0, 20, -1); s["EXR06"] = np.nan  # REER source unverified
    exr, _ = fam_score(s, {"EXR06": .4, "EXR08": .6}); fac, _ = fam_score(s, {"FAC01": .12, "FAC02": .30, "FAC03": .28, "FAC04": .30})
    rsk, _ = fam_score(s, {"RSK01": .35, "RSK03": .35, "RSK05": .30})
    parts = [(20, exr), (40, fac), (40, rsk)]; have = [(wt, v) for wt, v in parts if not pd.isna(v)]
    X = sum(wt * v for wt, v in have) / sum(wt for wt, _ in have) if have else np.nan
    return {**s, "EXR": exr, "FAC": fac, "RSK": rsk, "X": X}

def exp_excess(e, w, cost_bps=0.0, cost_ref_bps=0.0, priors=True):
    """EXR02: beta x ERP + clip(sum b_j x (x_ij - x_world,j), -2, 2) - cost difference, % a year."""
    beta = e.get("FAC05", np.nan)
    tilt = sum(B_PRIORS[k] * ((e.get(k) or 0) - (w.get(k) or 0)) for k in ["FAC01", "FAC02", "FAC03", "FAC04"]) + B_PRIORS["EXR08"] * ((e.get("EXR08") or 0) - 0)
    return beta * ERP + (float(np.clip(tilt, -2, 2)) if priors else 0.0) - (cost_bps - cost_ref_bps) / 100

def fit04(Ei, beta_i, EP, beta_P):
    """Expected alpha against the portfolio: alpha_i = E_i - (beta_i / beta_P) x E_P (identically 0 with zero tilts and equal costs)."""
    return Ei - (beta_i / beta_P) * EP

def self_check():
    """Built-in check from the spec: with zero tilts and equal costs, FIT04 = 0 for any beta."""
    for bi, bp in [(1.3, 1.05), (0.7, 1.0), (1.0, 0.9)]:
        a = fit04(bi * ERP, bi, bp * ERP, bp); assert abs(a) < 0.1, f"FIT04 identity failed: {a}"
    return True
