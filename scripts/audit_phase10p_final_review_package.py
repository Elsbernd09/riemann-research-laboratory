from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/final_review_package/README_FOR_PROFESSOR_REVIEW.md"),
    Path("original_results/finite_bombieri_stability/final_review_package/FINAL_RESEARCH_NOTE_DRAFT.md"),
    Path("original_results/finite_bombieri_stability/final_review_package/EXPERT_REVIEW_EMAIL.md"),
    Path("original_results/finite_bombieri_stability/final_review_package/PRIOR_ART_CHECKLIST.md"),
    Path("original_results/finite_bombieri_stability/final_review_package/BOUNDARY_AND_FRAMING_STATEMENT.md"),
    Path("original_results/finite_bombieri_stability/final_review_package/REVIEW_QUESTIONS.md"),
    Path("original_results/finite_bombieri_stability/final_review_package/PACKAGE_STATUS.md"),
]

required = [
    "Professor Review Package",
    "FINAL_RESEARCH_NOTE_DRAFT",
    "2Nm_{\\max}L_t(U)\\delta<g_0(M",
    "CORRECTNESS_REVIEW_READY",
    "NOVELTY_NOT_ESTABLISHED",
    "READY_FOR_EXPERT_FEEDBACK",
    "No RH proof",
    "No RH falsification",
    "No zeta zeros",
    "No novelty claim",
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
print("PHASE 10P FINAL PROFESSOR REVIEW PACKAGE AUDIT: PASS")
print("FINAL REVIEW PACKAGE: CREATED")
print("CORRECTNESS REVIEW: READY")
print("NOVELTY: NOT ESTABLISHED")
print("EXPERT FEEDBACK: READY")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
