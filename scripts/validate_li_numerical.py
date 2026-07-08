"""Arbitrary-precision numerical validation of Li susceptibility."""

from __future__ import annotations

import mpmath as mp

from src.li_susceptibility import (
    critical_line_point,
    finite_delta_quadratic_estimate,
    li_kernel_second_derivative_factored,
    li_kernel_second_derivative_numerical,
    li_susceptibility_exact,
    li_susceptibility_from_derivative,
)


def relative_error(a: mp.mpf | mp.mpc, b: mp.mpf | mp.mpc) -> mp.mpf:
    denominator = max(abs(a), abs(b), mp.mpf("1e-100"))
    return abs(a - b) / denominator


def main() -> None:
    mp.mp.dps = 100

    cases = [
        (1, mp.mpf("14.134725141734693790")),
        (2, mp.mpf("14.134725141734693790")),
        (5, mp.mpf("21.022039638771554993")),
        (20, mp.mpf("50")),
        (100, mp.mpf("100")),
        (500, mp.mpf("250")),
    ]

    print("ARBITRARY-PRECISION DIRECT DERIVATIVE CHECK")
    print("=" * 72)

    worst_derivative_error = mp.mpf("0")
    worst_formula_error = mp.mpf("0")

    for n, gamma in cases:
        rho = critical_line_point(gamma)

        manual = li_kernel_second_derivative_factored(rho, n)
        numerical = li_kernel_second_derivative_numerical(rho, n)

        chi_derivative = li_susceptibility_from_derivative(n, gamma)
        chi_exact = li_susceptibility_exact(n, gamma)

        derivative_error = relative_error(manual, numerical)
        formula_error = relative_error(chi_derivative, chi_exact)

        worst_derivative_error = max(
            worst_derivative_error,
            derivative_error,
        )

        worst_formula_error = max(
            worst_formula_error,
            formula_error,
        )

        print(
            f"n={n:<4d} gamma={mp.nstr(gamma, 12):>14s} "
            f"derivative_rel_error={mp.nstr(derivative_error, 5):>12s} "
            f"chi_rel_error={mp.nstr(formula_error, 5):>12s}"
        )

    print("\nWorst direct derivative relative error:")
    print(mp.nstr(worst_derivative_error, 20))

    print("\nWorst exact-formula relative error:")
    print(mp.nstr(worst_formula_error, 20))

    if worst_derivative_error > mp.mpf("1e-70"):
        raise AssertionError(
            "Direct derivative validation failed precision threshold"
        )

    if worst_formula_error > mp.mpf("1e-70"):
        raise AssertionError(
            "Exact susceptibility formula failed precision threshold"
        )

    print("\nFINITE-DELTA QUADRATIC CONVERGENCE")
    print("=" * 72)

    n = 100
    gamma = mp.mpf("100")
    target = li_susceptibility_exact(n, gamma)

    previous_error = None

    for exponent in range(1, 13):
        delta = mp.mpf(10) ** (-exponent)
        estimate = finite_delta_quadratic_estimate(
            delta,
            gamma,
            n,
        )
        error = abs(estimate - target)

        print(
            f"delta=1e-{exponent:<2d} "
            f"estimate={mp.nstr(estimate, 16):>22s} "
            f"abs_error={mp.nstr(error, 8):>14s}"
        )

        if previous_error is not None and exponent <= 8:
            if error >= previous_error:
                raise AssertionError(
                    "Finite-delta error failed to decrease "
                    "in the pre-roundoff convergence range"
                )

        previous_error = error

    print("\nNUMERICAL SUSCEPTIBILITY VALIDATION: PASS")


if __name__ == "__main__":
    main()
