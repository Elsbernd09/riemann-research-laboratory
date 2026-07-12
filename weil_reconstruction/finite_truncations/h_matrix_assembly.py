"""
Synthetic matrix assembly helpers for Bombieri Section 8 H-kernel.

This module may assemble matrices from synthetic finite Gamma multisets.

It does not compute eigenvalues.
It does not use zeta zeros.
It does not verify RH.
It does not claim numerical Bombieri-Weil verification.
"""

from __future__ import annotations

from collections import Counter
import importlib.util
from pathlib import Path
from typing import Iterable

module_path = Path("weil_reconstruction/finite_truncations/h_kernel_symbolic.py")
spec = importlib.util.spec_from_file_location("h_kernel_symbolic", module_path)
if spec is None or spec.loader is None:
    raise RuntimeError("Could not load h_kernel_symbolic module")

hks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hks)


def _key(z: complex, digits: int = 12) -> tuple[float, float]:
    zc = complex(z)
    return (round(zc.real, digits), round(zc.imag, digits))


class SyntheticGamma:
    """
    Synthetic finite Gamma multiset.

    This is not zeta data.
    """

    def __init__(self, values: Iterable[complex]):
        vals = tuple(complex(v) for v in values)
        if not vals:
            raise ValueError("SyntheticGamma cannot be empty")
        self.values = vals

    @classmethod
    def from_values(cls, values: Iterable[complex]) -> "SyntheticGamma":
        return cls(values)

    @property
    def size(self) -> int:
        return len(self.values)

    def distinct_values(self) -> tuple[complex, ...]:
        seen: dict[tuple[float, float], complex] = {}
        for value in self.values:
            seen.setdefault(_key(value), value)
        return tuple(seen[k] for k in sorted(seen))

    def multiplicities(self) -> dict[complex, int]:
        counts = Counter(_key(v) for v in self.values)
        representative: dict[tuple[float, float], complex] = {}
        for value in self.values:
            representative.setdefault(_key(value), value)
        return {representative[k]: counts[k] for k in counts}

    def repeated_zero_warning_count(self) -> int:
        return sum(m - 1 for m in self.multiplicities().values() if m > 1)

    def distinct_conjugate_pair_count(self) -> int:
        """
        Count distinct non-real conjugate pairs in Gamma.

        This is a synthetic helper for bookkeeping only.
        It does not compute eigenvalues.
        """
        keys = {_key(v) for v in self.distinct_values()}
        used: set[tuple[float, float]] = set()
        count = 0

        for value in self.distinct_values():
            k = _key(value)
            if k in used:
                continue

            conj_key = _key(value.conjugate())

            if abs(value.imag) > 1e-12 and conj_key in keys:
                count += 1
                used.add(k)
                used.add(conj_key)

        return count

    def assert_not_zeta_labeled(self) -> None:
        """
        Explicitly mark that this object is synthetic.
        """
        return None


def assemble_full_multiset_matrix(gamma: SyntheticGamma, t: complex) -> list[list[complex]]:
    """
    Assemble raw full multiset matrix A[j][k]=H(gamma_j,gamma_k;t).

    No eigenvalues are computed.
    """
    gamma.assert_not_zeta_labeled()
    return [
        [hks.H_kernel(gj, gk, t) for gk in gamma.values]
        for gj in gamma.values
    ]


def assemble_distinct_weighted_matrix(
    gamma: SyntheticGamma,
    t: complex,
) -> tuple[list[complex], dict[complex, int], list[list[complex]]]:
    """
    Assemble distinct weighted matrix B[j][k]=H(gamma_j,gamma_k;t)*m(gamma_k).

    No eigenvalues are computed.
    """
    gamma.assert_not_zeta_labeled()
    distinct = gamma.distinct_values()
    multiplicities = gamma.multiplicities()

    matrix = [
        [
            hks.H_kernel(gj, gk, t) * multiplicities[gk]
            for gk in distinct
        ]
        for gj in distinct
    ]

    return list(distinct), multiplicities, matrix


def matrix_shape(matrix: list[list[complex]]) -> tuple[int, int]:
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    return rows, cols


def all_entries_finite(matrix: list[list[complex]]) -> bool:
    import math

    for row in matrix:
        for entry in row:
            z = complex(entry)
            if not (math.isfinite(z.real) and math.isfinite(z.imag)):
                return False
    return True


def hermitian_residual(matrix: list[list[complex]]) -> float:
    """
    Return max |A[j][k]-conj(A[k][j])| for square matrices.

    This is only an inspection metric.
    It is not an eigenvalue computation.
    """
    rows, cols = matrix_shape(matrix)
    if rows != cols:
        raise ValueError("Hermitian residual requires a square matrix")

    max_res = 0.0
    for j in range(rows):
        for k in range(cols):
            res = abs(matrix[j][k] - matrix[k][j].conjugate())
            if res > max_res:
                max_res = res
    return max_res


def synthetic_cases() -> dict[str, SyntheticGamma]:
    return {
        "all_real": SyntheticGamma.from_values([-2, 0, 2]),
        "one_nonreal_conjugate_pair": SyntheticGamma.from_values([
            1 + 0.3j,
            1 - 0.3j,
            -1 + 0.3j,
            -1 - 0.3j,
        ]),
        "repeated_real_values": SyntheticGamma.from_values([1, 1, -1, -1]),
    }


if __name__ == "__main__":
    print("Synthetic H-matrix assembly helpers only.")
    print("No eigenvalues, no zeta zeros, no RH claims.")
