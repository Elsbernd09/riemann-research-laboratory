"""Symbolic validation of the resolvent susceptibility formulas."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    z = sp.symbols("z")
    a = sp.symbols("a", real=True)
    d = sp.symbols("d", positive=True, real=True)
    gamma = sp.symbols(
        "gamma",
        positive=True,
        real=True,
    )
    c = sp.symbols(
        "c",
        positive=True,
        real=True,
    )

    kernel = 1 / (a - z)

    direct_second_derivative = sp.diff(
        kernel,
        z,
        2,
    )

    derivative_candidate = 2 / (a - z) ** 3

    derivative_difference = sp.simplify(
        direct_second_derivative
        -
        derivative_candidate
    )

    print("Second derivative:")
    print(direct_second_derivative)

    print("\nDerivative candidate:")
    print(derivative_candidate)

    print("\nDerivative difference:")
    print(derivative_difference)

    if derivative_difference != 0:
        raise AssertionError(
            "Resolvent second derivative identity failed"
        )

    rho = sp.Rational(1, 2) + sp.I * gamma
    a_from_d = sp.Rational(1, 2) + d

    derivative_at_rho = (
        derivative_candidate
        .subs(a, a_from_d)
        .subs(z, rho)
    )

    susceptibility_from_derivative = sp.simplify(
        2 * sp.re(
            sp.expand_complex(
                derivative_at_rho
            )
        )
    )

    susceptibility_candidate = (
        4
        * d
        * (d**2 - 3 * gamma**2)
        /
        (d**2 + gamma**2) ** 3
    )

    susceptibility_difference = sp.simplify(
        susceptibility_from_derivative
        -
        susceptibility_candidate
    )

    print("\nSusceptibility from derivative:")
    print(susceptibility_from_derivative)

    print("\nExact rational candidate:")
    print(susceptibility_candidate)

    print("\nSusceptibility difference:")
    print(susceptibility_difference)

    if susceptibility_difference != 0:
        raise AssertionError(
            "Exact rational susceptibility identity failed"
        )

    similarity_scaled = sp.simplify(
        (
            gamma**3
            * susceptibility_candidate
        ).subs(
            d,
            c * gamma,
        )
    )

    profile_candidate = (
        4
        * c
        * (c**2 - 3)
        /
        (c**2 + 1) ** 3
    )

    profile_difference = sp.simplify(
        similarity_scaled - profile_candidate
    )

    print("\nExact similarity-scaled expression:")
    print(similarity_scaled)

    print("\nProfile candidate:")
    print(profile_candidate)

    print("\nProfile difference:")
    print(profile_difference)

    if profile_difference != 0:
        raise AssertionError(
            "Resolvent similarity profile identity failed"
        )

    fixed_d_limit = sp.limit(
        gamma**4
        * susceptibility_candidate,
        gamma,
        sp.oo,
    )

    fixed_d_target = -12 * d

    fixed_d_difference = sp.simplify(
        fixed_d_limit - fixed_d_target
    )

    print("\nFixed-d scaled limit:")
    print(fixed_d_limit)

    print("\nFixed-d target:")
    print(fixed_d_target)

    print("\nFixed-d difference:")
    print(fixed_d_difference)

    if fixed_d_difference != 0:
        raise AssertionError(
            "Fixed-a asymptotic limit failed"
        )

    profile_at_sqrt3 = sp.simplify(
        profile_candidate.subs(
            c,
            sp.sqrt(3),
        )
    )

    print("\nProfile at sqrt(3):")
    print(profile_at_sqrt3)

    if profile_at_sqrt3 != 0:
        raise AssertionError(
            "Predicted profile zero at sqrt(3) failed"
        )

    print(
        "\nRESOLVENT SYMBOLIC VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
