"""Symbolic validation of the Li blind-scale two-term expansion."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    t = sp.symbols("t")
    q = sp.symbols(
        "q",
        positive=True,
        real=True,
    )

    # t = 1 / gamma.
    #
    # theta_gamma
    # = gamma^-1 - gamma^-3/12 + gamma^-5/80 + O(gamma^-7).
    #
    # With n = q gamma = q/t:
    #
    # n theta_gamma
    # = q - q t^2/12 + q t^4/80 + O(t^6).
    phase = (
        q
        - q * t**2 / 12
        + q * t**4 / 80
    )

    gamma = 1 / t
    n = q / t

    susceptibility_model = (
        -2
        * n
        /
        (gamma**2 + sp.Rational(1, 4)) ** 2
        *
        (
            n * sp.cos(phase)
            + 2 * gamma * sp.sin(phase)
        )
    )

    expansion = sp.series(
        susceptibility_model,
        t,
        0,
        7,
    ).removeO()

    coefficient_t2 = sp.simplify(
        sp.expand(expansion).coeff(t, 2)
    )

    coefficient_t4 = sp.simplify(
        sp.expand(expansion).coeff(t, 4)
    )

    psi_candidate = -2 * q * (
        q * sp.cos(q)
        + 2 * sp.sin(q)
    )

    correction_candidate = (
        sp.Rational(4, 3)
        * q**2
        * sp.cos(q)
        +
        (
            2 * q
            - q**3 / 6
        )
        * sp.sin(q)
    )

    psi_difference = sp.simplify(
        coefficient_t2
        -
        psi_candidate
    )

    correction_difference = sp.simplify(
        coefficient_t4
        -
        correction_candidate
    )

    print("Coefficient of gamma^-2:")
    print(coefficient_t2)

    print("\nPsi candidate:")
    print(psi_candidate)

    print("\nPsi difference:")
    print(psi_difference)

    print("\nCoefficient of gamma^-4:")
    print(coefficient_t4)

    print("\nK candidate:")
    print(correction_candidate)

    print("\nK difference:")
    print(correction_difference)

    if psi_difference != 0:
        raise AssertionError(
            "Leading Li response profile failed symbolic validation"
        )

    if correction_difference != 0:
        raise AssertionError(
            "Li gamma^-4 correction profile failed symbolic validation"
        )

    c = sp.symbols(
        "c",
        positive=True,
        real=True,
    )

    K = correction_candidate.subs(q, c)

    root_relation_substitution = {
        sp.sin(c): -c * sp.cos(c) / 2,
    }

    K_at_root = sp.simplify(
        sp.expand(K).subs(
            root_relation_substitution
        )
    )

    root_candidate = (
        c**2
        * (c**2 + 4)
        * sp.cos(c)
        / 12
    )

    root_difference = sp.simplify(
        K_at_root
        -
        root_candidate
    )

    print("\nK under blind-scale root relation:")
    print(K_at_root)

    print("\nRoot-simplified candidate:")
    print(root_candidate)

    print("\nRoot-simplified difference:")
    print(root_difference)

    if root_difference != 0:
        raise AssertionError(
            "Blind-scale correction simplification failed"
        )

    print(
        "\nLI BLIND-SCALE SYMBOLIC VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
