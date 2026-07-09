"""Test deterministic transfer certificates and empirical explanatory power."""

from __future__ import annotations

import bisect
import csv
import json
import math
from pathlib import Path

import mpmath as mp

from src.li_susceptibility import (
    li_continuum_transfer_envelope,
    li_profile_to_transfer_ratio,
    li_susceptibility_exact,
    li_susceptibility_gamma_derivative,
    li_susceptibility_profile,
)


ZERO_CSV = Path(
    "data/zeta_zeros/"
    "mpmath_critical_line_zeros_first_500.csv"
)

OCCUPANCY_CSV = Path(
    "results/zeta_zero_data_audit/"
    "window_occupancy.csv"
)

DECOMPOSITION_CSV = Path(
    "results/"
    "li_zeta_window_discrepancy_decomposition/"
    "decomposition_components.csv"
)

ROOT_CSV = Path(
    "results/"
    "li_actual_zeta_window_response/"
    "window_root_comparison.csv"
)

CURVE_CSV = Path(
    "results/"
    "li_actual_zeta_window_response/"
    "window_curves.csv"
)

RESULT_DIR = Path(
    "results/li_zeta_window_transfer_analysis"
)

POINT_CSV = (
    RESULT_DIR / "transfer_points.csv"
)

ROOT_Q_CSV = (
    RESULT_DIR / "root_q_comparison.csv"
)

SUMMARY_JSON = (
    RESULT_DIR / "summary.json"
)


