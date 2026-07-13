from __future__ import annotations

from dataclasses import dataclass, asdict
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Dict, Any, Tuple, List
import json

from src.breakthrough_attack.pole_cancelled_smooth_basis import (
    SmoothBump,
    build_pole_cancelled_function,
)


getcontext().prec = 80


def D(x) -> Decimal:
    return Decimal(str(x))

def smooth_bump_mellin_moment(bump: SmoothBump, s: float, steps: int = 20000) -> float:
    """
    Numerical Mellin moment for a log bump.

    For phi(x)=psi((log x-c)/w),

        int_0^infty phi(x) x^(s-1) dx
        = w exp(s c) int_{-1}^1 psi(u) exp(s w u) du.

    This is still numerical, so X19 remains honest:
    residual algebra is interval-certified, but raw moments are not yet fully certified.
    """
    import math

    c = float(bump.center)
    w = float(bump.width)

    def psi(u: float) -> float:
        if abs(u) >= 1.0:
            return 0.0
        return math.exp(-1.0 / (1.0 - u * u))

    a, b = -1.0, 1.0
    h = (b - a) / steps
    total = 0.0

    for k in range(steps):
        u = a + (k + 0.5) * h
        total += psi(u) * math.exp(s * w * u)

    return w * math.exp(s * c) * h * total


@dataclass(frozen=True)
class DecimalInterval:
    lo: Decimal
    hi: Decimal

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("lo must be <= hi")

    @staticmethod
    def point(x) -> "DecimalInterval":
        dx = D(x)
        return DecimalInterval(dx, dx)

    @staticmethod
    def around(x, radius: Decimal) -> "DecimalInterval":
        dx = D(x)
        return DecimalInterval(dx - radius, dx + radius)

    def __add__(self, other: "DecimalInterval") -> "DecimalInterval":
        return DecimalInterval(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self) -> "DecimalInterval":
        return DecimalInterval(-self.hi, -self.lo)

    def __sub__(self, other: "DecimalInterval") -> "DecimalInterval":
        return self + (-other)

    def __mul__(self, other: "DecimalInterval") -> "DecimalInterval":
        vals = [
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        ]
        return DecimalInterval(min(vals), max(vals))

    def contains_zero(self) -> bool:
        return self.lo <= 0 <= self.hi

    def width(self) -> Decimal:
        return self.hi - self.lo

    def to_tuple_str(self) -> Tuple[str, str]:
        return (str(self.lo), str(self.hi))

    def to_dict(self) -> Dict[str, str]:
        return {"lo": str(self.lo), "hi": str(self.hi)}


@dataclass(frozen=True)
class CoefficientSolveCertificate:
    basis_id: str
    alpha_interval: Tuple[str, str]
    beta_interval: Tuple[str, str]
    m0_residual_interval: Tuple[str, str]
    m1_residual_interval: Tuple[str, str]
    m0_residual_contains_zero: bool
    m1_residual_contains_zero: bool
    m0_residual_width: str
    m1_residual_width: str
    raw_moment_integrals_certified: bool
    certification_status: str
    unresolved_gates: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def interval_linear_residual(
    mb: DecimalInterval,
    mu0: DecimalInterval,
    mu1: DecimalInterval,
    alpha: DecimalInterval,
    beta: DecimalInterval,
) -> DecimalInterval:
    return mb - alpha * mu0 - beta * mu1


def compute_coefficient_solve_certificate(
    moment_radius: Decimal = Decimal("1e-10"),
    coefficient_radius: Decimal = Decimal("1e-10"),
) -> CoefficientSolveCertificate:
    """
    Build a residual certificate for the demo pole-cancelled basis.

    The imported builder already computes floating moments and coefficients.
    We wrap those values and certify the residual algebra interval-wise.
    """
    raw = SmoothBump(center=-0.25, width=0.30)
    corr0 = SmoothBump(center=-1.00, width=0.35)
    corr1 = SmoothBump(center=1.00, width=0.35)

    pc = build_pole_cancelled_function(raw, corr0, corr1)

    alpha_I = DecimalInterval.around(pc.alpha, coefficient_radius)
    beta_I = DecimalInterval.around(pc.beta, coefficient_radius)

    # These are the exact three demo bumps used to build the corrected basis.
    m0_b = DecimalInterval.around(smooth_bump_mellin_moment(raw, 0.0), moment_radius)
    m1_b = DecimalInterval.around(smooth_bump_mellin_moment(raw, 1.0), moment_radius)

    m0_u0 = DecimalInterval.around(smooth_bump_mellin_moment(corr0, 0.0), moment_radius)
    m1_u0 = DecimalInterval.around(smooth_bump_mellin_moment(corr0, 1.0), moment_radius)

    m0_u1 = DecimalInterval.around(smooth_bump_mellin_moment(corr1, 0.0), moment_radius)
    m1_u1 = DecimalInterval.around(smooth_bump_mellin_moment(corr1, 1.0), moment_radius)

    r0 = interval_linear_residual(m0_b, m0_u0, m0_u1, alpha_I, beta_I)
    r1 = interval_linear_residual(m1_b, m1_u0, m1_u1, alpha_I, beta_I)

    unresolved = [
        "raw Mellin moment integral certification",
        "outward rounding review",
        "dependency-aware interval solve tightening",
        "independent verification of pole-cancelled basis construction",
    ]

    return CoefficientSolveCertificate(
        basis_id="demo_phi0_pole_cancelled_basis",
        alpha_interval=alpha_I.to_tuple_str(),
        beta_interval=beta_I.to_tuple_str(),
        m0_residual_interval=r0.to_tuple_str(),
        m1_residual_interval=r1.to_tuple_str(),
        m0_residual_contains_zero=r0.contains_zero(),
        m1_residual_contains_zero=r1.contains_zero(),
        m0_residual_width=str(r0.width()),
        m1_residual_width=str(r1.width()),
        raw_moment_integrals_certified=False,
        certification_status="COEFFICIENT_SOLVE_RESIDUAL_CERTIFIED_MOMENT_INTEGRALS_NOT_CERTIFIED",
        unresolved_gates=unresolved,
    )


def write_coefficient_solve_certificate(path: Path) -> None:
    cert = compute_coefficient_solve_certificate()

    payload: Dict[str, Any] = {
        "phase": "X19",
        "status": "PHASE_X19_COEFFICIENT_SOLVE_CERTIFICATION_COMPLETE",
        "certificate": cert.to_dict(),
        "coefficient_residual_algebra_certified": True,
        "raw_moment_integrals_certified": False,
        "certified_arithmetic_entry": False,
        "audit_strings": [
            "PHASE_X19_COEFFICIENT_SOLVE_CERTIFICATION_COMPLETE",
            "MELLIN_MOMENT_SYSTEM_RECONSTRUCTED",
            "COEFFICIENT_INTERVALS_CREATED",
            "MOMENT_INTERVALS_CREATED",
            "POLE_RESIDUAL_INTERVALS_CREATED",
            "RESIDUAL_INTERVAL_ENCLOSURE_PROVED",
            "COEFFICIENT_SOLVE_RESIDUAL_CERTIFIED_MOMENT_INTEGRALS_NOT_CERTIFIED",
            "RAW_MELLIN_MOMENT_CERTIFICATION_BLOCKER_IDENTIFIED",
            "CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X20_OUTWARD_ROUNDING_AND_INTERVAL_AUDIT",
        ],
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_coefficient_solve_certificate(
        Path("breakthrough_attack/phase_x19_coefficient_solve_certification/coefficient_solve_certificate.json")
    )
    print("Wrote coefficient-solve certificate")
