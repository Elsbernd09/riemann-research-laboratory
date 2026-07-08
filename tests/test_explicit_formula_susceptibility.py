"""Tests for the explicit-formula zero-kernel susceptibility."""

from __future__ import annotations

import mpmath as mp
import pytest

from src.explicit_formula_susceptibility import (
    amplitude_normalized_susceptibility,
    critical_line_point,
    directional_susceptibility_estimate,
    explicit_formula_kernel,
    explicit_formula_profile,
    explicit_formula_second_derivative_factored,
    explicit_formula_second_derivative_numerical,
    explicit_formula_susceptibility,
    scaled_normalized_susceptibility,
    vertical_zero_configuration,
)


mp.mp.dps = 120


@pytest.mark.parametrize(
    "L,gamma",
    [
        ("0.01", "14.134725141734693790"),
        ("0.05", "50"),
        ("0.1", "100"),
        ("0.5", "250"),
        ("1", "500"),
    ],
)
def test_second_derivative_matches_direct_diff(
    L: str,
    gamma: str,
) -> None:
    rho = critical_line_point(gamma)

    manual = explicit_formula_second_derivative_factored(
        rho,
        L,
    )

    numerical = explicit_formula_second_derivative_numerical(
        rho,
        L,
    )

    denominator = max(
        abs(manual),
        abs(numerical),
        mp.mpf("1e-150"),
    )

    relative_error = abs(
        manual - numerical
    ) / denominator

    assert relative_error < mp.mpf("1e-90")


def test_directional_contrast_recovers_susceptibility() -> None:
    L = mp.mpf("0.01")
    gamma = mp.mpf("100")
    delta = mp.mpf("1e-18")

    estimate = directional_susceptibility_estimate(
        delta,
        L,
        gamma,
    )

    target = explicit_formula_susceptibility(
        L,
        gamma,
    )

    denominator = max(
        abs(estimate),
        abs(target),
        mp.mpf("1e-150"),
    )

    relative_error = abs(
        estimate - target
    ) / denominator

    assert relative_error < mp.mpf("1e-45")


@pytest.mark.parametrize(
    "c",
    ["0.25", "0.5", "1", "2", "5"],
)
def test_mesoscopic_scaling_at_large_gamma(
    c: str,
) -> None:
    c_mp = mp.mpf(c)
    gamma = mp.mpf("100000")
    L = c_mp / gamma

    scaled = scaled_normalized_susceptibility(
        L,
        gamma,
    )

    target = explicit_formula_profile(c_mp)

    assert abs(
        scaled - target
    ) < mp.mpf("1e-3")


def test_amplitude_normalization_reconstructs_raw() -> None:
    L = mp.mpf("2")
    gamma = mp.mpf("100")

    raw = explicit_formula_susceptibility(
        L,
        gamma,
    )

    normalized = amplitude_normalized_susceptibility(
        L,
        gamma,
    )

    reconstructed = (
        mp.exp(L / 2)
        * normalized
    )

    denominator = max(
        abs(raw),
        abs(reconstructed),
        mp.mpf("1e-150"),
    )

    relative_error = abs(
        raw - reconstructed
    ) / denominator

    assert relative_error < mp.mpf("1e-100")


def test_invalid_L_rejected() -> None:
    with pytest.raises(ValueError):
        explicit_formula_kernel(
            mp.mpc(1, 1),
            0,
        )


def test_vertical_configuration_rejects_large_delta() -> None:
    with pytest.raises(ValueError):
        vertical_zero_configuration(
            "10",
            "10",
        )
