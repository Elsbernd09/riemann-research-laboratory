from __future__ import annotations

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


INPUT_CSV = Path(
    "results/li_zeta_window_sign_chambers/"
    "sign_chamber_points.csv"
)

RESULT_DIR = Path(
    "results/li_zeta_window_component_share_simplex"
)

POINT_CSV = RESULT_DIR / "simplex_points.csv"
CHAMBER_CSV = RESULT_DIR / "opposing_share_summary.csv"
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


def quantile_linear(
    values: list[mp.mpf],
    probability: mp.mpf,
) -> mp.mpf:
    if not values:
        return mp.nan

    ordered = sorted(values)

    if len(ordered) == 1:
        return ordered[0]

    position = (
        probability
        *
        (len(ordered) - 1)
    )

    lower_index = int(
        mp.floor(position)
    )

    upper_index = int(
        mp.ceil(position)
    )

    if lower_index == upper_index:
        return ordered[lower_index]

    weight = (
        position - lower_index
    )

    return (
        ordered[lower_index]
        *
        (1 - weight)
        +
        ordered[upper_index]
        *
        weight
    )


def interquartile_range(
    values: list[mp.mpf],
) -> mp.mpf:
    return (
        quantile_linear(
            values,
            mp.mpf("0.75"),
        )
        -
        quantile_linear(
            values,
            mp.mpf("0.25"),
        )
    )


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


def solve_ols_r_squared(
    design_rows: list[list[mp.mpf]],
    targets: list[mp.mpf],
) -> mp.mpf:
    if len(design_rows) != len(targets):
        raise ValueError(
            "Design and target lengths differ."
        )

    if not design_rows:
        return mp.nan

    X = mp.matrix(
        design_rows
    )

    y = mp.matrix(
        targets
    )

    Xt = X.T

    gram = Xt * X
    rhs = Xt * y

    try:
        beta = mp.lu_solve(
            gram,
            rhs,
        )
    except ZeroDivisionError:
        beta = mp.qr_solve(
            X,
            y,
        )[0]

    fitted = X * beta

    y_mean = (
        mp.fsum(targets)
        /
        len(targets)
    )

    ss_total = mp.fsum(
        (
            target - y_mean
        ) ** 2
        for target in targets
    )

    ss_residual = mp.fsum(
        (
            targets[index]
            -
            fitted[index]
        ) ** 2
        for index in range(
            len(targets)
        )
    )

    if ss_total == 0:
        return mp.nan

    return (
        1
        -
        ss_residual / ss_total
    )


def opposing_component_index(
    chamber: str,
) -> int | None:
    if chamber == "(+,-,-)":
        return 0

    if chamber == "(-,+,+)":
        return 0

    if chamber == "(+,-,+)":
        return 1

    if chamber == "(-,+,-)":
        return 1

    if chamber == "(+,+,-)":
        return 2

    if chamber == "(-,-,+)":
        return 2

    return None


