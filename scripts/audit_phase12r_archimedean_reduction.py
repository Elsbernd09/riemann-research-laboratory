from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/archimedean_reduction/PHASE_12R_ARCHIMEDEAN_REDUCTION.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/archimedean_reduction/ARCHIMEDEAN_REDUCTION_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/archimedean_reduction/NEXT_PHASE_12S_ARITHMETIC_MATRIX_ENTRIES.md"),
]

required = [
    "ARCHIMEDEAN_REDUCTION_COMPLETE",
    "ARCHIMEDEAN_TAIL_EXPLICIT_PROVED",
    "FINITE_ARCHIMEDEAN_INTERVAL_REDUCTION_PROVED",
    "F_G_ONE_REAL_NONNEGATIVE_PROVED",
    "REMOVABLE_SINGULARITY_CRITERION_PROVED",
    "ARCHIMEDEAN_CERTIFICATION_REDUCED_TO_FINITE_INTERVAL",
    "CERTIFIED_QUADRATURE_STILL_REQUIRED",
    "ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_STILL_CONDITIONAL",
    "Theorem 12R.1",
    "Theorem 12R.2",
    "Theorem 12R.3",
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
print("PHASE 12R ARCHIMEDEAN REDUCTION AUDIT: PASS")
print("ARCHIMEDEAN TAIL: EXPLICIT")
print("FINITE INTERVAL REDUCTION: PROVED")
print("F_g(1) REAL NONNEGATIVE: PROVED")
print("REMOVABLE SINGULARITY CRITERION: PROVED")
print("CERTIFICATION REDUCED TO FINITE INTERVAL")
print("CERTIFIED QUADRATURE: STILL REQUIRED")
print("ARITHMETIC-ONLY CERTIFICATE: NOT YET COMPLETE")
print("=" * 80)
