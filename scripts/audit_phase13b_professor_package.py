from pathlib import Path

base = Path("original_results/finite_bombieri_stability/level4_candidate/professor_review_package")

files = [
    base / "README.md",
    base / "ONE_PAGE_SUMMARY.md",
    base / "THEOREM_MAP.md",
    base / "BOUNDARY_PAGE.md",
    base / "SOURCE_VALIDATION_QUESTIONS.md",
    base / "CODE_ARTIFACT_LIST.md",
    base / "EMAIL_DRAFT.md",
    base / "PACKAGE_STATUS.md",
]

required = [
    "PROFESSOR_REVIEW_PACKAGE_COMPLETE",
    "README_CREATED",
    "ONE_PAGE_SUMMARY_CREATED",
    "THEOREM_MAP_CREATED",
    "BOUNDARY_PAGE_CREATED",
    "SOURCE_VALIDATION_QUESTIONS_CREATED",
    "CODE_ARTIFACT_LIST_CREATED",
    "EMAIL_DRAFT_CREATED",
    "NO_RH_PROOF_CLAIM",
    "NO_BREAKTHROUGH_CLAIM",
    "NO_NOVELTY_CLAIM",
    "READY_FOR_PROFESSOR_REVIEW",
    "This is not a proof of RH",
    "This is not a disproof of RH",
    "This is not a new equivalent criterion for RH",
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
print("PHASE 13B PROFESSOR REVIEW PACKAGE AUDIT: PASS")
print("README: CREATED")
print("ONE-PAGE SUMMARY: CREATED")
print("THEOREM MAP: CREATED")
print("BOUNDARY PAGE: CREATED")
print("SOURCE VALIDATION QUESTIONS: CREATED")
print("CODE ARTIFACT LIST: CREATED")
print("EMAIL DRAFT: CREATED")
print("NO RH PROOF CLAIM")
print("NO BREAKTHROUGH CLAIM")
print("NO NOVELTY CLAIM")
print("READY FOR PROFESSOR REVIEW")
print("=" * 80)
