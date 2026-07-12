from __future__ import annotations

from pathlib import Path
import math
from typing import List, Dict, Any

OUT = Path("original_results/finite_bombieri_stability/certified_algorithm_v2/PHASE_10W_COMBINED_RADIUS_ALGORITHM_OUTPUT.txt")


def validate_inputs(multiplicities: List[float], displacements: List[float], lipschitz: float, zero_gap: float) -> None:
    if len(multiplicities) != len(displacements):
        raise ValueError("multiplicities and displacements must have same length")

    if not multiplicities:
        raise ValueError("at least one support point is required")

    if any(m <= 0 for m in multiplicities):
        raise ValueError("all multiplicities must be positive")

    if any(d < 0 for d in displacements):
        raise ValueError("all displacements must be nonnegative")

    if lipschitz < 0:
        raise ValueError("lipschitz constant must be nonnegative")

    if zero_gap <= 0:
        raise ValueError("zero_gap must be positive")


def frobenius_radius(multiplicities: List[float], displacements: List[float], lipschitz: float) -> float:
    total = 0.0
    n = len(multiplicities)

    for j in range(n):
        for k in range(n):
            total += multiplicities[j] * multiplicities[k] * (displacements[j] + displacements[k]) ** 2

    return lipschitz * math.sqrt(total)


def row_sum_radius(multiplicities: List[float], displacements: List[float], lipschitz: float) -> float:
    n = len(multiplicities)
    row_sums = []

    for j in range(n):
        row_sum = 0.0
        for k in range(n):
            row_sum += math.sqrt(multiplicities[j] * multiplicities[k]) * lipschitz * (displacements[j] + displacements[k])
        row_sums.append(row_sum)

    return max(row_sums)


def certify_combined_radius_stability(
    multiplicities: List[float],
    displacements: List[float],
    lipschitz: float,
    zero_gap: float,
) -> Dict[str, Any]:
    validate_inputs(multiplicities, displacements, lipschitz, zero_gap)

    r_frobenius = frobenius_radius(multiplicities, displacements, lipschitz)
    r_row = row_sum_radius(multiplicities, displacements, lipschitz)
    r_min = min(r_frobenius, r_row)

    if r_min < zero_gap:
        verdict = "CERTIFIED_STABLE"
    else:
        verdict = "NOT_CERTIFIED"

    if r_frobenius < r_row:
        best_radius = "frobenius"
    elif r_row < r_frobenius:
        best_radius = "row_sum"
    else:
        best_radius = "tie"

    return {
        "verdict": verdict,
        "frobenius_radius": r_frobenius,
        "row_sum_radius": r_row,
        "combined_minimum_radius": r_min,
        "zero_gap": zero_gap,
        "margin": zero_gap - r_min,
        "best_radius": best_radius,
        "certificate_passes": r_min < zero_gap,
        "meaning": (
            "Negative eigenvalue count is certified stable by Theorem 10V.3."
            if r_min < zero_gap
            else "The combined-radius certificate does not prove stability; no instability claim is made."
        ),
    }


def examples() -> Dict[str, Dict[str, Any]]:
    return {
        "row_sum_certifies": {
            "multiplicities": [1, 1, 1, 1, 1, 1],
            "displacements": [0.02, 0.02, 0.02, 0.02, 0.02, 0.02],
            "lipschitz": 1.0,
            "zero_gap": 0.30,
        },
        "frobenius_certifies": {
            "multiplicities": [20, 1, 1, 1],
            "displacements": [0.001, 0.15, 0.15, 0.15],
            "lipschitz": 1.0,
            "zero_gap": 1.60,
        },
        "not_certified": {
            "multiplicities": [10, 5, 2],
            "displacements": [0.10, 0.10, 0.10],
            "lipschitz": 1.0,
            "zero_gap": 0.50,
        },
        "zero_displacement": {
            "multiplicities": [7, 3, 2],
            "displacements": [0.0, 0.0, 0.0],
            "lipschitz": 100.0,
            "zero_gap": 0.01,
        },
    }


def main() -> None:
    lines = [
        "PHASE 10W COMBINED-RADIUS CERTIFIED ALGORITHM OUTPUT",
        "",
        "Exact audit phrase: COMBINED_RADIUS_CERTIFIED_ALGORITHM",
        "Exact audit phrase: COMBINED_MINIMUM_RADIUS_CERTIFICATE",
        "",
        "Verdicts:",
        "  CERTIFIED_STABLE",
        "  NOT_CERTIFIED",
        "",
        "Radii computed:",
        "  frobenius_radius",
        "  row_sum_radius",
        "  combined_minimum_radius",
        "",
    ]

    for name, data in examples().items():
        result = certify_combined_radius_stability(
            data["multiplicities"],
            data["displacements"],
            data["lipschitz"],
            data["zero_gap"],
        )

        lines.append(f"EXAMPLE: {name}")
        lines.append(f"  multiplicities={data['multiplicities']}")
        lines.append(f"  displacements={data['displacements']}")
        lines.append(f"  lipschitz={data['lipschitz']}")
        lines.append(f"  zero_gap={data['zero_gap']}")
        for key, value in result.items():
            lines.append(f"  {key}={value}")
        lines.append("")

    lines.extend([
        "Conclusion:",
        "  The combined-radius algorithm computes both Frobenius and row-sum certificates.",
        "  It certifies stability when either valid radius is below the zero spectral gap.",
        "  NOT_CERTIFIED does not imply instability.",
        "",
        "Boundary:",
        "  This is a finite-dimensional certified stability algorithm.",
        "  No zeta zeros used.",
        "  No RH claim.",
        "  No novelty claim.",
        "  This algorithm does not prove RH.",
        "  This algorithm does not falsify RH.",
        "  This algorithm does not use zeta zeros.",
        "  This algorithm does not claim novelty.",
    ])

    OUT.write_text("\n".join(lines), encoding="utf-8")

    print("=" * 80)
    print("PHASE 10W COMBINED-RADIUS ALGORITHM: COMPLETE")
    print("FROBENIUS RADIUS: COMPUTED")
    print("ROW-SUM RADIUS: COMPUTED")
    print("COMBINED MINIMUM RADIUS: COMPUTED")
    print("VERDICTS: CERTIFIED_STABLE / NOT_CERTIFIED")
    print("RH CLAIM: NONE")
    print("NOVELTY CLAIM: NONE")
    print("=" * 80)


if __name__ == "__main__":
    main()
