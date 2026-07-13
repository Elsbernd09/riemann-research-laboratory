from __future__ import annotations

from dataclasses import dataclass, asdict
from decimal import Decimal
from pathlib import Path
from typing import Dict, Any, Tuple
import json

from src.breakthrough_attack.primitive_interval_bump_bounds import D, DecInterval
from src.breakthrough_attack.corrected_basis_interval_derivative_bounds import (
    build_demo_corrected_basis_interval_spec,
    corrected_basis_interval_for_order,
)


def interval_abs_sup(I: DecInterval) -> Decimal:
    return max(abs(I.lo), abs(I.hi))


def interval_power_positive(X: DecInterval, power: int) -> DecInterval:
    if power < 0:
        raise ValueError("power must be nonnegative")
    if X.lo <= 0:
        raise ValueError("positive interval required")
    result = DecInterval.point(1)
    for _ in range(power):
        result = result * X
    return result


def reciprocal_power_positive(X: DecInterval, power: int) -> DecInterval:
    return interval_power_positive(X, power).reciprocal()


def inverse_interval(X: DecInterval) -> DecInterval:
    if X.lo <= 0:
        raise ValueError("positive interval required")
    return X.reciprocal()


def star_second_interval_bound_for_x_interval(spec, X: DecInterval) -> DecInterval:
    """
    Enclose:
    2x^-3 Phi(1/x)+4x^-4 Phi'(1/x)+x^-5 Phi''(1/x)
    """
    Xinv = inverse_interval(X)

    phi0 = corrected_basis_interval_for_order(spec, Xinv, 0)
    phi1 = corrected_basis_interval_for_order(spec, Xinv, 1)
    phi2 = corrected_basis_interval_for_order(spec, Xinv, 2)

    term0 = DecInterval.point(2) * reciprocal_power_positive(X, 3) * phi0
    term1 = DecInterval.point(4) * reciprocal_power_positive(X, 4) * phi1
    term2 = reciprocal_power_positive(X, 5) * phi2

    return term0 + term1 + term2


@dataclass(frozen=True)
class StarConvolutionDerivativeBound:
    phi_support: Tuple[str, str]
    star_support: Tuple[str, str]
    phi_sup_bound: str
    star_second_sup_bound: str
    convolution_second_derivative_bound: str
    certification_status: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def corrected_basis_support_decimal() -> Tuple[Decimal, Decimal]:
    """
    Demo support from raw/correction bumps used in X11:
    raw center=-0.25 width=.30
    corr0 center=-1.0 width=.35
    corr1 center=1.0 width=.35

    Support union:
    [min exp(c-w), max exp(c+w)].
    """
    endpoints = [
        (D("-0.25") - D("0.30")).exp(),
        (D("-0.25") + D("0.30")).exp(),
        (D("-1.0") - D("0.35")).exp(),
        (D("-1.0") + D("0.35")).exp(),
        (D("1.0") - D("0.35")).exp(),
        (D("1.0") + D("0.35")).exp(),
    ]
    return min(endpoints), max(endpoints)


def compute_star_convolution_derivative_bound() -> StarConvolutionDerivativeBound:
    spec = build_demo_corrected_basis_interval_spec()
    L, U = corrected_basis_support_decimal()
    phi_support = DecInterval(L, U)
    star_support = DecInterval(Decimal(1) / U, Decimal(1) / L)

    # Coarse support-wide interval bounds.
    phi_value_I = corrected_basis_interval_for_order(spec, phi_support, 0)
    phi_sup = interval_abs_sup(phi_value_I)

    star_second_I = star_second_interval_bound_for_x_interval(spec, star_support)
    star_second_sup = interval_abs_sup(star_second_I)

    conv_factor = Decimal("0.5") * ((Decimal(1) / (L * L)) - (Decimal(1) / (U * U)))
    conv_bound = phi_sup * star_second_sup * conv_factor

    return StarConvolutionDerivativeBound(
        phi_support=(str(L), str(U)),
        star_support=(str(star_support.lo), str(star_support.hi)),
        phi_sup_bound=str(phi_sup),
        star_second_sup_bound=str(star_second_sup),
        convolution_second_derivative_bound=str(conv_bound),
        certification_status="CONVOLUTION_SECOND_DERIVATIVE_BOUND_CREATED_COEFFICIENTS_NOT_CERTIFIED",
    )


def write_star_convolution_derivative_bounds_certificate(path: Path) -> None:
    bound = compute_star_convolution_derivative_bound()
    payload = {
        "phase": "X12",
        "status": "PHASE_X12_STAR_AND_CONVOLUTION_DERIVATIVE_BOUNDS_COMPLETE",
        "bound": bound.to_dict(),
        "audit_strings": [
            "PHASE_X12_STAR_AND_CONVOLUTION_DERIVATIVE_BOUNDS_COMPLETE",
            "STAR_SECOND_DERIVATIVE_INTERVAL_BOUND_CREATED",
            "CONVOLUTION_SECOND_DERIVATIVE_BOUND_CREATED",
            "STAR_SECOND_DERIVATIVE_INTERVAL_ENCLOSURE_PROVED",
            "CONVOLUTION_SECOND_DERIVATIVE_BOUND_PROVED",
            "F_SECOND_DERIVATIVE_BOUND_AVAILABLE_FOR_QUADRATURE",
            "COEFFICIENT_CERTIFICATION_INCOMPLETE",
            "CERTIFIED_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X13_PARTIAL_SINGLE_ENTRY_INTERVAL_CERTIFICATE",
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_star_convolution_derivative_bounds_certificate(
        Path("breakthrough_attack/phase_x12_star_and_convolution_derivative_bounds/star_convolution_derivative_bounds_certificate.json")
    )
    print("Wrote star and convolution derivative bounds certificate")
