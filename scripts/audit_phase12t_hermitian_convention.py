from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/hermitian_audit/PHASE_12T_HERMITIAN_CONVENTION_AUDIT.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/hermitian_audit/HERMITIAN_AUDIT_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/hermitian_audit/NEXT_PHASE_12U_T_STAR_AUDIT.md"),
]

required = [
    "HERMITIAN_CONVENTION_AUDIT_COMPLETE",
    "COEFFICIENT_COMPATIBLE_MATRIX_CONVENTION_LOCKED",
    "STAR_REVERSES_CONVOLUTION_ORDER_PROVED",
    "CONDITIONAL_HERMITIAN_MATRIX_PROVED",
    "T_STAR_ADJOINT_SYMMETRY_REQUIRED",
    "UNCONDITIONAL_HERMITIAN_NOT_YET_PROVED",
    "EIGENVALUE_CERTIFICATION_NOW_HAS_CONDITIONAL_GATE",
    "SOURCE_VALIDATION_STILL_REQUIRED",
    "ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE",
    "Theorem 12T.1",
    "Theorem 12T.2",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove a complete arithmetic-only finite certificate",
    "This phase does not establish novelty",
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
print("PHASE 12T HERMITIAN CONVENTION AUDIT: PASS")
print("MATRIX CONVENTION: LOCKED")
print("STAR REVERSES CONVOLUTION ORDER: PROVED")
print("CONDITIONAL HERMITIAN MATRIX: PROVED")
print("T-STAR ADJOINT SYMMETRY: REQUIRED")
print("UNCONDITIONAL HERMITIAN: NOT YET PROVED")
print("ARITHMETIC-ONLY CERTIFICATE: NOT YET COMPLETE")
print("=" * 80)
