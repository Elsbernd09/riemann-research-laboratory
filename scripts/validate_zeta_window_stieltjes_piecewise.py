"""Targeted validation of the repaired piecewise Stieltjes evaluator."""

from __future__ import annotations

import bisect
import csv
from pathlib import Path

import mpmath as mp

from src.li_susceptibility import (
    li_susceptibility_exact,
    li_susceptibility_gamma_derivative,
)


ZERO_CSV = Path(
    "data/zeta_zeros/"
    "mpmath_critical_line_zeros_first_500.csv"
)

OCCUPANCY_CSV = Path(
    "results/zeta_zero_data_audit/"
    "window_occupancy.csv"
)


def smooth_counting_model(
    t: mp.mpf,
) -> mp.mpf:
    return (
        t
        / (2 * mp.pi)
        * mp.log(
            t / (2 * mp.pi)
        )
        -
        t / (2 * mp.pi)
        +
        mp.mpf(7) / 8
    )


def smooth_density(
    t: mp.mpf,
) -> mp.mpf:
    return (
        mp.log(
            t / (2 * mp.pi)
        )
        /
        (2 * mp.pi)
    )


def empirical_count(
    gammas: list[mp.mpf],
    t: mp.mpf,
) -> int:
    return bisect.bisect_right(
        gammas,
        t,
    )


def empirical_remainder(
    gammas: list[mp.mpf],
    t: mp.mpf,
) -> mp.mpf:
    return (
        empirical_count(
            gammas,
            t,
        )
        -
        smooth_counting_model(t)
    )


def main() -> None:
    mp.mp.dps = 80

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

    dense_windows = [
        row
        for row in occupancy_rows
        if (
            int(
                row[
                    "truncated_by_dataset_end"
                ]
            )
            == 0
            and int(
                row[
                    "window_occupancy"
                ]
            )
            >= 25
        )
    ]

    # Deliberately spread test cases across eta, height, and c.
    cases = [
        (0, 1),
        (3, 7),
        (8, 13),
        (12, 20),
        (17, 4),
        (17, 20),
    ]

    print(
        "PIECEWISE STIELTJES REPAIR VALIDATION"
    )

    print("=" * 110)

    maximum_error = mp.mpf("0")

    for window_position, c_requested in cases:
        row = dense_windows[
            window_position
        ]

        eta = mp.mpf(
            row["eta"]
        )

        anchor_zero_index = int(
            row["anchor_zero_index"]
        )

        # Recover H from the authoritative frozen zero dataset.
        #
        # Do not reconstruct an atomic endpoint from the rounded
        # 60-digit display value stored in the occupancy CSV.
        H = gammas[
            anchor_zero_index - 1
        ]

        B = (
            (1 + eta) * H
        )

        n = max(
            1,
            int(
                mp.nint(
                    mp.mpf(c_requested)
                    * H
                )
            ),
        )

        def f(
            t: mp.mpf,
        ) -> mp.mpf:
            return li_susceptibility_exact(
                n,
                t,
            )

        def f_prime(
            t: mp.mpf,
        ) -> mp.mpf:
            return (
                li_susceptibility_gamma_derivative(
                    n,
                    t,
                )
            )

        window_gammas = [
            gamma
            for gamma in gammas
            if H <= gamma <= B
        ]

        internal_breakpoints = [
            gamma
            for gamma in gammas
            if H < gamma < B
        ]

        breakpoints = [
            H,
            *internal_breakpoints,
            B,
        ]

        discrete = mp.fsum(
            f(gamma)
            for gamma in window_gammas
        )

        exact_smooth = mp.quad(
            lambda t: (
                f(t)
                * smooth_density(t)
            ),
            [
                H,
                B,
            ],
        )

        direct_count = (
            discrete
            -
            exact_smooth
        )

        weighted_pieces = []

        for left, right in zip(
            breakpoints,
            breakpoints[1:],
        ):
            midpoint = (
                left + right
            ) / 2

            interval_count = empirical_count(
                gammas,
                midpoint,
            )

            weighted_pieces.append(
                mp.quad(
                    lambda t, count=interval_count: (
                        (
                            mp.mpf(count)
                            -
                            smooth_counting_model(t)
                        )
                        *
                        f_prime(t)
                    ),
                    [
                        left,
                        right,
                    ],
                )
            )

        weighted_integral = mp.fsum(
            weighted_pieces
        )

        E_H = empirical_remainder(
            gammas,
            H,
        )

        E_B = empirical_remainder(
            gammas,
            B,
        )

        atom = f(H)

        stieltjes_count = (
            atom
            +
            f(B) * E_B
            -
            f(H) * E_H
            -
            weighted_integral
        )

        error = abs(
            direct_count
            -
            stieltjes_count
        )

        maximum_error = max(
            maximum_error,
            error,
        )

        print(
            f"window_position={window_position:<3d} "
            f"eta={mp.nstr(eta, 5):>6s} "
            f"H={mp.nstr(H, 12):>16s} "
            f"c={c_requested:<3d} "
            f"n={n:<6d} "
            f"direct={mp.nstr(direct_count, 22):>28s} "
            f"stieltjes={mp.nstr(stieltjes_count, 22):>28s} "
            f"error={mp.nstr(error, 10):>16s}"
        )

    print()
    print(
        "Maximum targeted repair error: "
        f"{mp.nstr(maximum_error, 30)}"
    )

    if maximum_error > mp.mpf(
        "1e-50"
    ):
        raise AssertionError(
            "Piecewise Stieltjes repair did not close "
            "to the required targeted tolerance"
        )

    print()
    print(
        "PIECEWISE STIELTJES REPAIR VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
