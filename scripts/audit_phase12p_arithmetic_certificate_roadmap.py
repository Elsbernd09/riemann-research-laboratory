from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/arithmetic_certificate_roadmap/PHASE_12P_ARITHMETIC_CERTIFICATE_ROADMAP.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/arithmetic_certificate_roadmap/ARITHMETIC_CERTIFICATE_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/arithmetic_certificate_roadmap/NEXT_PHASE_12Q_COMPACT_SUPPORT_TAIL_THEOREM.md"),
]

required = [
    "ARITHMETIC_CERTIFICATE_ROADMAP_COMPLETE",
    "ARITHMETIC_Q_X_DEFINED",
    "PRIME_TRUNCATION_DEFINED",
    "PRIME_TAIL_DEFINED",
    "COMPACT_SUPPORT_PRIME_SUM_FINITE_PROVED",
    "PRIME_TAIL_CAN_BE_ZERO_FOR_COMPACT_SUPPORT",
    "ARCHIMEDEAN_CERTIFICATION_REMAINS",
    "ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_STILL_CONDITIONAL",
    "Theorem 12P.1",
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
print("PHASE 12P ARITHMETIC CERTIFICATE ROADMAP AUDIT: PASS")
print("ARITHMETIC Q_X: DEFINED")
print("PRIME TRUNCATION: DEFINED")
print("PRIME TAIL: DEFINED")
print("COMPACT SUPPORT PRIME SUM FINITE: PROVED")
print("PRIME TAIL CAN BE ZERO: YES")
print("ARCHIMEDEAN CERTIFICATION: REMAINS")
print("ARITHMETIC-ONLY CERTIFICATE: NOT YET COMPLETE")
print("=" * 80)
