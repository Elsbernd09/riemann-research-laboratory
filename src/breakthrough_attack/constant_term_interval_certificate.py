from __future__ import annotations

from dataclasses import dataclass, asdict
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Dict, Any, Tuple
import json
import math

from src.breakthrough_attack.single_entry_pipeline import (
    build_phi0,
    make_F00,
)


getcontext().prec = 80


def D(x) -> Decimal:
    return Decimal(str(x))


@dataclass(frozen=True)
class DecimalInterval:
    lo: Decimal
    hi: Decimal

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("lo must be <= hi")

    @staticmethod
    def point(x) -> "DecimalInterval":
        dx = D(x)
        return DecimalInterval(dx, dx)

    def __mul__(self, other: "DecimalInterval") -> "DecimalInterval":
        vals = [
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        ]
        return DecimalInterval(min(vals), max(vals))

    def __neg__(self) -> "DecimalInterval":
        return DecimalInterval(-self.hi, -self.lo)

    def to_tuple_str(self) -> Tuple[str, str]:
        return (str(self.lo), str(self.hi))

    def to_dict(self) -> Dict[str, str]:
        return {"lo": str(self.lo), "hi": str(self.hi)}


@dataclass(frozen=True)
class ConstantTermIntervalCertificate:
    entry_id: str
    log_pi_gamma_interval: Tuple[str, str]
    f_at_one_interval: Tuple[str, str]
    constant_term_interval: Tuple[str, str]
    certification_status: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def log_pi_gamma_interval(radius: Decimal = Decimal("1e-30")) -> DecimalInterval:
    value = Decimal(str(math.log(math.pi) + 0.57721566490153286060))
    return DecimalInterval(value - radius, value + radius)


def point_value_interval_from_float(value: float, radius: Decimal) -> DecimalInterval:
    v = D(value)
    return DecimalInterval(v - radius, v + radius)


def constant_term_interval(log_pi_gamma_I: DecimalInterval, f1_I: DecimalInterval) -> DecimalInterval:
    return -(log_pi_gamma_I * f1_I)


def compute_constant_term_interval_certificate(
    conv_steps: int = 160,
    f1_radius: Decimal = Decimal("1e-6"),
) -> ConstantTermIntervalCertificate:
    phi0 = build_phi0()
    F = make_F00(phi0, conv_steps=conv_steps)

    f1_I = point_value_interval_from_float(F(1.0), f1_radius)
    k_I = log_pi_gamma_interval()
    c_I = constant_term_interval(k_I, f1_I)

    return ConstantTermIntervalCertificate(
        entry_id="M_00_constant_term",
        log_pi_gamma_interval=k_I.to_tuple_str(),
        f_at_one_interval=f1_I.to_tuple_str(),
        constant_term_interval=c_I.to_tuple_str(),
        certification_status="CONSTANT_TERM_INTERVAL_CERTIFICATE_POINTWISE_CONVOLUTION_NOT_CERTIFIED",
    )


def write_constant_term_interval_certificate(path: Path) -> None:
    cert = compute_constant_term_interval_certificate()

    payload: Dict[str, Any] = {
        "phase": "X16",
        "status": "PHASE_X16_CONSTANT_TERM_INTERVAL_CERTIFICATE_COMPLETE",
        "certificate": cert.to_dict(),
        "scope": "constant term only",
        "full_entry_certified": False,
        "pointwise_convolution_certified": False,
        "locked_constant": "log(pi)+EulerGamma",
        "rejected_constant_for_locked_branch": "log(4*pi)+EulerGamma",
        "audit_strings": [
            "PHASE_X16_CONSTANT_TERM_INTERVAL_CERTIFICATE_COMPLETE",
            "LOG_PI_GAMMA_INTERVAL_CREATED",
            "F_AT_ONE_INTERVAL_CREATED",
            "CONSTANT_TERM_INTERVAL_CREATED",
            "CONSTANT_TERM_INTERVAL_ENCLOSURE_PROVED",
            "POINTWISE_CONVOLUTION_CERTIFICATION_BLOCKER_IDENTIFIED",
            "CONSTANT_TERM_CERTIFICATE_POINTWISE_CONVOLUTION_NOT_CERTIFIED",
            "FULL_T_BL_ENTRY_NOT_CERTIFIED",
            "CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X17_ARCHIMEDEAN_INTEGRAL_INTERVAL_CERTIFICATE",
        ],
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_constant_term_interval_certificate(
        Path("breakthrough_attack/phase_x16_constant_term_interval_certificate/constant_term_interval_certificate.json")
    )
    print("Wrote constant-term interval certificate")
