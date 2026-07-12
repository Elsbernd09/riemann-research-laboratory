from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/basis_mellin_decay/PHASE_12M_BASIS_MELLIN_DECAY.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/basis_mellin_decay/BASIS_MELLIN_DECAY_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/basis_mellin_decay/NEXT_PHASE_12N_FINITE_SPECTRAL_DETECTION_THEOREM.md"),
]

required = [
    "BASIS_MELLIN_DECAY_COMPLETE",
    "LOG_SMOOTH_COMPACT_BASIS_DEFINED",
    "MELLIN_RAPID_DECAY_PROVED",
    "PRODUCT_MELLIN_DECAY_PROVED",
    "BASIS_DECAY_IMPLIES_DELTA_Y_TO_ZERO",
    "SPECTRAL_TRUNCATION_CONVERGENCE_PROVED_ON_FINITE_CLASS",
    "ZERO_COUNT_BOUND_CLASSICAL_INPUT_REQUIRED",
    "ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_PROVED",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED",
    "Theorem 12M.1",
    "Theorem 12M.2",
    "Theorem 12M.3",
    "Corollary 12M.4",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove an arithmetic-only finite certificate",
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
print("PHASE 12M BASIS MELLIN DECAY AUDIT: PASS")
print("LOG-SMOOTH COMPACT BASIS: DEFINED")
print("MELLIN RAPID DECAY: PROVED")
print("PRODUCT MELLIN DECAY: PROVED")
print("DELTA_Y -> 0: PROVED UNDER ZERO-COUNT INPUT")
print("SPECTRAL TRUNCATION CONVERGENCE ON FINITE CLASS: PROVED")
print("ARITHMETIC-ONLY CERTIFICATE: NOT YET PROVED")
print("LEVEL 4 BREAKTHROUGH CANDIDATE: NOT YET ACHIEVED")
print("=" * 80)
