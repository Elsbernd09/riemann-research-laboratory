from __future__ import annotations

import bisect
import csv
import hashlib
import json
import math
import platform
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Callable

import mpmath as mp
import numpy as np

import experiments.li_zeta_window_discrepancy_decomposition as dec
from src.li_susceptibility import (
    li_susceptibility_gamma_derivative,
)


PRIMARY_POINT_CSV = Path(
    "results/li_zeta_window_signed_transfer/"
    "signed_transfer_points.csv"
)

HIGHER_POINT_CSV = Path(
    "results/li_zeta_window_higher_zero_external_replication/"
    "external_simplex_points.csv"
)

PRIMARY_ZERO_CSV = Path(
    "data/zeta_zeros/"
    "mpmath_critical_line_zeros_first_500.csv"
)

HIGHER_ZERO_CSV = Path(
    "data/zeta_zeros/"
    "mpmath_critical_line_zeros_indices_501_1500.csv"
)

FROZEN_AXIS_JSON = Path(
    "results/phase5l_frozen_primary_axis.json"
)

HIGHER_DATASET_AUDIT_JSON = Path(
    "results/phase5l_higher_zero_dataset_audit.json"
)

RESULT_DIR = Path(
    "results/li_zeta_window_principal_line_mechanism_audit"
)

POINT_CSV = RESULT_DIR / "mechanism_points.csv"
BLOCK_CSV = RESULT_DIR / "block_scaling_metrics.csv"
SUMMARY_JSON = RESULT_DIR / "summary.json"


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
            lambda: handle.read(1024 * 1024),
            b"",
        ):
            digest.update(chunk)

    return digest.hexdigest()


def mp_value(
    value: object,
) -> mp.mpf:
    return mp.mpf(str(value))


def dot(
    left: mp.matrix,
    right: mp.matrix,
) -> mp.mpf:
    return mp.fsum(
        left[index] * right[index]
        for index in range(3)
    )


def squared_norm(
    vector: mp.matrix,
) -> mp.mpf:
    return dot(
        vector,
        vector,
    )


def unit_vector(
    vector: mp.matrix,
) -> mp.matrix:
    norm = mp.sqrt(
        squared_norm(vector)
    )

    if norm == 0:
        raise ArithmeticError(
            "Cannot normalize zero vector."
        )

    return vector / norm


def median_mpf(
    values: list[mp.mpf],
) -> mp.mpf:
    if not values:
        return mp.nan

    ordered = sorted(values)
    count = len(ordered)
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
    values: list[bool],
) -> mp.mpf:
    if not values:
        return mp.nan

    return (
        mp.fsum(
            mp.mpf(int(value))
            for value in values
        )
        /
        len(values)
    )


