"""Symbolic validation of the quarter-turn directional contrast filter."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    delta = sp.symbols("delta")
    derivatives = {
        order: sp.symbols(f"d{order}")
        for order in range(0, 15)
    }

    horizontal = sp.Integer(0)
    vertical = sp.Integer(0)

    for order in range(0, 15):
        coefficient = derivatives[order] / sp.factorial(order)

        horizontal += coefficient * (
            delta**order + (-delta)**order
        )

        vertical += coefficient * (
            (sp.I * delta) ** order
            + (-sp.I * delta) ** order
        )

    contrast = sp.expand(horizontal - vertical)

    print("Truncated symbolic directional contrast:")
    print(contrast)

    expected = (
        4 * derivatives[2] * delta**2 / sp.factorial(2)
        + 4 * derivatives[6] * delta**6 / sp.factorial(6)
        + 4 * derivatives[10] * delta**10 / sp.factorial(10)
        + 4 * derivatives[14] * delta**14 / sp.factorial(14)
    )

    difference = sp.simplify(contrast - expected)

    print("\nExpected 4k+2 derivative filter:")
    print(expected)

    print("\nDifference:")
    print(difference)

    if difference != 0:
        raise AssertionError(
            "Quarter-turn directional filter identity failed"
        )

    forbidden_orders = [0, 4, 8, 12]

    for order in forbidden_orders:
        coefficient = sp.expand(contrast).coeff(
            derivatives[order]
        )

        if coefficient != 0:
            raise AssertionError(
                f"Derivative order {order} should cancel"
            )

    print(
        "\nQUARTER-TURN DIRECTIONAL FILTER VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
