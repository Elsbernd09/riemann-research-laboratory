"""Arbitrary-precision validation of reflection-mediated orbit response."""

from __future__ import annotations

import mpmath as mp

from src.li_susceptibility import (
    li_inverse_phase_kernel,
    li_kernel,
    reflected_li_kernel,
    reflection_invariant_derivative_response,
    reflection_invariant_zero_response,
)


def relative_error(
    a: mp.mpc | mp.mpf,
    b: mp.mpc | mp.mpf,
) -> mp.mpf:
    denominator = max(
        abs(a),
        abs(b),
        mp.mpf("1e-100"),
    )
    return abs(a - b) / denominator


def main() -> None:
    mp.mp.dps = 120

    print("POINTWISE REFLECTION IDENTITY")
    print("=" * 80)

    point_cases = [
        mp.mpc("0.2", "1.7"),
        mp.mpc("0.7", "14.134725141734693790"),
        mp.mpc("-2.5", "8"),
        mp.mpc("3.25", "-4.75"),
    ]

    n_cases = [1, 2, 5, 20, 100]

    worst_point_error = mp.mpf("0")

    for z in point_cases:
        for n in n_cases:
            inverse_value = li_inverse_phase_kernel(z, n)
            reflected_value = reflected_li_kernel(z, n)

            error = relative_error(
                inverse_value,
                reflected_value,
            )

            worst_point_error = max(
                worst_point_error,
                error,
            )

            print(
                f"z={mp.nstr(z, 18):>28s} "
                f"n={n:<3d} "
                f"rel_error={mp.nstr(error, 8):>14s}"
            )

    if worst_point_error > mp.mpf("1e-90"):
        raise AssertionError(
            "Pointwise reflection identity failed precision threshold"
        )

    print("\nREFLECTION-INVARIANT ORBIT RESPONSE")
    print("=" * 80)

    orbit_cases = [
        (mp.mpf("1e-3"), mp.mpf("14.134725141734693790"), 1),
        (mp.mpf("0.05"), mp.mpf("14.134725141734693790"), 5),
        (mp.mpf("0.1"), mp.mpf("50"), 20),
        (mp.mpf("0.2"), mp.mpf("100"), 100),
        (mp.mpf("0.3"), mp.mpf("250"), 500),
    ]

    worst_orbit_error = mp.mpf("0")

    for delta, gamma, n in orbit_cases:
        zero_response = reflection_invariant_zero_response(
            delta,
            gamma,
            n,
        )

        derivative_response = (
            reflection_invariant_derivative_response(
                delta,
                gamma,
                n,
            )
        )

        error = relative_error(
            zero_response,
            derivative_response,
        )

        worst_orbit_error = max(
            worst_orbit_error,
            error,
        )

        print(
            f"delta={mp.nstr(delta, 8):>8s} "
            f"gamma={mp.nstr(gamma, 14):>16s} "
            f"n={n:<4d} "
            f"rel_error={mp.nstr(error, 8):>14s}"
        )

    print("\nWorst pointwise reflection relative error:")
    print(mp.nstr(worst_point_error, 30))

    print("\nWorst orbit-response relative error:")
    print(mp.nstr(worst_orbit_error, 30))

    if worst_orbit_error > mp.mpf("1e-90"):
        raise AssertionError(
            "Reflection-invariant orbit response identity failed"
        )

    print(
        "\nREFLECTION-MEDIATED ORBIT RESPONSE VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
