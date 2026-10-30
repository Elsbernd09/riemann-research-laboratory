"""Run with:  python3 -m experiments.li_quadratic_response_delta_range   (from the repository root)

How far in delta does the quadratic Li response R_f(delta, gamma) ~ delta^2 chi_n(gamma) stay accurate?

For one conjugate quartet {1/2 +- delta +- i gamma} and the Li kernel f_n(z) = 1 - (1 - 1/z)^n, compare the
exact orbit response R(delta, gamma, n) with delta^2 chi_n(gamma).  The error is measured against the
amplitude envelope A_n(gamma) = 2 n sqrt(n^2 + 4 gamma^2) / (gamma^2 + 1/4)^2 of |chi_n|, because the relative
error to chi_n itself is unbounded near the blind scales where chi_n vanishes.

delta = 3/8 is the largest displacement not excluded by a zero-free half-plane Re s > 7/8 (an UNREFEREED
EXTERNAL CLAIM; see docs/EXTERNAL_RESULTS_REGISTER.md).  This script does not use that claim.
"""

from __future__ import annotations

import csv
import json
import platform
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

from src.li_susceptibility import li_susceptibility_exact, signed_orbit_response

RESULT_DIR = Path("results/li_quadratic_response_delta_range")
GAMMAS = ["14.134725141734693", "21.022039638771555", "100", "1000"]
DELTAS = ["0.05", "0.125", "0.25", "0.375"]
C_VALUES = [mp.mpf(x) for x in mp.linspace(0.1, 10, 100)]
OUTSIDE_K = [("0.01", 0.375), ("0.1", 0.375), ("1", 0.375), ("3", 0.375)]


def envelope(n: int, gamma: mp.mpf) -> mp.mpf:
    return 2 * n * mp.sqrt(n * n + 4 * gamma * gamma) / (gamma * gamma + mp.mpf(1) / 4) ** 2


def git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout.strip()


def main() -> None:
    started = time.perf_counter()
    mp.mp.dps = 60
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for g_str in GAMMAS:
        g = mp.mpf(g_str)
        for d_str in DELTAS:
            d = mp.mpf(d_str)
            worst_env, worst_c = mp.mpf(0), None
            for c in C_VALUES:
                n = max(1, int(mp.nint(c * g)))
                r = signed_orbit_response(d, g, n)
                chi = li_susceptibility_exact(n, g)
                e = abs(r - d * d * chi) / (d * d * envelope(n, g))
                if e > worst_env:
                    worst_env, worst_c = e, mp.mpf(n) / g
            rows.append({"gamma": g_str, "delta": d_str, "worst_error_over_envelope": mp.nstr(worst_env, 6),
                         "at_n_over_gamma": mp.nstr(worst_c, 4)})
    # beyond the matched-scale window: n = k gamma^2 at the first zero ordinate
    g = mp.mpf(GAMMAS[0])
    beyond = []
    for k_str, d in OUTSIDE_K:
        n = max(1, int(mp.mpf(k_str) * g * g))
        dd = mp.mpf(d)
        r = signed_orbit_response(dd, g, n)
        chi = li_susceptibility_exact(n, g)
        beyond.append({"k": k_str, "n": n, "delta": d, "relative_error": mp.nstr(r / (dd * dd * chi) - 1, 6)})

    with (RESULT_DIR / "delta_range_results.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    meta = {
        "script": "experiments/li_quadratic_response_delta_range.py",
        "git_commit": git("rev-parse", "HEAD"),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "mpmath": mp.__version__,
        "dps": 60,
        "c_grid": "100 points on [0.1, 10], n = round(c*gamma)",
        "beyond_matched_scale": beyond,
        "seconds": round(time.perf_counter() - started, 2),
    }
    (RESULT_DIR / "metadata.json").write_text(json.dumps(meta, indent=2) + "\n")
    print("gamma  delta  worst |R-d^2 chi|/(d^2 A)  at n/gamma")
    for r in rows:
        print(f"{r['gamma'][:8]:>8} {r['delta']:>6} {r['worst_error_over_envelope']:>12} {r['at_n_over_gamma']:>8}")
    print("beyond matched scale (n = k gamma^2, gamma = gamma_1):")
    for b in beyond:
        print(" ", b)


if __name__ == "__main__":
    main()
