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


INDEX_START = 501
INDEX_END = 1500
EXPECTED_COUNT = (
    INDEX_END - INDEX_START + 1
)

WORKING_DPS = 80
VALIDATION_THRESHOLD = mp.mpf("1e-40")

RESULT_DIR = Path(
    "data/zeta_zeros"
)

ZERO_CSV = RESULT_DIR / (
    "mpmath_critical_line_zeros_"
    "indices_501_1500.csv"
)

METADATA_JSON = RESULT_DIR / (
    "mpmath_critical_line_zeros_"
    "indices_501_1500_metadata.json"
)

FIELDNAMES = [
    "zero_index",
    "gamma",
    "absolute_zeta_residual",
    "working_decimal_digits",
    "validation_threshold",
]


def git_output(
    *args: str,
) -> str:
    try:
        return subprocess.check_output(
            ["git", *args],
            text=True,
        ).strip()
    except Exception:
        return "unavailable"


def sha256_file(
    path: Path,
) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as handle:
        for chunk in iter(
            lambda: handle.read(
                1024 * 1024
            ),
            b"",
        ):
            digest.update(chunk)

    return digest.hexdigest()


def read_existing_rows() -> list[
    dict[str, str]
]:
    if not ZERO_CSV.exists():
        return []

    with ZERO_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        reader = csv.DictReader(handle)

        if reader.fieldnames != FIELDNAMES:
            raise RuntimeError(
                "Existing Phase 5L zero CSV has "
                "an unexpected schema.\n"
                f"Expected: {FIELDNAMES}\n"
                f"Observed: {reader.fieldnames}"
            )

        rows = list(reader)

    observed_indices = [
        int(row["zero_index"])
        for row in rows
    ]

    expected_indices = list(
        range(
            INDEX_START,
            INDEX_START + len(rows),
        )
    )

    if observed_indices != expected_indices:
        raise RuntimeError(
            "Existing Phase 5L zero CSV is not "
            "a contiguous authoritative prefix.\n"
            f"First observed indices: "
            f"{observed_indices[:10]}\n"
            f"Last observed indices: "
            f"{observed_indices[-10:]}"
        )

    if len(rows) > EXPECTED_COUNT:
        raise RuntimeError(
            "Existing CSV contains more than "
            f"{EXPECTED_COUNT} rows."
        )

    return rows


def append_row(
    row: dict[str, str | int],
) -> None:
    write_header = not ZERO_CSV.exists()

    with ZERO_CSV.open(
        "a",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=FIELDNAMES,
        )

        if write_header:
            writer.writeheader()

        writer.writerow(row)

        handle.flush()


def validate_existing_rows(
    rows: list[dict[str, str]],
) -> mp.mpf:
    maximum_residual = mp.mpf("0")

    for row in rows:
        index = int(
            row["zero_index"]
        )

        gamma = mp.mpf(
            row["gamma"]
        )

        stored_residual = mp.mpf(
            row["absolute_zeta_residual"]
        )

        if stored_residual >= VALIDATION_THRESHOLD:
            raise RuntimeError(
                f"Stored zero index {index} fails "
                "the frozen residual threshold: "
                f"{mp.nstr(stored_residual, 30)}"
            )

        residual = abs(
            mp.zeta(
                mp.mpf("0.5")
                +
                1j * gamma
            )
        )

        if residual >= VALIDATION_THRESHOLD:
            raise RuntimeError(
                f"Revalidation failed at zero "
                f"index {index}: "
                f"{mp.nstr(residual, 30)}"
            )

        maximum_residual = max(
            maximum_residual,
            residual,
        )

    return maximum_residual


