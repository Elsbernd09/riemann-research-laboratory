"""Compare original and authoritative-anchor Phase 5C summaries."""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp


OLD_PATH = Path(
    "results/"
    "li_actual_zeta_window_response_pre_anchor_repair/"
    "summary.json"
)

NEW_PATH = Path(
    "results/"
    "li_actual_zeta_window_response/"
    "summary.json"
)


def main() -> None:
    mp.mp.dps = 80

    old = json.loads(
        OLD_PATH.read_text()
    )

    new = json.loads(
        NEW_PATH.read_text()
    )

    bands = [
        "occupancy_at_least_10",
        "occupancy_at_least_25",
        "occupancy_at_least_50",
    ]

    metrics = [
        "mean_frozen_nrmse",
        "mean_finite_height_nrmse",
        "mean_frozen_correlation",
        "mean_finite_height_correlation",
        "mean_frozen_sign_agreement",
        "mean_finite_height_sign_agreement",
        "frozen_window_root_win_rate_vs_individual",
        "finite_height_root_win_rate_vs_individual",
    ]

    print(
        "PHASE 5C AUTHORITATIVE-ANCHOR REVALIDATION"
    )

    print("=" * 110)

    for band in bands:
        old_band = old["summaries"][band]
        new_band = new["summaries"][band]

        print()
        print(band)
        print("-" * 110)

        print(
            "old window count: "
            f"{old_band['window_count']}"
        )

        print(
            "new window count: "
            f"{new_band['window_count']}"
        )

        print(
            "old empirical root count: "
            f"{old_band['empirical_root_count']}"
        )

        print(
            "new empirical root count: "
            f"{new_band['empirical_root_count']}"
        )

        for metric in metrics:
            old_value = mp.mpf(
                str(
                    old_band[metric]
                )
            )

            new_value = mp.mpf(
                str(
                    new_band[metric]
                )
            )

            delta = (
                new_value - old_value
            )

            print(
                f"{metric:<55s} "
                f"old={mp.nstr(old_value, 16):>20s} "
                f"new={mp.nstr(new_value, 16):>20s} "
                f"delta={mp.nstr(delta, 12):>16s}"
            )

    print()
    print(
        "PHASE 5C ANCHOR REVALIDATION COMPARISON: COMPLETE"
    )


if __name__ == "__main__":
    main()
