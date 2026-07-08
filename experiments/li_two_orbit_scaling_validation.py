"""Direct nonresonant-versus-resonant two-orbit Li response validation."""

from __future__ import annotations

import mpmath as mp

from src.li_susceptibility import (
    li_blind_scale,
    li_resonant_height_ratio,
    li_two_orbit_aggregate_profile,
    li_two_orbit_aggregate_susceptibility,
    li_two_orbit_resonant_correction,
)


def main() -> None:
    mp.mp.dps = 180

    c_0 = li_blind_scale(0)

    n_values = [
        1000,
        2500,
        5000,
        10000,
        25000,
        50000,
        100000,
        250000,
        500000,
    ]

    print("NONRESONANT TWO-ORBIT RESTORATION")
    print("=" * 100)

    a_nonresonant = mp.mpf("2")

    target_nonresonant = (
        li_two_orbit_aggregate_profile(
            c_0,
            a_nonresonant,
        )
    )

    print(
        "a="
        f"{mp.nstr(a_nonresonant, 30)}"
    )

    print(
        "Gamma^2 aggregate target="
        f"{mp.nstr(target_nonresonant, 40)}"
    )

    previous_error = None

    for n in n_values:
        Gamma = mp.mpf(n) / c_0

        aggregate = (
            li_two_orbit_aggregate_susceptibility(
                n,
                Gamma,
                a_nonresonant,
            )
        )

        scaled = Gamma**2 * aggregate

        error = abs(
            scaled - target_nonresonant
        )

        print(
            f"n={n:<8d} "
            f"Gamma={mp.nstr(Gamma, 14):>18s} "
            f"Gamma^2X={mp.nstr(scaled, 24):>30s} "
            f"error={mp.nstr(error, 10):>16s}"
        )

        if n >= 10000:
            if previous_error is not None:
                if error >= previous_error:
                    raise AssertionError(
                        "Nonresonant Gamma^-2 restoration "
                        "failed to converge"
                    )

            previous_error = error

    print("\nRESONANT TWO-ORBIT FOURTH-ORDER LAW")
    print("=" * 100)

    a_resonant = li_resonant_height_ratio(
        0,
        1,
    )

    target_resonant = (
        li_two_orbit_resonant_correction(
            0,
            1,
        )
    )

    print(
        "a=c_0/c_1="
        f"{mp.nstr(a_resonant, 50)}"
    )

    print(
        "Gamma^4 aggregate target="
        f"{mp.nstr(target_resonant, 40)}"
    )

    previous_error = None

    for n in n_values:
        Gamma = mp.mpf(n) / c_0

        aggregate = (
            li_two_orbit_aggregate_susceptibility(
                n,
                Gamma,
                a_resonant,
            )
        )

        scaled = Gamma**4 * aggregate

        error = abs(
            scaled - target_resonant
        )

        print(
            f"n={n:<8d} "
            f"Gamma={mp.nstr(Gamma, 14):>18s} "
            f"Gamma^4X={mp.nstr(scaled, 24):>30s} "
            f"error={mp.nstr(error, 10):>16s}"
        )

        if n >= 10000:
            if previous_error is not None:
                if error >= previous_error:
                    raise AssertionError(
                        "Resonant Gamma^-4 law "
                        "failed to converge"
                    )

            previous_error = error

    print(
        "\nLI TWO-ORBIT SCALING VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
