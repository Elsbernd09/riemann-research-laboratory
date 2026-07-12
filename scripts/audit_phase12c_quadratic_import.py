from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/quadratic_form_import/PHASE_12C_QUADRATIC_WEIL_FORM_IMPORT_ATTEMPT.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/quadratic_form_import/QUADRATIC_IMPORT_GATE_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/quadratic_form_import/NEXT_PHASE_12D_EXTERNAL_SOURCE_REQUEST.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/quadratic_form_import/PHASE_12C_QUADRATIC_SOURCE_SCAN_REPORT.md"),
]

required = [
    "QUADRATIC_WEIL_FORM_IMPORT_ATTEMPT",
    "LOCAL_QUADRATIC_FORM_SCAN_PERFORMED",
    "T_FUNCTIONAL_AVAILABLE",
    "F_G_CONSTRUCTION_MISSING",
    "QUADRATIC_WEIL_FORM_NOT_FULLY_IMPORTED",
    "EXTERNAL_SOURCE_REVIEW_REQUIRED",
    "HONEST_GATE_FAILURE",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_BLOCKED",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED",
    "PHASE_12C_QUADRATIC_SOURCE_SCAN_COMPLETE",
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
print("PHASE 12C QUADRATIC WEIL FORM IMPORT AUDIT: PASS")
print("T FUNCTIONAL: AVAILABLE")
print("F_g CONSTRUCTION: MISSING")
print("QUADRATIC WEIL FORM: NOT FULLY IMPORTED")
print("HONEST GATE FAILURE: RECORDED")
print("EXTERNAL SOURCE REVIEW: REQUIRED")
print("LEVEL 4 BREAKTHROUGH CANDIDATE: BLOCKED")
print("=" * 80)
