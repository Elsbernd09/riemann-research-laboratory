from pathlib import Path

files = [
    Path("weil_reconstruction/finite_truncations/PHASE_8S_SECTION8_FINITE_APPROXIMATION_SKELETON.md"),
    Path("weil_reconstruction/finite_truncations/SECTION8_OBJECT_CARD.md"),
    Path("weil_reconstruction/finite_truncations/FINITE_TRUNCATION_TERM_TABLE.md"),
    Path("weil_reconstruction/finite_truncations/NEXT_EXTRACTION_TARGETS.md"),
]

required = [
    "Section 8 Finite Approximation Skeleton",
    "finite multiset",
    "rho=\\frac12+i\\gamma",
    "\\Phi(x)",
    "V^\\circ",
    "F(-t)=F(t)=0",
    "L[F](x)",
    "H(\\gamma,\\gamma';t)",
    "Do not implement matrices yet",
    "No RH proof",
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
print("PHASE 8S SECTION 8 SKELETON AUDIT: PASS")
print("FINITE MULTISET Z: LOCKED")
print("FINITE SPACE V: LOCKED")
print("BOUNDARY SUBSPACE V^circ: LOCKED")
print("SECTION 8 LINEAR OBJECT L[F]: LOCKED")
print("MATRIX ENTRIES: STILL UNLOCKED")
print("EIGENVALUE COMPUTATION: BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
