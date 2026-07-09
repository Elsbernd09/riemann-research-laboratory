"""Validate the exact gamma derivative of Li susceptibility."""

from __future__ import annotations

import mpmath as mp

from src.li_susceptibility import (
    li_susceptibility_exact,
    li_susceptibility_gamma_derivative,
)


def main() -> None:
    mp.mp.dps = 100

    cases = [
        (1, "14.134725"),
        (10, "50"),
        (100, "100"),
        (500, "250"),
        (1000, "500"),
        (5000, "811"),
    ]

    print("LI SUSCEPTIBILITY GAMMA-DERIVATIVE VALIDATION")
    print("=" * 100)

    for n, gamma_text in cases:
        gamma = mp.mpf(
            gamma_text
        )

        exact = (
            li_susceptibility_gamma_derivative(
                n,
                gamma,
            )
        )

        numerical = mp.diff(
            lambda value: (
                li_susceptibility_exact(
                    n,
                    value,
                )
            ),
            gamma,
        )

        denominator = max(
            abs(exact),
            abs(numerical),
            mp.mpf("1e-95"),
        )

        relative_error = (
            abs(exact - numerical)
            /
            denominator
        )

        print(
            f"n={n:<6d} "
            f"gamma={mp.nstr(gamma, 12):>15s} "
            f"exact={mp.nstr(exact, 22):>28s} "
            f"numerical={mp.nstr(numerical, 22):>28s} "
            f"relerr={mp.nstr(relative_error, 8):>14s}"
        )

        if relative_error > mp.mpf(
            "1e-80"
        ):
            raise AssertionError(
                "Li susceptibility gamma derivative "
                f"failed validation for n={n}, gamma={gamma}"
            )

    print()
    print(
        "LI SUSCEPTIBILITY GAMMA-DERIVATIVE VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
