"""Targeted search for equal-weight three-orbit blind-scale moment relations."""

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

from src.li_susceptibility import (
    li_blind_scale,
)


RESULT_DIR = Path(
    "results/li_three_orbit_equal_weight_search"
)

CANDIDATE_CSV = (
    RESULT_DIR / "best_candidates.csv"
)

CHECKPOINT_CSV = (
    RESULT_DIR / "range_checkpoints.csv"
)

METADATA_PATH = (
    RESULT_DIR / "metadata.json"
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


def main() -> None:
    started = time.perf_counter()

    mp.mp.dps = 100

    RESULT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    max_index = 2999

    checkpoint_limits = [
        99,
        249,
        499,
        999,
        1999,
        2999,
    ]

    commit_at_start = git_output(
        "rev-parse",
        "HEAD",
    )

    clean_at_start = (
        git_output("status", "--porcelain")
        == ""
    )

    prediction_path = Path(
        "conjectures/"
        "THREE_ORBIT_EQUAL_WEIGHT_PREDICTIONS.md"
    )

    prediction_sha256 = sha256_file(
        prediction_path
    )

    print(
        "LI THREE-ORBIT EQUAL-WEIGHT SEARCH"
    )

    print("=" * 110)

    print(
        f"Maximum blind-scale index: "
        f"{max_index}"
    )

    print(
        "Precomputing blind scales..."
    )

    roots = [
        li_blind_scale(k)
        for k in range(max_index + 1)
    ]

    print(
        f"Cached {len(roots)} blind scales."
    )

    print(
        "Precomputing blind-scale moments..."
    )

    moments = [
        root**6
        * mp.sqrt(root**2 + 4)
        for root in roots
    ]

    print(
        f"Cached {len(moments)} moments."
    )

    even_indices = list(
        range(0, max_index + 1, 2)
    )

    odd_indices = list(
        range(1, max_index + 1, 2)
    )

    even_moments = [
        moments[k]
        for k in even_indices
    ]

    odd_moments = [
        moments[k]
        for k in odd_indices
    ]

    best_candidates: list[
        dict[str, str | int]
    ] = []

    best_global = None
    best_local = None

    best_global_record = None
    best_local_record = None

    pair_count = 0

    checkpoint_records: list[
        dict[str, str | int]
    ] = []

    checkpoint_state = {
        limit: {
            "best_global": None,
            "best_local": None,
            "best_global_record": None,
            "best_local_record": None,
            "pair_count": 0,
        }
        for limit in checkpoint_limits
    }

    def register_candidate(
        p: int,
        q: int,
        r: int,
        target: mp.mpf,
        lower_moment: mp.mpf,
        upper_moment: mp.mpf,
    ) -> None:
        nonlocal best_global
        nonlocal best_local
        nonlocal best_global_record
        nonlocal best_local_record

        residual = abs(
            moments[r] - target
        )

        global_defect = (
            residual
            /
            (
                moments[r]
                + target
            )
        )

        local_gap = (
            upper_moment
            - lower_moment
        )

        local_defect = (
            residual / local_gap
        )

        record = {
            "p": p,
            "q": q,
            "r": r,
            "p_parity": p % 2,
            "r_parity": r % 2,
            "A_p": mp.nstr(
                moments[p],
                70,
            ),
            "A_q": mp.nstr(
                moments[q],
                70,
            ),
            "A_r": mp.nstr(
                moments[r],
                70,
            ),
            "raw_residual": mp.nstr(
                residual,
                70,
            ),
            "global_normalized_defect": mp.nstr(
                global_defect,
                70,
            ),
            "parity_local_gap": mp.nstr(
                local_gap,
                70,
            ),
            "parity_local_defect": mp.nstr(
                local_defect,
                70,
            ),
        }

        if (
            best_global is None
            or global_defect < best_global
        ):
            best_global = global_defect
            best_global_record = record

        if (
            best_local is None
            or local_defect < best_local
        ):
            best_local = local_defect
            best_local_record = record

        best_candidates.append(record)

        for limit in checkpoint_limits:
            if r <= limit:
                state = checkpoint_state[limit]

                state["pair_count"] = (
                    int(state["pair_count"])
                    + 1
                )

                current_global = (
                    state["best_global"]
                )

                current_local = (
                    state["best_local"]
                )

                if (
                    current_global is None
                    or global_defect
                    <
                    current_global
                ):
                    state["best_global"] = (
                        global_defect
                    )

                    state[
                        "best_global_record"
                    ] = record

                if (
                    current_local is None
                    or local_defect
                    <
                    current_local
                ):
                    state["best_local"] = (
                        local_defect
                    )

                    state[
                        "best_local_record"
                    ] = record

    print(
        "Searching same-parity pair sums..."
    )

    for parity in [0, 1]:
        if parity == 0:
            source_indices = even_indices
            target_indices = odd_indices
            target_moments = odd_moments
        else:
            source_indices = odd_indices
            target_indices = even_indices
            target_moments = even_moments

        source_count = len(
            source_indices
        )

        for source_position, p in enumerate(
            source_indices
        ):
            for q in source_indices[
                source_position:
            ]:
                target = (
                    moments[p]
                    + moments[q]
                )

                insertion = bisect.bisect_left(
                    target_moments,
                    target,
                )

                if (
                    insertion == 0
                    or insertion
                    >= len(target_moments)
                ):
                    continue

                lower_position = insertion - 1
                upper_position = insertion

                lower_index = target_indices[
                    lower_position
                ]

                upper_index = target_indices[
                    upper_position
                ]

                # Necessary ordering from Phase 4E:
                # r > max(p, q) = q.
                candidate_indices = []

                if lower_index > q:
                    candidate_indices.append(
                        lower_index
                    )

                if upper_index > q:
                    candidate_indices.append(
                        upper_index
                    )

                if not candidate_indices:
                    continue

                pair_count += 1

                lower_moment = target_moments[
                    lower_position
                ]

                upper_moment = target_moments[
                    upper_position
                ]

                for r in candidate_indices:
                    register_candidate(
                        p=p,
                        q=q,
                        r=r,
                        target=target,
                        lower_moment=lower_moment,
                        upper_moment=upper_moment,
                    )

            if (
                source_position % 250 == 0
                or source_position
                == source_count - 1
            ):
                print(
                    f"parity={parity} "
                    f"source position="
                    f"{source_position:4d}/"
                    f"{source_count - 1}"
                )

    if best_global_record is None:
        raise AssertionError(
            "No best-global candidate recorded"
        )

    if best_local_record is None:
        raise AssertionError(
            "No best-local candidate recorded"
        )

    best_candidates.sort(
        key=lambda row: mp.mpf(
            str(
                row[
                    "parity_local_defect"
                ]
            )
        )
    )

    top_candidates = (
        best_candidates[:200]
    )

    with CANDIDATE_CSV.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                top_candidates[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            top_candidates
        )

    for limit in checkpoint_limits:
        state = checkpoint_state[limit]

        if (
            state["best_global"] is None
            or state["best_local"] is None
        ):
            continue

        global_record = state[
            "best_global_record"
        ]

        local_record = state[
            "best_local_record"
        ]

        checkpoint_records.append(
            {
                "max_index": limit,
                "candidate_records_seen": int(
                    state["pair_count"]
                ),
                "best_global_defect": mp.nstr(
                    state["best_global"],
                    70,
                ),
                "best_global_p": int(
                    global_record["p"]
                ),
                "best_global_q": int(
                    global_record["q"]
                ),
                "best_global_r": int(
                    global_record["r"]
                ),
                "best_local_defect": mp.nstr(
                    state["best_local"],
                    70,
                ),
                "best_local_p": int(
                    local_record["p"]
                ),
                "best_local_q": int(
                    local_record["q"]
                ),
                "best_local_r": int(
                    local_record["r"]
                ),
            }
        )

    with CHECKPOINT_CSV.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(
                checkpoint_records[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(
            checkpoint_records
        )

    print()
    print(
        f"Admissible pair locations searched: "
        f"{pair_count}"
    )

    print(
        "\nBEST GLOBAL NORMALIZED DEFECT"
    )

    print(
        best_global_record
    )

    print(
        "\nBEST PARITY-LOCAL DEFECT"
    )

    print(
        best_local_record
    )

    print(
        "\nTen strongest parity-local candidates:"
    )

    for row in top_candidates[:10]:
        print(
            f"p={int(row['p']):<5d} "
            f"q={int(row['q']):<5d} "
            f"r={int(row['r']):<5d} "
            f"D={mp.nstr(mp.mpf(str(row['global_normalized_defect'])), 10):>14s} "
            f"E={mp.nstr(mp.mpf(str(row['parity_local_defect'])), 10):>14s}"
        )

    print(
        "\nRANGE CHECKPOINTS"
    )

    for row in checkpoint_records:
        print(
            f"N={int(row['max_index']):<5d} "
            f"best D={mp.nstr(mp.mpf(str(row['best_global_defect'])), 10):>14s} "
            f"best E={mp.nstr(mp.mpf(str(row['best_local_defect'])), 10):>14s}"
        )

    runtime_seconds = (
        time.perf_counter() - started
    )

    metadata = {
        "experiment_name": (
            "li_three_orbit_equal_weight_search"
        ),
        "precision_decimal_digits": (
            mp.mp.dps
        ),
        "max_blind_scale_index": (
            max_index
        ),
        "admissible_pair_locations_searched": (
            pair_count
        ),
        "prediction_file": str(
            prediction_path
        ),
        "prediction_file_sha256": (
            prediction_sha256
        ),
        "git_commit_at_start": (
            commit_at_start
        ),
        "git_clean_at_start": (
            clean_at_start
        ),
        "python_version": sys.version,
        "platform": platform.platform(),
        "runtime_seconds": runtime_seconds,
        "candidate_csv": str(
            CANDIDATE_CSV
        ),
        "checkpoint_csv": str(
            CHECKPOINT_CSV
        ),
    }

    metadata["candidate_csv_sha256"] = (
        sha256_file(CANDIDATE_CSV)
    )

    metadata["checkpoint_csv_sha256"] = (
        sha256_file(CHECKPOINT_CSV)
    )

    METADATA_PATH.write_text(
        json.dumps(
            metadata,
            indent=2,
        ),
        encoding="utf-8",
    )

    print()
    print("SEARCH COMPLETE")

    print(
        f"Runtime seconds: "
        f"{runtime_seconds:.3f}"
    )

    print(
        f"Candidates: {CANDIDATE_CSV}"
    )

    print(
        f"Checkpoints: {CHECKPOINT_CSV}"
    )

    print(
        f"Metadata: {METADATA_PATH}"
    )


if __name__ == "__main__":
    main()
