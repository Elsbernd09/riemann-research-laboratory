"""Scaling experiment for explicit-formula kernel susceptibility."""

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

from src.explicit_formula_susceptibility import (
    explicit_formula_profile,
    scaled_normalized_susceptibility,
)


RESULT_DIR = Path(
    "results/explicit_formula_mesoscopic_scaling"
)
CSV_PATH = RESULT_DIR / "scaling_results.csv"
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

    mp.mp.dps = 140
    RESULT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    c_values = [
        mp.mpf("0.25"),
        mp.mpf("0.5"),
        mp.mpf("1"),
        mp.mpf("2"),
        mp.mpf("3"),
        mp.mpf("5"),
        mp.mpf("8"),
    ]

    gamma_values = [
        mp.mpf("50"),
        mp.mpf("100"),
        mp.mpf("250"),
        mp.mpf("500"),
        mp.mpf("1000"),
        mp.mpf("2500"),
        mp.mpf("5000"),
        mp.mpf("10000"),
    ]

    rows: list[dict[str, str]] = []

    print(
        "EXPLICIT-FORMULA MESOSCOPIC SCALING VALIDATION"
    )
    print("=" * 96)

    for c in c_values:
        target = explicit_formula_profile(c)

        print(
            f"\nc={mp.nstr(c, 10)} "
            f"target={mp.nstr(target, 24)}"
        )

        previous_error = None

        for gamma in gamma_values:
            L = c / gamma

            scaled = scaled_normalized_susceptibility(
                L,
                gamma,
            )

            phase_coordinate = L * gamma

            error = abs(
                scaled - target
            )

            print(
                f"gamma={mp.nstr(gamma, 8):>8s} "
                f"L={mp.nstr(L, 12):>16s} "
                f"Lgamma={mp.nstr(phase_coordinate, 8):>10s} "
                f"scaled={mp.nstr(scaled, 18):>24s} "
                f"error={mp.nstr(error, 10):>14s}"
            )

            rows.append(
                {
                    "c": mp.nstr(c, 50),
                    "gamma": mp.nstr(gamma, 50),
                    "L": mp.nstr(L, 80),
                    "L_gamma": mp.nstr(
                        phase_coordinate,
                        80,
                    ),
                    "scaled_normalized_susceptibility": mp.nstr(
                        scaled,
                        90,
                    ),
                    "profile_target": mp.nstr(
                        target,
                        90,
                    ),
                    "absolute_error": mp.nstr(
                        error,
                        90,
                    ),
                }
            )

            if previous_error is not None:
                if error >= previous_error:
                    raise AssertionError(
                        "Scaling error failed to decrease "
                        f"for c={c}"
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

    clean_state = (
        git_output("status", "--porcelain")
        == ""
    )

    metadata = {
        "experiment_name": (
            "explicit_formula_mesoscopic_scaling"
        ),
        "mathematical_object": (
            "gamma^3 exp(-L/2) times the quadratic "
            "susceptibility of the individual explicit-formula "
            "zero kernel p_L(z) = -exp(Lz)/z"
        ),
        "precision_decimal_digits": mp.mp.dps,
        "numerical_backend": (
            f"mpmath {mp.__version__}"
        ),
        "random_seed": None,
        "git_commit": git_output(
            "rev-parse",
            "HEAD",
        ),
        "git_clean_at_metadata_capture": (
            clean_state
        ),
        "python_version": sys.version,
        "platform": platform.platform(),
        "runtime_seconds": runtime_seconds,
        "c_values": [
            str(value)
            for value in c_values
        ],
        "gamma_values": [
            str(value)
            for value in gamma_values
        ],
        "output_csv": str(CSV_PATH),
    }

    METADATA_PATH.write_text(
        json.dumps(
            metadata,
            indent=2,
        ),
        encoding="utf-8",
    )

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

    print("\n" + "=" * 96)
    print("SCALING CAMPAIGN COMPLETE")
    print(f"CSV: {CSV_PATH}")
    print(f"Metadata: {METADATA_PATH}")
    print(
        "CSV SHA256: "
        f"{metadata['output_csv_sha256']}"
    )


if __name__ == "__main__":
    main()
