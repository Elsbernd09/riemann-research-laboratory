from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/classical_definition_extraction/PHASE_10AO_CLASSICAL_DEFINITION_EXTRACTION_LEDGER.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/classical_definition_extraction/EXTRACTION_STATUS_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/classical_definition_extraction/NEXT_PHASE_10AP_CONVERGENCE_SKELETON.md"),
]

required = [
    "CLASSICAL_DEFINITION_EXTRACTION_LEDGER",
    "KNOWN_DEFINITION_KNOWN_THEOREM_PROJECT_DEFINITION_PROJECT_ASSUMPTION_MISSING",
    "TRUE_WEIL_FORM_MISSING",
    "TRUE_TEST_FUNCTION_DOMAIN_MISSING",
    "RH_POSITIVITY_RELATION_MISSING",
    "CLASSICAL_APPROXIMATION_MAP_MISSING",
    "QUANTITATIVE_CONVERGENCE_THEOREM_MISSING",
    "CONTRIBUTION_BOTTLENECK_IDENTIFIED",
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
print("PHASE 10AO CLASSICAL DEFINITION EXTRACTION AUDIT: PASS")
print("EXTRACTION LEDGER: CREATED")
print("MISSING CLASSICAL OBJECTS: RECORDED")
print("CONTRIBUTION BOTTLENECK: IDENTIFIED")
print("CONVERGENCE THEOREM: STILL MISSING")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
