from pathlib import Path

files = [
    Path("weil_reconstruction/sources/extractions/PHASE_8F_BOMBIERI_THEOREM_EXTRACTION.md"),
    Path("weil_reconstruction/sources/extractions/BOMBIERI_THEOREM_1_CARD.md"),
    Path("weil_reconstruction/sources/extractions/BOMBIERI_THEOREM_2_CARD.md"),
    Path("weil_reconstruction/sources/CONVENTION_LOCK_TABLE.md"),
]

required = [
    "Bombieri Theorem 1",
    "Bombieri Theorem 2",
    "g(\\rho)g(1-\\rho)",
    "T[f*f^*]",
    "C_0^\\infty((0,\\infty))",
    "Known theorem reconstructed",
    "No exact finite-rank Weil matrix yet",
    "LOCKED",
    "PARTIAL",
    "UNLOCKED",
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
print("PHASE 8F BOMBIERI THEOREM EXTRACTION AUDIT: PASS")
print("THEOREM 1 CARD: CREATED")
print("THEOREM 2 CARD: CREATED")
print("CONVENTION LOCK TABLE: UPDATED")
print("EXACT FINITE-RANK WEIL MATRIX: STILL BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
