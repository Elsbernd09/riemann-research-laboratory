from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/synthesis/PHASE_10AY_CONTRIBUTION_BRANCH_SYNTHESIS.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/synthesis/CONTRIBUTION_BRANCH_STATUS_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/synthesis/NEXT_PHASE_10AZ_FINAL_PACKAGE.md"),
]

required = [
    "CONTRIBUTION_BRANCH_SYNTHESIS",
    "STRONGER_CONDITIONAL_THEOREM_PACKAGE",
    "PROFESSOR_REVIEW_WORTHY_CONDITIONAL_FRAMEWORK",
    "FINITE_TEST_CLASS_GRAM_REDUCTION",
    "CONDITIONAL_GRAM_ERROR_TRANSFER",
    "CERTIFIED_NUMERICAL_ERROR_MODEL",
    "TRANSFER_CERTIFICATE_CALCULATOR",
    "RH_BREAKTHROUGH_NOT_ACHIEVED",
    "RH_CONTRIBUTION_NOT_ESTABLISHED",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove unconditional classical convergence",
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
print("PHASE 10AY CONTRIBUTION BRANCH SYNTHESIS AUDIT: PASS")
print("STATUS: STRONGER CONDITIONAL THEOREM PACKAGE")
print("PROFESSOR REVIEW: WORTHY AS CONDITIONAL FRAMEWORK")
print("RH BREAKTHROUGH: NOT ACHIEVED")
print("RH CONTRIBUTION: NOT ESTABLISHED")
print("NOVELTY: NOT ESTABLISHED")
print("=" * 80)
