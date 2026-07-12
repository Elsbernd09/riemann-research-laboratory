from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/polished_professor_package/README_FOR_PROFESSOR.md"),
    Path("original_results/finite_bombieri_stability/polished_professor_package/POLISHED_RESEARCH_NOTE.md"),
    Path("original_results/finite_bombieri_stability/polished_professor_package/PROFESSOR_EMAIL_DRAFT.md"),
    Path("original_results/finite_bombieri_stability/polished_professor_package/REVIEW_QUESTIONS.md"),
    Path("original_results/finite_bombieri_stability/polished_professor_package/BOUNDARY_AND_LIMITATIONS.md"),
    Path("original_results/finite_bombieri_stability/polished_professor_package/PACKAGE_STATUS.md"),
]

required = [
    "POLISHED_PROFESSOR_REVIEW_PACKAGE",
    "Explicit H-Kernel Support-Stability Certificates",
    "POLISHED_RESEARCH_NOTE",
    "PROFESSOR_EMAIL_DRAFT",
    "REVIEW_QUESTIONS",
    "BOUNDARY_AND_LIMITATIONS",
    "SERIOUS_FINITE_RESEARCH_NOTE_CANDIDATE",
    "READY_FOR_PROFESSOR_FEEDBACK_AFTER_POLISH",
    "NOT_A_BREAKTHROUGH_YET",
    "NOVELTY_NOT_ESTABLISHED",
    "This package does not prove RH",
    "This package does not falsify RH",
    "This package does not use zeta zeros",
    "This package does not claim novelty",
]

for path in files:
    if not path.exists():
        raise FileNotFoundError(path)
    text = path.read_text(encoding="utf-8")
    if "\x00" in text:
        raise ValueError(f"NUL byte found in {path}")

combined = "\n".join(path.read_text(encoding="utf-8") for path in files)

missing = [
    phrase for phrase in required
    if phrase.lower() not in combined.lower()
]

if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

print("=" * 80)
print("PHASE 10AI POLISHED PROFESSOR PACKAGE AUDIT: PASS")
print("POLISHED RESEARCH NOTE: CREATED")
print("PROFESSOR EMAIL: CREATED")
print("REVIEW QUESTIONS: CREATED")
print("BOUNDARY STATEMENT: CREATED")
print("STATUS: READY FOR PROFESSOR FEEDBACK AFTER POLISH")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
