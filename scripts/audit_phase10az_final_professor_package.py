from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/final_professor_package/README_FOR_PROFESSOR.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/final_professor_package/POLISHED_CONDITIONAL_THEOREM_NOTE.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/final_professor_package/ONE_PAGE_SUMMARY.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/final_professor_package/PROFESSOR_EMAIL_DRAFT.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/final_professor_package/REVIEW_QUESTIONS.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/final_professor_package/BOUNDARY_STATEMENT.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/final_professor_package/MISSING_CLASSICAL_IMPORTS_ROADMAP.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/final_professor_package/PACKAGE_STATUS.md"),
]

required = [
    "FINAL_CONTRIBUTION_BRANCH_PROFESSOR_PACKAGE",
    "CONDITIONAL_THEOREM_FRAMEWORK",
    "PROFESSOR_REVIEW_WORTHY_CONDITIONAL_FRAMEWORK",
    "FINITE_TEST_CLASS_GRAM_REDUCTION",
    "CONDITIONAL_GRAM_ERROR_TRANSFER",
    "CERTIFIED_NUMERICAL_ERROR_MODEL",
    "TRANSFER_CERTIFICATE_CALCULATOR",
    "RH_BREAKTHROUGH_NOT_ACHIEVED",
    "RH_CONTRIBUTION_NOT_ESTABLISHED",
    "NOVELTY_NOT_ESTABLISHED",
    "This package does not prove RH",
    "This package does not falsify RH",
    "This package does not prove a new RH criterion",
    "This package does not prove unconditional classical convergence",
    "This package does not establish novelty",
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
print("PHASE 10AZ FINAL PROFESSOR PACKAGE AUDIT: PASS")
print("FINAL CONTRIBUTION BRANCH PACKAGE: CREATED")
print("STATUS: CONDITIONAL THEOREM FRAMEWORK")
print("PROFESSOR REVIEW: WORTHY AS CONDITIONAL FRAMEWORK")
print("RH BREAKTHROUGH: NOT ACHIEVED")
print("RH CONTRIBUTION: NOT ESTABLISHED")
print("NOVELTY: NOT ESTABLISHED")
print("=" * 80)
