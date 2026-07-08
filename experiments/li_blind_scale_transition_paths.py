"""Reproducible experiment for near-blind Li response exponents."""

from __future__ import annotations

import csv
import hashlib
import json
import platform
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

from src.li_susceptibility import (
    li_blind_scale,
    li_blind_scale_correction,
    li_profile_derivative,
    li_susceptibility_exact,
    solve_near_blind_gamma,
)


RESULT_DIR = Path(
    "results/li_blind_scale_transition_paths"
)
CSV_PATH = RESULT_DIR / "transition_results.csv"
METADATA_PATH = RESULT_DIR / "metadata.json"


def git_output(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        check=True,
        capture_output=True,
        text=True,
    )

    return result.stdout.strip()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as handle:
        for chunk in iter(
            lambda: handle.read(65536),
            b"",
        ):
            digest.update(chunk)

    return digest.hexdigest()


def main() -> None:
    started = time.perf_counter()

    mp.mp.dps = 180

    commit_at_start = git_output(
        "rev-parse",
        "HEAD",
    )

    clean_at_start = (
        git_output("status", "--porcelain")
        == ""
    )

    RESULT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    k = 0
    beta = mp.mpf("1")

    c_k = li_blind_scale(k)

    psi_prime = li_profile_derivative(c_k)
    correction = li_blind_scale_correction(k)

    r_values = [
        mp.mpf("0.5"),
        mp.mpf("1"),
        mp.mpf("1.5"),
        mp.mpf("2"),
        mp.mpf("3"),
    ]

    n_values = [
        1000,
        2500,
        5000,
        10000,
        25000,
        50000,
        100000,
        250000,
        500000,
        1000000,
    ]

    rows: list[dict[str, str | int]] = []

    print("LI NEAR-BLIND TRANSITION PATHS")
    print("=" * 110)

    print(
        "c_0="
        f"{mp.nstr(c_k, 50)}"
    )

    print(
        "Psi'(c_0)="
        f"{mp.nstr(psi_prime, 50)}"
    )

    print(
        "K(c_0)="
        f"{mp.nstr(correction, 50)}"
    )

    for r in r_values:
        if r < 2:
            scaling_exponent = 2 + r
            target = beta * psi_prime
        elif r == 2:
            scaling_exponent = mp.mpf("4")
            target = (
                beta * psi_prime
                + correction
            )
        else:
            scaling_exponent = mp.mpf("4")
            target = correction

        print("\n" + "-" * 110)

        print(
            f"r={mp.nstr(r, 8)} "
            f"predicted exponent="
            f"{mp.nstr(scaling_exponent, 8)}"
        )

        print(
            "scaled target="
            f"{mp.nstr(target, 40)}"
        )

        previous_error = None

        for n in n_values:
            gamma = solve_near_blind_gamma(
                n=n,
                k=k,
                beta=beta,
                r=r,
            )

            q = mp.mpf(n) / gamma

            path_residual = (
                q
                -
                c_k
                -
                beta * gamma**(-r)
            )

            susceptibility = li_susceptibility_exact(
                n,
                gamma,
            )

            scaled = (
                gamma**scaling_exponent
                * susceptibility
            )

            error = abs(
                scaled - target
            )

            print(
                f"n={n:<8d} "
                f"gamma={mp.nstr(gamma, 14):>18s} "
                f"q-c={mp.nstr(q-c_k, 10):>14s} "
                f"scaled={mp.nstr(scaled, 20):>26s} "
                f"error={mp.nstr(error, 9):>14s}"
            )

            rows.append(
                {
                    "k": k,
                    "r": mp.nstr(r, 50),
                    "beta": mp.nstr(beta, 50),
                    "n": n,
                    "gamma": mp.nstr(gamma, 100),
                    "q": mp.nstr(q, 100),
                    "q_minus_c_k": mp.nstr(
                        q - c_k,
                        100,
                    ),
                    "path_residual": mp.nstr(
                        path_residual,
                        100,
                    ),
                    "predicted_effective_exponent": mp.nstr(
                        scaling_exponent,
                        50,
                    ),
                    "susceptibility": mp.nstr(
                        susceptibility,
                        100,
                    ),
                    "scaled_susceptibility": mp.nstr(
                        scaled,
                        100,
                    ),
                    "scaled_target": mp.nstr(
                        target,
                        100,
                    ),
                    "absolute_error": mp.nstr(
                        error,
                        100,
                    ),
                }
            )

            # For the late half of each sequence the asymptotic error
            # must decrease. Early transients are allowed.
            if n >= 25000:
                if previous_error is not None:
                    if error >= previous_error:
                        raise AssertionError(
                            "Near-blind transition scaling failed "
                            f"late-stage convergence for r={r}"
                        )

                previous_error = error

    with CSV_PATH.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0].keys()),
        )

        writer.writeheader()
        writer.writerows(rows)

    runtime_seconds = (
        time.perf_counter() - started
    )

    metadata = {
        "experiment_name": (
            "li_blind_scale_transition_paths"
        ),
        "mathematical_object": (
            "near-profile-zero transition asymptotics "
            "for the individual Li zero-kernel quadratic response"
        ),
        "precision_decimal_digits": mp.mp.dps,
        "numerical_backend": f"mpmath {mp.__version__}",
        "random_seed": None,
        "git_commit_at_start": commit_at_start,
        "git_clean_at_start": clean_at_start,
        "python_version": sys.version,
        "platform": platform.platform(),
        "runtime_seconds": runtime_seconds,
        "blind_scale_index": k,
        "blind_scale": mp.nstr(c_k, 100),
        "beta": mp.nstr(beta, 50),
        "r_values": [
            mp.nstr(value, 50)
            for value in r_values
        ],
        "n_values": n_values,
        "output_csv": str(CSV_PATH),
    }

    metadata["output_csv_sha256"] = (
        sha256_file(CSV_PATH)
    )

    METADATA_PATH.write_text(
        json.dumps(
            metadata,
            indent=2,
        ),
        encoding="utf-8",
    )

    print("\nCAMPAIGN COMPLETE")
    print(f"CSV: {CSV_PATH}")
    print(f"Metadata: {METADATA_PATH}")
    print(
        "CSV SHA256: "
        f"{metadata['output_csv_sha256']}"
    )


if __name__ == "__main__":
    main()
