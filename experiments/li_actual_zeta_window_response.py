"""Compare discrete actual-zero Li response windows with smooth-density profiles."""

from __future__ import annotations

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
    li_blind_scale,
    li_susceptibility_exact,
    li_window_continuum_profile,
    li_window_finite_height_profile,
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
    "results/li_actual_zeta_window_response"
)

CURVE_CSV = RESULT_DIR / "window_curves.csv"
METRIC_CSV = RESULT_DIR / "window_metrics.csv"
ROOT_CSV = RESULT_DIR / "window_root_comparison.csv"
SUMMARY_JSON = RESULT_DIR / "summary.json"


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


def pearson_correlation(
    x_values: list[mp.mpf],
    y_values: list[mp.mpf],
) -> mp.mpf:
    if len(x_values) != len(y_values):
        raise ValueError("Input lengths must match")

    if len(x_values) < 2:
        raise ValueError("At least two values required")

    x_mean = mp.fsum(x_values) / len(x_values)
    y_mean = mp.fsum(y_values) / len(y_values)

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

    denominator = x_scale * y_scale

    if denominator == 0:
        return mp.nan

    return numerator / denominator


def nrmse(
    observed: list[mp.mpf],
    predicted: list[mp.mpf],
) -> mp.mpf:
    mse = (
        mp.fsum(
            (y - p) ** 2
            for y, p in zip(
                observed,
                predicted,
            )
        )
        /
        len(observed)
    )

    predicted_rms = mp.sqrt(
        mp.fsum(
            p**2
            for p in predicted
        )
        /
        len(predicted)
    )

    if predicted_rms == 0:
        return mp.inf

    return (
        mp.sqrt(mse)
        /
        predicted_rms
    )


def sign_agreement(
    observed: list[mp.mpf],
    predicted: list[mp.mpf],
) -> mp.mpf:
    agreements = 0
    count = 0

    for observed_value, predicted_value in zip(
        observed,
        predicted,
    ):
        if (
            observed_value == 0
            or predicted_value == 0
        ):
            continue

        count += 1

        if (
            mp.sign(observed_value)
            ==
            mp.sign(predicted_value)
        ):
            agreements += 1

    if count == 0:
        return mp.nan

    return (
        mp.mpf(agreements)
        /
        count
    )


def interpolated_roots(
    c_values: list[mp.mpf],
    y_values: list[mp.mpf],
) -> list[mp.mpf]:
    roots: list[mp.mpf] = []

    for index in range(
        len(c_values) - 1
    ):
        c_left = c_values[index]
        c_right = c_values[index + 1]

        y_left = y_values[index]
        y_right = y_values[index + 1]

        if y_left == 0:
            roots.append(c_left)
            continue

        if y_left * y_right > 0:
            continue

        denominator = (
            y_right - y_left
        )

        if denominator == 0:
            continue

        root = (
            c_left
            -
            y_left
            * (
                c_right - c_left
            )
            /
            denominator
        )

        roots.append(root)

    return roots


def nearest_distance(
    value: mp.mpf,
    candidates: list[mp.mpf],
) -> mp.mpf:
    if not candidates:
        return mp.inf

    return min(
        abs(value - candidate)
        for candidate in candidates
    )


def occupancy_band(
    occupancy: int,
) -> str:
    if occupancy < 10:
        return "sparse"

    if occupancy < 25:
        return "moderate"

    if occupancy < 50:
        return "dense"

    return "high_occupancy"


