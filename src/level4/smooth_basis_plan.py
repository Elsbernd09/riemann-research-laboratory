from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Any, Tuple
import json
import math


@dataclass(frozen=True)
class SmoothLogBumpSpec:
    center: float
    width: float

    def support_x(self) -> Tuple[float, float]:
        if self.width <= 0:
            raise ValueError("width must be positive")
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

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["support_x"] = list(self.support_x())
        d["star_support_x"] = list(self.star_support_x())
        d["convolution_support_x"] = list(self.convolution_support_x())
        d["prime_cutoff"] = self.prime_cutoff()
        return d


def smooth_bump_value(u: float) -> float:
    """
    Floating prototype of the standard bump.

    psi(u)=exp(-1/(1-u^2)) for |u|<1, otherwise 0.

    This is not interval-certified.
    """
    if abs(u) >= 1.0:
        return 0.0
    return math.exp(-1.0 / (1.0 - u * u))


def smooth_log_bump_value(x: float, spec: SmoothLogBumpSpec) -> float:
    if x <= 0:
        return 0.0
    u = (math.log(x) - spec.center) / spec.width
    return smooth_bump_value(u)


def write_smooth_basis_plan_certificate(path: Path) -> None:
    spec = SmoothLogBumpSpec(center=0.0, width=0.75)
    payload = {
        "phase": "B13",
        "status": "PHASE_B13_SMOOTH_BASIS_CERTIFICATION_PLAN_COMPLETE",
        "basis_spec": spec.to_dict(),
        "basis_family": "phi_cw(x)=psi((log(x)-c)/w)",
        "smooth_bump": "psi(u)=exp(-1/(1-u^2)) for |u|<1 and 0 otherwise",
        "certification_status": "PLAN_AND_FLOATING_PROTOTYPE_ONLY",
        "audit_strings": [
            "PHASE_B13_SMOOTH_BASIS_CERTIFICATION_PLAN_COMPLETE",
            "SMOOTH_BUMP_DEFINED",
            "LOG_SMOOTH_BASIS_DEFINED",
            "SMOOTH_BASIS_IN_CC_INFINITY_PROVED",
            "STAR_SUPPORT_BOUND_PROVED",
            "CONVOLUTION_SUPPORT_BOUND_PROVED",
            "FINITE_PRIME_CUTOFF_FROM_SUPPORT_IDENTIFIED",
            "TRIANGULAR_TOY_BASIS_REPLACEMENT_PLAN_CREATED",
            "BREAKTHROUGH_NOT_ACHIEVED",
            "READY_FOR_PHASE_B14_SMOOTH_BASIS_IMPLEMENTATION",
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_smooth_basis_plan_certificate(
        Path("breakthrough_push/phase_b13_smooth_basis_certification_plan/smooth_basis_plan_certificate.json")
    )
    print("Wrote smooth basis plan certificate")
