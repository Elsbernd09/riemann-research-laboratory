from __future__ import annotations

import math
import random
from dataclasses import dataclass


@dataclass(frozen=True)
class ScanResult:
    coeffs: tuple[float, ...]
    min_value: float
    max_value: float
    theta_at_min: float
    theta_at_max: float


def leading_polynomial(coeffs: tuple[float, ...], theta: float) -> float:
    total = 0.0
    for idx, a in enumerate(coeffs, start=1):
        total += a * (idx ** 2) * math.cos(idx * theta)
    return total


def scan_coeffs(coeffs: tuple[float, ...], grid: int = 20000) -> ScanResult:
    min_value = float("inf")
    max_value = -float("inf")
    theta_at_min = 0.0
    theta_at_max = 0.0

    for k in range(grid):
        theta = 2.0 * math.pi * k / grid
        value = leading_polynomial(coeffs, theta)

        if value < min_value:
            min_value = value
            theta_at_min = theta

        if value > max_value:
            max_value = value
            theta_at_max = theta

    return ScanResult(
        coeffs=coeffs,
        min_value=min_value,
        max_value=max_value,
        theta_at_min=theta_at_min,
        theta_at_max=theta_at_max,
    )


def random_coeffs(n: int, rng: random.Random) -> tuple[float, ...]:
    return tuple(rng.uniform(-1.0, 1.0) for _ in range(n))


def main() -> None:
    rng = random.Random(20260710)

    deterministic_tests = [
        (1.0,),
        (-1.0,),
        (1.0, 1.0),
        (1.0, -1.0),
        (0.5, -0.25, 0.125),
        (0.0, 0.0, 1.0),
    ]

    print("=" * 80)
    print("PHASE 7B LINEAR FILTER SCAN")
    print("=" * 80)

    for coeffs in deterministic_tests:
        result = scan_coeffs(coeffs)
        print(f"coeffs={result.coeffs}")
        print(f"  min={result.min_value:.12g} at theta={result.theta_at_min:.12g}")
        print(f"  max={result.max_value:.12g} at theta={result.theta_at_max:.12g}")
        assert result.min_value < 0.0
        assert result.max_value > 0.0

    random_trials = 200

    for degree in range(1, 8):
        for _ in range(random_trials):
            coeffs = random_coeffs(degree, rng)
            if all(abs(c) < 1e-12 for c in coeffs):
                continue

            result = scan_coeffs(coeffs)

            if result.min_value >= -1e-6:
                raise AssertionError(
                    f"Unexpected nearly nonnegative nontrivial cosine polynomial: {result}"
                )

            if result.max_value <= 1e-6:
                raise AssertionError(
                    f"Unexpected nearly nonpositive nontrivial cosine polynomial: {result}"
                )

    print("Deterministic checks: PASS")
    print("Random finite cosine-polynomial scans: PASS")
    print("Interpretation: nontrivial zero-mean cosine filters show sign changes.")
    print("=" * 80)


if __name__ == "__main__":
    main()
