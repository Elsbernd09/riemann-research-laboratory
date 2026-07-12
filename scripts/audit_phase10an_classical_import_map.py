from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/classical_import_map/PHASE_10AN_CLASSICAL_IMPORT_MAP.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/classical_import_map/IMPORT_MAP_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/classical_import_map/NEXT_PHASE_10AO_PLAN.md"),
]

required = [
    "CLASSICAL_IMPORT_MAP",
    "TOY_TO_CLASSICAL_OBJECT_MAP",
    "TEST_FUNCTION_SPACE_IMPORT_MISSING",
    "INFINITE_WEIL_FORM_IMPORT_MISSING",
    "RH_RELATION_IMPORT_MISSING",
    "FINITE_MATRIX_CLASSICAL_VALIDATION_MISSING",
    "APPROXIMATION_MAP_MISSING",
    "CONVERGENCE_THEOREM_MISSING",
    "NOT_RH_CONTRIBUTION_YET",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove convergence",
    "This phase does not claim novelty",
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
print("PHASE 10AN CLASSICAL IMPORT MAP AUDIT: PASS")
print("TOY-TO-CLASSICAL OBJECT MAP: LOCKED")
print("MISSING CLASSICAL OBJECTS: RECORDED")
print("CONVERGENCE THEOREM: STILL MISSING")
print("RH CONTRIBUTION: NOT YET")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
