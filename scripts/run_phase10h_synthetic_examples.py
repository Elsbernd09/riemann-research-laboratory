from __future__ import annotations

from pathlib import Path
import math

OUT = Path("original_results/finite_bombieri_stability/examples/PHASE_10H_SYNTHETIC_EXAMPLES_OUTPUT.txt")


def eigenvalues_2x2_symmetric(a: float, b: float, d: float) -> tuple[float, float]:
    """
    Eigenvalues of [[a,b],[b,d]].
    """
    trace = a + d
    disc = math.sqrt((a - d) ** 2 + 4.0 * b * b)
    return ((trace - disc) / 2.0, (trace + disc) / 2.0)


def negative_count(vals: tuple[float, ...]) -> int:
    return sum(1 for x in vals if x < 0)


def zero_gap(vals: tuple[float, ...]) -> float:
    return min(abs(x) for x in vals)


def example_diagonal_stable():
    # M has eigenvalues -2, 3.
    M_vals = (-2.0, 3.0)
    N = 2
    eps = 0.10
    certificate = N * eps
    gap = zero_gap(M_vals)

    # Diagonal perturbation within entrywise eps.
    E_diag = (0.08, -0.05)
    Mt_vals = (M_vals[0] + E_diag[0], M_vals[1] + E_diag[1])

    return {
        "name": "stable_diagonal_case",
        "M_eigenvalues": M_vals,
        "perturbed_eigenvalues": Mt_vals,
        "N": N,
        "epsilon": eps,
        "N_epsilon": certificate,
        "g0": gap,
        "certificate_passes": certificate < gap,
        "negative_count_before": negative_count(M_vals),
        "negative_count_after": negative_count(Mt_vals),
        "count_stable": negative_count(M_vals) == negative_count(Mt_vals),
        "interpretation": "The theorem applies; the negative count is certified stable.",
    }


def example_gap_failure_but_count_stable():
    # M has eigenvalues close to zero: -0.05, 2.
    M_vals = (-0.05, 2.0)
    N = 2
    eps = 0.04
    certificate = N * eps
    gap = zero_gap(M_vals)

    # Actual perturbation happens not to flip the sign.
    E_diag = (-0.01, 0.01)
    Mt_vals = (M_vals[0] + E_diag[0], M_vals[1] + E_diag[1])

    return {
        "name": "certificate_fails_but_count_happens_stable",
        "M_eigenvalues": M_vals,
        "perturbed_eigenvalues": Mt_vals,
        "N": N,
        "epsilon": eps,
        "N_epsilon": certificate,
        "g0": gap,
        "certificate_passes": certificate < gap,
        "negative_count_before": negative_count(M_vals),
        "negative_count_after": negative_count(Mt_vals),
        "count_stable": negative_count(M_vals) == negative_count(Mt_vals),
        "interpretation": "The theorem does not certify stability, even though this particular perturbation did not flip the count.",
    }


def example_count_flip_when_gap_condition_fails():
    # M has eigenvalues -0.05, 2.
    M_vals = (-0.05, 2.0)
    N = 2
    eps = 0.08
    certificate = N * eps
    gap = zero_gap(M_vals)

    # Perturb the negative eigenvalue across zero.
    E_diag = (0.07, 0.0)
    Mt_vals = (M_vals[0] + E_diag[0], M_vals[1] + E_diag[1])

    return {
        "name": "count_flip_when_certificate_fails",
        "M_eigenvalues": M_vals,
        "perturbed_eigenvalues": Mt_vals,
        "N": N,
        "epsilon": eps,
        "N_epsilon": certificate,
        "g0": gap,
        "certificate_passes": certificate < gap,
        "negative_count_before": negative_count(M_vals),
        "negative_count_after": negative_count(Mt_vals),
        "count_stable": negative_count(M_vals) == negative_count(Mt_vals),
        "interpretation": "The theorem does not apply, and the negative count can change.",
    }


def example_offdiagonal_stable():
    # M = [[-2, 0.2], [0.2, 3]]
    M_vals = eigenvalues_2x2_symmetric(-2.0, 0.2, 3.0)
    N = 2
    eps = 0.05
    certificate = N * eps
    gap = zero_gap(M_vals)

    # Perturbed symmetric matrix.
    Mt_vals = eigenvalues_2x2_symmetric(-1.97, 0.23, 2.98)

    return {
        "name": "stable_offdiagonal_case",
        "M_eigenvalues": M_vals,
        "perturbed_eigenvalues": Mt_vals,
        "N": N,
        "epsilon": eps,
        "N_epsilon": certificate,
        "g0": gap,
        "certificate_passes": certificate < gap,
        "negative_count_before": negative_count(M_vals),
        "negative_count_after": negative_count(Mt_vals),
        "count_stable": negative_count(M_vals) == negative_count(Mt_vals),
        "interpretation": "The theorem applies to a non-diagonal Hermitian example.",
    }


def main():
    examples = [
        example_diagonal_stable(),
        example_gap_failure_but_count_stable(),
        example_count_flip_when_gap_condition_fails(),
        example_offdiagonal_stable(),
    ]

    lines = [
        "PHASE 10H SYNTHETIC EXAMPLES OUTPUT",
        "",
        "Purpose:",
        "  Demonstrate the finite stability theorem with stable cases and failure cases.",
        "",
    ]

    for ex in examples:
        lines.extend([
            f"EXAMPLE: {ex['name']}",
            f"  M_eigenvalues={ex['M_eigenvalues']}",
            f"  perturbed_eigenvalues={ex['perturbed_eigenvalues']}",
            f"  N={ex['N']}",
            f"  epsilon={ex['epsilon']}",
            f"  N_epsilon={ex['N_epsilon']}",
            f"  g0={ex['g0']}",
            f"  certificate_passes={ex['certificate_passes']}",
            f"  negative_count_before={ex['negative_count_before']}",
            f"  negative_count_after={ex['negative_count_after']}",
            f"  count_stable={ex['count_stable']}",
            f"  interpretation={ex['interpretation']}",
            "",
        ])

    lines.extend([
        "Boundary:",
        "  These are synthetic finite examples.",
        "  No zeta zeros used.",
        "  No RH claim.",
        "  No novelty claim.",
        "  No zeta-case verification claim.",
        "",
    ])

    OUT.write_text("\n".join(lines), encoding="utf-8")

    print("=" * 80)
    print("PHASE 10H SYNTHETIC EXAMPLES: COMPLETE")
    print("STABLE CASES: RECORDED")
    print("FAILURE CASES: RECORDED")
    print("ZETA ZERO USE: NONE")
    print("RH CLAIM: NONE")
    print("NOVELTY CLAIM: NONE")
    print("=" * 80)


if __name__ == "__main__":
    main()
