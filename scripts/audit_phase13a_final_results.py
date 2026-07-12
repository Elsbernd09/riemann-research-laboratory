from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/final_results_audit/PHASE_13A_FINAL_RESULTS_AUDIT.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/final_results_audit/FINAL_RESULTS_AUDIT_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/final_results_audit/NEXT_PHASE_13B_PROFESSOR_PACKAGE.md"),
]

required = [
    "FINAL_RESULTS_AUDIT_COMPLETE",
    "FINITE_SPECTRAL_DETECTION_THEOREM_IDENTIFIED_AS_STRONGEST_RESULT",
    "ARITHMETIC_PROTOTYPE_BUILT_NOT_CERTIFIED",
    "PRIMARY_SOURCE_VALIDATION_STILL_REQUIRED",
    "CERTIFIED_QUADRATURE_STILL_REQUIRED",
    "RH_BREAKTHROUGH_NOT_ACHIEVED",
    "RH_CONTRIBUTION_NOT_ESTABLISHED",
    "NOVELTY_NOT_ESTABLISHED",
    "PROFESSOR_REVIEW_READY_AFTER_PACKAGING",
    "STOP_THEOREM_BUILDING_RECOMMENDED",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove a complete arithmetic-only finite certificate",
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
print("PHASE 13A FINAL RESULTS AUDIT: PASS")
print("STRONGEST RESULT: FINITE SPECTRAL DETECTION THEOREM")
print("ARITHMETIC PROTOTYPE: BUILT BUT NOT CERTIFIED")
print("PRIMARY SOURCE VALIDATION: STILL REQUIRED")
print("CERTIFIED QUADRATURE: STILL REQUIRED")
print("RH BREAKTHROUGH: NOT ACHIEVED")
print("RH CONTRIBUTION: NOT ESTABLISHED")
print("NOVELTY: NOT ESTABLISHED")
print("PROFESSOR REVIEW: READY AFTER PACKAGING")
print("STOP THEOREM BUILDING: RECOMMENDED")
print("=" * 80)
