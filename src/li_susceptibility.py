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


def li_inverse_phase_kernel(z: mp.mpc, n: int) -> mp.mpc:
    """Return g_n(z) = 1 - (1 - 1/z)^(-n).

    This is the single-factor kernel produced by the Li-type derivative
    functional centered at s = 1.
    """
    validate_n(n)
    z = mp.mpc(z)

    if z == 0:
        raise ZeroDivisionError("Kernel is singular at z = 0")

    base = 1 - 1 / z

    if base == 0:
        raise ZeroDivisionError(
            "Inverse-phase Li kernel is singular at z = 1"
        )

    return 1 - base ** (-n)


def reflected_li_kernel(z: mp.mpc, n: int) -> mp.mpc:
    """Return f_n(1-z)."""
    validate_n(n)
    z = mp.mpc(z)

    reflected = 1 - z

    if reflected == 0:
        raise ZeroDivisionError(
            "Reflected Li kernel is singular when z = 1"
        )

    return li_kernel(reflected, n)


def orbit_response_from_kernel(
    delta: Number,
    gamma: Number,
    n: int,
    kernel,
) -> mp.mpf:
    """Evaluate the signed orbit response for a supplied kernel."""
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
            total += kernel(z, n)

    for eta in (-1, 1):
        z = mp.mpc(mp.mpf("0.5"), eta * gamma_mp)
        total -= 2 * kernel(z, n)

    return total


def reflection_invariant_zero_response(
    delta: Number,
    gamma: Number,
    n: int,
) -> mp.mpc:
    """Return the orbit response using the standard Li zero kernel."""
    return orbit_response_from_kernel(
        delta,
        gamma,
        n,
        li_kernel,
    )


def reflection_invariant_derivative_response(
    delta: Number,
    gamma: Number,
    n: int,
) -> mp.mpc:
    """Return the orbit response using the inverse-phase kernel."""
    return orbit_response_from_kernel(
        delta,
        gamma,
        n,
        li_inverse_phase_kernel,
    )


def asymmetric_signed_response(
    points_and_weights: list[tuple[mp.mpc, int]],
    n: int,
    kernel,
) -> mp.mpc:
    """Evaluate a finite signed response on an arbitrary point measure.

    The input is a list of (point, integer weight) pairs.
    """
    validate_n(n)

    total = mp.mpc(0)

    for point, weight in points_and_weights:
        total += int(weight) * kernel(mp.mpc(point), n)

    return total


def horizontal_zero_configuration(
    delta: Number,
    gamma: Number,
) -> list[mp.mpc]:
    """Return H_{delta,gamma}, the four-point horizontal configuration."""
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
    """Return V_{delta,gamma}, the four-point vertical configuration."""
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


def finite_configuration_kernel_sum(
    points: list[mp.mpc],
    n: int,
    kernel=li_kernel,
) -> mp.mpc:
    """Return the sum of a kernel over a finite point configuration."""
    validate_n(n)

    return mp.fsum(
        kernel(point, n)
        for point in points
    )


def horizontal_configuration_sum(
    delta: Number,
    gamma: Number,
    n: int,
) -> mp.mpc:
    """Return the Li-kernel sum over H_{delta,gamma}."""
    return finite_configuration_kernel_sum(
        horizontal_zero_configuration(delta, gamma),
        n,
    )


def vertical_configuration_sum(
    delta: Number,
    gamma: Number,
    n: int,
) -> mp.mpc:
    """Return the Li-kernel sum over V_{delta,gamma}."""
    return finite_configuration_kernel_sum(
        vertical_zero_configuration(delta, gamma),
        n,
    )


