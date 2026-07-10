from __future__ import annotations

import bisect
import csv
import json
import time
from pathlib import Path

import mpmath as mp

import experiments.li_zeta_window_discrepancy_decomposition as dec
from src.li_susceptibility import (
    li_susceptibility_gamma_derivative,
)


MECHANISM_CSV = Path(
    "results/"
    "li_zeta_window_principal_line_mechanism_audit/"
    "mechanism_points.csv"
)

PRIMARY_ZERO_CSV = Path(
    "data/zeta_zeros/"
    "mpmath_critical_line_zeros_first_500.csv"
)

HIGHER_ZERO_CSV = Path(
    "data/zeta_zeros/"
    "mpmath_critical_line_zeros_indices_501_1500.csv"
)

OUTPUT_JSON = Path(
    "results/"
    "li_zeta_window_principal_line_mechanism_audit/"
    "mpquad_reference_audit.json"
)

FROZEN_SELECTION = {
    "first_500": [
        1,
        120,
        240,
        360,
    ],
    "indices_501_1500": [
        1,
        140,
        280,
        420,
    ],
}

REFERENCE_RELATIVE_ERROR_THRESHOLD = mp.mpf(
    "1e-6"
)


def first500_count(
    gammas: list[mp.mpf],
    t: mp.mpf,
) -> int:
    return bisect.bisect_right(
        gammas,
        t,
    )


def higher_absolute_count(
    gammas: list[mp.mpf],
    t: mp.mpf,
) -> int:
    return (
        500
        +
        bisect.bisect_right(
            gammas,
            t,
        )
    )


def reference_absolute_integral(
    *,
    gammas: list[mp.mpf],
    H: mp.mpf,
    B: mp.mpf,
    n: int,
    count_function,
) -> mp.mpf:
    breakpoints = [
        H,
        *[
            gamma
            for gamma in gammas
            if H < gamma < B
        ],
        B,
    ]

    pieces: list[mp.mpf] = []

    for left, right in zip(
        breakpoints,
        breakpoints[1:],
    ):
        midpoint = (
            left + right
        ) / 2

        interval_count = count_function(
            gammas,
            midpoint,
        )

        def interval_E(
            t: mp.mpf,
            count: int = interval_count,
        ) -> mp.mpf:
            return (
                mp.mpf(count)
                -
                dec.smooth_counting_model(t)
            )

        pieces.append(
            mp.quad(
                lambda t: abs(
                    interval_E(t)
                    *
                    li_susceptibility_gamma_derivative(
                        n,
                        t,
                    )
                ),
                [
                    left,
                    right,
                ],
            )
        )

    return mp.fsum(pieces)


def main() -> None:
    started = time.perf_counter()

    mp.mp.dps = 60

    with MECHANISM_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        mechanism_rows = list(
            csv.DictReader(handle)
        )

    with PRIMARY_ZERO_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        primary_gammas = [
            mp.mpf(row["gamma"])
            for row in csv.DictReader(handle)
        ]

    with HIGHER_ZERO_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        higher_gammas = [
            mp.mpf(row["gamma"])
            for row in csv.DictReader(handle)
        ]

    block_configuration = {
        "first_500": (
            primary_gammas,
            first500_count,
        ),
        "indices_501_1500": (
            higher_gammas,
            higher_absolute_count,
        ),
    }

    audit_rows = []

    print(
        "PHASE 5M-D — MP.QUAD REFERENCE AUDIT"
    )
    print("=" * 104)

    print(
        "Frozen external reference threshold: "
        f"{mp.nstr(REFERENCE_RELATIVE_ERROR_THRESHOLD, 10)}"
    )

    for block_name, point_indices in (
        FROZEN_SELECTION.items()
    ):
        block_rows = [
            row
            for row in mechanism_rows
            if row["dataset_block"]
            ==
            block_name
        ]

        gammas, count_function = (
            block_configuration[
                block_name
            ]
        )

        for point_index in point_indices:
            row = block_rows[
                point_index - 1
            ]

            H = mp.mpf(row["H"])
            B = mp.mpf(row["B"])
            n = int(row["n"])

            accepted_value = mp.mpf(
                row[
                    "interior_absolute_integral"
                ]
            )

            print()
            print(
                f"block={block_name} "
                f"point={point_index} "
                f"H={mp.nstr(H, 14)} "
                f"n={n}"
            )

            reference_value = (
                reference_absolute_integral(
                    gammas=gammas,
                    H=H,
                    B=B,
                    n=n,
                    count_function=count_function,
                )
            )

            relative_error = abs(
                accepted_value
                -
                reference_value
            ) / max(
                abs(reference_value),
                mp.mpf("1e-300"),
            )

            passed = (
                relative_error
                <
                REFERENCE_RELATIVE_ERROR_THRESHOLD
            )

            audit_rows.append(
                {
                    "dataset_block": block_name,
                    "point_index": point_index,
                    "accepted_sign_split_value": (
                        mp.nstr(
                            accepted_value,
                            60,
                        )
                    ),
                    "mpquad_reference_value": (
                        mp.nstr(
                            reference_value,
                            60,
                        )
                    ),
                    "relative_error": mp.nstr(
                        relative_error,
                        60,
                    ),
                    "status": (
                        "PASS"
                        if passed
                        else "FAIL"
                    ),
                }
            )

            print(
                "  accepted: "
                f"{mp.nstr(accepted_value, 25)}"
            )

            print(
                "  reference: "
                f"{mp.nstr(reference_value, 25)}"
            )

            print(
                "  relative_error: "
                f"{mp.nstr(relative_error, 15)}"
            )

            print(
                "  status: "
                f"{'PASS' if passed else 'FAIL'}"
            )

    maximum_relative_error = max(
        mp.mpf(row["relative_error"])
        for row in audit_rows
    )

    pass_count = sum(
        row["status"] == "PASS"
        for row in audit_rows
    )

    all_pass = (
        pass_count == len(audit_rows)
    )

    audit = {
        "audit_name": (
            "phase5m_sign_split_against_mpquad"
        ),
        "selection_frozen_before_reference_values": (
            FROZEN_SELECTION
        ),
        "reference_relative_error_threshold": (
            "1e-6"
        ),
        "audit_point_count": len(
            audit_rows
        ),
        "pass_count": pass_count,
        "maximum_relative_error": mp.nstr(
            maximum_relative_error,
            60,
        ),
        "all_points_pass": all_pass,
        "point_results": audit_rows,
        "runtime_seconds": (
            time.perf_counter()
            -
            started
        ),
        "interpretation_boundary": (
            "Independent numerical reference audit "
            "against the original high-precision "
            "piecewise mp.quad absolute-integral method. "
            "This validates selected numerical values; "
            "it is not a proof of all 780 integrals."
        ),
    }

    OUTPUT_JSON.write_text(
        json.dumps(
            audit,
            indent=2,
        ),
        encoding="utf-8",
    )

    print()
    print("=" * 104)

    print(
        f"PASS COUNT: {pass_count}/"
        f"{len(audit_rows)}"
    )

    print(
        "MAXIMUM RELATIVE ERROR: "
        f"{mp.nstr(maximum_relative_error, 20)}"
    )

    print(
        "PHASE 5M-D REFERENCE AUDIT: "
        f"{'PASS' if all_pass else 'FAIL'}"
    )

    if not all_pass:
        raise RuntimeError(
            "Phase 5M-D mp.quad reference audit failed."
        )


if __name__ == "__main__":
    main()
