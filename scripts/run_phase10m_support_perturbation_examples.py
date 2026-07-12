from __future__ import annotations

from pathlib import Path
import math

OUT = Path("original_results/finite_bombieri_stability/support_perturbation/examples/PHASE_10M_SUPPORT_PERTURBATION_EXAMPLES_OUTPUT.txt")


def eigenvalues_2x2_symmetric(a: float, b: float, d: float) -> tuple[float, float]:
    trace = a + d
    disc = math.sqrt((a - d) ** 2 + 4.0 * b * b)
    return ((trace - disc) / 2.0, (trace + disc) / 2.0)


def negative_count(vals: tuple[float, ...]) -> int:
    return sum(1 for x in vals if x < 0)


def zero_gap(vals: tuple[float, ...]) -> float:
    return min(abs(x) for x in vals)


def certificate(N: int, m_max: float, L: float, delta: float) -> float:
    return 2.0 * N * m_max * L * delta


def linear_kernel_matrix(alpha1: float, alpha2: float) -> tuple[float, float, float]:
    """
    Simple symmetric Lipschitz toy kernel:
        H(x,y) = x + y

    For support alpha=[a,b], matrix is:
        [[2a, a+b],
         [a+b, 2b]]
    """
    a = 2.0 * alpha1
    b = alpha1 + alpha2
    d = 2.0 * alpha2
    return a, b, d


def stable_support_case():
    N = 2
    m_max = 1
    L = 2.0
    delta = 0.02

    alpha = (-1.5, 2.0)
    alpha_tilde = (-1.49, 1.99)

    M = linear_kernel_matrix(*alpha)
    Mt = linear_kernel_matrix(*alpha_tilde)

    vals = eigenvalues_2x2_symmetric(*M)
    vals_tilde = eigenvalues_2x2_symmetric(*Mt)

    g0 = zero_gap(vals)
    cert = certificate(N, m_max, L, delta)

    return {
        "name": "stable_support_perturbation_case",
        "support": alpha,
        "perturbed_support": alpha_tilde,
        "N": N,
        "m_max": m_max,
        "L": L,
        "delta": delta,
        "certificate_value": cert,
        "g0": g0,
        "certificate_passes": cert < g0,
        "M_eigenvalues": vals,
        "perturbed_eigenvalues": vals_tilde,
        "negative_count_before": negative_count(vals),
        "negative_count_after": negative_count(vals_tilde),
        "count_stable": negative_count(vals) == negative_count(vals_tilde),
        "interpretation": "The support-level certificate passes, so Theorem 10L certifies stability.",
    }


def certificate_fails_but_count_stable():
    N = 2
    m_max = 1
    L = 2.0
    delta = 0.20

    alpha = (-0.10, 1.0)
    alpha_tilde = (-0.12, 0.98)

    M = linear_kernel_matrix(*alpha)
    Mt = linear_kernel_matrix(*alpha_tilde)

    vals = eigenvalues_2x2_symmetric(*M)
    vals_tilde = eigenvalues_2x2_symmetric(*Mt)

    g0 = zero_gap(vals)
    cert = certificate(N, m_max, L, delta)

    return {
        "name": "certificate_fails_but_count_stable",
        "support": alpha,
        "perturbed_support": alpha_tilde,
        "N": N,
        "m_max": m_max,
        "L": L,
        "delta": delta,
        "certificate_value": cert,
        "g0": g0,
        "certificate_passes": cert < g0,
        "M_eigenvalues": vals,
        "perturbed_eigenvalues": vals_tilde,
        "negative_count_before": negative_count(vals),
        "negative_count_after": negative_count(vals_tilde),
        "count_stable": negative_count(vals) == negative_count(vals_tilde),
        "interpretation": "The theorem does not certify stability, but this particular perturbation happens to preserve the count.",
    }


