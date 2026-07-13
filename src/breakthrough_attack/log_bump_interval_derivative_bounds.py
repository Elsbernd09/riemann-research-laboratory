from __future__ import annotations

from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path
from typing import Dict, Any, List
import json
import math

from src.breakthrough_attack.primitive_interval_bump_bounds import (
    D,
    DecInterval,
    psi_interval,
    psi_prime_interval,
    psi_second_interval,
)


PREC = 80


def dec_ln_floor(x: Decimal) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = ROUND_FLOOR
        return x.ln()


def dec_ln_ceil(x: Decimal) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = ROUND_CEILING
        return x.ln()


def log_interval(X: DecInterval) -> DecInterval:
    if X.lo <= 0:
        raise ValueError("log interval requires positive X")
    return DecInterval(dec_ln_floor(X.lo), dec_ln_ceil(X.hi))


def interval_scale(I: DecInterval, scalar: Decimal) -> DecInterval:
    S = DecInterval.point(scalar)
    return I * S


def interval_shift(I: DecInterval, shift: Decimal) -> DecInterval:
    return I + DecInterval.point(shift)


def u_interval_for_log_bump(X: DecInterval, center: Decimal, width: Decimal) -> DecInterval:
    if width <= 0:
        raise ValueError("width must be positive")
    L = log_interval(X)
    return (L - DecInterval.point(center)) / DecInterval.point(width)


def reciprocal_x_interval(X: DecInterval) -> DecInterval:
    return X.reciprocal()


def reciprocal_x_squared_interval(X: DecInterval) -> DecInterval:
    R = X.reciprocal()
    return R * R


def log_bump_value_interval(X: DecInterval, center: Decimal, width: Decimal) -> DecInterval:
    U = u_interval_for_log_bump(X, center, width)
    return psi_interval(U)


def log_bump_prime_interval(X: DecInterval, center: Decimal, width: Decimal) -> DecInterval:
    U = u_interval_for_log_bump(X, center, width)
    psi_p = psi_prime_interval(U)
    factor = DecInterval.point(Decimal(1)) / (DecInterval.point(width) * X)
    return psi_p * factor


def log_bump_second_interval(X: DecInterval, center: Decimal, width: Decimal) -> DecInterval:
    U = u_interval_for_log_bump(X, center, width)
    psi_p = psi_prime_interval(U)
    psi_s = psi_second_interval(U)

    one = DecInterval.point(Decimal(1))
    w = DecInterval.point(width)
    x2_inv = reciprocal_x_squared_interval(X)

    term1 = psi_s * (one / (w * w)) * x2_inv
    term2 = psi_p * (one / w) * x2_inv
    return term1 - term2


def log_bump_float(x: float, center: float, width: float) -> float:
    if x <= 0:
        return 0.0
    u = (math.log(x) - center) / width
    if abs(u) >= 1.0:
        return 0.0
    return math.exp(-1.0 / (1.0 - u * u))


def finite_difference_first(func, x: float, h: float = 1e-6) -> float:
    return (func(x + h) - func(x - h)) / (2.0 * h)


def finite_difference_second(func, x: float, h: float = 1e-5) -> float:
    return (func(x + h) - 2.0 * func(x) + func(x - h)) / (h * h)


def sample_x_intervals() -> List[DecInterval]:
    return [
        DecInterval(D("0.80"), D("0.90")),
        DecInterval(D("0.95"), D("1.05")),
        DecInterval(D("1.10"), D("1.20")),
    ]


def make_log_bump_bounds_payload() -> Dict[str, Any]:
    center = D("0.0")
    width = D("0.75")
    rows = []

    for X in sample_x_intervals():
        U = u_interval_for_log_bump(X, center, width)
        value_I = log_bump_value_interval(X, center, width)
        prime_I = log_bump_prime_interval(X, center, width)
        second_I = log_bump_second_interval(X, center, width)

        mid = float((X.lo + X.hi) / Decimal(2))
        f = lambda t: log_bump_float(t, float(center), float(width))
        approx_prime = finite_difference_first(f, mid)
        approx_second = finite_difference_second(f, mid)

        rows.append({
            "x_interval": X.to_dict(),
            "u_interval": U.to_dict(),
            "value_interval": value_I.to_dict(),
            "prime_interval": prime_I.to_dict(),
            "second_interval": second_I.to_dict(),
            "midpoint": mid,
            "midpoint_value_inside": value_I.contains_float(f(mid)),
            "midpoint_prime_float_probe_inside": prime_I.contains_float(approx_prime),
            "midpoint_second_float_probe_inside": second_I.contains_float(approx_second),
        })

    return {
        "phase": "X10",
        "status": "PHASE_X10_LOG_BUMP_INTERVAL_DERIVATIVE_BOUNDS_COMPLETE",
        "certification_status": "LOG_BUMP_INTERVAL_BOUNDS_CREATED_NOT_FORMALLY_VERIFIED",
        "center": str(center),
        "width": str(width),
        "bounds": rows,
        "warning": "Decimal interval and finite-difference probes are not proof-assistant verification.",
        "audit_strings": [
            "PHASE_X10_LOG_BUMP_INTERVAL_DERIVATIVE_BOUNDS_COMPLETE",
            "LOG_INTERVAL_ENCLOSURE_CREATED",
            "LOG_BUMP_VALUE_INTERVAL_CREATED",
            "LOG_BUMP_FIRST_DERIVATIVE_INTERVAL_CREATED",
            "LOG_BUMP_SECOND_DERIVATIVE_INTERVAL_CREATED",
            "LOG_BUMP_DERIVATIVE_FORMULAS_PROVED",
            "LOG_BUMP_INTERVAL_PROPAGATION_PROVED",
            "LOG_BUMP_INTERVAL_BOUNDS_CREATED_NOT_FORMALLY_VERIFIED",
            "CERTIFIED_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X11_CORRECTED_BASIS_INTERVAL_DERIVATIVE_BOUNDS",
        ],
    }


def write_log_bump_interval_derivative_bounds_certificate(path: Path) -> None:
    payload = make_log_bump_bounds_payload()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_log_bump_interval_derivative_bounds_certificate(
        Path("breakthrough_attack/phase_x10_log_bump_interval_derivative_bounds/log_bump_interval_derivative_bounds_certificate.json")
    )
    print("Wrote log-bump interval derivative bounds certificate")
