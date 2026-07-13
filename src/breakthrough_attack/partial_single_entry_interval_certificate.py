from __future__ import annotations

from dataclasses import dataclass, asdict
from decimal import Decimal
from pathlib import Path
from typing import Dict, Any, Tuple
import json

from src.breakthrough_attack.single_entry_pipeline import (
    build_phi0,
    make_F00,
)
from src.breakthrough_attack.support_prime_cutoff import entry_support_data
from src.breakthrough_attack.certified_quadrature import midpoint_quadrature
from src.breakthrough_attack.star_convolution_derivative_bounds import (
    compute_star_convolution_derivative_bound,
)


@dataclass(frozen=True)
class PartialCentralIntegralCertificate:
    entry_id: str
    support: Tuple[float, float]
    n_subintervals: int
    midpoint_value: float
    f_second_derivative_bound: str
    error_radius: str
    interval_lower: str
    interval_upper: str
    certification_status: str

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["support"] = list(self.support)
        return d


def decimal_error_radius(a: Decimal, b: Decimal, n: int, b2: Decimal) -> Decimal:
    if n <= 0:
        raise ValueError("n must be positive")
    if b < a:
        raise ValueError("b must be >= a")
    if b2 < 0:
        raise ValueError("second derivative bound must be nonnegative")
    return ((b - a) ** Decimal(3)) * b2 / (Decimal(24) * Decimal(n * n))


def compute_partial_central_integral_certificate(
    n_subintervals: int = 160,
    conv_steps: int = 120,
) -> PartialCentralIntegralCertificate:
    phi0 = build_phi0()
    support_data = entry_support_data(0, 0, phi0, phi0)
    a_float, b_float = support_data.entry_support

    F = make_F00(phi0, conv_steps=conv_steps)
    q = midpoint_quadrature(F, a_float, b_float, n_subintervals)

    bound = compute_star_convolution_derivative_bound()
    b2 = Decimal(bound.convolution_second_derivative_bound)

    a_dec = Decimal(str(a_float))
    b_dec = Decimal(str(b_float))
    q_dec = Decimal(str(q))
    e = decimal_error_radius(a_dec, b_dec, n_subintervals, b2)

    lo = q_dec - e
    hi = q_dec + e

    return PartialCentralIntegralCertificate(
        entry_id="M_00_central_integral",
        support=(a_float, b_float),
        n_subintervals=n_subintervals,
        midpoint_value=q,
        f_second_derivative_bound=str(b2),
        error_radius=str(e),
        interval_lower=str(lo),
        interval_upper=str(hi),
        certification_status="PARTIAL_SINGLE_ENTRY_INTERVAL_CERTIFICATE",
    )


def write_partial_single_entry_interval_certificate(path: Path) -> None:
    cert = compute_partial_central_integral_certificate()

    payload: Dict[str, Any] = {
        "phase": "X13",
        "status": "PHASE_X13_PARTIAL_SINGLE_ENTRY_INTERVAL_CERTIFICATE_COMPLETE",
        "certificate": cert.to_dict(),
        "scope": "central integral term only",
        "full_entry_certified": False,
        "unresolved_terms": [
            "tilde integral",
            "finite prime side",
            "constant term",
            "archimedean continuous-extension integral",
            "coefficient solve certification",
            "outward-rounded arithmetic review",
        ],
        "audit_strings": [
            "PHASE_X13_PARTIAL_SINGLE_ENTRY_INTERVAL_CERTIFICATE_COMPLETE",
            "CENTRAL_INTEGRAL_INTERVAL_CERTIFICATE_CREATED",
            "MIDPOINT_QUADRATURE_THEOREM_APPLIED_TO_F",
            "F_SECOND_DERIVATIVE_BOUND_USED",
            "PARTIAL_SINGLE_ENTRY_INTERVAL_CERTIFICATE_CREATED",
            "FULL_T_BL_ENTRY_NOT_CERTIFIED",
            "CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X14_TILDE_INTEGRAL_INTERVAL_CERTIFICATE",
        ],
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_partial_single_entry_interval_certificate(
        Path("breakthrough_attack/phase_x13_partial_single_entry_interval_certificate/partial_single_entry_interval_certificate.json")
    )
    print("Wrote partial single-entry interval certificate")
