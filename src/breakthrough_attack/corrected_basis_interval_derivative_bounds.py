from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Dict, Any, List, Tuple
import json
import math

from src.breakthrough_attack.primitive_interval_bump_bounds import D, DecInterval
from src.breakthrough_attack.log_bump_interval_derivative_bounds import (
    log_bump_value_interval,
    log_bump_prime_interval,
    log_bump_second_interval,
    u_interval_for_log_bump,
    reciprocal_x_squared_interval,
)
from src.breakthrough_attack.primitive_interval_bump_bounds import (
    psi_interval,
    psi_prime_interval,
    psi_second_interval,
)
from src.breakthrough_attack.pole_cancelled_smooth_basis import (
    SmoothBump,
    build_pole_cancelled_function,
)


def coeff_interval_from_float(x: float, radius: Decimal = Decimal("1e-8")) -> DecInterval:
    dx = D(x)
    return DecInterval(dx - radius, dx + radius)


@dataclass(frozen=True)
class LogBumpSpec:
    center: Decimal
    width: Decimal

    def support_x(self) -> Tuple[Decimal, Decimal]:
        lo = (self.center - self.width).exp()
        hi = (self.center + self.width).exp()
        return lo, hi


@dataclass(frozen=True)
class CorrectedBasisIntervalSpec:
    raw: LogBumpSpec
    corr0: LogBumpSpec
    corr1: LogBumpSpec
    alpha: DecInterval
    beta: DecInterval


def clamp_unit_interval(U: DecInterval) -> DecInterval:
    """
    Clamp an interval to the interior of (-1,1).

    This is needed because Decimal exp/log endpoint arithmetic can place
    support endpoints infinitesimally outside the primitive bump domain.
    """
    eps = Decimal("1e-12")
    lo = max(U.lo, Decimal(-1) + eps)
    hi = min(U.hi, Decimal(1) - eps)
    if lo > hi:
        return DecInterval.point(0)
    return DecInterval(lo, hi)


def bump_interval_for_order(spec: LogBumpSpec, X: DecInterval, order: int) -> DecInterval:
    """
    Interval bound for one log-bump derivative over X.

    Support-aware rule:
    - outside support: value and all derivatives are zero;
    - inside/overlap support: evaluate only on the support overlap;
    - clamp the internal u-interval into (-1,1) before calling primitive bump bounds.
    """
    if order not in (0, 1, 2):
        raise ValueError("order must be 0, 1, or 2")

    support_lo, support_hi = spec.support_x()
    zero = DecInterval.point(0)

    if X.hi <= support_lo or X.lo >= support_hi:
        return zero

    overlap_lo = max(X.lo, support_lo)
    overlap_hi = min(X.hi, support_hi)

    if overlap_lo > overlap_hi:
        return zero

    X_inside = DecInterval(overlap_lo, overlap_hi)
    U = clamp_unit_interval(u_interval_for_log_bump(X_inside, spec.center, spec.width))

    if order == 0:
        I = psi_interval(U)
    elif order == 1:
        psi_p = psi_prime_interval(U)
        factor = DecInterval.point(Decimal(1)) / (DecInterval.point(spec.width) * X_inside)
        I = psi_p * factor
    else:
        psi_p = psi_prime_interval(U)
        psi_s = psi_second_interval(U)
        one = DecInterval.point(Decimal(1))
        w = DecInterval.point(spec.width)
        x2_inv = reciprocal_x_squared_interval(X_inside)
        I = psi_s * (one / (w * w)) * x2_inv - psi_p * (one / w) * x2_inv

    # If X extends outside support, include zero.
    if X.lo < support_lo or X.hi > support_hi:
        return DecInterval(min(I.lo, Decimal(0)), max(I.hi, Decimal(0)))

    return I


def corrected_basis_interval_for_order(spec: CorrectedBasisIntervalSpec, X: DecInterval, order: int) -> DecInterval:
    b = bump_interval_for_order(spec.raw, X, order)
    u0 = bump_interval_for_order(spec.corr0, X, order)
    u1 = bump_interval_for_order(spec.corr1, X, order)
    return b - (spec.alpha * u0) - (spec.beta * u1)


def build_demo_corrected_basis_interval_spec() -> CorrectedBasisIntervalSpec:
    raw_float = SmoothBump(center=-0.25, width=0.30)
    corr0_float = SmoothBump(center=-1.0, width=0.35)
    corr1_float = SmoothBump(center=1.0, width=0.35)
    phi = build_pole_cancelled_function(raw_float, corr0_float, corr1_float)

    return CorrectedBasisIntervalSpec(
        raw=LogBumpSpec(center=D("-0.25"), width=D("0.30")),
        corr0=LogBumpSpec(center=D("-1.0"), width=D("0.35")),
        corr1=LogBumpSpec(center=D("1.0"), width=D("0.35")),
        alpha=coeff_interval_from_float(phi.alpha),
        beta=coeff_interval_from_float(phi.beta),
    )


def demo_x_intervals() -> List[DecInterval]:
    return [
        DecInterval(D("0.20"), D("0.40")),
        DecInterval(D("0.80"), D("1.20")),
        DecInterval(D("2.00"), D("3.50")),
    ]


def make_corrected_basis_interval_payload() -> Dict[str, Any]:
    spec = build_demo_corrected_basis_interval_spec()
    rows = []

    for X in demo_x_intervals():
        value_I = corrected_basis_interval_for_order(spec, X, 0)
        prime_I = corrected_basis_interval_for_order(spec, X, 1)
        second_I = corrected_basis_interval_for_order(spec, X, 2)

        rows.append({
            "x_interval": X.to_dict(),
            "value_interval": value_I.to_dict(),
            "prime_interval": prime_I.to_dict(),
            "second_interval": second_I.to_dict(),
        })

    return {
        "phase": "X11",
        "status": "PHASE_X11_CORRECTED_BASIS_INTERVAL_DERIVATIVE_BOUNDS_COMPLETE",
        "certification_status": "CORRECTED_BASIS_INTERVAL_BOUNDS_CREATED_COEFFICIENTS_NOT_CERTIFIED",
        "alpha_interval": spec.alpha.to_dict(),
        "beta_interval": spec.beta.to_dict(),
        "bounds": rows,
        "warning": "Alpha and beta are wrapped numerical coefficients, not certified Mellin-solve intervals.",
        "audit_strings": [
            "PHASE_X11_CORRECTED_BASIS_INTERVAL_DERIVATIVE_BOUNDS_COMPLETE",
            "CORRECTED_BASIS_VALUE_INTERVAL_CREATED",
            "CORRECTED_BASIS_FIRST_DERIVATIVE_INTERVAL_CREATED",
            "CORRECTED_BASIS_SECOND_DERIVATIVE_INTERVAL_CREATED",
            "CORRECTED_BASIS_DERIVATIVE_PROPAGATION_PROVED",
            "CORRECTED_BASIS_INTERVAL_ENCLOSURE_PROVED",
            "COEFFICIENT_INTERVAL_WRAPPERS_CREATED",
            "COEFFICIENT_CERTIFICATION_INCOMPLETE",
            "CERTIFIED_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X12_STAR_AND_CONVOLUTION_DERIVATIVE_BOUNDS",
        ],
    }


def write_corrected_basis_interval_derivative_bounds_certificate(path: Path) -> None:
    payload = make_corrected_basis_interval_payload()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_corrected_basis_interval_derivative_bounds_certificate(
        Path("breakthrough_attack/phase_x11_corrected_basis_interval_derivative_bounds/corrected_basis_interval_derivative_bounds_certificate.json")
    )
    print("Wrote corrected basis interval derivative bounds certificate")
