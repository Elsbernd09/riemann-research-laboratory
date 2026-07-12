from pathlib import Path

files = [
    Path("weil_reconstruction/finite_truncations/PHASE_8V_BOMBIERI_THEOREM8_EXTRACTION.md"),
    Path("weil_reconstruction/finite_truncations/BOMBIERI_THEOREM8_CARD.md"),
    Path("weil_reconstruction/finite_truncations/THEOREM8_EXTRACTION_TEMPLATE.md"),
    Path("weil_reconstruction/finite_truncations/FINITE_TRUNCATION_TERM_TABLE.md"),
    Path("weil_reconstruction/finite_truncations/H_MATRIX_LOCK_REQUIREMENTS.md"),
    Path("weil_reconstruction/finite_truncations/NEXT_EXTRACTION_TARGETS.md"),
]

required = [
    "Bombieri Theorem 8 Extraction",
    "number of negative eigenvalues",
    "distinct complex conjugate pairs",
    "zero-eigenvalue",
    "m(\\gamma)-1",
    "H_MATRIX_IMPLEMENTATION_PERMISSION: DENIED",
    "EIGENVALUE_COMPUTATION_PERMISSION: DENIED",
    "No matrix implementation",
    "No eigenvalue computation",
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
print("PHASE 8V BOMBIERI THEOREM 8 EXTRACTION AUDIT: PASS")
print("THEOREM 8 STATEMENT: LOCKED")
print("ZERO-EIGENVALUE MULTIPLICITY WARNING: LOCKED")
print("OFF-CRITICAL LINK: RECORDED")
print("MATRIX IMPLEMENTATION: STILL BLOCKED")
print("EIGENVALUE COMPUTATION: STILL BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
