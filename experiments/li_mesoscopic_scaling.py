"""Validation experiment for the Li mesoscopic susceptibility profile."""

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
    li_mesoscopic_profile,
    scaled_li_susceptibility,
)


RESULT_DIR = Path("results/li_mesoscopic_scaling")
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
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)

    return digest.hexdigest()


def main() -> None:
    started = time.perf_counter()

    mp.mp.dps = 100
    RESULT_DIR.mkdir(parents=True, exist_ok=True)

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
        mp.mpf("100"),
        mp.mpf("250"),
        mp.mpf("500"),
        mp.mpf("1000"),
        mp.mpf("2500"),
        mp.mpf("5000"),
        mp.mpf("10000"),
    ]

    rows: list[dict[str, str | int]] = []

    print("LI MESOSCOPIC SCALING VALIDATION")
    print("=" * 88)

    for c in c_values:
        target = li_mesoscopic_profile(c)

        print(
            f"\nc={mp.nstr(c, 8)} "
            f"target={mp.nstr(target, 18)}"
        )

        previous_error = None

        for gamma in gamma_values:
            n = max(1, int(mp.nint(c * gamma)))

            scaled = scaled_li_susceptibility(n, gamma)
            ratio = mp.mpf(n) / gamma
            effective_target = li_mesoscopic_profile(ratio)
            error_to_limit = abs(scaled - target)
            error_to_effective = abs(scaled - effective_target)

            print(
                f"gamma={mp.nstr(gamma, 8):>8s} "
                f"n={n:<7d} "
                f"n/gamma={mp.nstr(ratio, 8):>10s} "
                f"scaled={mp.nstr(scaled, 16):>21s} "
                f"err={mp.nstr(error_to_limit, 8):>12s}"
            )

            rows.append(
                {
                    "c_target": mp.nstr(c, 40),
                    "gamma": mp.nstr(gamma, 40),
                    "n": n,
                    "n_over_gamma": mp.nstr(ratio, 40),
                    "scaled_susceptibility": mp.nstr(scaled, 60),
                    "profile_target": mp.nstr(target, 60),
                    "effective_profile_target": mp.nstr(
                        effective_target,
                        60,
                    ),
                    "absolute_error_to_limit": mp.nstr(
                        error_to_limit,
                        60,
                    ),
                    "absolute_error_to_effective_target": mp.nstr(
                        error_to_effective,
                        60,
                    ),
                }
            )

            if previous_error is not None:
                if error_to_limit > previous_error * mp.mpf("1.05"):
                    print(
                        "  NOTE: limit error did not monotonically decrease; "
                        "integer rounding in n may contribute."
                    )

            previous_error = error_to_limit

    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0].keys()),
        )
        writer.writeheader()
        writer.writerows(rows)

    runtime_seconds = time.perf_counter() - started

    clean_state = git_output("status", "--porcelain") == ""

    metadata = {
        "experiment_name": "li_mesoscopic_scaling",
        "mathematical_object": (
            "gamma^2 times the signed quadratic susceptibility "
            "of the individual Li zero kernel"
        ),
        "precision_decimal_digits": mp.mp.dps,
        "numerical_backend": f"mpmath {mp.__version__}",
        "random_seed": None,
        "git_commit": git_output("rev-parse", "HEAD"),
        "git_clean_at_metadata_capture": clean_state,
        "python_version": sys.version,
        "platform": platform.platform(),
        "runtime_seconds": runtime_seconds,
        "parameter_c_values": [str(value) for value in c_values],
        "parameter_gamma_values": [
            str(value) for value in gamma_values
        ],
        "output_csv": str(CSV_PATH),
    }

    METADATA_PATH.write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )

    metadata["output_csv_sha256"] = sha256_file(CSV_PATH)

    METADATA_PATH.write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )

    print("\n" + "=" * 88)
    print("SCALING EXPERIMENT COMPLETE")
    print(f"CSV: {CSV_PATH}")
    print(f"Metadata: {METADATA_PATH}")
    print(f"CSV SHA256: {metadata['output_csv_sha256']}")


if __name__ == "__main__":
    main()
