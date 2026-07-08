"""Symbolic validation of the two-orbit resonance formulas."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    x = sp.symbols(
        "x",
        positive=True,
        real=True,
    )

    K_root = (
        x**2
        * (x**2 + 4)
        / 12
        * sp.symbols("cosx")
    )

    sign = sp.symbols("s", real=True)

    cos_root = (
        sign
        * 2
        / sp.sqrt(x**2 + 4)
    )

    simplified = sp.simplify(
        K_root.subs(
            sp.symbols("cosx"),
            cos_root,
        )
    )

    candidate = (
        sign
        * x**2
        * sp.sqrt(x**2 + 4)
        / 6
    )

    difference = sp.simplify(
        simplified - candidate
    )

    print("Root correction simplification:")
    print(simplified)

    print("\nCandidate:")
    print(candidate)

    print("\nDifference:")
    print(difference)

    if difference != 0:
        raise AssertionError(
            "Closed blind-scale correction formula failed"
        )

    F = x**6 * sp.sqrt(x**2 + 4)

    derivative = sp.factor(
        sp.diff(F, x)
    )

    derivative_candidate = (
        x**5
        * (7 * x**2 + 24)
        / sp.sqrt(x**2 + 4)
    )

    derivative_difference = sp.simplify(
        derivative - derivative_candidate
    )

    print("\nF'(x):")
    print(derivative)

    print("\nDerivative difference:")
    print(derivative_difference)

    if derivative_difference != 0:
        raise AssertionError(
            "Monotone-transform derivative failed"
        )

    print(
        "\nLI TWO-ORBIT RESONANCE SYMBOLIC VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
