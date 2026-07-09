"""Audit the endpoint mismatch caused by rounded occupancy-file H values."""

from __future__ import annotations

import bisect
import csv
from pathlib import Path

import mpmath as mp


ZERO_CSV = Path(
    "data/zeta_zeros/"
    "mpmath_critical_line_zeros_first_500.csv"
)

OCCUPANCY_CSV = Path(
    "results/zeta_zero_data_audit/"
    "window_occupancy.csv"
)


def main() -> None:
    mp.mp.dps = 90

    with ZERO_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        zero_rows = list(
            csv.DictReader(handle)
        )

    gammas = [
        mp.mpf(row["gamma"])
        for row in zero_rows
    ]

    with OCCUPANCY_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        occupancy_rows = list(
            csv.DictReader(handle)
        )

    complete_rows = [
        row
        for row in occupancy_rows
        if int(
            row["truncated_by_dataset_end"]
        ) == 0
    ]

    exact_count = 0
    rounded_below_count = 0
    rounded_above_count = 0

    print("ZETA-WINDOW ANCHOR ROUNDING AUDIT")
    print("=" * 110)

    for row_number, row in enumerate(
        complete_rows,
        start=1,
    ):
        anchor_index = int(
            row["anchor_zero_index"]
        )

        authoritative_H = gammas[
            anchor_index - 1
        ]

        serialized_H = mp.mpf(
            row["H"]
        )

        difference = (
            serialized_H
            -
            authoritative_H
        )

        count_serialized = bisect.bisect_right(
            gammas,
            serialized_H,
        )

        count_left_authoritative = bisect.bisect_left(
            gammas,
            authoritative_H,
        )

        count_right_authoritative = bisect.bisect_right(
            gammas,
            authoritative_H,
        )

        authoritative_jump = (
            count_right_authoritative
            -
            count_left_authoritative
        )

        if difference == 0:
            classification = "exact"
            exact_count += 1
        elif difference < 0:
            classification = "rounded_below"
            rounded_below_count += 1
        else:
            classification = "rounded_above"
            rounded_above_count += 1

        print(
            f"row={row_number:<3d} "
            f"anchor={anchor_index:<4d} "
            f"class={classification:>13s} "
            f"H_serialized-H_exact="
            f"{mp.nstr(difference, 12):>18s} "
            f"N(serialized H)={count_serialized:<4d} "
            f"exact_jump={authoritative_jump}"
        )

        if authoritative_jump != 1:
            raise AssertionError(
                "Authoritative frozen dataset anchor "
                f"does not have unit jump at index {anchor_index}"
            )

    print()
    print("ANCHOR ROUNDING SUMMARY")
    print("=" * 110)

    print(
        f"Complete rows audited: "
        f"{len(complete_rows)}"
    )

    print(
        f"Exact serialized anchors: "
        f"{exact_count}"
    )

    print(
        f"Serialized anchors rounded below zero: "
        f"{rounded_below_count}"
    )

    print(
        f"Serialized anchors rounded above zero: "
        f"{rounded_above_count}"
    )

    print()
    print(
        "ZETA-WINDOW ANCHOR ROUNDING AUDIT: PASS"
    )


if __name__ == "__main__":
    main()
