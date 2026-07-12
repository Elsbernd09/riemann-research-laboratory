from __future__ import annotations

from dataclasses import dataclass, asdict, field
from enum import Enum
from pathlib import Path
from typing import Dict, Any, Optional, List
import json

from src.level4.conventions import BOMBIERI_LAGARIAS_CONVENTION


class EntryCertificationStatus(str, Enum):
    METADATA_ONLY = "METADATA_ONLY"
    PROTOTYPE_FLOATING_POINT = "PROTOTYPE_FLOATING_POINT"
    INTERVAL_CANDIDATE = "INTERVAL_CANDIDATE"
    CERTIFIED_INTERVAL_ENTRY = "CERTIFIED_INTERVAL_ENTRY"


@dataclass(frozen=True)
class ErrorDecomposition:
    prime_sum_error: Optional[str] = None
    archimedean_quadrature_error: Optional[str] = None
    convolution_error: Optional[str] = None
    rounding_error: Optional[str] = None
    normalization_error: Optional[str] = None
    pole_constraint_error: Optional[str] = None

    def complete_for_certification(self) -> bool:
        fields = asdict(self)
        return all(value not in (None, "", "UNKNOWN") for value in fields.values())


@dataclass(frozen=True)
class CertifiedEntryMetadata:
    entry_id: str
    basis_i: int
    basis_j: int
    source_name: str
    normalization_label: str
    mellin_transform: str
    involution: str
    conjugation_policy: str
    convolution: str
    constant_term: str
    pole_constraint_status: str
    certification_status: EntryCertificationStatus
    interval_value: Optional[List[float]] = None
    error_decomposition: ErrorDecomposition = field(default_factory=ErrorDecomposition)
    quadrature_method: str = "NOT_COMPUTED"
    prime_cutoff: str = "NOT_COMPUTED"
    archimedean_cutoff: str = "NOT_COMPUTED"
    reviewer_warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        payload = asdict(self)
        payload["certification_status"] = self.certification_status.value
        return payload

    def is_certified_interval_entry(self) -> bool:
        if self.certification_status != EntryCertificationStatus.CERTIFIED_INTERVAL_ENTRY:
            return False
        if self.interval_value is None or len(self.interval_value) != 2:
            return False
        lo, hi = self.interval_value
        if lo > hi:
            return False
        return self.error_decomposition.complete_for_certification()


def make_metadata_only_entry(entry_id: str, basis_i: int, basis_j: int) -> CertifiedEntryMetadata:
    c = BOMBIERI_LAGARIAS_CONVENTION
    return CertifiedEntryMetadata(
        entry_id=entry_id,
        basis_i=basis_i,
        basis_j=basis_j,
        source_name=c.source_name,
        normalization_label=c.normalization_label,
        mellin_transform=c.mellin_transform,
        involution=c.involution,
        conjugation_policy=c.conjugation_policy,
        convolution=c.convolution,
        constant_term=c.constant_term,
        pole_constraint_status=c.pole_constraint_status,
        certification_status=EntryCertificationStatus.METADATA_ONLY,
        reviewer_warnings=[
            "Metadata object only; no certified value computed.",
            "Pole constraints remain plausible but not fully locked.",
            "Do not use this entry in a certified matrix.",
        ],
    )


def matrix_is_certified(entries: List[CertifiedEntryMetadata]) -> bool:
    return bool(entries) and all(entry.is_certified_interval_entry() for entry in entries)


def write_metadata_schema_certificate(path: Path) -> None:
    example = make_metadata_only_entry("M_00_arith", 0, 0)
    payload = {
        "phase": "B8",
        "status": "PHASE_B8_CERTIFIED_ENTRY_METADATA_COMPLETE",
        "allowed_statuses": [status.value for status in EntryCertificationStatus],
        "example_metadata_only_entry": example.to_dict(),
        "example_is_certified": example.is_certified_interval_entry(),
        "certified_matrix_rule_example": matrix_is_certified([example]),
        "audit_strings": [
            "PHASE_B8_CERTIFIED_ENTRY_METADATA_COMPLETE",
            "CERTIFIED_ENTRY_METADATA_SCHEMA_CREATED",
            "ENTRY_CERTIFICATION_STATUS_LEVELS_DEFINED",
            "METADATA_ONLY_STATUS_DEFINED",
            "PROTOTYPE_FLOATING_POINT_STATUS_DEFINED",
            "INTERVAL_CANDIDATE_STATUS_DEFINED",
            "CERTIFIED_INTERVAL_ENTRY_STATUS_DEFINED",
            "CERTIFIED_MATRIX_REQUIRES_ALL_CERTIFIED_ENTRIES",
            "NORMALIZATION_REQUIRED_FOR_CERTIFICATION",
            "BREAKTHROUGH_NOT_ACHIEVED",
            "READY_FOR_PHASE_B9_METADATA_ONLY_ENTRY",
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_metadata_schema_certificate(
        Path("breakthrough_push/phase_b8_certified_entry_metadata/metadata_schema_certificate.json")
    )
    print("Wrote metadata schema certificate")
