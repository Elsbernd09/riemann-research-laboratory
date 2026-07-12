from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/true_weil_form_import/PHASE_12B_TRUE_WEIL_FORM_IMPORT_ATTEMPT.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/true_weil_form_import/IMPORTED_T_FUNCTIONAL_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/true_weil_form_import/NEXT_PHASE_12C_QUADRATIC_FORM_IMPORT.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/true_weil_form_import/PHASE_12B_SOURCE_SCAN_REPORT.md"),
]

required = [
    "TRUE_WEIL_FORM_IMPORT_ATTEMPT",
    "SOURCE_EXTRACTED_BOMBIIERI_FUNCTIONAL_IMPORTED",
    "T_FUNCTIONAL_IMPORTED",
    "TRUE_WEIL_QUADRATIC_FORM_STILL_MISSING",
    "TEST_FUNCTION_DOMAIN_STILL_MISSING",
    "HERMITIAN_FORM_STILL_MISSING",
    "PARTIAL_CLASSICAL_IMPORT_ACHIEVED",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED",
    "PHASE_12B_SOURCE_SCAN_COMPLETE",
    "LOCAL_SOURCE_SCAN_PERFORMED",
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
print("PHASE 12B TRUE WEIL FORM IMPORT AUDIT: PASS")
print("T FUNCTIONAL: IMPORTED FROM PROJECT EXTRACTION")
print("TRUE WEIL QUADRATIC FORM: STILL MISSING")
print("TEST FUNCTION DOMAIN: STILL MISSING")
print("HERMITIAN FORM: STILL MISSING")
print("PARTIAL CLASSICAL IMPORT: ACHIEVED")
print("LEVEL 4 BREAKTHROUGH CANDIDATE: NOT YET ACHIEVED")
print("=" * 80)
