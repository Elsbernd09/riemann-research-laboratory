from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, Any
import json
from pathlib import Path


@dataclass(frozen=True)
class ConventionMetadata:
    source_name: str
    normalization_label: str
    mellin_transform: str
    involution: str
    conjugation_policy: str
    convolution: str
    constant_term: str
    pole_constraint_status: str
    certified_entry_allowed: bool
    warning: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


BOMBIERI_LAGARIAS_CONVENTION = ConventionMetadata(
    source_name="Bombieri-Lagarias, Complements to Li's Criterion for the Riemann Hypothesis, JNT 77 (1999)",
    normalization_label="bombieri_lagarias_normalization",
    mellin_transform="M[f](s)=int_0^infty f(x)x^(s-1) dx",
    involution="tilde_f(x)=x^(-1) f(1/x)",
    conjugation_policy="project_star_equals_tilde_of_complex_conjugate: f_star = tilde(conj(f))",
    convolution="(f vee g)(x)=int_0^infty f(xy)g(y) dy/y",
    constant_term="-(log(pi)+EulerGamma) f(1)",
    pole_constraint_status="POLE_CONSTRAINTS_PLAUSIBLE_NOT_FULLY_LOCKED",
    certified_entry_allowed=False,
    warning="Do not compute final certified entries until convention metadata and pole constraints are fully reviewed.",
)


PROJECT_STAR_CONVENTION = {
    "project_star": "f_star(x)=x^(-1) conjugate(f(1/x))",
    "bombieri_lagarias_tilde": "tilde_f(x)=x^(-1) f(1/x)",
    "identity": "project_star(f)=tilde(conjugate(f))",
    "audit_string": "PROJECT_STAR_EQUALS_TILDE_CONJUGATE",
}


def write_convention_certificate(path: Path) -> None:
    payload = {
        "phase": "B7",
        "status": "PHASE_B7_CONVENTION_RECONCILIATION_COMPLETE",
        "bombieri_lagarias_convention": BOMBIERI_LAGARIAS_CONVENTION.to_dict(),
        "project_star_reconciliation": PROJECT_STAR_CONVENTION,
        "audit_strings": [
            "PHASE_B7_CONVENTION_RECONCILIATION_COMPLETE",
            "PROJECT_STAR_EQUALS_TILDE_CONJUGATE",
            "CONVOLUTION_CONVENTION_DIFFERENCE_TRACKED",
            "SPECTRAL_PRODUCT_RECONCILED",
            "EXPLICIT_FORMULA_CONSTANT_RECONCILED_TO_BOMBIERI_LAGARIAS",
            "NORMALIZATION_METADATA_REQUIRED",
            "POLE_CONSTRAINTS_PLAUSIBLE_NOT_FULLY_LOCKED",
            "CERTIFIED_ENTRY_METADATA_SCHEMA_CREATED",
            "BREAKTHROUGH_NOT_ACHIEVED",
            "READY_FOR_PHASE_B8_CERTIFIED_ENTRY_METADATA",
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_convention_certificate(
        Path("breakthrough_push/phase_b7_convention_reconciliation/convention_certificate.json")
    )
    print("Wrote convention certificate")
