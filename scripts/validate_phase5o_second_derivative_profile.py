from __future__ import annotations

import mpmath as mp

from src.li_susceptibility import (
    li_susceptibility_gamma_derivative,
)


def J(
    q: mp.mpf,
) -> mp.mpf:
    return (
        2 * q**3 * mp.sin(q)
        -
        12 * q**2 * mp.cos(q)
        -
        12 * q * mp.sin(q)
    )


def J_prime(
    q: mp.mpf,
) -> mp.mpf:
    return (
        2 * q**3 * mp.cos(q)
        +
        18 * q**2 * mp.sin(q)
        -
        36 * q * mp.cos(q)
        -
        12 * mp.sin(q)
    )


def K2_definition(
    q: mp.mpf,
) -> mp.mpf:
    return (
        3 * J(q)
        +
        q * J_prime(q)
    )


def K2_explicit(
    q: mp.mpf,
) -> mp.mpf:
    return (
        2 * q**4 * mp.cos(q)
        +
        24 * q**3 * mp.sin(q)
        -
        72 * q**2 * mp.cos(q)
        -
        48 * q * mp.sin(q)
    )


def chi_second_derivative(
    n: int,
    gamma: mp.mpf,
) -> mp.mpf:
    return mp.diff(
        lambda value: (
            li_susceptibility_gamma_derivative(
                n,
                value,
            )
        ),
        gamma,
    )


def main() -> None:
    mp.mp.dps = 70

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

    maximum_profile_identity_error = mp.mpf("0")
    maximum_gamma2_scaled_remainder = mp.mpf("0")

    print(
        "PHASE 5O SECOND-DERIVATIVE PROFILE VALIDATOR"
    )
    print("=" * 96)

    for q in q_values:
        identity_error = abs(
            K2_definition(q)
            -
            K2_explicit(q)
        )

        maximum_profile_identity_error = max(
            maximum_profile_identity_error,
            identity_error,
        )

        print()
        print(
            f"q_target={mp.nstr(q, 10)} "
            f"profile_identity_error="
            f"{mp.nstr(identity_error, 12)}"
        )

        for gamma in gamma_values:
            n = max(
                1,
                int(
                    mp.nint(
                        q * gamma
                    )
                ),
            )

            q_realized = (
                mp.mpf(n) / gamma
            )

            second_derivative = (
                chi_second_derivative(
                    n,
                    gamma,
                )
            )

            scaled = (
                gamma**4
                *
                second_derivative
            )

            remainder = (
                scaled
                -
                K2_explicit(
                    q_realized
                )
            )

            gamma2_scaled_remainder = (
                gamma**2
                *
                remainder
            )

            maximum_gamma2_scaled_remainder = max(
                maximum_gamma2_scaled_remainder,
                abs(
                    gamma2_scaled_remainder
                ),
            )

            print(
                f"  gamma={int(gamma):4d} "
                f"n={n:6d} "
                f"q={mp.nstr(q_realized, 8):>10s} "
                f"gamma2_remainder="
                f"{mp.nstr(gamma2_scaled_remainder, 18)}"
            )

    if (
        maximum_profile_identity_error
        >
        mp.mpf("1e-60")
    ):
        raise ArithmeticError(
            "K2 explicit-profile identity validation failed."
        )

    if not mp.isfinite(
        maximum_gamma2_scaled_remainder
    ):
        raise ArithmeticError(
            "Nonfinite scaled second-derivative remainder."
        )

    print()
    print("=" * 96)

    print(
        "maximum_profile_identity_error: "
        f"{mp.nstr(maximum_profile_identity_error, 30)}"
    )

    print(
        "maximum_absolute_gamma2_scaled_remainder: "
        f"{mp.nstr(maximum_gamma2_scaled_remainder, 30)}"
    )

    print(
        "VALIDATION STATUS: PASS"
    )

    print(
        "INTERPRETATION: NUMERICAL CONSISTENCY ONLY. "
        "THE PROOF USES THE EXACT PHASE 5F-A "
        "ANALYTIC REPRESENTATION."
    )


if __name__ == "__main__":
    main()
