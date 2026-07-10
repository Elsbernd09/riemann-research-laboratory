from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import mpmath as mp


PRIMARY_AXIS_JSON = Path(
    "results/phase5l_frozen_primary_axis.json"
)

HIGHER_ZERO_CSV = Path(
    "data/zeta_zeros/"
    "mpmath_critical_line_zeros_indices_501_1500.csv"
)

HIGHER_ZERO_METADATA = Path(
    "data/zeta_zeros/"
    "mpmath_critical_line_zeros_indices_501_1500_metadata.json"
)

AUDIT_JSON = Path(
    "results/phase5l_higher_zero_dataset_audit.json"
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


def main() -> None:
    mp.mp.dps = 80

    for path in (
        PRIMARY_AXIS_JSON,
        HIGHER_ZERO_CSV,
        HIGHER_ZERO_METADATA,
    ):
        if not path.exists():
            raise FileNotFoundError(
                f"Missing required artifact: {path}"
            )

    frozen = json.loads(
        PRIMARY_AXIS_JSON.read_text(
            encoding="utf-8"
        )
    )

    metadata = json.loads(
        HIGHER_ZERO_METADATA.read_text(
            encoding="utf-8"
        )
    )

    source_csv = Path(
        frozen["source_csv"]
    )

    if not source_csv.exists():
        raise FileNotFoundError(
            "Frozen first-500 simplex source CSV "
            f"is missing: {source_csv}"
        )

    current_primary_source_sha = sha256_file(
        source_csv
    )

    frozen_primary_source_sha = frozen[
        "source_csv_sha256"
    ]

    primary_axis_source_unchanged = (
        current_primary_source_sha
        ==
        frozen_primary_source_sha
    )

    current_higher_zero_sha = sha256_file(
        HIGHER_ZERO_CSV
    )

    metadata_higher_zero_sha = metadata[
        "csv_sha256"
    ]

    higher_zero_hash_matches_metadata = (
        current_higher_zero_sha
        ==
        metadata_higher_zero_sha
    )

    with HIGHER_ZERO_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        rows = list(
            csv.DictReader(handle)
        )

    indices = [
        int(row["zero_index"])
        for row in rows
    ]

    gammas = [
        mp.mpf(row["gamma"])
        for row in rows
    ]

    residuals = [
        mp.mpf(
            row["absolute_zeta_residual"]
        )
        for row in rows
    ]

    expected_indices = list(
        range(501, 1501)
    )

    exact_index_sequence = (
        indices == expected_indices
    )

    strictly_increasing_gamma = all(
        left < right
        for left, right in zip(
            gammas,
            gammas[1:],
        )
    )

    all_residuals_below_threshold = all(
        residual < mp.mpf("1e-40")
        for residual in residuals
    )

    expected_count = (
        len(rows) == 1000
    )

    disjoint_from_primary_indices = (
        min(indices) > 500
    )

    frozen_range_matches = (
        frozen["higher_zero_index_start"]
        == 501
        and frozen["higher_zero_index_end"]
        == 1500
        and frozen["higher_zero_count"]
        == 1000
    )

    frozen_anchor_indices_match = (
        frozen["frozen_anchor_zero_indices"]
        ==
        [
            550,
            700,
            850,
            1000,
            1150,
            1300,
            1400,
        ]
    )

    frozen_eta_values_match = (
        frozen["frozen_eta_values"]
        ==
        [
            "0.05",
            "0.10",
            "0.20",
            "0.50",
        ]
    )

    frozen_c_grid_matches = (
        frozen["requested_c_values"]
        ==
        list(range(1, 21))
    )

    p_ext_001_reaudit = all(
        (
            primary_axis_source_unchanged,
            higher_zero_hash_matches_metadata,
            exact_index_sequence,
            strictly_increasing_gamma,
            all_residuals_below_threshold,
            expected_count,
            disjoint_from_primary_indices,
            frozen_range_matches,
            frozen_anchor_indices_match,
            frozen_eta_values_match,
            frozen_c_grid_matches,
        )
    )

    audit = {
        "audit_name": (
            "phase5l_higher_zero_dataset_audit"
        ),
        "primary_axis_source_csv": str(
            source_csv
        ),
        "frozen_primary_source_sha256": (
            frozen_primary_source_sha
        ),
        "current_primary_source_sha256": (
            current_primary_source_sha
        ),
        "primary_axis_source_unchanged": (
            primary_axis_source_unchanged
        ),
        "higher_zero_csv": str(
            HIGHER_ZERO_CSV
        ),
        "metadata_higher_zero_sha256": (
            metadata_higher_zero_sha
        ),
        "current_higher_zero_sha256": (
            current_higher_zero_sha
        ),
        "higher_zero_hash_matches_metadata": (
            higher_zero_hash_matches_metadata
        ),
        "row_count": len(rows),
        "exact_index_sequence_501_through_1500": (
            exact_index_sequence
        ),
        "strictly_increasing_gamma": (
            strictly_increasing_gamma
        ),
        "all_residuals_below_1e_minus_40": (
            all_residuals_below_threshold
        ),
        "maximum_stored_absolute_zeta_residual": (
            mp.nstr(
                max(residuals),
                80,
            )
        ),
        "first_zero_index": min(indices),
        "last_zero_index": max(indices),
        "first_gamma": mp.nstr(
            gammas[0],
            80,
        ),
        "last_gamma": mp.nstr(
            gammas[-1],
            80,
        ),
        "authoritative_index_disjointness_from_primary": (
            disjoint_from_primary_indices
        ),
        "frozen_range_matches": (
            frozen_range_matches
        ),
        "frozen_anchor_indices_match": (
            frozen_anchor_indices_match
        ),
        "frozen_eta_values_match": (
            frozen_eta_values_match
        ),
        "frozen_c_grid_matches": (
            frozen_c_grid_matches
        ),
        "P_EXT_001_REAUDIT": (
            "PASS"
            if p_ext_001_reaudit
            else "FAIL"
        ),
        "scoring_status": (
            "NO HIGHER-ZERO COMPONENT SHARES "
            "OR EXTERNAL PRINCIPAL-AXIS SCORES "
            "COMPUTED BY THIS AUDIT"
        ),
    }

    AUDIT_JSON.write_text(
        json.dumps(
            audit,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        "PHASE 5L — HIGHER-ZERO DATASET AUDIT"
    )
    print("=" * 100)

    for key, value in audit.items():
        print(
            f"{key}: {value}"
        )

    if not p_ext_001_reaudit:
        raise RuntimeError(
            "Phase 5L dataset reaudit failed."
        )

    print()
    print(
        "PHASE 5L HIGHER-ZERO DATASET: HASH FROZEN"
    )

    print(
        "P-EXT-001 REAUDIT: PASS"
    )

    print(
        "P-EXT-002 THROUGH P-EXT-007: NOT SCORED"
    )


if __name__ == "__main__":
    main()
