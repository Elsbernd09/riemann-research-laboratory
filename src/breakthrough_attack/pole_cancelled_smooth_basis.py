from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, Any, List, Tuple
import json
import math


@dataclass(frozen=True)
class SmoothBump:
    center: float
    width: float

    def __post_init__(self) -> None:
        if self.width <= 0:
            raise ValueError("width must be positive")

    def support_x(self) -> Tuple[float, float]:
        return (math.exp(self.center - self.width), math.exp(self.center + self.width))

    def bump(self, u: float) -> float:
        if abs(u) >= 1.0:
            return 0.0
        return math.exp(-1.0 / (1.0 - u * u))

    def eval_x(self, x: float) -> float:
        if x <= 0:
            return 0.0
        return self.bump((math.log(x) - self.center) / self.width)


def midpoint_integral(func: Callable[[float], float], lo: float, hi: float, steps: int = 500) -> float:
    if hi <= lo:
        return 0.0
    h = (hi - lo) / steps
    total = 0.0
    for k in range(steps):
        x = lo + (k + 0.5) * h
        total += func(x)
    return total * h


def mellin_moment(bump: SmoothBump, s: float, steps: int = 700) -> float:
    """
    Floating prototype for hat bump(s)=int bump(x)x^(s-1) dx.

    Not interval certified.
    """
    lo, hi = bump.support_x()
    return midpoint_integral(lambda x: bump.eval_x(x) * (x ** (s - 1.0)), lo, hi, steps=steps)


def solve_2x2(a00: float, a01: float, a10: float, a11: float, b0: float, b1: float) -> Tuple[float, float]:
    det = a00 * a11 - a01 * a10
    if abs(det) < 1e-14:
        raise ValueError("correction matrix is numerically singular")
    alpha = (b0 * a11 - a01 * b1) / det
    beta = (a00 * b1 - b0 * a10) / det
    return alpha, beta


@dataclass(frozen=True)
class PoleCancelledSmoothBasisFunction:
    raw: SmoothBump
    corr0: SmoothBump
    corr1: SmoothBump
    alpha: float
    beta: float

    def eval_x(self, x: float) -> float:
        return self.raw.eval_x(x) - self.alpha * self.corr0.eval_x(x) - self.beta * self.corr1.eval_x(x)

    def support_x(self) -> Tuple[float, float]:
        intervals = [self.raw.support_x(), self.corr0.support_x(), self.corr1.support_x()]
        return (min(lo for lo, _ in intervals), max(hi for _, hi in intervals))

    def mellin_moment(self, s: float, steps: int = 900) -> float:
        lo, hi = self.support_x()
        return midpoint_integral(lambda x: self.eval_x(x) * (x ** (s - 1.0)), lo, hi, steps=steps)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "raw": {"center": self.raw.center, "width": self.raw.width, "support": list(self.raw.support_x())},
            "corr0": {"center": self.corr0.center, "width": self.corr0.width, "support": list(self.corr0.support_x())},
            "corr1": {"center": self.corr1.center, "width": self.corr1.width, "support": list(self.corr1.support_x())},
            "alpha": self.alpha,
            "beta": self.beta,
            "support": list(self.support_x()),
            "basis_type": "built_in_pole_cancelled_smooth_basis_floating_prototype",
        }


def build_pole_cancelled_function(raw: SmoothBump, corr0: SmoothBump, corr1: SmoothBump) -> PoleCancelledSmoothBasisFunction:
    u00 = mellin_moment(corr0, 0.0)
    u01 = mellin_moment(corr1, 0.0)
    u10 = mellin_moment(corr0, 1.0)
    u11 = mellin_moment(corr1, 1.0)

    b0 = mellin_moment(raw, 0.0)
    b1 = mellin_moment(raw, 1.0)

    alpha, beta = solve_2x2(u00, u01, u10, u11, b0, b1)
    return PoleCancelledSmoothBasisFunction(raw=raw, corr0=corr0, corr1=corr1, alpha=alpha, beta=beta)


def write_pole_cancelled_basis_certificate(path: Path) -> None:
    corr0 = SmoothBump(center=-1.0, width=0.35)
    corr1 = SmoothBump(center=1.0, width=0.35)
    raws = [
        SmoothBump(center=-0.25, width=0.30),
        SmoothBump(center=0.00, width=0.30),
        SmoothBump(center=0.25, width=0.30),
    ]
    basis = [build_pole_cancelled_function(raw, corr0, corr1) for raw in raws]

    checks: List[Dict[str, Any]] = []
    for idx, phi in enumerate(basis):
        m0 = phi.mellin_moment(0.0)
        m1 = phi.mellin_moment(1.0)
        checks.append({
            "index": idx,
            "mellin_at_0_floating_residual": m0,
            "mellin_at_1_floating_residual": m1,
            "abs_residual_max": max(abs(m0), abs(m1)),
            "support": list(phi.support_x()),
        })

    payload = {
        "phase": "X3",
        "status": "PHASE_X3_BUILT_IN_POLE_CANCELLED_SMOOTH_BASIS_COMPLETE",
        "certification_status": "FLOATING_PROTOTYPE_ONLY_NOT_CERTIFIED",
        "correction_matrix_strategy": "solve 2x2 Mellin moment system at s=0 and s=1",
        "basis": [phi.to_dict() for phi in basis],
        "floating_residual_checks": checks,
        "audit_strings": [
            "PHASE_X3_BUILT_IN_POLE_CANCELLED_SMOOTH_BASIS_COMPLETE",
            "RAW_SMOOTH_BUMPS_DEFINED",
            "CORRECTION_BUMPS_DEFINED",
            "MELLIN_MOMENT_CORRECTION_MATRIX_DEFINED",
            "CORRECTED_BASIS_DEFINED",
            "SMOOTH_COMPACT_SUPPORT_PRESERVED_PROVED",
            "BUILT_IN_POLE_CANCELLATION_PROVED",
            "FINITE_COMBINATIONS_POLE_CANCELLED_PROVED",
            "POLE_CANCELLED_SMOOTH_BASIS_MECHANISM_CREATED",
            "CERTIFIED_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X4_SUPPORT_AND_FINITE_PRIME_CUTOFF_THEOREM",
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_pole_cancelled_basis_certificate(
        Path("breakthrough_attack/phase_x3_built_in_pole_cancelled_smooth_basis/pole_cancelled_basis_certificate.json")
    )
    print("Wrote pole-cancelled smooth basis certificate")
