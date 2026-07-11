from __future__ import annotations

import math
import random
from dataclasses import dataclass


@dataclass(frozen=True)
class ZeroCandidate:
    beta: float
    gamma: float


def radial_defect(z: ZeroCandidate) -> float:
    rho = complex(z.beta, z.gamma)
    w = 1.0 - 1.0 / rho
    return math.log(abs(w)) ** 2


def aggregate_defect(zeros: list[ZeroCandidate], weights: list[float]) -> float:
    if len(zeros) != len(weights):
        raise ValueError("zeros and weights must have the same length")
    if any(w <= 0.0 for w in weights):
        raise ValueError("weights must be positive")

    return sum(w * radial_defect(z) for z, w in zip(zeros, weights))


def main() -> None:
    print("=" * 80)
    print("PHASE 7D AGGREGATION BARRIER VALIDATION")
    print("=" * 80)

    critical_line = [
        ZeroCandidate(0.5, 14.134725141734693),
        ZeroCandidate(0.5, 21.022039638771554),
        ZeroCandidate(0.5, 25.010857580145688),
    ]

    weights = [1.0, 0.5, 2.0]

    cl_energy = aggregate_defect(critical_line, weights)

    print(f"critical-line aggregate energy = {cl_energy:.18e}")

    assert abs(cl_energy) < 1e-24

    off_critical = [
        ZeroCandidate(0.5, 14.134725141734693),
        ZeroCandidate(0.55, 21.022039638771554),
        ZeroCandidate(0.5, 25.010857580145688),
    ]

    off_energy = aggregate_defect(off_critical, weights)

    print(f"one off-critical aggregate energy = {off_energy:.18e}")

    assert off_energy > 0.0

    rng = random.Random(20260710)

    for trial in range(500):
        zeros = []
        weights = []

        has_off_critical = False

        for _ in range(10):
            gamma = rng.uniform(5.0, 200.0)

            if rng.random() < 0.8:
                beta = 0.5
            else:
                beta = 0.5 + rng.choice([-1.0, 1.0]) * rng.uniform(1e-4, 0.2)
                has_off_critical = True

            zeros.append(ZeroCandidate(beta, gamma))
            weights.append(rng.uniform(0.1, 3.0))

        energy = aggregate_defect(zeros, weights)

        if has_off_critical:
            if energy <= 0.0:
                raise AssertionError("off-critical configuration produced zero energy")
        else:
            if abs(energy) > 1e-24:
                raise AssertionError("critical-line configuration produced nonzero energy")

    print("finite positive aggregation tests: PASS")
    print("interpretation: positivity is easy; arithmetic-side control remains open")
    print("=" * 80)


if __name__ == "__main__":
    main()
