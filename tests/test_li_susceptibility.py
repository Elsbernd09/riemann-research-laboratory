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


def test_inverse_phase_equals_reflected_kernel() -> None:
    from src.li_susceptibility import (
        li_inverse_phase_kernel,
        reflected_li_kernel,
    )

    z = mp.mpc("0.7", "14.134725141734693790")

    for n in [1, 2, 5, 20, 100]:
        left = li_inverse_phase_kernel(z, n)
        right = reflected_li_kernel(z, n)

        denominator = max(
            abs(left),
            abs(right),
            mp.mpf("1e-100"),
        )
        relative_error = abs(left - right) / denominator

        assert relative_error < mp.mpf("1e-70")


def test_reflection_invariant_orbit_bridge() -> None:
    from src.li_susceptibility import (
        reflection_invariant_derivative_response,
        reflection_invariant_zero_response,
    )

    cases = [
        ("0.01", "14.134725141734693790", 1),
        ("0.05", "50", 5),
        ("0.1", "100", 20),
        ("0.2", "250", 100),
    ]

    for delta, gamma, n in cases:
        left = reflection_invariant_zero_response(
            delta,
            gamma,
            n,
        )
        right = reflection_invariant_derivative_response(
            delta,
            gamma,
            n,
        )

        denominator = max(
            abs(left),
            abs(right),
            mp.mpf("1e-100"),
        )
        relative_error = abs(left - right) / denominator

        assert relative_error < mp.mpf("1e-70")


def test_asymmetric_measure_generically_breaks_bridge() -> None:
    from src.li_susceptibility import (
        asymmetric_signed_response,
        li_inverse_phase_kernel,
        li_kernel,
    )

    measure = [
        (mp.mpc("0.6", "14"), 1),
        (mp.mpc("0.5", "14"), -1),
    ]

    f_response = asymmetric_signed_response(
        measure,
        20,
        li_kernel,
    )

    g_response = asymmetric_signed_response(
        measure,
        20,
        li_inverse_phase_kernel,
    )

    assert abs(f_response - g_response) > mp.mpf("1e-20")


def test_horizontal_and_vertical_configurations_have_four_points() -> None:
    from src.li_susceptibility import (
        horizontal_zero_configuration,
        vertical_zero_configuration,
    )

    horizontal = horizontal_zero_configuration(
        "0.1",
        "14",
    )

    vertical = vertical_zero_configuration(
        "0.1",
        "14",
    )

    assert len(horizontal) == 4
    assert len(vertical) == 4


def test_directional_contrast_recovers_susceptibility() -> None:
    from src.li_susceptibility import (
        horizontal_vertical_contrast,
        li_susceptibility_exact,
    )

    n = 20
    gamma = mp.mpf("50")
    delta = mp.mpf("1e-15")

    contrast = horizontal_vertical_contrast(
        delta,
        gamma,
        n,
    )

    estimate = contrast / (2 * delta**2)
    target = li_susceptibility_exact(n, gamma)

    denominator = max(
        abs(estimate),
        abs(target),
        mp.mpf("1e-100"),
    )

    relative_error = abs(estimate - target) / denominator

    assert relative_error < mp.mpf("1e-45")


def test_directional_contrast_has_sixth_order_leading_error() -> None:
    from src.li_susceptibility import (
        horizontal_vertical_contrast,
        li_susceptibility_exact,
        sixth_order_contrast_coefficient,
    )

    n = 20
    gamma = mp.mpf("50")
    delta = mp.mpf("1e-8")

    contrast = horizontal_vertical_contrast(
        delta,
        gamma,
        n,
    )

    chi = li_susceptibility_exact(n, gamma)

    scaled_residual = (
        contrast
        -
        2 * delta**2 * chi
    ) / delta**6

    target = sixth_order_contrast_coefficient(
        n,
        gamma,
    )

    denominator = max(
        abs(scaled_residual),
        abs(target),
        mp.mpf("1e-100"),
    )

    relative_error = abs(
        scaled_residual - target
    ) / denominator

    assert relative_error < mp.mpf("1e-20")


def test_vertical_configuration_rejects_delta_ge_gamma() -> None:
    from src.li_susceptibility import (
        vertical_zero_configuration,
    )

    with pytest.raises(ValueError):
        vertical_zero_configuration(
            "14",
            "14",
        )
