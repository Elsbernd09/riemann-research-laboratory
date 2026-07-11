from __future__ import annotations

import cmath
import math


def synthetic_quartet(x: float, gamma: float) -> list[complex]:
    return [
        complex(0.5 + x, gamma),
        complex(0.5 - x, gamma),
        complex(0.5 + x, -gamma),
        complex(0.5 - x, -gamma),
    ]


def feature_vector(rho: complex, degree: int) -> list[complex]:
    w = 1.0 - 1.0 / rho
    return [w ** k for k in range(1, degree + 1)]


def matrix_norm_frobenius(matrix: list[list[complex]]) -> float:
    total = 0.0
    for row in matrix:
        for value in row:
            total += abs(value) ** 2
    return math.sqrt(total)


def toy_signed_matrix(x: float, gamma: float, degree: int) -> list[list[complex]]:
    zeros = synthetic_quartet(x, gamma)

    matrix = [
        [0j for _ in range(degree)]
        for _ in range(degree)
    ]

    for rho in zeros:
        beta = rho.real
        sign = 1.0 if beta > 0.5 else -1.0
        v = feature_vector(rho, degree)

        for i in range(degree):
            for j in range(degree):
                matrix[i][j] += sign * v[i] * v[j].conjugate()

    # Hermitian symmetrization
    for i in range(degree):
        for j in range(i + 1, degree):
            avg = 0.5 * (matrix[i][j] + matrix[j][i].conjugate())
            matrix[i][j] = avg
            matrix[j][i] = avg.conjugate()

    for i in range(degree):
        matrix[i][i] = complex(matrix[i][i].real, 0.0)

    return matrix


def rayleigh_value(matrix: list[list[complex]], vector: list[complex]) -> float:
    degree = len(vector)
    numerator = 0j
    denominator = 0.0

    for i in range(degree):
        denominator += abs(vector[i]) ** 2

        for j in range(degree):
            numerator += vector[i].conjugate() * matrix[i][j] * vector[j]

    if denominator == 0.0:
        raise ValueError("zero vector")

    return float((numerator / denominator).real)


def scan_rayleigh(matrix: list[list[complex]]) -> tuple[float, float]:
    degree = len(matrix)

    test_vectors: list[list[complex]] = []

    # Basis directions
    for i in range(degree):
        v = [0j for _ in range(degree)]
        v[i] = 1.0 + 0j
        test_vectors.append(v)

    # Pairwise real and imaginary combinations
    for i in range(degree):
        for j in range(i + 1, degree):
            v1 = [0j for _ in range(degree)]
            v1[i] = 1.0 + 0j
            v1[j] = 1.0 + 0j
            test_vectors.append(v1)

            v2 = [0j for _ in range(degree)]
            v2[i] = 1.0 + 0j
            v2[j] = 1j
            test_vectors.append(v2)

    values = [rayleigh_value(matrix, v) for v in test_vectors]

    return min(values), max(values)


def main() -> None:
    print("=" * 80)
    print("PHASE 7G TOY WEIL-INTERFACE MATRIX EXPERIMENT")
    print("=" * 80)
    print("This is a toy signed feature model, not a Weil theorem.")
    print("Pure Python version: no numpy required.")
    print("=" * 80)

    gamma = 14.134725141734693

    for degree in [2, 3, 4, 5, 8]:
        print(f"degree={degree}")

        for x in [0.0, 1e-4, 1e-3, 1e-2, 5e-2]:
            matrix = toy_signed_matrix(x=x, gamma=gamma, degree=degree)
            norm = matrix_norm_frobenius(matrix)
            rmin, rmax = scan_rayleigh(matrix)

            print(
                f"  x={x:.1e} "
                f"rayleigh_min={rmin:+.12e} "
                f"rayleigh_max={rmax:+.12e} "
                f"fro_norm={norm:.12e}"
            )

        print()

    print("Interpretation:")
    print("  The toy matrix is a diagnostic laboratory only.")
    print("  It is not an explicit-formula Weil quadratic form.")
    print("  A future phase must replace this toy sign model with a classical Weil-compatible construction.")
    print("=" * 80)


if __name__ == "__main__":
    main()
