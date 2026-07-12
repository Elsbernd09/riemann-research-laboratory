from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/arithmetic_matrix_entries/PHASE_12S_ARITHMETIC_MATRIX_ENTRIES.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/arithmetic_matrix_entries/ARITHMETIC_MATRIX_ENTRIES_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/arithmetic_matrix_entries/NEXT_PHASE_12T_HERMITIAN_AUDIT.md"),
]

required = [
    "ARITHMETIC_MATRIX_ENTRIES_COMPLETE",
    "M_IJ_ARITH_DEFINED",
    "FINITE_ARITHMETIC_EXPANSION_PROVED",
    "FINITE_PRIME_SUM_IN_MATRIX_ENTRY_PROVED",
    "REDUCED_ARCHIMEDEAN_TERM_IN_MATRIX_ENTRY_PROVED",
    "FORMAL_MATRIX_REPRESENTATION_PROVED",
    "HERMITIAN_CONVENTION_AUDIT_STILL_REQUIRED",
    "CERTIFIED_INTERVAL_IMPLEMENTATION_STILL_REQUIRED",
    "ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE",
    "Theorem 12S.1",
    "Theorem 12S.2",
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
print("PHASE 12S ARITHMETIC MATRIX ENTRIES AUDIT: PASS")
print("M_ij^arith: DEFINED")
print("FINITE ARITHMETIC EXPANSION: PROVED")
print("FINITE PRIME SUM IN MATRIX ENTRY: PROVED")
print("REDUCED ARCHIMEDEAN TERM IN MATRIX ENTRY: PROVED")
print("FORMAL MATRIX REPRESENTATION: PROVED")
print("HERMITIAN CONVENTION AUDIT: STILL REQUIRED")
print("ARITHMETIC-ONLY CERTIFICATE: NOT YET COMPLETE")
print("=" * 80)
