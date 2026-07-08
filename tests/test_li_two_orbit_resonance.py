"""Tests for finite two-orbit Li blind-scale resonance."""

from __future__ import annotations

import mpmath as mp
import pytest

from src.li_susceptibility import (
    li_blind_scale,
    li_blind_scale_correction,
    li_blind_scale_correction_closed,
    li_resonance_monotone_transform,
    li_resonant_cancellation_ratio,
    li_resonant_height_ratio,
    li_two_orbit_aggregate_profile,
    li_two_orbit_aggregate_susceptibility,
    li_two_orbit_resonant_correction,
)


mp.mp.dps = 140


@pytest.mark.parametrize(
    "k",
    [0, 1, 2, 3, 10, 20],
)
def test_closed_blind_scale_correction_formula(
    k: int,
) -> None:
    direct = li_blind_scale_correction(k)

    closed = li_blind_scale_correction_closed(k)

    denominator = max(
        abs(direct),
        abs(closed),
        mp.mpf("1e-150"),
    )

    assert (
        abs(direct - closed)
        / denominator
        <
        mp.mpf("1e-110")
    )


def test_resonance_monotone_transform_increases() -> None:
    values = [
        li_resonance_monotone_transform(
            li_blind_scale(k)
        )
        for k in range(20)
    ]

    assert all(
        later > earlier
        for earlier, later in zip(
            values,
            values[1:],
        )
    )


@pytest.mark.parametrize(
    "k,m",
    [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 2),
        (2, 5),
        (10, 11),
        (10, 12),
        (20, 19),
    ],
)
def test_resonant_fourth_order_coefficient_never_zero(
    k: int,
    m: int,
) -> None:
    coefficient = (
        li_two_orbit_resonant_correction(
            k,
            m,
        )
    )

    assert coefficient != 0


def test_adjacent_relative_cancellation_strengthens() -> None:
    ratios = [
        li_resonant_cancellation_ratio(
            k,
            k + 1,
        )
        for k in [10, 20, 40, 80]
    ]

    assert all(
        later < earlier
        for earlier, later in zip(
            ratios,
            ratios[1:],
        )
    )


def test_nonresonant_second_orbit_restores_gamma2_response() -> None:
    c_0 = li_blind_scale(0)

    a = mp.mpf("2")

    target = li_two_orbit_aggregate_profile(
        c_0,
        a,
    )

    n = 1_000_000
    Gamma = mp.mpf(n) / c_0

    aggregate = (
        li_two_orbit_aggregate_susceptibility(
            n,
            Gamma,
            a,
        )
    )

    scaled = Gamma**2 * aggregate

    assert abs(
        scaled - target
    ) < mp.mpf("1e-8")


def test_resonant_two_orbit_gamma4_law() -> None:
    c_0 = li_blind_scale(0)

    a = li_resonant_height_ratio(
        0,
        1,
    )

    target = (
        li_two_orbit_resonant_correction(
            0,
            1,
        )
    )

    n = 1_000_000
    Gamma = mp.mpf(n) / c_0

    aggregate = (
        li_two_orbit_aggregate_susceptibility(
            n,
            Gamma,
            a,
        )
    )

    scaled = Gamma**4 * aggregate

    assert abs(
        scaled - target
    ) < mp.mpf("1e-6")
