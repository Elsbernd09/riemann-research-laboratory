from __future__ import annotations

from dataclasses import dataclass, asdict
from decimal import Decimal
from pathlib import Path
from typing import Dict, Any, List, Tuple
import json
import math

from src.breakthrough_attack.single_entry_pipeline import (
    build_phi0,
    make_F00,
    von_mangoldt,
)
from src.breakthrough_attack.support_prime_cutoff import entry_support_data


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

    def __add__(self, other: "DecimalInterval") -> "DecimalInterval":
        return DecimalInterval(self.lo + other.lo, self.hi + other.hi)

    def scale_nonnegative(self, scalar) -> "DecimalInterval":
        s = D(scalar)
        if s < 0:
            raise ValueError("scalar must be nonnegative")
        return DecimalInterval(s * self.lo, s * self.hi)

    def to_dict(self) -> Dict[str, str]:
        return {"lo": str(self.lo), "hi": str(self.hi)}


@dataclass(frozen=True)
class PrimeTermInterval:
    n: int
    von_mangoldt: str
    f_interval: Tuple[str, str]
    tilde_f_interval: Tuple[str, str]
    term_interval: Tuple[str, str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class PrimeSideIntervalCertificate:
    entry_id: str
    f_support: Tuple[float, float]
    finite_prime_cutoff: int
    terms: List[PrimeTermInterval]
    prime_side_interval: Tuple[str, str]
    certification_status: str

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["f_support"] = list(self.f_support)
        return d


def point_value_interval_from_float(value: float, radius: Decimal) -> DecimalInterval:
    v = D(value)
    return DecimalInterval(v - radius, v + radius)


def tilde_value_interval_from_f_at_inv_n(f_inv_n_interval: DecimalInterval, n: int) -> DecimalInterval:
    scale = Decimal(1) / Decimal(n)
    return f_inv_n_interval.scale_nonnegative(scale)


def compute_prime_side_interval_certificate(
    conv_steps: int = 140,
    point_radius: Decimal = Decimal("1e-6"),
) -> PrimeSideIntervalCertificate:
    phi0 = build_phi0()
    support_data = entry_support_data(0, 0, phi0, phi0)
    A, B = support_data.entry_support
    cutoff = support_data.finite_prime_cutoff

    F = make_F00(phi0, conv_steps=conv_steps)

    total = DecimalInterval.point(0)
    terms: List[PrimeTermInterval] = []

    for n in range(1, cutoff + 1):
        lam = von_mangoldt(n)
        if lam == 0.0:
            continue

        f_n_I = point_value_interval_from_float(F(float(n)), point_radius)
        f_inv_I = point_value_interval_from_float(F(1.0 / float(n)), point_radius)
        tilde_I = tilde_value_interval_from_f_at_inv_n(f_inv_I, n)

        term_I = (f_n_I + tilde_I).scale_nonnegative(lam)
        total = total + term_I

        terms.append(
            PrimeTermInterval(
                n=n,
                von_mangoldt=str(D(lam)),
                f_interval=(str(f_n_I.lo), str(f_n_I.hi)),
                tilde_f_interval=(str(tilde_I.lo), str(tilde_I.hi)),
                term_interval=(str(term_I.lo), str(term_I.hi)),
            )
        )

    return PrimeSideIntervalCertificate(
        entry_id="M_00_prime_side",
        f_support=(A, B),
        finite_prime_cutoff=cutoff,
        terms=terms,
        prime_side_interval=(str(total.lo), str(total.hi)),
        certification_status="PRIME_SIDE_INTERVAL_CERTIFICATE_POINTWISE_CONVOLUTION_NOT_CERTIFIED",
    )


def write_prime_side_interval_certificate(path: Path) -> None:
    cert = compute_prime_side_interval_certificate()

    payload: Dict[str, Any] = {
        "phase": "X15",
        "status": "PHASE_X15_PRIME_SIDE_INTERVAL_CERTIFICATE_COMPLETE",
        "certificate": cert.to_dict(),
        "scope": "finite prime side only",
        "full_entry_certified": False,
        "pointwise_convolution_certified": False,
        "audit_strings": [
            "PHASE_X15_PRIME_SIDE_INTERVAL_CERTIFICATE_COMPLETE",
            "FINITE_PRIME_CUTOFF_USED",
            "VON_MANGOLDT_FINITE_TERMS_CREATED",
            "PRIME_SIDE_INTERVAL_SUM_CREATED",
            "FINITE_PRIME_SIDE_INTERVAL_SUMMATION_PROVED",
            "POINTWISE_CONVOLUTION_CERTIFICATION_BLOCKER_IDENTIFIED",
            "PRIME_SIDE_CERTIFICATE_POINTWISE_CONVOLUTION_NOT_CERTIFIED",
            "FULL_T_BL_ENTRY_NOT_CERTIFIED",
            "CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED",
            "READY_FOR_PHASE_X16_CONSTANT_TERM_INTERVAL_CERTIFICATE",
        ],
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_prime_side_interval_certificate(
        Path("breakthrough_attack/phase_x15_prime_side_interval_certificate/prime_side_interval_certificate.json")
    )
    print("Wrote prime-side interval certificate")
