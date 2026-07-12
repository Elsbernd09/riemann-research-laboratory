from pathlib import Path

files = [
    Path("weil_reconstruction/finite_truncations/PHASE_8N_FINITE_TRUNCATION_EXTRACTION_WORKSHEET.md"),
    Path("weil_reconstruction/finite_truncations/FINITE_TRUNCATION_TERM_TABLE.md"),
    Path("weil_reconstruction/finite_truncations/FINITE_TRUNCATION_DANGER_NOTE.md"),
]

required = [
    "Finite Truncation Extraction Worksheet",
    "does not implement a matrix",
    "does not compute eigenvalues",
    "Matrix entries",
    "negative eigenvalues",
    "off-critical zeros",
    "CLASSICAL_WEIL_MATRIX_IMPLEMENTATION_PERMISSION: DENIED",
    "EIGENVALUE_COMPUTATION_PERMISSION: DENIED",
    "source-derived Bombieri-Weil truncation",
    "No matrix code should be written",
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
print("PHASE 8N FINITE TRUNCATION WORKSHEET AUDIT: PASS")
print("FINITE TRUNCATION EXTRACTION WORKSHEET: CREATED")
print("TERM TABLE: CREATED")
print("DANGER NOTE: CREATED")
print("CLASSICAL WEIL MATRIX IMPLEMENTATION: BLOCKED")
print("EIGENVALUE COMPUTATION: BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
