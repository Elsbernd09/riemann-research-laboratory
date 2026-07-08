"""Independent symbolic validation of the Li-kernel derivative.

The validator uses multiple simplification routes because SymPy's
factor(together(...)) does not always collapse identities containing
symbolic integer exponents.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    z = sp.symbols("z", nonzero=True)
    n = sp.symbols("n", integer=True, positive=True)

    kernel = 1 - (1 - 1 / z) ** n

    direct_second_derivative = sp.diff(kernel, z, 2)

    candidate = (
        n
        * (1 - 1 / z) ** (n - 2)
        * (2 * z - n - 1)
        / z**4
    )

    raw_difference = direct_second_derivative - candidate

    simplified_difference = sp.simplify(raw_difference)

    print("Direct symbolic second derivative:")
    print(sp.factor(direct_second_derivative))

    print("\nCandidate formula:")
    print(candidate)

    print("\nSymPy simplify difference:")
    print(simplified_difference)

    if simplified_difference != 0:
        print(
            "\nGeneral symbolic simplification was inconclusive. "
            "Running fixed-integer adversarial checks."
        )

        for n_value in range(1, 51):
            fixed_difference = sp.cancel(
                sp.together(
                    raw_difference.subs(n, n_value)
                )
            )

            if fixed_difference != 0:
                raise AssertionError(
                    "Derivative identity failed at "
                    f"n={n_value}: {fixed_difference}"
                )

        print(
            "Fixed-integer symbolic checks passed for "
            "n = 1, 2, ..., 50."
        )
    else:
        print(
            "\nGeneral symbolic identity simplified exactly to zero."
        )

    print("\nSYMBOLIC DERIVATIVE VALIDATION: PASS")


if __name__ == "__main__":
    main()
