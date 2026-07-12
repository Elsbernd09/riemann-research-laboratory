from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List
import json
import math

from src.level4.toy_basis import TriangularLogBump
from src.level4.toy_arithmetic_entry import compute_toy_entry
from src.level4.interval_matrix import Interval, IntervalMatrix
from src.level4.admissible_subspace import (
    build_three_function_basis,
    constraint_matrix_for_basis,
    nullspace_2xm,
    restrict_matrix,
)


def assemble_three_basis_toy_matrix(integral_steps: int = 60, conv_steps: int = 60) -> List[List[float]]:
    basis = build_three_function_basis()
    n = len(basis)
    M: List[List[float]] = []
    for i in range(n):
        row: List[float] = []
        for j in range(n):
            comps = compute_toy_entry(
                basis[j],
                basis[i],
                B=1.2,
                integral_steps=integral_steps,
                conv_steps=conv_steps,
            )
            row.append(comps.entry_value)
        M.append(row)
    return M


def symmetrize(M: List[List[float]]) -> List[List[float]]:
    n = len(M)
    return [[0.5 * (M[i][j] + M[j][i]) for j in range(n)] for i in range(n)]


def interval_wrap_square(M: List[List[float]], radius: float = 1.0) -> IntervalMatrix:
    return IntervalMatrix([[Interval(x - radius, x + radius) for x in row] for row in M])


def scan_restricted_rayleigh(Madm: List[List[float]]) -> Dict[str, Any]:
    if not Madm:
        return {
            "restricted_dimension": 0,
            "message": "No admissible nullspace dimension",
            "results": [],
        }

    imat = interval_wrap_square(Madm, radius=1.0)
    vectors: List[List[float]] = []
    n = len(Madm)
    for i in range(n):
        v = [0.0] * n
        v[i] = 1.0
        vectors.append(v)
    if n == 1:
        vectors.append([2.0])
    if n == 2:
        vectors.extend([[1.0, 1.0], [1.0, -1.0]])

    results = [imat.negative_direction_certificate(v) for v in vectors]
    return {
        "restricted_dimension": n,
        "interval_matrix": imat.to_dict(),
        "results": results,
        "any_certified_negative_direction": any(r["verdict"] == "CERTIFIED_NEGATIVE_DIRECTION" for r in results),
    }


def write_admissible_toy_matrix_certificate(output_path: Path) -> None:
    basis = build_three_function_basis()
    C = constraint_matrix_for_basis(basis)
    N = nullspace_2xm(C)

    raw = assemble_three_basis_toy_matrix()
    sym = symmetrize(raw)
    Madm = restrict_matrix(sym, N)
    rayleigh = scan_restricted_rayleigh(Madm)

    payload: Dict[str, Any] = {
        "phase": "B3",
        "status": "PHASE_B3_ADMISSIBLE_TOY_MATRIX_COMPLETE",
        "important_boundary": "TOY_FLOATING_POINT_PIPELINE_ONLY",
        "constraint_matrix_C": C,
        "nullspace_basis_N": N,
        "raw_toy_matrix": raw,
        "symmetrized_toy_matrix": sym,
        "admissible_restricted_matrix": Madm,
        "rayleigh_scan": rayleigh,
        "audit_strings": [
            "PHASE_B3_ADMISSIBLE_TOY_MATRIX_COMPLETE",
            "TOY_ARITHMETIC_MATRIX_ASSEMBLED_FOR_ADMISSIBLE_TEST",
            "POLE_CONSTRAINT_MATRIX_USED",
            "ADMISSIBLE_NULLSPACE_USED",
            "TOY_ADMISSIBLE_MATRIX_COMPUTED",
            "TOY_ADMISSIBLE_RAYLEIGH_LOGIC_TESTED",
            "POLE_ORTHOGONAL_PIPELINE_IMPLEMENTED",
            "BREAKTHROUGH_NOT_ACHIEVED",
            "READY_FOR_PHASE_B4_PRIOR_ART_COLLISION",
        ],
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    out = Path("breakthrough_push/phase_b3_admissible_toy_matrix/admissible_toy_matrix_certificate.json")
    write_admissible_toy_matrix_certificate(out)
    print(f"Wrote {out}")
