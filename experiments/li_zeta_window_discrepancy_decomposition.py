"""Independently evaluate counting and kernel remainders in zeta-zero windows."""

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
from pathlib import Path

import mpmath as mp

from src.li_susceptibility import (
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

RESULT_DIR = Path(
    "results/li_zeta_window_discrepancy_decomposition"
)

COMPONENT_CSV = (
    RESULT_DIR
    / "decomposition_components.csv"
)

WINDOW_CSV = (
    RESULT_DIR
    / "window_component_metrics.csv"
)

SUMMARY_JSON = (
    RESULT_DIR
    / "summary.json"
)


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


def rms(
    values: list[mp.mpf],
) -> mp.mpf:
    return mp.sqrt(
        mp.fsum(
            value**2
            for value in values
        )
        /
        len(values)
    )


def log_log_slope(
    heights: list[mp.mpf],
    magnitudes: list[mp.mpf],
) -> mp.mpf:
    filtered = [
        (height, magnitude)
        for height, magnitude in zip(
            heights,
            magnitudes,
        )
        if magnitude > 0
    ]

    if len(filtered) < 3:
        return mp.nan

    x_values = [
        mp.log(height)
        for height, _ in filtered
    ]

    y_values = [
        mp.log(magnitude)
        for _, magnitude in filtered
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

    denominator = mp.fsum(
        (x - x_mean) ** 2
        for x in x_values
    )

    if denominator == 0:
        return mp.nan

    return numerator / denominator


def main() -> None:
    started = time.perf_counter()

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

    c_requested_values = [
        mp.mpf(index)
        for index in range(
            1,
            21,
        )
    ]

    component_rows: list[
        dict[str, str | int]
    ] = []

    window_rows: list[
        dict[str, str | int]
    ] = []

    maximum_closure_error = mp.mpf("0")
    maximum_stieltjes_error = mp.mpf("0")

    print("ZETA-WINDOW DISCREPANCY DECOMPOSITION")
    print("=" * 110)

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

        H = mp.mpf(
            row["H"]
        )

        B = (
            (1 + eta) * H
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

        quadrature_breakpoints = [
            H,
            *internal_breakpoints,
            B,
        ]

        occupancy = len(
            window_gammas
        )

        normalized_count_components: list[
            mp.mpf
        ] = []

        normalized_kernel_components: list[
            mp.mpf
        ] = []

        normalized_full_residuals: list[
            mp.mpf
        ] = []

        normalized_atom_components: list[
            mp.mpf
        ] = []

        normalized_open_residuals: list[
            mp.mpf
        ] = []

        normalized_closed_residuals: list[
            mp.mpf
        ] = []

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

            def profile_kernel(
                t: mp.mpf,
            ) -> mp.mpf:
                return (
                    t**(-2)
                    * li_susceptibility_profile(
                        mp.mpf(n) / t
                    )
                )

            discrete_response = mp.fsum(
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

            profile_smooth = mp.quad(
                lambda t: (
                    profile_kernel(t)
                    * smooth_density(t)
                ),
                [
                    H,
                    B,
                ],
            )

            count_direct = (
                discrete_response
                -
                exact_smooth
            )

            E_H = empirical_remainder(
                gammas,
                H,
            )

            E_B = empirical_remainder(
                gammas,
                B,
            )

            left_atom_jump = mp.mpf("1")

            atom = (
                f(H)
                * left_atom_jump
            )

            weighted_derivative_integral = (
                mp.quad(
                    lambda t: (
                        empirical_remainder(
                            gammas,
                            t,
                        )
                        * f_prime(t)
                    ),
                    quadrature_breakpoints,
                )
            )

            count_stieltjes = (
                atom
                +
                f(B) * E_B
                -
                f(H) * E_H
                -
                weighted_derivative_integral
            )

            kernel_remainder = (
                exact_smooth
                -
                profile_smooth
            )

            full_profile_residual = (
                discrete_response
                -
                profile_smooth
            )

            decomposition_sum = (
                count_stieltjes
                +
                kernel_remainder
            )

            closure_error = abs(
                full_profile_residual
                -
                decomposition_sum
            )

            stieltjes_error = abs(
                count_direct
                -
                count_stieltjes
            )

            maximum_closure_error = max(
                maximum_closure_error,
                closure_error,
            )

            maximum_stieltjes_error = max(
                maximum_stieltjes_error,
                stieltjes_error,
            )

            normalization = (
                H / mp.log(H)
            )

            normalized_count = (
                normalization
                * count_stieltjes
            )

            normalized_kernel = (
                normalization
                * kernel_remainder
            )

            normalized_full = (
                normalization
                * full_profile_residual
            )

            normalized_atom = (
                normalization
                * atom
            )

            open_discrete_response = (
                discrete_response
                -
                atom
            )

            open_profile_residual = (
                open_discrete_response
                -
                profile_smooth
            )

            normalized_open_residual = (
                normalization
                * open_profile_residual
            )

            normalized_closed_residual = (
                normalized_full
            )

            normalized_count_components.append(
                normalized_count
            )

            normalized_kernel_components.append(
                normalized_kernel
            )

            normalized_full_residuals.append(
                normalized_full
            )

            normalized_atom_components.append(
                normalized_atom
            )

            normalized_open_residuals.append(
                normalized_open_residual
            )

            normalized_closed_residuals.append(
                normalized_closed_residual
            )

            component_rows.append(
                {
                    "window_number": window_number,
                    "eta": mp.nstr(
                        eta,
                        30,
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
                    "discrete_response": mp.nstr(
                        discrete_response,
                        60,
                    ),
                    "exact_smooth_response": mp.nstr(
                        exact_smooth,
                        60,
                    ),
                    "profile_smooth_response": mp.nstr(
                        profile_smooth,
                        60,
                    ),
                    "count_remainder_direct": mp.nstr(
                        count_direct,
                        60,
                    ),
                    "count_remainder_stieltjes": mp.nstr(
                        count_stieltjes,
                        60,
                    ),
                    "kernel_remainder": mp.nstr(
                        kernel_remainder,
                        60,
                    ),
                    "left_atom": mp.nstr(
                        atom,
                        60,
                    ),
                    "normalized_count_remainder": mp.nstr(
                        normalized_count,
                        60,
                    ),
                    "normalized_kernel_remainder": mp.nstr(
                        normalized_kernel,
                        60,
                    ),
                    "normalized_full_profile_residual": mp.nstr(
                        normalized_full,
                        60,
                    ),
                    "normalized_left_atom": mp.nstr(
                        normalized_atom,
                        60,
                    ),
                    "normalized_open_profile_residual": mp.nstr(
                        normalized_open_residual,
                        60,
                    ),
                    "closure_error": mp.nstr(
                        closure_error,
                        60,
                    ),
                    "stieltjes_direct_error": mp.nstr(
                        stieltjes_error,
                        60,
                    ),
                }
            )

        count_rms = rms(
            normalized_count_components
        )

        kernel_rms = rms(
            normalized_kernel_components
        )

        full_rms = rms(
            normalized_full_residuals
        )

        atom_rms = rms(
            normalized_atom_components
        )

        closed_residual_rms = rms(
            normalized_closed_residuals
        )

        open_residual_rms = rms(
            normalized_open_residuals
        )

        atom_removal_ratio = (
            open_residual_rms
            /
            closed_residual_rms
            if closed_residual_rms != 0
            else mp.nan
        )

        window_rows.append(
            {
                "window_number": window_number,
                "eta": mp.nstr(
                    eta,
                    30,
                ),
                "H": mp.nstr(
                    H,
                    60,
                ),
                "occupancy": occupancy,
                "normalized_count_rms": mp.nstr(
                    count_rms,
                    60,
                ),
                "normalized_kernel_rms": mp.nstr(
                    kernel_rms,
                    60,
                ),
                "count_to_kernel_rms_ratio": mp.nstr(
                    count_rms / kernel_rms,
                    60,
                ),
                "normalized_full_residual_rms": mp.nstr(
                    full_rms,
                    60,
                ),
                "normalized_atom_rms": mp.nstr(
                    atom_rms,
                    60,
                ),
                "closed_profile_residual_rms": mp.nstr(
                    closed_residual_rms,
                    60,
                ),
                "open_profile_residual_rms": mp.nstr(
                    open_residual_rms,
                    60,
                ),
                "open_to_closed_residual_rms_ratio": mp.nstr(
                    atom_removal_ratio,
                    60,
                ),
            }
        )

        print(
            f"window={window_number:<2d} "
            f"eta={mp.nstr(eta, 5):>5s} "
            f"H={mp.nstr(H, 10):>12s} "
            f"N={occupancy:<3d} "
            f"countRMS={mp.nstr(count_rms, 8):>13s} "
            f"kernelRMS={mp.nstr(kernel_rms, 8):>13s} "
            f"ratio={mp.nstr(count_rms/kernel_rms, 7):>10s} "
            f"atom-open/closed={mp.nstr(atom_removal_ratio, 7):>10s}"
        )

    with COMPONENT_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                component_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            component_rows
        )

    with WINDOW_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                window_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            window_rows
        )

    high_occupancy_rows = [
        row
        for row in window_rows
        if int(row["occupancy"]) >= 50
    ]

    def mean_window_metric(
        rows: list[dict[str, str | int]],
        key: str,
    ) -> mp.mpf:
        return (
            mp.fsum(
                mp.mpf(
                    str(row[key])
                )
                for row in rows
            )
            /
            len(rows)
        )

    dense_count_dominance_rate = (
        mp.fsum(
            mp.mpf(
                str(
                    row[
                        "normalized_count_rms"
                    ]
                )
            )
            >
            mp.mpf(
                str(
                    row[
                        "normalized_kernel_rms"
                    ]
                )
            )
            for row in window_rows
        )
        /
        len(window_rows)
    )

    high_count_dominance_rate = (
        mp.fsum(
            mp.mpf(
                str(
                    row[
                        "normalized_count_rms"
                    ]
                )
            )
            >
            mp.mpf(
                str(
                    row[
                        "normalized_kernel_rms"
                    ]
                )
            )
            for row in high_occupancy_rows
        )
        /
        len(high_occupancy_rows)
    )

    # Estimate height slopes using per-window RMS magnitudes.
    heights = [
        mp.mpf(
            str(row["H"])
        )
        for row in window_rows
    ]

    count_magnitudes = [
        mp.mpf(
            str(
                row[
                    "normalized_count_rms"
                ]
            )
        )
        for row in window_rows
    ]

    kernel_magnitudes = [
        mp.mpf(
            str(
                row[
                    "normalized_kernel_rms"
                ]
            )
        )
        for row in window_rows
    ]

    count_slope = log_log_slope(
        heights,
        count_magnitudes,
    )

    kernel_slope = log_log_slope(
        heights,
        kernel_magnitudes,
    )

    mean_high_count_rms = (
        mean_window_metric(
            high_occupancy_rows,
            "normalized_count_rms",
        )
    )

    mean_high_kernel_rms = (
        mean_window_metric(
            high_occupancy_rows,
            "normalized_kernel_rms",
        )
    )

    mean_high_atom_ratio = (
        mean_window_metric(
            high_occupancy_rows,
            "open_to_closed_residual_rms_ratio",
        )
    )

    mean_high_atom_rms = (
        mean_window_metric(
            high_occupancy_rows,
            "normalized_atom_rms",
        )
    )

    runtime_seconds = (
        time.perf_counter()
        - started
    )

    summary = {
        "experiment_name": (
            "li_zeta_window_discrepancy_decomposition"
        ),
        "dense_complete_window_count": len(
            window_rows
        ),
        "high_occupancy_window_count": len(
            high_occupancy_rows
        ),
        "coordinates_per_window": len(
            c_requested_values
        ),
        "decomposition_point_count": len(
            component_rows
        ),
        "precision_decimal_digits": mp.mp.dps,
        "maximum_closure_error": mp.nstr(
            maximum_closure_error,
            50,
        ),
        "maximum_stieltjes_direct_error": mp.nstr(
            maximum_stieltjes_error,
            50,
        ),
        "dense_count_dominance_rate": mp.nstr(
            dense_count_dominance_rate,
            50,
        ),
        "high_occupancy_count_dominance_rate": mp.nstr(
            high_count_dominance_rate,
            50,
        ),
        "mean_high_occupancy_normalized_count_rms": mp.nstr(
            mean_high_count_rms,
            50,
        ),
        "mean_high_occupancy_normalized_kernel_rms": mp.nstr(
            mean_high_kernel_rms,
            50,
        ),
        "mean_high_occupancy_count_to_kernel_ratio": mp.nstr(
            mean_high_count_rms
            /
            mean_high_kernel_rms,
            50,
        ),
        "fitted_dense_window_count_height_slope": mp.nstr(
            count_slope,
            50,
        ),
        "fitted_dense_window_kernel_height_slope": mp.nstr(
            kernel_slope,
            50,
        ),
        "mean_high_occupancy_open_to_closed_residual_rms_ratio": mp.nstr(
            mean_high_atom_ratio,
            50,
        ),
        "mean_high_occupancy_normalized_atom_rms": mp.nstr(
            mean_high_atom_rms,
            50,
        ),
        "zero_dataset_sha256": sha256_file(
            ZERO_CSV
        ),
        "git_commit_at_start": git_output(
            "rev-parse",
            "HEAD",
        ),
        "python_version": sys.version,
        "platform": platform.platform(),
        "runtime_seconds": runtime_seconds,
        "interpretation_boundary": (
            "Exact empirical Stieltjes decomposition on the "
            "frozen first-500-zero dataset. Height slopes are "
            "finite-range descriptive fits, not asymptotic theorems."
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
    print("DISCREPANCY DECOMPOSITION SUMMARY")
    print("=" * 110)

    for key, value in summary.items():
        print(
            f"{key}: {value}"
        )

    print()
    print(
        "ZETA-WINDOW DISCREPANCY DECOMPOSITION: COMPLETE"
    )

    print(
        f"Component CSV: {COMPONENT_CSV}"
    )

    print(
        f"Window CSV: {WINDOW_CSV}"
    )

    print(
        f"Summary: {SUMMARY_JSON}"
    )


if __name__ == "__main__":
    main()
