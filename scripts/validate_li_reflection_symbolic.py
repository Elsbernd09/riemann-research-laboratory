"""Symbolic validation of the reflection-mediated Li response identity."""

from __future__ import annotations

import sympy as sp


def derive_single_factor_for_fixed_n(
    n_value: int,
) -> tuple[sp.Expr, sp.Expr]:
    """Derive the Li-type derivative functional for one finite factor."""
    s, rho = sp.symbols("s rho")
    n = n_value

    expression = (
        s ** (n - 1)
        * sp.log(1 - s / rho)
    )

    derivative_value = (
        sp.diff(expression, s, n)
        .subs(s, 1)
        / sp.factorial(n - 1)
    )

    candidate = 1 - (1 - 1 / rho) ** (-n)

    return (
        sp.simplify(derivative_value),
        sp.simplify(candidate),
    )


def main() -> None:
    z = sp.symbols("z")
    n = sp.symbols("n", integer=True, positive=True)

    f = 1 - (1 - 1 / z) ** n
    g = 1 - (1 - 1 / z) ** (-n)

    reflected = sp.simplify(
        1 - (1 - 1 / (1 - z)) ** n
    )

    reflection_difference = sp.simplify(g - reflected)

    print("Reflection identity difference:")
    print(reflection_difference)

    if reflection_difference != 0:
        raise AssertionError(
            "Symbolic reflection identity did not simplify to zero"
        )

    print("\nReflection identity: PASS")

    print("\nFixed-n single-factor derivative checks")
    print("=" * 72)

    for n_value in range(1, 21):
        derived, candidate = derive_single_factor_for_fixed_n(
            n_value
        )

        difference = sp.simplify(derived - candidate)

        print(
            f"n={n_value:<2d} difference={difference}"
        )

        if difference != 0:
            raise AssertionError(
                "Single-factor derivative identity failed at "
                f"n={n_value}"
            )

    print(
        "\nSINGLE-FACTOR DERIVATIVE KERNEL VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
