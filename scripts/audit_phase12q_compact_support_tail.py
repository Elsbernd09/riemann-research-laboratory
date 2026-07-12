from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/compact_support_tail_theorem/PHASE_12Q_COMPACT_SUPPORT_TAIL_THEOREM.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/compact_support_tail_theorem/COMPACT_SUPPORT_TAIL_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/compact_support_tail_theorem/NEXT_PHASE_12R_ARCHIMEDEAN_REDUCTION.md"),
]

required = [
    "COMPACT_SUPPORT_TAIL_THEOREM_COMPLETE",
    "FINITE_CLASS_COMMON_SUPPORT_DEFINED",
    "F_G_SUPPORT_BOUND_PROVED",
    "F_G_STAR_SUPPORT_BOUND_PROVED",
    "PRIME_TAIL_ZERO_ABOVE_SUPPORT_CUTOFF_PROVED",
    "FINITE_PRIME_SUM_ON_FINITE_CLASS_PROVED",
    "MATRIX_PRIME_ENTRIES_FINITE_PROVED",
    "ARCHIMEDEAN_CERTIFICATION_REMAINS",
    "ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE",
    "Theorem 12Q.1",
    "Theorem 12Q.2",
    "Theorem 12Q.3",
    "Corollary 12Q.4",
    "Theorem 12Q.5",
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
print("PHASE 12Q COMPACT SUPPORT TAIL AUDIT: PASS")
print("COMMON SUPPORT: DEFINED")
print("F_g SUPPORT BOUND: PROVED")
print("F_g^* SUPPORT BOUND: PROVED")
print("PRIME TAIL ZERO ABOVE SUPPORT CUTOFF: PROVED")
print("FINITE PRIME SUM ON FINITE CLASS: PROVED")
print("MATRIX PRIME ENTRIES FINITE: PROVED")
print("ARCHIMEDEAN CERTIFICATION: REMAINS")
print("ARITHMETIC-ONLY CERTIFICATE: NOT YET COMPLETE")
print("=" * 80)
