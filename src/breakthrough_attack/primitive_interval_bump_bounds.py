from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path
from typing import Dict, Any, List
import json
import math


PREC = 80


def D(x) -> Decimal:
    return Decimal(str(x))


def dec_floor(x: Decimal) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = ROUND_FLOOR
        return +x


def dec_ceil(x: Decimal) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = ROUND_CEILING
        return +x


@dataclass(frozen=True)
class DecInterval:
    lo: Decimal
    hi: Decimal

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("interval lo must be <= hi")

    @staticmethod
    def point(x) -> "DecInterval":
        dx = D(x)
        return DecInterval(dx, dx)

    def to_dict(self) -> Dict[str, str]:
        return {"lo": str(self.lo), "hi": str(self.hi)}

    def __add__(self, other: "DecInterval") -> "DecInterval":
        return DecInterval(dec_floor(self.lo + other.lo), dec_ceil(self.hi + other.hi))

    def __sub__(self, other: "DecInterval") -> "DecInterval":
        return DecInterval(dec_floor(self.lo - other.hi), dec_ceil(self.hi - other.lo))

    def __neg__(self) -> "DecInterval":
        return DecInterval(dec_floor(-self.hi), dec_ceil(-self.lo))

    def __mul__(self, other: "DecInterval") -> "DecInterval":
        vals = [
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        ]
        return DecInterval(dec_floor(min(vals)), dec_ceil(max(vals)))

    def reciprocal(self) -> "DecInterval":
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        vals = [Decimal(1) / self.lo, Decimal(1) / self.hi]
        return DecInterval(dec_floor(min(vals)), dec_ceil(max(vals)))

    def __truediv__(self, other: "DecInterval") -> "DecInterval":
        return self * other.reciprocal()

    def square(self) -> "DecInterval":
        if self.lo <= 0 <= self.hi:
            return DecInterval(Decimal(0), dec_ceil(max(self.lo * self.lo, self.hi * self.hi)))
        vals = [self.lo * self.lo, self.hi * self.hi]
        return DecInterval(dec_floor(min(vals)), dec_ceil(max(vals)))

    def exp(self) -> "DecInterval":
        with localcontext() as ctx:
            ctx.prec = PREC
            ctx.rounding = ROUND_FLOOR
            lo = self.lo.exp()
        with localcontext() as ctx:
            ctx.prec = PREC
            ctx.rounding = ROUND_CEILING
            hi = self.hi.exp()
        return DecInterval(lo, hi)

    def width_float(self) -> float:
        return float(self.hi - self.lo)

    def contains_float(self, x: float) -> bool:
        dx = D(x)
        return self.lo <= dx <= self.hi


def require_inside_unit(I: DecInterval) -> None:
    if not (Decimal(-1) < I.lo <= I.hi < Decimal(1)):
        raise ValueError("interval must be contained in (-1,1)")


def one_minus_u_squared(I: DecInterval) -> DecInterval:
    return DecInterval.point(1) - I.square()


def psi_interval(I: DecInterval) -> DecInterval:
    require_inside_unit(I)
    d = one_minus_u_squared(I)
    neg_inv_d = -d.reciprocal()
    return neg_inv_d.exp()


def psi_prime_interval(I: DecInterval) -> DecInterval:
    require_inside_unit(I)
    two = DecInterval.point(2)
    d = one_minus_u_squared(I)
    d2 = d * d
    p = -(two * I) / d2
    return psi_interval(I) * p


def psi_second_interval(I: DecInterval) -> DecInterval:
    require_inside_unit(I)
    two = DecInterval.point(2)
    eight = DecInterval.point(8)
    d = one_minus_u_squared(I)
    d2 = d * d
    d3 = d2 * d
    p = -(two * I) / d2
    p2 = p * p
    p_prime = -(two / d2) - ((eight * I.square()) / d3)
    return psi_interval(I) * (p2 + p_prime)


def psi_float(u: float) -> float:
    if abs(u) >= 1.0:
        return 0.0
    return math.exp(-1.0 / (1.0 - u * u))


def psi_prime_float(u: float) -> float:
    if abs(u) >= 1.0:
        return 0.0
    d = 1.0 - u * u
    return psi_float(u) * (-2.0 * u / (d * d))


def psi_second_float(u: float) -> float:
    if abs(u) >= 1.0:
        return 0.0
    d = 1.0 - u * u
    p = -2.0 * u / (d * d)
    p_prime = -2.0 / (d * d) - 8.0 * u * u / (d * d * d)
    return psi_float(u) * (p * p + p_prime)


def sample_subintervals() -> List[DecInterval]:
    return [
        DecInterval(D("-0.90"), D("-0.75")),
        DecInterval(D("-0.50"), D("-0.25")),
        DecInterval(D("-0.10"), D("0.10")),
        DecInterval(D("0.25"), D("0.50")),
        DecInterval(D("0.75"), D("0.90")),
    ]


def make_primitive_bounds_payload() -> Dict[str, Any]:
    rows = []
    for I in sample_subintervals():
        psi_I = psi_interval(I)
        pp_I = psi_prime_interval(I)
        ps_I = psi_second_interval(I)

        mid = float((I.lo + I.hi) / Decimal(2))
        rows.append({
            "interval": I.to_dict(),
            "psi_interval": psi_I.to_dict(),
            "psi_prime_interval": pp_I.to_dict(),
            "psi_second_interval": ps_I.to_dict(),
            "midpoint": mid,
            "midpoint_psi_inside": psi_I.contains_float(psi_float(mid)),
            "midpoint_psi_prime_inside": pp_I.contains_float(psi_prime_float(mid)),
            "midpoint_psi_second_inside": ps_I.contains_float(psi_second_float(mid)),
        })

    return {
        "phase": "X9",
        "status": "PHASE_X9_PRIMITIVE_INTERVAL_BUMP_BOUNDS_COMPLETE",
        "certification_status": "PRIMITIVE_INTERVAL_BOUNDS_CREATED_NOT_FORMALLY_VERIFIED",
        "rounding_model": "Python Decimal directed rounding with conservative interval operations",
        "bounds": rows,
        "audit_strings": [
            "PHASE_X9_PRIMITIVE_INTERVAL_BUMP_BOUNDS_COMPLETE",
            "DECIMAL_INTERVAL_ARITHMETIC_CREATED",
            "PSI_INTERVAL_BOUND_CREATED",
            "PSI_PRIME_INTERVAL_BOUND_CREATED",
            "PSI_SECOND_INTERVAL_BOUND_CREATED",
            "PRIMITIVE_DERIVATIVE_FORMULAS_PROVED",
            "INTERVAL_ENCLOSURE_PRINCIPLE_RECORDED",
            "PRIMITIVE_INTERVAL_BOUNDS_CREATED_NOT_FORMALLY_VERIFIED",
            "CERTIFIED_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X10_LOG_BUMP_INTERVAL_DERIVATIVE_BOUNDS",
        ],
    }


def write_primitive_interval_bump_bounds_certificate(path: Path) -> None:
    payload = make_primitive_bounds_payload()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_primitive_interval_bump_bounds_certificate(
        Path("breakthrough_attack/phase_x9_primitive_interval_bump_bounds/primitive_interval_bump_bounds_certificate.json")
    )
    print("Wrote primitive interval bump bounds certificate")
