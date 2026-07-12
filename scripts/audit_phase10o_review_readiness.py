from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/review_readiness/PHASE_10O_PRIOR_ART_EXPERT_REVIEW_READINESS.md"),
    Path("original_results/finite_bombieri_stability/review_readiness/PRIOR_ART_CHECKLIST.md"),
    Path("original_results/finite_bombieri_stability/review_readiness/EXPERT_REVIEW_EMAIL_DRAFT.md"),
    Path("original_results/finite_bombieri_stability/review_readiness/ADMISSIONS_FRAMING_LOCK.md"),
]

required = [
    "Prior-Art",
    "CORRECTNESS_REVIEW_READY",
    "NOVELTY_NOT_ESTABLISHED",
    "READY_FOR_EXPERT_FEEDBACK",
    "Weyl",
    "Davis-Kahan",
    "Bauer-Fike",
    "kernel matrix",
    "Expert Review Email",
    "Admissions Framing",
    "This audit does not prove RH",
    "This audit does not falsify RH",
    "This audit does not use zeta zeros",
    "This audit does not claim novelty",
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
print("PHASE 10O PRIOR-ART / EXPERT REVIEW READINESS AUDIT: PASS")
print("CORRECTNESS REVIEW: READY")
print("NOVELTY: NOT ESTABLISHED")
print("EXPERT FEEDBACK: READY")
print("ADMISSIONS FRAMING: LOCKED HONESTLY")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
