from pathlib import Path

files = [
    Path("weil_reconstruction/symbolic/PHASE_8J_COMPLEX_STAR_CONVENTION_AUDIT.md"),
    Path("weil_reconstruction/symbolic/STAR_CONVENTION_STATUS.md"),
    Path("weil_reconstruction/symbolic/COMPLEX_STAR_EXTRACTION_TODO.md"),
]

required = [
    "Complex Star Convention Audit",
    "f^*(x)=x^{-1}f(1/x)",
    "f^\\dagger",
    "complex conjugation",
    "Hermitian positivity",
    "UNLOCKED",
    "FINITE-RANK WEIL MATRICES: BLOCKED",
    "Do not implement positivity code yet",
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
print("PHASE 8J COMPLEX STAR CONVENTION AUDIT: PASS")
print("ALGEBRAIC STAR: DISTINGUISHED")
print("HERMITIAN ADJOINT CANDIDATE: RECORDED")
print("COMPLEX CONJUGATION CONVENTION: STILL UNLOCKED")
print("FINITE-RANK WEIL MATRICES: BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
