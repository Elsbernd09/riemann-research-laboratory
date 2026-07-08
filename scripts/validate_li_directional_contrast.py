"""High-precision validation of Li horizontal-vertical contrast."""

from __future__ import annotations

import mpmath as mp

from src.li_susceptibility import (
    finite_delta_quadratic_estimate,
    horizontal_configuration_sum,
    horizontal_vertical_contrast,
    li_susceptibility_exact,
    sixth_order_contrast_coefficient,
    vertical_configuration_sum,
)


def relative_error(a: mp.mpf, b: mp.mpf) -> mp.mpf:
    denominator = max(
        abs(a),
        abs(b),
        mp.mpf("1e-150"),
    )
    return abs(a - b) / denominator


def main() -> None:
    mp.mp.dps = 160

    cases = [
        (1, mp.mpf("14.134725141734693790")),
        (5, mp.mpf("14.134725141734693790")),
        (20, mp.mpf("50")),
        (100, mp.mpf("100")),
        (500, mp.mpf("250")),
    ]

    print("HORIZONTAL-VERTICAL DIRECTIONAL CONTRAST")
    print("=" * 96)

    for n, gamma in cases:
        chi = li_susceptibility_exact(n, gamma)

        print(
            f"\nn={n} gamma={mp.nstr(gamma, 18)} "
            f"chi={mp.nstr(chi, 22)}"
        )

        previous_quadratic_error = None

        for exponent in range(1, 9):
            delta = mp.mpf(10) ** (-exponent)

            contrast = horizontal_vertical_contrast(
                delta,
                gamma,
                n,
            )

            estimate = contrast / (2 * delta**2)

            quadratic_error = abs(estimate - chi)

            print(
                f"delta=1e-{exponent:<2d} "
                f"contrast/(2d^2)={mp.nstr(estimate, 20):>26s} "
                f"abs_error={mp.nstr(quadratic_error, 10):>16s}"
            )

            if previous_quadratic_error is not None:
                if quadratic_error >= previous_quadratic_error:
                    raise AssertionError(
                        "Directional contrast failed to converge "
                        "toward susceptibility"
                    )

            previous_quadratic_error = quadratic_error

    print("\nOLD SIGNED RESPONSE VERSUS HORIZONTAL RESPONSE")
    print("=" * 96)

    n = 100
    gamma = mp.mpf("100")

    for exponent in range(1, 7):
        delta = mp.mpf(10) ** (-exponent)

        old_estimate = finite_delta_quadratic_estimate(
            delta,
            gamma,
            n,
        )

        horizontal_sum = horizontal_configuration_sum(
            delta,
            gamma,
            n,
        )

        center_pair_sum = (
            horizontal_configuration_sum(
                mp.mpf("1e-40"),
                gamma,
                n,
            )
        )

        chi = li_susceptibility_exact(n, gamma)

        print(
            f"delta=1e-{exponent:<2d} "
            f"old_signed_est={mp.nstr(old_estimate, 18):>23s} "
            f"chi={mp.nstr(chi, 18):>23s}"
        )

    print("\nSIXTH-ORDER ERROR LAW")
    print("=" * 96)

    sixth_target = sixth_order_contrast_coefficient(
        n,
        gamma,
    )

    print(
        "Expected limit of "
        "(A - 2 delta^2 chi) / delta^6:"
    )
    print(mp.nstr(sixth_target, 40))

    previous_sixth_error = None

    for exponent in range(1, 8):
        delta = mp.mpf(10) ** (-exponent)

        contrast = horizontal_vertical_contrast(
            delta,
            gamma,
            n,
        )

        residual = (
            contrast
            -
            2 * delta**2 * chi
        )

        scaled_residual = residual / delta**6

        error = abs(
            scaled_residual
            -
            sixth_target
        )

        print(
            f"delta=1e-{exponent:<2d} "
            f"scaled_residual={mp.nstr(scaled_residual, 24):>30s} "
            f"error={mp.nstr(error, 10):>16s}"
        )

        if previous_sixth_error is not None and exponent <= 5:
            if error >= previous_sixth_error:
                raise AssertionError(
                    "Sixth-order scaled residual failed to converge "
                    "in the designated range"
                )

        previous_sixth_error = error

    print(
        "\nLI DIRECTIONAL CONTRAST VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
