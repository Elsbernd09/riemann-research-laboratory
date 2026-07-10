from __future__ import annotations

import csv
import json
import platform
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp


INPUT_CSV = Path(
    "results/li_zeta_window_component_share_simplex/"
    "simplex_points.csv"
)

RESULT_DIR = Path(
    "results/li_zeta_window_principal_axis_holdout"
)

POINT_CSV = RESULT_DIR / "heldout_point_residuals.csv"
PRIMARY_CSV = RESULT_DIR / "primary_fold_metrics.csv"
LOO_CSV = RESULT_DIR / "leave_one_window_out_metrics.csv"
SUMMARY_JSON = RESULT_DIR / "summary.json"

PRIMARY_FOLDS = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (10, 11, 12),
    (13, 14, 15),
    (16, 17, 18),
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


def vector_from_row(
    row: dict[str, str],
) -> mp.matrix:
    return mp.matrix(
        [
            mp_value(row["a_share"]),
            mp_value(row["e_share"]),
            mp_value(row["i_share"]),
        ]
    )


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


def fit_principal_axis(
    vectors: list[mp.matrix],
) -> tuple[
    mp.matrix,
    mp.matrix,
    list[mp.mpf],
    mp.mpf,
]:
    if len(vectors) < 3:
        raise ValueError(
            "At least three vectors are required."
        )

    centroid = mp.matrix(
        [
            mean_mpf(
                [
                    vector[index]
                    for vector in vectors
                ]
            )
            for index in range(3)
        ]
    )

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
                        centroid[row_index]
                    )
                    *
                    (
                        vector[column_index]
                        -
                        centroid[column_index]
                    )
                    for vector in vectors
                )
                /
                len(vectors)
            )

    eigenvalues_matrix, eigenvectors = (
        mp.eigsy(
            covariance
        )
    )

    indexed_eigenpairs = sorted(
        [
            (
                mp.mpf(
                    eigenvalues_matrix[index]
                ),
                mp.matrix(
                    [
                        eigenvectors[row, index]
                        for row in range(3)
                    ]
                ),
            )
            for index in range(3)
        ],
        key=lambda pair: pair[0],
        reverse=True,
    )

    eigenvalues = [
        pair[0]
        for pair in indexed_eigenpairs
    ]

    leading_axis = unit_vector(
        indexed_eigenpairs[0][1]
    )

    positive_in_plane = [
        value
        for value in eigenvalues
        if value > mp.mpf("1e-50")
    ]

    if len(positive_in_plane) != 2:
        raise RuntimeError(
            "Expected exactly two positive "
            "in-plane covariance eigenvalues; "
            f"observed {positive_in_plane}"
        )

    leading_fraction = (
        positive_in_plane[0]
        /
        (
            positive_in_plane[0]
            +
            positive_in_plane[1]
        )
    )

    return (
        centroid,
        leading_axis,
        eigenvalues,
        leading_fraction,
    )


def evaluate_axis(
    vectors: list[mp.matrix],
    centroid: mp.matrix,
    axis: mp.matrix,
) -> tuple[
    mp.mpf,
    list[dict[str, mp.mpf]],
]:
    total_residual_energy = mp.mpf("0")
    total_centered_energy = mp.mpf("0")

    point_metrics: list[
        dict[str, mp.mpf]
    ] = []

    for vector in vectors:
        centered = (
            vector - centroid
        )

        coordinate = dot(
            centered,
            axis,
        )

        projection = (
            centroid
            +
            coordinate * axis
        )

        residual = (
            vector - projection
        )

        residual_squared = squared_norm(
            residual
        )

        centered_squared = squared_norm(
            centered
        )

        total_residual_energy += (
            residual_squared
        )

        total_centered_energy += (
            centered_squared
        )

        if centered_squared == 0:
            normalized_residual = mp.nan
        else:
            normalized_residual = (
                mp.sqrt(
                    residual_squared
                )
                /
                mp.sqrt(
                    centered_squared
                )
            )

        point_metrics.append(
            {
                "principal_coordinate": (
                    coordinate
                ),
                "residual_squared": (
                    residual_squared
                ),
                "centered_squared": (
                    centered_squared
                ),
                "normalized_residual": (
                    normalized_residual
                ),
            }
        )

    if total_centered_energy == 0:
        explained_fraction = mp.nan
    else:
        explained_fraction = (
            1
            -
            total_residual_energy
            /
            total_centered_energy
        )

    return (
        explained_fraction,
        point_metrics,
    )


