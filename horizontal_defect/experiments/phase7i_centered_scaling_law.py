from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class ScalingSample:
    degree: int
    gamma: float
    x: float
    fro_norm: float
    norm_over_x2: float
    min_rayleigh: float
    max_rayleigh: float


def w_coord(rho: complex) -> complex:
    return 1.0 - 1.0 / rho


def feature_vector(rho: complex, degree: int) -> list[complex]:
    w = w_coord(rho)
    return [w ** k for k in range(1, degree + 1)]


def zero_matrix(n: int) -> list[list[complex]]:
    return [[0j for _ in range(n)] for _ in range(n)]


def add_outer(matrix: list[list[complex]], v: list[complex], scale: float) -> None:
    n = len(v)
    for i in range(n):
        for j in range(n):
            matrix[i][j] += scale * v[i] * v[j].conjugate()


def centered_matrix(x: float, gamma: float, degree: int) -> list[list[complex]]:
    matrix = zero_matrix(degree)

    for eps in [-1.0, 1.0]:
        for eta in [-1.0, 1.0]:
            rho = complex(0.5 + eps * x, eta * gamma)
            add_outer(matrix, feature_vector(rho, degree), 1.0)

    for eta in [-1.0, 1.0]:
        rho0 = complex(0.5, eta * gamma)
        add_outer(matrix, feature_vector(rho0, degree), -2.0)

    for i in range(degree):
        for j in range(i + 1, degree):
            avg = 0.5 * (matrix[i][j] + matrix[j][i].conjugate())
            matrix[i][j] = avg
            matrix[j][i] = avg.conjugate()

    for i in range(degree):
        matrix[i][i] = complex(matrix[i][i].real, 0.0)

    return matrix


def frobenius_norm(matrix: list[list[complex]]) -> float:
    return math.sqrt(sum(abs(z) ** 2 for row in matrix for z in row))


def rayleigh(matrix: list[list[complex]], v: list[complex]) -> float:
    denominator = sum(abs(z) ** 2 for z in v)
    if denominator == 0.0:
        raise ValueError("zero vector")

    numerator = 0j
    n = len(v)

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
            for z in [1.0 + 0j, -1.0 + 0j, 1j, -1j]:
                v = [0j for _ in range(degree)]
                v[i] = 1.0 + 0j
                v[j] = z
                vectors.append(v)

    return vectors


def scan(degree: int, gamma: float, x: float) -> ScalingSample:
    matrix = centered_matrix(x=x, gamma=gamma, degree=degree)
    fro = frobenius_norm(matrix)
    rays = [rayleigh(matrix, v) for v in test_vectors(degree)]

    return ScalingSample(
        degree=degree,
        gamma=gamma,
        x=x,
        fro_norm=fro,
        norm_over_x2=fro / (x * x) if x != 0.0 else 0.0,
        min_rayleigh=min(rays),
        max_rayleigh=max(rays),
    )


def main() -> None:
    print("=" * 80)
    print("PHASE 7I CENTERED QUARTET SIGNAL SCALING LAW")
    print("=" * 80)
    print("Pure Python; no numpy required.")
    print("This is a diagnostic scaling experiment, not a Weil theorem.")
    print("=" * 80)

    gamma = 14.134725141734693
    x_values = [1e-1, 5e-2, 1e-2, 5e-3, 1e-3, 5e-4]

    for degree in [2, 3, 4, 5, 8]:
        print(f"degree={degree}")

        ratios = []

        for x in x_values:
            sample = scan(degree=degree, gamma=gamma, x=x)
            ratios.append(sample.norm_over_x2)

            print(
                f"  x={x:.1e} "
                f"fro={sample.fro_norm:.12e} "
                f"fro/x^2={sample.norm_over_x2:.12e} "
                f"min_rayleigh={sample.min_rayleigh:+.12e} "
                f"max_rayleigh={sample.max_rayleigh:+.12e}"
            )

            assert sample.fro_norm > 0.0

        tail = ratios[-3:]
        spread = max(tail) - min(tail)
        rel_spread = spread / max(1e-30, sum(abs(r) for r in tail) / len(tail))

        print(f"  tail relative spread for fro/x^2 = {rel_spread:.6e}")

        assert rel_spread < 5e-3

        print()

    print("Quadratic scaling check: PASS")
    print("Interpretation: centered quartet signal scales like x^2 as x -> 0.")
    print("=" * 80)


if __name__ == "__main__":
    main()
