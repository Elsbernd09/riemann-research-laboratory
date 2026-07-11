from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable


BasisFn = Callable[[complex, int], list[complex]]


@dataclass(frozen=True)
class StabilityResult:
    basis_name: str
    degree: int
    gamma: float
    h: float
    fro_norm: float
    min_rayleigh: float
    max_rayleigh: float
    both_signs: bool


def w_coord(rho: complex) -> complex:
    return 1.0 - 1.0 / rho


def basis_power(rho: complex, degree: int) -> list[complex]:
    w = w_coord(rho)
    return [w ** k for k in range(1, degree + 1)]


def basis_shifted_power(rho: complex, degree: int) -> list[complex]:
    w = w_coord(rho) - 1.0
    return [w ** k for k in range(1, degree + 1)]


def basis_reciprocal(rho: complex, degree: int) -> list[complex]:
    return [rho ** (-k) for k in range(1, degree + 1)]


def basis_hybrid(rho: complex, degree: int) -> list[complex]:
    w = w_coord(rho)
    return [w ** k + rho ** (-k) for k in range(1, degree + 1)]


BASES: list[tuple[str, BasisFn]] = [
    ("power_w", basis_power),
    ("shifted_power_w_minus_1", basis_shifted_power),
    ("reciprocal_rho", basis_reciprocal),
    ("hybrid_w_plus_reciprocal", basis_hybrid),
]


def zero_matrix(n: int) -> list[list[complex]]:
    return [[0j for _ in range(n)] for _ in range(n)]


def add_outer(matrix: list[list[complex]], v: list[complex], scale: float) -> None:
    n = len(v)
    for i in range(n):
        for j in range(n):
            matrix[i][j] += scale * v[i] * v[j].conjugate()


def centered_matrix(
    x: float,
    gamma: float,
    degree: int,
    basis: BasisFn,
) -> list[list[complex]]:
    matrix = zero_matrix(degree)

    for eps in [-1.0, 1.0]:
        for eta in [-1.0, 1.0]:
            rho = complex(0.5 + eps * x, eta * gamma)
            add_outer(matrix, basis(rho, degree), 1.0)

    for eta in [-1.0, 1.0]:
        rho0 = complex(0.5, eta * gamma)
        add_outer(matrix, basis(rho0, degree), -2.0)

    for i in range(degree):
        for j in range(i + 1, degree):
            avg = 0.5 * (matrix[i][j] + matrix[j][i].conjugate())
            matrix[i][j] = avg
            matrix[j][i] = avg.conjugate()

    for i in range(degree):
        matrix[i][i] = complex(matrix[i][i].real, 0.0)

    return matrix


def scale_matrix(matrix: list[list[complex]], scale: float) -> list[list[complex]]:
    return [[scale * z for z in row] for row in matrix]


def frobenius_norm(matrix: list[list[complex]]) -> float:
    return math.sqrt(sum(abs(z) ** 2 for row in matrix for z in row))


def rayleigh(matrix: list[list[complex]], v: list[complex]) -> float:
    denom = sum(abs(z) ** 2 for z in v)
    if denom == 0.0:
        raise ValueError("zero vector")

    numerator = 0j
    n = len(v)

    for i in range(n):
        for j in range(n):
            numerator += v[i].conjugate() * matrix[i][j] * v[j]

    return float((numerator / denom).real)


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
                1.0 - 1j,
                -1.0 - 1j,
            ]:
                v = [0j for _ in range(degree)]
                v[i] = 1.0 + 0j
                v[j] = z
                vectors.append(v)

    vectors.append([1.0 + 0j for _ in range(degree)])
    vectors.append([((-1.0) ** k) + 0j for k in range(degree)])
    vectors.append([complex(math.cos(k), math.sin(k)) for k in range(degree)])
    vectors.append([complex(math.cos(2 * k), math.sin(2 * k)) for k in range(degree)])

    return vectors


def audit_case(
    basis_name: str,
    basis: BasisFn,
    degree: int,
    gamma: float,
    h: float,
) -> StabilityResult:
    c = centered_matrix(x=h, gamma=gamma, degree=degree, basis=basis)
    b = scale_matrix(c, 1.0 / (h * h))
    values = [rayleigh(b, v) for v in test_vectors(degree)]

    min_r = min(values)
    max_r = max(values)

    return StabilityResult(
        basis_name=basis_name,
        degree=degree,
        gamma=gamma,
        h=h,
        fro_norm=frobenius_norm(b),
        min_rayleigh=min_r,
        max_rayleigh=max_r,
        both_signs=(min_r < -1e-10 and max_r > 1e-10),
    )


def main() -> None:
    print("=" * 80)
    print("PHASE 7K STABILITY AUDIT ACROSS HEIGHTS AND BASIS CHOICES")
    print("=" * 80)
    print("Pure Python; no numpy required.")
    print("This is diagnostic, not a Weil theorem.")
    print("=" * 80)

    gammas = [
        14.134725141734693,
        21.022039638771554,
        25.010857580145688,
        50.0,
        100.0,
        250.0,
    ]

    degrees = [2, 3, 4, 5, 8]
    h = 5e-4

    total = 0
    both_sign_count = 0
    failures: list[StabilityResult] = []

    for basis_name, basis in BASES:
        print(f"basis={basis_name}")

        for gamma in gammas:
            for degree in degrees:
                result = audit_case(
                    basis_name=basis_name,
                    basis=basis,
                    degree=degree,
                    gamma=gamma,
                    h=h,
                )

                total += 1

                if result.both_signs:
                    both_sign_count += 1
                else:
                    failures.append(result)

                print(
                    f"  gamma={gamma:.6f} degree={degree} "
                    f"fro={result.fro_norm:.6e} "
                    f"min={result.min_rayleigh:+.6e} "
                    f"max={result.max_rayleigh:+.6e} "
                    f"both={result.both_signs}"
                )

        print()

    print("=" * 80)
    print(f"total cases={total}")
    print(f"both-sign cases={both_sign_count}")
    print(f"failure cases={len(failures)}")

    if failures:
        print("Recorded failures/non-detections:")
        for item in failures[:20]:
            print(
                f"  basis={item.basis_name} gamma={item.gamma} degree={item.degree} "
                f"min={item.min_rayleigh:+.6e} max={item.max_rayleigh:+.6e}"
            )

    success_rate = both_sign_count / total

    print(f"both-sign success rate={success_rate:.6f}")

    if success_rate < 0.80:
        raise AssertionError("Diagnostic stability rate below 80% threshold.")

    print("Stability audit: PASS")
    print("Interpretation: both-sign diagnostic behavior is broadly stable but not promoted to a theorem.")
    print("=" * 80)


if __name__ == "__main__":
    main()
