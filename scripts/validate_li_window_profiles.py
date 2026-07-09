"""Validate the closed and integral forms of the Li window profiles."""

from __future__ import annotations

import mpmath as mp

from src.li_susceptibility import (
    li_susceptibility_profile,
    li_window_continuum_profile,
    li_window_finite_height_profile,
)


def integral_leading_profile(
    c: mp.mpf,
    eta: mp.mpf,
) -> mp.mpf:
    return (
        mp.quad(
            lambda u: (
                u**(-2)
                * li_susceptibility_profile(
                    c / u
                )
            ),
            [
                mp.mpf("1"),
                1 + eta,
            ],
        )
        /
        (2 * mp.pi)
    )


def main() -> None:
    mp.mp.dps = 100

    eta_values = [
        mp.mpf("0.05"),
        mp.mpf("0.1"),
        mp.mpf("0.2"),
        mp.mpf("0.5"),
    ]

    c_values = [
        mp.mpf("0.5"),
        mp.mpf("1"),
        mp.mpf("2.288929728103404"),
        mp.mpf("5"),
        mp.mpf("10"),
        mp.mpf("20"),
    ]

    print("LI WINDOW PROFILE VALIDATION")
    print("=" * 100)

    for eta in eta_values:
        for c in c_values:
            closed = (
                li_window_continuum_profile(
                    c,
                    eta,
                )
            )

            integral = (
                integral_leading_profile(
                    c,
                    eta,
                )
            )

            denominator = max(
                abs(closed),
                abs(integral),
                mp.mpf("1e-90"),
            )

            relative_error = abs(
                closed - integral
            ) / denominator

            if relative_error > mp.mpf("1e-80"):
                raise AssertionError(
                    "Closed window profile failed "
                    f"for c={c}, eta={eta}"
                )

    print(
        "Closed profile versus integral form: PASS"
    )

    c = mp.mpf("2.5")

    eta_values_small = [
        mp.mpf("0.1"),
        mp.mpf("0.05"),
        mp.mpf("0.02"),
        mp.mpf("0.01"),
        mp.mpf("0.005"),
        mp.mpf("0.002"),
    ]

    target = (
        li_susceptibility_profile(c)
        /
        (2 * mp.pi)
    )

    previous_error = None

    print()
    print("NARROW-WINDOW CONSISTENCY")

    for eta in eta_values_small:
        scaled = (
            li_window_continuum_profile(
                c,
                eta,
            )
            /
            eta
        )

        error = abs(
            scaled - target
        )

        print(
            f"eta={mp.nstr(eta, 8):>10s} "
            f"Phi/eta={mp.nstr(scaled, 24):>30s} "
            f"error={mp.nstr(error, 10):>16s}"
        )

        if previous_error is not None:
            if error >= previous_error:
                raise AssertionError(
                    "Narrow-window consistency "
                    "failed to converge"
                )

        previous_error = error

    # Finite-height profile must approach the frozen leading profile.
    eta = mp.mpf("0.2")
    c = mp.mpf("5")

    frozen = li_window_continuum_profile(
        c,
        eta,
    )

    H_values = [
        mp.mpf("1e3"),
        mp.mpf("1e5"),
        mp.mpf("1e10"),
        mp.mpf("1e20"),
        mp.mpf("1e50"),
    ]

    previous_error = None

    print()
    print("FINITE-HEIGHT PROFILE APPROACH")

    for H in H_values:
        finite_height = (
            li_window_finite_height_profile(
                c,
                eta,
                H,
            )
        )

        error = abs(
            finite_height - frozen
        )

        print(
            f"H={mp.nstr(H, 8):>12s} "
            f"FH={mp.nstr(finite_height, 24):>30s} "
            f"error={mp.nstr(error, 10):>16s}"
        )

        if previous_error is not None:
            if error >= previous_error:
                raise AssertionError(
                    "Finite-height profile did not "
                    "approach frozen leading profile"
                )

        previous_error = error

    print()
    print(
        "LI WINDOW PROFILE VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
