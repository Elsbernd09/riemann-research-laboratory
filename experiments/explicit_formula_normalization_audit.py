"""Audit exact critical-line amplitude normalization for p_L."""

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
    critical_line_point,
    explicit_formula_second_derivative_factored,
)


RESULT_DIR = Path(
    "results/explicit_formula_normalization_audit"
)
CSV_PATH = RESULT_DIR / "normalization_results.csv"
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

    mp.mp.dps = 120

    RESULT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    L_values = [
        mp.mpf("0.1"),
        mp.mpf("0.5"),
        mp.mpf("1"),
        mp.mpf("2"),
        mp.mpf("5"),
    ]

    gamma_values = [
        mp.mpf("10"),
        mp.mpf("25"),
        mp.mpf("50"),
        mp.mpf("100"),
    ]

    rows: list[dict[str, str]] = []

    print("EXPLICIT-FORMULA NORMALIZATION AUDIT")
    print("=" * 88)

    for L in L_values:
        exact_amplitude = mp.exp(L / 2)

        print(
            f"\nL={mp.nstr(L, 8)} "
            f"critical-line exp amplitude="
            f"{mp.nstr(exact_amplitude, 18)}"
        )

        for gamma in gamma_values:
            rho = critical_line_point(gamma)

            derivative = (
                explicit_formula_second_derivative_factored(
                    rho,
                    L,
                )
            )

            rational_component = -(
                L**2 / rho
                - 2 * L / rho**2
                + 2 / rho**3
            )

            exact_removed = (
                derivative
                * mp.exp(-L / 2)
            )

            expected_removed = (
                mp.exp(1j * L * gamma)
                * rational_component
            )

            error = abs(
                exact_removed
                -
                expected_removed
            )

            wrong_removed = (
                derivative
                * mp.exp(-L / 3)
            )

            wrong_ratio = abs(
                wrong_removed
                /
                expected_removed
            )

            expected_wrong_ratio = mp.exp(
                L / 6
            )

            print(
                f"gamma={mp.nstr(gamma, 8):>8s} "
                f"exact_error={mp.nstr(error, 8):>14s} "
                f"wrong_ratio={mp.nstr(wrong_ratio, 12):>16s}"
            )

            rows.append(
                {
                    "L": mp.nstr(L, 50),
                    "gamma": mp.nstr(gamma, 50),
                    "exact_amplitude": mp.nstr(
                        exact_amplitude,
                        80,
                    ),
                    "exact_removed_error": mp.nstr(
                        error,
                        80,
                    ),
                    "wrong_normalization_ratio": mp.nstr(
                        wrong_ratio,
                        80,
                    ),
                    "expected_wrong_ratio": mp.nstr(
                        expected_wrong_ratio,
                        80,
                    ),
                }
            )

            if error > mp.mpf("1e-100"):
                raise AssertionError(
                    "Exact amplitude removal failed"
                )

            if abs(
                wrong_ratio
                -
                expected_wrong_ratio
            ) > mp.mpf("1e-100"):
                raise AssertionError(
                    "Wrong-normalization scale factor "
                    "did not match prediction"
                )

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
            "explicit_formula_normalization_audit"
        ),
        "mathematical_object": (
            "exact removal of the critical-line exponential "
            "amplitude exp(L/2) from p_L''"
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
            git_output("status", "--porcelain")
            == ""
        ),
        "python_version": sys.version,
        "platform": platform.platform(),
        "runtime_seconds": runtime_seconds,
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

    print("\nNORMALIZATION AUDIT COMPLETE")
    print(f"CSV: {CSV_PATH}")
    print(f"Metadata: {METADATA_PATH}")
    print(
        "CSV SHA256: "
        f"{metadata['output_csv_sha256']}"
    )


if __name__ == "__main__":
    main()
