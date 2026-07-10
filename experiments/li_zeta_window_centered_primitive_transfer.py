from __future__ import annotations

import bisect
import csv
import json
import math
import platform
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

import mpmath as mp
import numpy as np

import experiments.li_zeta_window_discrepancy_decomposition as dec
from src.li_susceptibility import (
    li_susceptibility_exact,
    li_susceptibility_gamma_derivative,
)


MECHANISM_CSV = Path(
    "results/"
    "li_zeta_window_principal_line_mechanism_audit/"
    "mechanism_points.csv"
)

PRIMARY_POINT_CSV = Path(
    "results/li_zeta_window_signed_transfer/"
    "signed_transfer_points.csv"
)

HIGHER_POINT_CSV = Path(
    "results/"
    "li_zeta_window_higher_zero_external_replication/"
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

RESULT_DIR = Path(
    "results/"
    "li_zeta_window_centered_primitive_transfer"
)

POINT_CSV = RESULT_DIR / "primitive_transfer_points.csv"
BLOCK_CSV = RESULT_DIR / "block_metrics.csv"
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


def mp_value(
    value: object,
) -> mp.mpf:
    return mp.mpf(str(value))


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


def pearson(
    xs: list[mp.mpf],
    ys: list[mp.mpf],
) -> mp.mpf:
    pairs = [
        (x, y)
        for x, y in zip(xs, ys)
        if (
            mp.isfinite(x)
            and mp.isfinite(y)
        )
    ]

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

    x_mean = mean_mpf(
        x_values
    )

    y_mean = mean_mpf(
        y_values
    )

    x_centered = [
        value - x_mean
        for value in x_values
    ]

    y_centered = [
        value - y_mean
        for value in y_values
    ]

    numerator = mp.fsum(
        x_value * y_value
        for x_value, y_value in zip(
            x_centered,
            y_centered,
        )
    )

    x_energy = mp.fsum(
        value**2
        for value in x_centered
    )

    y_energy = mp.fsum(
        value**2
        for value in y_centered
    )

    denominator = mp.sqrt(
        x_energy * y_energy
    )

    if denominator == 0:
        return mp.nan

    return numerator / denominator


def smooth_counting_antiderivative(
    t: mp.mpf,
) -> mp.mpf:
    t_mp = mp.mpf(t)

    return (
        (
            t_mp**2
            /
            (
                4 * mp.pi
            )
        )
        *
        mp.log(
            t_mp
            /
            (
                2 * mp.pi
            )
        )
        -
        (
            3
            *
            t_mp**2
            /
            (
                8 * mp.pi
            )
        )
        +
        (
            7
            *
            t_mp
            /
            8
        )
    )


def empirical_count(
    *,
    block_name: str,
    gammas: list[mp.mpf],
    t: mp.mpf,
) -> int:
    prefix = (
        0
        if block_name == "first_500"
        else 500
    )

    return (
        prefix
        +
        bisect.bisect_right(
            gammas,
            t,
        )
    )


def interval_E_integral(
    *,
    count: int,
    left: mp.mpf,
    right: mp.mpf,
) -> mp.mpf:
    return (
        mp.mpf(count)
        *
        (
            right - left
        )
        -
        (
            smooth_counting_antiderivative(
                right
            )
            -
            smooth_counting_antiderivative(
                left
            )
        )
    )


def centered_primitive_value_inside_interval(
    *,
    F_left: mp.mpf,
    count: int,
    E_bar: mp.mpf,
    left: mp.mpf,
    t: mp.mpf,
) -> mp.mpf:
    return (
        F_left
        +
        (
            mp.mpf(count)
            -
            E_bar
        )
        *
        (
            t - left
        )
        -
        (
            smooth_counting_antiderivative(
                t
            )
            -
            smooth_counting_antiderivative(
                left
            )
        )
    )


def bisect_mp_root(
    function,
    left: mp.mpf,
    right: mp.mpf,
    *,
    iterations: int = 200,
) -> mp.mpf:
    a = mp.mpf(left)
    b = mp.mpf(right)

    f_a = function(a)
    f_b = function(b)

    if f_a == 0:
        return a

    if f_b == 0:
        return b

    if mp.sign(f_a) == mp.sign(f_b):
        raise ValueError(
            "Root bracket does not change sign."
        )

    for _ in range(iterations):
        midpoint = (
            a + b
        ) / 2

        if midpoint == a or midpoint == b:
            return midpoint

        f_midpoint = function(
            midpoint
        )

        if f_midpoint == 0:
            return midpoint

        if (
            mp.sign(f_a)
            !=
            mp.sign(f_midpoint)
        ):
            b = midpoint
        else:
            a = midpoint
            f_a = f_midpoint

    return (
        a + b
    ) / 2


def centered_primitive_statistics(
    *,
    block_name: str,
    gammas: list[mp.mpf],
    H: mp.mpf,
    B: mp.mpf,
) -> tuple[
    mp.mpf,
    mp.mpf,
    mp.mpf,
    mp.mpf,
]:
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

    interval_records = []

    total_E_integral = mp.mpf("0")

    for left, right in zip(
        breakpoints,
        breakpoints[1:],
    ):
        midpoint = (
            left + right
        ) / 2

        count = empirical_count(
            block_name=block_name,
            gammas=gammas,
            t=midpoint,
        )

        E_integral = interval_E_integral(
            count=count,
            left=left,
            right=right,
        )

        total_E_integral += E_integral

        interval_records.append(
            (
                left,
                right,
                count,
                E_integral,
            )
        )

    E_bar = (
        total_E_integral
        /
        (
            B - H
        )
    )

    F_left = mp.mpf("0")

    F_sup = mp.mpf("0")

    centered_E_sup = mp.mpf("0")

    for (
        left,
        right,
        count,
        E_integral,
    ) in interval_records:
        E_left = (
            mp.mpf(count)
            -
            dec.smooth_counting_model(
                left
            )
        )

        E_right = (
            mp.mpf(count)
            -
            dec.smooth_counting_model(
                right
            )
        )

        centered_E_sup = max(
            centered_E_sup,
            abs(
                E_left - E_bar
            ),
            abs(
                E_right - E_bar
            ),
        )

        F_right = (
            F_left
            +
            E_integral
            -
            E_bar
            *
            (
                right - left
            )
        )

        F_sup = max(
            F_sup,
            abs(F_left),
            abs(F_right),
        )

        def centered_E(
            t: mp.mpf,
        ) -> mp.mpf:
            return (
                mp.mpf(count)
                -
                dec.smooth_counting_model(
                    t
                )
                -
                E_bar
            )

        left_value = centered_E(
            left
        )

        right_value = centered_E(
            right
        )

        if (
            left_value != 0
            and right_value != 0
            and mp.sign(left_value)
            !=
            mp.sign(right_value)
        ):
            critical_point = bisect_mp_root(
                centered_E,
                left,
                right,
            )

            F_critical = (
                centered_primitive_value_inside_interval(
                    F_left=F_left,
                    count=count,
                    E_bar=E_bar,
                    left=left,
                    t=critical_point,
                )
            )

            F_sup = max(
                F_sup,
                abs(F_critical),
            )

        F_left = F_right

    endpoint_closure = abs(
        F_left
    )

    if endpoint_closure > mp.mpf(
        "1e-45"
    ):
        raise ArithmeticError(
            "Centered primitive endpoint closure "
            "failure: "
            f"{mp.nstr(endpoint_closure, 30)}"
        )

    denominator = (
        (
            B - H
        )
        *
        centered_E_sup
    )

    if denominator <= 0:
        primitive_compression = mp.nan
    else:
        primitive_compression = (
            F_sup
            /
            denominator
        )

    return (
        E_bar,
        F_sup,
        centered_E_sup,
        primitive_compression,
    )


def chi_second_derivative_float(
    n: int,
    gamma: np.ndarray,
) -> np.ndarray:
    gamma_array = np.asarray(
        gamma,
        dtype=np.float64,
    )

    n_float = float(n)

    D = (
        gamma_array**2
        +
        0.25
    )

    theta = (
        2.0
        *
        np.arctan(
            1.0
            /
            (
                2.0
                *
                gamma_array
            )
        )
    )

    phase = (
        n_float
        *
        theta
    )

    sin_phase = np.sin(
        phase
    )

    cos_phase = np.cos(
        phase
    )

    A = (
        n_float
        *
        cos_phase
        +
        2.0
        *
        gamma_array
        *
        sin_phase
    )

    A_prime = (
        (
            n_float**2
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

    A_second = -(
        (
            4.0
            *
            n_float**2
            *
            gamma_array
            *
            sin_phase
        )
        +
        (
            n_float
            *
            (
                n_float**2
                +
                1.0
            )
            *
            cos_phase
        )
    ) / (
        D**2
    )

    return (
        (
            8.0
            *
            n_float
            *
            A
            /
            (
                D**3
            )
        )
        +
        (
            16.0
            *
            n_float
            *
            gamma_array
            *
            A_prime
            /
            (
                D**3
            )
        )
        -
        (
            48.0
            *
            n_float
            *
            gamma_array**2
            *
            A
            /
            (
                D**4
            )
        )
        -
        (
            2.0
            *
            n_float
            *
            A_second
            /
            (
                D**2
            )
        )
    )


def bisect_float_root(
    function,
    left: float,
    right: float,
    *,
    iterations: int = 100,
) -> float:
    a = float(left)
    b = float(right)

    f_a = float(
        function(a)
    )

    f_b = float(
        function(b)
    )

    if f_a == 0.0:
        return a

    if f_b == 0.0:
        return b

    if (
        np.signbit(f_a)
        ==
        np.signbit(f_b)
    ):
        raise ValueError(
            "Float bracket does not change sign."
        )

    for _ in range(iterations):
        midpoint = (
            a + b
        ) / 2.0

        if midpoint == a or midpoint == b:
            return midpoint

        f_midpoint = float(
            function(midpoint)
        )

        if f_midpoint == 0.0:
            return midpoint

        if (
            np.signbit(f_a)
            !=
            np.signbit(f_midpoint)
        ):
            b = midpoint
        else:
            a = midpoint
            f_a = f_midpoint

    return (
        a + b
    ) / 2.0


def derivative_variation(
    *,
    n: int,
    H: mp.mpf,
    B: mp.mpf,
    scan_count: int,
) -> tuple[
    mp.mpf,
    int,
]:
    samples = np.linspace(
        float(H),
        float(B),
        scan_count,
        dtype=np.float64,
    )

    values = (
        chi_second_derivative_float(
            n,
            samples,
        )
    )

    roots: list[float] = []

    def scalar_second(
        value: float,
    ) -> float:
        return float(
            chi_second_derivative_float(
                n,
                np.asarray(
                    [value],
                    dtype=np.float64,
                ),
            )[0]
        )

    for index in range(
        len(samples) - 1
    ):
        left = float(
            samples[index]
        )

        right = float(
            samples[index + 1]
        )

        y_left = float(
            values[index]
        )

        y_right = float(
            values[index + 1]
        )

        if (
            not np.isfinite(y_left)
            or not np.isfinite(y_right)
        ):
            raise ArithmeticError(
                "Nonfinite second-derivative scan."
            )

        if y_left == 0.0:
            roots.append(
                left
            )

        if (
            y_left != 0.0
            and y_right != 0.0
            and np.signbit(y_left)
            !=
            np.signbit(y_right)
        ):
            roots.append(
                bisect_float_root(
                    scalar_second,
                    left,
                    right,
                )
            )

    roots = sorted(
        set(roots)
    )

    split_points = [
        mp.mpf(H),
        *[
            mp.mpf(
                repr(root)
            )
            for root in roots
            if (
                float(H)
                <
                root
                <
                float(B)
            )
        ],
        mp.mpf(B),
    ]

    variation = mp.fsum(
        abs(
            li_susceptibility_gamma_derivative(
                n,
                right,
            )
            -
            li_susceptibility_gamma_derivative(
                n,
                left,
            )
        )
        for left, right in zip(
            split_points,
            split_points[1:],
        )
    )

    return (
        variation,
        len(roots),
    )


def validated_derivative_variation(
    *,
    n: int,
    H: mp.mpf,
    B: mp.mpf,
) -> tuple[
    mp.mpf,
    mp.mpf,
]:
    coarse_value, coarse_roots = (
        derivative_variation(
            n=n,
            H=H,
            B=B,
            scan_count=257,
        )
    )

    fine_value, fine_roots = (
        derivative_variation(
            n=n,
            H=H,
            B=B,
            scan_count=513,
        )
    )

    if coarse_roots != fine_roots:
        raise ArithmeticError(
            "Second-derivative root-count "
            "validation failure: "
            f"coarse={coarse_roots}, "
            f"fine={fine_roots}, "
            f"H={mp.nstr(H, 20)}, "
            f"n={n}"
        )

    relative_discrepancy = abs(
        fine_value - coarse_value
    ) / max(
        abs(fine_value),
        mp.mpf("1e-300"),
    )

    if (
        relative_discrepancy
        >
        mp.mpf("1e-8")
    ):
        raise ArithmeticError(
            "Derivative variation validation "
            "failure: "
            f"{mp.nstr(relative_discrepancy, 30)}"
        )

    return (
        fine_value,
        relative_discrepancy,
    )


def main() -> None:
    started = time.perf_counter()

    mp.mp.dps = 60

    for path in (
        MECHANISM_CSV,
        PRIMARY_POINT_CSV,
        HIGHER_POINT_CSV,
        PRIMARY_ZERO_CSV,
        HIGHER_ZERO_CSV,
    ):
        if not path.exists():
            raise FileNotFoundError(
                f"Missing Phase 5N input: {path}"
            )

    RESULT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    with MECHANISM_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        mechanism_rows = list(
            csv.DictReader(handle)
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

    if len(mechanism_rows) != 780:
        raise RuntimeError(
            "Expected 780 Phase 5M mechanism rows."
        )

    if len(primary_rows) != 360:
        raise RuntimeError(
            "Expected 360 primary rows."
        )

    if len(higher_rows) != 420:
        raise RuntimeError(
            "Expected 420 higher-zero rows."
        )

    source_rows_by_block = {
        "first_500": primary_rows,
        "indices_501_1500": higher_rows,
    }

    gammas_by_block = {
        "first_500": primary_gammas,
        "indices_501_1500": higher_gammas,
    }

    point_rows = []

    maximum_hybrid_closure_error = mp.mpf(
        "0"
    )

    certificate_pass_count = 0

    print(
        "PHASE 5N — CENTERED-PRIMITIVE "
        "CANCELLATION TRANSFER"
    )
    print("=" * 116)

    mechanism_rows_by_block = defaultdict(
        list
    )

    for row in mechanism_rows:
        mechanism_rows_by_block[
            row["dataset_block"]
        ].append(row)

    for block_name in (
        "first_500",
        "indices_501_1500",
    ):
        block_mechanism_rows = (
            mechanism_rows_by_block[
                block_name
            ]
        )

        source_rows = (
            source_rows_by_block[
                block_name
            ]
        )

        gammas = gammas_by_block[
            block_name
        ]

        if (
            len(block_mechanism_rows)
            !=
            len(source_rows)
        ):
            raise RuntimeError(
                f"Block row mismatch for {block_name}."
            )

        print()
        print(
            f"BLOCK: {block_name}"
        )
        print("-" * 116)

        for index, (
            mechanism_row,
            source_row,
        ) in enumerate(
            zip(
                block_mechanism_rows,
                source_rows,
            ),
            start=1,
        ):
            H = mp_value(
                mechanism_row["H"]
            )

            B = mp_value(
                mechanism_row["B"]
            )

            n = int(
                mechanism_row["n"]
            )

            C1 = mp_value(
                mechanism_row[
                    "interior_absolute_integral"
                ]
            )

            R_int = mp_value(
                source_row[
                    "interior_component"
                ]
            )

            (
                E_bar,
                F_sup,
                centered_E_sup,
                primitive_compression,
            ) = centered_primitive_statistics(
                block_name=block_name,
                gammas=gammas,
                H=H,
                B=B,
            )

            f_H = li_susceptibility_exact(
                n,
                H,
            )

            f_B = li_susceptibility_exact(
                n,
                B,
            )

            R_mean = -(
                E_bar
                *
                (
                    f_B - f_H
                )
            )

            # Exact identity already proved in Phase 5N.
            #
            # R_prim is reconstructed from the proved
            # decomposition. Closure is therefore a
            # bookkeeping validation, not an independent
            # numerical proof of integration by parts.
            R_prim = (
                R_int - R_mean
            )

            reconstructed = (
                R_mean + R_prim
            )

            closure_error = abs(
                R_int - reconstructed
            )

            hybrid_scale = max(
                mp.mpf("1"),
                abs(R_int),
                abs(R_mean),
                abs(R_prim),
            )

            hybrid_closure_error = (
                closure_error
                /
                hybrid_scale
            )

            maximum_hybrid_closure_error = max(
                maximum_hybrid_closure_error,
                hybrid_closure_error,
            )

            (
                f_prime_variation,
                variation_discrepancy,
            ) = validated_derivative_variation(
                n=n,
                H=H,
                B=B,
            )

            mean_certificate_term = (
                abs(E_bar)
                *
                abs(
                    f_B - f_H
                )
            )

            primitive_certificate_term = (
                F_sup
                *
                f_prime_variation
            )

            C2 = (
                mean_certificate_term
                +
                primitive_certificate_term
            )

            if C2 <= 0:
                raise ArithmeticError(
                    "Nonpositive Phase 5N certificate."
                )

            certificate_tolerance = mp.mpf(
                "1e-40"
            )

            certificate_pass = (
                abs(R_int)
                <=
                C2
                +
                certificate_tolerance
            )

            certificate_pass_count += int(
                certificate_pass
            )

            Q21 = C2 / C1

            T2 = abs(R_int) / C2

            mean_share = (
                mean_certificate_term
                /
                C2
            )

            point_rows.append(
                {
                    "dataset_block": block_name,
                    "point_number_within_block": index,
                    "window_number": source_row[
                        "window_number"
                    ],
                    "H": mp.nstr(
                        H,
                        60,
                    ),
                    "B": mp.nstr(
                        B,
                        60,
                    ),
                    "eta": source_row["eta"],
                    "requested_c": source_row[
                        "requested_c"
                    ],
                    "n": n,
                    "R_int": mp.nstr(
                        R_int,
                        60,
                    ),
                    "E_bar": mp.nstr(
                        E_bar,
                        60,
                    ),
                    "F_sup": mp.nstr(
                        F_sup,
                        60,
                    ),
                    "centered_E_sup": mp.nstr(
                        centered_E_sup,
                        60,
                    ),
                    "primitive_compression_G": mp.nstr(
                        primitive_compression,
                        60,
                    ),
                    "f_H": mp.nstr(
                        f_H,
                        60,
                    ),
                    "f_B": mp.nstr(
                        f_B,
                        60,
                    ),
                    "R_mean": mp.nstr(
                        R_mean,
                        60,
                    ),
                    "R_prim": mp.nstr(
                        R_prim,
                        60,
                    ),
                    "hybrid_closure_error": mp.nstr(
                        hybrid_closure_error,
                        60,
                    ),
                    "f_prime_variation": mp.nstr(
                        f_prime_variation,
                        60,
                    ),
                    "variation_scan_relative_discrepancy": mp.nstr(
                        variation_discrepancy,
                        60,
                    ),
                    "C1_absolute_integral_scale": mp.nstr(
                        C1,
                        60,
                    ),
                    "mean_certificate_term": mp.nstr(
                        mean_certificate_term,
                        60,
                    ),
                    "primitive_certificate_term": mp.nstr(
                        primitive_certificate_term,
                        60,
                    ),
                    "C2_second_order_certificate": mp.nstr(
                        C2,
                        60,
                    ),
                    "Q21_C2_over_C1": mp.nstr(
                        Q21,
                        60,
                    ),
                    "T2_certificate_tightness": mp.nstr(
                        T2,
                        60,
                    ),
                    "mean_certificate_share": mp.nstr(
                        mean_share,
                        60,
                    ),
                    "certificate_pass": int(
                        certificate_pass
                    ),
                }
            )

            if (
                index == 1
                or index % 20 == 0
                or index == len(source_rows)
            ):
                print(
                    f"  point={index:4d}/"
                    f"{len(source_rows):4d} "
                    f"Q21={mp.nstr(Q21, 8):>11s} "
                    f"T2={mp.nstr(T2, 8):>11s} "
                    f"G={mp.nstr(primitive_compression, 8):>11s}",
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
                point_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            point_rows
        )

    rows_by_block = defaultdict(
        list
    )

    for row in point_rows:
        rows_by_block[
            row["dataset_block"]
        ].append(row)

    block_summaries = {}

    block_summary_rows = []

    for block_name in (
        "first_500",
        "indices_501_1500",
    ):
        rows = rows_by_block[
            block_name
        ]

        R_int_abs = [
            abs(
                mp_value(row["R_int"])
            )
            for row in rows
        ]

        C2_values = [
            mp_value(
                row[
                    "C2_second_order_certificate"
                ]
            )
            for row in rows
        ]

        H_values = [
            mp_value(row["H"])
            for row in rows
        ]

        Q21_values = [
            mp_value(
                row["Q21_C2_over_C1"]
            )
            for row in rows
        ]

        T2_values = [
            mp_value(
                row["T2_certificate_tightness"]
            )
            for row in rows
        ]

        mean_shares = [
            mp_value(
                row["mean_certificate_share"]
            )
            for row in rows
        ]

        G_values = [
            mp_value(
                row["primitive_compression_G"]
            )
            for row in rows
            if mp.isfinite(
                mp_value(
                    row[
                        "primitive_compression_G"
                    ]
                )
            )
        ]

        log_Y = [
            mp.log(value)
            for value in R_int_abs
            if value > 0
        ]

        log_C2 = [
            mp.log(C2_values[index])
            for index, value in enumerate(
                R_int_abs
            )
            if value > 0
        ]

        log_H_minus_2 = [
            mp.log(
                H_values[index] ** (-2)
            )
            for index, value in enumerate(
                R_int_abs
            )
            if value > 0
        ]

        corr_C2 = pearson(
            log_Y,
            log_C2,
        )

        corr_H = pearson(
            log_Y,
            log_H_minus_2,
        )

        block_summary = {
            "point_count": len(rows),
            "median_Q21_C2_over_C1": mp.nstr(
                median_mpf(
                    Q21_values
                ),
                50,
            ),
            "mean_Q21_C2_over_C1": mp.nstr(
                mean_mpf(
                    Q21_values
                ),
                50,
            ),
            "median_T2_certificate_tightness": mp.nstr(
                median_mpf(
                    T2_values
                ),
                50,
            ),
            "median_mean_certificate_share": mp.nstr(
                median_mpf(
                    mean_shares
                ),
                50,
            ),
            "median_primitive_compression_G": mp.nstr(
                median_mpf(
                    G_values
                ),
                50,
            ),
            "correlation_log_abs_Rint_log_C2": mp.nstr(
                corr_C2,
                50,
            ),
            "correlation_log_abs_Rint_log_H_minus_2": mp.nstr(
                corr_H,
                50,
            ),
            "correlation_advantage_C2_over_height": mp.nstr(
                corr_C2 - corr_H,
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

    first_summary = block_summaries[
        "first_500"
    ]

    higher_summary = block_summaries[
        "indices_501_1500"
    ]

    p_prm_001 = (
        maximum_hybrid_closure_error
        <
        mp.mpf("1e-40")
    )

    p_prm_002 = (
        certificate_pass_count
        ==
        len(point_rows)
    )

    p_prm_003 = (
        mp_value(
            first_summary[
                "median_Q21_C2_over_C1"
            ]
        )
        <
        mp.mpf("0.25")
        and
        mp_value(
            higher_summary[
                "median_Q21_C2_over_C1"
            ]
        )
        <
        mp.mpf("0.25")
    )

    p_prm_004 = (
        mp_value(
            first_summary[
                "correlation_log_abs_Rint_log_C2"
            ]
        )
        >
        mp_value(
            first_summary[
                "correlation_log_abs_Rint_log_H_minus_2"
            ]
        )
        and
        mp_value(
            higher_summary[
                "correlation_log_abs_Rint_log_C2"
            ]
        )
        >
        mp_value(
            higher_summary[
                "correlation_log_abs_Rint_log_H_minus_2"
            ]
        )
    )

    p_prm_005 = (
        mp_value(
            first_summary[
                "median_T2_certificate_tightness"
            ]
        )
        >
        mp.mpf("0.05")
        or
        mp_value(
            higher_summary[
                "median_T2_certificate_tightness"
            ]
        )
        >
        mp.mpf("0.05")
    )

    p_prm_006 = (
        mp_value(
            first_summary[
                "median_mean_certificate_share"
            ]
        )
        <
        mp.mpf("0.90")
        and
        mp_value(
            higher_summary[
                "median_mean_certificate_share"
            ]
        )
        <
        mp.mpf("0.90")
    )

    p_prm_007 = (
        mp_value(
            first_summary[
                "median_primitive_compression_G"
            ]
        )
        <
        mp.mpf("0.25")
        and
        mp_value(
            higher_summary[
                "median_primitive_compression_G"
            ]
        )
        <
        mp.mpf("0.25")
    )

    runtime_seconds = (
        time.perf_counter()
        -
        started
    )

    summary = {
        "experiment_name": (
            "li_zeta_window_centered_primitive_transfer"
        ),
        "point_count": len(
            point_rows
        ),
        "maximum_hybrid_closure_error": mp.nstr(
            maximum_hybrid_closure_error,
            50,
        ),
        "certificate_pass_count": (
            certificate_pass_count
        ),
        "certificate_pass_rate": mp.nstr(
            mp.mpf(certificate_pass_count)
            /
            len(point_rows),
            50,
        ),
        "block_summaries": (
            block_summaries
        ),
        "P_PRM_001": (
            "PASS"
            if p_prm_001
            else "FAIL"
        ),
        "P_PRM_002": (
            "PASS"
            if p_prm_002
            else "FAIL"
        ),
        "P_PRM_003": (
            "PASS"
            if p_prm_003
            else "FAIL"
        ),
        "P_PRM_004": (
            "PASS"
            if p_prm_004
            else "FAIL"
        ),
        "P_PRM_005": (
            "PASS"
            if p_prm_005
            else "FAIL"
        ),
        "P_PRM_006": (
            "PASS"
            if p_prm_006
            else "FAIL"
        ),
        "P_PRM_007": (
            "PASS"
            if p_prm_007
            else "FAIL"
        ),
        "git_commit_at_start": git_output(
            "rev-parse",
            "HEAD",
        ),
        "python_version": sys.version,
        "platform": platform.platform(),
        "runtime_seconds": runtime_seconds,
        "interpretation_boundary": (
            "Finite-data centered-primitive transfer "
            "audit. The decomposition identity and "
            "certificate are elementary deterministic "
            "integration-by-parts consequences. "
            "P-PRM-001 is bookkeeping closure because "
            "R_prim is reconstructed from the proved "
            "identity. Correlation results are in-sample "
            "descriptive. No asymptotic primitive bound, "
            "off-critical-zero constraint, or RH "
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
        "PHASE 5N — BLOCK PRIMITIVE TRANSFER SUMMARY"
    )
    print("=" * 116)

    for block_name, block_summary in (
        block_summaries.items()
    ):
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
        "PHASE 5N FINAL SCORECARD"
    )
    print("=" * 116)

    print(
        "maximum_hybrid_closure_error: "
        f"{mp.nstr(maximum_hybrid_closure_error, 50)}"
    )

    print(
        "certificate_pass_count: "
        f"{certificate_pass_count}/"
        f"{len(point_rows)}"
    )

    for prediction in (
        "P_PRM_001",
        "P_PRM_002",
        "P_PRM_003",
        "P_PRM_004",
        "P_PRM_005",
        "P_PRM_006",
        "P_PRM_007",
    ):
        print(
            f"{prediction}: "
            f"{summary[prediction]}"
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
        "PHASE 5N CENTERED-PRIMITIVE TRANSFER: COMPLETE"
    )


if __name__ == "__main__":
    main()
