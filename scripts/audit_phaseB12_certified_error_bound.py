from pathlib import Path

files = [
    Path("breakthrough_push/phase_b12_certified_error_bound_audit/PHASE_B12_CERTIFIED_ERROR_BOUND_AUDIT.md"),
    Path("breakthrough_push/phase_b12_certified_error_bound_audit/ERROR_GATE_TABLE.md"),
    Path("breakthrough_push/phase_b12_certified_error_bound_audit/NEXT_PHASE_B13_SMOOTH_BASIS_CERTIFICATION_PLAN.md"),
    Path("breakthrough_push/phase_b12_certified_error_bound_audit/CERTIFICATION_VERDICT.md"),
]

required = [
    "PHASE_B12_CERTIFIED_ERROR_BOUND_AUDIT_COMPLETE",
    "ERROR_GATES_AUDITED",
    "QUADRATURE_ERROR_HARD_BUT_POSSIBLE",
    "CONVOLUTION_ERROR_NEEDS_NEW_THEOREM_OR_IMPLEMENTATION",
    "ARCHIMEDEAN_SINGULARITY_BLOCKS_CERTIFICATION",
    "ROUNDING_ERROR_EASY_TO_CERTIFY",
    "TOY_BASIS_BLOCKS_TRUE_WEIL_CERTIFICATION",
    "POLE_CONSTRAINTS_REQUIRE_SOURCE_REVIEW",
    "SOURCE_NORMALIZATION_REQUIRES_REVIEW",
    "INTERVAL_CANDIDATE_NOT_CERTIFIED",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "READY_FOR_PHASE_B13_SMOOTH_BASIS_CERTIFICATION_PLAN",
    "Theorem B12.1",
    "Theorem B12.2",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a breakthrough",
    "This phase does not prove novelty",
    "This phase does not certify the interval candidate",
]

for path in files:
    if not path.exists():
        raise FileNotFoundError(path)
    text = path.read_text(encoding="utf-8")
    if "\x00" in text:
        raise ValueError(f"NUL byte found in {path}")

combined = "\n".join(path.read_text(encoding="utf-8") for path in files)
missing = [phrase for phrase in required if phrase.lower() not in combined.lower()]
if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

print("=" * 80)
print("PHASE B12 CERTIFIED ERROR-BOUND AUDIT: PASS")
print("ERROR GATES: AUDITED")
print("QUADRATURE ERROR: HARD BUT POSSIBLE")
print("CONVOLUTION ERROR: NEEDS NEW THEOREM OR IMPLEMENTATION")
print("ARCHIMEDEAN SINGULARITY: BLOCKS CERTIFICATION")
print("ROUNDING ERROR: EASY TO CERTIFY")
print("TOY BASIS: BLOCKS TRUE WEIL CERTIFICATION")
print("POLE CONSTRAINTS: REQUIRE SOURCE REVIEW")
print("SOURCE NORMALIZATION: REQUIRES REVIEW")
print("INTERVAL CANDIDATE: NOT CERTIFIED")
print("BREAKTHROUGH: NOT ACHIEVED")
print("=" * 80)
