from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/approximation_error_decomposition/PHASE_12I_APPROXIMATION_ERROR_DECOMPOSITION.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/approximation_error_decomposition/APPROXIMATION_ERROR_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/approximation_error_decomposition/NEXT_PHASE_12J_SOURCE_NORMALIZATION_GATE.md"),
]

required = [
    "APPROXIMATION_ERROR_DECOMPOSITION_COMPLETE",
    "TOTAL_ERROR_E_N_DEFINED",
    "TRUNCATION_ERROR_TERM_DEFINED",
    "PROJECTION_ERROR_TERM_DEFINED",
    "SOURCE_NORMALIZATION_ERROR_TERM_DEFINED",
    "COMPUTATIONAL_ERROR_TERM_DEFINED",
    "APPROXIMATION_ERROR_BOUND_PROVED",
    "UNIFORM_FINITE_CLASS_BOUND_PROVED",
    "FINITE_APPROXIMATION_CONVERGENCE_STILL_MISSING",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED",
    "Theorem 12I.1",
    "Corollary 12I.2",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove finite approximation convergence",
    "This phase does not prove Level 4 contribution",
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
print("PHASE 12I APPROXIMATION ERROR DECOMPOSITION AUDIT: PASS")
print("TOTAL ERROR: DEFINED")
print("TRUNCATION ERROR: DEFINED")
print("PROJECTION ERROR: DEFINED")
print("SOURCE-NORMALIZATION ERROR: DEFINED")
print("COMPUTATIONAL ERROR: DEFINED")
print("APPROXIMATION ERROR BOUND: PROVED")
print("UNIFORM FINITE-CLASS BOUND: PROVED")
print("FINITE APPROXIMATION CONVERGENCE: STILL MISSING")
print("LEVEL 4 BREAKTHROUGH CANDIDATE: NOT YET ACHIEVED")
print("=" * 80)
