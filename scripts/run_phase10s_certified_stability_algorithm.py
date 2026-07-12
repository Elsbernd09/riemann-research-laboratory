from __future__ import annotations

from pathlib import Path
import math
from typing import List, Dict, Any

OUT = Path("original_results/finite_bombieri_stability/certified_algorithm/PHASE_10S_CERTIFIED_ALGORITHM_OUTPUT.txt")


def weighted_radius(multiplicities: List[float], displacements: List[float], lipschitz: float) -> float:
    if len(multiplicities) != len(displacements):
        raise ValueError("multiplicities and displacements must have the same length")

    if not multiplicities:
        raise ValueError("at least one support point is required")

    if any(m <= 0 for m in multiplicities):
        raise ValueError("all multiplicities must be positive")

    if any(d < 0 for d in displacements):
        raise ValueError("all displacements must be nonnegative")

    if lipschitz < 0:
        raise ValueError("Lipschitz constant must be nonnegative")

    total = 0.0
    n = len(multiplicities)

    for j in range(n):
        for k in range(n):
            total += multiplicities[j] * multiplicities[k] * (displacements[j] + displacements[k]) ** 2

    return lipschitz * math.sqrt(total)


def certify_weighted_support_stability(
    multiplicities: List[float],
    displacements: List[float],
    lipschitz: float,
    zero_gap: float,
) -> Dict[str, Any]:
    if zero_gap <= 0:
        raise ValueError("zero_gap must be positive")

    radius = weighted_radius(multiplicities, displacements, lipschitz)

    if radius < zero_gap:
        verdict = "CERTIFIED_STABLE"
    else:
        verdict = "NOT_CERTIFIED"

    return {
        "verdict": verdict,
        "weighted_radius": radius,
        "zero_gap": zero_gap,
        "margin": zero_gap - radius,
        "certificate_passes": radius < zero_gap,
        "meaning": (
            "Negative eigenvalue count is certified stable by Theorem 10Q."
            if radius < zero_gap
            else "The certificate does not prove stability; the count may still be stable or unstable."
        ),
    }


def examples() -> Dict[str, Dict[str, Any]]:
    return {
        "certified_stable_weighted_case": {
            "multiplicities": [10, 1, 1, 1, 1],
            "displacements": [0.001, 0.10, 0.10, 0.10, 0.10],
            "lipschitz": 1.0,
            "zero_gap": 1.35,
        },
        "not_certified_case": {
            "multiplicities": [10, 1, 1, 1, 1],
            "displacements": [0.08, 0.10, 0.10, 0.10, 0.10],
            "lipschitz": 1.0,
            "zero_gap": 0.75,
        },
        "zero_displacement_case": {
            "multiplicities": [3, 2, 1],
            "displacements": [0.0, 0.0, 0.0],
            "lipschitz": 5.0,
            "zero_gap": 0.1,
        },
    }


def main() -> None:
    lines = [
        "PHASE 10S CERTIFIED STABILITY ALGORITHM OUTPUT",
        "",
        "Algorithm:",
        "  Weighted Support Stability Certification",
        "",
        "Verdicts:",
        "  CERTIFIED_STABLE",
        "  NOT_CERTIFIED",
        "",
        "Certificate:",
        "  R(Gamma,Gamma_tilde,t) < g0(M)",
        "",
        "Exact audit phrase: CERTIFIED_STABILITY_ALGORITHM",
        "",
    ]

    for name, data in examples().items():
        result = certify_weighted_support_stability(
            data["multiplicities"],
            data["displacements"],
            data["lipschitz"],
            data["zero_gap"],
        )

        lines.extend([
            f"EXAMPLE: {name}",
            f"  multiplicities={data['multiplicities']}",
            f"  displacements={data['displacements']}",
            f"  lipschitz={data['lipschitz']}",
            f"  zero_gap={data['zero_gap']}",
            f"  weighted_radius={result['weighted_radius']}",
            f"  margin={result['margin']}",
            f"  verdict={result['verdict']}",
            f"  certificate_passes={result['certificate_passes']}",
            f"  meaning={result['meaning']}",
            "",
        ])

    lines.extend([
        "Boundary:",
        "  This is a finite-dimensional certified stability algorithm.",
        "  No zeta zeros used.",
        "  No RH claim.",
        "  No novelty claim.",
        "  No zeta-case verification claim.",
        "",
        "Exact audit boundary phrases:",
        "  This algorithm does not prove RH.",
        "  This algorithm does not falsify RH.",
        "  This algorithm does not use zeta zeros.",
        "  This algorithm does not claim novelty.",
    ])

    OUT.write_text("\n".join(lines), encoding="utf-8")

    print("=" * 80)
    print("PHASE 10S CERTIFIED STABILITY ALGORITHM: COMPLETE")
    print("CERTIFIED_STABLE / NOT_CERTIFIED VERDICTS: IMPLEMENTED")
    print("WEIGHTED RADIUS CERTIFICATE: IMPLEMENTED")
    print("RH CLAIM: NONE")
    print("NOVELTY CLAIM: NONE")
    print("=" * 80)


if __name__ == "__main__":
    main()
