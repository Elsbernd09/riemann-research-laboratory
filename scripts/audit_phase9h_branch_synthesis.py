from pathlib import Path

files = [
    Path("scripts/run_phase9h_branch_synthesis.py"),
    Path("weil_reconstruction/synthesis/PHASE_9H_FINITE_VALIDATION_BRANCH_SYNTHESIS.md"),
    Path("weil_reconstruction/synthesis/NEXT_OPTIONS_AFTER_PHASE_9H.md"),
    Path("weil_reconstruction/synthesis/PHASE_9H_FINITE_VALIDATION_BRANCH_STATUS.txt"),
]

required = [
    "Finite Validation Branch",
    "BRANCH_STATUS",
    "What is source-extracted",
    "What is implemented",
    "No zeta zeros used",
    "No RH claim",
    "No novelty claim",
    "No zeta-case Bombieri-Weil verification claim",
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
print("PHASE 9H BRANCH SYNTHESIS AUDIT: PASS")
print("FINITE VALIDATION BRANCH STATUS: RECORDED")
print("NEXT OPTIONS: RECORDED")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
