"""Tests for the resolvent susceptibility family."""

from __future__ import annotations

import mpmath as mp
import pytest

from src.resolvent_susceptibility import (
    critical_line_point,
    fixed_a_asymptotic_target,
    fixed_a_scaled_susceptibility,
    resolvent_kernel,
    resolvent_profile,
    resolvent_second_derivative_factored,
    resolvent_second_derivative_numerical,
    resolvent_susceptibility_exact,
    resolvent_susceptibility_from_derivative,
    scaled_resolvent_susceptibility,
)


mp.mp.dps = 140


@pytest.mark.parametrize(
    "a,gamma",
    [
        ("1", "14.134725141734693790"),
        ("2", "50"),
        ("10", "100"),
        ("100", "250"),
        ("500", "1000"),
    ],
)
def test_second_derivative_matches_direct_diff(
    a: str,
    gamma: str,
) -> None:
    rho = critical_line_point(gamma)

    manual = resolvent_second_derivative_factored(
        rho,
        a,
    )

    numerical = resolvent_second_derivative_numerical(
        rho,
        a,
    )

    denominator = max(
        abs(manual),
        abs(numerical),
        mp.mpf("1e-160"),
    )

    relative_error = abs(
        manual - numerical
    ) / denominator

    assert relative_error < mp.mpf("1e-100")


@pytest.mark.parametrize(
    "a,gamma",
    [
        ("1", "14"),
        ("2", "50"),
        ("10", "100"),
        ("100", "250"),
    ],
)
def test_exact_formula_matches_derivative_response(
    a: str,
    gamma: str,
) -> None:
    derivative_value = (
        resolvent_susceptibility_from_derivative(
            a,
            gamma,
        )
    )

    exact_value = resolvent_susceptibility_exact(
        a,
        gamma,
    )

    denominator = max(
        abs(derivative_value),
        abs(exact_value),
        mp.mpf("1e-160"),
    )

    relative_error = abs(
        derivative_value - exact_value
    ) / denominator

    assert relative_error < mp.mpf("1e-110")


@pytest.mark.parametrize(
    "c",
    ["0.1", "0.25", "0.5", "1", "1.5", "2", "3", "5"],
)
def test_similarity_profile_is_exact_on_scaled_path(
    c: str,
) -> None:
    c_mp = mp.mpf(c)
    gamma = mp.mpf("1234.5")
    d = c_mp * gamma
    a = mp.mpf("0.5") + d

    scaled = scaled_resolvent_susceptibility(
        a,
        gamma,
    )

    target = resolvent_profile(c_mp)

    assert abs(
        scaled - target
    ) < mp.mpf("1e-120")


@pytest.mark.parametrize(
    "a",
    ["0.75", "1", "2", "5", "10"],
)
def test_fixed_a_scaled_limit(
    a: str,
) -> None:
    a_mp = mp.mpf(a)
    gamma = mp.mpf("1e8")

    scaled = fixed_a_scaled_susceptibility(
        a_mp,
        gamma,
    )

    target = fixed_a_asymptotic_target(
        a_mp,
    )

    assert abs(
        scaled - target
    ) < mp.mpf("1e-10")


def test_profile_zero_at_sqrt_three() -> None:
    value = resolvent_profile(
        mp.sqrt(3)
    )

    assert abs(value) < mp.mpf("1e-130")


def test_profile_changes_sign_at_sqrt_three() -> None:
    center = mp.sqrt(3)
    epsilon = mp.mpf("1e-8")

    left = resolvent_profile(
        center - epsilon
    )

    right = resolvent_profile(
        center + epsilon
    )

    assert left < 0
    assert right > 0


def test_invalid_a_rejected() -> None:
    with pytest.raises(ValueError):
        resolvent_kernel(
            mp.mpc(1, 1),
            "0.5",
        )
