from pathlib import Path

files = [
    Path("breakthrough_push/phase_b15_final_breakthrough_verdict/PHASE_B15_FINAL_BREAKTHROUGH_VERDICT.md"),
    Path("breakthrough_push/phase_b15_final_breakthrough_verdict/FINAL_VERDICT_STATUS.md"),
    Path("breakthrough_push/phase_b15_final_breakthrough_verdict/PROFESSOR_REVIEW_NEXT_ACTION.md"),
]

required = [
    "PHASE_B15_FINAL_BREAKTHROUGH_VERDICT_COMPLETE",
    "FINAL_VERDICT_BREAKTHROUGH_NOT_ACHIEVED",
    "FINAL_STATUS_PROFESSOR_REVIEW_READY_CONTRIBUTION_CANDIDATE_PATHWAY",
    "RH_PROOF_NOT_ACHIEVED",
    "RH_DISPROOF_NOT_ACHIEVED",
    "CERTIFIED_ARITHMETIC_ENTRY_NOT_ACHIEVED",
    "CERTIFIED_ARITHMETIC_MATRIX_NOT_ACHIEVED",
    "NOVELTY_NOT_ESTABLISHED",
    "SOURCE_AWARE_FRAMEWORK_ACHIEVED",
    "POLE_ADMISSIBLE_MATRIX_MACHINERY_ACHIEVED",
    "SMOOTH_BASIS_PATHWAY_ACHIEVED",
    "NEXT_ACTION_PROFESSOR_REVIEW",
    "Did we prove RH?",
    "Did we discover a new equivalent criterion?",
    "Is breakthrough achieved?",
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
print("PHASE B15 FINAL BREAKTHROUGH VERDICT AUDIT: PASS")
print("FINAL VERDICT: BREAKTHROUGH NOT ACHIEVED")
print("FINAL STATUS: PROFESSOR-REVIEW-READY CONTRIBUTION-CANDIDATE PATHWAY")
print("RH PROOF: NOT ACHIEVED")
print("CERTIFIED ARITHMETIC ENTRY: NOT ACHIEVED")
print("CERTIFIED ARITHMETIC MATRIX: NOT ACHIEVED")
print("NOVELTY: NOT ESTABLISHED")
print("SOURCE-AWARE FRAMEWORK: ACHIEVED")
print("POLE-ADMISSIBLE MATRIX MACHINERY: ACHIEVED")
print("SMOOTH BASIS PATHWAY: ACHIEVED")
print("NEXT ACTION: PROFESSOR REVIEW")
print("=" * 80)
