from __future__ import annotations

from pathlib import Path
import math

OUT = Path("original_results/finite_bombieri_stability/sharper_bounds/examples/PHASE_10R_STRICT_IMPROVEMENT_EXAMPLES_OUTPUT.txt")


def old_certificate(N: int, m_max: float, L: float, delta: float) -> float:
    return 2.0 * N * m_max * L * delta


def new_uniform_certificate(m_tot: float, L: float, delta: float) -> float:
    return 2.0 * L * m_tot * delta


def weighted_radius(multiplicities: list[float], displacements: list[float], L: float) -> float:
    total = 0.0
    n = len(multiplicities)
    for j in range(n):
        for k in range(n):
            total += multiplicities[j] * multiplicities[k] * (displacements[j] + displacements[k]) ** 2
    return L * math.sqrt(total)


def example_old_fails_new_uniform_passes():
    """
    N=5, m_max=10, but only one point has high multiplicity.
    M_tot=14, far below N*m_max=50.

    Choose g0 so:
      old = 10.0 fails,
      new_uniform = 2.8 passes.
    """
    N = 5
    multiplicities = [10, 1, 1, 1, 1]
    m_max = max(multiplicities)
    m_tot = sum(multiplicities)
    L = 1.0
    delta = 0.10
    g0 = 5.0

    old = old_certificate(N, m_max, L, delta)
    new = new_uniform_certificate(m_tot, L, delta)
    displacements = [delta] * N
    weighted = weighted_radius(multiplicities, displacements, L)

    return {
        "name": "old_fails_new_uniform_passes",
        "N": N,
        "multiplicities": multiplicities,
        "m_max": m_max,
        "m_tot": m_tot,
        "L": L,
        "delta": delta,
        "g0": g0,
        "old_certificate": old,
        "new_uniform_certificate": new,
        "weighted_radius": weighted,
        "old_passes": old < g0,
        "new_uniform_passes": new < g0,
        "weighted_passes": weighted < g0,
        "interpretation": "The old worst-case bound fails, but the improved total-multiplicity certificate passes.",
    }


def example_uniform_fails_weighted_passes():
    """
    Same multiplicities, but the large-multiplicity point barely moves.
    Uniform certificate uses max delta, while weighted radius uses actual d_j.

    Choose g0 so:
      old fails,
      new uniform fails,
      weighted passes.
    """
    N = 5
    multiplicities = [10, 1, 1, 1, 1]
    m_max = max(multiplicities)
    m_tot = sum(multiplicities)
    L = 1.0
    delta = 0.10
    displacements = [0.001, 0.10, 0.10, 0.10, 0.10]
    g0 = 1.35

    old = old_certificate(N, m_max, L, delta)
    new = new_uniform_certificate(m_tot, L, delta)
    weighted = weighted_radius(multiplicities, displacements, L)

    return {
        "name": "uniform_fails_weighted_passes",
        "N": N,
        "multiplicities": multiplicities,
        "m_max": m_max,
        "m_tot": m_tot,
        "L": L,
        "delta": delta,
        "displacements": displacements,
        "g0": g0,
        "old_certificate": old,
        "new_uniform_certificate": new,
        "weighted_radius": weighted,
        "old_passes": old < g0,
        "new_uniform_passes": new < g0,
        "weighted_passes": weighted < g0,
        "interpretation": "Both uniform certificates fail, but the actual weighted displacement certificate passes.",
    }


def example_all_fail_near_gap():
    """
    Shows the sharper theorem does not magically certify unstable cases.
    """
    N = 5
    multiplicities = [10, 1, 1, 1, 1]
    m_max = max(multiplicities)
    m_tot = sum(multiplicities)
    L = 1.0
    delta = 0.10
    displacements = [0.08, 0.10, 0.10, 0.10, 0.10]
    g0 = 0.75

    old = old_certificate(N, m_max, L, delta)
    new = new_uniform_certificate(m_tot, L, delta)
    weighted = weighted_radius(multiplicities, displacements, L)

    return {
        "name": "all_certificates_fail_near_gap",
        "N": N,
        "multiplicities": multiplicities,
        "m_max": m_max,
        "m_tot": m_tot,
        "L": L,
        "delta": delta,
        "displacements": displacements,
        "g0": g0,
        "old_certificate": old,
        "new_uniform_certificate": new,
        "weighted_radius": weighted,
        "old_passes": old < g0,
        "new_uniform_passes": new < g0,
        "weighted_passes": weighted < g0,
        "interpretation": "All certificates fail; the sharper result remains honest and does not over-certify.",
    }


def main():
    examples = [
        example_old_fails_new_uniform_passes(),
        example_uniform_fails_weighted_passes(),
        example_all_fail_near_gap(),
    ]

    lines = [
        "PHASE 10R STRICT-IMPROVEMENT EXAMPLES OUTPUT",
        "",
        "Purpose:",
        "  Show that the Phase 10Q weighted certificate is strictly stronger than the old Phase 10L worst-case certificate.",
        "",
        "Old certificate:",
        "  2 N m_max L_t(U) delta < g0(M)",
        "",
        "New uniform certificate:",
        "  2 L_t(U) M_tot delta < g0(M)",
        "",
        "New weighted certificate:",
        "  R(Gamma,Gamma_tilde,t) < g0(M)",
        "",
        "Exact audit phrase: STRICT_IMPROVEMENT_EXAMPLES",
        "",
    ]

    for ex in examples:
        lines.append(f"EXAMPLE: {ex['name']}")
        for key, value in ex.items():
            if key != "name":
                lines.append(f"  {key}={value}")
        lines.append("")

    lines.extend([
        "Conclusion:",
        "  The sharper bound is not merely cosmetic.",
        "  There are cases where the old certificate fails and the new certificate passes.",
        "  There are also cases where even the sharper certificate fails, preserving honest non-certification.",
        "",
        "Boundary:",
        "  These are synthetic finite examples.",
        "  No zeta zeros used.",
        "  No RH claim.",
        "  No novelty claim.",
        "  No zeta-case verification claim.",
        "",
        "Exact audit boundary phrases:",
        "  This phase does not prove RH.",
        "  This phase does not falsify RH.",
        "  This phase does not use zeta zeros.",
        "  This phase does not claim novelty.",
    ])

    OUT.write_text("\n".join(lines), encoding="utf-8")

    print("=" * 80)
    print("PHASE 10R STRICT-IMPROVEMENT EXAMPLES: COMPLETE")
    print("OLD FAILS / NEW PASSES CASES: RECORDED")
    print("WEIGHTED RADIUS ADVANTAGE: RECORDED")
    print("HONEST NON-CERTIFICATION CASE: RECORDED")
    print("RH CLAIM: NONE")
    print("NOVELTY CLAIM: NONE")
    print("=" * 80)


if __name__ == "__main__":
    main()
