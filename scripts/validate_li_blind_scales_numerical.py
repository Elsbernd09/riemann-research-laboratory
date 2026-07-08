"""High-precision validation of Li response-profile blind scales."""

from __future__ import annotations

import mpmath as mp

from src.li_susceptibility import (
    li_blind_scale,
    li_blind_scale_asymptotic,
    li_susceptibility_profile,
)


def main() -> None:
    mp.mp.dps = 140

    print("LI QUADRATIC-RESPONSE BLIND SCALES")
    print("=" * 96)

    previous_scaled_asymptotic_error = None

    for k in range(0, 51):
        root = li_blind_scale(k)

        left = (
            (mp.mpf(k) + mp.mpf("0.5"))
            * mp.pi
        )

        right = (
            (mp.mpf(k) + 1)
            * mp.pi
        )

        profile_value = li_susceptibility_profile(
            root
        )

        asymptotic = li_blind_scale_asymptotic(
            k
        )

        asymptotic_error = abs(
            root - asymptotic
        )

        a_k = left

        scaled_asymptotic_error = (
            asymptotic_error
            * a_k**5
        )

        if not (
            left < root < right
        ):
            raise AssertionError(
                f"Blind scale k={k} left predicted interval"
            )

        if abs(profile_value) > mp.mpf("1e-120"):
            raise AssertionError(
                f"Profile root validation failed for k={k}"
            )

        if k <= 10 or k in [20, 30, 40, 50]:
            print(
                f"k={k:<2d} "
                f"c_k={mp.nstr(root, 30):>34s} "
                f"|Psi|={mp.nstr(abs(profile_value), 8):>14s} "
                f"asym_error={mp.nstr(asymptotic_error, 10):>16s} "
                f"a_k^5 error={mp.nstr(scaled_asymptotic_error, 12):>18s}"
            )

        # The three-term approximation is asymptotic, not expected to
        # improve monotonically for the first few roots.
        if k >= 10:
            if previous_scaled_asymptotic_error is not None:
                relative_change = abs(
                    scaled_asymptotic_error
                    -
                    previous_scaled_asymptotic_error
                ) / max(
                    abs(scaled_asymptotic_error),
                    abs(previous_scaled_asymptotic_error),
                    mp.mpf("1e-140"),
                )

                # a_k^5 * error should remain bounded and settle toward
                # the next asymptotic coefficient.
                if scaled_asymptotic_error > mp.mpf("100"):
                    raise AssertionError(
                        "Root asymptotic does not exhibit O(a_k^-5) "
                        "behavior"
                    )

            previous_scaled_asymptotic_error = (
                scaled_asymptotic_error
            )

    print("\nFirst five blind scales:")

    for k in range(5):
        print(
            f"c_{k} = "
            f"{mp.nstr(li_blind_scale(k), 50)}"
        )

    print(
        "\nLI BLIND-SCALE ROOT VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
