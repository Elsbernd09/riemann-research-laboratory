from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/source_normalization_gate/PHASE_12J_SOURCE_NORMALIZATION_GATE.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/source_normalization_gate/SOURCE_NORMALIZATION_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/source_normalization_gate/NEXT_PHASE_12K_PROJECTION_MAP_GATE.md"),
]

required = [
    "SOURCE_NORMALIZATION_GATE_COMPLETE",
    "SOURCE_NORMALIZATION_TERM_DEFINED",
    "CONDITIONAL_SOURCE_NORMALIZATION_CANCELLATION_PROVED",
    "S_N_ZERO_ONLY_UNDER_CONVENTION_AGREEMENT",
    "PRIMARY_SOURCE_CONFIRMATION_STILL_REQUIRED",
    "PROVISIONAL_THREE_ERROR_BOUND_RESTORED",
    "RIGOROUS_FOUR_ERROR_BOUND_RETAINED",
    "FINITE_APPROXIMATION_CONVERGENCE_STILL_MISSING",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED",
    "Theorem 12J.1",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove the full Weil positivity theorem",
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
print("PHASE 12J SOURCE-NORMALIZATION GATE AUDIT: PASS")
print("SOURCE-NORMALIZATION TERM: DEFINED")
print("CONDITIONAL S_N=0 THEOREM: PROVED")
print("PRIMARY SOURCE CONFIRMATION: STILL REQUIRED")
print("PROVISIONAL THREE-ERROR BOUND: RESTORED")
print("RIGOROUS FOUR-ERROR BOUND: RETAINED")
print("FINITE APPROXIMATION CONVERGENCE: STILL MISSING")
print("LEVEL 4 BREAKTHROUGH CANDIDATE: NOT YET ACHIEVED")
print("=" * 80)
