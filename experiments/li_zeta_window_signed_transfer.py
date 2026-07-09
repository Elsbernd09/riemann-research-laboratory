from __future__ import annotations

import csv
import json
import math
import platform
import statistics
import subprocess
import sys
import time
from pathlib import Path
from typing import Iterable

import mpmath as mp

import experiments.li_zeta_window_discrepancy_decomposition as dec
from src.li_susceptibility import (
    li_susceptibility_exact,
    li_susceptibility_gamma_derivative,
)


RESULT_DIR = Path(
    "results/li_zeta_window_signed_transfer"
)

POINT_CSV = RESULT_DIR / "signed_transfer_points.csv"
SUMMARY_JSON = RESULT_DIR / "summary.json"

TRANSFER_CSV = Path(
    "results/li_zeta_window_transfer_analysis/transfer_points.csv"
)


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


def mp_value(
    value: object,
) -> mp.mpf:
    return mp.mpf(str(value))


def safe_log(
    value: mp.mpf,
) -> mp.mpf | None:
    value_mp = mp.mpf(value)

    if (
        not mp.isfinite(value_mp)
        or value_mp <= 0
    ):
        return None

    return mp.log(value_mp)


def pearson_log_correlation(
    xs: Iterable[mp.mpf],
    ys: Iterable[mp.mpf],
) -> mp.mpf:
    pairs: list[
        tuple[mp.mpf, mp.mpf]
    ] = []

    for x_value, y_value in zip(xs, ys):
        log_x = safe_log(x_value)
        log_y = safe_log(y_value)

        if (
            log_x is None
            or log_y is None
        ):
            continue

        pairs.append(
            (
                log_x,
                log_y,
            )
        )

    if len(pairs) < 3:
        return mp.nan

    x_values = [
        pair[0]
        for pair in pairs
    ]

    y_values = [
        pair[1]
        for pair in pairs
    ]

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

    covariance = mp.fsum(
        (
            x_value - x_mean
        )
        *
        (
            y_value - y_mean
        )
        for x_value, y_value in pairs
    )

    x_energy = mp.fsum(
        (
            x_value - x_mean
        ) ** 2
        for x_value in x_values
    )

    y_energy = mp.fsum(
        (
            y_value - y_mean
        ) ** 2
        for y_value in y_values
    )

    denominator = mp.sqrt(
        x_energy * y_energy
    )

    if denominator == 0:
        return mp.nan

    return covariance / denominator


