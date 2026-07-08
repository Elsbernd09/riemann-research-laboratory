"""Arbitrary-precision validation of explicit-formula susceptibility."""

from __future__ import annotations

import mpmath as mp

from src.explicit_formula_susceptibility import (
    amplitude_normalized_susceptibility,
    critical_line_point,
    directional_susceptibility_estimate,
    explicit_formula_second_derivative_factored,
    explicit_formula_second_derivative_numerical,
    explicit_formula_susceptibility,
    scaled_normalized_susceptibility,
)


def relative_error(
    a: mp.mpf | mp.mpc,
    b: mp.mpf | mp.mpc,
) -> mp.mpf:
    denominator = max(
        abs(a),
        abs(b),
        mp.mpf("1e-150"),
    )

    return abs(a - b) / denominator


def main() -> None:
    mp.mp.dps = 140

    cases = [
        (mp.mpf("0.01"), mp.mpf("14.134725141734693790")),
        (mp.mpf("0.05"), mp.mpf("50")),
        (mp.mpf("0.1"), mp.mpf("100")),
        (mp.mpf("0.5"), mp.mpf("250")),
        (mp.mpf("1"), mp.mpf("500")),
    ]

    print("EXPLICIT-FORMULA DIRECT DERIVATIVE CHECK")
    print("=" * 88)

    worst_error = mp.mpf("0")

    for L, gamma in cases:
        rho = critical_line_point(gamma)

        manual = (
            explicit_formula_second_derivative_factored(
                rho,
                L,
            )
        )

        numerical = (
            explicit_formula_second_derivative_numerical(
                rho,
                L,
            )
        )

        error = relative_error(
            manual,
            numerical,
        )

        worst_error = max(
            worst_error,
            error,
        )

        print(
            f"L={mp.nstr(L, 10):>10s} "
            f"gamma={mp.nstr(gamma, 16):>18s} "
            f"relative_error={mp.nstr(error, 10):>16s}"
        )

    print("\nWorst derivative relative error:")
    print(mp.nstr(worst_error, 40))

    if worst_error > mp.mpf("1e-100"):
        raise AssertionError(
            "Explicit-formula direct derivative validation failed"
        )

    print("\nDIRECTIONAL CONTRAST RECOVERY")
    print("=" * 88)

    L = mp.mpf("0.01")
    gamma = mp.mpf("100")

    target = explicit_formula_susceptibility(
        L,
        gamma,
    )

    previous_error = None

    for exponent in range(1, 11):
        delta = mp.mpf(10) ** (-exponent)

        estimate = directional_susceptibility_estimate(
            delta,
            L,
            gamma,
        )

        error = abs(
            estimate - target
        )

        print(
            f"delta=1e-{exponent:<2d} "
            f"estimate={mp.nstr(estimate, 24):>30s} "
            f"error={mp.nstr(error, 10):>16s}"
        )

        if previous_error is not None and exponent <= 8:
            if error >= previous_error:
                raise AssertionError(
                    "Directional susceptibility estimate "
                    "failed to converge in designated range"
                )

        previous_error = error

    print("\nAMPLITUDE NORMALIZATION CHECK")
    print("=" * 88)

    raw = explicit_formula_susceptibility(
        L,
        gamma,
    )

    normalized = amplitude_normalized_susceptibility(
        L,
        gamma,
    )

    reconstructed = (
        mp.exp(L / 2)
        * normalized
    )

    reconstruction_error = relative_error(
        raw,
        reconstructed,
    )

    print(
        "raw susceptibility="
        f"{mp.nstr(raw, 30)}"
    )

    print(
        "normalized susceptibility="
        f"{mp.nstr(normalized, 30)}"
    )

    print(
        "reconstruction relative error="
        f"{mp.nstr(reconstruction_error, 20)}"
    )

    if reconstruction_error > mp.mpf("1e-110"):
        raise AssertionError(
            "Amplitude normalization reconstruction failed"
        )

    print("\nSCALED NORMALIZED VALUE")
    print("=" * 88)

    scaled = scaled_normalized_susceptibility(
        L,
        gamma,
    )

    print(
        "gamma^3 exp(-L/2) chi="
        f"{mp.nstr(scaled, 40)}"
    )

    print(
        "\nEXPLICIT-FORMULA NUMERICAL VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