def main() -> None:
    started = time.perf_counter()

    mp.mp.dps = WORKING_DPS

    RESULT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    existing_rows = read_existing_rows()

    print(
        "PHASE 5L — HIGHER ZETA ZERO GENERATION"
    )
    print("=" * 104)

    print(
        f"Authoritative index range: "
        f"{INDEX_START} through {INDEX_END}"
    )

    print(
        f"Expected zero count: "
        f"{EXPECTED_COUNT}"
    )

    print(
        f"Working precision: "
        f"{WORKING_DPS} dps"
    )

    print(
        "Frozen validation threshold: "
        f"{mp.nstr(VALIDATION_THRESHOLD, 10)}"
    )

    print(
        f"Existing validated rows detected: "
        f"{len(existing_rows)}"
    )

    maximum_residual = mp.mpf("0")

    if existing_rows:
        print()
        print(
            "Revalidating existing resumable prefix..."
        )

        maximum_residual = (
            validate_existing_rows(
                existing_rows
            )
        )

        print(
            "Existing prefix revalidated."
        )

        print(
            "Maximum existing revalidation residual: "
            f"{mp.nstr(maximum_residual, 12)}"
        )

    next_index = (
        INDEX_START + len(existing_rows)
    )

    if next_index <= INDEX_END:
        print()
        print(
            f"Generation resumes at authoritative "
            f"zero index {next_index}."
        )

    else:
        print()
        print(
            "All authoritative indices are already "
            "present. No generation required."
        )

    generation_started = time.perf_counter()

    for zero_index in range(
        next_index,
        INDEX_END + 1,
    ):
        item_started = time.perf_counter()

        zero = mp.zetazero(
            zero_index
        )

        gamma = mp.im(
            zero
        )

        real_part_error = abs(
            mp.re(zero)
            -
            mp.mpf("0.5")
        )

        if real_part_error > mp.mpf("1e-70"):
            raise RuntimeError(
                f"mpmath zetazero returned unexpected "
                f"real part at index {zero_index}: "
                f"{mp.nstr(mp.re(zero), 40)}"
            )

        residual = abs(
            mp.zeta(
                mp.mpf("0.5")
                +
                1j * gamma
            )
        )

        if residual >= VALIDATION_THRESHOLD:
            raise RuntimeError(
                f"P-EXT-001 numerical validation "
                f"failure at zero index {zero_index}: "
                f"|zeta|={mp.nstr(residual, 40)}"
            )

        maximum_residual = max(
            maximum_residual,
            residual,
        )

        append_row(
            {
                "zero_index": zero_index,
                "gamma": mp.nstr(
                    gamma,
                    80,
                ),
                "absolute_zeta_residual": mp.nstr(
                    residual,
                    80,
                ),
                "working_decimal_digits": (
                    WORKING_DPS
                ),
                "validation_threshold": (
                    "1e-40"
                ),
            }
        )

        item_seconds = (
            time.perf_counter()
            -
            item_started
        )

        completed = (
            zero_index - INDEX_START + 1
        )

        remaining = (
            INDEX_END - zero_index
        )

        generation_elapsed = (
            time.perf_counter()
            -
            generation_started
        )

        generated_this_run = (
            zero_index - next_index + 1
        )

        seconds_per_new_zero = (
            generation_elapsed
            /
            generated_this_run
        )

        estimated_remaining_seconds = (
            seconds_per_new_zero
            *
            remaining
        )

        print(
            f"index={zero_index:4d} "
            f"completed={completed:4d}/"
            f"{EXPECTED_COUNT} "
            f"gamma={mp.nstr(gamma, 16):>19s} "
            f"|zeta|={mp.nstr(residual, 5):>11s} "
            f"step={item_seconds:7.2f}s "
            f"ETA={estimated_remaining_seconds/60:8.1f}m",
            flush=True,
        )

    final_rows = read_existing_rows()

    observed_indices = [
        int(row["zero_index"])
        for row in final_rows
    ]

    expected_indices = list(
        range(
            INDEX_START,
            INDEX_END + 1,
        )
    )

    exact_index_validation = (
        observed_indices
        ==
        expected_indices
    )

    residuals = [
        mp.mpf(
            row["absolute_zeta_residual"]
        )
        for row in final_rows
    ]

    all_residuals_pass = (
        len(residuals) == EXPECTED_COUNT
        and all(
            residual
            <
            VALIDATION_THRESHOLD
            for residual in residuals
        )
    )

    p_ext_001 = (
        exact_index_validation
        and all_residuals_pass
        and len(final_rows)
        ==
        EXPECTED_COUNT
    )

    if not p_ext_001:
        raise RuntimeError(
            "P-EXT-001 failed final dataset audit."
        )

    gamma_values = [
        mp.mpf(row["gamma"])
        for row in final_rows
    ]

    runtime_seconds = (
        time.perf_counter()
        -
        started
    )

    metadata = {
        "dataset_name": (
            "mpmath_critical_line_zeros_"
            "indices_501_1500"
        ),
        "authoritative_index_start": (
            INDEX_START
        ),
        "authoritative_index_end": (
            INDEX_END
        ),
        "zero_count": len(
            final_rows
        ),
        "working_decimal_digits": (
            WORKING_DPS
        ),
        "validation_threshold": (
            "1e-40"
        ),
        "exact_authoritative_index_sequence": (
            exact_index_validation
        ),
        "all_stored_residuals_below_threshold": (
            all_residuals_pass
        ),
        "maximum_stored_absolute_zeta_residual": mp.nstr(
            max(residuals),
            80,
        ),
        "first_gamma": mp.nstr(
            gamma_values[0],
            80,
        ),
        "last_gamma": mp.nstr(
            gamma_values[-1],
            80,
        ),
        "strictly_increasing_gamma": all(
            left < right
            for left, right in zip(
                gamma_values,
                gamma_values[1:],
            )
        ),
        "csv_sha256": sha256_file(
            ZERO_CSV
        ),
        "P_EXT_001": (
            "PASS"
            if p_ext_001
            else "FAIL"
        ),
        "git_commit_at_generation_start": (
            git_output(
                "rev-parse",
                "HEAD",
            )
        ),
        "python_version": sys.version,
        "mpmath_version": mp.__version__,
        "platform": platform.platform(),
        "runtime_seconds_current_invocation": (
            runtime_seconds
        ),
        "interpretation_boundary": (
            "Finite numerical critical-line zero "
            "ordinates generated with mpmath.zetazero. "
            "This dataset does not prove RH, zero "
            "completeness beyond the stated numerical "
            "generation protocol, or zero simplicity."
        ),
    }

    if not metadata[
        "strictly_increasing_gamma"
    ]:
        raise RuntimeError(
            "Generated gamma sequence is not "
            "strictly increasing."
        )

    METADATA_JSON.write_text(
        json.dumps(
            metadata,
            indent=2,
        ),
        encoding="utf-8",
    )

    print()
    print("=" * 104)
    print(
        "PHASE 5L HIGHER-ZERO DATASET SUMMARY"
    )
    print("=" * 104)

    for key, value in metadata.items():
        print(
            f"{key}: {value}"
        )

    print()
    print(
        f"Zero CSV: {ZERO_CSV}"
    )

    print(
        f"Metadata JSON: {METADATA_JSON}"
    )

    print()
    print(
        "P-EXT-001: PASS"
    )

    print(
        "NO COMPONENT SHARES COMPUTED"
    )

    print(
        "NO EXTERNAL PCA METRIC INSPECTED"
    )


if __name__ == "__main__":
    main()
