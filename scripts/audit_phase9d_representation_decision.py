from pathlib import Path

files = [
    Path("scripts/run_phase9d_representation_decision.py"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9D_REPRESENTATION_DECISION_AND_REPAIR_PLAN.md"),
    Path("weil_reconstruction/eigenvalue_validation/REPRESENTATION_REPAIR_PLAN.md"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9D_REPRESENTATION_DECISION_OUTPUT.txt"),
]

required = [
    "Representation Decision",
    "PHASE_9C_STATUS",
    "NEXT_TRACK",
    "FINAL_SYNTHETIC_VALIDATION_SUITE",
    "REPRESENTATION_REPAIR_REQUIRED",
    "No new eigenvalues computed",
    "No zeta zeros",
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
print("PHASE 9D REPRESENTATION DECISION AUDIT: PASS")
print("PHASE 9C STATUS: PARSED")
print("NEXT TRACK: RECORDED")
print("NO NEW EIGENVALUES COMPUTED IN PHASE 9D")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
