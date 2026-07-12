from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/negative_obstruction_template/PHASE_12H_NEGATIVE_OBSTRUCTION_TEMPLATE.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/negative_obstruction_template/NEGATIVE_OBSTRUCTION_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/negative_obstruction_template/NEXT_PHASE_12I_APPROXIMATION_ERROR_DECOMPOSITION.md"),
]

required = [
    "NEGATIVE_OBSTRUCTION_TEMPLATE_COMPLETE",
    "NEGATIVE_DETECTION_TEMPLATE_PROVED",
    "EVENTUAL_FINITE_DETECTION_COROLLARY_PROVED",
    "UNIFORM_FINITE_CLASS_DETECTION_PROVED",
    "FINITE_APPROXIMATION_THEOREM_STILL_MISSING",
    "EPSILON_N_CONVERGENCE_STILL_MISSING",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED",
    "Theorem 12H.1",
    "Corollary 12H.2",
    "Theorem 12H.3",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove the full Weil positivity theorem",
    "This phase does not prove the finite approximation theorem",
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
print("PHASE 12H NEGATIVE OBSTRUCTION TEMPLATE AUDIT: PASS")
print("NEGATIVE DETECTION TEMPLATE: PROVED")
print("EVENTUAL FINITE DETECTION COROLLARY: PROVED")
print("UNIFORM FINITE-CLASS DETECTION: PROVED")
print("FINITE APPROXIMATION THEOREM: STILL MISSING")
print("LEVEL 4 BREAKTHROUGH CANDIDATE: NOT YET ACHIEVED")
print("=" * 80)
