"""Li-kernel signed quadratic susceptibility.

This module implements the individual Li zero kernel

    f_n(z) = 1 - (1 - 1/z)^n

and several mathematically independent representations of its
second derivative and critical-line susceptibility.

No function in this module claims to evaluate a full Li coefficient.
"""

from __future__ import annotations

from typing import Union

import mpmath as mp


Number = Union[int, float, mp.mpf]


def validate_n(n: int) -> None:
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 1:
        raise ValueError("n must satisfy n >= 1")


def validate_gamma(gamma: Number) -> mp.mpf:
    gamma_mp = mp.mpf(gamma)
    if gamma_mp <= 0:
        raise ValueError("gamma must satisfy gamma > 0")
    return gamma_mp


def li_kernel(z: mp.mpc, n: int) -> mp.mpc:
    """Return f_n(z) = 1 - (1 - 1/z)^n."""
    validate_n(n)
    z = mp.mpc(z)

    if z == 0:
        raise ZeroDivisionError("Li kernel is singular at z = 0")

    return 1 - (1 - 1 / z) ** n


def li_kernel_second_derivative_factored(
    z: mp.mpc,
    n: int,
) -> mp.mpc:
    """Return the manually derived factored formula for f_n''(z)."""
    validate_n(n)
    z = mp.mpc(z)

    if z == 0:
        raise ZeroDivisionError("Li kernel is singular at z = 0")

    return (
        n
        * (1 - 1 / z) ** (n - 2)
        * (2 * z - n - 1)
        / z**4
    )


def li_kernel_second_derivative_numerical(
    z: mp.mpc,
    n: int,
) -> mp.mpc:
    """Differentiate the original kernel numerically using mpmath."""
    validate_n(n)
    z = mp.mpc(z)

    if z == 0:
        raise ZeroDivisionError("Li kernel is singular at z = 0")

    return mp.diff(lambda w: li_kernel(w, n), z, 2)


def critical_line_point(gamma: Number) -> mp.mpc:
    """Return rho_gamma = 1/2 + i gamma."""
    gamma_mp = validate_gamma(gamma)
    return mp.mpc(mp.mpf("0.5"), gamma_mp)


def theta_gamma(gamma: Number) -> mp.mpf:
    """Return theta_gamma = 2 atan(1 / (2 gamma))."""
    gamma_mp = validate_gamma(gamma)
    return 2 * mp.atan(1 / (2 * gamma_mp))


def li_susceptibility_from_derivative(
    n: int,
    gamma: Number,
) -> mp.mpf:
    """Return chi = 2 Re f_n''(1/2 + i gamma)."""
    validate_n(n)
    rho = critical_line_point(gamma)

    value = li_kernel_second_derivative_factored(rho, n)
    return 2 * mp.re(value)


def li_susceptibility_exact(
    n: int,
    gamma: Number,
) -> mp.mpf:
    """Return the exact trigonometric susceptibility formula."""
    validate_n(n)
    gamma_mp = validate_gamma(gamma)

    theta = theta_gamma(gamma_mp)
    denominator = (gamma_mp**2 + mp.mpf("0.25")) ** 2

    bracket = (
        n * mp.cos(n * theta)
        + 2 * gamma_mp * mp.sin(n * theta)
    )

    return -(2 * n / denominator) * bracket


def signed_orbit_response(
    delta: Number,
    gamma: Number,
    n: int,
) -> mp.mpf:
    """Return the signed double-orbit splitting response.

    R_f(delta, gamma) =
        sum_{eps=+-1, eta=+-1}
        f(1/2 + eps delta + i eta gamma)
        -
        2 sum_{eta=+-1}
        f(1/2 + i eta gamma).
    """
    validate_n(n)
    gamma_mp = validate_gamma(gamma)
    delta_mp = mp.mpf(delta)

    total = mp.mpc(0)

    for epsilon in (-1, 1):
        for eta in (-1, 1):
            z = mp.mpc(
                mp.mpf("0.5") + epsilon * delta_mp,
                eta * gamma_mp,
            )
            total += li_kernel(z, n)

    for eta in (-1, 1):
        z = mp.mpc(mp.mpf("0.5"), eta * gamma_mp)
        total -= 2 * li_kernel(z, n)

    imaginary_residual = abs(mp.im(total))

    tolerance = mp.mpf(10) ** (-(mp.mp.dps // 2))
    if imaginary_residual > tolerance:
        raise ArithmeticError(
            "Signed response should be real under conjugation symmetry; "
            f"imaginary residual={imaginary_residual}"
        )

    return mp.re(total)


def finite_delta_quadratic_estimate(
    delta: Number,
    gamma: Number,
    n: int,
) -> mp.mpf:
    """Return R_f(delta, gamma) / delta^2."""
    delta_mp = mp.mpf(delta)

    if delta_mp == 0:
        raise ValueError("delta must be nonzero")

    return signed_orbit_response(delta_mp, gamma, n) / delta_mp**2


def li_mesoscopic_profile(c: Number) -> mp.mpf:
    """Return Psi_Li(c) = -2 c (c cos c + 2 sin c)."""
    c_mp = mp.mpf(c)

    if c_mp <= 0:
        raise ValueError("c must satisfy c > 0")

    return -2 * c_mp * (
        c_mp * mp.cos(c_mp)
        + 2 * mp.sin(c_mp)
    )


def scaled_li_susceptibility(
    n: int,
    gamma: Number,
) -> mp.mpf:
    """Return gamma^2 chi_n^Li(gamma)."""
    gamma_mp = validate_gamma(gamma)

    return gamma_mp**2 * li_susceptibility_exact(n, gamma_mp)
