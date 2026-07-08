"""Validate asymptotic relative cancellation for adjacent blind scales."""

from __future__ import annotations

import mpmath as mp

from src.li_susceptibility import (
    li_blind_scale,
    li_resonant_cancellation_ratio,
    li_two_orbit_resonant_correction,
)


def main() -> None:
    mp.mp.dps = 120

    k_values = [
        10,
        20,
        50,
        100,
        200,
        500,
        1000,
    ]

    print("ADJACENT RESONANCE ASYMPTOTICS")
    print("=" * 100)

    previous_ratio = None

    for k in k_values:
        c_k = li_blind_scale(k)

        ratio = li_resonant_cancellation_ratio(
            k,
            k + 1,
        )

        relative_scaled = (
            ratio
            * 2
            * c_k
            / (7 * mp.pi)
        )

        coefficient = abs(
            li_two_orbit_resonant_correction(
                k,
                k + 1,
            )
        )

        absolute_scaled = (
            coefficient
            * 6
            / (
                7
                * mp.pi
                * c_k**2
            )
        )

        print(
            f"k={k:<5d} "
            f"R={mp.nstr(ratio, 16):>20s} "
            f"R/(7pi/2c)={mp.nstr(relative_scaled, 16):>20s} "
            f"|Kagg|={mp.nstr(coefficient, 16):>22s} "
            f"K/(7pi c^2/6)={mp.nstr(absolute_scaled, 16):>20s}"
        )

        if previous_ratio is not None:
            if ratio >= previous_ratio:
                raise AssertionError(
                    "Adjacent relative cancellation ratio "
                    "did not decrease"
                )

        previous_ratio = ratio

    if abs(
        relative_scaled - 1
    ) > mp.mpf("0.01"):
        raise AssertionError(
            "Relative cancellation asymptotic failed"
        )

    if abs(
        absolute_scaled - 1
    ) > mp.mpf("0.01"):
        raise AssertionError(
            "Absolute coefficient asymptotic failed"
        )

    print(
        "\nADJACENT RESONANCE ASYMPTOTIC VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