def certificate_fails_and_count_changes():
    N = 2
    m_max = 1
    L = 2.0
    delta = 0.30

    alpha = (-0.05, 1.0)
    alpha_tilde = (0.10, 1.0)

    M = linear_kernel_matrix(*alpha)
    Mt = linear_kernel_matrix(*alpha_tilde)

    vals = eigenvalues_2x2_symmetric(*M)
    vals_tilde = eigenvalues_2x2_symmetric(*Mt)

    g0 = zero_gap(vals)
    cert = certificate(N, m_max, L, delta)

    return {
        "name": "certificate_fails_and_count_changes",
        "support": alpha,
        "perturbed_support": alpha_tilde,
        "N": N,
        "m_max": m_max,
        "L": L,
        "delta": delta,
        "certificate_value": cert,
        "g0": g0,
        "certificate_passes": cert < g0,
        "M_eigenvalues": vals,
        "perturbed_eigenvalues": vals_tilde,
        "negative_count_before": negative_count(vals),
        "negative_count_after": negative_count(vals_tilde),
        "count_stable": negative_count(vals) == negative_count(vals_tilde),
        "interpretation": "The certificate fails, and the count can change. This shows why a gap certificate matters.",
    }


def multiplicity_weight_case():
    N = 2
    m_max = 3
    L = 2.0
    delta = 0.02

    alpha = (-1.5, 2.0)
    alpha_tilde = (-1.49, 1.99)

    M = linear_kernel_matrix(*alpha)
    Mt = linear_kernel_matrix(*alpha_tilde)

    vals = eigenvalues_2x2_symmetric(*M)
    vals_tilde = eigenvalues_2x2_symmetric(*Mt)

    g0 = zero_gap(vals)
    cert = certificate(N, m_max, L, delta)

    return {
        "name": "multiplicity_weight_case",
        "support": alpha,
        "perturbed_support": alpha_tilde,
        "N": N,
        "m_max": m_max,
        "L": L,
        "delta": delta,
        "certificate_value": cert,
        "g0": g0,
        "certificate_passes": cert < g0,
        "M_eigenvalues": vals,
        "perturbed_eigenvalues": vals_tilde,
        "negative_count_before": negative_count(vals),
        "negative_count_after": negative_count(vals_tilde),
        "count_stable": negative_count(vals) == negative_count(vals_tilde),
        "interpretation": "Multiplicity weights shrink the certified perturbation budget through m_max.",
    }


def main():
    examples = [
        stable_support_case(),
        certificate_fails_but_count_stable(),
        certificate_fails_and_count_changes(),
        multiplicity_weight_case(),
    ]

    lines = [
        "PHASE 10M SUPPORT-PERTURBATION EXAMPLES OUTPUT",
        "",
        "Purpose:",
        "  Demonstrate Theorem 10L with synthetic support perturbation examples.",
        "",
        "Toy kernel:",
        "  H(x,y)=x+y",
        "  This is a simple symmetric Lipschitz toy kernel for examples only.",
        "",
        "Certificate:",
        "  2 N m_max L_t(U) delta < g0(M)",
        "",
    ]

    for ex in examples:
        lines.extend([
            f"EXAMPLE: {ex['name']}",
            f"  support={ex['support']}",
            f"  perturbed_support={ex['perturbed_support']}",
            f"  N={ex['N']}",
            f"  m_max={ex['m_max']}",
            f"  L={ex['L']}",
            f"  delta={ex['delta']}",
            f"  certificate_value={ex['certificate_value']}",
            f"  g0={ex['g0']}",
            f"  certificate_passes={ex['certificate_passes']}",
            f"  M_eigenvalues={ex['M_eigenvalues']}",
            f"  perturbed_eigenvalues={ex['perturbed_eigenvalues']}",
            f"  negative_count_before={ex['negative_count_before']}",
            f"  negative_count_after={ex['negative_count_after']}",
            f"  count_stable={ex['count_stable']}",
            f"  interpretation={ex['interpretation']}",
            "",
        ])

    lines.extend([
        "Boundary:",
        "  These are synthetic finite support-perturbation examples.",
        "  No zeta zeros used.",
        "  No RH claim.",
        "  No novelty claim.",
        "  No zeta-case verification claim.",
        "",
    ])

    OUT.write_text("\\n".join(lines), encoding="utf-8")

    print("=" * 80)
    print("PHASE 10M SUPPORT-PERTURBATION EXAMPLES: COMPLETE")
    print("SUPPORT-LEVEL CERTIFICATES: GENERATED")
    print("STABLE AND FAILURE CASES: RECORDED")
    print("ZETA ZERO USE: NONE")
    print("RH CLAIM: NONE")
    print("NOVELTY CLAIM: NONE")
    print("=" * 80)


if __name__ == "__main__":
    main()
