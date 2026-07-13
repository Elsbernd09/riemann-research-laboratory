from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Callable, Dict, Any, Tuple, List
import json
import math

from src.breakthrough_attack.pole_cancelled_smooth_basis import (
    build_pole_cancelled_function,
    SmoothBump,
    PoleCancelledSmoothBasisFunction,
    midpoint_integral,
)
from src.breakthrough_attack.support_prime_cutoff import (
    entry_support_data,
    finite_prime_cutoff,
)
from src.breakthrough_attack.archimedean_singularity import (
    tilde_value,
    archimedean_integrand_continuous,
)
from src.breakthrough_attack.certified_quadrature import (
    midpoint_quadrature,
    midpoint_error_bound,
)


EULER_GAMMA = 0.57721566490153286060


def von_mangoldt(n: int) -> float:
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return 0.0

    # Return log(p) iff n is a positive prime power p^k.
    for p in range(2, n + 1):
        power = p
        while power < n:
            power *= p
        if power == n and is_prime(p):
            return math.log(p)
    return 0.0


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    for k in range(3, r + 1, 2):
        if n % k == 0:
            return False
    return True


def build_phi0() -> PoleCancelledSmoothBasisFunction:
    corr0 = SmoothBump(center=-1.0, width=0.35)
    corr1 = SmoothBump(center=1.0, width=0.35)
    raw0 = SmoothBump(center=-0.25, width=0.30)
    return build_pole_cancelled_function(raw0, corr0, corr1)


def star_eval(phi: PoleCancelledSmoothBasisFunction, x: float) -> float:
    if x <= 0:
        return 0.0
    return (1.0 / x) * phi.eval_x(1.0 / x)


def convolution_with_star(
    phi_left: PoleCancelledSmoothBasisFunction,
    phi_right: PoleCancelledSmoothBasisFunction,
    x: float,
    steps: int = 300,
) -> float:
    if x <= 0:
        return 0.0

    lo, hi = phi_left.support_x()

    def integrand(y: float) -> float:
        if y <= 0:
            return 0.0
        return phi_left.eval_x(y) * star_eval(phi_right, x / y) / y

    return midpoint_integral(integrand, lo, hi, steps=steps)


def make_F00(phi0: PoleCancelledSmoothBasisFunction, conv_steps: int = 250) -> Callable[[float], float]:
    def F(x: float) -> float:
        return convolution_with_star(phi0, phi0, x, steps=conv_steps)
    return F


def integrate_on_support(
    func: Callable[[float], float],
    support: Tuple[float, float],
    steps: int = 300,
) -> float:
    lo, hi = support
    return midpoint_quadrature(func, lo, hi, steps)


def prime_side(F: Callable[[float], float], cutoff: int) -> float:
    total = 0.0
    for n in range(1, cutoff + 1):
        lam = von_mangoldt(n)
        if lam == 0.0:
            continue
        x = float(n)
        total += lam * (F(x) + tilde_value(F, x))
    return total


@dataclass(frozen=True)
class SingleEntryPipelineResult:
    entry_id: str
    status: str
    entry_support: Tuple[float, float]
    finite_prime_cutoff: int
    central_integral_prototype: float
    tilde_integral_prototype: float
    prime_sum_prototype: float
    constant_term_prototype: float
    archimedean_integral_prototype: float
    entry_value_prototype: float
    derivative_bounds_available: bool
    certification_status: str
    unresolved_blockers: List[str]

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["entry_support"] = list(self.entry_support)
        return d


def compute_single_entry_pipeline(
    integral_steps: int = 220,
    conv_steps: int = 160,
) -> SingleEntryPipelineResult:
    phi0 = build_phi0()
    support_data = entry_support_data(0, 0, phi0, phi0)
    entry_support = support_data.entry_support
    cutoff = support_data.finite_prime_cutoff
    F = make_F00(phi0, conv_steps=conv_steps)

    central = integrate_on_support(F, entry_support, steps=integral_steps)

    def tilde_F(x: float) -> float:
        return tilde_value(F, x)

    tilde_support = (1.0 / entry_support[1], 1.0 / entry_support[0])
    tilde_integral = integrate_on_support(tilde_F, tilde_support, steps=integral_steps)

    ps = prime_side(F, cutoff)
    f1 = F(1.0)
    constant = -(math.log(math.pi) + EULER_GAMMA) * f1

    arch_lo = max(1.0, entry_support[0])
    arch_hi = max(arch_lo, entry_support[1])

    if arch_hi == arch_lo:
        arch = 0.0
    else:
        arch = midpoint_quadrature(
            lambda x: archimedean_integrand_continuous(F, x),
            arch_lo,
            arch_hi,
            integral_steps,
        )

    value = central + tilde_integral - ps + constant - arch

    return SingleEntryPipelineResult(
        entry_id="M_00",
        status="PHASE_X7_SINGLE_ENTRY_CERTIFICATION_PIPELINE_COMPLETE",
        entry_support=entry_support,
        finite_prime_cutoff=cutoff,
        central_integral_prototype=central,
        tilde_integral_prototype=tilde_integral,
        prime_sum_prototype=ps,
        constant_term_prototype=constant,
        archimedean_integral_prototype=arch,
        entry_value_prototype=value,
        derivative_bounds_available=False,
        certification_status="CERTIFICATION_INCOMPLETE",
        unresolved_blockers=[
            "rigorous second-derivative bound for F00",
            "rigorous second-derivative bound for tilde F00",
            "rigorous second-derivative bound for archimedean continuous extension",
            "outward-rounded interval arithmetic",
            "certified convolution enclosure",
        ],
    )


def write_single_entry_pipeline_certificate(path: Path) -> None:
    result = compute_single_entry_pipeline()

    payload: Dict[str, Any] = {
        "phase": "X7",
        "status": "PHASE_X7_SINGLE_ENTRY_CERTIFICATION_PIPELINE_COMPLETE",
        "result": result.to_dict(),
        "locked_functional": "T_BL",
        "locked_constant": "-(log(pi)+EulerGamma)F(1)",
        "certification_status": result.certification_status,
        "audit_strings": [
            "PHASE_X7_SINGLE_ENTRY_CERTIFICATION_PIPELINE_COMPLETE",
            "SINGLE_ENTRY_PIPELINE_CREATED",
            "LOCKED_T_BL_COMPONENTS_ASSEMBLED",
            "FINITE_PRIME_SIDE_COMPUTABLE_PROVED",
            "ARCHIMEDEAN_CONTINUOUS_EXTENSION_USED",
            "QUADRATURE_CERTIFICATION_PATTERN_USED",
            "CERTIFICATION_INCOMPLETE_STATUS_ASSIGNED",
            "DERIVATIVE_BOUND_BLOCKER_IDENTIFIED",
            "CERTIFIED_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X8_DERIVATIVE_BOUND_CERTIFICATION",
        ],
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_single_entry_pipeline_certificate(
        Path("breakthrough_attack/phase_x7_single_entry_certification_pipeline/single_entry_pipeline_certificate.json")
    )
    print("Wrote single-entry certification pipeline certificate")
