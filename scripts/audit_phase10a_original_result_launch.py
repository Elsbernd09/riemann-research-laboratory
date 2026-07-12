from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/PHASE_10A_ORIGINAL_RESULT_TARGET.md"),
    Path("original_results/finite_bombieri_stability/ORIGINALITY_DISCIPLINE.md"),
    Path("original_results/finite_bombieri_stability/LEVEL_2_LEVEL_3_PLAN.md"),
]

required = [
    "Original Result Target",
    "Finite Bombieri-Matrix Perturbation Stability",
    "Level 2",
    "Level 3",
    "professor-readable",
    "Hermitian",
    "operator-norm",
    "negative eigenvalues",
    "does not prove RH",
    "does not claim novelty",
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
print("PHASE 10A ORIGINAL RESULT BRANCH LAUNCH: PASS")
print("TARGET: FINITE BOMBIERI-MATRIX PERTURBATION STABILITY")
print("LEVEL 2 TARGET: PROFESSOR-READABLE RESEARCH NOTE")
print("LEVEL 3 ASPIRATION: EXPERT-INTEREST RESULT AFTER REVIEW")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
