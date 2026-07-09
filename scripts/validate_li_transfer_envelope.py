"""Validate J_Li and matched-scale transfer-envelope convergence."""

from __future__ import annotations

import mpmath as mp

from src.li_susceptibility import (
    li_continuum_transfer_envelope,
    li_derivative_response_profile,
    li_susceptibility_exact,
    li_susceptibility_gamma_derivative,
    li_susceptibility_profile,
)


def exact_lambda(
    n: int,
    H: mp.mpf,
    eta: mp.mpf,
) -> mp.mpf:
    B = (
        (1 + eta) * H
    )

    return (
        abs(
            li_susceptibility_exact(
                n,
                H,
            )
        )
        +
        abs(
            li_susceptibility_exact(
                n,
                B,
            )
        )
        +
        mp.quad(
            lambda t: abs(
                li_susceptibility_gamma_derivative(
                    n,
                    t,
                )
            ),
            [
                H,
                B,
            ],
        )
    )


def main() -> None:
    mp.mp.dps = 100

    print("LI TRANSFER-ENVELOPE VALIDATION")
    print("=" * 100)

    q_values = [
        mp.mpf("0.5"),
        mp.mpf("1"),
        mp.mpf("2.5"),
        mp.mpf("5"),
        mp.mpf("10"),
        mp.mpf("20"),
    ]

    print("DERIVATIVE-RESPONSE PROFILE")

    for q in q_values:
        closed = (
            li_derivative_response_profile(
                q
            )
        )

        numerical = (
            2
            * li_susceptibility_profile(q)
            +
            q
            * mp.diff(
                li_susceptibility_profile,
                q,
            )
        )

        denominator = max(
            abs(closed),
            abs(numerical),
            mp.mpf("1e-90"),
        )

        relative_error = (
            abs(closed - numerical)
            /
            denominator
        )

        print(
            f"q={mp.nstr(q, 8):>8s} "
            f"J={mp.nstr(closed, 24):>30s} "
            f"relerr={mp.nstr(relative_error, 8):>14s}"
        )

        if relative_error > mp.mpf(
            "1e-80"
        ):
            raise AssertionError(
                "J_Li validation failed"
            )

    print()
    print(
        "J_Li explicit formula: PASS"
    )

    cases = [
        (
            mp.mpf("2.5"),
            mp.mpf("0.1"),
        ),
        (
            mp.mpf("5"),
            mp.mpf("0.2"),
        ),
        (
            mp.mpf("10"),
            mp.mpf("0.5"),
        ),
    ]

    H_values = [
        mp.mpf("1e2"),
        mp.mpf("5e2"),
        mp.mpf("1e3"),
        mp.mpf("5e3"),
        mp.mpf("1e4"),
        mp.mpf("5e4"),
        mp.mpf("1e5"),
    ]

    print()
    print(
        "MATCHED-SCALE TRANSFER CONVERGENCE"
    )

    for c, eta in cases:
        target = (
            li_continuum_transfer_envelope(
                c,
                eta,
            )
        )

        previous_error = None

        print()
        print(
            f"c={mp.nstr(c, 8)} "
            f"eta={mp.nstr(eta, 8)} "
            f"target={mp.nstr(target, 30)}"
        )

        for H in H_values:
            n = max(
                1,
                int(
                    mp.nint(
                        c * H
                    )
                ),
            )

            scaled = (
                H**2
                * exact_lambda(
                    n,
                    H,
                    eta,
                )
            )

            error = abs(
                scaled - target
            )

            print(
                f"H={mp.nstr(H, 8):>12s} "
                f"H^2Lambda={mp.nstr(scaled, 24):>30s} "
                f"error={mp.nstr(error, 10):>16s}"
            )

            if H >= mp.mpf("1e3"):
                if previous_error is not None:
                    if error >= previous_error:
                        raise AssertionError(
                            "Transfer-envelope convergence "
                            "failed monotonic validation"
                        )

                previous_error = error

        if previous_error is None:
            raise AssertionError(
                "No asymptotic validation points"
            )

        if (
            previous_error
            /
            max(
                abs(target),
                mp.mpf("1e-90"),
            )
            >
            mp.mpf("1e-7")
        ):
            raise AssertionError(
                "Transfer-envelope terminal relative error "
                "exceeded tolerance"
            )

    print()
    print(
        "LI TRANSFER-ENVELOPE VALIDATION: PASS"
    )


if __name__ == "__main__":
    main()
