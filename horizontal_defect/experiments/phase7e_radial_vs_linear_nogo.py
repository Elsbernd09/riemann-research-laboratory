from __future__ import annotations

import math
import random
from dataclasses import dataclass


@dataclass(frozen=True)
class FilterScan:
    coeffs: tuple[float, ...]
    min_ratio: float
    max_ratio: float
    theta_min: float
    theta_max: float


def p_theta(coeffs: tuple[float, ...], theta: float) -> float:
    return sum(a * (n ** 2) * math.cos(n * theta) for n, a in enumerate(coeffs, start=1))


def linear_filter(coeffs: tuple[float, ...], u: float, theta: float) -> float:
    return sum(
        a * math.cos(n * theta) * (math.cosh(n * u) - 1.0)
        for n, a in enumerate(coeffs, start=1)
    )


def scan_ratio(coeffs: tuple[float, ...], u: float, grid: int = 20000) -> FilterScan:
    min_ratio = float("inf")
    max_ratio = -float("inf")
    theta_min = 0.0
    theta_max = 0.0

    for k in range(grid):
        theta = 2.0 * math.pi * k / grid
        ratio = linear_filter(coeffs, u, theta) / (u * u)

        if ratio < min_ratio:
            min_ratio = ratio
            theta_min = theta

        if ratio > max_ratio:
            max_ratio = ratio
            theta_max = theta

    return FilterScan(
        coeffs=coeffs,
        min_ratio=min_ratio,
        max_ratio=max_ratio,
        theta_min=theta_min,
        theta_max=theta_max,
    )


def main() -> None:
    print("=" * 80)
    print("PHASE 7E RADIAL DEFECT VS LINEAR FILTER NO-GO SCAN")
    print("=" * 80)

    deterministic = [
        (1.0,),
        (-1.0,),
        (1.0, 1.0),
        (1.0, -0.5),
        (0.25, -0.75, 0.5),
        (0.0, 1.0, 0.0, -0.25),
    ]

    u_values = [1e-1, 5e-2, 1e-2]

    for coeffs in deterministic:
        print(f"coeffs={coeffs}")

        for u in u_values:
            result = scan_ratio(coeffs, u)
            print(
                f"  u={u:.1e} "
                f"min L/u^2={result.min_ratio:+.12e} "
                f"max L/u^2={result.max_ratio:+.12e}"
            )

            if all(abs(c) < 1e-14 for c in coeffs):
                continue

            assert result.min_ratio < 0.0
            assert result.max_ratio > 0.0

    rng = random.Random(20260710)

    for degree in range(1, 8):
        for _ in range(100):
            coeffs = tuple(rng.uniform(-1.0, 1.0) for _ in range(degree))

            if all(abs(c) < 1e-12 for c in coeffs):
                continue

            result = scan_ratio(coeffs, 1e-2)

            if result.min_ratio >= -1e-5:
                raise AssertionError(
                    f"Unexpected nonnegative lower ratio for coeffs={coeffs}, result={result}"
                )

    print("Deterministic scans: PASS")
    print("Random scans: PASS")
    print("Interpretation: finite linear filters cannot uniformly dominate u^2.")
    print("=" * 80)


if __name__ == "__main__":
    main()
