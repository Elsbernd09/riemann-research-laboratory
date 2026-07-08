"""High-precision validation of resolvent susceptibility."""

from __future__ import annotations

import mpmath as mp

from src.resolvent_susceptibility import (
    critical_line_point,
    fixed_a_asymptotic_target,
    fixed_a_scaled_susceptibility,
    resolvent_profile,
    resolvent_second_derivative_factored,
    resolvent_second_derivative_numerical,
    resolvent_susceptibility_exact,
    resolvent_susceptibility_from_derivative,
    scaled_resolvent_susceptibility,
)


def relative_error(
    a: mp.mpf | mp.mpc,
    b: mp.mpf | mp.mpc,
) -> mp.mpf:
    denominator = max(
        abs(a),
        abs(b),
        mp.mpf("1e-180"),
    )

    return abs(a - b) / denominator


def main() -> None:
    mp.mp.dps = 160

    print("DIRECT SECOND-DERIVATIVE VALIDATION")
    print("=" * 92)

    derivative_cases = [
        (mp.mpf("1"), mp.mpf("14.134725141734693790")),
        (mp.mpf("2"), mp.mpf("50")),
        (mp.mpf("10"), mp.mpf("100")),
        (mp.mpf("100"), mp.mpf("250")),
        (mp.mpf("500"), mp.mpf("1000")),
    ]

    worst_derivative_error = mp.mpf("0")

    for a, gamma in derivative_cases:
        rho = critical_line_point(gamma)

        manual = resolvent_second_derivative_factored(
            rho,
            a,
        )

        numerical = resolvent_second_derivative_numerical(
            rho,
            a,
        )

        error = relative_error(
            manual,
            numerical,
        )

        worst_derivative_error = max(
            worst_derivative_error,
            error,
        )

        print(
            f"a={mp.nstr(a, 12):>12s} "
            f"gamma={mp.nstr(gamma, 18):>20s} "
            f"relative_error={mp.nstr(error, 10):>16s}"
        )

    if worst_derivative_error > mp.mpf("1e-110"):
        raise AssertionError(
            "Resolvent direct derivative validation failed"
        )

    print("\nEXACT RATIONAL SUSCEPTIBILITY")
    print("=" * 92)

    worst_formula_error = mp.mpf("0")

    for a, gamma in derivative_cases:
        derivative_value = (
            resolvent_susceptibility_from_derivative(
                a,
                gamma,
            )
        )

        exact_value = resolvent_susceptibility_exact(
            a,
            gamma,
        )

        error = relative_error(
            derivative_value,
            exact_value,
        )

        worst_formula_error = max(
            worst_formula_error,
            error,
        )

        print(
            f"a={mp.nstr(a, 12):>12s} "
            f"gamma={mp.nstr(gamma, 18):>20s} "
            f"relative_error={mp.nstr(error, 10):>16s}"
        )

    if worst_formula_error > mp.mpf("1e-120"):
        raise AssertionError(
            "Exact rational susceptibility validation failed"
        )

    print("\nGENERIC SIMILARITY PROFILE")
    print("=" * 92)

    c_values = [
        mp.mpf("0.25"),
        mp.mpf("0.5"),
        mp.mpf("1"),
        mp.mpf("1.5"),
        mp.mpf("2"),
        mp.mpf("3"),
        mp.mpf("5"),
    ]

    gamma_values = [
        mp.mpf("10"),
        mp.mpf("100"),
        mp.mpf("1000"),
    ]

    for c in c_values:
        target = resolvent_profile(c)

        for gamma in gamma_values:
            d = c * gamma
            a = mp.mpf("0.5") + d

            scaled = scaled_resolvent_susceptibility(
                a,
                gamma,
            )

            error = relative_error(
                scaled,
                target,
            )

            print(
                f"c={mp.nstr(c, 8):>8s} "
                f"gamma={mp.nstr(gamma, 8):>8s} "
                f"scaled={mp.nstr(scaled, 20):>26s} "
                f"error={mp.nstr(error, 8):>14s}"
            )

            if error > mp.mpf("1e-120"):
                raise AssertionError(
                    "Exact similarity-scaled profile identity failed"
                )

    print("\nFIXED-a ASYMPTOTIC LAW")
    print("=" * 92)

    a_values = [
        mp.mpf("0.75"),
        mp.mpf("1"),
        mp.mpf("2"),
        mp.mpf("10"),
    ]

    gamma_values = [
        mp.mpf("50"),
        mp.mpf("100"),
        mp.mpf("250"),
        mp.mpf("500"),
        mp.mpf("1000"),
        mp.mpf("2500"),
        mp.mpf("5000"),
        mp.mpf("10000"),
    ]

    for a in a_values:
        target = fixed_a_asymptotic_target(a)
        previous_error = None

        print(
            f"\na={mp.nstr(a, 10)} "
            f"target={mp.nstr(target, 20)}"
        )

        for gamma in gamma_values:
            scaled = fixed_a_scaled_susceptibility(
                a,
                gamma,
            )

            error = abs(
                scaled - target
            )

            print(
                f"gamma={mp.nstr(gamma, 8):>8s} "
                f"gamma^4 chi={mp.nstr(scaled, 22):>28s} "
                f"error={mp.nstr(error, 10):>16s}"
            )

            if previous_error is not None:
                if error >= previous_error:
                    raise AssertionError(
                        "Fixed-a scaled limit failed to converge"
                    )

            previous_error = error

    print("\nEXACT ZERO AT c = sqrt(3)")
    print("=" * 92)

    gamma = mp.mpf("1000")
    c_zero = mp.sqrt(3)
    d = c_zero * gamma
    a = mp.mpf("0.5") + d

    zero_value = resolvent_susceptibility_exact(
        a,
        gamma,
    )

    print(
        "susceptibility at c=sqrt(3): "
        f"{mp.nstr(zero_value, 50)}"
    )

    if abs(zero_value) > mp.mpf("1e-150"):
        raise AssertionError(
            "Resolvent susceptibility zero at sqrt(3) failed"
        )

    epsilon = mp.mpf("1e-6")

    left_c = c_zero - epsilon
    right_c = c_zero + epsilon

    left_value = resolvent_profile(left_c)
    right_value = resolvent_profile(right_c)

    print(
        "profile immediately left of sqrt(3): "
        f"{mp.nstr(left_value, 30)}"
    )

    print(
        "profile immediately right of sqrt(3): "
        f"{mp.nstr(right_value, 30)}"
    )

    if not (
        left_value < 0
        and right_value > 0
    ):
        raise AssertionError(
            "Expected profile sign transition not observed"
        )

    print(
        "\nRESOLVENT NUMERICAL VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
