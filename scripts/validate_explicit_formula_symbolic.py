"""Symbolic validation of the explicit-formula kernel derivative."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    z = sp.symbols("z", nonzero=True)
    L = sp.symbols("L", positive=True)

    kernel = -sp.exp(L * z) / z

    direct_second_derivative = sp.diff(
        kernel,
        z,
        2,
    )

    candidate = -sp.exp(L * z) * (
        L**2 / z
        - 2 * L / z**2
        + 2 / z**3
    )

    difference = sp.simplify(
        direct_second_derivative - candidate
    )

    print("Direct symbolic second derivative:")
    print(sp.factor(direct_second_derivative))

    print("\nCandidate formula:")
    print(candidate)

    print("\nDifference:")
    print(difference)

    if difference != 0:
        raise AssertionError(
            "Explicit-formula derivative identity failed"
        )

    print(
        "\nEXPLICIT-FORMULA SYMBOLIC DERIVATIVE VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
