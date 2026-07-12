from __future__ import annotations

from pathlib import Path
from typing import Dict, Any, List
import json
import math

from src.level4.certified_entry_metadata import (
    CertifiedEntryMetadata,
    EntryCertificationStatus,
    ErrorDecomposition,
    matrix_is_certified,
)
from src.level4.conventions import BOMBIERI_LAGARIAS_CONVENTION
from src.level4.prototype_floating_entry import compute_m00_prototype_value


def conservative_radius_from_components(components: Dict[str, float]) -> float:
    """
    Wide safety radius for interval-candidate status.

    This is intentionally conservative but not a rigorous proof bound.
    """
    values = [abs(v) for v in components.values() if isinstance(v, (int, float)) and math.isfinite(v)]
    scale = sum(values) if values else 1.0
    floor = 1.0
    return max(floor, 0.25 * scale)


def make_interval(lo: float, hi: float) -> List[float]:
    if lo <= hi:
        return [lo, hi]
    return [hi, lo]


def make_m00_interval_candidate_entry() -> Dict[str, Any]:
    c = BOMBIERI_LAGARIAS_CONVENTION
    comps = compute_m00_prototype_value(integral_steps=80, conv_steps=80)
    value = comps["entry_value"]
    radius = conservative_radius_from_components(comps)
    interval_value = make_interval(value - radius, value + radius)

    metadata = CertifiedEntryMetadata(
        entry_id="M_00_arith",
        basis_i=0,
        basis_j=0,
        source_name=c.source_name,
        normalization_label=c.normalization_label,
        mellin_transform=c.mellin_transform,
        involution=c.involution,
        conjugation_policy=c.conjugation_policy,
        convolution=c.convolution,
        constant_term=c.constant_term,
        pole_constraint_status=c.pole_constraint_status,
        certification_status=EntryCertificationStatus.INTERVAL_CANDIDATE,
        interval_value=interval_value,
        error_decomposition=ErrorDecomposition(
            prime_sum_error="CANDIDATE_ONLY_NOT_RIGOROUS",
            archimedean_quadrature_error="CANDIDATE_ONLY_NOT_RIGOROUS",
            convolution_error="CANDIDATE_ONLY_NOT_RIGOROUS",
            rounding_error="CANDIDATE_ONLY_NOT_RIGOROUS",
            normalization_error="BOMBIERI_LAGARIAS_NORMALIZATION_USED_BUT_FULL_REVIEW_STILL_REQUIRED",
            pole_constraint_error="POLE_CONSTRAINTS_PLAUSIBLE_NOT_FULLY_LOCKED",
        ),
        quadrature_method="midpoint floating-point toy quadrature with conservative non-rigorous radius",
        prime_cutoff="finite toy cutoff induced by B=1.2",
        archimedean_cutoff="toy finite cutoff B=1.2",
        reviewer_warnings=[
            "Interval candidate only.",
            "Error bounds are not rigorous.",
            "Not a certified interval entry.",
            "Do not use in a certified matrix.",
            "Do not use for RH claims.",
        ],
    )

    return {
        "phase": "B11",
        "status": "PHASE_B11_INTERVAL_CANDIDATE_ENTRY_COMPLETE",
        "entry_metadata": metadata.to_dict(),
        "components": comps,
        "prototype_value": value,
        "candidate_radius": radius,
        "candidate_interval": interval_value,
        "entry_is_certified": metadata.is_certified_interval_entry(),
        "matrix_with_this_entry_is_certified": matrix_is_certified([metadata]),
        "unresolved_error_gates": [
            "quadrature_error",
            "convolution_error",
            "archimedean_singularity_error",
            "rounding_error",
            "basis_smoothness_error",
            "pole_constraint_error",
            "source_normalization_review",
        ],
        "audit_strings": [
            "PHASE_B11_INTERVAL_CANDIDATE_ENTRY_COMPLETE",
            "M_00_ARITH_INTERVAL_CANDIDATE_CREATED",
            "INTERVAL_CANDIDATE_STATUS_USED",
            "CONSERVATIVE_INTERVAL_WRAPPER_CREATED",
            "ERROR_GATES_RECORDED",
            "INTERVAL_CANDIDATE_ENTRY_NOT_CERTIFIED",
            "CERTIFIED_MATRIX_CANNOT_USE_INTERVAL_CANDIDATE",
            "BREAKTHROUGH_NOT_ACHIEVED",
            "READY_FOR_PHASE_B12_CERTIFIED_ERROR_BOUND_AUDIT",
        ],
    }


def write_m00_interval_candidate_entry(path: Path) -> None:
    payload = make_m00_interval_candidate_entry()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_m00_interval_candidate_entry(
        Path("breakthrough_push/phase_b11_interval_candidate_entry/M_00_interval_candidate_entry.json")
    )
    print("Wrote M_00 interval candidate entry")
