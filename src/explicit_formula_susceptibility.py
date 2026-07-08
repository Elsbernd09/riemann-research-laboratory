"""Explicit-formula zero-kernel susceptibility.

This module studies the individual kernel

    p_L(z) = -exp(L z) / z

associated with the standard zero contribution -x^rho / rho,
where L = log(x) > 0.

The module does not evaluate the full Riemann explicit formula.
"""

from __future__ import annotations

from typing import Union

import mpmath as mp


Number = Union[int, float, mp.mpf]


def validate_L(L: Number) -> mp.mpf:
    L_mp = mp.mpf(L)

    if L_mp <= 0:
        raise ValueError("L must satisfy L > 0")

    return L_mp


def validate_gamma(gamma: Number) -> mp.mpf:
    gamma_mp = mp.mpf(gamma)

    if gamma_mp <= 0:
        raise ValueError("gamma must satisfy gamma > 0")

    return gamma_mp


def explicit_formula_kernel(
    z: mp.mpc,
    L: Number,
) -> mp.mpc:
    """Return p_L(z) = -exp(L z) / z."""
    L_mp = validate_L(L)
    z = mp.mpc(z)

    if z == 0:
        raise ZeroDivisionError(
            "Explicit-formula kernel is singular at z = 0"
        )

    return -mp.exp(L_mp * z) / z


def explicit_formula_second_derivative_factored(
    z: mp.mpc,
    L: Number,
) -> mp.mpc:
    """Return the manually derived formula for p_L''(z)."""
    L_mp = validate_L(L)
    z = mp.mpc(z)

    if z == 0:
        raise ZeroDivisionError(
            "Explicit-formula kernel is singular at z = 0"
        )

    return -mp.exp(L_mp * z) * (
        L_mp**2 / z
        - 2 * L_mp / z**2
        + 2 / z**3
    )


def explicit_formula_second_derivative_numerical(
    z: mp.mpc,
    L: Number,
) -> mp.mpc:
    """Numerically differentiate the original kernel twice."""
    L_mp = validate_L(L)
    z = mp.mpc(z)

    if z == 0:
        raise ZeroDivisionError(
            "Explicit-formula kernel is singular at z = 0"
        )

    return mp.diff(
        lambda w: explicit_formula_kernel(w, L_mp),
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


def explicit_formula_susceptibility(
    L: Number,
    gamma: Number,
) -> mp.mpf:
    """Return chi_L^EF(gamma) = 2 Re p_L''(rho_gamma)."""
    L_mp = validate_L(L)
    rho = critical_line_point(gamma)

    value = explicit_formula_second_derivative_factored(
        rho,
        L_mp,
    )

    return 2 * mp.re(value)


def amplitude_normalized_susceptibility(
    L: Number,
    gamma: Number,
) -> mp.mpf:
    """Return exp(-L/2) times the raw susceptibility."""
    L_mp = validate_L(L)

    return (
        mp.exp(-L_mp / 2)
        * explicit_formula_susceptibility(L_mp, gamma)
    )


def explicit_formula_profile(c: Number) -> mp.mpf:
    """Return Psi_EF(c)."""
    c_mp = mp.mpf(c)

    if c_mp <= 0:
        raise ValueError("c must satisfy c > 0")

    return (
        -4 * c_mp * mp.cos(c_mp)
        + 2 * (2 - c_mp**2) * mp.sin(c_mp)
    )


def horizontal_zero_configuration(
    delta: Number,
    gamma: Number,
) -> list[mp.mpc]:
    """Return the four-point horizontal configuration."""
    delta_mp = mp.mpf(delta)
    gamma_mp = validate_gamma(gamma)

    if delta_mp <= 0:
        raise ValueError("delta must satisfy delta > 0")

    return [
        mp.mpc(
            mp.mpf("0.5") + epsilon * delta_mp,
            eta * gamma_mp,
        )
        for epsilon in (-1, 1)
        for eta in (-1, 1)
    ]


def vertical_zero_configuration(
    delta: Number,
    gamma: Number,
) -> list[mp.mpc]:
    """Return the four-point vertical configuration."""
    delta_mp = mp.mpf(delta)
    gamma_mp = validate_gamma(gamma)

    if delta_mp <= 0:
        raise ValueError("delta must satisfy delta > 0")

    if delta_mp >= gamma_mp:
        raise ValueError("delta must satisfy delta < gamma")

    return [
        mp.mpc(
            mp.mpf("0.5"),
            eta * (gamma_mp + epsilon * delta_mp),
        )
        for epsilon in (-1, 1)
        for eta in (-1, 1)
    ]


def configuration_sum(
    points: list[mp.mpc],
    L: Number,
) -> mp.mpc:
    """Return the kernel sum over a finite zero configuration."""
    L_mp = validate_L(L)

    return mp.fsum(
        explicit_formula_kernel(point, L_mp)
        for point in points
    )


def directional_contrast(
    delta: Number,
    L: Number,
    gamma: Number,
) -> mp.mpf:
    """Return horizontal configuration sum minus vertical sum."""
    horizontal = configuration_sum(
        horizontal_zero_configuration(delta, gamma),
        L,
    )

    vertical = configuration_sum(
        vertical_zero_configuration(delta, gamma),
        L,
    )

    value = horizontal - vertical

    imaginary_residual = abs(mp.im(value))
    tolerance = mp.mpf(10) ** (-(mp.mp.dps // 2))

    if imaginary_residual > tolerance:
        raise ArithmeticError(
            "Directional contrast should be real under "
            "conjugation symmetry; "
            f"imaginary residual={imaginary_residual}"
        )

    return mp.re(value)


def directional_susceptibility_estimate(
    delta: Number,
    L: Number,
    gamma: Number,
) -> mp.mpf:
    """Return A(delta,L,gamma)/(2 delta^2)."""
    delta_mp = mp.mpf(delta)

    if delta_mp == 0:
        raise ValueError("delta must be nonzero")

    return (
        directional_contrast(
            delta_mp,
            L,
            gamma,
        )
        /
        (2 * delta_mp**2)
    )


def scaled_normalized_susceptibility(
    L: Number,
    gamma: Number,
) -> mp.mpf:
    """Return gamma^3 exp(-L/2) chi_L^EF(gamma)."""
    gamma_mp = validate_gamma(gamma)

    return (
        gamma_mp**3
        * amplitude_normalized_susceptibility(
            L,
            gamma_mp,
        )
    )
