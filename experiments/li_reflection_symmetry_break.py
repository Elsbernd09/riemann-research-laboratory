"""Negative-control experiment for the reflection-mediated Li bridge."""

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
    asymmetric_signed_response,
    li_inverse_phase_kernel,
    li_kernel,
)


RESULT_DIR = Path("results/li_reflection_symmetry_break")
CSV_PATH = RESULT_DIR / "symmetry_break_results.csv"
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

    gamma_values = [
        mp.mpf("5"),
        mp.mpf("14"),
        mp.mpf("50"),
        mp.mpf("100"),
    ]

    horizontal_shifts = [
        mp.mpf("0.01"),
        mp.mpf("0.05"),
        mp.mpf("0.1"),
        mp.mpf("0.2"),
    ]

    n_values = [1, 2, 5, 20, 100]

    rows: list[dict[str, str | int]] = []

    print("REFLECTION-SYMMETRY NEGATIVE CONTROL")
    print("=" * 88)

    nonzero_differences = 0

    for gamma in gamma_values:
        for shift in horizontal_shifts:
            baseline = mp.mpc("0.5", gamma)
            displaced = mp.mpc(
                mp.mpf("0.5") + shift,
                gamma,
            )

            measure = [
                (displaced, 1),
                (baseline, -1),
            ]

            for n in n_values:
                f_response = asymmetric_signed_response(
                    measure,
                    n,
                    li_kernel,
                )

                g_response = asymmetric_signed_response(
                    measure,
                    n,
                    li_inverse_phase_kernel,
                )

                difference = g_response - f_response

                if abs(difference) > mp.mpf("1e-80"):
                    nonzero_differences += 1

                print(
                    f"gamma={mp.nstr(gamma, 6):>6s} "
                    f"shift={mp.nstr(shift, 6):>7s} "
                    f"n={n:<3d} "
                    f"|g-f|={mp.nstr(abs(difference), 10):>16s}"
                )

                rows.append(
                    {
                        "gamma": mp.nstr(gamma, 40),
                        "horizontal_shift": mp.nstr(shift, 40),
                        "n": n,
                        "f_response_real": mp.nstr(
                            mp.re(f_response),
                            60,
                        ),
                        "f_response_imag": mp.nstr(
                            mp.im(f_response),
                            60,
                        ),
                        "g_response_real": mp.nstr(
                            mp.re(g_response),
                            60,
                        ),
                        "g_response_imag": mp.nstr(
                            mp.im(g_response),
                            60,
                        ),
                        "difference_abs": mp.nstr(
                            abs(difference),
                            60,
                        ),
                    }
                )

    total_cases = (
        len(gamma_values)
        * len(horizontal_shifts)
        * len(n_values)
    )

    print("\nCases with numerically nonzero bridge failure:")
    print(f"{nonzero_differences} / {total_cases}")

    if nonzero_differences == 0:
        raise AssertionError(
            "Negative control failed: asymmetric perturbations "
            "unexpectedly preserved the bridge in every test case"
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
        "experiment_name": "li_reflection_symmetry_break",
        "mathematical_object": (
            "difference between standard and inverse-phase "
            "Li kernel responses on a non-reflection-invariant "
            "finite signed measure"
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
        "total_cases": total_cases,
        "nonzero_bridge_failure_cases": nonzero_differences,
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

    print("\nNEGATIVE CONTROL COMPLETE")
    print(f"CSV: {CSV_PATH}")
    print(f"Metadata: {METADATA_PATH}")
    print(f"CSV SHA256: {metadata['output_csv_sha256']}")


if __name__ == "__main__":
    main()