def smooth_counting_model(
    t: mp.mpf,
) -> mp.mpf:
    return (
        t
        /
        (2 * mp.pi)
        *
        mp.log(
            t / (2 * mp.pi)
        )
        -
        t
        /
        (2 * mp.pi)
        +
        mp.mpf(7) / 8
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


def pearson(
    x_values: list[mp.mpf],
    y_values: list[mp.mpf],
) -> mp.mpf:
    if len(x_values) != len(y_values):
        raise ValueError(
            "length mismatch"
        )

    if len(x_values) < 3:
        return mp.nan

    x_mean = (
        mp.fsum(x_values)
        /
        len(x_values)
    )

    y_mean = (
        mp.fsum(y_values)
        /
        len(y_values)
    )

    numerator = mp.fsum(
        (
            x - x_mean
        )
        *
        (
            y - y_mean
        )
        for x, y in zip(
            x_values,
            y_values,
        )
    )

    x_scale = mp.sqrt(
        mp.fsum(
            (x - x_mean) ** 2
            for x in x_values
        )
    )

    y_scale = mp.sqrt(
        mp.fsum(
            (y - y_mean) ** 2
            for y in y_values
        )
    )

    if (
        x_scale == 0
        or y_scale == 0
    ):
        return mp.nan

    return (
        numerator
        /
        (
            x_scale * y_scale
        )
    )


def median(
    values: list[mp.mpf],
) -> mp.mpf:
    ordered = sorted(values)

    count = len(ordered)

    if count == 0:
        return mp.nan

    midpoint = count // 2

    if count % 2 == 1:
        return ordered[midpoint]

    return (
        ordered[midpoint - 1]
        +
        ordered[midpoint]
    ) / 2


def main() -> None:
    mp.mp.dps = 60

    RESULT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

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

    dense_rows = [
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

    with DECOMPOSITION_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        decomposition_rows = list(
            csv.DictReader(handle)
        )

    decomposition_lookup = {
        (
            int(row["window_number"]),
            int(
                mp.nint(
                    mp.mpf(
                        row["requested_c"]
                    )
                )
            ),
        ): row
        for row in decomposition_rows
    }

    point_rows = []

    sup_certificate_pass_count = 0
    l2_tighter_count = 0

    log_targets = []
    log_transfer_predictors = []
    log_height_predictors = []

    print(
        "ZETA-WINDOW TRANSFER ANALYSIS"
    )

    print("=" * 110)

    for window_number, row in enumerate(
        dense_rows,
        start=1,
    ):
        eta = mp.mpf(
            row["eta"]
        )

        anchor_index = int(
            row["anchor_zero_index"]
        )

        H = gammas[
            anchor_index - 1
        ]

        B = (
            (1 + eta) * H
        )

        internal_zeros = [
            gamma
            for gamma in gammas
            if H < gamma < B
        ]

        breakpoints = [
            H,
            *internal_zeros,
            B,
        ]

        E_values_for_sup = [
            abs(
                empirical_remainder(
                    gammas,
                    point,
                )
            )
            for point in breakpoints
        ]

        # Include left limits at every internal jump.
        for gamma in internal_zeros:
            left_count = bisect.bisect_left(
                gammas,
                gamma,
            )

            E_left = (
                left_count
                -
                smooth_counting_model(
                    gamma
                )
            )

            E_values_for_sup.append(
                abs(E_left)
            )

        E_sup = max(
            E_values_for_sup
        )

        for c_requested in range(
            1,
            21,
        ):
            decomposition = (
                decomposition_lookup[
                    (
                        window_number,
                        c_requested,
                    )
                ]
            )

            n = int(
                decomposition["n"]
            )

            c_realized = mp.mpf(
                decomposition["realized_c"]
            )

            normalized_count = mp.mpf(
                decomposition[
                    "normalized_count_remainder"
                ]
            )

            atom = mp.mpf(
                decomposition[
                    "left_atom"
                ]
            )

            count_stieltjes = mp.mpf(
                decomposition[
                    "count_remainder_stieltjes"
                ]
            )

            non_atomic_count = (
                count_stieltjes
                -
                atom
            )

            def f(
                t: mp.mpf,
            ) -> mp.mpf:
                return (
                    li_susceptibility_exact(
                        n,
                        t,
                    )
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

            variation = mp.quad(
                lambda t: abs(
                    f_prime(t)
                ),
                [
                    H,
                    B,
                ],
            )

            Lambda = (
                abs(f(H))
                +
                abs(f(B))
                +
                variation
            )

            sup_certificate = (
                Lambda * E_sup
            )

            if (
                abs(non_atomic_count)
                <=
                sup_certificate
                +
                mp.mpf("1e-50")
            ):
                sup_certificate_pass_count += 1

            E_B = empirical_remainder(
                gammas,
                B,
            )

            E_H = empirical_remainder(
                gammas,
                H,
            )

            E_l2_squared_pieces = []

            fprime_l2_squared_pieces = []

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

                E_l2_squared_pieces.append(
                    mp.quad(
                        lambda t, count=interval_count: (
                            (
                                mp.mpf(count)
                                -
                                smooth_counting_model(t)
                            )
                            ** 2
                        ),
                        [
                            left,
                            right,
                        ],
                    )
                )

                fprime_l2_squared_pieces.append(
                    mp.quad(
                        lambda t: (
                            f_prime(t) ** 2
                        ),
                        [
                            left,
                            right,
                        ],
                    )
                )

            E_l2 = mp.sqrt(
                mp.fsum(
                    E_l2_squared_pieces
                )
            )

            fprime_l2 = mp.sqrt(
                mp.fsum(
                    fprime_l2_squared_pieces
                )
            )

            l2_certificate = (
                abs(f(B))
                * abs(E_B)
                +
                abs(f(H))
                * abs(E_H)
                +
                E_l2
                * fprime_l2
            )

            if (
                l2_certificate
                <
                sup_certificate
            ):
                l2_tighter_count += 1

            envelope = (
                li_continuum_transfer_envelope(
                    c_realized,
                    eta,
                )
            )

            transfer_predictor = (
                (
                    abs(
                        li_susceptibility_profile(
                            c_realized
                        )
                    )
                    +
                    envelope * E_sup
                )
                /
                (
                    H * mp.log(H)
                )
            )

            height_predictor = (
                1 / H
            )

            target = abs(
                normalized_count
            )

            if (
                target > 0
                and transfer_predictor > 0
                and height_predictor > 0
            ):
                log_targets.append(
                    mp.log(target)
                )

                log_transfer_predictors.append(
                    mp.log(
                        transfer_predictor
                    )
                )

                log_height_predictors.append(
                    mp.log(
                        height_predictor
                    )
                )

            point_rows.append(
                {
                    "window_number": (
                        window_number
                    ),
                    "eta": mp.nstr(
                        eta,
                        30,
                    ),
                    "H": mp.nstr(
                        H,
                        60,
                    ),
                    "occupancy": int(
                        row[
                            "window_occupancy"
                        ]
                    ),
                    "requested_c": (
                        c_requested
                    ),
                    "realized_c": mp.nstr(
                        c_realized,
                        60,
                    ),
                    "E_sup": mp.nstr(
                        E_sup,
                        60,
                    ),
                    "exact_lambda": mp.nstr(
                        Lambda,
                        60,
                    ),
                    "scaled_exact_lambda": mp.nstr(
                        H**2 * Lambda,
                        60,
                    ),
                    "continuum_envelope": mp.nstr(
                        envelope,
                        60,
                    ),
                    "non_atomic_count_remainder": mp.nstr(
                        non_atomic_count,
                        60,
                    ),
                    "sup_certificate": mp.nstr(
                        sup_certificate,
                        60,
                    ),
                    "l2_certificate": mp.nstr(
                        l2_certificate,
                        60,
                    ),
                    "l2_tighter_than_sup": int(
                        l2_certificate
                        <
                        sup_certificate
                    ),
                    "normalized_count_magnitude": mp.nstr(
                        target,
                        60,
                    ),
                    "continuum_transfer_predictor": mp.nstr(
                        transfer_predictor,
                        60,
                    ),
                    "height_only_predictor": mp.nstr(
                        height_predictor,
                        60,
                    ),
                }
            )

        print(
            f"window={window_number:<2d} "
            f"eta={mp.nstr(eta, 5):>5s} "
            f"H={mp.nstr(H, 10):>12s} "
            f"N={int(row['window_occupancy']):<3d} "
            f"E_sup={mp.nstr(E_sup, 8):>12s}"
        )

    with POINT_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                point_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            point_rows
        )

    # Root-neighborhood Q comparison.
    with ROOT_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        root_rows = list(
            csv.DictReader(handle)
        )

    with CURVE_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        curve_rows = list(
            csv.DictReader(handle)
        )

    dense_window_numbers = {
        int(row["window_number"])
        for row in point_rows
    }

    roots_by_window = {}

    for row in root_rows:
        window_number = int(
            row["window_number"]
        )

        if (
            int(row["occupancy"]) < 25
        ):
            continue

        roots_by_window.setdefault(
            window_number,
            [],
        ).append(
            mp.mpf(
                row["empirical_root"]
            )
        )

    curve_by_window = {}

    for row in curve_rows:
        window_number = int(
            row["window_number"]
        )

        if (
            int(row["occupancy"]) < 25
        ):
            continue

        curve_by_window.setdefault(
            window_number,
            [],
        ).append(row)

    root_q_values = []
    generic_q_values = []

    root_q_rows = []

    exclusion_radius = mp.mpf("0.5")

    for window_number, roots in (
        roots_by_window.items()
    ):
        rows = curve_by_window[
            window_number
        ]

        eta = mp.mpf(
            rows[0]["eta"]
        )

        for empirical_root in roots:
            q_value = (
                li_profile_to_transfer_ratio(
                    empirical_root,
                    eta,
                )
            )

            root_q_values.append(
                q_value
            )

            root_q_rows.append(
                {
                    "window_number": (
                        window_number
                    ),
                    "eta": mp.nstr(
                        eta,
                        30,
                    ),
                    "coordinate_type": (
                        "empirical_root"
                    ),
                    "coordinate": mp.nstr(
                        empirical_root,
                        60,
                    ),
                    "Q": mp.nstr(
                        q_value,
                        60,
                    ),
                }
            )

        for curve_row in rows:
            c_realized = mp.mpf(
                curve_row["realized_c"]
            )

            nearest_root_distance = min(
                abs(
                    c_realized - root
                )
                for root in roots
            )

            if (
                nearest_root_distance
                <
                exclusion_radius
            ):
                continue

            q_value = (
                li_profile_to_transfer_ratio(
                    c_realized,
                    eta,
                )
            )

            generic_q_values.append(
                q_value
            )

            root_q_rows.append(
                {
                    "window_number": (
                        window_number
                    ),
                    "eta": mp.nstr(
                        eta,
                        30,
                    ),
                    "coordinate_type": (
                        "generic"
                    ),
                    "coordinate": mp.nstr(
                        c_realized,
                        60,
                    ),
                    "Q": mp.nstr(
                        q_value,
                        60,
                    ),
                }
            )

    with ROOT_Q_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                root_q_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            root_q_rows
        )

    point_count = len(
        point_rows
    )

    sup_pass_rate = (
        mp.mpf(
            sup_certificate_pass_count
        )
        /
        point_count
    )

    l2_tighter_rate = (
        mp.mpf(
            l2_tighter_count
        )
        /
        point_count
    )

    root_q_median = median(
        root_q_values
    )

    generic_q_median = median(
        generic_q_values
    )

    transfer_log_correlation = pearson(
        log_targets,
        log_transfer_predictors,
    )

    height_log_correlation = pearson(
        log_targets,
        log_height_predictors,
    )

    summary = {
        "experiment_name": (
            "li_zeta_window_transfer_analysis"
        ),
        "dense_window_count": len(
            dense_rows
        ),
        "transfer_point_count": point_count,
        "sup_certificate_pass_count": (
            sup_certificate_pass_count
        ),
        "sup_certificate_pass_rate": mp.nstr(
            sup_pass_rate,
            50,
        ),
        "l2_tighter_count": (
            l2_tighter_count
        ),
        "l2_tighter_rate": mp.nstr(
            l2_tighter_rate,
            50,
        ),
        "root_q_count": len(
            root_q_values
        ),
        "generic_q_count": len(
            generic_q_values
        ),
        "root_q_median": mp.nstr(
            root_q_median,
            50,
        ),
        "generic_q_median": mp.nstr(
            generic_q_median,
            50,
        ),
        "root_to_generic_q_median_ratio": mp.nstr(
            root_q_median
            /
            generic_q_median,
            50,
        ),
        "log_residual_transfer_predictor_correlation": mp.nstr(
            transfer_log_correlation,
            50,
        ),
        "log_residual_height_only_correlation": mp.nstr(
            height_log_correlation,
            50,
        ),
        "transfer_minus_height_correlation": mp.nstr(
            transfer_log_correlation
            -
            height_log_correlation,
            50,
        ),
        "P_TRN_002_pass_rule": (
            "sup certificate pass rate must equal 1"
        ),
        "P_TRN_003_pass_rule": (
            "L2 tighter rate must exceed 0.5"
        ),
        "P_TRN_004_pass_rule": (
            "root Q median must be less than generic Q median"
        ),
        "P_TRN_005_pass_rule": (
            "log residual correlation with continuum transfer "
            "predictor must exceed correlation with 1/H"
        ),
        "interpretation_boundary": (
            "Transfer certificates are deterministic bounds. "
            "Empirical correlation tests measure explanatory "
            "power and do not affect inequality validity."
        ),
    }

    SUMMARY_JSON.write_text(
        json.dumps(
            summary,
            indent=2,
        ),
        encoding="utf-8",
    )

    print()
    print("=" * 110)

    print(
        "TRANSFER ANALYSIS SUMMARY"
    )

    print("=" * 110)

    for key, value in summary.items():
        print(
            f"{key}: {value}"
        )

    print()
    print(
        "ZETA-WINDOW TRANSFER ANALYSIS: COMPLETE"
    )

    print(
        f"Point CSV: {POINT_CSV}"
    )

    print(
        f"Root-Q CSV: {ROOT_Q_CSV}"
    )

    print(
        f"Summary: {SUMMARY_JSON}"
    )


if __name__ == "__main__":
    main()
