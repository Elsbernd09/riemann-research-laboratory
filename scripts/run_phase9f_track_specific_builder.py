from __future__ import annotations

from pathlib import Path

base = Path("weil_reconstruction/eigenvalue_validation")
output = base / "PHASE_9F_TRACK_SPECIFIC_BUILDER_OUTPUT.txt"

final_plan = base / "FINAL_SYNTHETIC_VALIDATION_PLAN.md"
repair_diag = base / "REPRESENTATION_REPAIR_DIAGNOSTIC.md"
manual_audit = base / "MANUAL_AUDIT_REQUIRED.md"

if final_plan.exists():
    track = "FINAL_SYNTHETIC_VALIDATION_SUITE"
elif repair_diag.exists():
    track = "REPRESENTATION_REPAIR_REQUIRED"
elif manual_audit.exists():
    track = "MANUAL_AUDIT_REQUIRED"
else:
    track = "UNKNOWN"

lines = [
    "PHASE 9F TRACK-SPECIFIC BUILDER OUTPUT",
    "",
    f"DETECTED_TRACK={track}",
    "",
]

if track == "FINAL_SYNTHETIC_VALIDATION_SUITE":
    next_file = base / "PHASE_9G_FINAL_SYNTHETIC_VALIDATION_SPEC.md"
    next_file.write_text(
        """# Phase 9G Final Synthetic Validation Specification

## Purpose

The next phase may run a broader synthetic finite validation suite because the prior track indicated preliminary synthetic lock is possible.

## Allowed

The next phase may compute eigenvalues on synthetic finite \(\Gamma\)-multisets only.

It must keep:

1. Hermitian residual gate;
2. negative-eigenvalue tolerance;
3. numerical-zero reporting;
4. failure logging;
5. no zeta-zero input.

## Required synthetic cases

1. all real values;
2. one non-real conjugate pair;
3. two non-real conjugate pairs;
4. repeated real values;
5. repeated non-real conjugate pair;
6. mixed real and non-real values;
7. asymmetric invalid control case that must be rejected;
8. near-real non-real pair stress test.

## Required output

The next phase must produce a table with:

- case name;
- selected representation;
- Hermitian residual;
- eigenvalues;
- negative count;
- numerical zero count;
- expected count;
- pass/fail;
- boundary statement.

## Forbidden

No zeta zeros.

No RH claims.

No novelty claims.

No zeta-case Bombieri-Weil verification claims.
""",
        encoding="utf-8",
    )
    lines.extend([
        "Created: PHASE_9G_FINAL_SYNTHETIC_VALIDATION_SPEC.md",
        "Next phase: run broader final synthetic validation suite.",
    ])

elif track == "REPRESENTATION_REPAIR_REQUIRED":
    next_file = base / "PHASE_9G_REPRESENTATION_REPAIR_SPEC.md"
    next_file.write_text(
        """# Phase 9G Representation Repair Specification

## Purpose

The next phase must repair the finite representation before any broader synthetic validation.

## Required repair sequence

1. Re-read the Phase 9B residuals.
2. Identify which candidate had the smallest Hermitian residual.
3. Re-check the source formula for \(K^*(x,y;t)\).
4. Re-check the source formula for \(H(x,y;t)\).
5. Compare the \(K^*\)-based implementation against the closed-form \(H\)-kernel if source confidence permits.
6. Re-check whether the denominator \(1/4+y^2\) should be attached to the column variable.
7. Re-check weighted inner-product interpretation.
8. Re-check similarity symmetrization.
9. Re-run synthetic validation only after an explicit repair.

## Required output

The next phase must produce:

- a repair diagnosis;
- the suspected source of mismatch or blocked gates;
- the exact repair attempted;
- a before/after Hermitian residual table;
- a statement that no zeta zeros were used.

## Forbidden

No zeta zeros.

No RH claims.

No novelty claims.

No zeta-case Bombieri-Weil verification claims.
""",
        encoding="utf-8",
    )
    lines.extend([
        "Created: PHASE_9G_REPRESENTATION_REPAIR_SPEC.md",
        "Next phase: repair representation before broader validation.",
    ])

elif track == "MANUAL_AUDIT_REQUIRED":
    next_file = base / "PHASE_9G_MANUAL_AUDIT_SPEC.md"
    next_file.write_text(
        """# Phase 9G Manual Audit Specification

## Purpose

The next phase must manually inspect the Phase 9D and Phase 9E outputs because the track was not machine-resolved.

## Required files to inspect

- `PHASE_9B_SYNTHETIC_EIGENVALUE_OUTPUT.txt`
- `PHASE_9C_REPRESENTATION_NORMALIZATION_AUDIT_OUTPUT.txt`
- `PHASE_9D_REPRESENTATION_DECISION_OUTPUT.txt`
- `PHASE_9E_FOLLOW_RECORDED_TRACK_OUTPUT.txt`

## Forbidden

No zeta zeros.

No RH claims.

No novelty claims.

No new eigenvalue runs until the track is resolved.
""",
        encoding="utf-8",
    )
    lines.extend([
        "Created: PHASE_9G_MANUAL_AUDIT_SPEC.md",
        "Next phase: manual audit.",
    ])

else:
    next_file = base / "PHASE_9G_UNKNOWN_TRACK_STOP.md"
    next_file.write_text(
        """# Phase 9G Unknown Track Stop

No valid Phase 9E track artifact was detected.

Stop and inspect the repository manually.

No zeta zeros.

No RH claims.

No novelty claims.
""",
        encoding="utf-8",
    )
    lines.extend([
        "Created: PHASE_9G_UNKNOWN_TRACK_STOP.md",
        "Next phase: stop and inspect manually.",
    ])

lines.extend([
    "",
    "Boundary:",
    "  No eigenvalues computed in Phase 9F.",
    "  No zeta zeros used.",
    "  No RH claim.",
    "  No novelty claim.",
    "  No zeta-case Bombieri-Weil verification claim.",
    "",
])

output.write_text("\n".join(lines), encoding="utf-8")

print("=" * 80)
print("PHASE 9F TRACK-SPECIFIC BUILDER: COMPLETE")
print(f"DETECTED_TRACK: {track}")
print("NO EIGENVALUES COMPUTED IN PHASE 9F")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