def median_mpf(
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


def mean_mpf(
    values: list[mp.mpf],
) -> mp.mpf:
    if not values:
        return mp.nan

    return mp.fsum(values) / len(values)


def fraction_true(
    values: Iterable[bool],
) -> mp.mpf:
    materialized = list(values)

    if not materialized:
        return mp.nan

    return (
        mp.fsum(
            mp.mpf(int(value))
            for value in materialized
        )
        /
        len(materialized)
    )


def load_transfer_lookup() -> dict[
    tuple[int, int],
    dict[str, str],
]:
    if not TRANSFER_CSV.exists():
        raise FileNotFoundError(
            f"Missing frozen Phase 5G transfer CSV: "
            f"{TRANSFER_CSV}"
        )

    with TRANSFER_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        rows = list(
            csv.DictReader(handle)
        )

    lookup: dict[
        tuple[int, int],
        dict[str, str],
    ] = {}

    for row in rows:
        key = (
            int(row["window_number"]),
            int(mp.mpf(row["requested_c"])),
        )

        if key in lookup:
            raise ValueError(
                "Duplicate Phase 5G transfer key "
                f"{key}"
            )

        lookup[key] = row

    return lookup


def main() -> None:
    started = time.perf_counter()

    mp.mp.dps = 60

    RESULT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    with dec.ZERO_CSV.open(
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

    with dec.OCCUPANCY_CSV.open(
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
                row["window_occupancy"]
            )
            >= 25
        )
    ]

    c_requested_values = [
        mp.mpf(index)
        for index in range(
            1,
            21,
        )
    ]

    transfer_lookup = (
        load_transfer_lookup()
    )

    point_rows: list[
        dict[str, str | int]
    ] = []

    print(
        "PHASE 5H — CANCELLATION-AWARE "
        "SIGNED TRANSFER"
    )
    print("=" * 112)

    print(
        f"Dense complete windows: "
        f"{len(dense_windows)}"
    )

    print(
        f"Coordinates per window: "
        f"{len(c_requested_values)}"
    )

    for window_number, row in enumerate(
        dense_windows,
        start=1,
    ):
        eta = mp.mpf(
            row["eta"]
        )

        anchor_zero_index = int(
            row["anchor_zero_index"]
        )

        # Authoritative endpoint provenance.
        #
        # This intentionally follows the repaired
        # Phase 5E implementation. Never reconstruct
        # H from the rounded display serialization in
        # the occupancy CSV.
        H = gammas[
            anchor_zero_index - 1
        ]

        B = (
            (1 + eta) * H
        )

        internal_breakpoints = [
            gamma
            for gamma in gammas
            if H < gamma < B
        ]

        quadrature_breakpoints = [
            H,
            *internal_breakpoints,
            B,
        ]

        window_gammas = [
            gamma
            for gamma in gammas
            if H <= gamma <= B
        ]

        occupancy = len(
            window_gammas
        )

        print(
            f"\nwindow={window_number:<2d} "
            f"eta={mp.nstr(eta, 5):>5s} "
            f"H={mp.nstr(H, 12):>14s} "
            f"N={occupancy:<3d}"
        )

        for c_requested in c_requested_values:
            n = max(
                1,
                int(
                    mp.nint(
                        c_requested * H
                    )
                ),
            )

            c_realized = (
                mp.mpf(n) / H
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

            E_H = dec.empirical_remainder(
                gammas,
                H,
            )

            E_B = dec.empirical_remainder(
                gammas,
                B,
            )

            atom = f(H)

            endpoint_component = (
                f(B) * E_B
                -
                f(H) * E_H
            )

            weighted_pieces: list[
                mp.mpf
            ] = []

            E_squared_pieces: list[
                mp.mpf
            ] = []

            derivative_squared_pieces: list[
                mp.mpf
            ] = []

            for left, right in zip(
                quadrature_breakpoints,
                quadrature_breakpoints[1:],
            ):
                midpoint = (
                    left + right
                ) / 2

                interval_count = (
                    dec.empirical_count(
                        gammas,
                        midpoint,
                    )
                )

                def interval_E(
                    t: mp.mpf,
                    count: int = interval_count,
                ) -> mp.mpf:
                    return (
                        mp.mpf(count)
                        -
                        dec.smooth_counting_model(
                            t
                        )
                    )

                weighted_piece = mp.quad(
                    lambda t: (
                        interval_E(t)
                        *
                        f_prime(t)
                    ),
                    [
                        left,
                        right,
                    ],
                )

                E_squared_piece = mp.quad(
                    lambda t: (
                        interval_E(t) ** 2
                    ),
                    [
                        left,
                        right,
                    ],
                )

                derivative_squared_piece = mp.quad(
                    lambda t: (
                        f_prime(t) ** 2
                    ),
                    [
                        left,
                        right,
                    ],
                )

                weighted_pieces.append(
                    weighted_piece
                )

                E_squared_pieces.append(
                    E_squared_piece
                )

                derivative_squared_pieces.append(
                    derivative_squared_piece
                )

            weighted_integral = mp.fsum(
                weighted_pieces
            )

            E_l2 = mp.sqrt(
                mp.fsum(
                    E_squared_pieces
                )
            )

            derivative_l2 = mp.sqrt(
                mp.fsum(
                    derivative_squared_pieces
                )
            )

            interior_component = (
                -weighted_integral
            )

            count_remainder = (
                atom
                +
                endpoint_component
                +
                interior_component
            )

            denominator = (
                E_l2
                *
                derivative_l2
            )

            if denominator == 0:
                kappa = mp.nan
            else:
                kappa = (
                    weighted_integral
                    /
                    denominator
                )

            if (
                mp.isfinite(kappa)
                and abs(kappa) > 1
                and abs(kappa) - 1
                < mp.mpf("1e-45")
            ):
                kappa = mp.sign(kappa)

            if (
                mp.isfinite(kappa)
                and abs(kappa)
                >
                1 + mp.mpf("1e-40")
            ):
                raise ArithmeticError(
                    "Cauchy-Schwarz violation: "
                    f"window={window_number}, "
                    f"n={n}, "
                    f"kappa={mp.nstr(kappa, 40)}"
                )

            definitional_identity_error = abs(
                interior_component
                -
                (
                    -kappa
                    *
                    denominator
                )
            )

            component_absolute_sum = (
                abs(atom)
                +
                abs(endpoint_component)
                +
                abs(interior_component)
            )

            if component_absolute_sum == 0:
                scalar_cancellation = mp.nan
            else:
                scalar_cancellation = (
                    abs(count_remainder)
                    /
                    component_absolute_sum
                )

            P_abs = denominator

            P_kappa = (
                abs(kappa)
                *
                denominator
                +
                abs(atom)
                +
                abs(endpoint_component)
            )

            transfer_key = (
                window_number,
                int(c_requested),
            )

            if (
                transfer_key
                not in transfer_lookup
            ):
                raise KeyError(
                    "No Phase 5G transfer row for "
                    f"{transfer_key}"
                )

            transfer_row = (
                transfer_lookup[
                    transfer_key
                ]
            )

            E_sup = mp_value(
                transfer_row["E_sup"]
            )

            exact_lambda = mp_value(
                transfer_row["exact_lambda"]
            )

            stored_non_atomic = mp_value(
                transfer_row[
                    "non_atomic_count_remainder"
                ]
            )

            sup_certificate = (
                abs(atom)
                +
                exact_lambda * E_sup
            )

            if sup_certificate <= 0:
                sup_tightness = mp.nan
            else:
                sup_tightness = (
                    abs(count_remainder)
                    /
                    sup_certificate
                )

            signed_closure_error = abs(
                count_remainder
                -
                (
                    atom
                    +
                    endpoint_component
                    +
                    interior_component
                )
            )

            non_atomic_reconstruction_error = abs(
                (
                    endpoint_component
                    +
                    interior_component
                )
                -
                stored_non_atomic
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
                    "anchor_zero_index": (
                        anchor_zero_index
                    ),
                    "H": mp.nstr(
                        H,
                        60,
                    ),
                    "B": mp.nstr(
                        B,
                        60,
                    ),
                    "occupancy": occupancy,
                    "requested_c": mp.nstr(
                        c_requested,
                        30,
                    ),
                    "n": n,
                    "realized_c": mp.nstr(
                        c_realized,
                        60,
                    ),
                    "E_H": mp.nstr(
                        E_H,
                        60,
                    ),
                    "E_B": mp.nstr(
                        E_B,
                        60,
                    ),
                    "atom_component": mp.nstr(
                        atom,
                        60,
                    ),
                    "endpoint_component": mp.nstr(
                        endpoint_component,
                        60,
                    ),
                    "weighted_derivative_integral": mp.nstr(
                        weighted_integral,
                        60,
                    ),
                    "interior_component": mp.nstr(
                        interior_component,
                        60,
                    ),
                    "count_remainder": mp.nstr(
                        count_remainder,
                        60,
                    ),
                    "E_l2": mp.nstr(
                        E_l2,
                        60,
                    ),
                    "derivative_l2": mp.nstr(
                        derivative_l2,
                        60,
                    ),
                    "kappa": mp.nstr(
                        kappa,
                        60,
                    ),
                    "absolute_kappa": mp.nstr(
                        abs(kappa),
                        60,
                    ),
                    "definitional_identity_error": mp.nstr(
                        definitional_identity_error,
                        60,
                    ),
                    "component_absolute_sum": mp.nstr(
                        component_absolute_sum,
                        60,
                    ),
                    "scalar_cancellation_coefficient": mp.nstr(
                        scalar_cancellation,
                        60,
                    ),
                    "P_abs": mp.nstr(
                        P_abs,
                        60,
                    ),
                    "P_kappa": mp.nstr(
                        P_kappa,
                        60,
                    ),
                    "E_sup": mp.nstr(
                        E_sup,
                        60,
                    ),
                    "exact_lambda": mp.nstr(
                        exact_lambda,
                        60,
                    ),
                    "sup_certificate": mp.nstr(
                        sup_certificate,
                        60,
                    ),
                    "sup_certificate_tightness": mp.nstr(
                        sup_tightness,
                        60,
                    ),
                    "signed_closure_error": mp.nstr(
                        signed_closure_error,
                        60,
                    ),
                    "non_atomic_reconstruction_error": mp.nstr(
                        non_atomic_reconstruction_error,
                        60,
                    ),
                }
            )

            print(
                f"  c={int(c_requested):>2d} "
                f"kappa={mp.nstr(kappa, 7):>11s} "
                f"C={mp.nstr(scalar_cancellation, 7):>11s} "
                f"Tsup={mp.nstr(sup_tightness, 7):>11s}"
            )

    if len(point_rows) != 360:
        raise RuntimeError(
            "Frozen Phase 5H population mismatch: "
            f"expected 360 points, got "
            f"{len(point_rows)}"
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

    def values(
        key: str,
    ) -> list[mp.mpf]:
        return [
            mp_value(row[key])
            for row in point_rows
        ]

    absolute_kappas = values(
        "absolute_kappa"
    )

    kappas = values(
        "kappa"
    )

    scalar_cancellations = values(
        "scalar_cancellation_coefficient"
    )

    sup_tightnesses = values(
        "sup_certificate_tightness"
    )

    count_magnitudes = [
        abs(value)
        for value in values(
            "count_remainder"
        )
    ]

    P_abs_values = values(
        "P_abs"
    )

    P_kappa_values = values(
        "P_kappa"
    )

    heights = values(
        "H"
    )

    inverse_heights = [
        1 / H
        for H in heights
    ]

    closure_errors = values(
        "signed_closure_error"
    )

    identity_errors = values(
        "definitional_identity_error"
    )

    reconstruction_errors = values(
        "non_atomic_reconstruction_error"
    )

    corr_count_P_abs = (
        pearson_log_correlation(
            count_magnitudes,
            P_abs_values,
        )
    )

    corr_count_P_kappa = (
        pearson_log_correlation(
            count_magnitudes,
            P_kappa_values,
        )
    )

    corr_tightness_cancellation = (
        pearson_log_correlation(
            sup_tightnesses,
            scalar_cancellations,
        )
    )

    corr_tightness_height = (
        pearson_log_correlation(
            sup_tightnesses,
            inverse_heights,
        )
    )

    median_absolute_kappa = (
        median_mpf(
            absolute_kappas
        )
    )

    fraction_kappa_below_005 = (
        fraction_true(
            value < mp.mpf("0.05")
            for value in absolute_kappas
        )
    )

    fraction_kappa_above_025 = (
        fraction_true(
            value > mp.mpf("0.25")
            for value in absolute_kappas
        )
    )

    fraction_C_below_05 = fraction_true(
        value < mp.mpf("0.5")
        for value in scalar_cancellations
    )

    fraction_C_below_025 = fraction_true(
        value < mp.mpf("0.25")
        for value in scalar_cancellations
    )

    p_sgn_001 = (
        max(closure_errors)
        <
        mp.mpf("1e-45")
    )

    p_sgn_002 = (
        median_absolute_kappa
        >
        mp.mpf("0.05")
    )

    p_sgn_003 = (
        corr_count_P_kappa
        >
        corr_count_P_abs
    )

    p_sgn_004 = (
        fraction_C_below_05
        >=
        mp.mpf("0.25")
    )

    p_sgn_005 = (
        abs(
            corr_tightness_cancellation
        )
        >
        abs(
            corr_tightness_height
        )
    )

    runtime_seconds = (
        time.perf_counter()
        -
        started
    )

    summary = {
        "experiment_name": (
            "li_zeta_window_signed_transfer"
        ),
        "point_count": len(
            point_rows
        ),
        "dense_window_count": len(
            dense_windows
        ),
        "coordinates_per_window": len(
            c_requested_values
        ),
        "precision_decimal_digits": (
            mp.mp.dps
        ),
        "maximum_signed_closure_error": mp.nstr(
            max(closure_errors),
            50,
        ),
        "maximum_definitional_identity_error": mp.nstr(
            max(identity_errors),
            50,
        ),
        "maximum_non_atomic_reconstruction_error": mp.nstr(
            max(reconstruction_errors),
            50,
        ),
        "minimum_kappa": mp.nstr(
            min(kappas),
            50,
        ),
        "maximum_kappa": mp.nstr(
            max(kappas),
            50,
        ),
        "median_absolute_kappa": mp.nstr(
            median_absolute_kappa,
            50,
        ),
        "mean_absolute_kappa": mp.nstr(
            mean_mpf(
                absolute_kappas
            ),
            50,
        ),
        "fraction_absolute_kappa_below_0_05": mp.nstr(
            fraction_kappa_below_005,
            50,
        ),
        "fraction_absolute_kappa_above_0_25": mp.nstr(
            fraction_kappa_above_025,
            50,
        ),
        "correlation_log_count_residual_log_P_abs": mp.nstr(
            corr_count_P_abs,
            50,
        ),
        "correlation_log_count_residual_log_P_kappa": mp.nstr(
            corr_count_P_kappa,
            50,
        ),
        "correlation_improvement_P_kappa_minus_P_abs": mp.nstr(
            corr_count_P_kappa
            -
            corr_count_P_abs,
            50,
        ),
        "median_scalar_cancellation_coefficient": mp.nstr(
            median_mpf(
                scalar_cancellations
            ),
            50,
        ),
        "fraction_scalar_cancellation_below_0_5": mp.nstr(
            fraction_C_below_05,
            50,
        ),
        "fraction_scalar_cancellation_below_0_25": mp.nstr(
            fraction_C_below_025,
            50,
        ),
        "median_sup_certificate_tightness": mp.nstr(
            median_mpf(
                sup_tightnesses
            ),
            50,
        ),
        "correlation_log_Tsup_log_Cscalar": mp.nstr(
            corr_tightness_cancellation,
            50,
        ),
        "correlation_log_Tsup_log_inverse_H": mp.nstr(
            corr_tightness_height,
            50,
        ),
        "absolute_correlation_Cscalar": mp.nstr(
            abs(
                corr_tightness_cancellation
            ),
            50,
        ),
        "absolute_correlation_inverse_H": mp.nstr(
            abs(
                corr_tightness_height
            ),
            50,
        ),
        "P_SGN_001": (
            "PASS"
            if p_sgn_001
            else "FAIL"
        ),
        "P_SGN_002": (
            "PASS"
            if p_sgn_002
            else "FAIL"
        ),
        "P_SGN_003": (
            "PASS"
            if p_sgn_003
            else "FAIL"
        ),
        "P_SGN_004": (
            "PASS"
            if p_sgn_004
            else "FAIL"
        ),
        "P_SGN_005": (
            "PASS"
            if p_sgn_005
            else "FAIL"
        ),
        "git_commit_at_start": git_output(
            "rev-parse",
            "HEAD",
        ),
        "python_version": sys.version,
        "platform": platform.platform(),
        "runtime_seconds": (
            runtime_seconds
        ),
        "interpretation_boundary": (
            "In-sample descriptive signed-transfer "
            "geometry on the frozen first-500-zero "
            "dataset. Kappa exactly reconstructs the "
            "interior component by definition. Full "
            "signed closure is an identity check, not "
            "predictive evidence. No RH consequence."
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
    print("=" * 112)
    print(
        "PHASE 5H SIGNED TRANSFER SUMMARY"
    )
    print("=" * 112)

    for key, value in summary.items():
        print(
            f"{key}: {value}"
        )

    print()
    print(
        f"Point CSV: {POINT_CSV}"
    )

    print(
        f"Summary JSON: {SUMMARY_JSON}"
    )

    print()
    print(
        "PHASE 5H SIGNED TRANSFER: COMPLETE"
    )


if __name__ == "__main__":
    main()
