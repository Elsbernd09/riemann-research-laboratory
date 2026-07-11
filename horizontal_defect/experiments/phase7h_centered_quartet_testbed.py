from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class ScanSummary:
    degree: int
    x: float
    gamma: float
    fro_norm: float
    min_rayleigh: float
    max_rayleigh: float


def w_coord(rho: complex) -> complex:
    return 1.0 - 1.0 / rho


def feature_vector(rho: complex, degree: int) -> list[complex]:
    w = w_coord(rho)
    return [w ** k for k in range(1, degree + 1)]


def outer(v: list[complex]) -> list[list[complex]]:
    n = len(v)
    return [
        [v[i] * v[j].conjugate() for j in range(n)]
        for i in range(n)
    ]


def zero_matrix(n: int) -> list[list[complex]]:
    return [[0j for _ in range(n)] for _ in range(n)]


def add_scaled(
    target: list[list[complex]],
    source: list[list[complex]],
    scale: float,
) -> None:
    n = len(target)
    for i in range(n):
        for j in range(n):
            target[i][j] += scale * source[i][j]


def centered_matrix(x: float, gamma: float, degree: int) -> list[list[complex]]:
    matrix = zero_matrix(degree)

    for eps in [-1.0, 1.0]:
        for eta in [-1.0, 1.0]:
            rho = complex(0.5 + eps * x, eta * gamma)
            add_scaled(matrix, outer(feature_vector(rho, degree)), 1.0)

    for eta in [-1.0, 1.0]:
        rho0 = complex(0.5, eta * gamma)
        add_scaled(matrix, outer(feature_vector(rho0, degree)), -2.0)

    # Hermitian symmetrize to remove floating roundoff.
    for i in range(degree):
        for j in range(i + 1, degree):
            avg = 0.5 * (matrix[i][j] + matrix[j][i].conjugate())
            matrix[i][j] = avg
            matrix[j][i] = avg.conjugate()

    for i in range(degree):
        matrix[i][i] = complex(matrix[i][i].real, 0.0)

    return matrix


def frobenius_norm(matrix: list[list[complex]]) -> float:
    return math.sqrt(sum(abs(x) ** 2 for row in matrix for x in row))


def rayleigh(matrix: list[list[complex]], v: list[complex]) -> float:
    n = len(v)
    denominator = sum(abs(z) ** 2 for z in v)

    if denominator == 0.0:
        raise ValueError("zero vector")

    numerator = 0j

    for i in range(n):
        for j in range(n):
            numerator += v[i].conjugate() * matrix[i][j] * v[j]

    return float((numerator / denominator).real)


def test_vectors(degree: int) -> list[list[complex]]:
    vectors: list[list[complex]] = []

    for i in range(degree):
        v = [0j for _ in range(degree)]
        v[i] = 1.0 + 0j
        vectors.append(v)

    for i in range(degree):
        for j in range(i + 1, degree):
            v = [0j for _ in range(degree)]
            v[i] = 1.0 + 0j
            v[j] = 1.0 + 0j
            vectors.append(v)

            v = [0j for _ in range(degree)]
            v[i] = 1.0 + 0j
            v[j] = -1.0 + 0j
            vectors.append(v)

            v = [0j for _ in range(degree)]
            v[i] = 1.0 + 0j
            v[j] = 1j
            vectors.append(v)

            v = [0j for _ in range(degree)]
            v[i] = 1.0 + 0j
            v[j] = -1j
            vectors.append(v)

    return vectors


def scan(x: float, gamma: float, degree: int) -> ScanSummary:
    matrix = centered_matrix(x=x, gamma=gamma, degree=degree)
    values = [rayleigh(matrix, v) for v in test_vectors(degree)]

    return ScanSummary(
        degree=degree,
        x=x,
        gamma=gamma,
        fro_norm=frobenius_norm(matrix),
        min_rayleigh=min(values),
        max_rayleigh=max(values),
    )


def main() -> None:
    print("=" * 80)
    print("PHASE 7H CENTERED FINITE-RANK QUARTET TESTBED")
    print("=" * 80)
    print("Pure Python; no numpy required.")
    print("This is a diagnostic matrix model, not a Weil theorem.")
    print("=" * 80)

    gamma = 14.134725141734693

    for degree in [2, 3, 4, 5, 8]:
        print(f"degree={degree}")

        zero_summary = scan(x=0.0, gamma=gamma, degree=degree)

        print(
            f"  x={0.0:.1e} "
            f"min={zero_summary.min_rayleigh:+.12e} "
            f"max={zero_summary.max_rayleigh:+.12e} "
            f"fro={zero_summary.fro_norm:.12e}"
        )

        assert zero_summary.fro_norm < 1e-12

        for x in [1e-4, 1e-3, 1e-2, 5e-2]:
            s = scan(x=x, gamma=gamma, degree=degree)

            print(
                f"  x={x:.1e} "
                f"min={s.min_rayleigh:+.12e} "
                f"max={s.max_rayleigh:+.12e} "
                f"fro={s.fro_norm:.12e}"
            )

            assert s.fro_norm > 0.0

        print()

    print("Critical-line collapse check: PASS")
    print("Horizontal displacement signal check: PASS")
    print("Interpretation: centered testbed now vanishes at x=0 and responds for x != 0.")
    print("=" * 80)


if __name__ == "__main__":
    main()
