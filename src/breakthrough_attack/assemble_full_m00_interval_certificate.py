from __future__ import annotations

from dataclasses import dataclass, asdict
from decimal import Decimal
from pathlib import Path
from typing import Dict, Any, Tuple, List
import json

from src.breakthrough_attack.partial_single_entry_interval_certificate import (
    compute_partial_central_integral_certificate,
)
from src.breakthrough_attack.tilde_integral_interval_certificate import (
    compute_tilde_integral_certificate,
)
from src.breakthrough_attack.prime_side_interval_certificate import (
    compute_prime_side_interval_certificate,
)
from src.breakthrough_attack.constant_term_interval_certificate import (
    compute_constant_term_interval_certificate,
)
from src.breakthrough_attack.archimedean_integral_interval_certificate import (
    compute_archimedean_integral_certificate,
)


@dataclass(frozen=True)
class DecimalInterval:
    lo: Decimal
    hi: Decimal

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("lo must be <= hi")

    @staticmethod
    def from_tuple_str(pair: Tuple[str, str]) -> "DecimalInterval":
        return DecimalInterval(Decimal(pair[0]), Decimal(pair[1]))

    def __add__(self, other: "DecimalInterval") -> "DecimalInterval":
        return DecimalInterval(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self) -> "DecimalInterval":
        return DecimalInterval(-self.hi, -self.lo)

    def __sub__(self, other: "DecimalInterval") -> "DecimalInterval":
        return self + (-other)

    def to_tuple_str(self) -> Tuple[str, str]:
        return (str(self.lo), str(self.hi))

    def to_dict(self) -> Dict[str, str]:
        return {"lo": str(self.lo), "hi": str(self.hi)}


@dataclass(frozen=True)
class FullM00IntervalCertificate:
    entry_id: str
    central_integral_interval: Tuple[str, str]
    tilde_integral_interval: Tuple[str, str]
    prime_side_interval: Tuple[str, str]
    constant_term_interval: Tuple[str, str]
    archimedean_integral_interval: Tuple[str, str]
    assembled_m00_interval: Tuple[str, str]
    sign_structure: str
    unresolved_gates: List[str]
    certification_status: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def assemble_m00_interval(
    central: DecimalInterval,
    tilde: DecimalInterval,
    prime: DecimalInterval,
    constant: DecimalInterval,
    archimedean: DecimalInterval,
) -> DecimalInterval:
    return central + tilde - prime + constant - archimedean


def compute_full_m00_interval_certificate() -> FullM00IntervalCertificate:
    central_cert = compute_partial_central_integral_certificate(n_subintervals=120, conv_steps=100)
    tilde_cert = compute_tilde_integral_certificate(n_subintervals=120, conv_steps=100)
    prime_cert = compute_prime_side_interval_certificate(conv_steps=100, point_radius=Decimal("1e-6"))
    constant_cert = compute_constant_term_interval_certificate(conv_steps=100, f1_radius=Decimal("1e-6"))
    arch_cert = compute_archimedean_integral_certificate(n_subintervals=120, conv_steps=100)

    central = DecimalInterval(Decimal(central_cert.interval_lower), Decimal(central_cert.interval_upper))
    tilde = DecimalInterval(Decimal(tilde_cert.interval_lower), Decimal(tilde_cert.interval_upper))
    prime = DecimalInterval.from_tuple_str(prime_cert.prime_side_interval)
    constant = DecimalInterval.from_tuple_str(constant_cert.constant_term_interval)
    arch = DecimalInterval(Decimal(arch_cert.interval_lower), Decimal(arch_cert.interval_upper))

    assembled = assemble_m00_interval(central, tilde, prime, constant, arch)

    unresolved = [
        "prime-side pointwise convolution certificates",
        "constant-term pointwise convolution certificate for F(1)",
        "archimedean continuous-extension derivative bound",
        "coefficient-solve certification",
        "outward-rounded arithmetic review",
    ]

    return FullM00IntervalCertificate(
        entry_id="M_00_full_Bombieri_Lagarias_entry",
        central_integral_interval=central.to_tuple_str(),
        tilde_integral_interval=tilde.to_tuple_str(),
        prime_side_interval=prime.to_tuple_str(),
        constant_term_interval=constant.to_tuple_str(),
        archimedean_integral_interval=arch.to_tuple_str(),
        assembled_m00_interval=assembled.to_tuple_str(),
        sign_structure="central + tilde - prime + constant - archimedean",
        unresolved_gates=unresolved,
        certification_status="FULL_M00_INTERVAL_CERTIFICATE_ASSEMBLED_BUT_NOT_FULLY_CERTIFIED",
    )


def write_full_m00_interval_certificate(path: Path) -> None:
    cert = compute_full_m00_interval_certificate()

    payload: Dict[str, Any] = {
        "phase": "X18",
        "status": "PHASE_X18_ASSEMBLE_FULL_M00_INTERVAL_CERTIFICATE_COMPLETE",
        "certificate": cert.to_dict(),
        "full_entry_certified": False,
        "certified_arithmetic_entry": False,
        "audit_strings": [
            "PHASE_X18_ASSEMBLE_FULL_M00_INTERVAL_CERTIFICATE_COMPLETE",
            "CENTRAL_TERM_IMPORTED",
            "TILDE_TERM_IMPORTED",
            "PRIME_SIDE_TERM_IMPORTED",
            "CONSTANT_TERM_IMPORTED",
            "ARCHIMEDEAN_TERM_IMPORTED",
            "FULL_M00_INTERVAL_ASSEMBLED",
            "FULL_M00_INTERVAL_CERTIFICATE_ASSEMBLED_BUT_NOT_FULLY_CERTIFIED",
            "CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X19_COEFFICIENT_SOLVE_CERTIFICATION",
        ],
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_full_m00_interval_certificate(
        Path("breakthrough_attack/phase_x18_assemble_full_m00_interval_certificate/full_m00_interval_certificate.json")
    )
    print("Wrote full M00 interval certificate candidate")
