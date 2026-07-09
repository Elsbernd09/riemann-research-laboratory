"""Generate and validate a finite critical-line zeta-zero ordinate dataset."""

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


DATA_DIR = Path("data/zeta_zeros")

ZERO_CSV = (
    DATA_DIR
    / "mpmath_critical_line_zeros_first_500.csv"
)

METADATA_PATH = (
    DATA_DIR
    / "mpmath_critical_line_zeros_first_500_metadata.json"
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

    mp.mp.dps = 80

    zero_count = 500

    commit_at_start = git_output(
        "rev-parse",
        "HEAD",
    )

    clean_at_start = (
        git_output("status", "--porcelain")
        == ""
    )

    print("FINITE ZETA-ZERO DATA GENERATION")
    print("=" * 100)

    print(
        f"Backend: mpmath {mp.__version__}"
    )

    print(
        f"Decimal precision: {mp.mp.dps}"
    )

    print(
        f"Requested ordinates: {zero_count}"
    )

    print()

    rows: list[dict[str, str | int]] = []

    max_residual = mp.mpf("0")
    max_residual_index = None

    previous_gamma = None

    for index in range(
        1,
        zero_count + 1,
    ):
        zero = mp.zetazero(index)

        gamma = mp.im(zero)

        evaluation_point = (
            mp.mpf("0.5")
            +
            1j * gamma
        )

        zeta_value = mp.zeta(
            evaluation_point
        )

        residual = abs(zeta_value)

        if gamma <= 0:
            raise AssertionError(
                f"Nonpositive ordinate returned at index {index}"
            )

        if previous_gamma is not None:
            if gamma <= previous_gamma:
                raise AssertionError(
                    "Returned ordinates are not strictly "
                    f"increasing at index {index}"
                )

        # This is a numerical quality gate, not a theorem-level
        # certification statement.
        if residual > mp.mpf("1e-40"):
            raise AssertionError(
                "Zeta residual exceeded numerical validation "
                f"threshold at index {index}: {residual}"
            )

        if residual > max_residual:
            max_residual = residual
            max_residual_index = index

        rows.append(
            {
                "zero_index": index,
                "gamma": mp.nstr(
                    gamma,
                    75,
                ),
                "zeta_abs_residual": mp.nstr(
                    residual,
                    75,
                ),
                "decimal_precision": mp.mp.dps,
            }
        )

        previous_gamma = gamma

        if (
            index == 1
            or index % 25 == 0
            or index == zero_count
        ):
            elapsed = (
                time.perf_counter()
                - started
            )

            print(
                f"index={index:<4d} "
                f"gamma={mp.nstr(gamma, 20):>24s} "
                f"|zeta|={mp.nstr(residual, 8):>14s} "
                f"elapsed={elapsed:10.3f}s"
            )

    with ZERO_CSV.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(rows)

    runtime_seconds = (
        time.perf_counter()
        - started
    )

    zero_csv_sha256 = sha256_file(
        ZERO_CSV
    )

    metadata = {
        "dataset_name": (
            "mpmath_critical_line_zeros_first_500"
        ),
        "backend": "mpmath.zetazero",
        "mpmath_version": mp.__version__,
        "precision_decimal_digits": mp.mp.dps,
        "requested_zero_count": zero_count,
        "returned_zero_count": len(rows),
        "first_zero_index": 1,
        "last_zero_index": zero_count,
        "first_gamma": rows[0]["gamma"],
        "last_gamma": rows[-1]["gamma"],
        "maximum_zeta_abs_residual": mp.nstr(
            max_residual,
            75,
        ),
        "maximum_residual_zero_index": (
            max_residual_index
        ),
        "numerical_residual_gate": "1e-40",
        "git_commit_at_start": commit_at_start,
        "git_clean_at_start": clean_at_start,
        "python_version": sys.version,
        "platform": platform.platform(),
        "runtime_seconds": runtime_seconds,
        "zero_csv": str(ZERO_CSV),
        "zero_csv_sha256": zero_csv_sha256,
        "interpretation_boundary": (
            "Finite numerical critical-line zero ordinate "
            "dataset. Residual validation does not prove RH, "
            "zero simplicity, global zero completeness, or "
            "absence of off-critical zeros."
        ),
    }

    METADATA_PATH.write_text(
        json.dumps(
            metadata,
            indent=2,
        ),
        encoding="utf-8",
    )

    print()
    print("=" * 100)
    print("ZERO DATA GENERATION COMPLETE")
    print("=" * 100)

    print(
        f"Returned ordinates: {len(rows)}"
    )

    print(
        "Maximum |zeta| residual: "
        f"{mp.nstr(max_residual, 30)}"
    )

    print(
        "Maximum residual index: "
        f"{max_residual_index}"
    )

    print(
        f"Runtime seconds: "
        f"{runtime_seconds:.3f}"
    )

    print(
        f"CSV: {ZERO_CSV}"
    )

    print(
        "CSV SHA256: "
        f"{zero_csv_sha256}"
    )

    print(
        f"Metadata: {METADATA_PATH}"
    )


if __name__ == "__main__":
    main()
