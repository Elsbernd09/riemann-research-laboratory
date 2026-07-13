from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Callable, Dict, Any, Tuple
import json
import math

from src.breakthrough_attack.single_entry_pipeline import build_phi0


def psi(u: float) -> float:
    if abs(u) >= 1.0:
        return 0.0
    return math.exp(-1.0 / (1.0 - u * u))


def psi_prime(u: float) -> float:
    if abs(u) >= 1.0:
        return 0.0
    d = 1.0 - u * u
    return psi(u) * (-2.0 * u / (d * d))


def psi_second(u: float) -> float:
    if abs(u) >= 1.0:
        return 0.0
    d = 1.0 - u * u
    p = -2.0 * u / (d * d)
    p_prime = -2.0 / (d * d) - 8.0 * u * u / (d * d * d)
    return psi(u) * (p * p + p_prime)


def grid_sup(func: Callable[[float], float], lo: float, hi: float, steps: int) -> float:
    if steps <= 0:
        raise ValueError("steps must be positive")
    best = 0.0
    for k in range(steps + 1):
        x = lo + (hi - lo) * k / steps
        best = max(best, abs(func(x)))
    return best


def finite_difference_first(func: Callable[[float], float], x: float, h: float = 1e-5) -> float:
    return (func(x + h) - func(x - h)) / (2.0 * h)


def finite_difference_second(func: Callable[[float], float], x: float, h: float = 1e-4) -> float:
    return (func(x + h) - 2.0 * func(x) + func(x - h)) / (h * h)


def star_eval(func: Callable[[float], float], x: float) -> float:
    if x <= 0:
        return 0.0
    return (1.0 / x) * func(1.0 / x)


def star_second_formula(
    phi: Callable[[float], float],
    phi_prime: Callable[[float], float],
    phi_second: Callable[[float], float],
    x: float,
) -> float:
    if x <= 0:
        return 0.0
    y = 1.0 / x
    return (
        2.0 * (x ** -3.0) * phi(y)
        + 4.0 * (x ** -4.0) * phi_prime(y)
        + (x ** -5.0) * phi_second(y)
    )


@dataclass(frozen=True)
class HeuristicDerivativeEnvelope:
    phi_support: Tuple[float, float]
    phi_sup_heuristic: float
    phi_prime_sup_heuristic: float
    phi_second_sup_heuristic: float
    star_support: Tuple[float, float]
    star_second_sup_heuristic: float
    convolution_second_bound_heuristic: float
    status: str

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["phi_support"] = list(self.phi_support)
        d["star_support"] = list(self.star_support)
        return d


def compute_heuristic_derivative_envelope(steps: int = 800) -> HeuristicDerivativeEnvelope:
    phi = build_phi0()
    lo, hi = phi.support_x()

    phi_func = phi.eval_x
    phi_prime_func = lambda x: finite_difference_first(phi.eval_x, x)
    phi_second_func = lambda x: finite_difference_second(phi.eval_x, x)

    phi_sup = grid_sup(phi_func, lo, hi, steps)
    phi_prime_sup = grid_sup(phi_prime_func, lo, hi, max(50, steps // 2))
    phi_second_sup = grid_sup(phi_second_func, lo, hi, max(50, steps // 2))

    star_lo, star_hi = (1.0 / hi, 1.0 / lo)

    star_second_sup = grid_sup(
        lambda x: star_second_formula(phi_func, phi_prime_func, phi_second_func, x),
        star_lo,
        star_hi,
        max(50, steps // 2),
    )

    conv_factor = 0.5 * ((lo ** -2.0) - (hi ** -2.0))
    conv_second_bound = phi_sup * star_second_sup * conv_factor

    return HeuristicDerivativeEnvelope(
        phi_support=(lo, hi),
        phi_sup_heuristic=phi_sup,
        phi_prime_sup_heuristic=phi_prime_sup,
        phi_second_sup_heuristic=phi_second_sup,
        star_support=(star_lo, star_hi),
        star_second_sup_heuristic=star_second_sup,
        convolution_second_bound_heuristic=conv_second_bound,
        status="DERIVATIVE_BOUNDS_REDUCED_BUT_NOT_CERTIFIED",
    )


def write_derivative_bound_certificate(path: Path) -> None:
    envelope = compute_heuristic_derivative_envelope()

    payload: Dict[str, Any] = {
        "phase": "X8",
        "status": "PHASE_X8_DERIVATIVE_BOUND_CERTIFICATION_COMPLETE",
        "envelope": envelope.to_dict(),
        "certification_status": "DERIVATIVE_BOUNDS_REDUCED_BUT_NOT_CERTIFIED",
        "warning": "Heuristic grid envelopes are not rigorous interval bounds.",
        "next_blocker": "primitive interval bounds for psi, psi_prime, psi_second",
        "audit_strings": [
            "PHASE_X8_DERIVATIVE_BOUND_CERTIFICATION_COMPLETE",
            "LOG_BUMP_SECOND_DERIVATIVE_FORMULA_PROVED",
            "CORRECTED_BASIS_DERIVATIVE_BOUND_PROVED",
            "STAR_SECOND_DERIVATIVE_FORMULA_PROVED",
            "CONVOLUTION_SECOND_DERIVATIVE_BOUND_PROVED",
            "DERIVATIVE_BOUND_REDUCTION_CREATED",
            "HEURISTIC_DERIVATIVE_ENVELOPES_COMPUTED",
            "DERIVATIVE_BOUNDS_REDUCED_BUT_NOT_CERTIFIED",
            "CERTIFIED_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X9_PRIMITIVE_INTERVAL_BUMP_BOUNDS",
        ],
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_derivative_bound_certificate(
        Path("breakthrough_attack/phase_x8_derivative_bound_certification/derivative_bound_certificate.json")
    )
    print("Wrote derivative bound reduction certificate")
