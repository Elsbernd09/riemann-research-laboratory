from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Any, Tuple
import json
import math


@dataclass(frozen=True)
class SmoothLogBump:
    center: float
    width: float

    def __post_init__(self) -> None:
        if self.width <= 0:
            raise ValueError("width must be positive")

    def support_x(self) -> Tuple[float, float]:
        return (math.exp(self.center - self.width), math.exp(self.center + self.width))

    def star_support_x(self) -> Tuple[float, float]:
        lo, hi = self.support_x()
        return (1.0 / hi, 1.0 / lo)

    def convolution_support_x(self) -> Tuple[float, float]:
        lo, hi = self.support_x()
        slo, shi = self.star_support_x()
        return (lo * slo, hi * shi)

    def prime_cutoff(self) -> int:
        _, hi = self.convolution_support_x()
        return int(math.floor(hi))

    def bump(self, u: float) -> float:
        if abs(u) >= 1.0:
            return 0.0
        return math.exp(-1.0 / (1.0 - u * u))

    def eval_x(self, x: float) -> float:
        if x <= 0:
            return 0.0
        u = (math.log(x) - self.center) / self.width
        return self.bump(u)

    def star_eval_x(self, x: float) -> float:
        if x <= 0:
            return 0.0
        return (1.0 / x) * self.eval_x(1.0 / x)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "center": self.center,
            "width": self.width,
            "support_x": list(self.support_x()),
            "star_support_x": list(self.star_support_x()),
            "convolution_support_x": list(self.convolution_support_x()),
            "prime_cutoff": self.prime_cutoff(),
            "basis_type": "smooth_log_bump_C_c_infinity",
        }


def midpoint_integral(func, lo: float, hi: float, steps: int) -> float:
    if hi <= lo:
        return 0.0
    h = (hi - lo) / steps
    total = 0.0
    for k in range(steps):
        x = lo + (k + 0.5) * h
        total += func(x)
    return total * h


def smooth_convolution_with_star(phi_left: SmoothLogBump, phi_right: SmoothLogBump, x: float, steps: int = 200) -> float:
    """
    Floating prototype:

    F(x)=int phi_left(y) phi_right^*(x/y) dy/y.

    Not interval certified.
    """
    if x <= 0:
        return 0.0

    lo, hi = phi_left.support_x()

    def integrand(y: float) -> float:
        if y <= 0:
            return 0.0
        return phi_left.eval_x(y) * phi_right.star_eval_x(x / y) / y

    return midpoint_integral(integrand, lo, hi, steps)


def write_smooth_basis_implementation_certificate(path: Path) -> None:
    phi = SmoothLogBump(center=0.0, width=0.75)
    support = phi.support_x()
    star_support = phi.star_support_x()
    conv_support = phi.convolution_support_x()

    sample_values = {
        "phi_at_1": phi.eval_x(1.0),
        "phi_star_at_1": phi.star_eval_x(1.0),
        "convolution_at_1": smooth_convolution_with_star(phi, phi, 1.0, steps=100),
    }

    payload = {
        "phase": "B14",
        "status": "PHASE_B14_SMOOTH_BASIS_IMPLEMENTATION_COMPLETE",
        "basis": phi.to_dict(),
        "support_checks": {
            "support_lo_less_hi": support[0] < support[1],
            "star_support_lo_less_hi": star_support[0] < star_support[1],
            "convolution_support_lo_less_hi": conv_support[0] < conv_support[1],
            "support_contains_1": support[0] <= 1.0 <= support[1],
            "convolution_support_contains_1": conv_support[0] <= 1.0 <= conv_support[1],
        },
        "sample_values": sample_values,
        "certification_status": "FLOATING_IMPLEMENTATION_ONLY",
        "audit_strings": [
            "PHASE_B14_SMOOTH_BASIS_IMPLEMENTATION_COMPLETE",
            "SMOOTH_LOG_BUMP_IMPLEMENTED",
            "SMOOTH_BASIS_SUPPORT_IMPLEMENTED",
            "STAR_SUPPORT_IMPLEMENTED",
            "CONVOLUTION_SUPPORT_IMPLEMENTED",
            "FINITE_PRIME_CUTOFF_IMPLEMENTED",
            "FLOATING_SMOOTH_CONVOLUTION_PROTOTYPE_IMPLEMENTED",
            "CERTIFIED_ENTRY_NOT_COMPUTED",
            "BREAKTHROUGH_NOT_ACHIEVED",
            "READY_FOR_PHASE_B15_FINAL_BREAKTHROUGH_VERDICT",
        ],
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_smooth_basis_implementation_certificate(
        Path("breakthrough_push/phase_b14_smooth_basis_implementation/smooth_basis_implementation_certificate.json")
    )
    print("Wrote smooth basis implementation certificate")
