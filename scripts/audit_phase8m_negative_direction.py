from pathlib import Path

files = [
    Path("weil_reconstruction/negative_directions/PHASE_8M_OFF_CRITICAL_NEGATIVE_DIRECTION_EXTRACTION.md"),
    Path("weil_reconstruction/negative_directions/NEGATIVE_DIRECTION_MECHANISM_CARD.md"),
    Path("weil_reconstruction/negative_directions/FINITE_TRUNCATION_LOCK_STATUS.md"),
]

required = [
    "Off-Critical Negative-Direction Extraction",
    "negative directions",
    "off-critical",
    "negative eigenvalues",
    "finite truncations",
    "basis-dependence",
    "FINITE_TRUNCATION_MODEL: UNLOCKED",
    "CLASSICAL_WEIL_MATRIX_IMPLEMENTATION_PERMISSION: DENIED",
    "No RH proof",
    "No new Weil criterion",
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
print("PHASE 8M OFF-CRITICAL NEGATIVE-DIRECTION AUDIT: PASS")
print("NEGATIVE-DIRECTION MECHANISM: RECORDED")
print("FINITE TRUNCATION STATUS: UNLOCKED")
print("CLASSICAL WEIL MATRIX IMPLEMENTATION: BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
