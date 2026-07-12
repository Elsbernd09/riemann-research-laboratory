from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Sequence
import json
import math

from src.level4.interval_matrix import Interval, IntervalMatrix
from src.level4.toy_basis import build_default_toy_basis
from src.level4.toy_arithmetic_entry import compute_toy_entry


def assemble_toy_matrix(
    integral_steps: int = 120,
    conv_steps: int = 120,
) -> List[List[float]]:
    basis = build_default_toy_basis()
    n = len(basis)
    matrix: List[List[float]] = []
    for i in range(n):
        row: List[float] = []
        for j in range(n):
            comps = compute_toy_entry(
                basis[j],
                basis[i],
                integral_steps=integral_steps,
                conv_steps=conv_steps,
            )
            row.append(comps.entry_value)
        matrix.append(row)
    return matrix


def symmetrize(matrix: List[List[float]]) -> List[List[float]]:
    n = len(matrix)
    return [
        [0.5 * (matrix[i][j] + matrix[j][i]) for j in range(n)]
        for i in range(n)
    ]


def interval_wrap(matrix: List[List[float]], radius: float = 0.25) -> IntervalMatrix:
    if radius <= 0:
        raise ValueError("radius must be positive")
    return IntervalMatrix([
        [Interval(value - radius, value + radius) for value in row]
        for row in matrix
    ])


def candidate_vectors(n: int) -> List[List[float]]:
    vectors: List[List[float]] = []
    for i in range(n):
        v = [0.0] * n
        v[i] = 1.0
        vectors.append(v)
    if n == 2:
        vectors.extend([
            [1.0, 1.0],
            [1.0, -1.0],
            [1.0, 0.5],
            [0.5, 1.0],
        ])
    return vectors


def scan_negative_directions(interval_matrix: IntervalMatrix) -> List[Dict[str, Any]]:
    results = []
    for v in candidate_vectors(interval_matrix.n):
        cert = interval_matrix.negative_direction_certificate(v)
        results.append(cert)
    return results


def write_toy_matrix_certificate(output_path: Path) -> None:
    raw = assemble_toy_matrix()
    sym = symmetrize(raw)
    interval_matrix = interval_wrap(sym, radius=0.5)
    rayleigh_results = scan_negative_directions(interval_matrix)

    payload = {
        "phase": "12Z",
        "status": "TOY_ARITHMETIC_MATRIX_PROTOTYPE_COMPLETE",
        "important_boundary": "FLOATING_POINT_TOY_PIPELINE_ONLY",
        "raw_matrix": raw,
        "symmetrized_matrix": sym,
        "interval_radius": 0.5,
        "interval_matrix": interval_matrix.to_dict(),
        "rayleigh_results": rayleigh_results,
        "any_certified_negative_direction": any(
            r["verdict"] == "CERTIFIED_NEGATIVE_DIRECTION" for r in rayleigh_results
        ),
        "audit_strings": [
            "TOY_ARITHMETIC_MATRIX_PROTOTYPE_COMPLETE",
            "TOY_ARITHMETIC_MATRIX_ASSEMBLED",
            "TOY_MATRIX_INTERVAL_WRAPPER_CREATED",
            "TOY_HERMITIAN_SYMMETRIZATION_PERFORMED",
            "TOY_RAYLEIGH_INTERVAL_COMPUTED",
            "TOY_NEGATIVE_DIRECTION_LOGIC_TESTED",
            "FLOATING_POINT_TOY_PIPELINE_ONLY",
            "CERTIFIED_ARITHMETIC_MATRIX_NOT_YET_PROVED",
            "READY_FOR_FINAL_RESULTS_AUDIT",
        ],
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    out = Path("original_results/finite_bombieri_stability/level4_candidate/toy_matrix_prototype/toy_matrix_certificate.json")
    write_toy_matrix_certificate(out)
    print(f"Wrote {out}")
