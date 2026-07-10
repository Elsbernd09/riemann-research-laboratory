from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path

import mpmath as mp


INPUT_CSV = Path(
    "results/li_zeta_window_component_share_simplex/"
    "simplex_points.csv"
)

OUTPUT_JSON = Path(
    "results/phase5l_frozen_primary_axis.json"
)


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


def dot(
    left: mp.matrix,
    right: mp.matrix,
) -> mp.mpf:
    return mp.fsum(
        left[index] * right[index]
        for index in range(3)
    )


def norm(
    vector: mp.matrix,
) -> mp.mpf:
    return mp.sqrt(
        dot(vector, vector)
    )


def main() -> None:
    mp.mp.dps = 80

    if not INPUT_CSV.exists():
        raise FileNotFoundError(
            f"Missing Phase 5J simplex CSV: "
            f"{INPUT_CSV}"
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
            f"Expected 360 frozen simplex rows, "
            f"got {len(rows)}"
        )

    vectors = [
        mp.matrix(
            [
                mp_value(row["a_share"]),
                mp_value(row["e_share"]),
                mp_value(row["i_share"]),
            ]
        )
        for row in rows
    ]

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

    axis = eigenpairs[0][1]
    axis = axis / norm(axis)

    # Canonicalize PCA sign.
    #
    # The first coordinate with magnitude above 1e-40
    # is required to be positive.
    for index in range(3):
        if abs(axis[index]) > mp.mpf("1e-40"):
            if axis[index] < 0:
                axis = -axis
            break

    positive_eigenvalues = [
        pair[0]
        for pair in eigenpairs
        if pair[0] > mp.mpf("1e-50")
    ]

    if len(positive_eigenvalues) != 2:
        raise RuntimeError(
            "Expected exactly two positive "
            "simplex-plane eigenvalues."
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

    artifact = {
        "artifact_name": (
            "phase5l_frozen_first500_principal_axis"
        ),
        "source_population": (
            "Phase 5J frozen 360-point simplex population "
            "derived from first 500 computed critical-line zeros"
        ),
        "source_csv": str(INPUT_CSV),
        "source_csv_sha256": sha256_file(
            INPUT_CSV
        ),
        "source_point_count": len(rows),
        "centroid": [
            mp.nstr(
                centroid[index],
                80,
            )
            for index in range(3)
        ],
        "canonical_principal_axis": [
            mp.nstr(
                axis[index],
                80,
            )
            for index in range(3)
        ],
        "covariance_eigenvalues_descending": [
            mp.nstr(
                pair[0],
                80,
            )
            for pair in eigenpairs
        ],
        "leading_in_plane_fraction": mp.nstr(
            leading_fraction,
            80,
        ),
        "axis_sign_rule": (
            "First coordinate with absolute magnitude "
            "above 1e-40 is positive."
        ),
        "higher_zero_index_start": 501,
        "higher_zero_index_end": 1500,
        "higher_zero_count": 1000,
        "zero_generation_decimal_digits": 80,
        "zero_validation_absolute_zeta_threshold": (
            "1e-40"
        ),
        "frozen_anchor_zero_indices": [
            550,
            700,
            850,
            1000,
            1150,
            1300,
            1400,
        ],
        "frozen_eta_values": [
            "0.05",
            "0.10",
            "0.20",
            "0.50",
        ],
        "minimum_window_occupancy": 25,
        "requested_c_values": list(
            range(1, 21)
        ),
        "git_commit_at_freeze": git_output(
            "rev-parse",
            "HEAD",
        ),
        "interpretation_boundary": (
            "The centroid and principal axis are frozen "
            "before generation or inspection of any "
            "Phase 5L higher-zero component-share point."
        ),
    }

    OUTPUT_JSON.write_text(
        json.dumps(
            artifact,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        "PHASE 5L PRIMARY AXIS FROZEN"
    )
    print("=" * 96)

    print(
        "centroid:"
    )

    for value in artifact["centroid"]:
        print(
            f"  {value}"
        )

    print(
        "canonical_principal_axis:"
    )

    for value in artifact[
        "canonical_principal_axis"
    ]:
        print(
            f"  {value}"
        )

    print(
        "leading_in_plane_fraction: "
        f"{artifact['leading_in_plane_fraction']}"
    )

    print(
        f"artifact: {OUTPUT_JSON}"
    )


if __name__ == "__main__":
    main()
