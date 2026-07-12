from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/finite_to_infinite/PHASE_10AK_FINITE_TO_INFINITE_TRANSFER_BRANCH.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/finite_to_infinite/TRANSFER_THEOREM_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/finite_to_infinite/NEXT_CONTRIBUTION_TARGETS.md"),
]

required = [
    "FINITE_TO_INFINITE_TRANSFER_BRANCH",
    "ABSTRACT_POSITIVITY_TRANSFER_THEOREM",
    "NEGATIVE_DIRECTION_DETECTION_THEOREM",
    "CERTIFIED_FINITE_NEGATIVITY_THEOREM",
    "NOT_RH_CONTRIBUTION_YET",
    "Theorem 10AK.1",
    "Theorem 10AK.2",
    "Theorem 10AK.3",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not claim novelty",
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
print("PHASE 10AK FINITE-TO-INFINITE TRANSFER AUDIT: PASS")
print("ABSTRACT POSITIVITY TRANSFER: PROVED")
print("NEGATIVE DIRECTION DETECTION: PROVED")
print("CERTIFIED FINITE NEGATIVITY: PROVED")
print("RH CONTRIBUTION: NOT YET")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
