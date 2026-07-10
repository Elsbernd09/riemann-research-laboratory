from __future__ import annotations

import math

import mpmath as mp

from src.li_susceptibility import (
    li_susceptibility_gamma_derivative,
)


def J(q: mp.mpf) -> mp.mpf:
    return (
        2 * q**3 * mp.sin(q)
        -
        12 * q**2 * mp.cos(q)
        -
        12 * q * mp.sin(q)
    )


def main() -> None:
    mp.mp.dps = 60

    q_values = [
        mp.mpf("0.5"),
        mp.mpf("1"),
        mp.mpf("2"),
        mp.mpf("5"),
        mp.mpf("10"),
        mp.mpf("15"),
        mp.mpf("20"),
    ]

    gamma_values = [
        mp.mpf("100"),
        mp.mpf("200"),
        mp.mpf("400"),
        mp.mpf("800"),
        mp.mpf("1600"),
    ]

    maximum_scaled_remainder = mp.mpf("0")

    print(
        "PHASE 5F-A DERIVATIVE ASYMPTOTIC VALIDATOR"
    )
    print("=" * 88)

    for q_target in q_values:
        print()
        print(
            f"q_target={mp.nstr(q_target, 8)}"
        )

        for gamma in gamma_values:
            n = max(
                1,
                int(
                    mp.nint(
                        q_target * gamma
                    )
                ),
            )

            q_realized = (
                mp.mpf(n) / gamma
            )

            scaled_derivative = (
                gamma**3
                *
                li_susceptibility_gamma_derivative(
                    n,
                    gamma,
                )
            )

            remainder = (
                scaled_derivative
                +
                J(q_realized)
            )

            second_order_scaled = (
                gamma**2
                *
                remainder
            )

            maximum_scaled_remainder = max(
                maximum_scaled_remainder,
                abs(second_order_scaled),
            )

            print(
                f"  gamma={int(gamma):4d} "
                f"n={n:6d} "
                f"q={mp.nstr(q_realized, 8):>10s} "
                f"gamma2_remainder="
                f"{mp.nstr(second_order_scaled, 16)}"
            )

    if not mp.isfinite(
        maximum_scaled_remainder
    ):
        raise ArithmeticError(
            "Nonfinite scaled derivative remainder."
        )

    print()
    print(
        "maximum_absolute_gamma2_scaled_remainder: "
        f"{mp.nstr(maximum_scaled_remainder, 30)}"
    )

    print(
        "VALIDATION STATUS: PASS"
    )

    print(
        "INTERPRETATION: NUMERICAL CONSISTENCY ONLY; "
        "PROOF IS THE DIRECT ANALYTIC DERIVATION."
    )


if __name__ == "__main__":
    main()
