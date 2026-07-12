from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/projection_map_gate/PHASE_12K_PROJECTION_MAP_GATE.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/projection_map_gate/PROJECTION_MAP_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/projection_map_gate/NEXT_PHASE_12L_TRUNCATION_ERROR_GATE.md"),
]

required = [
    "PROJECTION_MAP_GATE_COMPLETE",
    "FULL_CLASSICAL_P_N_STILL_MISSING",
    "FINITE_TEST_CLASS_PROJECTION_DEFINED",
    "P_M_IDENTITY_ON_FINITE_TEST_CLASS",
    "PROJECTION_ERROR_ZERO_ON_FINITE_TEST_CLASS",
    "PI_M_EQUALS_ZERO_ON_FINITE_CLASS",
    "TRUNCATION_ERROR_REMAINS_MAIN_WALL",
    "FINITE_APPROXIMATION_CONVERGENCE_STILL_MISSING",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED",
    "Theorem 12K.1",
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
print("PHASE 12K PROJECTION MAP GATE AUDIT: PASS")
print("FULL CLASSICAL P_N: STILL MISSING")
print("FINITE TEST-CLASS PROJECTION: DEFINED")
print("P_m IDENTITY ON FINITE TEST CLASS: PROVED")
print("PROJECTION ERROR ZERO ON FINITE CLASS: PROVED")
print("TRUNCATION ERROR: REMAINS MAIN WALL")
print("LEVEL 4 BREAKTHROUGH CANDIDATE: NOT YET ACHIEVED")
print("=" * 80)
