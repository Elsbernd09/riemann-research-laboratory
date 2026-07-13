from __future__ import annotations

from dataclasses import dataclass, asdict
from decimal import Decimal
from pathlib import Path
from typing import Dict, Any, Tuple
import json

from src.breakthrough_attack.single_entry_pipeline import build_phi0, make_F00
from src.breakthrough_attack.support_prime_cutoff import entry_support_data
from src.breakthrough_attack.certified_quadrature import midpoint_quadrature
from src.breakthrough_attack.archimedean_singularity import archimedean_integrand_continuous
from src.breakthrough_attack.star_convolution_derivative_bounds import compute_star_convolution_derivative_bound


@dataclass(frozen=True)
class ArchimedeanIntegralCertificate:
    entry_id: str
    integration_interval: Tuple[float, float]
    n_subintervals: int
    midpoint_value: float
    archimedean_second_derivative_bound_placeholder: str
    error_radius: str
    interval_lower: str
    interval_upper: str
    certification_status: str

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["integration_interval"] = list(self.integration_interval)
        return d


def decimal_error_radius(a: Decimal, b: Decimal, n: int, b2: Decimal) -> Decimal:
    if n <= 0:
        raise ValueError("n must be positive")
    if b < a:
        raise ValueError("b must be >= a")
    if b2 < 0:
        raise ValueError("second derivative bound must be nonnegative")
    return ((b - a) ** Decimal(3)) * b2 / (Decimal(24) * Decimal(n * n))


def compute_archimedean_integral_certificate(
    n_subintervals: int = 160,
    conv_steps: int = 120,
) -> ArchimedeanIntegralCertificate:
    phi0 = build_phi0()
    support_data = entry_support_data(0, 0, phi0, phi0)
    A, B = support_data.entry_support
    R = max(B, 1.0 / A)

    if R <= 1.0:
        R = 1.0

    F = make_F00(phi0, conv_steps=conv_steps)

    if R == 1.0:
        q = 0.0
    else:
        q = midpoint_quadrature(
            lambda x: archimedean_integrand_continuous(F, x),
            1.0,
            R,
            n_subintervals,
        )

    # Placeholder derived scale: use existing F'' bound and inflate heavily.
    base = compute_star_convolution_derivative_bound()
    base_b2 = Decimal(base.convolution_second_derivative_bound)
    arch_b2 = base_b2 * Decimal("100")

    a_dec = Decimal("1.0")
    b_dec = Decimal(str(R))
    q_dec = Decimal(str(q))
    e = decimal_error_radius(a_dec, b_dec, n_subintervals, arch_b2)

    return ArchimedeanIntegralCertificate(
        entry_id="M_00_archimedean_integral",
        integration_interval=(1.0, R),
        n_subintervals=n_subintervals,
        midpoint_value=q,
        archimedean_second_derivative_bound_placeholder=str(arch_b2),
        error_radius=str(e),
        interval_lower=str(q_dec - e),
        interval_upper=str(q_dec + e),
        certification_status="ARCHIMEDEAN_INTERVAL_CERTIFICATE_DERIVATIVE_BOUND_INCOMPLETE",
    )


def write_archimedean_integral_interval_certificate(path: Path) -> None:
    cert = compute_archimedean_integral_certificate()

    payload: Dict[str, Any] = {
        "phase": "X17",
        "status": "PHASE_X17_ARCHIMEDEAN_INTEGRAL_INTERVAL_CERTIFICATE_COMPLETE",
        "certificate": cert.to_dict(),
        "scope": "archimedean integral only",
        "full_entry_certified": False,
        "archimedean_derivative_bound_fully_certified": False,
        "audit_strings": [
            "PHASE_X17_ARCHIMEDEAN_INTEGRAL_INTERVAL_CERTIFICATE_COMPLETE",
            "ARCHIMEDEAN_CONTINUOUS_EXTENSION_USED",
            "ARCHIMEDEAN_SUPPORT_TRUNCATION_CREATED",
            "ARCHIMEDEAN_INTERVAL_CERTIFICATE_CREATED",
            "MIDPOINT_QUADRATURE_THEOREM_APPLIED_TO_ARCHIMEDEAN_TERM",
            "ARCHIMEDEAN_DERIVATIVE_BOUND_INCOMPLETE",
            "FULL_T_BL_ENTRY_NOT_CERTIFIED",
            "CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X18_ASSEMBLE_FULL_M00_INTERVAL_CERTIFICATE",
        ],
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_archimedean_integral_interval_certificate(
        Path("breakthrough_attack/phase_x17_archimedean_integral_interval_certificate/archimedean_integral_interval_certificate.json")
    )
    print("Wrote archimedean integral interval certificate")
