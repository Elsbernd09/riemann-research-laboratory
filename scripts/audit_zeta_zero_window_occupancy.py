"""Audit relative-height window occupancy in the finite zeta-zero dataset."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import mpmath as mp


ZERO_CSV = Path(
    "data/zeta_zeros/"
    "mpmath_critical_line_zeros_first_500.csv"
)

RESULT_DIR = Path(
    "results/zeta_zero_data_audit"
)

OCCUPANCY_CSV = (
    RESULT_DIR
    / "window_occupancy.csv"
)

SUMMARY_PATH = (
    RESULT_DIR
    / "window_occupancy_summary.json"
)


def main() -> None:
    mp.mp.dps = 80

    RESULT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    with ZERO_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        rows = list(
            csv.DictReader(handle)
        )

    gammas = [
        mp.mpf(row["gamma"])
        for row in rows
    ]

    if len(gammas) != 500:
        raise AssertionError(
            "Expected exactly 500 zero ordinates"
        )

    eta_values = [
        mp.mpf("0.05"),
        mp.mpf("0.10"),
        mp.mpf("0.20"),
        mp.mpf("0.50"),
    ]

    # Use actual zero ordinates as reproducible H anchors.
    #
    # We deliberately spread anchors through the data range while
    # retaining enough headroom for (1 + eta) H.
    anchor_indices = [
        10,
        25,
        50,
        75,
        100,
        150,
        200,
        250,
        300,
        350,
        400,
    ]

    occupancy_rows: list[
        dict[str, str | int]
    ] = []

    print("ZETA-ZERO WINDOW OCCUPANCY AUDIT")
    print("=" * 100)

    for eta in eta_values:
        print()
        print(
            f"eta={mp.nstr(eta, 8)}"
        )

        for anchor_index in anchor_indices:
            H = gammas[
                anchor_index - 1
            ]

            upper = (
                (1 + eta) * H
            )

            window_indices = [
                index + 1
                for index, gamma in enumerate(
                    gammas
                )
                if H <= gamma <= upper
            ]

            occupancy = len(
                window_indices
            )

            first_index = (
                window_indices[0]
                if window_indices
                else None
            )

            last_index = (
                window_indices[-1]
                if window_indices
                else None
            )

            truncated_by_dataset = (
                upper > gammas[-1]
            )

            occupancy_rows.append(
                {
                    "eta": mp.nstr(
                        eta,
                        30,
                    ),
                    "anchor_zero_index": (
                        anchor_index
                    ),
                    "H": mp.nstr(
                        H,
                        60,
                    ),
                    "upper_height": mp.nstr(
                        upper,
                        60,
                    ),
                    "window_occupancy": (
                        occupancy
                    ),
                    "first_zero_index_in_window": (
                        first_index
                    ),
                    "last_zero_index_in_window": (
                        last_index
                    ),
                    "truncated_by_dataset_end": int(
                        truncated_by_dataset
                    ),
                }
            )

            print(
                f"H at zero #{anchor_index:<3d} "
                f"H={mp.nstr(H, 14):>18s} "
                f"count={occupancy:<4d} "
                f"indices={first_index}-{last_index} "
                f"truncated={truncated_by_dataset}"
            )

    with OCCUPANCY_CSV.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                occupancy_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            occupancy_rows
        )

    complete_rows = [
        row
        for row in occupancy_rows
        if int(
            row[
                "truncated_by_dataset_end"
            ]
        )
        == 0
    ]

    occupancies = [
        int(row["window_occupancy"])
        for row in complete_rows
    ]

    summary = {
        "zero_dataset_count": len(gammas),
        "first_gamma": mp.nstr(
            gammas[0],
            60,
        ),
        "last_gamma": mp.nstr(
            gammas[-1],
            60,
        ),
        "eta_values": [
            mp.nstr(
                eta,
                30,
            )
            for eta in eta_values
        ],
        "complete_window_record_count": len(
            complete_rows
        ),
        "minimum_complete_window_occupancy": min(
            occupancies
        ),
        "maximum_complete_window_occupancy": max(
            occupancies
        ),
        "windows_with_at_least_10_zeros": sum(
            occupancy >= 10
            for occupancy in occupancies
        ),
        "windows_with_at_least_25_zeros": sum(
            occupancy >= 25
            for occupancy in occupancies
        ),
        "windows_with_at_least_50_zeros": sum(
            occupancy >= 50
            for occupancy in occupancies
        ),
        "interpretation": (
            "Occupancy audit determines whether the first-500-zero "
            "dataset supports initial discrete window-response tests. "
            "Truncated windows are excluded from occupancy summaries."
        ),
    }

    SUMMARY_PATH.write_text(
        json.dumps(
            summary,
            indent=2,
        ),
        encoding="utf-8",
    )

    print()
    print("=" * 100)
    print("WINDOW OCCUPANCY SUMMARY")
    print("=" * 100)

    print(
        f"First gamma: "
        f"{mp.nstr(gammas[0], 20)}"
    )

    print(
        f"Last gamma: "
        f"{mp.nstr(gammas[-1], 20)}"
    )

    print(
        "Minimum complete-window occupancy: "
        f"{summary['minimum_complete_window_occupancy']}"
    )

    print(
        "Maximum complete-window occupancy: "
        f"{summary['maximum_complete_window_occupancy']}"
    )

    print(
        "Complete windows with >= 10 zeros: "
        f"{summary['windows_with_at_least_10_zeros']}"
    )

    print(
        "Complete windows with >= 25 zeros: "
        f"{summary['windows_with_at_least_25_zeros']}"
    )

    print(
        "Complete windows with >= 50 zeros: "
        f"{summary['windows_with_at_least_50_zeros']}"
    )

    print()
    print(
        f"Occupancy CSV: {OCCUPANCY_CSV}"
    )

    print(
        f"Summary: {SUMMARY_PATH}"
    )

    print()
    print(
        "ZETA-ZERO WINDOW OCCUPANCY AUDIT: PASS"
    )


if __name__ == "__main__":
    main()
