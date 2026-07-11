from __future__ import annotations

import math
import random


def delta(n: int, u: float, theta: float) -> float:
    return math.cos(n * theta) * (math.cosh(n * u) - 1.0)


def q12(u: float, theta: float) -> float:
    d1 = delta(1, u, theta)
    d2 = delta(2, u, theta)
    return d1 * d1 + d2 * d2


def leading_profile(theta: float) -> float:
    return 0.25 * (math.cos(theta) ** 2 + 16.0 * math.cos(2.0 * theta) ** 2)


def scan_grid(u: float, grid: int = 50000) -> tuple[float, float, float]:
    min_q = float("inf")
    theta_min = 0.0
    max_q = -float("inf")

    for k in range(grid):
        theta = 2.0 * math.pi * k / grid
        value = q12(u, theta)

        if value < min_q:
            min_q = value
            theta_min = theta

        if value > max_q:
            max_q = value

    return min_q, max_q, theta_min


def main() -> None:
    print("=" * 80)
    print("PHASE 7F QUADRATIC LI-FILTER POSITIVITY VALIDATION")
    print("=" * 80)

    for u in [1e-1, 5e-2, 1e-2, 1e-3]:
        min_q, max_q, theta_min = scan_grid(u)
        print(
            f"u={u:.1e} "
            f"min Q12={min_q:.12e} "
            f"max Q12={max_q:.12e} "
            f"theta_min={theta_min:.12f}"
        )

        assert min_q > 0.0
        assert max_q > min_q

    rng = random.Random(20260710)

    for _ in range(20000):
        u = rng.uniform(1e-5, 0.5)
        theta = rng.uniform(0.0, 2.0 * math.pi)
        value = q12(u, theta)

        if value <= 0.0:
            raise AssertionError((u, theta, value))

    print("Random positivity test: PASS")

    for theta in [0.0, 0.3, math.pi / 4, math.pi / 2, 2.0]:
        u = 1e-5
        ratio = q12(u, theta) / (u ** 4)
        profile = leading_profile(theta)
        relerr = abs(ratio - profile) / max(1.0, abs(profile))
        print(
            f"theta={theta:.6f} "
            f"Q/u^4={ratio:.12e} "
            f"profile={profile:.12e} "
            f"relerr={relerr:.3e}"
        )

        assert relerr < 1e-4

    print("Small-displacement profile: PASS")
    print("Interpretation: quadratic lift defeats finite linear phase sign obstruction.")
    print("=" * 80)


if __name__ == "__main__":
    main()
