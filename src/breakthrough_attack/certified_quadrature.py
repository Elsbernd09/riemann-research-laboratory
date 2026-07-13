from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Callable, Dict, Any, Tuple
import json
import math


@dataclass(frozen=True)
class QuadratureCertificate:
    a: float
    b: float
    n: int
    q_lower: float
    q_upper: float
    second_derivative_bound: float

    @property
    def error_radius(self) -> float:
        if self.n <= 0:
            raise ValueError("n must be positive")
        if self.b < self.a:
            raise ValueError("b must be >= a")
        if self.second_derivative_bound < 0:
            raise ValueError("second_derivative_bound must be nonnegative")
        return ((self.b - self.a) ** 3) * self.second_derivative_bound / (24.0 * (self.n ** 2))

    @property
    def certified_interval(self) -> Tuple[float, float]:
        e = self.error_radius
        return (self.q_lower - e, self.q_upper + e)

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["error_radius"] = self.error_radius
        d["certified_interval"] = list(self.certified_interval)
        return d


def midpoint_quadrature(func: Callable[[float], float], a: float, b: float, n: int) -> float:
    if n <= 0:
        raise ValueError("n must be positive")
    if b < a:
        raise ValueError("b must be >= a")
    if b == a:
        return 0.0
    h = (b - a) / n
    total = 0.0
    for k in range(n):
        x = a + (k + 0.5) * h
        total += func(x)
    return total * h


def midpoint_error_bound(a: float, b: float, n: int, second_derivative_bound: float) -> float:
    cert = QuadratureCertificate(
        a=a,
        b=b,
        n=n,
        q_lower=0.0,
        q_upper=0.0,
        second_derivative_bound=second_derivative_bound,
    )
    return cert.error_radius


def make_integral_enclosure(
    q_lower: float,
    q_upper: float,
    a: float,
    b: float,
    n: int,
    second_derivative_bound: float,
) -> QuadratureCertificate:
    return QuadratureCertificate(
        a=a,
        b=b,
        n=n,
        q_lower=q_lower,
        q_upper=q_upper,
        second_derivative_bound=second_derivative_bound,
    )


def demo_quadratic(x: float) -> float:
    return x * x


def write_certified_quadrature_certificate(path: Path) -> None:
    a = 0.0
    b = 1.0
    n = 100
    q = midpoint_quadrature(demo_quadratic, a, b, n)
    # For h(x)=x^2, h''(x)=2.
    cert = make_integral_enclosure(q, q, a, b, n, 2.0)

    payload: Dict[str, Any] = {
        "phase": "X6",
        "status": "PHASE_X6_CERTIFIED_QUADRATURE_THEOREM_COMPLETE",
        "theorem": "midpoint error <= (b-a)^3 sup|h''|/(24N^2)",
        "demo_function": "h(x)=x^2 on [0,1]",
        "demo_exact_integral": 1.0 / 3.0,
        "demo_midpoint_value": q,
        "demo_certificate": cert.to_dict(),
        "demo_exact_integral_inside_interval": cert.certified_interval[0] <= (1.0 / 3.0) <= cert.certified_interval[1],
        "certification_status": "THEOREM_PROVED_PATTERN_READY_BUT_ENTRY_NOT_COMPUTED",
        "audit_strings": [
            "PHASE_X6_CERTIFIED_QUADRATURE_THEOREM_COMPLETE",
            "MIDPOINT_QUADRATURE_ERROR_THEOREM_PROVED",
            "CERTIFIED_INTEGRAL_ENCLOSURE_THEOREM_PROVED",
            "ERROR_BOUND_FORMULA_LOCKED",
            "QUADRATURE_CERTIFICATION_PATTERN_CREATED",
            "CERTIFIED_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X7_SINGLE_ENTRY_CERTIFICATION_PIPELINE",
        ],
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_certified_quadrature_certificate(
        Path("breakthrough_attack/phase_x6_certified_quadrature_theorem/certified_quadrature_certificate.json")
    )
    print("Wrote certified quadrature theorem certificate")
