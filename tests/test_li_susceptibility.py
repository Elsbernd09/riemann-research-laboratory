"""Tests for the individual Li-kernel susceptibility implementation."""

from __future__ import annotations

import mpmath as mp
import pytest

from src.li_susceptibility import (
    critical_line_point,
    finite_delta_quadratic_estimate,
    li_kernel,
    li_kernel_second_derivative_factored,
    li_kernel_second_derivative_numerical,
    li_mesoscopic_profile,
    li_susceptibility_exact,
    li_susceptibility_from_derivative,
    theta_gamma,
)


mp.mp.dps = 100


@pytest.mark.parametrize("n", [1, 2, 3, 10, 100])
@pytest.mark.parametrize("gamma", ["1", "14.134725", "100"])
def test_exact_formula_matches_derivative(n: int, gamma: str) -> None:
    left = li_susceptibility_exact(n, gamma)
    right = li_susceptibility_from_derivative(n, gamma)

    denominator = max(
        abs(left),
        abs(right),
        mp.mpf("1e-100"),
    )
    relative_error = abs(left - right) / denominator

    assert relative_error < mp.mpf("1e-70")


@pytest.mark.parametrize("n", [1, 2, 5, 20])
def test_manual_second_derivative_matches_mpmath(n: int) -> None:
    rho = critical_line_point("14.134725141734693790")

    manual = li_kernel_second_derivative_factored(rho, n)
    numerical = li_kernel_second_derivative_numerical(rho, n)

    assert mp.almosteq(manual, numerical)


def test_critical_line_phase_has_unit_modulus() -> None:
    gamma = mp.mpf("14.134725141734693790")
    rho = critical_line_point(gamma)

    value = 1 - 1 / rho

    assert mp.almosteq(abs(value), 1)
    assert mp.almosteq(value, mp.e ** (1j * theta_gamma(gamma)))


def test_signed_response_quadratic_limit() -> None:
    n = 20
    gamma = mp.mpf("50")
    target = li_susceptibility_exact(n, gamma)

    delta = mp.mpf("1e-20")
    estimate = finite_delta_quadratic_estimate(delta, gamma, n)

    assert mp.almosteq(
        estimate,
        target,
        rel_eps=mp.mpf("1e-35"),
        abs_eps=mp.mpf("1e-35"),
    )


@pytest.mark.parametrize("c", ["0.25", "0.5", "1", "2", "5"])
def test_mesoscopic_scaling_at_large_gamma(c: str) -> None:
    c_mp = mp.mpf(c)
    gamma = mp.mpf("100000")
    n = int(mp.nint(c_mp * gamma))

    scaled = gamma**2 * li_susceptibility_exact(n, gamma)
    target = li_mesoscopic_profile(mp.mpf(n) / gamma)

    assert abs(scaled - target) < mp.mpf("1e-3")


def test_invalid_n_rejected() -> None:
    with pytest.raises(ValueError):
        li_kernel(mp.mpc(1, 1), 0)


def test_zero_kernel_singularity_rejected() -> None:
    with pytest.raises(ZeroDivisionError):
        li_kernel(mp.mpc(0), 1)