def main() -> None:
    started = time.perf_counter()

    mp.mp.dps = 60

    if not INPUT_CSV.exists():
        raise FileNotFoundError(
            f"Missing frozen Phase 5J input: "
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
            "Frozen Phase 5J population mismatch: "
            f"expected 360 rows, got {len(rows)}"
        )

    windows = sorted(
        {
            int(row["window_number"])
            for row in rows
        }
    )

    if windows != list(
        range(
            1,
            19,
        )
    ):
        raise RuntimeError(
            "Expected window numbers 1 through 18; "
            f"observed {windows}"
        )

    full_vectors = [
        vector_from_row(row)
        for row in rows
    ]

    (
        full_centroid,
        full_axis,
        full_eigenvalues,
        full_leading_fraction,
    ) = fit_principal_axis(
        full_vectors
    )

    primary_fold_rows: list[
        dict[str, str | int]
    ] = []

    heldout_point_rows: list[
        dict[str, str | int]
    ] = []

    primary_training_fractions: list[
        mp.mpf
    ] = []

    primary_holdout_fractions: list[
        mp.mpf
    ] = []

    primary_axis_alignments: list[
        mp.mpf
    ] = []

    primary_vertex_fractions: list[
        mp.mpf
    ] = []

    global_primary_normalized_residuals: list[
        mp.mpf
    ] = []

    print(
        "PHASE 5K — PRINCIPAL-AXIS "
        "WINDOW HOLDOUT"
    )
    print("=" * 112)

    print(
        "Full-sample leading in-plane fraction: "
        f"{mp.nstr(full_leading_fraction, 16)}"
    )

    for fold_number, heldout_windows in enumerate(
        PRIMARY_FOLDS,
        start=1,
    ):
        heldout_window_set = set(
            heldout_windows
        )

        training_rows = [
            row
            for row in rows
            if int(
                row["window_number"]
            )
            not in heldout_window_set
        ]

        test_rows = [
            row
            for row in rows
            if int(
                row["window_number"]
            )
            in heldout_window_set
        ]

        if len(training_rows) != 300:
            raise RuntimeError(
                f"Fold {fold_number} expected "
                f"300 training points, got "
                f"{len(training_rows)}"
            )

        if len(test_rows) != 60:
            raise RuntimeError(
                f"Fold {fold_number} expected "
                f"60 test points, got "
                f"{len(test_rows)}"
            )

        training_vectors = [
            vector_from_row(row)
            for row in training_rows
        ]

        test_vectors = [
            vector_from_row(row)
            for row in test_rows
        ]

        (
            train_centroid,
            train_axis,
            train_eigenvalues,
            train_leading_fraction,
        ) = fit_principal_axis(
            training_vectors
        )

        (
            holdout_explained_fraction,
            test_point_metrics,
        ) = evaluate_axis(
            test_vectors,
            train_centroid,
            train_axis,
        )

        axis_alignment = abs(
            dot(
                train_axis,
                full_axis,
            )
        )

        finite_residuals = [
            metric[
                "normalized_residual"
            ]
            for metric in test_point_metrics
            if mp.isfinite(
                metric[
                    "normalized_residual"
                ]
            )
        ]

        fold_median_residual = median_mpf(
            finite_residuals
        )

        vertex_fraction = (
            mp.fsum(
                mp.mpf(
                    int(
                        max(
                            mp_value(
                                row["a_share"]
                            ),
                            mp_value(
                                row["e_share"]
                            ),
                            mp_value(
                                row["i_share"]
                            ),
                        )
                        >
                        mp.mpf("0.8")
                    )
                )
                for row in test_rows
            )
            /
            len(test_rows)
        )

        primary_training_fractions.append(
            train_leading_fraction
        )

        primary_holdout_fractions.append(
            holdout_explained_fraction
        )

        primary_axis_alignments.append(
            axis_alignment
        )

        primary_vertex_fractions.append(
            vertex_fraction
        )

        global_primary_normalized_residuals.extend(
            finite_residuals
        )

        primary_fold_rows.append(
            {
                "fold_number": fold_number,
                "heldout_windows": ",".join(
                    str(value)
                    for value in heldout_windows
                ),
                "training_window_count": 15,
                "training_point_count": len(
                    training_rows
                ),
                "test_window_count": 3,
                "test_point_count": len(
                    test_rows
                ),
                "training_leading_in_plane_fraction": mp.nstr(
                    train_leading_fraction,
                    60,
                ),
                "holdout_explained_fraction": mp.nstr(
                    holdout_explained_fraction,
                    60,
                ),
                "axis_alignment_with_full": mp.nstr(
                    axis_alignment,
                    60,
                ),
                "median_normalized_point_residual": mp.nstr(
                    fold_median_residual,
                    60,
                ),
                "vertex_dominant_fraction": mp.nstr(
                    vertex_fraction,
                    60,
                ),
            }
        )

        for row, metric in zip(
            test_rows,
            test_point_metrics,
        ):
            heldout_point_rows.append(
                {
                    "fold_number": fold_number,
                    "heldout_windows": ",".join(
                        str(value)
                        for value in heldout_windows
                    ),
                    "window_number": int(
                        row["window_number"]
                    ),
                    "requested_c": row[
                        "requested_c"
                    ],
                    "n": row["n"],
                    "a_share": row["a_share"],
                    "e_share": row["e_share"],
                    "i_share": row["i_share"],
                    "principal_coordinate": mp.nstr(
                        metric[
                            "principal_coordinate"
                        ],
                        60,
                    ),
                    "residual_squared": mp.nstr(
                        metric[
                            "residual_squared"
                        ],
                        60,
                    ),
                    "centered_squared": mp.nstr(
                        metric[
                            "centered_squared"
                        ],
                        60,
                    ),
                    "normalized_residual": mp.nstr(
                        metric[
                            "normalized_residual"
                        ],
                        60,
                    ),
                }
            )

        print(
            f"fold={fold_number} "
            f"holdout={heldout_windows} "
            f"trainF={mp.nstr(train_leading_fraction, 9)} "
            f"testF={mp.nstr(holdout_explained_fraction, 9)} "
            f"align={mp.nstr(axis_alignment, 9)} "
            f"rho50={mp.nstr(fold_median_residual, 9)} "
            f"vertex={mp.nstr(vertex_fraction, 6)}"
        )

    if len(heldout_point_rows) != 360:
        raise RuntimeError(
            "Each point must appear exactly once "
            "across the six primary holdout folds."
        )

    # Secondary leave-one-window-out audit.
    loo_rows: list[
        dict[str, str | int]
    ] = []

    loo_explained_fractions: list[
        mp.mpf
    ] = []

    loo_count_above_090 = 0

    print()
    print(
        "LEAVE-ONE-WINDOW-OUT AUDIT"
    )
    print("=" * 112)

    for heldout_window in windows:
        training_rows = [
            row
            for row in rows
            if int(
                row["window_number"]
            )
            != heldout_window
        ]

        test_rows = [
            row
            for row in rows
            if int(
                row["window_number"]
            )
            ==
            heldout_window
        ]

        if len(training_rows) != 340:
            raise RuntimeError(
                f"LOO window {heldout_window} "
                f"expected 340 training points."
            )

        if len(test_rows) != 20:
            raise RuntimeError(
                f"LOO window {heldout_window} "
                f"expected 20 test points."
            )

        training_vectors = [
            vector_from_row(row)
            for row in training_rows
        ]

        test_vectors = [
            vector_from_row(row)
            for row in test_rows
        ]

        (
            train_centroid,
            train_axis,
            _,
            train_leading_fraction,
        ) = fit_principal_axis(
            training_vectors
        )

        (
            holdout_explained_fraction,
            point_metrics,
        ) = evaluate_axis(
            test_vectors,
            train_centroid,
            train_axis,
        )

        axis_alignment = abs(
            dot(
                train_axis,
                full_axis,
            )
        )

        finite_residuals = [
            metric[
                "normalized_residual"
            ]
            for metric in point_metrics
            if mp.isfinite(
                metric[
                    "normalized_residual"
                ]
            )
        ]

        median_residual = median_mpf(
            finite_residuals
        )

        if (
            holdout_explained_fraction
            >
            mp.mpf("0.90")
        ):
            loo_count_above_090 += 1

        loo_explained_fractions.append(
            holdout_explained_fraction
        )

        loo_rows.append(
            {
                "heldout_window": (
                    heldout_window
                ),
                "training_window_count": 17,
                "training_point_count": len(
                    training_rows
                ),
                "test_point_count": len(
                    test_rows
                ),
                "training_leading_in_plane_fraction": mp.nstr(
                    train_leading_fraction,
                    60,
                ),
                "holdout_explained_fraction": mp.nstr(
                    holdout_explained_fraction,
                    60,
                ),
                "axis_alignment_with_full": mp.nstr(
                    axis_alignment,
                    60,
                ),
                "median_normalized_point_residual": mp.nstr(
                    median_residual,
                    60,
                ),
            }
        )

        print(
            f"window={heldout_window:<2d} "
            f"testF={mp.nstr(holdout_explained_fraction, 10):>12s} "
            f"align={mp.nstr(axis_alignment, 10):>12s} "
            f"rho50={mp.nstr(median_residual, 10):>12s}"
        )

    p_hld_001 = all(
        value > mp.mpf("0.99")
        for value in primary_training_fractions
    )

    median_holdout_fraction = median_mpf(
        primary_holdout_fractions
    )

    mean_holdout_fraction = mean_mpf(
        primary_holdout_fractions
    )

    minimum_holdout_fraction = min(
        primary_holdout_fractions
    )

    p_hld_002 = (
        median_holdout_fraction
        >
        mp.mpf("0.95")
    )

    p_hld_003 = (
        minimum_holdout_fraction
        >
        mp.mpf("0.85")
    )

    minimum_axis_alignment = min(
        primary_axis_alignments
    )

    p_hld_004 = (
        minimum_axis_alignment
        >
        mp.mpf("0.995")
    )

    global_median_normalized_residual = (
        median_mpf(
            global_primary_normalized_residuals
        )
    )

    p_hld_005 = (
        global_median_normalized_residual
        <
        mp.mpf("0.20")
    )

    p_hld_006 = (
        loo_count_above_090
        >=
        16
    )

    maximum_vertex_fraction = max(
        primary_vertex_fractions
    )

    p_hld_007 = all(
        value < mp.mpf("0.40")
        for value in primary_vertex_fractions
    )

    with POINT_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                heldout_point_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            heldout_point_rows
        )

    with PRIMARY_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                primary_fold_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            primary_fold_rows
        )

    with LOO_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                loo_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            loo_rows
        )

    runtime_seconds = (
        time.perf_counter()
        -
        started
    )

    summary = {
        "experiment_name": (
            "li_zeta_window_principal_axis_holdout"
        ),
        "point_count": len(rows),
        "window_count": len(windows),
        "full_sample_leading_in_plane_fraction": mp.nstr(
            full_leading_fraction,
            50,
        ),
        "full_sample_covariance_eigenvalues_descending": [
            mp.nstr(
                value,
                50,
            )
            for value in full_eigenvalues
        ],
        "primary_fold_definitions": [
            list(fold)
            for fold in PRIMARY_FOLDS
        ],
        "primary_training_leading_fractions": [
            mp.nstr(
                value,
                50,
            )
            for value in primary_training_fractions
        ],
        "primary_holdout_explained_fractions": [
            mp.nstr(
                value,
                50,
            )
            for value in primary_holdout_fractions
        ],
        "minimum_primary_holdout_explained_fraction": mp.nstr(
            minimum_holdout_fraction,
            50,
        ),
        "median_primary_holdout_explained_fraction": mp.nstr(
            median_holdout_fraction,
            50,
        ),
        "mean_primary_holdout_explained_fraction": mp.nstr(
            mean_holdout_fraction,
            50,
        ),
        "primary_axis_alignments_with_full": [
            mp.nstr(
                value,
                50,
            )
            for value in primary_axis_alignments
        ],
        "minimum_primary_axis_alignment": mp.nstr(
            minimum_axis_alignment,
            50,
        ),
        "global_primary_median_normalized_residual": mp.nstr(
            global_median_normalized_residual,
            50,
        ),
        "primary_vertex_dominant_fractions": [
            mp.nstr(
                value,
                50,
            )
            for value in primary_vertex_fractions
        ],
        "maximum_primary_vertex_dominant_fraction": mp.nstr(
            maximum_vertex_fraction,
            50,
        ),
        "leave_one_window_out_explained_fractions": {
            str(row["heldout_window"]): row[
                "holdout_explained_fraction"
            ]
            for row in loo_rows
        },
        "leave_one_window_out_count_above_0_90": (
            loo_count_above_090
        ),
        "leave_one_window_out_minimum_explained_fraction": mp.nstr(
            min(
                loo_explained_fractions
            ),
            50,
        ),
        "leave_one_window_out_median_explained_fraction": mp.nstr(
            median_mpf(
                loo_explained_fractions
            ),
            50,
        ),
        "P_HLD_001": (
            "PASS"
            if p_hld_001
            else "FAIL"
        ),
        "P_HLD_002": (
            "PASS"
            if p_hld_002
            else "FAIL"
        ),
        "P_HLD_003": (
            "PASS"
            if p_hld_003
            else "FAIL"
        ),
        "P_HLD_004": (
            "PASS"
            if p_hld_004
            else "FAIL"
        ),
        "P_HLD_005": (
            "PASS"
            if p_hld_005
            else "FAIL"
        ),
        "P_HLD_006": (
            "PASS"
            if p_hld_006
            else "FAIL"
        ),
        "P_HLD_007": (
            "PASS"
            if p_hld_007
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
            "Window-level holdout validation inside "
            "the frozen first-500-zero dataset. Entire "
            "test windows are excluded from PCA fitting. "
            "This is not external dataset replication. "
            "No asymptotic, off-critical-zero, predictive "
            "RH, or RH consequence is claimed."
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
        "PHASE 5K — PRINCIPAL-AXIS HOLDOUT SUMMARY"
    )
    print("=" * 112)

    for key, value in summary.items():
        print(
            f"{key}: {value}"
        )

    print()
    print(
        f"Held-out point CSV: {POINT_CSV}"
    )

    print(
        f"Primary fold CSV: {PRIMARY_CSV}"
    )

    print(
        f"LOO CSV: {LOO_CSV}"
    )

    print(
        f"Summary JSON: {SUMMARY_JSON}"
    )

    print()
    print(
        "PHASE 5K PRINCIPAL-AXIS HOLDOUT: COMPLETE"
    )


if __name__ == "__main__":
    main()