def linear_regression_log_slope(
    xs: list[mp.mpf],
    ys: list[mp.mpf],
) -> tuple[
    mp.mpf,
    mp.mpf,
    mp.mpf,
    int,
]:
    pairs = [
        (
            mp.log(x),
            mp.log(y),
        )
        for x, y in zip(xs, ys)
        if (
            mp.isfinite(x)
            and mp.isfinite(y)
            and x > 0
            and y > 0
        )
    ]

    if len(pairs) < 3:
        return (
            mp.nan,
            mp.nan,
            mp.nan,
            len(pairs),
        )

    x_values = [
        pair[0]
        for pair in pairs
    ]

    y_values = [
        pair[1]
        for pair in pairs
    ]

    x_mean = mean_mpf(
        x_values
    )

    y_mean = mean_mpf(
        y_values
    )

    x_energy = mp.fsum(
        (
            value - x_mean
        ) ** 2
        for value in x_values
    )

    if x_energy == 0:
        return (
            mp.nan,
            mp.nan,
            mp.nan,
            len(pairs),
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

    slope = covariance / x_energy

    intercept = (
        y_mean
        -
        slope * x_mean
    )

    fitted = [
        intercept
        +
        slope * x_value
        for x_value in x_values
    ]

    ss_total = mp.fsum(
        (
            value - y_mean
        ) ** 2
        for value in y_values
    )

    ss_residual = mp.fsum(
        (
            actual - predicted
        ) ** 2
        for actual, predicted in zip(
            y_values,
            fitted,
        )
    )

    if ss_total == 0:
        r_squared = mp.nan
    else:
        r_squared = (
            1
            -
            ss_residual / ss_total
        )

    return (
        slope,
        intercept,
        r_squared,
        len(pairs),
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


def li_susceptibility_gamma_derivative_float(
    n: int,
    gamma: np.ndarray,
) -> np.ndarray:
    """Vectorized float64 evaluation of the exact gamma derivative.

    Formula matches src.li_susceptibility.
    """
    gamma_array = np.asarray(
        gamma,
        dtype=np.float64,
    )

    n_float = float(n)

    D = (
        gamma_array * gamma_array
        +
        0.25
    )

    theta = 2.0 * np.arctan(
        1.0
        /
        (
            2.0 * gamma_array
        )
    )

    phase = (
        n_float * theta
    )

    sin_phase = np.sin(
        phase
    )

    cos_phase = np.cos(
        phase
    )

    A = (
        n_float * cos_phase
        +
        2.0
        *
        gamma_array
        *
        sin_phase
    )

    A_prime = (
        (
            n_float
            *
            n_float
            /
            D
        )
        *
        sin_phase
        +
        2.0
        *
        sin_phase
        -
        (
            2.0
            *
            n_float
            *
            gamma_array
            /
            D
        )
        *
        cos_phase
    )

    return (
        (
            8.0
            *
            n_float
            *
            gamma_array
            /
            (
                D ** 3
            )
        )
        *
        A
        -
        (
            2.0
            *
            n_float
            /
            (
                D ** 2
            )
        )
        *
        A_prime
    )


def smooth_counting_model_float(
    t: np.ndarray,
) -> np.ndarray:
    """Float64 form of the Phase 5E smooth counting model."""
    t_array = np.asarray(
        t,
        dtype=np.float64,
    )

    return (
        (
            t_array
            /
            (
                2.0 * np.pi
            )
        )
        *
        np.log(
            t_array
            /
            (
                2.0 * np.pi
            )
        )
        -
        (
            t_array
            /
            (
                2.0 * np.pi
            )
        )
        +
        7.0 / 8.0
    )


def composite_gauss_legendre_absolute_integral(
    *,
    gammas: list[mp.mpf],
    H: mp.mpf,
    B: mp.mpf,
    n: int,
    empirical_count: Callable[
        [list[mp.mpf], mp.mpf],
        int,
    ],
    order: int,
    subpanels_per_zero_interval: int,
) -> mp.mpf:
    """Composite piecewise Gauss-Legendre integration.

    Each empirical-count interval is first identified
    using authoritative zero ordinates.

    The empirical staircase count is frozen on that open
    zero interval.

    Each zero interval is then divided uniformly into
    smaller quadrature panels before Gauss-Legendre
    evaluation. This improves resolution of sign changes
    in E_D(t) * chi_n'(t) before the absolute value.
    """
    if order < 1:
        raise ValueError(
            "order must be positive."
        )

    if subpanels_per_zero_interval < 1:
        raise ValueError(
            "subpanels_per_zero_interval must "
            "be positive."
        )

    internal_breakpoints = [
        gamma
        for gamma in gammas
        if H < gamma < B
    ]

    zero_breakpoints_mp = [
        H,
        *internal_breakpoints,
        B,
    ]

    zero_left = np.asarray(
        [
            float(value)
            for value in zero_breakpoints_mp[:-1]
        ],
        dtype=np.float64,
    )

    zero_right = np.asarray(
        [
            float(value)
            for value in zero_breakpoints_mp[1:]
        ],
        dtype=np.float64,
    )

    interval_counts = np.asarray(
        [
            empirical_count(
                gammas,
                (
                    zero_breakpoints_mp[index]
                    +
                    zero_breakpoints_mp[index + 1]
                )
                /
                2
            )
            for index in range(
                len(zero_breakpoints_mp) - 1
            )
        ],
        dtype=np.float64,
    )

    subdivision_edges = np.linspace(
        0.0,
        1.0,
        subpanels_per_zero_interval + 1,
        dtype=np.float64,
    )

    fractions_left = subdivision_edges[:-1]
    fractions_right = subdivision_edges[1:]

    zero_width = (
        zero_right - zero_left
    )

    panel_left = (
        zero_left[:, None]
        +
        zero_width[:, None]
        *
        fractions_left[None, :]
    )

    panel_right = (
        zero_left[:, None]
        +
        zero_width[:, None]
        *
        fractions_right[None, :]
    )

    panel_midpoint = (
        panel_left + panel_right
    ) / 2.0

    panel_half_width = (
        panel_right - panel_left
    ) / 2.0

    nodes, weights = (
        np.polynomial.legendre.leggauss(
            order
        )
    )

    sample_points = (
        panel_midpoint[:, :, None]
        +
        panel_half_width[:, :, None]
        *
        nodes[None, None, :]
    )

    E_values = (
        interval_counts[:, None, None]
        -
        smooth_counting_model_float(
            sample_points
        )
    )

    derivative_values = (
        li_susceptibility_gamma_derivative_float(
            n,
            sample_points,
        )
    )

    integrand = np.abs(
        E_values
        *
        derivative_values
    )

    panel_integrals = (
        panel_half_width
        *
        np.sum(
            integrand
            *
            weights[None, None, :],
            axis=2,
        )
    )

    result = np.sum(
        panel_integrals,
        dtype=np.float64,
    )

    if (
        not np.isfinite(result)
        or result <= 0
    ):
        raise ArithmeticError(
            "Invalid composite quadrature "
            "absolute integral: "
            f"{result}"
        )

    return mp.mpf(
        repr(
            float(result)
        )
    )


def build_absolute_integral(
    *,
    gammas: list[mp.mpf],
    H: mp.mpf,
    B: mp.mpf,
    n: int,
    empirical_count: Callable[
        [list[mp.mpf], mp.mpf],
        int,
    ],
) -> tuple[
    mp.mpf,
    mp.mpf,
]:
    """Return fine composite value and coarse/fine discrepancy.

    Coarse rule:
        8 subpanels per zero interval,
        16 Gauss-Legendre nodes per subpanel.

    Fine rule:
        16 subpanels per zero interval,
        32 Gauss-Legendre nodes per subpanel.

    The frozen acceptance threshold remains 1e-7.
    """
    coarse_value = (
        composite_gauss_legendre_absolute_integral(
            gammas=gammas,
            H=H,
            B=B,
            n=n,
            empirical_count=empirical_count,
            order=16,
            subpanels_per_zero_interval=8,
        )
    )

    fine_value = (
        composite_gauss_legendre_absolute_integral(
            gammas=gammas,
            H=H,
            B=B,
            n=n,
            empirical_count=empirical_count,
            order=32,
            subpanels_per_zero_interval=16,
        )
    )

    relative_discrepancy = (
        abs(
            fine_value
            -
            coarse_value
        )
        /
        max(
            abs(fine_value),
            mp.mpf("1e-300"),
        )
    )

    if (
        relative_discrepancy
        >
        mp.mpf("1e-7")
    ):
        raise ArithmeticError(
            "Phase 5M composite-quadrature "
            "self-convergence failure: "
            f"relative discrepancy="
            f"{mp.nstr(relative_discrepancy, 30)}, "
            f"H={mp.nstr(H, 20)}, "
            f"B={mp.nstr(B, 20)}, "
            f"n={n}"
        )

    return (
        fine_value,
        relative_discrepancy,
    )


def edge_projection(
    vector: mp.matrix,
) -> mp.matrix:
    # Elementary simplex edge:
    #
    # i = 0
    # a + e = 1
    #
    # Base point and unit direction.
    base = mp.matrix(
        [
            mp.mpf("0.5"),
            mp.mpf("0.5"),
            mp.mpf("0"),
        ]
    )

    direction = mp.matrix(
        [
            1 / mp.sqrt(2),
            -1 / mp.sqrt(2),
            mp.mpf("0"),
        ]
    )

    coordinate = dot(
        vector - base,
        direction,
    )

    return (
        base
        +
        coordinate * direction
    )


def fixed_line_explained_fraction(
    vectors: list[mp.matrix],
    *,
    denominator_centroid: mp.matrix,
    projection_function: Callable[
        [mp.matrix],
        mp.matrix,
    ],
) -> mp.mpf:
    residual_energy = mp.fsum(
        squared_norm(
            vector
            -
            projection_function(
                vector
            )
        )
        for vector in vectors
    )

    centered_energy = mp.fsum(
        squared_norm(
            vector
            -
            denominator_centroid
        )
        for vector in vectors
    )

    if centered_energy == 0:
        return mp.nan

    return (
        1
        -
        residual_energy
        /
        centered_energy
    )


def main() -> None:
    started = time.perf_counter()

    mp.mp.dps = 60

    required_paths = (
        PRIMARY_POINT_CSV,
        HIGHER_POINT_CSV,
        PRIMARY_ZERO_CSV,
        HIGHER_ZERO_CSV,
        FROZEN_AXIS_JSON,
        HIGHER_DATASET_AUDIT_JSON,
    )

    for path in required_paths:
        if not path.exists():
            raise FileNotFoundError(
                f"Missing required Phase 5M artifact: "
                f"{path}"
            )

    RESULT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    frozen = json.loads(
        FROZEN_AXIS_JSON.read_text(
            encoding="utf-8"
        )
    )

    higher_audit = json.loads(
        HIGHER_DATASET_AUDIT_JSON.read_text(
            encoding="utf-8"
        )
    )

    if (
        sha256_file(
            Path(
                frozen["source_csv"]
            )
        )
        !=
        frozen["source_csv_sha256"]
    ):
        raise RuntimeError(
            "Frozen first-500 simplex source "
            "hash drift detected."
        )

    if (
        sha256_file(
            HIGHER_ZERO_CSV
        )
        !=
        higher_audit[
            "current_higher_zero_sha256"
        ]
    ):
        raise RuntimeError(
            "Higher-zero dataset hash drift "
            "detected."
        )

    frozen_centroid = mp.matrix(
        [
            mp.mpf(value)
            for value in frozen[
                "centroid"
            ]
        ]
    )

    frozen_axis = unit_vector(
        mp.matrix(
            [
                mp.mpf(value)
                for value in frozen[
                    "canonical_principal_axis"
                ]
            ]
        )
    )

    atom_endpoint_axis = unit_vector(
        mp.matrix(
            [
                mp.mpf("1"),
                mp.mpf("-1"),
                mp.mpf("0"),
            ]
        )
    )

    exchange_axis_alignment = abs(
        dot(
            frozen_axis,
            atom_endpoint_axis,
        )
    )

    with PRIMARY_POINT_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        primary_rows = list(
            csv.DictReader(handle)
        )

    with HIGHER_POINT_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        higher_rows = list(
            csv.DictReader(handle)
        )

    if len(primary_rows) != 360:
        raise RuntimeError(
            "Expected 360 first-500 mechanism "
            f"points, got {len(primary_rows)}."
        )

    with PRIMARY_ZERO_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        primary_zero_rows = list(
            csv.DictReader(handle)
        )

    with HIGHER_ZERO_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        higher_zero_rows = list(
            csv.DictReader(handle)
        )

    primary_gammas = [
        mp.mpf(row["gamma"])
        for row in primary_zero_rows
    ]

    higher_gammas = [
        mp.mpf(row["gamma"])
        for row in higher_zero_rows
    ]

    mechanism_rows: list[
        dict[str, str | int]
    ] = []

    print(
        "PHASE 5M — ANALYTIC ORIGIN OF THE "
        "REPLICATED PRINCIPAL LINE"
    )
    print("=" * 116)

    print(
        f"First-500 points: {len(primary_rows)}"
    )

    print(
        f"Higher-zero points: {len(higher_rows)}"
    )

    print(
        "Frozen-axis alignment with "
        "(1,-1,0)/sqrt(2): "
        f"{mp.nstr(exchange_axis_alignment, 16)}"
    )

    block_specs = (
        (
            "first_500",
            primary_rows,
            primary_gammas,
            first500_count,
        ),
        (
            "indices_501_1500",
            higher_rows,
            higher_gammas,
            higher_absolute_count,
        ),
    )

    for (
        block_name,
        source_rows,
        gammas,
        count_function,
    ) in block_specs:
        print()
        print(
            f"BLOCK: {block_name}"
        )
        print("-" * 116)

        for point_number, row in enumerate(
            source_rows,
            start=1,
        ):
            H = mp_value(
                row["H"]
            )

            B = mp_value(
                row["B"]
            )

            n = int(
                row["n"]
            )

            atom_magnitude = abs(
                mp_value(
                    row["atom_component"]
                )
            )

            endpoint_magnitude = abs(
                mp_value(
                    row["endpoint_component"]
                )
            )

            interior_magnitude = abs(
                mp_value(
                    row["interior_component"]
                )
            )

            magnitude_sum = (
                atom_magnitude
                +
                endpoint_magnitude
                +
                interior_magnitude
            )

            if magnitude_sum <= 0:
                raise ArithmeticError(
                    "Nonpositive component magnitude sum."
                )

            interior_share = (
                interior_magnitude
                /
                magnitude_sum
            )

            (
                absolute_integral,
                quadrature_relative_discrepancy,
            ) = build_absolute_integral(
                gammas=gammas,
                H=H,
                B=B,
                n=n,
                empirical_count=count_function,
            )

            if absolute_integral <= 0:
                raise ArithmeticError(
                    "Nonpositive interior absolute "
                    "integral scale."
                )

            cancellation_ratio = (
                interior_magnitude
                /
                absolute_integral
            )

            if (
                cancellation_ratio
                >
                1
                +
                mp.mpf("1e-40")
            ):
                raise ArithmeticError(
                    "Triangle-inequality violation in "
                    "interior cancellation ratio: "
                    f"{mp.nstr(cancellation_ratio, 40)}"
                )

            if (
                cancellation_ratio > 1
                and cancellation_ratio - 1
                <
                mp.mpf("1e-40")
            ):
                cancellation_ratio = mp.mpf("1")

            mechanism_rows.append(
                {
                    "dataset_block": block_name,
                    "point_number_within_block": (
                        point_number
                    ),
                    "window_number": int(
                        row["window_number"]
                    ),
                    "H": mp.nstr(
                        H,
                        60,
                    ),
                    "B": mp.nstr(
                        B,
                        60,
                    ),
                    "eta": row["eta"],
                    "requested_c": row[
                        "requested_c"
                    ],
                    "n": n,
                    "atom_magnitude": mp.nstr(
                        atom_magnitude,
                        60,
                    ),
                    "endpoint_magnitude": mp.nstr(
                        endpoint_magnitude,
                        60,
                    ),
                    "interior_magnitude": mp.nstr(
                        interior_magnitude,
                        60,
                    ),
                    "interior_share": mp.nstr(
                        interior_share,
                        60,
                    ),
                    "interior_absolute_integral": mp.nstr(
                        absolute_integral,
                        60,
                    ),
                    "quadrature_composite_relative_discrepancy": mp.nstr(
                        quadrature_relative_discrepancy,
                        60,
                    ),
                    "interior_cancellation_ratio": mp.nstr(
                        cancellation_ratio,
                        60,
                    ),
                }
            )

            if (
                point_number == 1
                or point_number % 20 == 0
                or point_number
                ==
                len(source_rows)
            ):
                print(
                    f"  point={point_number:4d}/"
                    f"{len(source_rows):4d} "
                    f"H={mp.nstr(H, 11):>13s} "
                    f"i={mp.nstr(interior_share, 7):>11s} "
                    f"Cint={mp.nstr(cancellation_ratio, 7):>11s}",
                    flush=True,
                )

    with POINT_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                mechanism_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            mechanism_rows
        )

    rows_by_block: dict[
        str,
        list[dict[str, str | int]],
    ] = defaultdict(list)

    for row in mechanism_rows:
        rows_by_block[
            str(row["dataset_block"])
        ].append(row)

    block_summary_rows: list[
        dict[str, str | int]
    ] = []

    block_summaries: dict[
        str,
        dict[str, object],
    ] = {}

    for block_name in (
        "first_500",
        "indices_501_1500",
    ):
        rows = rows_by_block[
            block_name
        ]

        heights = [
            mp_value(row["H"])
            for row in rows
        ]

        interior_shares = [
            mp_value(
                row["interior_share"]
            )
            for row in rows
        ]

        atom_magnitudes = [
            mp_value(
                row["atom_magnitude"]
            )
            for row in rows
        ]

        endpoint_magnitudes = [
            mp_value(
                row["endpoint_magnitude"]
            )
            for row in rows
        ]

        interior_magnitudes = [
            mp_value(
                row["interior_magnitude"]
            )
            for row in rows
        ]

        cancellation_ratios = [
            mp_value(
                row[
                    "interior_cancellation_ratio"
                ]
            )
            for row in rows
        ]

        (
            interior_share_slope,
            interior_share_intercept,
            interior_share_r_squared,
            interior_share_fit_count,
        ) = linear_regression_log_slope(
            heights,
            interior_shares,
        )

        (
            atom_slope,
            atom_intercept,
            atom_r_squared,
            atom_fit_count,
        ) = linear_regression_log_slope(
            heights,
            atom_magnitudes,
        )

        (
            endpoint_slope,
            endpoint_intercept,
            endpoint_r_squared,
            endpoint_fit_count,
        ) = linear_regression_log_slope(
            heights,
            endpoint_magnitudes,
        )

        (
            interior_slope,
            interior_intercept,
            interior_r_squared,
            interior_fit_count,
        ) = linear_regression_log_slope(
            heights,
            interior_magnitudes,
        )

        median_cancellation_ratio = (
            median_mpf(
                cancellation_ratios
            )
        )

        strong_cancellation_fraction = (
            fraction_true(
                [
                    value
                    <
                    mp.mpf("0.25")
                    for value in cancellation_ratios
                ]
            )
        )

        very_strong_cancellation_fraction = (
            fraction_true(
                [
                    value
                    <
                    mp.mpf("0.10")
                    for value in cancellation_ratios
                ]
            )
        )

        block_summary = {
            "point_count": len(rows),
            "minimum_H": mp.nstr(
                min(heights),
                50,
            ),
            "maximum_H": mp.nstr(
                max(heights),
                50,
            ),
            "median_interior_share": mp.nstr(
                median_mpf(
                    interior_shares
                ),
                50,
            ),
            "mean_interior_share": mp.nstr(
                mean_mpf(
                    interior_shares
                ),
                50,
            ),
            "log_interior_share_vs_log_H_slope": mp.nstr(
                interior_share_slope,
                50,
            ),
            "log_interior_share_vs_log_H_R_squared": mp.nstr(
                interior_share_r_squared,
                50,
            ),
            "log_atom_magnitude_vs_log_H_slope": mp.nstr(
                atom_slope,
                50,
            ),
            "log_atom_magnitude_vs_log_H_R_squared": mp.nstr(
                atom_r_squared,
                50,
            ),
            "log_endpoint_magnitude_vs_log_H_slope": mp.nstr(
                endpoint_slope,
                50,
            ),
            "log_endpoint_magnitude_vs_log_H_R_squared": mp.nstr(
                endpoint_r_squared,
                50,
            ),
            "log_interior_magnitude_vs_log_H_slope": mp.nstr(
                interior_slope,
                50,
            ),
            "log_interior_magnitude_vs_log_H_R_squared": mp.nstr(
                interior_r_squared,
                50,
            ),
            "median_interior_cancellation_ratio": mp.nstr(
                median_cancellation_ratio,
                50,
            ),
            "fraction_Cint_below_0_25": mp.nstr(
                strong_cancellation_fraction,
                50,
            ),
            "fraction_Cint_below_0_10": mp.nstr(
                very_strong_cancellation_fraction,
                50,
            ),
        }

        block_summaries[
            block_name
        ] = block_summary

        block_summary_rows.append(
            {
                "dataset_block": block_name,
                **block_summary,
            }
        )

    with BLOCK_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                block_summary_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            block_summary_rows
        )

    # -------------------------------------------------
    # M-004:
    # Frozen PCA line versus elementary i=0 edge
    # on the already-frozen higher-zero population.
    # -------------------------------------------------

    higher_vectors = [
        mp.matrix(
            [
                mp_value(row["a_share"]),
                mp_value(row["e_share"]),
                mp_value(row["i_share"]),
            ]
        )
        for row in higher_rows
    ]

    def frozen_pca_projection(
        vector: mp.matrix,
    ) -> mp.matrix:
        centered = (
            vector - frozen_centroid
        )

        coordinate = dot(
            centered,
            frozen_axis,
        )

        return (
            frozen_centroid
            +
            coordinate * frozen_axis
        )

    frozen_pca_explained_fraction = (
        fixed_line_explained_fraction(
            higher_vectors,
            denominator_centroid=frozen_centroid,
            projection_function=frozen_pca_projection,
        )
    )

    elementary_edge_explained_fraction = (
        fixed_line_explained_fraction(
            higher_vectors,
            denominator_centroid=frozen_centroid,
            projection_function=edge_projection,
        )
    )

    explained_fraction_gap = (
        frozen_pca_explained_fraction
        -
        elementary_edge_explained_fraction
    )

    if abs(
        explained_fraction_gap
    ) < mp.mpf("0.01"):
        edge_interpretation = (
            "ELEMENTARY_I_ZERO_EDGE_CAPTURES_"
            "NEARLY_ALL_FROZEN_PCA_ENERGY_EXPLANATION"
        )
    elif (
        explained_fraction_gap
        >=
        mp.mpf("0.01")
    ):
        edge_interpretation = (
            "FROZEN_PCA_LINE_CONTAINS_MATERIALLY_"
            "MORE_FINITE_DATA_GEOMETRY"
        )
    else:
        edge_interpretation = (
            "ELEMENTARY_EDGE_OUTPERFORMS_FROZEN_"
            "PCA_UNDER_SHARED_DENOMINATOR_CONVENTION"
        )

    runtime_seconds = (
        time.perf_counter()
        -
        started
    )

    summary = {
        "experiment_name": (
            "li_zeta_window_principal_line_"
            "mechanism_audit"
        ),
        "analysis_status": (
            "POST_REPLICATION_MECHANISM_AUDIT"
        ),
        "first_500_point_count": len(
            primary_rows
        ),
        "higher_zero_point_count": len(
            higher_rows
        ),
        "block_scaling_and_cancellation_summaries": (
            block_summaries
        ),
        "frozen_axis_alignment_with_atom_endpoint_exchange_direction": mp.nstr(
            exchange_axis_alignment,
            50,
        ),
        "higher_zero_frozen_PCA_explained_fraction": mp.nstr(
            frozen_pca_explained_fraction,
            50,
        ),
        "higher_zero_elementary_i_zero_edge_explained_fraction": mp.nstr(
            elementary_edge_explained_fraction,
            50,
        ),
        "PCA_minus_i_zero_edge_explained_fraction_gap": mp.nstr(
            explained_fraction_gap,
            50,
        ),
        "M_004_edge_interpretation": (
            edge_interpretation
        ),
        "M_001_status": (
            "DESCRIPTIVE_HEIGHT_TREND_REPORTED"
        ),
        "M_002_status": (
            "DESCRIPTIVE_RAW_COMPONENT_SLOPES_REPORTED"
        ),
        "M_003_status": (
            "INTERIOR_SIGNED_CANCELLATION_DIAGNOSTIC_REPORTED"
        ),
        "M_004_status": (
            "FIXED_EDGE_COMPARATOR_SCORED"
        ),
        "M_005_status": (
            "ATOM_ENDPOINT_EXCHANGE_ALIGNMENT_REPORTED"
        ),
        "git_commit_at_start": git_output(
            "rev-parse",
            "HEAD",
        ),
        "python_version": sys.version,
        "platform": platform.platform(),
        "runtime_seconds": runtime_seconds,
        "interpretation_boundary": (
            "Post-replication mechanism audit. "
            "Small interior share was visible before "
            "this protocol. Height slopes are finite-data "
            "descriptive regressions and do not prove "
            "asymptotic power laws. Interior cancellation "
            "ratios do not establish independence or "
            "randomness. No off-critical-zero or RH "
            "consequence is claimed."
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
    print("=" * 116)
    print(
        "PHASE 5M — BLOCK MECHANISM SUMMARY"
    )
    print("=" * 116)

    for (
        block_name,
        block_summary,
    ) in block_summaries.items():
        print()
        print(
            f"[{block_name}]"
        )

        for key, value in (
            block_summary.items()
        ):
            print(
                f"{key}: {value}"
            )

    print()
    print("=" * 116)
    print(
        "PHASE 5M — GEOMETRIC MECHANISM SUMMARY"
    )
    print("=" * 116)

    print(
        "frozen_axis_alignment_with_"
        "atom_endpoint_exchange_direction: "
        f"{mp.nstr(exchange_axis_alignment, 50)}"
    )

    print(
        "higher_zero_frozen_PCA_explained_fraction: "
        f"{mp.nstr(frozen_pca_explained_fraction, 50)}"
    )

    print(
        "higher_zero_elementary_i_zero_edge_"
        "explained_fraction: "
        f"{mp.nstr(elementary_edge_explained_fraction, 50)}"
    )

    print(
        "PCA_minus_i_zero_edge_explained_fraction_gap: "
        f"{mp.nstr(explained_fraction_gap, 50)}"
    )

    print(
        "M_004_edge_interpretation: "
        f"{edge_interpretation}"
    )

    print()
    print(
        f"Point CSV: {POINT_CSV}"
    )

    print(
        f"Block CSV: {BLOCK_CSV}"
    )

    print(
        f"Summary JSON: {SUMMARY_JSON}"
    )

    print()
    print(
        "PHASE 5M PRINCIPAL-LINE MECHANISM AUDIT: "
        "COMPLETE"
    )


if __name__ == "__main__":
    main()
