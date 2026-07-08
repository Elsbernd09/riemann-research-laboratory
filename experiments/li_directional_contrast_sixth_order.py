"""Reproducible experiment for the sixth-order Li contrast error law."""

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
    horizontal_vertical_contrast,
    li_susceptibility_exact,
    sixth_order_contrast_coefficient,
)


RESULT_DIR = Path("results/li_directional_contrast_sixth_order")
CSV_PATH = RESULT_DIR / "sixth_order_results.csv"
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

    mp.mp.dps = 180
    RESULT_DIR.mkdir(parents=True, exist_ok=True)

    cases = [
        (5, mp.mpf("14.134725141734693790")),
        (20, mp.mpf("50")),
        (100, mp.mpf("100")),
        (500, mp.mpf("250")),
    ]

    delta_values = [
        mp.mpf("1e-1"),
        mp.mpf("5e-2"),
        mp.mpf("2e-2"),
        mp.mpf("1e-2"),
        mp.mpf("5e-3"),
        mp.mpf("2e-3"),
        mp.mpf("1e-3"),
        mp.mpf("5e-4"),
        mp.mpf("2e-4"),
        mp.mpf("1e-4"),
    ]

    rows: list[dict[str, str | int]] = []

    print("LI DIRECTIONAL CONTRAST SIXTH-ORDER CAMPAIGN")
    print("=" * 96)

    for n, gamma in cases:
        chi = li_susceptibility_exact(n, gamma)

        target = sixth_order_contrast_coefficient(
            n,
            gamma,
        )

        print(
            f"\nn={n} gamma={mp.nstr(gamma, 18)}"
        )

        print(
            "sixth-order target="
            f"{mp.nstr(target, 24)}"
        )

        for delta in delta_values:
            contrast = horizontal_vertical_contrast(
                delta,
                gamma,
                n,
            )

            residual = (
                contrast
                -
                2 * delta**2 * chi
            )

            scaled_residual = residual / delta**6
            error = abs(scaled_residual - target)

            print(
                f"delta={mp.nstr(delta, 8):>8s} "
                f"scaled_residual={mp.nstr(scaled_residual, 20):>26s} "
                f"error={mp.nstr(error, 8):>14s}"
            )

            rows.append(
                {
                    "n": n,
                    "gamma": mp.nstr(gamma, 50),
                    "delta": mp.nstr(delta, 50),
                    "chi": mp.nstr(chi, 80),
                    "contrast": mp.nstr(contrast, 80),
                    "residual": mp.nstr(residual, 80),
                    "scaled_residual_delta6": mp.nstr(
                        scaled_residual,
                        80,
                    ),
                    "sixth_order_target": mp.nstr(
                        target,
                        80,
                    ),
                    "absolute_error": mp.nstr(
                        error,
                        80,
                    ),
                }
            )

    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0].keys()),
        )
        writer.writeheader()
        writer.writerows(rows)

    runtime_seconds = time.perf_counter() - started

    metadata = {
        "experiment_name": (
            "li_directional_contrast_sixth_order"
        ),
        "mathematical_object": (
            "sixth-order residual of the horizontal-minus-vertical "
            "four-zero Li-kernel contrast"
        ),
        "precision_decimal_digits": mp.mp.dps,
        "numerical_backend": f"mpmath {mp.__version__}",
        "random_seed": None,
        "git_commit": git_output("rev-parse", "HEAD"),
        "git_clean_at_metadata_capture": (
            git_output("status", "--porcelain") == ""
        ),
        "python_version": sys.version,
        "platform": platform.platform(),
        "runtime_seconds": runtime_seconds,
        "cases": [
            {
                "n": n,
                "gamma": str(gamma),
            }
            for n, gamma in cases
        ],
        "delta_values": [
            str(delta)
            for delta in delta_values
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

    print("\nCAMPAIGN COMPLETE")
    print(f"CSV: {CSV_PATH}")
    print(f"Metadata: {METADATA_PATH}")
    print(
        "CSV SHA256: "
        f"{metadata['output_csv_sha256']}"
    )


if __name__ == "__main__":
    main()
