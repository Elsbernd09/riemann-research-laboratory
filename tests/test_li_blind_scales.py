"""Tests for Li quadratic-response blind scales."""

from __future__ import annotations

import mpmath as mp
import pytest

from src.li_susceptibility import (
    li_blind_scale,
    li_blind_scale_asymptotic,
    li_blind_scale_correction,
    li_profile_derivative,
    li_susceptibility_correction_profile,
    li_susceptibility_exact,
    li_susceptibility_profile,
    solve_near_blind_gamma,
)


mp.mp.dps = 140


@pytest.mark.parametrize(
    "k",
    [0, 1, 2, 3, 4, 10, 20],
)
def test_blind_scale_is_unique_root_in_predicted_interval(
    k: int,
) -> None:
    c_k = li_blind_scale(k)

    left = (
        mp.mpf(k) + mp.mpf("0.5")
    ) * mp.pi

    right = (
        mp.mpf(k) + 1
    ) * mp.pi

    assert left < c_k < right

    assert abs(
        li_susceptibility_profile(c_k)
    ) < mp.mpf("1e-110")


def test_blind_scale_asymptotic_improves_at_large_k() -> None:
    k_values = [10, 20, 40, 80]

    errors = []

    for k in k_values:
        errors.append(
            abs(
                li_blind_scale(k)
                -
                li_blind_scale_asymptotic(k)
            )
        )

    assert all(
        later < earlier
        for earlier, later in zip(
            errors,
            errors[1:],
        )
    )


def test_root_simplified_correction_formula() -> None:
    c_0 = li_blind_scale(0)

    direct = li_susceptibility_correction_profile(
        c_0
    )

    simplified = li_blind_scale_correction(0)

    denominator = max(
        abs(direct),
        abs(simplified),
        mp.mpf("1e-150"),
    )

    relative_error = abs(
        direct - simplified
    ) / denominator

    assert relative_error < mp.mpf("1e-110")


def test_exact_matched_blind_scale_gamma4_law() -> None:
    c_0 = li_blind_scale(0)
    target = li_blind_scale_correction(0)

    n = 1_000_000
    gamma = mp.mpf(n) / c_0

    scaled = (
        gamma**4
        * li_susceptibility_exact(
            n,
            gamma,
        )
    )

    assert abs(
        scaled - target
    ) < mp.mpf("1e-8")


@pytest.mark.parametrize(
    "r,expected_exponent",
    [
        ("0.5", "2.5"),
        ("1", "3"),
        ("1.5", "3.5"),
        ("2", "4"),
        ("3", "4"),
    ],
)
def test_near_blind_transition_paths(
    r: str,
    expected_exponent: str,
) -> None:
    r_mp = mp.mpf(r)
    exponent = mp.mpf(expected_exponent)

    c_0 = li_blind_scale(0)
    psi_prime = li_profile_derivative(c_0)
    correction = li_blind_scale_correction(0)

    beta = mp.mpf("1")
    n = 1_000_000

    gamma = solve_near_blind_gamma(
        n=n,
        k=0,
        beta=beta,
        r=r_mp,
    )

    q = mp.mpf(n) / gamma

    path_residual = (
        q
        -
        c_0
        -
        beta * gamma**(-r_mp)
    )

    assert abs(path_residual) < mp.mpf("1e-100")

    susceptibility = li_susceptibility_exact(
        n,
        gamma,
    )

    scaled = (
        gamma**exponent
        * susceptibility
    )

    if r_mp < 2:
        target = beta * psi_prime
        tolerance = mp.mpf("0.1")
    elif r_mp == 2:
        target = (
            beta * psi_prime
            + correction
        )
        tolerance = mp.mpf("1e-6")
    else:
        target = correction
        tolerance = mp.mpf("1e-2")

    assert abs(
        scaled - target
    ) < tolerance
