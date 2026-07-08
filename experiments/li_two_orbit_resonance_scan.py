"""Adversarial cached scan of Li two-orbit resonant coefficients."""

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
)


RESULT_DIR = Path(
    "results/li_two_orbit_resonance_scan"
)

CSV_PATH = RESULT_DIR / "closest_relative_cancellations.csv"
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

    commit_at_start = git_output(
        "rev-parse",
        "HEAD",
    )

    clean_at_start = (
        git_output("status", "--porcelain")
        == ""
    )

    max_index = 199

    print("LI TWO-ORBIT RESONANCE SCAN")
    print("=" * 100)

    print(
        "Precomputing blind scales once..."
    )

    roots = [
        li_blind_scale(k)
        for k in range(max_index + 1)
    ]

    print(
        f"Cached {len(roots)} blind scales."
    )

    # K(c_k) in exact sign-explicit closed form.
    corrections = [
        (
            mp.mpf(-1) ** (k + 1)
            * roots[k] ** 2
            * mp.sqrt(
                roots[k] ** 2 + 4
            )
            / 6
        )
        for k in range(max_index + 1)
    ]

    # F(c_k) = c_k^6 sqrt(c_k^2 + 4).
    transformed = [
        roots[k] ** 6
        * mp.sqrt(
            roots[k] ** 2 + 4
        )
        for k in range(max_index + 1)
    ]

    print(
        "Checking monotone-transform ordering..."
    )

    for k in range(max_index):
        if not (
            transformed[k]
            <
            transformed[k + 1]
        ):
            raise AssertionError(
                "Monotone transform failed "
                f"numerical ordering at k={k}"
            )

    print(
        "Monotone-transform ordering: PASS"
    )

    records: list[
        dict[str, str | int]
    ] = []

    minimum_ratio: mp.mpf | None = None
    minimum_pair: tuple[int, int] | None = None

    pair_count = 0
    opposite_parity_count = 0

    print(
        "Scanning 40,000 cached ordered pairs..."
    )

    for k in range(max_index + 1):
        c_k = roots[k]
        K_k = corrections[k]

        for m in range(max_index + 1):
            pair_count += 1

            c_m = roots[m]
            K_m = corrections[m]

            ratio_scale = (
                c_m / c_k
            ) ** 4

            coefficient = (
                K_k
                +
                ratio_scale * K_m
            )

            if coefficient == 0:
                raise AssertionError(
                    "Exact resonant fourth-order "
                    "cancellation found: "
                    f"k={k}, m={m}"
                )

            if (k - m) % 2 != 0:
                opposite_parity_count += 1

                first_magnitude = abs(K_k)

                second_magnitude = (
                    ratio_scale
                    * abs(K_m)
                )

                cancellation_ratio = (
                    abs(coefficient)
                    /
                    (
                        first_magnitude
                        +
                        second_magnitude
                    )
                )

                if (
                    minimum_ratio is None
                    or
                    cancellation_ratio
                    <
                    minimum_ratio
                ):
                    minimum_ratio = (
                        cancellation_ratio
                    )

                    minimum_pair = (
                        k,
                        m,
                    )

                records.append(
                    {
                        "k": k,
                        "m": m,
                        "c_k": mp.nstr(
                            c_k,
                            80,
                        ),
                        "c_m": mp.nstr(
                            c_m,
                            80,
                        ),
                        "height_ratio_c_k_over_c_m": mp.nstr(
                            c_k / c_m,
                            80,
                        ),
                        "fourth_order_coefficient": mp.nstr(
                            coefficient,
                            80,
                        ),
                        "normalized_cancellation_ratio": mp.nstr(
                            cancellation_ratio,
                            80,
                        ),
                    }
                )

        if (
            k % 25 == 0
            or
            k == max_index
        ):
            print(
                f"Completed k={k:3d} / "
                f"{max_index}"
            )

    if minimum_ratio is None:
        raise AssertionError(
            "No opposite-parity pairs were scanned"
        )

    if minimum_pair is None:
        raise AssertionError(
            "Minimum pair was not recorded"
        )

    records.sort(
        key=lambda row: mp.mpf(
            str(
                row[
                    "normalized_cancellation_ratio"
                ]
            )
        )
    )

    top_records = records[:100]

    with CSV_PATH.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                top_records[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(top_records)

    print()
    print(
        f"Total ordered pairs checked: "
        f"{pair_count}"
    )

    print(
        "Opposite-parity ordered pairs checked: "
        f"{opposite_parity_count}"
    )

    print(
        "Minimum normalized cancellation ratio: "
        f"{mp.nstr(minimum_ratio, 30)}"
    )

    print(
        "Minimum pair: "
        f"{minimum_pair}"
    )

    print(
        "\nTen strongest relative cancellations:"
    )

    for row in top_records[:10]:
        print(
            f"k={int(row['k']):<3d} "
            f"m={int(row['m']):<3d} "
            f"ratio="
            f"{mp.nstr(mp.mpf(str(row['normalized_cancellation_ratio'])), 14):>18s} "
            f"Kagg="
            f"{mp.nstr(mp.mpf(str(row['fourth_order_coefficient'])), 14):>20s}"
        )

    runtime_seconds = (
        time.perf_counter() - started
    )

    metadata = {
        "experiment_name": (
            "li_two_orbit_resonance_scan"
        ),
        "implementation_note": (
            "Blind scales and correction coefficients "
            "were precomputed once and cached before "
            "the pair scan."
        ),
        "precision_decimal_digits": mp.mp.dps,
        "max_blind_scale_index": max_index,
        "ordered_pair_count": pair_count,
        "opposite_parity_ordered_pair_count": (
            opposite_parity_count
        ),
        "minimum_normalized_cancellation_ratio": (
            mp.nstr(
                minimum_ratio,
                100,
            )
        ),
        "minimum_pair": list(
            minimum_pair
        ),
        "git_commit_at_start": commit_at_start,
        "git_clean_at_start": clean_at_start,
        "python_version": sys.version,
        "platform": platform.platform(),
        "runtime_seconds": runtime_seconds,
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

    print(
        "\nSCAN COMPLETE"
    )

    print(
        f"Runtime seconds: "
        f"{runtime_seconds:.3f}"
    )

    print(
        f"CSV: {CSV_PATH}"
    )

    print(
        f"Metadata: {METADATA_PATH}"
    )


if __name__ == "__main__":
    main()
