from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class AuditResult:
    degree: int
    gamma: float
    h: float
    fro_norm: float
    min_rayleigh: float
    max_rayleigh: float
    has_negative: bool
    has_positive: bool


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

    # Hermitian cleanup
    for i in range(degree):
        for j in range(i + 1, degree):
            avg = 0.5 * (matrix[i][j] + matrix[j][i].conjugate())
            matrix[i][j] = avg
            matrix[j][i] = avg.conjugate()

    for i in range(degree):
        matrix[i][i] = complex(matrix[i][i].real, 0.0)

    return matrix


def scaled_second_order_matrix(h: float, gamma: float, degree: int) -> list[list[complex]]:
    c = centered_matrix(x=h, gamma=gamma, degree=degree)
    scale = 1.0 / (h * h)

    return [
        [scale * value for value in row]
        for row in c
    ]


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
            for z in [
                1.0 + 0j,
                -1.0 + 0j,
                1j,
                -1j,
                0.5 + 0.5j,
                -0.5 + 0.5j,
            ]:
                v = [0j for _ in range(degree)]
                v[i] = 1.0 + 0j
                v[j] = z
                vectors.append(v)

    # Low-frequency all-ones style probes
    vectors.append([1.0 + 0j for _ in range(degree)])
    vectors.append([((-1.0) ** k) + 0j for k in range(degree)])
    vectors.append([complex(math.cos(k), math.sin(k)) for k in range(degree)])

    return vectors


def audit(degree: int, gamma: float, h: float) -> AuditResult:
    matrix = scaled_second_order_matrix(h=h, gamma=gamma, degree=degree)
    values = [rayleigh(matrix, v) for v in test_vectors(degree)]

    min_rayleigh = min(values)
    max_rayleigh = max(values)

    return AuditResult(
        degree=degree,
        gamma=gamma,
        h=h,
        fro_norm=frobenius_norm(matrix),
        min_rayleigh=min_rayleigh,
        max_rayleigh=max_rayleigh,
        has_negative=min_rayleigh < -1e-10,
        has_positive=max_rayleigh > 1e-10,
    )


def main() -> None:
    print("=" * 80)
    print("PHASE 7J SECOND-ORDER COEFFICIENT INDEFINITENESS AUDIT")
    print("=" * 80)
    print("Pure Python; no numpy required.")
    print("This scans Rayleigh quotients of C_m(h,gamma)/h^2.")
    print("This is diagnostic, not a Weil theorem.")
    print("=" * 80)

    gammas = [
        14.134725141734693,
        21.022039638771554,
        50.0,
        100.0,
    ]

    h_values = [1e-3, 5e-4]

    all_passed = True

    for gamma in gammas:
        print(f"gamma={gamma}")

        for degree in [2, 3, 4, 5, 8]:
            for h in h_values:
                result = audit(degree=degree, gamma=gamma, h=h)

                print(
                    f"  degree={degree} h={h:.1e} "
                    f"fro={result.fro_norm:.12e} "
                    f"min={result.min_rayleigh:+.12e} "
                    f"max={result.max_rayleigh:+.12e} "
                    f"both_signs={result.has_negative and result.has_positive}"
                )

                if not (result.has_negative and result.has_positive):
                    all_passed = False

        print()

    if not all_passed:
        raise AssertionError(
            "At least one tested configuration did not show both signs in the deterministic Rayleigh scan."
        )

    print("Second-order tested Rayleigh indefiniteness: PASS")
    print("Interpretation: the finite-rank diagnostic signal shows both positive and negative directions in tested cases.")
    print("=" * 80)


if __name__ == "__main__":
    main()
