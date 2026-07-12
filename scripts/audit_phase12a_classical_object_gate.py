from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/classical_object_import/PHASE_12A_CLASSICAL_OBJECT_IMPORT_GATE.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/classical_object_import/LEVEL4_GATE_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/classical_object_import/NEXT_PHASE_12B_TRUE_WEIL_FORM_IMPORT.md"),
]

required = [
    "LEVEL4_CANDIDATE_BRANCH_STARTED",
    "CLASSICAL_OBJECT_IMPORT_GATE",
    "TRUE_WEIL_FORM_MISSING",
    "TEST_FUNCTION_DOMAIN_MISSING",
    "APPROXIMATION_MAP_MISSING",
    "TRUNCATION_PROJECTION_BOUNDS_MISSING",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED",
    "NO_ARCHITECTURE_ONLY_PHASES_RULE",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
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
print("PHASE 12A CLASSICAL OBJECT IMPORT GATE AUDIT: PASS")
print("LEVEL 4 CANDIDATE BRANCH: STARTED")
print("TRUE WEIL FORM: MISSING")
print("TEST FUNCTION DOMAIN: MISSING")
print("APPROXIMATION MAP: MISSING")
print("TRUNCATION/PROJECTION BOUNDS: MISSING")
print("LEVEL 4 BREAKTHROUGH CANDIDATE: NOT YET ACHIEVED")
print("NO ARCHITECTURE-ONLY RULE: LOCKED")
print("=" * 80)
