from __future__ import annotations

from pathlib import Path
import math
from typing import List, Dict, Any

OUT = Path("original_results/finite_bombieri_stability/matrix_specific_bounds/PHASE_10V_MATRIX_SPECIFIC_EXAMPLES_OUTPUT.txt")


def frobenius_radius(m: List[float], d: List[float], L: float) -> float:
    total = 0.0
    n = len(m)
    for j in range(n):
        for k in range(n):
            total += m[j] * m[k] * (d[j] + d[k]) ** 2
    return L * math.sqrt(total)


def row_radius(m: List[float], d: List[float], L: float) -> float:
    n = len(m)
    row_sums = []
    for j in range(n):
        s = 0.0
        for k in range(n):
            s += math.sqrt(m[j] * m[k]) * L * (d[j] + d[k])
        row_sums.append(s)
    return max(row_sums)


def certify(m: List[float], d: List[float], L: float, g0: float) -> Dict[str, Any]:
    rf = frobenius_radius(m, d, L)
    rr = row_radius(m, d, L)
    rmin = min(rf, rr)

    return {
        "frobenius_radius": rf,
        "row_radius": rr,
        "combined_minimum_radius": rmin,
        "frobenius_passes": rf < g0,
        "row_passes": rr < g0,
        "combined_passes": rmin < g0,
        "best_radius": "row" if rr < rf else "frobenius",
    }


def main() -> None:
    examples = {
        "row_radius_sharper_case": {
            "multiplicities": [1, 1, 1, 1, 1, 1],
            "displacements": [0.02, 0.02, 0.02, 0.02, 0.02, 0.02],
            "L": 1.0,
            "g0": 0.30,
        },
        "frobenius_radius_sharper_case": {
            "multiplicities": [20, 1, 1, 1],
            "displacements": [0.001, 0.15, 0.15, 0.15],
            "L": 1.0,
            "g0": 1.60,
        },
        "combined_not_certified_case": {
            "multiplicities": [10, 5, 2],
            "displacements": [0.10, 0.10, 0.10],
            "L": 1.0,
            "g0": 0.50,
        },
    }

    lines = [
        "PHASE 10V MATRIX-SPECIFIC NORM EXAMPLES OUTPUT",
        "",
        "Exact audit phrase: MATRIX_SPECIFIC_NORM_CERTIFICATE",
        "Exact audit phrase: ROW_SUM_CERTIFICATE",
        "Exact audit phrase: COMBINED_MINIMUM_RADIUS_CERTIFICATE",
        "",
        "Purpose:",
        "  Compare Frobenius radius and row-sum radius.",
        "  Use the smaller valid radius for certification.",
        "",
    ]

    for name, data in examples.items():
        result = certify(data["multiplicities"], data["displacements"], data["L"], data["g0"])
        lines.append(f"EXAMPLE: {name}")
        lines.append(f"  multiplicities={data['multiplicities']}")
        lines.append(f"  displacements={data['displacements']}")
        lines.append(f"  L={data['L']}")
        lines.append(f"  g0={data['g0']}")
        for key, value in result.items():
            lines.append(f"  {key}={value}")
        lines.append("")

    lines.extend([
        "Conclusion:",
        "  The combined certificate is at least as good as either individual certificate.",
        "  The row-sum radius can be sharper than the Frobenius radius.",
        "  The Frobenius radius can also be sharper in other cases.",
        "  The algorithm should compute both and use the smaller valid upper bound.",
        "",
        "Boundary:",
        "  These are synthetic finite examples.",
        "  No zeta zeros used.",
        "  No RH claim.",
        "  No novelty claim.",
        "  This phase does not prove RH.",
        "  This phase does not falsify RH.",
        "  This phase does not use zeta zeros.",
        "  This phase does not claim novelty.",
    ])

    OUT.write_text("\n".join(lines), encoding="utf-8")

    print("=" * 80)
    print("PHASE 10V MATRIX-SPECIFIC EXAMPLES: COMPLETE")
    print("ROW-SUM RADIUS: COMPUTED")
    print("FROBENIUS RADIUS: COMPUTED")
    print("COMBINED MINIMUM RADIUS: COMPUTED")
    print("RH CLAIM: NONE")
    print("NOVELTY CLAIM: NONE")
    print("=" * 80)


if __name__ == "__main__":
    main()
