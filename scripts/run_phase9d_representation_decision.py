from __future__ import annotations

from pathlib import Path

input_path = Path("weil_reconstruction/eigenvalue_validation/PHASE_9C_REPRESENTATION_NORMALIZATION_AUDIT_OUTPUT.txt")
output_path = Path("weil_reconstruction/eigenvalue_validation/PHASE_9D_REPRESENTATION_DECISION_OUTPUT.txt")

if not input_path.exists():
    raise FileNotFoundError("Phase 9C output not found. Run Phase 9C first.")

text = input_path.read_text(encoding="utf-8")

if "REPRESENTATION_LOCK_STATUS=PRELIMINARY_SYNTHETIC_LOCK_POSSIBLE" in text:
    status = "PRELIMINARY_SYNTHETIC_LOCK_POSSIBLE"
    next_track = "FINAL_SYNTHETIC_VALIDATION_SUITE"
    decision = (
        "The Phase 9B/9C synthetic cases passed the current representation gate. "
        "The next phase may run a broader final synthetic validation suite, still with no zeta zeros."
    )
elif "REPRESENTATION_LOCK_STATUS=REPRESENTATION_NOT_LOCKED" in text:
    status = "REPRESENTATION_NOT_LOCKED"
    next_track = "REPRESENTATION_REPAIR_REQUIRED"
    decision = (
        "The representation is not locked. The next phase must repair normalization, Hermitian conversion, "
        "or multiplicity handling before stronger synthetic validation."
    )
else:
    status = "UNKNOWN"
    next_track = "MANUAL_AUDIT_REQUIRED"
    decision = (
        "The Phase 9C status could not be parsed. The next phase must manually inspect the Phase 9C output."
    )

lines = [
    "PHASE 9D REPRESENTATION DECISION OUTPUT",
    "",
    f"PHASE_9C_STATUS={status}",
    f"NEXT_TRACK={next_track}",
    f"Decision: {decision}",
    "",
    "Allowed next actions:",
]

if next_track == "FINAL_SYNTHETIC_VALIDATION_SUITE":
    lines.extend([
        "  - Run broader synthetic finite Gamma validation.",
        "  - Keep Hermitian gate active.",
        "  - Keep negative-eigenvalue tolerance active.",
        "  - Keep failure logging active.",
        "  - Use no zeta zeros.",
    ])
elif next_track == "REPRESENTATION_REPAIR_REQUIRED":
    lines.extend([
        "  - Inspect which candidates failed Hermitian gates.",
        "  - Compare raw, weighted, and similarity-symmetrized forms.",
        "  - Re-check source normalization for H(x,y;t).",
        "  - Re-check multiplicity weighting.",
        "  - Do not run final validation until repair passes.",
    ])
else:
    lines.extend([
        "  - Manually inspect Phase 9C output.",
        "  - Do not proceed to final validation.",
    ])

lines.extend([
    "",
    "Boundary:",
    "  No new eigenvalues computed in Phase 9D.",
    "  No zeta zeros used.",
    "  No RH claim.",
    "  No novelty claim.",
    "  No zeta-case Bombieri-Weil verification claim.",
    "",
])

output_path.write_text("\n".join(lines), encoding="utf-8")

print("=" * 80)
print("PHASE 9D REPRESENTATION DECISION: COMPLETE")
print(f"PHASE_9C_STATUS: {status}")
print(f"NEXT_TRACK: {next_track}")
print("NO NEW EIGENVALUES COMPUTED IN PHASE 9D")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
