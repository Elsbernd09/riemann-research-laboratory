from __future__ import annotations

import csv
import json
import math
import platform
import statistics
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import mpmath as mp


INPUT_CSV = Path(
    "results/li_zeta_window_signed_transfer/"
    "signed_transfer_points.csv"
)

RESULT_DIR = Path(
    "results/li_zeta_window_sign_chambers"
)

POINT_CSV = RESULT_DIR / "sign_chamber_points.csv"
CHAMBER_CSV = RESULT_DIR / "chamber_summary.csv"
SUMMARY_JSON = RESULT_DIR / "summary.json"

ZERO_TOLERANCE = mp.mpf("1e-50")

CHAMBERS = (
    "(+,+,+)",
    "(+,+,-)",
    "(+,-,+)",
    "(+,-,-)",
    "(-,+,+)",
    "(-,+,-)",
    "(-,-,+)",
    "(-,-,-)",
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


def sign_symbol(
    value: mp.mpf,
) -> str:
    if abs(value) <= ZERO_TOLERANCE:
        return "0"

    if value > 0:
        return "+"

    return "-"


def chamber_label(
    atom: mp.mpf,
    endpoint: mp.mpf,
    interior: mp.mpf,
) -> str:
    symbols = (
        sign_symbol(atom),
        sign_symbol(endpoint),
        sign_symbol(interior),
    )

    if "0" in symbols:
        return "BOUNDARY"

    return (
        f"({symbols[0]},"
        f"{symbols[1]},"
        f"{symbols[2]})"
    )


def main() -> None:
    started = time.perf_counter()

    mp.mp.dps = 60

    if not INPUT_CSV.exists():
        raise FileNotFoundError(
            f"Missing frozen Phase 5H input: "
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
            "Frozen Phase 5H population mismatch: "
            f"expected 360 rows, got {len(rows)}"
        )

    classified_rows: list[
        dict[str, str | int]
    ] = []

    chamber_members: dict[
        str,
        list[dict[str, object]],
    ] = defaultdict(list)

    print(
        "PHASE 5I — SIGN-CHAMBER GEOMETRY"
    )
    print("=" * 104)

    for row in rows:
        atom = mp_value(
            row["atom_component"]
        )

        endpoint = mp_value(
            row["endpoint_component"]
        )

        interior = mp_value(
            row["interior_component"]
        )

        C_scalar = mp_value(
            row[
                "scalar_cancellation_coefficient"
            ]
        )

        T_sup = mp_value(
            row["sup_certificate_tightness"]
        )

        chamber = chamber_label(
            atom,
            endpoint,
            interior,
        )

        classified = {
            **row,
            "sign_chamber": chamber,
            "is_boundary": int(
                chamber == "BOUNDARY"
            ),
            "is_mixed_sign": int(
                chamber
                not in (
                    "(+,+,+)",
                    "(-,-,-)",
                    "BOUNDARY",
                )
            ),
            "is_same_sign": int(
                chamber
                in (
                    "(+,+,+)",
                    "(-,-,-)",
                )
            ),
            "is_extreme_cancellation": int(
                C_scalar
                <
                mp.mpf("0.25")
            ),
        }

        classified_rows.append(
            classified
        )

        chamber_members[
            chamber
        ].append(
            {
                "row": classified,
                "C_scalar": C_scalar,
                "T_sup": T_sup,
            }
        )

    boundary_count = sum(
        int(
            row["is_boundary"]
        )
        for row in classified_rows
    )

    chamber_counts = Counter(
        str(row["sign_chamber"])
        for row in classified_rows
    )

    same_sign_rows = [
        row
        for row in classified_rows
        if int(
            row["is_same_sign"]
        )
        == 1
    ]

    same_sign_deviations = [
        abs(
            mp_value(
                row[
                    "scalar_cancellation_coefficient"
                ]
            )
            -
            1
        )
        for row in same_sign_rows
    ]

    maximum_same_sign_deviation = (
        max(same_sign_deviations)
        if same_sign_deviations
        else mp.nan
    )

    extreme_rows = [
        row
        for row in classified_rows
        if int(
            row[
                "is_extreme_cancellation"
            ]
        )
        == 1
    ]

    extreme_mixed_count = sum(
        int(
            row["is_mixed_sign"]
        )
        for row in extreme_rows
    )

    mixed_share_of_extreme = (
        mp.mpf(extreme_mixed_count)
        /
        len(extreme_rows)
        if extreme_rows
        else mp.nan
    )

    mixed_chamber_rates: dict[
        str,
        mp.mpf,
    ] = {}

    eligible_mixed_rates: list[
        mp.mpf
    ] = []

    for chamber in CHAMBERS:
        members = chamber_members.get(
            chamber,
            [],
        )

        if chamber in (
            "(+,+,+)",
            "(-,-,-)",
        ):
            continue

        if not members:
            continue

        rate = (
            mp.fsum(
                mp.mpf(
                    int(
                        member["row"][
                            "is_extreme_cancellation"
                        ]
                    )
                )
                for member in members
            )
            /
            len(members)
        )

        mixed_chamber_rates[
            chamber
        ] = rate

        if len(members) >= 10:
            eligible_mixed_rates.append(
                rate
            )

    if len(eligible_mixed_rates) >= 2:
        eligible_rate_range = (
            max(eligible_mixed_rates)
            -
            min(eligible_mixed_rates)
        )
    else:
        eligible_rate_range = mp.nan

    T_sup_values = sorted(
        mp_value(
            row[
                "sup_certificate_tightness"
            ]
        )
        for row in classified_rows
    )

    # Frozen bottom quartile: 90 smallest values
    # from the 360-point Phase 5H population.
    bottom_quartile_count = (
        len(T_sup_values) // 4
    )

    if bottom_quartile_count != 90:
        raise RuntimeError(
            "Unexpected bottom-quartile size: "
            f"{bottom_quartile_count}"
        )

    bottom_threshold = (
        T_sup_values[
            bottom_quartile_count - 1
        ]
    )

    ranked_rows = sorted(
        classified_rows,
        key=lambda row: mp_value(
            row[
                "sup_certificate_tightness"
            ]
        ),
    )

    bottom_rows = ranked_rows[
        :bottom_quartile_count
    ]

    global_frequency: dict[
        str,
        mp.mpf,
    ] = {}

    bottom_frequency: dict[
        str,
        mp.mpf,
    ] = {}

    chamber_enrichment: dict[
        str,
        mp.mpf,
    ] = {}

    for chamber in (
        *CHAMBERS,
        "BOUNDARY",
    ):
        global_count = chamber_counts.get(
            chamber,
            0,
        )

        bottom_count = sum(
            str(
                row["sign_chamber"]
            )
            == chamber
            for row in bottom_rows
        )

        p_j = (
            mp.mpf(global_count)
            /
            len(classified_rows)
        )

        q_j = (
            mp.mpf(bottom_count)
            /
            len(bottom_rows)
        )

        global_frequency[
            chamber
        ] = p_j

        bottom_frequency[
            chamber
        ] = q_j

        if p_j > 0:
            chamber_enrichment[
                chamber
            ] = q_j / p_j
        else:
            chamber_enrichment[
                chamber
            ] = mp.nan

    finite_enrichments = [
        value
        for value in chamber_enrichment.values()
        if mp.isfinite(value)
    ]

    maximum_enrichment = max(
        finite_enrichments
    )

    # Group and order the frozen c-grid.
    rows_by_window: dict[
        int,
        list[dict[str, str | int]],
    ] = defaultdict(list)

    for row in classified_rows:
        rows_by_window[
            int(row["window_number"])
        ].append(row)

    transitions_per_window: list[int] = []

    transition_edges_by_window: dict[
        int,
        list[int],
    ] = {}

    for window_number, window_rows in (
        sorted(
            rows_by_window.items()
        )
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
                f"{len(ordered)} points, expected 20."
            )

        transition_edges: list[int] = []

        for index in range(
            len(ordered) - 1
        ):
            left_chamber = str(
                ordered[index][
                    "sign_chamber"
                ]
            )

            right_chamber = str(
                ordered[index + 1][
                    "sign_chamber"
                ]
            )

            if (
                left_chamber
                !=
                right_chamber
            ):
                # Edge index represents transition
                # between c=index+1 and c=index+2.
                transition_edges.append(
                    index
                )

        transition_edges_by_window[
            window_number
        ] = transition_edges

        transitions_per_window.append(
            len(transition_edges)
        )

    # Transition distance:
    #
    # Each edge at index e touches point positions
    # e and e+1. Distance is minimum integer grid
    # distance to either endpoint of any transition.
    for row in classified_rows:
        window_number = int(
            row["window_number"]
        )

        c_position = (
            int(
                mp.mpf(
                    str(row["requested_c"])
                )
            )
            -
            1
        )

        transition_edges = (
            transition_edges_by_window[
                window_number
            ]
        )

        if not transition_edges:
            transition_distance = 999
        else:
            transition_distance = min(
                min(
                    abs(
                        c_position - edge
                    ),
                    abs(
                        c_position - (edge + 1)
                    ),
                )
                for edge in transition_edges
            )

        row[
            "transition_distance"
        ] = transition_distance

        row[
            "is_near_transition"
        ] = int(
            transition_distance <= 1
        )

        row[
            "is_far_transition"
        ] = int(
            transition_distance >= 3
        )

    near_rows = [
        row
        for row in classified_rows
        if int(
            row["is_near_transition"]
        )
        == 1
    ]

    far_rows = [
        row
        for row in classified_rows
        if int(
            row["is_far_transition"]
        )
        == 1
    ]

    near_C_values = [
        mp_value(
            row[
                "scalar_cancellation_coefficient"
            ]
        )
        for row in near_rows
    ]

    far_C_values = [
        mp_value(
            row[
                "scalar_cancellation_coefficient"
            ]
        )
        for row in far_rows
    ]

    median_near_C = median_mpf(
        near_C_values
    )

    median_far_C = median_mpf(
        far_C_values
    )

    p_chm_001 = (
        len(classified_rows) == 360
        and boundary_count == 0
        and sum(
            chamber_counts.get(
                chamber,
                0,
            )
            for chamber in CHAMBERS
        )
        == 360
    )

    p_chm_002 = (
        bool(
            same_sign_rows
        )
        and maximum_same_sign_deviation
        <
        mp.mpf("1e-45")
    )

    p_chm_003 = (
        mp.isfinite(
            mixed_share_of_extreme
        )
        and mixed_share_of_extreme
        >=
        mp.mpf("0.95")
    )

    p_chm_004 = (
        mp.isfinite(
            eligible_rate_range
        )
        and eligible_rate_range
        >
        mp.mpf("0.25")
    )

    p_chm_005 = (
        maximum_enrichment
        >
        mp.mpf("1.5")
    )

    mean_transitions = mean_mpf(
        [
            mp.mpf(value)
            for value in transitions_per_window
        ]
    )

    median_transitions = median_mpf(
        [
            mp.mpf(value)
            for value in transitions_per_window
        ]
    )

    p_chm_006 = (
        mean_transitions > 5
    )

    p_chm_007 = (
        bool(near_rows)
        and bool(far_rows)
        and median_near_C
        <
        median_far_C
    )

    chamber_summary_rows: list[
        dict[str, str | int]
    ] = []

    for chamber in (
        *CHAMBERS,
        "BOUNDARY",
    ):
        members = chamber_members.get(
            chamber,
            [],
        )

        count = len(members)

        C_values = [
            mp.mpf(
                str(
                    member[
                        "C_scalar"
                    ]
                )
            )
            for member in members
        ]

        extreme_rate = (
            fraction_true(
                [
                    value
                    <
                    mp.mpf("0.25")
                    for value in C_values
                ]
            )
            if C_values
            else mp.nan
        )

        bottom_count = sum(
            str(
                row[
                    "sign_chamber"
                ]
            )
            == chamber
            for row in bottom_rows
        )

        chamber_summary_rows.append(
            {
                "sign_chamber": chamber,
                "point_count": count,
                "global_frequency": mp.nstr(
                    global_frequency[
                        chamber
                    ],
                    60,
                ),
                "median_C_scalar": mp.nstr(
                    median_mpf(
                        C_values
                    ),
                    60,
                ),
                "extreme_cancellation_rate": mp.nstr(
                    extreme_rate,
                    60,
                ),
                "bottom_quartile_count": (
                    bottom_count
                ),
                "bottom_quartile_frequency": mp.nstr(
                    bottom_frequency[
                        chamber
                    ],
                    60,
                ),
                "bottom_quartile_enrichment": mp.nstr(
                    chamber_enrichment[
                        chamber
                    ],
                    60,
                ),
            }
        )

    with POINT_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                classified_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            classified_rows
        )

    with CHAMBER_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                chamber_summary_rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            chamber_summary_rows
        )

    runtime_seconds = (
        time.perf_counter()
        -
        started
    )

    summary = {
        "experiment_name": (
            "li_zeta_window_sign_chambers"
        ),
        "point_count": len(
            classified_rows
        ),
        "boundary_tolerance": mp.nstr(
            ZERO_TOLERANCE,
            20,
        ),
        "boundary_point_count": (
            boundary_count
        ),
        "chamber_counts": {
            chamber: chamber_counts.get(
                chamber,
                0,
            )
            for chamber in CHAMBERS
        },
        "chamber_frequencies": {
            chamber: mp.nstr(
                global_frequency[
                    chamber
                ],
                50,
            )
            for chamber in CHAMBERS
        },
        "same_sign_validation_point_count": len(
            same_sign_rows
        ),
        "maximum_same_sign_deviation_from_one": mp.nstr(
            maximum_same_sign_deviation,
            50,
        ),
        "extreme_cancellation_point_count": len(
            extreme_rows
        ),
        "mixed_sign_share_of_extreme_cancellation": mp.nstr(
            mixed_share_of_extreme,
            50,
        ),
        "mixed_chamber_extreme_cancellation_rates": {
            chamber: mp.nstr(
                rate,
                50,
            )
            for chamber, rate in sorted(
                mixed_chamber_rates.items()
            )
        },
        "eligible_mixed_chamber_rate_range": mp.nstr(
            eligible_rate_range,
            50,
        ),
        "bottom_quartile_point_count": (
            bottom_quartile_count
        ),
        "bottom_quartile_Tsup_threshold": mp.nstr(
            bottom_threshold,
            50,
        ),
        "chamber_bottom_quartile_enrichment": {
            chamber: mp.nstr(
                chamber_enrichment[
                    chamber
                ],
                50,
            )
            for chamber in CHAMBERS
        },
        "maximum_chamber_enrichment": mp.nstr(
            maximum_enrichment,
            50,
        ),
        "transitions_per_window": (
            transitions_per_window
        ),
        "mean_transitions_per_window": mp.nstr(
            mean_transitions,
            50,
        ),
        "median_transitions_per_window": mp.nstr(
            median_transitions,
            50,
        ),
        "near_transition_point_count": len(
            near_rows
        ),
        "far_transition_point_count": len(
            far_rows
        ),
        "median_near_transition_C_scalar": mp.nstr(
            median_near_C,
            50,
        ),
        "median_far_transition_C_scalar": mp.nstr(
            median_far_C,
            50,
        ),
        "P_CHM_001": (
            "PASS"
            if p_chm_001
            else "FAIL"
        ),
        "P_CHM_002": (
            "PASS"
            if p_chm_002
            else "FAIL"
        ),
        "P_CHM_003": (
            "PASS"
            if p_chm_003
            else "FAIL"
        ),
        "P_CHM_004": (
            "PASS"
            if p_chm_004
            else "FAIL"
        ),
        "P_CHM_005": (
            "PASS"
            if p_chm_005
            else "FAIL"
        ),
        "P_CHM_006": (
            "PASS"
            if p_chm_006
            else "FAIL"
        ),
        "P_CHM_007": (
            "PASS"
            if p_chm_007
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
            "In-sample descriptive sign-chamber "
            "geometry on the frozen 360-point Phase "
            "5H dataset. Chamber labels are derived "
            "from the response components themselves. "
            "Same-sign and mixed-sign consequences "
            "are partly algebraic or definition-driven. "
            "No causal, asymptotic, predictive, or RH "
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
    print("=" * 104)
    print("CHAMBER COUNTS")
    print("=" * 104)

    for chamber in CHAMBERS:
        print(
            f"{chamber}: "
            f"{chamber_counts.get(chamber, 0)}"
        )

    print()
    print("=" * 104)
    print("PHASE 5I SUMMARY")
    print("=" * 104)

    for key, value in summary.items():
        print(
            f"{key}: {value}"
        )

    print()
    print(
        f"Point CSV: {POINT_CSV}"
    )

    print(
        f"Chamber CSV: {CHAMBER_CSV}"
    )

    print(
        f"Summary JSON: {SUMMARY_JSON}"
    )

    print()
    print(
        "PHASE 5I SIGN-CHAMBER GEOMETRY: "
        "COMPLETE"
    )


if __name__ == "__main__":
    main()