def main() -> None:
    started = time.perf_counter()

    mp.mp.dps = 60

    if not INPUT_CSV.exists():
        raise FileNotFoundError(
            f"Missing frozen Phase 5I input: "
            f"{INPUT_CSV}"
        )

    RESULT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    with INPUT_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        rows = list(
            csv.DictReader(handle)
        )

    if len(rows) != 360:
        raise RuntimeError(
            "Frozen Phase 5I population mismatch: "
            f"expected 360 rows, got {len(rows)}"
        )

    simplex_rows: list[
        dict[str, str | int]
    ] = []

    share_vectors: list[
        tuple[mp.mpf, mp.mpf, mp.mpf]
    ] = []

    closure_errors: list[
        mp.mpf
    ] = []

    dominant_shares: list[
        mp.mpf
    ] = []

    chamber_names = sorted(
        {
            str(row["sign_chamber"])
            for row in rows
        }
    )

    if "BOUNDARY" in chamber_names:
        raise RuntimeError(
            "Phase 5J received a BOUNDARY point "
            "despite frozen Phase 5I result."
        )

    for row in rows:
        atom = abs(
            mp_value(
                row["atom_component"]
            )
        )

        endpoint = abs(
            mp_value(
                row["endpoint_component"]
            )
        )

        interior = abs(
            mp_value(
                row["interior_component"]
            )
        )

        total = (
            atom
            +
            endpoint
            +
            interior
        )

        if total <= 0:
            raise ArithmeticError(
                "Nonpositive component magnitude sum."
            )

        a_share = atom / total
        e_share = endpoint / total
        i_share = interior / total

        closure_error = abs(
            a_share
            +
            e_share
            +
            i_share
            -
            1
        )

        dominant_share = max(
            a_share,
            e_share,
            i_share,
        )

        chamber = str(
            row["sign_chamber"]
        )

        signs = chamber.strip("()").split(",")

        weights = (
            a_share,
            e_share,
            i_share,
        )

        positive_mass = mp.fsum(
            weight
            for sign, weight in zip(
                signs,
                weights,
            )
            if sign == "+"
        )

        negative_mass = mp.fsum(
            weight
            for sign, weight in zip(
                signs,
                weights,
            )
            if sign == "-"
        )

        is_mixed = (
            positive_mass > 0
            and negative_mass > 0
        )

        if is_mixed:
            balance_distance = abs(
                positive_mass
                -
                mp.mpf("0.5")
            )
        else:
            balance_distance = mp.mpf(
                "0.5"
            )

        C_scalar = mp_value(
            row[
                "scalar_cancellation_coefficient"
            ]
        )

        opposing_index = (
            opposing_component_index(
                chamber
            )
        )

        if opposing_index is None:
            opposing_share = mp.nan
        else:
            opposing_share = weights[
                opposing_index
            ]

        simplex_rows.append(
            {
                **row,
                "a_share": mp.nstr(
                    a_share,
                    60,
                ),
                "e_share": mp.nstr(
                    e_share,
                    60,
                ),
                "i_share": mp.nstr(
                    i_share,
                    60,
                ),
                "simplex_closure_error": mp.nstr(
                    closure_error,
                    60,
                ),
                "dominant_share": mp.nstr(
                    dominant_share,
                    60,
                ),
                "positive_mass_share": mp.nstr(
                    positive_mass,
                    60,
                ),
                "negative_mass_share": mp.nstr(
                    negative_mass,
                    60,
                ),
                "balance_distance": mp.nstr(
                    balance_distance,
                    60,
                ),
                "opposing_share": mp.nstr(
                    opposing_share,
                    60,
                ),
            }
        )

        share_vectors.append(
            (
                a_share,
                e_share,
                i_share,
            )
        )

        closure_errors.append(
            closure_error
        )

        dominant_shares.append(
            dominant_share
        )

    # Covariance geometry.
    means = [
        mean_mpf(
            [
                vector[index]
                for vector in share_vectors
            ]
        )
        for index in range(3)
    ]

    covariance = mp.matrix(
        3,
        3,
    )

    for row_index in range(3):
        for column_index in range(3):
            covariance[
                row_index,
                column_index,
            ] = (
                mp.fsum(
                    (
                        vector[row_index]
                        -
                        means[row_index]
                    )
                    *
                    (
                        vector[column_index]
                        -
                        means[column_index]
                    )
                    for vector in share_vectors
                )
                /
                len(share_vectors)
            )

    eigenvalues_matrix, _ = mp.eigsy(
        covariance
    )

    eigenvalues = sorted(
        [
            mp.mpf(
                eigenvalues_matrix[index]
            )
            for index in range(3)
        ],
        reverse=True,
    )

    positive_eigenvalues = [
        value
        for value in eigenvalues
        if value > mp.mpf("1e-50")
    ]

    if len(positive_eigenvalues) != 2:
        raise RuntimeError(
            "Expected exactly two positive "
            "in-plane covariance eigenvalues; "
            f"observed {positive_eigenvalues}"
        )

    lambda_1 = positive_eigenvalues[0]
    lambda_2 = positive_eigenvalues[1]

    in_plane_fraction = (
        lambda_1
        /
        (
            lambda_1
            +
            lambda_2
        )
    )

    fraction_dominant_above_08 = (
        fraction_true(
            [
                value
                >
                mp.mpf("0.8")
                for value in dominant_shares
            ]
        )
    )

    extreme_rows = [
        row
        for row in simplex_rows
        if mp_value(
            row[
                "scalar_cancellation_coefficient"
            ]
        )
        <
        mp.mpf("0.25")
    ]

    extreme_balance_fraction = (
        fraction_true(
            [
                mp_value(
                    row[
                        "balance_distance"
                    ]
                )
                <
                mp.mpf("0.125")
                for row in extreme_rows
            ]
        )
    )

    # OLS model comparison.
    #
    # Use seven chamber indicators plus intercept
    # to avoid exact dummy-variable collinearity.
    reference_chamber = chamber_names[-1]

    target_rows = [
        row
        for row in simplex_rows
        if mp_value(
            row[
                "scalar_cancellation_coefficient"
            ]
        )
        >
        0
    ]

    targets = [
        mp.log(
            mp_value(
                row[
                    "scalar_cancellation_coefficient"
                ]
            )
        )
        for row in target_rows
    ]

    model_A_design: list[
        list[mp.mpf]
    ] = []

    model_B_design: list[
        list[mp.mpf]
    ] = []

    non_reference_chambers = [
        chamber
        for chamber in chamber_names
        if chamber != reference_chamber
    ]

    for row in target_rows:
        chamber = str(
            row["sign_chamber"]
        )

        chamber_features = [
            mp.mpf(
                int(
                    chamber
                    ==
                    candidate
                )
            )
            for candidate in (
                non_reference_chambers
            )
        ]

        base = [
            mp.mpf("1"),
            *chamber_features,
        ]

        model_A_design.append(
            base
        )

        model_B_design.append(
            [
                *base,
                mp_value(
                    row["a_share"]
                ),
                mp_value(
                    row["e_share"]
                ),
            ]
        )

    chamber_only_r_squared = (
        solve_ols_r_squared(
            model_A_design,
            targets,
        )
    )

    chamber_plus_shares_r_squared = (
        solve_ols_r_squared(
            model_B_design,
            targets,
        )
    )

    r_squared_improvement = (
        chamber_plus_shares_r_squared
        -
        chamber_only_r_squared
    )

    # Opposing-share concentration.
    opposing_share_by_chamber: dict[
        str,
        list[mp.mpf],
    ] = defaultdict(list)

    for row in simplex_rows:
        chamber = str(
            row["sign_chamber"]
        )

        opposing_share = mp_value(
            row["opposing_share"]
        )

        if mp.isfinite(
            opposing_share
        ):
            opposing_share_by_chamber[
                chamber
            ].append(
                opposing_share
            )

    opposing_summary_rows: list[
        dict[str, str | int]
    ] = []

    eligible_opposing_iqrs: dict[
        str,
        mp.mpf,
    ] = {}

    for chamber in sorted(
        opposing_share_by_chamber
    ):
        values = (
            opposing_share_by_chamber[
                chamber
            ]
        )

        iqr = interquartile_range(
            values
        )

        eligible = (
            len(values) >= 50
        )

        if eligible:
            eligible_opposing_iqrs[
                chamber
            ] = iqr

        opposing_summary_rows.append(
            {
                "sign_chamber": chamber,
                "point_count": len(values),
                "eligible_point_count_ge_50": int(
                    eligible
                ),
                "median_opposing_share": mp.nstr(
                    median_mpf(
                        values
                    ),
                    60,
                ),
                "q1_opposing_share": mp.nstr(
                    quantile_linear(
                        values,
                        mp.mpf("0.25"),
                    ),
                    60,
                ),
                "q3_opposing_share": mp.nstr(
                    quantile_linear(
                        values,
                        mp.mpf("0.75"),
                    ),
                    60,
                ),
                "opposing_share_iqr": mp.nstr(
                    iqr,
                    60,
                ),
            }
        )

    eligible_iqr_below_025_count = sum(
        value
        <
        mp.mpf("0.25")
        for value in (
            eligible_opposing_iqrs.values()
        )
    )

    # Adjacent c-grid simplex steps.
    rows_by_window: dict[
        int,
        list[dict[str, str | int]],
    ] = defaultdict(list)

    for row in simplex_rows:
        rows_by_window[
            int(row["window_number"])
        ].append(row)

    transition_step_distances: list[
        mp.mpf
    ] = []

    same_chamber_step_distances: list[
        mp.mpf
    ] = []

    for window_number, window_rows in sorted(
        rows_by_window.items()
    ):
        ordered = sorted(
            window_rows,
            key=lambda row: int(
                mp.mpf(
                    str(row["requested_c"])
                )
            ),
        )

        if len(ordered) != 20:
            raise RuntimeError(
                f"Window {window_number} has "
                f"{len(ordered)} rows."
            )

        for left, right in zip(
            ordered,
            ordered[1:],
        ):
            delta_a = (
                mp_value(
                    right["a_share"]
                )
                -
                mp_value(
                    left["a_share"]
                )
            )

            delta_e = (
                mp_value(
                    right["e_share"]
                )
                -
                mp_value(
                    left["e_share"]
                )
            )

            delta_i = (
                mp_value(
                    right["i_share"]
                )
                -
                mp_value(
                    left["i_share"]
                )
            )

            distance = mp.sqrt(
                delta_a**2
                +
                delta_e**2
                +
                delta_i**2
            )

            if (
                str(
                    left["sign_chamber"]
                )
                !=
                str(
                    right["sign_chamber"]
                )
            ):
                transition_step_distances.append(
                    distance
                )
            else:
                same_chamber_step_distances.append(
                    distance
                )

    median_transition_distance = (
        median_mpf(
            transition_step_distances
        )
    )

    median_same_chamber_distance = (
        median_mpf(
            same_chamber_step_distances
        )
    )

    if median_same_chamber_distance == 0:
        transition_to_same_ratio = (
            mp.inf
        )
    else:
        transition_to_same_ratio = (
            median_transition_distance
            /
            median_same_chamber_distance
        )

    p_sim_001 = (
        max(closure_errors)
        <
        mp.mpf("1e-45")
    )

    p_sim_002 = (
        fraction_dominant_above_08
        <
        mp.mpf("0.90")
    )

    p_sim_003 = (
        in_plane_fraction
        >
        mp.mpf("0.90")
    )

    p_sim_004 = (
        extreme_balance_fraction
        >=
        mp.mpf("0.90")
    )

    p_sim_005 = (
        r_squared_improvement
        >
        mp.mpf("0.20")
    )

    p_sim_006 = (
        eligible_iqr_below_025_count
        >=
        3
    )

    p_sim_007 = (
        bool(
            transition_step_distances
        )
        and bool(
            same_chamber_step_distances
        )
        and transition_to_same_ratio
        <
        mp.mpf("2.5")
    )

    with POINT_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                simplex_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            simplex_rows
        )

    with CHAMBER_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                opposing_summary_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            opposing_summary_rows
        )

    runtime_seconds = (
        time.perf_counter()
        -
        started
    )

    summary = {
        "experiment_name": (
            "li_zeta_window_component_share_simplex"
        ),
        "point_count": len(
            simplex_rows
        ),
        "maximum_simplex_closure_error": mp.nstr(
            max(closure_errors),
            50,
        ),
        "median_dominant_share": mp.nstr(
            median_mpf(
                dominant_shares
            ),
            50,
        ),
        "fraction_dominant_share_above_0_8": mp.nstr(
            fraction_dominant_above_08,
            50,
        ),
        "covariance_eigenvalues_descending": [
            mp.nstr(
                value,
                50,
            )
            for value in eigenvalues
        ],
        "leading_in_plane_explained_fraction": mp.nstr(
            in_plane_fraction,
            50,
        ),
        "extreme_cancellation_point_count": len(
            extreme_rows
        ),
        "extreme_cancellation_balance_neighborhood_fraction": mp.nstr(
            extreme_balance_fraction,
            50,
        ),
        "ols_reference_chamber": (
            reference_chamber
        ),
        "chamber_only_R_squared": mp.nstr(
            chamber_only_r_squared,
            50,
        ),
        "chamber_plus_shares_R_squared": mp.nstr(
            chamber_plus_shares_r_squared,
            50,
        ),
        "R_squared_improvement": mp.nstr(
            r_squared_improvement,
            50,
        ),
        "eligible_opposing_share_IQRs": {
            chamber: mp.nstr(
                value,
                50,
            )
            for chamber, value in sorted(
                eligible_opposing_iqrs.items()
            )
        },
        "eligible_chamber_count": len(
            eligible_opposing_iqrs
        ),
        "eligible_IQR_below_0_25_count": (
            eligible_iqr_below_025_count
        ),
        "transition_step_count": len(
            transition_step_distances
        ),
        "same_chamber_step_count": len(
            same_chamber_step_distances
        ),
        "median_transition_simplex_distance": mp.nstr(
            median_transition_distance,
            50,
        ),
        "median_same_chamber_simplex_distance": mp.nstr(
            median_same_chamber_distance,
            50,
        ),
        "transition_to_same_median_distance_ratio": mp.nstr(
            transition_to_same_ratio,
            50,
        ),
        "P_SIM_001": (
            "PASS"
            if p_sim_001
            else "FAIL"
        ),
        "P_SIM_002": (
            "PASS"
            if p_sim_002
            else "FAIL"
        ),
        "P_SIM_003": (
            "PASS"
            if p_sim_003
            else "FAIL"
        ),
        "P_SIM_004": (
            "PASS"
            if p_sim_004
            else "FAIL"
        ),
        "P_SIM_005": (
            "PASS"
            if p_sim_005
            else "FAIL"
        ),
        "P_SIM_006": (
            "PASS"
            if p_sim_006
            else "FAIL"
        ),
        "P_SIM_007": (
            "PASS"
            if p_sim_007
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
            "In-sample descriptive simplex geometry "
            "on the frozen 360-point signed-transfer "
            "population. Simplex closure, the null "
            "covariance direction, and mixed-sign "
            "balance identities are structural or "
            "algebraic. OLS and PCA results are "
            "descriptive only. No predictive, "
            "asymptotic, or RH consequence."
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
    print("=" * 108)
    print(
        "PHASE 5J — COMPONENT-SHARE SIMPLEX SUMMARY"
    )
    print("=" * 108)

    for key, value in summary.items():
        print(
            f"{key}: {value}"
        )

    print()
    print(
        f"Point CSV: {POINT_CSV}"
    )

    print(
        f"Opposing-share CSV: {CHAMBER_CSV}"
    )

    print(
        f"Summary JSON: {SUMMARY_JSON}"
    )

    print()
    print(
        "PHASE 5J COMPONENT-SHARE SIMPLEX: COMPLETE"
    )


if __name__ == "__main__":
    main()
