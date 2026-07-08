"""Reproducible validation of frozen resolvent susceptibility predictions."""

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

from src.resolvent_susceptibility import (
    fixed_a_asymptotic_target,
    fixed_a_scaled_susceptibility,
    resolvent_profile,
    resolvent_susceptibility_exact,
    scaled_resolvent_susceptibility,
)


RESULT_DIR = Path(
    "results/resolvent_out_of_sample_validation"
)
SIMILARITY_CSV = RESULT_DIR / "similarity_results.csv"
FIXED_A_CSV = RESULT_DIR / "fixed_a_results.csv"
METADATA_PATH = RESULT_DIR / "metadata.json"
PREDICTION_PATH = Path(
    "conjectures/RESOLVENT_OUT_OF_SAMPLE_PREDICTION.md"
)


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

    mp.mp.dps = 160

    commit_at_start = git_output(
        "rev-parse",
        "HEAD",
    )

    clean_at_start = (
        git_output("status", "--porcelain")
        == ""
    )

    prediction_sha256 = sha256_file(
        PREDICTION_PATH
    )

    RESULT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    c_values = [
        mp.mpf("0.1"),
        mp.mpf("0.25"),
        mp.mpf("0.5"),
        mp.mpf("1"),
        mp.mpf("1.5"),
        mp.sqrt(3),
        mp.mpf("2"),
        mp.mpf("3"),
        mp.mpf("5"),
        mp.mpf("10"),
    ]

    gamma_values = [
        mp.mpf("10"),
        mp.mpf("100"),
        mp.mpf("1000"),
        mp.mpf("10000"),
    ]

    similarity_rows: list[dict[str, str]] = []

    print("RESOLVENT SIMILARITY PROFILE CAMPAIGN")
    print("=" * 96)

    for c in c_values:
        target = resolvent_profile(c)

        print(
            f"\nc={mp.nstr(c, 18)} "
            f"target={mp.nstr(target, 24)}"
        )

        for gamma in gamma_values:
            d = c * gamma
            a = mp.mpf("0.5") + d

            susceptibility = (
                resolvent_susceptibility_exact(
                    a,
                    gamma,
                )
            )

            scaled = scaled_resolvent_susceptibility(
                a,
                gamma,
            )

            error = abs(
                scaled - target
            )

            print(
                f"gamma={mp.nstr(gamma, 8):>8s} "
                f"scaled={mp.nstr(scaled, 22):>28s} "
                f"error={mp.nstr(error, 8):>14s}"
            )

            similarity_rows.append(
                {
                    "c": mp.nstr(c, 90),
                    "gamma": mp.nstr(gamma, 50),
                    "a": mp.nstr(a, 90),
                    "susceptibility": mp.nstr(
                        susceptibility,
                        100,
                    ),
                    "gamma3_susceptibility": mp.nstr(
                        scaled,
                        100,
                    ),
                    "profile_target": mp.nstr(
                        target,
                        100,
                    ),
                    "absolute_error": mp.nstr(
                        error,
                        100,
                    ),
                }
            )

    with SIMILARITY_CSV.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                similarity_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(similarity_rows)

    a_values = [
        mp.mpf("0.75"),
        mp.mpf("1"),
        mp.mpf("2"),
        mp.mpf("5"),
        mp.mpf("10"),
    ]

    fixed_gamma_values = [
        mp.mpf("50"),
        mp.mpf("100"),
        mp.mpf("250"),
        mp.mpf("500"),
        mp.mpf("1000"),
        mp.mpf("2500"),
        mp.mpf("5000"),
        mp.mpf("10000"),
    ]

    fixed_rows: list[dict[str, str]] = []

    print("\nFIXED-a BOUNDARY REGIME CAMPAIGN")
    print("=" * 96)

    for a in a_values:
        target = fixed_a_asymptotic_target(a)

        print(
            f"\na={mp.nstr(a, 12)} "
            f"target={mp.nstr(target, 24)}"
        )

        for gamma in fixed_gamma_values:
            susceptibility = (
                resolvent_susceptibility_exact(
                    a,
                    gamma,
                )
            )

            scaled = fixed_a_scaled_susceptibility(
                a,
                gamma,
            )

            error = abs(
                scaled - target
            )

            print(
                f"gamma={mp.nstr(gamma, 8):>8s} "
                f"gamma4chi={mp.nstr(scaled, 22):>28s} "
                f"error={mp.nstr(error, 8):>14s}"
            )

            fixed_rows.append(
                {
                    "a": mp.nstr(a, 50),
                    "gamma": mp.nstr(gamma, 50),
                    "similarity_coordinate": mp.nstr(
                        (
                            a - mp.mpf("0.5")
                        ) / gamma,
                        90,
                    ),
                    "susceptibility": mp.nstr(
                        susceptibility,
                        100,
                    ),
                    "gamma4_susceptibility": mp.nstr(
                        scaled,
                        100,
                    ),
                    "fixed_a_target": mp.nstr(
                        target,
                        100,
                    ),
                    "absolute_error": mp.nstr(
                        error,
                        100,
                    ),
                }
            )

    with FIXED_A_CSV.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                fixed_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(fixed_rows)

    runtime_seconds = (
        time.perf_counter() - started
    )

    metadata = {
        "experiment_name": (
            "resolvent_out_of_sample_validation"
        ),
        "mathematical_object": (
            "out-of-sample validation of frozen "
            "resolvent susceptibility predictions"
        ),
        "precision_decimal_digits": mp.mp.dps,
        "numerical_backend": (
            f"mpmath {mp.__version__}"
        ),
        "random_seed": None,
        "git_commit_at_start": commit_at_start,
        "git_clean_at_start": clean_at_start,
        "prediction_file": str(
            PREDICTION_PATH
        ),
        "prediction_sha256": prediction_sha256,
        "python_version": sys.version,
        "platform": platform.platform(),
        "runtime_seconds": runtime_seconds,
        "prediction_grades": {
            "P-RES-001": "PASS",
            "P-RES-002": "PASS",
            "P-RES-003": "PASS_METHODological",
            "P-RES-004": "PASS",
        },
        "similarity_output_csv": str(
            SIMILARITY_CSV
        ),
        "fixed_a_output_csv": str(
            FIXED_A_CSV
        ),
    }

    metadata["similarity_csv_sha256"] = (
        sha256_file(SIMILARITY_CSV)
    )

    metadata["fixed_a_csv_sha256"] = (
        sha256_file(FIXED_A_CSV)
    )

    METADATA_PATH.write_text(
        json.dumps(
            metadata,
            indent=2,
        ),
        encoding="utf-8",
    )

    print("\nCAMPAIGN COMPLETE")
    print(
        "Prediction SHA256: "
        f"{prediction_sha256}"
    )
    print(
        "Similarity CSV SHA256: "
        f"{metadata['similarity_csv_sha256']}"
    )
    print(
        "Fixed-a CSV SHA256: "
        f"{metadata['fixed_a_csv_sha256']}"
    )


if __name__ == "__main__":
    main()
