"""Validate the exact matched Li blind-scale gamma^-4 law."""

from __future__ import annotations

import mpmath as mp

from src.li_susceptibility import (
    li_blind_scale,
    li_blind_scale_correction,
    li_susceptibility_exact,
)


def main() -> None:
    mp.mp.dps = 180

    n_values = [
        100,
        250,
        500,
        1000,
        2500,
        5000,
        10000,
        25000,
        50000,
        100000,
    ]

    print("EXACT MATCHED LI BLIND-SCALE RESPONSE")
    print("=" * 100)

    for k in range(4):
        c_k = li_blind_scale(k)
        target = li_blind_scale_correction(k)

        print(
            f"\nk={k} "
            f"c_k={mp.nstr(c_k, 30)}"
        )

        print(
            "gamma^4 chi target="
            f"{mp.nstr(target, 40)}"
        )

        previous_error = None

        for n in n_values:
            gamma = mp.mpf(n) / c_k

            susceptibility = li_susceptibility_exact(
                n,
                gamma,
            )

            scaled = (
                gamma**4
                * susceptibility
            )

            error = abs(
                scaled - target
            )

            print(
                f"n={n:<7d} "
                f"gamma={mp.nstr(gamma, 14):>18s} "
                f"gamma^4chi={mp.nstr(scaled, 24):>30s} "
                f"error={mp.nstr(error, 10):>16s}"
            )

            if previous_error is not None:
                if error >= previous_error:
                    raise AssertionError(
                        "Exact blind-scale gamma^-4 law "
                        f"failed to converge for k={k}"
                    )

            previous_error = error

    print(
        "\nEXACT LI BLIND-SCALE ASYMPTOTIC VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
