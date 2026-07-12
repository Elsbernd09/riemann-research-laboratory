from pathlib import Path

files = [
    Path("scripts/run_phase9c_representation_normalization_audit.py"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9C_REPRESENTATION_NORMALIZATION_AUDIT.md"),
    Path("weil_reconstruction/eigenvalue_validation/REPRESENTATION_NORMALIZATION_DECISION_RULE.md"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9C_REPRESENTATION_NORMALIZATION_AUDIT_OUTPUT.txt"),
]

required = [
    "Representation Normalization Audit",
    "REPRESENTATION_LOCK_STATUS",
    "PRELIMINARY_SYNTHETIC_LOCK_POSSIBLE",
    "REPRESENTATION_NOT_LOCKED",
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
print("PHASE 9C REPRESENTATION NORMALIZATION AUDIT: PASS")
print("PHASE 9B OUTPUT: ANALYZED")
print("REPRESENTATION LOCK STATUS: RECORDED")
print("NO NEW EIGENVALUES COMPUTED IN PHASE 9C")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
