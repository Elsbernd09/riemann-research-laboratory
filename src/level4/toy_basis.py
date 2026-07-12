from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, List
import json
import math


@dataclass(frozen=True)
class TriangularLogBump:
    """Toy compactly supported basis phi(x)=max(0,1-|log(x)-center|/width)."""

    center: float
    width: float

    def __post_init__(self) -> None:
        if self.width <= 0:
            raise ValueError("width must be positive")

    @property
    def support_log(self) -> tuple[float, float]:
        return (self.center - self.width, self.center + self.width)

    @property
    def support_x(self) -> tuple[float, float]:
        lo, hi = self.support_log
        return (math.exp(lo), math.exp(hi))

    def eval_log(self, u: float) -> float:
        z = abs(u - self.center) / self.width
        return max(0.0, 1.0 - z)

    def eval_x(self, x: float) -> float:
        if x <= 0:
            return 0.0
        return self.eval_log(math.log(x))

    def star_x(self, x: float) -> float:
        if x <= 0:
            return 0.0
        return (1.0 / x) * self.eval_x(1.0 / x)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "TriangularLogBump",
            "center": self.center,
            "width": self.width,
            "support_log": list(self.support_log),
            "support_x": list(self.support_x),
        }


def convolution_eval_x(phi_j: TriangularLogBump, phi_i: TriangularLogBump, x: float, steps: int = 2000) -> float:
    """
    Numerically approximate F_ij(x) = phi_j * phi_i^*(x).

    In log variables:
    F_ij(e^u) = integral phi_j(e^v) phi_i^*(e^(u-v)) dv.

    This is a prototype non-certified midpoint quadrature.
    """
    if x <= 0:
        return 0.0
    if steps <= 0:
        raise ValueError("steps must be positive")

    u = math.log(x)
    a, b = phi_j.support_log
    h = (b - a) / steps
    total = 0.0
    for k in range(steps):
        v = a + (k + 0.5) * h
        y = math.exp(v)
        z = math.exp(u - v)
        total += phi_j.eval_x(y) * phi_i.star_x(z)
    return total * h


def build_default_toy_basis() -> List[TriangularLogBump]:
    return [
        TriangularLogBump(center=-0.25, width=0.75),
        TriangularLogBump(center=0.25, width=0.75),
    ]


def write_toy_basis_certificate(output_path: Path) -> None:
    basis = build_default_toy_basis()
    sample_x = [math.exp(-1.0), 1.0, math.exp(1.0)]
    samples = []
    for i, phi_i in enumerate(basis):
        for j, phi_j in enumerate(basis):
            values = {str(x): convolution_eval_x(phi_j, phi_i, x, steps=400) for x in sample_x}
            samples.append({"i": i, "j": j, "F_ij_samples": values})

    payload = {
        "phase": "12X",
        "status": "TOY_BASIS_PROTOTYPE_COMPLETE",
        "important_boundary": "TOY_BASIS_ONLY_NOT_FINAL_C_C_INFINITY_BASIS",
        "basis": [b.to_dict() for b in basis],
        "sample_convolutions": samples,
        "audit_strings": [
            "TOY_BASIS_PROTOTYPE_COMPLETE",
            "TRIANGULAR_LOG_BUMP_DEFINED",
            "MULTIPLICATIVE_TOY_BASIS_DEFINED",
            "TOY_BASIS_COMPACT_SUPPORT_PROVED",
            "STAR_EVALUATOR_IMPLEMENTED",
            "CONVOLUTION_EVALUATOR_IMPLEMENTED",
            "TOY_BASIS_ONLY_NOT_FINAL_C_C_INFINITY_BASIS",
            "TRUE_CERTIFIED_ARITHMETIC_ENTRY_NOT_YET_COMPUTED",
            "LEVEL4_READY_FOR_TOY_ENTRY_PROTOTYPE",
        ],
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    out = Path("original_results/finite_bombieri_stability/level4_candidate/toy_basis_prototype/toy_basis_certificate.json")
    write_toy_basis_certificate(out)
    print(f"Wrote {out}")
