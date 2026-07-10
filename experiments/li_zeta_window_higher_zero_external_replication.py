from __future__ import annotations

import bisect
import csv
import hashlib
import json
import platform
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

import experiments.li_zeta_window_discrepancy_decomposition as dec
from src.li_susceptibility import (
    li_susceptibility_exact,
    li_susceptibility_gamma_derivative,
)


FROZEN_AXIS_JSON = Path(
    "results/phase5l_frozen_primary_axis.json"
)

DATASET_AUDIT_JSON = Path(
    "results/phase5l_higher_zero_dataset_audit.json"
)

HIGHER_ZERO_CSV = Path(
    "data/zeta_zeros/"
    "mpmath_critical_line_zeros_indices_501_1500.csv"
)

RESULT_DIR = Path(
    "results/li_zeta_window_higher_zero_external_replication"
)

POINT_CSV = RESULT_DIR / "external_simplex_points.csv"
WINDOW_CSV = RESULT_DIR / "external_window_metrics.csv"
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
    return dot(vector, vector)


def unit_vector(
    vector: mp.matrix,
) -> mp.matrix:
    norm = mp.sqrt(
        squared_norm(vector)
    )

    if norm == 0:
        raise ArithmeticError(
            "Cannot normalize a zero vector."
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


def empirical_absolute_count(
    gammas: list[mp.mpf],
    t: mp.mpf,
) -> int:
    # The generated higher block begins at
    # authoritative zero index 501.
    #
    # Exactly 500 critical-line ordinates precede
    # this block in the numerical enumeration.
    return (
        500
        +
        bisect.bisect_right(
            gammas,
            t,
        )
    )


def empirical_absolute_remainder(
    gammas: list[mp.mpf],
    t: mp.mpf,
) -> mp.mpf:
    return (
        mp.mpf(
            empirical_absolute_count(
                gammas,
                t,
            )
        )
        -
        dec.smooth_counting_model(t)
    )


def fit_principal_axis(
    vectors: list[mp.matrix],
) -> tuple[
    mp.matrix,
    mp.matrix,
    list[mp.mpf],
    mp.mpf,
]:
    centroid = mp.matrix(
        [
            mp.fsum(
                vector[index]
                for vector in vectors
            )
            /
            len(vectors)
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
        mp.eigsy(covariance)
    )

    eigenpairs = sorted(
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

    leading_axis = unit_vector(
        eigenpairs[0][1]
    )

    positive_eigenvalues = [
        pair[0]
        for pair in eigenpairs
        if pair[0] > mp.mpf("1e-50")
    ]

    if len(positive_eigenvalues) != 2:
        raise RuntimeError(
            "Expected exactly two positive "
            "simplex-plane covariance eigenvalues."
        )

    leading_fraction = (
        positive_eigenvalues[0]
        /
        (
            positive_eigenvalues[0]
            +
            positive_eigenvalues[1]
        )
    )

    return (
        centroid,
        leading_axis,
        [
            pair[0]
            for pair in eigenpairs
        ],
        leading_fraction,
    )


def evaluate_frozen_line(
    vectors: list[mp.matrix],
    centroid: mp.matrix,
    axis: mp.matrix,
) -> tuple[
    mp.mpf,
    list[dict[str, mp.mpf]],
]:
    residual_energy = mp.mpf("0")
    centered_energy = mp.mpf("0")

    metrics: list[
        dict[str, mp.mpf]
    ] = []

    for vector in vectors:
        centered = vector - centroid

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

        residual_energy += residual_squared
        centered_energy += centered_squared

        if centered_squared == 0:
            normalized_residual = mp.nan
        else:
            normalized_residual = (
                mp.sqrt(residual_squared)
                /
                mp.sqrt(centered_squared)
            )

        metrics.append(
            {
                "principal_coordinate": coordinate,
                "residual_squared": residual_squared,
                "centered_squared": centered_squared,
                "normalized_residual": normalized_residual,
            }
        )

    if centered_energy == 0:
        explained_fraction = mp.nan
    else:
        explained_fraction = (
            1
            -
            residual_energy
            /
            centered_energy
        )

    return (
        explained_fraction,
        metrics,
    )


def main() -> None:
    started = time.perf_counter()

    mp.mp.dps = 60

    for path in (
        FROZEN_AXIS_JSON,
        DATASET_AUDIT_JSON,
        HIGHER_ZERO_CSV,
    ):
        if not path.exists():
            raise FileNotFoundError(
                f"Missing required Phase 5L artifact: "
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

    dataset_audit = json.loads(
        DATASET_AUDIT_JSON.read_text(
            encoding="utf-8"
        )
    )

    if (
        dataset_audit[
            "P_EXT_001_REAUDIT"
        ]
        !=
        "PASS"
    ):
        raise RuntimeError(
            "Phase 5L dataset reaudit is not PASS."
        )

    current_higher_sha = sha256_file(
        HIGHER_ZERO_CSV
    )

    if (
        current_higher_sha
        !=
        dataset_audit[
            "current_higher_zero_sha256"
        ]
    ):
        raise RuntimeError(
            "Higher-zero dataset hash drift detected."
        )

    primary_source = Path(
        frozen["source_csv"]
    )

    if (
        sha256_file(primary_source)
        !=
        frozen["source_csv_sha256"]
    ):
        raise RuntimeError(
            "Frozen primary-axis source hash drift "
            "detected."
        )

    frozen_centroid = mp.matrix(
        [
            mp.mpf(value)
            for value in frozen["centroid"]
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

    anchor_indices = [
        int(value)
        for value in frozen[
            "frozen_anchor_zero_indices"
        ]
    ]

    eta_values = [
        mp.mpf(value)
        for value in frozen[
            "frozen_eta_values"
        ]
    ]

    requested_c_values = [
        mp.mpf(value)
        for value in frozen[
            "requested_c_values"
        ]
    ]

    minimum_occupancy = int(
        frozen["minimum_window_occupancy"]
    )

    with HIGHER_ZERO_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        zero_rows = list(
            csv.DictReader(handle)
        )

    indices = [
        int(row["zero_index"])
        for row in zero_rows
    ]

    gammas = [
        mp.mpf(row["gamma"])
        for row in zero_rows
    ]

    index_to_gamma = {
        index: gamma
        for index, gamma in zip(
            indices,
            gammas,
        )
    }

    last_gamma = gammas[-1]

    eligible_windows: list[
        dict[str, object]
    ] = []

    frozen_pairs: list[
        dict[str, object]
    ] = []

    for anchor_index in anchor_indices:
        H = index_to_gamma[
            anchor_index
        ]

        for eta in eta_values:
            B = (
                (1 + eta) * H
            )

            endpoint_contained = (
                B <= last_gamma
            )

            if endpoint_contained:
                window_gammas = [
                    gamma
                    for gamma in gammas
                    if H <= gamma <= B
                ]

                occupancy = len(
                    window_gammas
                )
            else:
                window_gammas = []
                occupancy = 0

            eligible = (
                endpoint_contained
                and occupancy
                >=
                minimum_occupancy
            )

            frozen_pairs.append(
                {
                    "anchor_zero_index": (
                        anchor_index
                    ),
                    "eta": eta,
                    "H": H,
                    "B": B,
                    "endpoint_contained": (
                        endpoint_contained
                    ),
                    "occupancy": occupancy,
                    "eligible": eligible,
                }
            )

            if eligible:
                eligible_windows.append(
                    {
                        "anchor_zero_index": (
                            anchor_index
                        ),
                        "eta": eta,
                        "H": H,
                        "B": B,
                        "occupancy": occupancy,
                    }
                )

    if not eligible_windows:
        raise RuntimeError(
            "Frozen Phase 5L rules produced no "
            "eligible higher-zero windows."
        )

    print(
        "PHASE 5L — HIGHER-ZERO EXTERNAL REPLICATION"
    )
    print("=" * 116)

    print(
        f"Frozen anchor-width pairs: "
        f"{len(frozen_pairs)}"
    )

    print(
        f"Eligible higher-zero windows: "
        f"{len(eligible_windows)}"
    )

    print(
        "Eligible windows were selected only by "
        "endpoint containment and frozen occupancy."
    )

    point_rows: list[
        dict[str, str | int]
    ] = []

    external_vectors: list[
        mp.matrix
    ] = []

    window_vectors: dict[
        int,
        list[mp.matrix],
    ] = {}

    for window_number, window in enumerate(
        eligible_windows,
        start=1,
    ):
        anchor_index = int(
            window["anchor_zero_index"]
        )

        eta = mp.mpf(
            window["eta"]
        )

        H = mp.mpf(
            window["H"]
        )

        B = mp.mpf(
            window["B"]
        )

        occupancy = int(
            window["occupancy"]
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

        E_H = empirical_absolute_remainder(
            gammas,
            H,
        )

        E_B = empirical_absolute_remainder(
            gammas,
            B,
        )

        print()
        print(
            f"window={window_number:<2d} "
            f"anchor={anchor_index:<4d} "
            f"eta={mp.nstr(eta, 5):>5s} "
            f"H={mp.nstr(H, 13):>15s} "
            f"N={occupancy:<4d}"
        )

        window_vectors[
            window_number
        ] = []

        for c_requested in requested_c_values:
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

            atom_component = f(H)

            endpoint_component = (
                f(B) * E_B
                -
                f(H) * E_H
            )

            weighted_pieces: list[
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
                    empirical_absolute_count(
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

                weighted_pieces.append(
                    mp.quad(
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
                )

            weighted_integral = mp.fsum(
                weighted_pieces
            )

            interior_component = (
                -weighted_integral
            )

            count_remainder = (
                atom_component
                +
                endpoint_component
                +
                interior_component
            )

            magnitude_sum = (
                abs(atom_component)
                +
                abs(endpoint_component)
                +
                abs(interior_component)
            )

            if magnitude_sum <= 0:
                raise ArithmeticError(
                    "Nonpositive response-component "
                    "magnitude sum."
                )

            a_share = (
                abs(atom_component)
                /
                magnitude_sum
            )

            e_share = (
                abs(endpoint_component)
                /
                magnitude_sum
            )

            i_share = (
                abs(interior_component)
                /
                magnitude_sum
            )

            simplex_closure_error = abs(
                a_share
                +
                e_share
                +
                i_share
                -
                1
            )

            if (
                simplex_closure_error
                >
                mp.mpf("1e-45")
            ):
                raise ArithmeticError(
                    "External simplex closure failure."
                )

            vector = mp.matrix(
                [
                    a_share,
                    e_share,
                    i_share,
                ]
            )

            external_vectors.append(
                vector
            )

            window_vectors[
                window_number
            ].append(
                vector
            )

            point_rows.append(
                {
                    "window_number": (
                        window_number
                    ),
                    "anchor_zero_index": (
                        anchor_index
                    ),
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
                    "E_H": mp.nstr(
                        E_H,
                        60,
                    ),
                    "E_B": mp.nstr(
                        E_B,
                        60,
                    ),
                    "atom_component": mp.nstr(
                        atom_component,
                        60,
                    ),
                    "endpoint_component": mp.nstr(
                        endpoint_component,
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
                        simplex_closure_error,
                        60,
                    ),
                    "dominant_share": mp.nstr(
                        max(
                            a_share,
                            e_share,
                            i_share,
                        ),
                        60,
                    ),
                }
            )

            print(
                f"  c={int(c_requested):>2d} "
                f"a={mp.nstr(a_share, 6):>9s} "
                f"e={mp.nstr(e_share, 6):>9s} "
                f"i={mp.nstr(i_share, 6):>9s}"
            )

    # -------------------------------------------------
    # PRIMARY FROZEN-AXIS SCORING
    #
    # No higher-zero PCA has been fitted above this line.
    # -------------------------------------------------

    (
        external_explained_fraction,
        external_point_metrics,
    ) = evaluate_frozen_line(
        external_vectors,
        frozen_centroid,
        frozen_axis,
    )

    external_normalized_residuals = [
        metric["normalized_residual"]
        for metric in external_point_metrics
        if mp.isfinite(
            metric["normalized_residual"]
        )
    ]

    median_external_normalized_residual = (
        median_mpf(
            external_normalized_residuals
        )
    )

    for row, metric in zip(
        point_rows,
        external_point_metrics,
    ):
        row[
            "frozen_axis_principal_coordinate"
        ] = mp.nstr(
            metric[
                "principal_coordinate"
            ],
            60,
        )

        row[
            "frozen_axis_residual_squared"
        ] = mp.nstr(
            metric[
                "residual_squared"
            ],
            60,
        )

        row[
            "frozen_axis_centered_squared"
        ] = mp.nstr(
            metric[
                "centered_squared"
            ],
            60,
        )

        row[
            "frozen_axis_normalized_residual"
        ] = mp.nstr(
            metric[
                "normalized_residual"
            ],
            60,
        )

    window_rows: list[
        dict[str, str | int]
    ] = []

    window_explained_fractions: list[
        mp.mpf
    ] = []

    for window_number, vectors in sorted(
        window_vectors.items()
    ):
        (
            window_explained_fraction,
            window_point_metrics,
        ) = evaluate_frozen_line(
            vectors,
            frozen_centroid,
            frozen_axis,
        )

        finite_residuals = [
            metric["normalized_residual"]
            for metric in window_point_metrics
            if mp.isfinite(
                metric["normalized_residual"]
            )
        ]

        matching_point = next(
            row
            for row in point_rows
            if int(row["window_number"])
            ==
            window_number
        )

        window_explained_fractions.append(
            window_explained_fraction
        )

        window_rows.append(
            {
                "window_number": (
                    window_number
                ),
                "anchor_zero_index": (
                    matching_point[
                        "anchor_zero_index"
                    ]
                ),
                "eta": matching_point["eta"],
                "H": matching_point["H"],
                "occupancy": matching_point[
                    "occupancy"
                ],
                "point_count": len(vectors),
                "frozen_axis_explained_fraction": mp.nstr(
                    window_explained_fraction,
                    60,
                ),
                "median_normalized_residual": mp.nstr(
                    median_mpf(
                        finite_residuals
                    ),
                    60,
                ),
                "vertex_dominant_fraction": mp.nstr(
                    mp.fsum(
                        mp.mpf(
                            int(
                                max(
                                    vector[index]
                                    for index in range(3)
                                )
                                >
                                mp.mpf("0.8")
                            )
                        )
                        for vector in vectors
                    )
                    /
                    len(vectors),
                    60,
                ),
            }
        )

    window_count_above_090 = sum(
        value > mp.mpf("0.90")
        for value in window_explained_fractions
    )

    window_fraction_above_090 = (
        mp.mpf(
            window_count_above_090
        )
        /
        len(
            window_explained_fractions
        )
    )

    minimum_window_explained_fraction = min(
        window_explained_fractions
    )

    p_ext_002 = (
        external_explained_fraction
        >
        mp.mpf("0.95")
    )

    p_ext_003 = (
        median_external_normalized_residual
        <
        mp.mpf("0.20")
    )

    p_ext_004 = (
        window_fraction_above_090
        >=
        mp.mpf("0.80")
    )

    p_ext_005 = (
        minimum_window_explained_fraction
        >
        mp.mpf("0.75")
    )

    primary_score_snapshot = {
        "P_EXT_002": (
            "PASS"
            if p_ext_002
            else "FAIL"
        ),
        "P_EXT_003": (
            "PASS"
            if p_ext_003
            else "FAIL"
        ),
        "P_EXT_004": (
            "PASS"
            if p_ext_004
            else "FAIL"
        ),
        "P_EXT_005": (
            "PASS"
            if p_ext_005
            else "FAIL"
        ),
        "external_explained_fraction": (
            mp.nstr(
                external_explained_fraction,
                80,
            )
        ),
        "median_external_normalized_residual": (
            mp.nstr(
                median_external_normalized_residual,
                80,
            )
        ),
        "window_fraction_above_0_90": (
            mp.nstr(
                window_fraction_above_090,
                80,
            )
        ),
        "minimum_window_explained_fraction": (
            mp.nstr(
                minimum_window_explained_fraction,
                80,
            )
        ),
    }

    # -------------------------------------------------
    # SECONDARY HIGHER-ZERO PCA
    #
    # Primary P-EXT-002 through P-EXT-005 have already
    # been calculated and snapshotted above.
    # -------------------------------------------------

    (
        higher_centroid,
        higher_axis,
        higher_eigenvalues,
        higher_leading_fraction,
    ) = fit_principal_axis(
        external_vectors
    )

    higher_axis_alignment = abs(
        dot(
            higher_axis,
            frozen_axis,
        )
    )

    p_ext_006 = (
        higher_axis_alignment
        >
        mp.mpf("0.995")
    )

    p_ext_007 = (
        higher_leading_fraction
        >
        mp.mpf("0.95")
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

    runtime_seconds = (
        time.perf_counter()
        -
        started
    )

    summary = {
        "experiment_name": (
            "li_zeta_window_higher_zero_"
            "external_replication"
        ),
        "higher_zero_csv_sha256": (
            current_higher_sha
        ),
        "frozen_primary_source_sha256": (
            frozen["source_csv_sha256"]
        ),
        "eligible_window_count": len(
            eligible_windows
        ),
        "external_point_count": len(
            point_rows
        ),
        "eligible_windows": [
            {
                "window_number": (
                    window_number
                ),
                "anchor_zero_index": int(
                    window[
                        "anchor_zero_index"
                    ]
                ),
                "eta": mp.nstr(
                    mp.mpf(window["eta"]),
                    20,
                ),
                "occupancy": int(
                    window["occupancy"]
                ),
            }
            for window_number, window in enumerate(
                eligible_windows,
                start=1,
            )
        ],
        "primary_scores_frozen_before_secondary_refit": (
            primary_score_snapshot
        ),
        "external_frozen_axis_explained_fraction": (
            mp.nstr(
                external_explained_fraction,
                50,
            )
        ),
        "median_external_normalized_residual": (
            mp.nstr(
                median_external_normalized_residual,
                50,
            )
        ),
        "window_count_above_0_90": (
            window_count_above_090
        ),
        "window_fraction_above_0_90": (
            mp.nstr(
                window_fraction_above_090,
                50,
            )
        ),
        "minimum_window_explained_fraction": (
            mp.nstr(
                minimum_window_explained_fraction,
                50,
            )
        ),
        "median_window_explained_fraction": (
            mp.nstr(
                median_mpf(
                    window_explained_fractions
                ),
                50,
            )
        ),
        "mean_window_explained_fraction": (
            mp.nstr(
                mean_mpf(
                    window_explained_fractions
                ),
                50,
            )
        ),
        "higher_zero_refitted_centroid": [
            mp.nstr(
                higher_centroid[index],
                50,
            )
            for index in range(3)
        ],
        "higher_zero_refitted_axis": [
            mp.nstr(
                higher_axis[index],
                50,
            )
            for index in range(3)
        ],
        "higher_zero_covariance_eigenvalues_descending": [
            mp.nstr(
                value,
                50,
            )
            for value in higher_eigenvalues
        ],
        "higher_zero_leading_in_plane_fraction": (
            mp.nstr(
                higher_leading_fraction,
                50,
            )
        ),
        "higher_zero_axis_alignment_with_frozen_primary": (
            mp.nstr(
                higher_axis_alignment,
                50,
            )
        ),
        "P_EXT_001": "PASS",
        "P_EXT_002": (
            "PASS"
            if p_ext_002
            else "FAIL"
        ),
        "P_EXT_003": (
            "PASS"
            if p_ext_003
            else "FAIL"
        ),
        "P_EXT_004": (
            "PASS"
            if p_ext_004
            else "FAIL"
        ),
        "P_EXT_005": (
            "PASS"
            if p_ext_005
            else "FAIL"
        ),
        "P_EXT_006": (
            "PASS"
            if p_ext_006
            else "FAIL"
        ),
        "P_EXT_007": (
            "PASS"
            if p_ext_007
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
            "Disjoint higher-zero window replication "
            "against a first-500 centroid and principal "
            "axis frozen before higher-zero share "
            "generation. Primary frozen-axis metrics "
            "were scored before secondary higher-zero "
            "PCA refitting. This is finite numerical "
            "replication, not statistical independence, "
            "an asymptotic theorem, an off-critical-zero "
            "constraint, or an RH consequence."
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
        "PHASE 5L — PRIMARY FROZEN-AXIS SCORES"
    )
    print("=" * 116)

    for key, value in (
        primary_score_snapshot.items()
    ):
        print(
            f"{key}: {value}"
        )

    print()
    print("=" * 116)
    print(
        "PHASE 5L — SECONDARY REFIT DIAGNOSTICS"
    )
    print("=" * 116)

    print(
        "higher_zero_axis_alignment_with_frozen_primary: "
        f"{mp.nstr(higher_axis_alignment, 50)}"
    )

    print(
        "higher_zero_leading_in_plane_fraction: "
        f"{mp.nstr(higher_leading_fraction, 50)}"
    )

    print()
    print("=" * 116)
    print(
        "PHASE 5L FINAL SCORECARD"
    )
    print("=" * 116)

    for prediction in (
        "P_EXT_001",
        "P_EXT_002",
        "P_EXT_003",
        "P_EXT_004",
        "P_EXT_005",
        "P_EXT_006",
        "P_EXT_007",
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
        f"Window CSV: {WINDOW_CSV}"
    )

    print(
        f"Summary JSON: {SUMMARY_JSON}"
    )

    print()
    print(
        "PHASE 5L HIGHER-ZERO EXTERNAL "
        "REPLICATION: COMPLETE"
    )


if __name__ == "__main__":
    main()
