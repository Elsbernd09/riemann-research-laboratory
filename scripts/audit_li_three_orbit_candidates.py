"""High-precision audit of top equal-weight three-orbit candidates."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import mpmath as mp

from src.li_susceptibility import (
    li_blind_scale,
)


RESULT_DIR = Path(
    "results/li_three_orbit_equal_weight_search"
)

INPUT_CSV = RESULT_DIR / "best_candidates.csv"
CHECKPOINT_CSV = RESULT_DIR / "range_checkpoints.csv"

AUDIT_CSV = RESULT_DIR / "high_precision_candidate_audit.csv"
AUDIT_JSON = RESULT_DIR / "high_precision_audit_summary.json"


def load_top_candidates(
    limit: int = 15,
) -> list[dict[str, str]]:
    with INPUT_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        rows = list(
            csv.DictReader(handle)
        )

    return rows[:limit]


def compute_root(
    k: int,
) -> mp.mpf:
    # 2200 bisection iterations comfortably exceed the
    # approximately 1661 binary digits required for 500 decimals.
    return li_blind_scale(
        k,
        iterations=2200,
    )


def moment(
    c: mp.mpf,
) -> mp.mpf:
    return (
        c**6
        * mp.sqrt(c**2 + 4)
    )


def main() -> None:
    mp.mp.dps = 500

    candidates = load_top_candidates(
        limit=15,
    )

    indices = sorted(
        {
            int(row[key])
            for row in candidates
            for key in ("p", "q", "r")
        }
    )

    # We also need parity neighbors around each r.
    neighbor_indices = set(indices)

    for row in candidates:
        r = int(row["r"])

        if r >= 2:
            neighbor_indices.add(r - 2)

        neighbor_indices.add(r + 2)

    neighbor_indices = sorted(
        neighbor_indices
    )

    print("THREE-ORBIT 500-DIGIT AUDIT")
    print("=" * 110)

    print(
        f"Unique blind scales required: "
        f"{len(neighbor_indices)}"
    )

    roots: dict[int, mp.mpf] = {}
    moments: dict[int, mp.mpf] = {}

    for position, k in enumerate(
        neighbor_indices,
        start=1,
    ):
        roots[k] = compute_root(k)
        moments[k] = moment(roots[k])

        print(
            f"Computed k={k:<5d} "
            f"({position}/{len(neighbor_indices)})"
        )

    audit_rows: list[dict[str, str | int]] = []

    for rank, row in enumerate(
        candidates,
        start=1,
    ):
        p = int(row["p"])
        q = int(row["q"])
        r = int(row["r"])

        A_p = moments[p]
        A_q = moments[q]
        A_r = moments[r]

        target = A_p + A_q

        signed_residual = (
            A_r - target
        )

        residual = abs(
            signed_residual
        )

        D = (
            residual
            /
            (
                A_r
                + target
            )
        )

        lower_r = r - 2
        upper_r = r + 2

        if lower_r < 0:
            raise AssertionError(
                "Unexpected missing lower parity neighbor"
            )

        lower = moments[lower_r]
        upper = moments[upper_r]

        # Confirm the candidate target really lies in the local
        # parity neighborhood associated with r.
        if not (
            lower < target < upper
        ):
            raise AssertionError(
                "High-precision target left expected "
                f"parity neighborhood for rank {rank}"
            )

        parity_gap = upper - lower

        E = (
            residual
            /
            parity_gap
        )

        search_D = mp.mpf(
            row["global_normalized_defect"]
        )

        search_E = mp.mpf(
            row["parity_local_defect"]
        )

        D_relative_change = (
            abs(D - search_D)
            /
            max(
                abs(D),
                abs(search_D),
                mp.mpf("1e-490"),
            )
        )

        E_relative_change = (
            abs(E - search_E)
            /
            max(
                abs(E),
                abs(search_E),
                mp.mpf("1e-490"),
            )
        )

        audit_rows.append(
            {
                "rank": rank,
                "p": p,
                "q": q,
                "r": r,
                "signed_residual_500dps": mp.nstr(
                    signed_residual,
                    300,
                ),
                "absolute_residual_500dps": mp.nstr(
                    residual,
                    300,
                ),
                "global_defect_500dps": mp.nstr(
                    D,
                    300,
                ),
                "parity_local_defect_500dps": mp.nstr(
                    E,
                    300,
                ),
                "search_global_defect": row[
                    "global_normalized_defect"
                ],
                "search_parity_local_defect": row[
                    "parity_local_defect"
                ],
                "global_defect_relative_change": mp.nstr(
                    D_relative_change,
                    100,
                ),
                "local_defect_relative_change": mp.nstr(
                    E_relative_change,
                    100,
                ),
            }
        )

        print()
        print(
            f"Rank {rank}: "
            f"(p,q,r)=({p},{q},{r})"
        )

        print(
            "signed residual = "
            f"{mp.nstr(signed_residual, 40)}"
        )

        print(
            "D = "
            f"{mp.nstr(D, 30)}"
        )

        print(
            "E = "
            f"{mp.nstr(E, 30)}"
        )

        print(
            "D relative change from search = "
            f"{mp.nstr(D_relative_change, 8)}"
        )

        print(
            "E relative change from search = "
            f"{mp.nstr(E_relative_change, 8)}"
        )

        if residual == 0:
            raise AssertionError(
                "Numerical exact equality occurred at 500 dps. "
                "This requires a separate exact-mathematics audit."
            )

    with AUDIT_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                audit_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(audit_rows)

    # Read full-search checkpoint count and best E.
    with CHECKPOINT_CSV.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        checkpoints = list(
            csv.DictReader(handle)
        )

    full_checkpoint = checkpoints[-1]

    M = int(
        full_checkpoint[
            "candidate_records_seen"
        ]
    )

    observed_E = mp.mpf(
        full_checkpoint[
            "best_local_defect"
        ]
    )

    # Crude iid null:
    # E ~ Uniform(0, 1/2), so P(E <= e) = 2e.
    #
    # For M independent samples:
    # P(min E <= e) = 1 - (1 - 2e)^M.
    expected_min = (
        mp.mpf(1)
        /
        (
            2
            * (M + 1)
        )
    )

    null_tail_probability = (
        1
        -
        mp.power(
            1 - 2 * observed_E,
            M,
        )
    )

    min_ratio_to_expected = (
        observed_E
        /
        expected_min
    )

    summary = {
        "precision_decimal_digits": mp.mp.dps,
        "candidate_count_audited": len(
            audit_rows
        ),
        "full_checkpoint_candidate_records_seen": M,
        "observed_best_parity_local_defect": mp.nstr(
            observed_E,
            200,
        ),
        "iid_uniform_half_interval_expected_minimum": mp.nstr(
            expected_min,
            200,
        ),
        "observed_minimum_over_expected_minimum": mp.nstr(
            min_ratio_to_expected,
            100,
        ),
        "iid_uniform_half_interval_probability_min_le_observed": mp.nstr(
            null_tail_probability,
            100,
        ),
        "null_model_warning": (
            "The iid Uniform(0,1/2) benchmark is heuristic. "
            "Candidate defects are dependent and need not be "
            "uniformly distributed."
        ),
    }

    AUDIT_JSON.write_text(
        json.dumps(
            summary,
            indent=2,
        ),
        encoding="utf-8",
    )

    print()
    print("=" * 110)
    print("EXTREME-VALUE BENCHMARK")
    print("=" * 110)

    print(
        f"Candidate records M = {M}"
    )

    print(
        "Observed best E = "
        f"{mp.nstr(observed_E, 30)}"
    )

    print(
        "Crude iid-null expected minimum = "
        f"{mp.nstr(expected_min, 30)}"
    )

    print(
        "Observed / expected minimum = "
        f"{mp.nstr(min_ratio_to_expected, 20)}"
    )

    print(
        "Crude null P(min <= observed E) = "
        f"{mp.nstr(null_tail_probability, 20)}"
    )

    print()
    print(
        "WARNING: this probability is heuristic because "
        "candidate defects are dependent and not proven uniform."
    )

    print()
    print("500-DIGIT CANDIDATE AUDIT: PASS")

    print(
        f"Audit CSV: {AUDIT_CSV}"
    )

    print(
        f"Audit summary: {AUDIT_JSON}"
    )


if __name__ == "__main__":
    main()
