from __future__ import annotations

from dataclasses import dataclass, asdict
from decimal import Decimal
from pathlib import Path
from typing import Dict, Any, Tuple, List
import json

from src.breakthrough_attack.assemble_full_m00_interval_certificate import (
    compute_full_m00_interval_certificate,
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

    @staticmethod
    def point(x) -> "DecimalInterval":
        dx = Decimal(str(x))
        return DecimalInterval(dx, dx)

    def __add__(self, other: "DecimalInterval") -> "DecimalInterval":
        return DecimalInterval(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other: "DecimalInterval") -> "DecimalInterval":
        return DecimalInterval(self.lo - other.hi, self.hi - other.lo)

    def __mul__(self, other: "DecimalInterval") -> "DecimalInterval":
        vals = [
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        ]
        return DecimalInterval(min(vals), max(vals))

    def scale(self, s: Decimal) -> "DecimalInterval":
        if s >= 0:
            return DecimalInterval(s * self.lo, s * self.hi)
        return DecimalInterval(s * self.hi, s * self.lo)

    def to_tuple_str(self) -> Tuple[str, str]:
        return (str(self.lo), str(self.hi))

    def to_dict(self) -> Dict[str, str]:
        return {"lo": str(self.lo), "hi": str(self.hi)}


@dataclass(frozen=True)
class TwoByTwoMatrixCertificateCandidate:
    matrix_entries: List[List[Tuple[str, str]]]
    trace_interval: Tuple[str, str]
    determinant_interval: Tuple[str, str]
    hermitian_consistency: bool
    construction_notes: List[str]
    unresolved_gates: List[str]
    certification_status: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def determinant_2x2(
    m00: DecimalInterval,
    m01: DecimalInterval,
    m10: DecimalInterval,
    m11: DecimalInterval,
) -> DecimalInterval:
    return (m00 * m11) - (m01 * m10)


def compute_two_by_two_matrix_certificate_candidate() -> TwoByTwoMatrixCertificateCandidate:
    full = compute_full_m00_interval_certificate()
    m00 = DecimalInterval.from_tuple_str(full.assembled_m00_interval)

    # Candidate-only synthetic expansion around M00.
    # This is deliberately marked not fully certified.
    radius_scale = Decimal("0.10")

    width = m00.hi - m00.lo
    padding = width * radius_scale if width > 0 else Decimal("1e-6")

    m11 = DecimalInterval(m00.lo - padding, m00.hi + padding)
    off = m00.scale(Decimal("0.05"))
    m01 = off
    m10 = off

    trace = m00 + m11
    det = determinant_2x2(m00, m01, m10, m11)

    unresolved = [
        "independent M01 construction",
        "independent M10 construction",
        "independent M11 construction",
        "certified pointwise convolution for all entries",
        "certified coefficient solves for all basis functions",
        "formal outward rounding",
        "finite-to-Weil positivity theorem",
        "prior-art review",
    ]

    notes = [
        "M00 imported from X18 assembled interval certificate candidate",
        "M11 and off-diagonal entries are prototype intervals, not independently certified",
        "Hermitian consistency imposed by using identical real intervals for M01 and M10",
        "Trace and determinant intervals are candidate diagnostics only",
    ]

    return TwoByTwoMatrixCertificateCandidate(
        matrix_entries=[
            [m00.to_tuple_str(), m01.to_tuple_str()],
            [m10.to_tuple_str(), m11.to_tuple_str()],
        ],
        trace_interval=trace.to_tuple_str(),
        determinant_interval=det.to_tuple_str(),
        hermitian_consistency=(m01.to_tuple_str() == m10.to_tuple_str()),
        construction_notes=notes,
        unresolved_gates=unresolved,
        certification_status="TWO_BY_TWO_MATRIX_CERTIFICATE_CANDIDATE_NOT_FULLY_CERTIFIED",
    )


def write_two_by_two_matrix_certificate_candidate(path: Path) -> None:
    cert = compute_two_by_two_matrix_certificate_candidate()

    payload: Dict[str, Any] = {
        "phase": "X21",
        "status": "PHASE_X21_TWO_BY_TWO_MATRIX_CERTIFICATE_CANDIDATE_COMPLETE",
        "certificate": cert.to_dict(),
        "certified_finite_weil_matrix": False,
        "breakthrough_status": "NO_BREAKTHROUGH_YET",
        "audit_strings": [
            "PHASE_X21_TWO_BY_TWO_MATRIX_CERTIFICATE_CANDIDATE_COMPLETE",
            "FULL_M00_INTERVAL_IMPORTED",
            "TWO_BY_TWO_INTERVAL_MATRIX_CREATED",
            "HERMITIAN_CONSISTENCY_CHECK_CREATED",
            "TRACE_INTERVAL_CREATED",
            "DETERMINANT_INTERVAL_CREATED",
            "TWO_BY_TWO_MATRIX_CERTIFICATE_CANDIDATE_NOT_FULLY_CERTIFIED",
            "CERTIFIED_FINITE_WEIL_MATRIX_NOT_COMPUTED",
            "NO_BREAKTHROUGH_YET",
            "READY_FOR_PHASE_X22_FINAL_BREAKTHROUGH_CANDIDATE_VERDICT",
        ],
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_two_by_two_matrix_certificate_candidate(
        Path("breakthrough_attack/phase_x21_two_by_two_matrix_certificate_candidate/two_by_two_matrix_certificate_candidate.json")
    )
    print("Wrote two-by-two matrix certificate candidate")
