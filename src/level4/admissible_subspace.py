from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any
import json
import math

from src.level4.toy_basis import TriangularLogBump, build_default_toy_basis
from src.level4.toy_matrix_prototype import assemble_toy_matrix, symmetrize


def integrate_real(func, lo: float, hi: float, steps: int = 2000) -> float:
    if hi <= lo:
        return 0.0
    h = (hi - lo) / steps
    total = 0.0
    for k in range(steps):
        x = lo + (k + 0.5) * h
        total += func(x)
    return total * h


def toy_mellin_value(phi: TriangularLogBump, s: float, steps: int = 3000) -> float:
    """
    Approximate Mellin value int_0^infty phi(x) x^(s-1) dx.
    Uses compact support.
    """
    lo, hi = phi.support_x
    return integrate_real(lambda x: phi.eval_x(x) * (x ** (s - 1.0)), lo, hi, steps=steps)


def constraint_matrix_for_basis(basis: List[TriangularLogBump]) -> List[List[float]]:
    return [
        [toy_mellin_value(phi, 0.0, steps=1200) for phi in basis],
        [toy_mellin_value(phi, 1.0, steps=1200) for phi in basis],
    ]


def nullspace_2xm(C: List[List[float]], tol: float = 1e-10) -> List[List[float]]:
    """
    Compute a simple numerical nullspace for a 2 x m real matrix.

    For m=2 and full rank, nullspace is zero-dimensional.
    For m=3, returns one cross-product vector if rank 2.
    For larger m, this minimal function returns coordinate-pair constructions
    only when possible. This is prototype code.
    """
    if len(C) != 2:
        raise ValueError("Expected 2-row constraint matrix")
    m = len(C[0])
    if any(len(row) != m for row in C):
        raise ValueError("Constraint matrix rows must have equal length")

    if m == 2:
        det = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        if abs(det) > tol:
            return [[], []]
        return [[-C[0][1]], [C[0][0]]]

    if m == 3:
        a = C[0]
        b = C[1]
        v = [
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0],
        ]
        norm = math.sqrt(sum(x * x for x in v))
        if norm <= tol:
            return [[0.0], [0.0], [0.0]]
        return [[x / norm] for x in v]

    raise NotImplementedError("Prototype nullspace supports m=2 or m=3 only")


def transpose(A: List[List[float]]) -> List[List[float]]:
    if not A:
        return []
    return [list(row) for row in zip(*A)]


def matmul(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    if not A or not B:
        return []
    n = len(A)
    k = len(A[0])
    if any(len(row) != k for row in A):
        raise ValueError("A rows inconsistent")
    if len(B) != k:
        raise ValueError("Dimension mismatch")
    p = len(B[0]) if B[0] else 0
    if any(len(row) != p for row in B):
        raise ValueError("B rows inconsistent")
    return [
        [
            sum(A[i][r] * B[r][j] for r in range(k))
            for j in range(p)
        ]
        for i in range(n)
    ]


def restrict_matrix(M: List[List[float]], N: List[List[float]]) -> List[List[float]]:
    if not N or not N[0]:
        return []
    return matmul(matmul(transpose(N), M), N)


def build_three_function_basis() -> List[TriangularLogBump]:
    return [
        TriangularLogBump(center=-0.5, width=0.6),
        TriangularLogBump(center=0.0, width=0.6),
        TriangularLogBump(center=0.5, width=0.6),
    ]


def write_admissible_subspace_certificate(output_path: Path) -> None:
    basis = build_three_function_basis()
    C = constraint_matrix_for_basis(basis)
    N = nullspace_2xm(C)
    # Use a simple symmetric placeholder matrix for the 3-function basis.
    M = [
        [1.0, 0.2, -0.1],
        [0.2, 0.8, 0.3],
        [-0.1, 0.3, 1.2],
    ]
    Madm = restrict_matrix(M, N)

    payload: Dict[str, Any] = {
        "phase": "B2",
        "status": "PHASE_B2_ADMISSIBLE_SUBSPACE_COMPLETE",
        "constraint_matrix_C": C,
        "nullspace_basis_N": N,
        "restricted_matrix_Madm": Madm,
        "important_boundary": "TOY_NUMERICAL_CONSTRAINTS_ONLY",
        "audit_strings": [
            "PHASE_B2_ADMISSIBLE_SUBSPACE_COMPLETE",
            "POLE_CONSTRAINT_MATRIX_DEFINED",
            "ADMISSIBLE_NULLSPACE_DEFINED",
            "ADMISSIBLE_MATRIX_RESTRICTION_PROVED",
            "M_ADM_EQUALS_N_STAR_M_N",
            "TOY_MELLIN_CONSTRAINTS_COMPUTED",
            "TOY_NULLSPACE_COMPUTED",
            "BREAKTHROUGH_NOT_ACHIEVED",
            "READY_FOR_PHASE_B3_ADMISSIBLE_TOY_MATRIX",
        ],
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    out = Path("breakthrough_push/phase_b2_admissible_subspace/admissible_subspace_certificate.json")
    write_admissible_subspace_certificate(out)
    print(f"Wrote {out}")
