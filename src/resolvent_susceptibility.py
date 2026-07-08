"""Resolvent zero-kernel susceptibility.

The individual kernel is

    r_a(z) = 1 / (a - z)

for real a > 1/2.
"""

from __future__ import annotations

from typing import Union

import mpmath as mp


Number = Union[int, float, mp.mpf]


def validate_a(a: Number) -> mp.mpf:
    a_mp = mp.mpf(a)

    if a_mp <= mp.mpf("0.5"):
        raise ValueError("a must satisfy a > 1/2")

    return a_mp


def validate_gamma(gamma: Number) -> mp.mpf:
    gamma_mp = mp.mpf(gamma)

    if gamma_mp <= 0:
        raise ValueError("gamma must satisfy gamma > 0")

    return gamma_mp


def resolvent_kernel(
    z: mp.mpc,
    a: Number,
) -> mp.mpc:
    """Return r_a(z) = 1 / (a - z)."""
    a_mp = validate_a(a)
    z = mp.mpc(z)

    denominator = a_mp - z

    if denominator == 0:
        raise ZeroDivisionError(
            "Resolvent kernel is singular at z = a"
        )

    return 1 / denominator


def resolvent_second_derivative_factored(
    z: mp.mpc,
    a: Number,
) -> mp.mpc:
    """Return the manually derived second derivative."""
    a_mp = validate_a(a)
    z = mp.mpc(z)

    denominator = a_mp - z

    if denominator == 0:
        raise ZeroDivisionError(
            "Resolvent kernel is singular at z = a"
        )

    return 2 / denominator**3


def resolvent_second_derivative_numerical(
    z: mp.mpc,
    a: Number,
) -> mp.mpc:
    """Numerically differentiate the original kernel twice."""
    a_mp = validate_a(a)
    z = mp.mpc(z)

    return mp.diff(
        lambda w: resolvent_kernel(w, a_mp),
        z,
        2,
    )


def critical_line_point(gamma: Number) -> mp.mpc:
    """Return rho_gamma = 1/2 + i gamma."""
    gamma_mp = validate_gamma(gamma)

    return mp.mpc(
        mp.mpf("0.5"),
        gamma_mp,
    )


def resolvent_susceptibility_from_derivative(
    a: Number,
    gamma: Number,
) -> mp.mpf:
    """Return 2 Re r_a''(rho_gamma)."""
    a_mp = validate_a(a)
    rho = critical_line_point(gamma)

    return 2 * mp.re(
        resolvent_second_derivative_factored(
            rho,
            a_mp,
        )
    )


def resolvent_susceptibility_exact(
    a: Number,
    gamma: Number,
) -> mp.mpf:
    """Return the exact real rational susceptibility formula."""
    a_mp = validate_a(a)
    gamma_mp = validate_gamma(gamma)

    d = a_mp - mp.mpf("0.5")

    return (
        4
        * d
        * (d**2 - 3 * gamma_mp**2)
        /
        (d**2 + gamma_mp**2) ** 3
    )


def resolvent_similarity_coordinate(
    a: Number,
    gamma: Number,
) -> mp.mpf:
    """Return (a - 1/2) / gamma."""
    a_mp = validate_a(a)
    gamma_mp = validate_gamma(gamma)

    return (
        a_mp - mp.mpf("0.5")
    ) / gamma_mp


def resolvent_profile(c: Number) -> mp.mpf:
    """Return Psi_Res(c)."""
    c_mp = mp.mpf(c)

    if c_mp <= 0:
        raise ValueError("c must satisfy c > 0")

    return (
        4
        * c_mp
        * (c_mp**2 - 3)
        /
        (c_mp**2 + 1) ** 3
    )


def scaled_resolvent_susceptibility(
    a: Number,
    gamma: Number,
) -> mp.mpf:
    """Return gamma^3 chi_a^Res(gamma)."""
    gamma_mp = validate_gamma(gamma)

    return (
        gamma_mp**3
        * resolvent_susceptibility_exact(
            a,
            gamma_mp,
        )
    )


def fixed_a_scaled_susceptibility(
    a: Number,
    gamma: Number,
) -> mp.mpf:
    """Return gamma^4 chi_a^Res(gamma)."""
    gamma_mp = validate_gamma(gamma)

    return (
        gamma_mp**4
        * resolvent_susceptibility_exact(
            a,
            gamma_mp,
        )
    )


def fixed_a_asymptotic_target(
    a: Number,
) -> mp.mpf:
    """Return -12(a - 1/2)."""
    a_mp = validate_a(a)

    return -12 * (
        a_mp - mp.mpf("0.5")
    )
