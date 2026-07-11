from pathlib import Path

files = [
    Path("weil_reconstruction/symbolic/PHASE_8K_SOURCE_LOCK_COMPLEX_STAR.md"),
    Path("weil_reconstruction/symbolic/STAR_CONVENTION_STATUS.md"),
    Path("weil_reconstruction/sources/extractions/BOMBIERI_COMPLEX_STAR_CARD.md"),
]

required = [
    "Source-Lock Complex Star Convention",
    "transpose conjugate",
    "g^*_{\\mathrm{pos}}",
    "overline",
    "|g(\\rho)|^2",
    "LOCKED for Bombieri positivity mechanism",
    "FINITE-RANK WEIL MATRICES: BLOCKED",
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
print("PHASE 8K SOURCE-LOCK STAR CONVENTION AUDIT: PASS")
print("ALGEBRAIC STAR: LOCKED")
print("POSITIVITY STAR: LOCKED")
print("HERMITIAN POSITIVITY MECHANISM: RECORDED")
print("FINITE-RANK WEIL MATRICES: STILL BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