def horizontal_vertical_contrast(
    delta: Number,
    gamma: Number,
    n: int,
) -> mp.mpf:
    """Return sum_H f_n - sum_V f_n."""
    value = (
        horizontal_configuration_sum(delta, gamma, n)
        -
        vertical_configuration_sum(delta, gamma, n)
    )

    imaginary_residual = abs(mp.im(value))
    tolerance = mp.mpf(10) ** (-(mp.mp.dps // 2))

    if imaginary_residual > tolerance:
        raise ArithmeticError(
            "Horizontal-vertical contrast should be real under "
            "conjugation symmetry; "
            f"imaginary residual={imaginary_residual}"
        )

    return mp.re(value)


def li_kernel_derivative(
    z: mp.mpc,
    n: int,
    order: int,
) -> mp.mpc:
    """Numerically differentiate the original Li kernel to a given order."""
    validate_n(n)

    if isinstance(order, bool) or not isinstance(order, int):
        raise TypeError("order must be an integer")

    if order < 0:
        raise ValueError("order must satisfy order >= 0")

    z = mp.mpc(z)

    return mp.diff(
        lambda w: li_kernel(w, n),
        z,
        order,
    )


def sixth_order_contrast_coefficient(
    n: int,
    gamma: Number,
) -> mp.mpf:
    """Return Re f_n^(6)(rho_gamma) / 90."""
    rho = critical_line_point(gamma)

    derivative = li_kernel_derivative(
        rho,
        n,
        6,
    )

    return mp.re(derivative) / 90


def li_susceptibility_profile(c: Number) -> mp.mpf:
    """Return Psi_Li(c) = -2c(c cos c + 2 sin c)."""
    c_mp = mp.mpf(c)

    if c_mp <= 0:
        raise ValueError("c must satisfy c > 0")

    return -2 * c_mp * (
        c_mp * mp.cos(c_mp)
        + 2 * mp.sin(c_mp)
    )


def li_susceptibility_correction_profile(
    q: Number,
) -> mp.mpf:
    """Return the gamma^-4 correction profile K_Li(q)."""
    q_mp = mp.mpf(q)

    if q_mp <= 0:
        raise ValueError("q must satisfy q > 0")

    return (
        mp.mpf(4) / 3
        * q_mp**2
        * mp.cos(q_mp)
        +
        (
            2 * q_mp
            -
            q_mp**3 / 6
        )
        * mp.sin(q_mp)
    )


def li_profile_derivative(c: Number) -> mp.mpf:
    """Return the first derivative of Psi_Li."""
    c_mp = mp.mpf(c)

    if c_mp <= 0:
        raise ValueError("c must satisfy c > 0")

    return mp.diff(
        li_susceptibility_profile,
        c_mp,
    )


def li_blind_scale(
    k: int,
    iterations: int = 600,
) -> mp.mpf:
    """Return the unique positive profile zero in interval I_k.

    Uses monotone bisection on

        tan(c) + c/2 = 0

    over

        ((k+1/2) pi, (k+1) pi).
    """
    if isinstance(k, bool) or not isinstance(k, int):
        raise TypeError("k must be an integer")

    if k < 0:
        raise ValueError("k must satisfy k >= 0")

    if iterations <= 0:
        raise ValueError("iterations must satisfy iterations > 0")

    epsilon = mp.mpf(10) ** (-(mp.mp.dps - 10))

    left = (
        (mp.mpf(k) + mp.mpf("0.5"))
        * mp.pi
        + epsilon
    )

    right = (
        (mp.mpf(k) + 1)
        * mp.pi
        - epsilon
    )

    def equation(c: mp.mpf) -> mp.mpf:
        return mp.tan(c) + c / 2

    left_value = equation(left)
    right_value = equation(right)

    if not (
        left_value < 0
        and right_value > 0
    ):
        raise ArithmeticError(
            "Blind-scale bisection interval "
            "does not bracket the expected root"
        )

    for _ in range(iterations):
        midpoint = (left + right) / 2
        value = equation(midpoint)

        if value < 0:
            left = midpoint
        else:
            right = midpoint

    return (left + right) / 2


def li_blind_scale_asymptotic(
    k: int,
) -> mp.mpf:
    """Return the three-term large-k blind-scale approximation."""
    if isinstance(k, bool) or not isinstance(k, int):
        raise TypeError("k must be an integer")

    if k < 0:
        raise ValueError("k must satisfy k >= 0")

    a_k = (
        mp.mpf(k) + mp.mpf("0.5")
    ) * mp.pi

    return (
        a_k
        + 2 / a_k
        - mp.mpf(20) / (3 * a_k**3)
    )


def li_blind_scale_correction(
    k: int,
) -> mp.mpf:
    """Return K_Li(c_k) using the root-simplified formula."""
    c_k = li_blind_scale(k)

    return (
        c_k**2
        * (c_k**2 + 4)
        * mp.cos(c_k)
        / 12
    )


def solve_near_blind_gamma(
    n: int,
    k: int,
    beta: Number,
    r: Number,
) -> mp.mpf:
    """Solve n/gamma - c_k = beta gamma^(-r).

    This preserves integer n while enforcing the claimed near-blind
    parameter path without integer-rounding contamination.
    """
    validate_n(n)

    beta_mp = mp.mpf(beta)
    r_mp = mp.mpf(r)

    if beta_mp == 0:
        raise ValueError("beta must be nonzero")

    if r_mp <= 0:
        raise ValueError("r must satisfy r > 0")

    c_k = li_blind_scale(k)
    n_mp = mp.mpf(n)

    def equation(gamma: mp.mpf) -> mp.mpf:
        return (
            n_mp / gamma
            - c_k
            - beta_mp * gamma ** (-r_mp)
        )

    initial = n_mp / c_k

    gamma = mp.findroot(
        equation,
        (
            mp.mpf("0.9") * initial,
            mp.mpf("1.1") * initial,
        ),
    )

    if gamma <= 0:
        raise ArithmeticError(
            "Near-blind gamma solver returned nonpositive gamma"
        )

    residual = abs(equation(gamma))
    tolerance = mp.mpf(10) ** (-(mp.mp.dps // 2))

    if residual > tolerance:
        raise ArithmeticError(
            "Near-blind gamma solver residual exceeded tolerance: "
            f"{residual}"
        )

    return gamma


def li_blind_scale_correction_closed(
    k: int,
) -> mp.mpf:
    """Return K_Li(c_k) in the sign-explicit closed form."""
    c_k = li_blind_scale(k)

    sign = mp.mpf(-1) ** (k + 1)

    return (
        sign
        * c_k**2
        * mp.sqrt(c_k**2 + 4)
        / 6
    )


def li_resonant_height_ratio(
    k: int,
    m: int,
) -> mp.mpf:
    """Return the two-orbit blind-scale resonance ratio c_k / c_m."""
    c_k = li_blind_scale(k)
    c_m = li_blind_scale(m)

    return c_k / c_m


def li_two_orbit_aggregate_susceptibility(
    n: int,
    Gamma: Number,
    a: Number,
) -> mp.mpf:
    """Equal-weight aggregate susceptibility at heights Gamma and a*Gamma."""
    validate_n(n)

    Gamma_mp = validate_gamma(Gamma)
    a_mp = mp.mpf(a)

    if a_mp <= 0:
        raise ValueError("a must satisfy a > 0")

    return (
        li_susceptibility_exact(
            n,
            Gamma_mp,
        )
        +
        li_susceptibility_exact(
            n,
            a_mp * Gamma_mp,
        )
    )


def li_two_orbit_aggregate_profile(
    c: Number,
    a: Number,
) -> mp.mpf:
    """Return Psi(c) + a^-2 Psi(c/a)."""
    c_mp = mp.mpf(c)
    a_mp = mp.mpf(a)

    if c_mp <= 0:
        raise ValueError("c must satisfy c > 0")

    if a_mp <= 0:
        raise ValueError("a must satisfy a > 0")

    return (
        li_susceptibility_profile(c_mp)
        +
        a_mp**(-2)
        * li_susceptibility_profile(
            c_mp / a_mp
        )
    )


def li_two_orbit_resonant_correction(
    k: int,
    m: int,
) -> mp.mpf:
    """Return the exact fourth-order coefficient at resonance c_k/c_m."""
    c_k = li_blind_scale(k)
    c_m = li_blind_scale(m)

    return (
        li_blind_scale_correction_closed(k)
        +
        (c_m / c_k) ** 4
        * li_blind_scale_correction_closed(m)
    )


def li_resonance_monotone_transform(
    c: Number,
) -> mp.mpf:
    """Return F(c) = c^6 sqrt(c^2 + 4)."""
    c_mp = mp.mpf(c)

    if c_mp <= 0:
        raise ValueError("c must satisfy c > 0")

    return (
        c_mp**6
        * mp.sqrt(c_mp**2 + 4)
    )


def li_resonant_cancellation_ratio(
    k: int,
    m: int,
) -> mp.mpf:
    """Return normalized cancellation ratio for a resonant pair."""
    c_k = li_blind_scale(k)
    c_m = li_blind_scale(m)

    first = abs(
        li_blind_scale_correction_closed(k)
    )

    second = (
        (c_m / c_k) ** 4
        * abs(
            li_blind_scale_correction_closed(m)
        )
    )

    numerator = abs(
        li_two_orbit_resonant_correction(
            k,
            m,
        )
    )

    denominator = first + second

    return numerator / denominator


def li_window_continuum_profile(
    c: Number,
    eta: Number,
) -> mp.mpf:
    """Return the frozen leading smooth-density window profile Phi_eta(c)."""
    c_mp = mp.mpf(c)
    eta_mp = mp.mpf(eta)

    if c_mp <= 0:
        raise ValueError("c must satisfy c > 0")

    if eta_mp <= 0:
        raise ValueError("eta must satisfy eta > 0")

    upper_scale = 1 + eta_mp

    return (
        c_mp
        / mp.pi
        *
        (
            upper_scale**(-2)
            * mp.sin(
                c_mp / upper_scale
            )
            -
            mp.sin(c_mp)
        )
    )


def li_window_finite_height_profile(
    c: Number,
    eta: Number,
    H: Number,
) -> mp.mpf:
    """Return the finite-height leading-density window benchmark."""
    c_mp = mp.mpf(c)
    eta_mp = mp.mpf(eta)
    H_mp = mp.mpf(H)

    if c_mp <= 0:
        raise ValueError("c must satisfy c > 0")

    if eta_mp <= 0:
        raise ValueError("eta must satisfy eta > 0")

    if H_mp <= 1:
        raise ValueError("H must satisfy H > 1")

    def integrand(
        u: mp.mpf,
    ) -> mp.mpf:
        return (
            u**(-2)
            * li_susceptibility_profile(
                c_mp / u
            )
            * mp.log(
                u * H_mp / (2 * mp.pi)
            )
        )

    integral = mp.quad(
        integrand,
        [
            mp.mpf("1"),
            1 + eta_mp,
        ],
    )

    return (
        integral
        /
        (
            2
            * mp.pi
            * mp.log(H_mp)
        )
    )


def li_susceptibility_gamma_derivative(
    n: int,
    gamma: Number,
) -> mp.mpf:
    """Exact derivative d/dgamma of the Li quadratic susceptibility."""
    validate_n(n)
    gamma_mp = validate_gamma(gamma)

    n_mp = mp.mpf(n)

    D = (
        gamma_mp**2
        + mp.mpf("0.25")
    )

    theta = theta_gamma(
        gamma_mp
    )

    phase = n_mp * theta

    sine = mp.sin(phase)
    cosine = mp.cos(phase)

    A = (
        n_mp * cosine
        +
        2 * gamma_mp * sine
    )

    A_prime = (
        n_mp**2
        / D
        * sine
        +
        2 * sine
        -
        2
        * n_mp
        * gamma_mp
        / D
        * cosine
    )

    return (
        8
        * n_mp
        * gamma_mp
        / D**3
        * A
        -
        2
        * n_mp
        / D**2
        * A_prime
    )


def li_derivative_response_profile(
    q: Number,
) -> mp.mpf:
    """Return J_Li(q) = 2 Psi_Li(q) + q Psi_Li'(q)."""
    q_mp = mp.mpf(q)

    return (
        2
        * q_mp**3
        * mp.sin(q_mp)
        -
        12
        * q_mp**2
        * mp.cos(q_mp)
        -
        12
        * q_mp
        * mp.sin(q_mp)
    )


def li_continuum_transfer_envelope(
    c: Number,
    eta: Number,
) -> mp.mpf:
    """Return the continuum sup-norm response-transfer envelope."""
    c_mp = mp.mpf(c)
    eta_mp = mp.mpf(eta)

    if c_mp <= 0:
        raise ValueError("c must satisfy c > 0")

    if eta_mp <= 0:
        raise ValueError("eta must satisfy eta > 0")

    upper_scale = 1 + eta_mp

    lower_endpoint = abs(
        li_susceptibility_profile(
            c_mp
        )
    )

    upper_endpoint = (
        upper_scale**(-2)
        * abs(
            li_susceptibility_profile(
                c_mp / upper_scale
            )
        )
    )

    variation = mp.quad(
        lambda u: (
            u**(-3)
            * abs(
                li_derivative_response_profile(
                    c_mp / u
                )
            )
        ),
        [
            mp.mpf("1"),
            upper_scale,
        ],
    )

    return (
        lower_endpoint
        +
        upper_endpoint
        +
        variation
    )


def li_profile_to_transfer_ratio(
    c: Number,
    eta: Number,
) -> mp.mpf:
    """Return |Phi_eta(c)| / L_eta(c)."""
    envelope = (
        li_continuum_transfer_envelope(
            c,
            eta,
        )
    )

    if envelope <= 0:
        raise ValueError(
            "transfer envelope must be positive"
        )

    return (
        abs(
            li_window_continuum_profile(
                c,
                eta,
            )
        )
        /
        envelope
    )
