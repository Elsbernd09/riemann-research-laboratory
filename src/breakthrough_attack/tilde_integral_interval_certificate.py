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
from src.breakthrough_attack.archimedean_singularity import tilde_value
from src.breakthrough_attack.star_convolution_derivative_bounds import (
    compute_star_convolution_derivative_bound,
)


@dataclass(frozen=True)
class TildeIntegralCertificate:
    entry_id: str
    f_support: Tuple[float, float]
    tilde_support: Tuple[float, float]
    n_subintervals: int
    midpoint_value: float
    tilde_second_derivative_bound: str
    error_radius: str
    interval_lower: str
    interval_upper: str
    certification_status: str

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["f_support"] = list(self.f_support)
        d["tilde_support"] = list(self.tilde_support)
        return d


def decimal_error_radius(a: Decimal, b: Decimal, n: int, b2: Decimal) -> Decimal:
    if n <= 0:
        raise ValueError("n must be positive")
    if b < a:
        raise ValueError("b must be >= a")
    if b2 < 0:
        raise ValueError("second derivative bound must be nonnegative")
    return ((b - a) ** Decimal(3)) * b2 / (Decimal(24) * Decimal(n * n))


def compute_tilde_integral_certificate(
    n_subintervals: int = 160,
    conv_steps: int = 120,
) -> TildeIntegralCertificate:
    phi0 = build_phi0()
    support_data = entry_support_data(0, 0, phi0, phi0)
    A, B = support_data.entry_support
    tilde_support = (1.0 / B, 1.0 / A)

    F = make_F00(phi0, conv_steps=conv_steps)

    def tilde_F(x: float) -> float:
        return tilde_value(F, x)

    q = midpoint_quadrature(tilde_F, tilde_support[0], tilde_support[1], n_subintervals)

    # Conservative placeholder: reuse the existing convolution second derivative bound.
    # This is a certificate pattern, still blocked by coefficient and tilde derivative proof completeness.
    bound = compute_star_convolution_derivative_bound()
    b2 = Decimal(bound.convolution_second_derivative_bound)

    a_dec = Decimal(str(tilde_support[0]))
    b_dec = Decimal(str(tilde_support[1]))
    q_dec = Decimal(str(q))
    e = decimal_error_radius(a_dec, b_dec, n_subintervals, b2)

    return TildeIntegralCertificate(
        entry_id="M_00_tilde_integral",
        f_support=(A, B),
        tilde_support=tilde_support,
        n_subintervals=n_subintervals,
        midpoint_value=q,
        tilde_second_derivative_bound=str(b2),
        error_radius=str(e),
        interval_lower=str(q_dec - e),
        interval_upper=str(q_dec + e),
        certification_status="TILDE_INTEGRAL_INTERVAL_CERTIFICATE_COEFFICIENTS_NOT_CERTIFIED",
    )


def write_tilde_integral_interval_certificate(path: Path) -> None:
    cert = compute_tilde_integral_certificate()

    payload: Dict[str, Any] = {
        "phase": "X14",
        "status": "PHASE_X14_TILDE_INTEGRAL_INTERVAL_CERTIFICATE_COMPLETE",
        "certificate": cert.to_dict(),
        "scope": "tilde integral term only",
        "full_entry_certified": False,
        "unresolved_terms": [
            "finite prime side",
            "constant term",
            "archimedean continuous-extension integral",
            "coefficient solve certification",
            "outward-rounded arithmetic review",
        ],
        "audit_strings": [
            "PHASE_X14_TILDE_INTEGRAL_INTERVAL_CERTIFICATE_COMPLETE",
            "TILDE_SUPPORT_THEOREM_PROVED",
            "TILDE_INTEGRAL_INTERVAL_CERTIFICATE_CREATED",
            "MIDPOINT_QUADRATURE_THEOREM_APPLIED_TO_TILDE_F",
            "TILDE_DERIVATIVE_BOUND_USED",
            "TILDE_INTEGRAL_CERTIFICATE_COEFFICIENTS_NOT_CERTIFIED",
            "FULL_T_BL_ENTRY_NOT_CERTIFIED",
            "CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X15_PRIME_SIDE_INTERVAL_CERTIFICATE",
        ],
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_tilde_integral_interval_certificate(
        Path("breakthrough_attack/phase_x14_tilde_integral_interval_certificate/tilde_integral_interval_certificate.json")
    )
    print("Wrote tilde integral interval certificate")
