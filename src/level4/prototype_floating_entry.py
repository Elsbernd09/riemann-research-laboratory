from __future__ import annotations

from pathlib import Path
from typing import Dict, Any
import json
import math

from src.level4.certified_entry_metadata import (
    CertifiedEntryMetadata,
    EntryCertificationStatus,
    ErrorDecomposition,
)
from src.level4.conventions import BOMBIERI_LAGARIAS_CONVENTION
from src.level4.toy_basis import TriangularLogBump


EULER_GAMMA = 0.5772156649015328606


def corrected_constant_component(f_at_one: float) -> float:
    """
    Bombieri-Lagarias displayed normalization:
    - (log(pi) + EulerGamma) f(1)
    """
    return -1.0 * (math.log(math.pi) + EULER_GAMMA) * f_at_one


def midpoint_integral(func, lo: float, hi: float, steps: int) -> float:
    if hi <= lo:
        return 0.0
    h = (hi - lo) / steps
    total = 0.0
    for k in range(steps):
        x = lo + (k + 0.5) * h
        total += func(x)
    return total * h


def star_eval(phi: TriangularLogBump, x: float) -> float:
    """
    Direct project star/involution for real toy functions:

    phi_star(x) = x^(-1) phi(1/x).

    This avoids assuming the toy object has a .star() method.
    """
    if x <= 0.0:
        return 0.0
    return (1.0 / x) * phi.eval_x(1.0 / x)


def toy_convolution_with_star(
    phi_left: TriangularLogBump,
    phi_right: TriangularLogBump,
    x: float,
    steps: int,
) -> float:
    """
    Floating-point toy convolution proxy:

    F(x) = integral phi_left(y) phi_right_star(x/y) dy/y.

    This is not certified.
    """
    if x <= 0.0:
        return 0.0

    lo, hi = phi_left.support_x

    def integrand(y: float) -> float:
        if y <= 0.0:
            return 0.0
        return phi_left.eval_x(y) * star_eval(phi_right, x / y) / y

    return midpoint_integral(integrand, lo, hi, steps)


def tilde_value_of_F(
    phi_left: TriangularLogBump,
    phi_right: TriangularLogBump,
    x: float,
    conv_steps: int,
) -> float:
    """
    Tilde of F:

    F_tilde(x) = x^(-1) F(1/x).
    """
    if x <= 0.0:
        return 0.0
    return (1.0 / x) * toy_convolution_with_star(phi_left, phi_right, 1.0 / x, conv_steps)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    for k in range(3, r + 1, 2):
        if n % k == 0:
            return False
    return True


def von_mangoldt(n: int) -> float:
    """
    Lambda(n)=log(p) if n=p^k, else 0.
    """
    if n < 2:
        return 0.0

    for p in range(2, n + 1):
        if not is_prime(p):
            continue
        power = p
        while power < n:
            power *= p
        if power == n:
            return math.log(p)

    return 0.0


def central_integral(
    phi_left: TriangularLogBump,
    phi_right: TriangularLogBump,
    B: float,
    steps: int,
    conv_steps: int,
) -> float:
    lo = math.exp(-2.0 * B)
    hi = math.exp(2.0 * B)
    return midpoint_integral(
        lambda x: toy_convolution_with_star(phi_left, phi_right, x, conv_steps),
        lo,
        hi,
        steps,
    )


def star_central_integral(
    phi_left: TriangularLogBump,
    phi_right: TriangularLogBump,
    B: float,
    steps: int,
    conv_steps: int,
) -> float:
    lo = math.exp(-2.0 * B)
    hi = math.exp(2.0 * B)
    return midpoint_integral(
        lambda x: tilde_value_of_F(phi_left, phi_right, x, conv_steps),
        lo,
        hi,
        steps,
    )


def finite_prime_sum(
    phi_left: TriangularLogBump,
    phi_right: TriangularLogBump,
    B: float,
    conv_steps: int,
) -> float:
    """
    Floating toy prime component:

    sum Lambda(n) [F(n)+F_tilde(n)] for n <= exp(2B).
    """
    cutoff = int(math.floor(math.exp(2.0 * B)))
    total = 0.0

    for n in range(1, cutoff + 1):
        lam = von_mangoldt(n)
        if lam == 0.0:
            continue
        x = float(n)
        F_n = toy_convolution_with_star(phi_left, phi_right, x, conv_steps)
        Ft_n = tilde_value_of_F(phi_left, phi_right, x, conv_steps)
        total += lam * (F_n + Ft_n)

    return total


