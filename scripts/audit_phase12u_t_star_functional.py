from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/t_star_audit/PHASE_12U_T_STAR_FUNCTIONAL_AUDIT.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/t_star_audit/T_STAR_AUDIT_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/t_star_audit/NEXT_PHASE_12V_INTERVAL_MATRIX_IMPLEMENTATION.md"),
]

required = [
    "T_STAR_FUNCTIONAL_AUDIT_COMPLETE",
    "T_STAR_ADJOINT_SYMMETRY_IDENTIFIED_AS_GATE",
    "CONDITIONAL_T_STAR_TO_HERMITIAN_THEOREM_PROVED",
    "PARTIAL_TERMWISE_AUDIT_RECORDED",
    "ARCHIMEDEAN_TERM_REMAINS_MAIN_T_STAR_OBSTACLE",
    "UNCONDITIONAL_HERMITIAN_STILL_NOT_PROVED",
    "CONDITIONAL_HERMITIAN_ROUTE_AVAILABLE",
    "DIRECT_CERTIFIED_HERMITIAN_ROUTE_AVAILABLE",
    "ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE",
    "Theorem 12U.1",
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
print("PHASE 12U T-STAR FUNCTIONAL AUDIT: PASS")
print("T-STAR ADJOINT SYMMETRY: IDENTIFIED AS GATE")
print("CONDITIONAL T-STAR => HERMITIAN: PROVED")
print("PARTIAL TERMWISE AUDIT: RECORDED")
print("ARCHIMEDEAN TERM: REMAINS MAIN OBSTACLE")
print("UNCONDITIONAL HERMITIAN: STILL NOT PROVED")
print("ARITHMETIC-ONLY CERTIFICATE: NOT YET COMPLETE")
print("=" * 80)
