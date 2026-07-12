from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/synthesis/PHASE_11E_BREAKTHROUGH_ATTEMPT_SYNTHESIS.md"),
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/synthesis/BREAKTHROUGH_ATTEMPT_STATUS_LOCK.md"),
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/synthesis/NEXT_FINAL_DOCUMENT_PLAN.md"),
]

required = [
    "BREAKTHROUGH_ATTEMPT_SYNTHESIS",
    "REAL_CONDITIONAL_IMPROVEMENT",
    "KAPPA_ZERO_RELATIVE_TO_EXTRACTED_KERNEL",
    "THREE_ERROR_TRANSFER_BOUND_FINAL",
    "STRONGER_PROFESSOR_REVIEW_PACKAGE",
    "RH_BREAKTHROUGH_NOT_ACHIEVED",
    "RH_CONTRIBUTION_NOT_ESTABLISHED",
    "STOP_FOR_PROFESSOR_FEEDBACK_RECOMMENDED",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove full classical validation",
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
print("PHASE 11E BREAKTHROUGH ATTEMPT SYNTHESIS AUDIT: PASS")
print("REAL CONDITIONAL IMPROVEMENT: YES")
print("KAPPA ZERO RELATIVE TO EXTRACTED KERNEL: YES")
print("THREE-ERROR TRANSFER BOUND: FINAL")
print("RH BREAKTHROUGH: NOT ACHIEVED")
print("RH CONTRIBUTION: NOT ESTABLISHED")
print("RECOMMENDATION: STOP FOR PROFESSOR FEEDBACK")
print("=" * 80)