def archimedean_component(
    phi_left: TriangularLogBump,
    phi_right: TriangularLogBump,
    B: float,
    steps: int,
    conv_steps: int,
) -> float:
    """
    Floating toy archimedean component using the Bombieri-Lagarias displayed
    integrand shape over a finite interval.

    Not certified.
    """
    M = math.exp(2.0 * B)
    f1 = toy_convolution_with_star(phi_left, phi_right, 1.0, conv_steps)

    eps = 1e-5
    lo = 1.0 + eps
    hi = M

    def integrand(x: float) -> float:
        F = toy_convolution_with_star(phi_left, phi_right, x, conv_steps)
        Ft = tilde_value_of_F(phi_left, phi_right, x, conv_steps)
        numerator = F + Ft - (2.0 / (x * x)) * f1
        return numerator * x / (x * x - 1.0)

    finite_part = midpoint_integral(integrand, lo, hi, steps)

    # Toy finite-tail proxy. Not certified.
    tail_proxy = -f1 * math.log((M + 1.0) / (M - 1.0))

    return finite_part + tail_proxy


def compute_m00_prototype_value(integral_steps: int = 80, conv_steps: int = 80) -> Dict[str, float]:
    """
    Compute a toy floating-point prototype for M_00 under Bombieri-Lagarias normalization.

    This is not certified.
    """
    phi = TriangularLogBump(center=0.0, width=0.6)
    B = 1.2

    central = central_integral(phi, phi, B=B, steps=integral_steps, conv_steps=conv_steps)
    star_central = star_central_integral(phi, phi, B=B, steps=integral_steps, conv_steps=conv_steps)
    prime = finite_prime_sum(phi, phi, B=B, conv_steps=conv_steps)
    f_at_one = toy_convolution_with_star(phi, phi, 1.0, steps=conv_steps)
    constant = corrected_constant_component(f_at_one)
    arch = archimedean_component(phi, phi, B=B, steps=integral_steps, conv_steps=conv_steps)

    entry_value = central + star_central - prime + constant - arch

    return {
        "central_component": central,
        "star_central_component": star_central,
        "prime_component": prime,
        "f_at_one": f_at_one,
        "bombieri_lagarias_constant_component": constant,
        "archimedean_component": arch,
        "entry_value": entry_value,
    }


def make_m00_prototype_entry() -> Dict[str, Any]:
    c = BOMBIERI_LAGARIAS_CONVENTION
    comps = compute_m00_prototype_value()

    metadata = CertifiedEntryMetadata(
        entry_id="M_00_arith",
        basis_i=0,
        basis_j=0,
        source_name=c.source_name,
        normalization_label=c.normalization_label,
        mellin_transform=c.mellin_transform,
        involution=c.involution,
        conjugation_policy=c.conjugation_policy,
        convolution=c.convolution,
        constant_term=c.constant_term,
        pole_constraint_status=c.pole_constraint_status,
        certification_status=EntryCertificationStatus.PROTOTYPE_FLOATING_POINT,
        interval_value=None,
        error_decomposition=ErrorDecomposition(
            prime_sum_error="NOT_CERTIFIED",
            archimedean_quadrature_error="NOT_CERTIFIED",
            convolution_error="NOT_CERTIFIED",
            rounding_error="NOT_CERTIFIED",
            normalization_error="Bombieri-Lagarias constant used, but full convention still requires review",
            pole_constraint_error="POLE_CONSTRAINTS_PLAUSIBLE_NOT_FULLY_LOCKED",
        ),
        quadrature_method="midpoint floating-point toy quadrature",
        prime_cutoff="finite toy cutoff induced by B=1.2",
        archimedean_cutoff="toy finite cutoff B=1.2",
        reviewer_warnings=[
            "Prototype floating-point only.",
            "Not interval certified.",
            "Not a certified arithmetic matrix entry.",
            "Do not use for RH claims.",
        ],
    )

    return {
        "phase": "B10",
        "status": "PHASE_B10_PROTOTYPE_FLOATING_ENTRY_COMPLETE",
        "entry_metadata": metadata.to_dict(),
        "components": comps,
        "entry_is_certified": metadata.is_certified_interval_entry(),
        "normalization_check": {
            "used": "LOG_PI_GAMMA_NORMALIZATION_USED",
            "not_used": "EARLIER_LOG_4PI_GAMMA_NOT_USED",
        },
        "audit_strings": [
            "PHASE_B10_PROTOTYPE_FLOATING_ENTRY_COMPLETE",
            "M_00_ARITH_PROTOTYPE_FLOATING_ENTRY_CREATED",
            "BOMBIERI_LAGARIAS_CONSTANT_USED",
            "LOG_PI_GAMMA_NORMALIZATION_USED",
            "EARLIER_LOG_4PI_GAMMA_NOT_USED",
            "PROTOTYPE_FLOATING_POINT_ENTRY_NOT_CERTIFIED",
            "NUMERICAL_VALUE_COMPUTED_BUT_NOT_CERTIFIED",
            "BREAKTHROUGH_NOT_ACHIEVED",
            "READY_FOR_PHASE_B11_INTERVAL_CANDIDATE_ENTRY",
        ],
    }


def write_m00_prototype_entry(path: Path) -> None:
    payload = make_m00_prototype_entry()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_m00_prototype_entry(
        Path("breakthrough_push/phase_b10_prototype_floating_entry/M_00_prototype_floating_entry.json")
    )
    print("Wrote M_00 prototype floating entry")