def main() -> None:
    started = time.perf_counter()

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

    complete_windows = [
        row
        for row in occupancy_rows
        if int(
            row[
                "truncated_by_dataset_end"
            ]
        )
        == 0
    ]

    c_requested_values = [
        mp.mpf(index) / 4
        for index in range(
            1,
            81,
        )
    ]

    curve_rows: list[
        dict[str, str | int]
    ] = []

    metric_rows: list[
        dict[str, str | int]
    ] = []

    root_rows: list[
        dict[str, str | int]
    ] = []

    blind_scales = [
        li_blind_scale(k)
        for k in range(10)
    ]

    print("ACTUAL ZETA-ZERO WINDOW RESPONSE")
    print("=" * 110)

    print(
        f"Complete windows: "
        f"{len(complete_windows)}"
    )

    print(
        f"Requested c-grid points: "
        f"{len(c_requested_values)}"
    )

    for window_number, row in enumerate(
        complete_windows,
        start=1,
    ):
        eta = mp.mpf(row["eta"])

        anchor_zero_index = int(
            row["anchor_zero_index"]
        )

        # Recover the atomic left endpoint from the authoritative
        # frozen zero dataset rather than the rounded occupancy-file
        # display serialization.
        H = gammas[
            anchor_zero_index - 1
        ]

        upper = (
            (1 + eta) * H
        )

        window_gammas = [
            gamma
            for gamma in gammas
            if H <= gamma <= upper
        ]

        occupancy = len(window_gammas)

        discrete_values: list[
            mp.mpf
        ] = []

        frozen_values: list[
            mp.mpf
        ] = []

        finite_height_values: list[
            mp.mpf
        ] = []

        realized_c_values: list[
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

            susceptibility_sum = mp.fsum(
                li_susceptibility_exact(
                    n,
                    gamma,
                )
                for gamma in window_gammas
            )

            normalized_discrete = (
                H
                /
                mp.log(H)
                *
                susceptibility_sum
            )

            frozen = (
                li_window_continuum_profile(
                    c_realized,
                    eta,
                )
            )

            finite_height = (
                li_window_finite_height_profile(
                    c_realized,
                    eta,
                    H,
                )
            )

            realized_c_values.append(
                c_realized
            )

            discrete_values.append(
                normalized_discrete
            )

            frozen_values.append(
                frozen
            )

            finite_height_values.append(
                finite_height
            )

            curve_rows.append(
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
                    "occupancy_band": occupancy_band(
                        occupancy
                    ),
                    "requested_c": mp.nstr(
                        c_requested,
                        30,
                    ),
                    "n": n,
                    "realized_c": mp.nstr(
                        c_realized,
                        60,
                    ),
                    "normalized_discrete_response": mp.nstr(
                        normalized_discrete,
                        70,
                    ),
                    "frozen_profile": mp.nstr(
                        frozen,
                        70,
                    ),
                    "finite_height_profile": mp.nstr(
                        finite_height,
                        70,
                    ),
                }
            )

        frozen_nrmse = nrmse(
            discrete_values,
            frozen_values,
        )

        finite_height_nrmse = nrmse(
            discrete_values,
            finite_height_values,
        )

        frozen_correlation = (
            pearson_correlation(
                discrete_values,
                frozen_values,
            )
        )

        finite_height_correlation = (
            pearson_correlation(
                discrete_values,
                finite_height_values,
            )
        )

        frozen_sign_agreement = sign_agreement(
            discrete_values,
            frozen_values,
        )

        finite_height_sign_agreement = sign_agreement(
            discrete_values,
            finite_height_values,
        )

        discrete_roots = interpolated_roots(
            realized_c_values,
            discrete_values,
        )

        frozen_roots = interpolated_roots(
            realized_c_values,
            frozen_values,
        )

        finite_height_roots = interpolated_roots(
            realized_c_values,
            finite_height_values,
        )

        metric_rows.append(
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
                "occupancy_band": occupancy_band(
                    occupancy
                ),
                "frozen_nrmse": mp.nstr(
                    frozen_nrmse,
                    60,
                ),
                "finite_height_nrmse": mp.nstr(
                    finite_height_nrmse,
                    60,
                ),
                "frozen_correlation": mp.nstr(
                    frozen_correlation,
                    60,
                ),
                "finite_height_correlation": mp.nstr(
                    finite_height_correlation,
                    60,
                ),
                "frozen_sign_agreement": mp.nstr(
                    frozen_sign_agreement,
                    60,
                ),
                "finite_height_sign_agreement": mp.nstr(
                    finite_height_sign_agreement,
                    60,
                ),
                "discrete_root_count": len(
                    discrete_roots
                ),
                "frozen_root_count": len(
                    frozen_roots
                ),
                "finite_height_root_count": len(
                    finite_height_roots
                ),
            }
        )

        for root_number, empirical_root in enumerate(
            discrete_roots,
            start=1,
        ):
            window_distance = nearest_distance(
                empirical_root,
                frozen_roots,
            )

            individual_distance = nearest_distance(
                empirical_root,
                blind_scales,
            )

            finite_height_distance = nearest_distance(
                empirical_root,
                finite_height_roots,
            )

            root_rows.append(
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
                    "occupancy_band": occupancy_band(
                        occupancy
                    ),
                    "empirical_root_number": root_number,
                    "empirical_root": mp.nstr(
                        empirical_root,
                        60,
                    ),
                    "nearest_frozen_window_root_distance": mp.nstr(
                        window_distance,
                        60,
                    ),
                    "nearest_finite_height_root_distance": mp.nstr(
                        finite_height_distance,
                        60,
                    ),
                    "nearest_individual_blind_scale_distance": mp.nstr(
                        individual_distance,
                        60,
                    ),
                    "frozen_window_closer_than_individual": int(
                        window_distance
                        <
                        individual_distance
                    ),
                    "finite_height_closer_than_individual": int(
                        finite_height_distance
                        <
                        individual_distance
                    ),
                }
            )

        print(
            f"window={window_number:<2d} "
            f"eta={mp.nstr(eta, 5):>5s} "
            f"H={mp.nstr(H, 10):>12s} "
            f"N={occupancy:<3d} "
            f"band={occupancy_band(occupancy):>14s} "
            f"NRMSE A={mp.nstr(frozen_nrmse, 6):>10s} "
            f"NRMSE B={mp.nstr(finite_height_nrmse, 6):>10s} "
            f"corr A={mp.nstr(frozen_correlation, 6):>9s} "
            f"corr B={mp.nstr(finite_height_correlation, 6):>9s}"
        )

    with CURVE_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                curve_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(curve_rows)

    with METRIC_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                metric_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(metric_rows)

    with ROOT_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                root_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(root_rows)

    def summarize_band(
        minimum_occupancy: int,
    ) -> dict[str, object]:
        selected_metrics = [
            row
            for row in metric_rows
            if int(row["occupancy"])
            >= minimum_occupancy
        ]

        selected_roots = [
            row
            for row in root_rows
            if int(row["occupancy"])
            >= minimum_occupancy
        ]

        if not selected_metrics:
            return {
                "minimum_occupancy": minimum_occupancy,
                "window_count": 0,
            }

        def mean_metric(
            key: str,
        ) -> mp.mpf:
            return (
                mp.fsum(
                    mp.mpf(
                        str(row[key])
                    )
                    for row in selected_metrics
                )
                /
                len(selected_metrics)
            )

        frozen_root_win_rate = (
            mp.fsum(
                int(
                    row[
                        "frozen_window_closer_than_individual"
                    ]
                )
                for row in selected_roots
            )
            /
            len(selected_roots)
            if selected_roots
            else mp.nan
        )

        finite_height_root_win_rate = (
            mp.fsum(
                int(
                    row[
                        "finite_height_closer_than_individual"
                    ]
                )
                for row in selected_roots
            )
            /
            len(selected_roots)
            if selected_roots
            else mp.nan
        )

        return {
            "minimum_occupancy": minimum_occupancy,
            "window_count": len(
                selected_metrics
            ),
            "empirical_root_count": len(
                selected_roots
            ),
            "mean_frozen_nrmse": mp.nstr(
                mean_metric(
                    "frozen_nrmse"
                ),
                50,
            ),
            "mean_finite_height_nrmse": mp.nstr(
                mean_metric(
                    "finite_height_nrmse"
                ),
                50,
            ),
            "mean_frozen_correlation": mp.nstr(
                mean_metric(
                    "frozen_correlation"
                ),
                50,
            ),
            "mean_finite_height_correlation": mp.nstr(
                mean_metric(
                    "finite_height_correlation"
                ),
                50,
            ),
            "mean_frozen_sign_agreement": mp.nstr(
                mean_metric(
                    "frozen_sign_agreement"
                ),
                50,
            ),
            "mean_finite_height_sign_agreement": mp.nstr(
                mean_metric(
                    "finite_height_sign_agreement"
                ),
                50,
            ),
            "frozen_window_root_win_rate_vs_individual": mp.nstr(
                frozen_root_win_rate,
                50,
            ),
            "finite_height_root_win_rate_vs_individual": mp.nstr(
                finite_height_root_win_rate,
                50,
            ),
        }

    summaries = {
        "occupancy_at_least_10": summarize_band(
            10
        ),
        "occupancy_at_least_25": summarize_band(
            25
        ),
        "occupancy_at_least_50": summarize_band(
            50
        ),
    }

    runtime_seconds = (
        time.perf_counter()
        - started
    )

    summary = {
        "experiment_name": (
            "li_actual_zeta_window_response"
        ),
        "zero_dataset": str(
            ZERO_CSV
        ),
        "zero_dataset_sha256": sha256_file(
            ZERO_CSV
        ),
        "complete_window_count": len(
            complete_windows
        ),
        "requested_c_grid_start": "0.25",
        "requested_c_grid_end": "20",
        "requested_c_grid_step": "0.25",
        "requested_c_grid_count": len(
            c_requested_values
        ),
        "precision_decimal_digits": (
            mp.mp.dps
        ),
        "summaries": summaries,
        "runtime_seconds": (
            runtime_seconds
        ),
        "git_commit_at_start": git_output(
            "rev-parse",
            "HEAD",
        ),
        "git_clean_at_end_before_outputs_added": (
            git_output(
                "status",
                "--porcelain",
            )
            == ""
        ),
        "python_version": sys.version,
        "platform": platform.platform(),
        "interpretation_boundary": (
            "Finite numerical response experiment on the "
            "first 500 critical-line zero ordinates in the "
            "project dataset. Agreement or disagreement does "
            "not prove or disprove RH."
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
    print("OCCUPANCY-STRATIFIED SUMMARY")
    print("=" * 110)

    for name, band_summary in summaries.items():
        print()
        print(name)

        for key, value in band_summary.items():
            print(
                f"  {key}: {value}"
            )

    print()
    print("ACTUAL-ZERO WINDOW RESPONSE EXPERIMENT: COMPLETE")

    print(
        f"Runtime seconds: "
        f"{runtime_seconds:.3f}"
    )

    print(
        f"Curve CSV: {CURVE_CSV}"
    )

    print(
        f"Metric CSV: {METRIC_CSV}"
    )

    print(
        f"Root CSV: {ROOT_CSV}"
    )

    print(
        f"Summary: {SUMMARY_JSON}"
    )


if __name__ == "__main__":
    main()
