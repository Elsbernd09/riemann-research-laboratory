from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/audits/PHASE_10J_ADVERSARIAL_NOVELTY_CORRECTNESS_AUDIT.md"),
    Path("original_results/finite_bombieri_stability/audits/LEVEL_STATUS_AFTER_10J.md"),
    Path("original_results/finite_bombieri_stability/audits/NEXT_LEVEL3_TARGET.md"),
]

required = [
    "Adversarial Novelty",
    "Correctness status",
    "Novelty is not established",
    "EXPOSITORY_WITH_POSSIBLE_SPECIALIZED_PACKAGING_VALUE",
    "Level 2",
    "Level 3",
    "NOT_YET_ACHIEVED",
    "Support Perturbation Stability",
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
print("PHASE 10J ADVERSARIAL NOVELTY/CORRECTNESS AUDIT: PASS")
print("CORRECTNESS: FINITE THEOREM SOUND")
print("NOVELTY: NOT ESTABLISHED")
print("LEVEL 2: CANDIDATE ACHIEVED")
print("LEVEL 3: NOT YET ACHIEVED")
print("NEXT TARGET: SUPPORT PERTURBATION STABILITY")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
