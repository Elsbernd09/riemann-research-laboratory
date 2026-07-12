from pathlib import Path

files = [
    Path("weil_reconstruction/finite_truncations/PHASE_8T_H_MATRIX_EXTRACTION_WORKSHEET.md"),
    Path("weil_reconstruction/finite_truncations/H_MATRIX_LOCK_REQUIREMENTS.md"),
    Path("weil_reconstruction/finite_truncations/THEOREM8_EXTRACTION_TEMPLATE.md"),
]

required = [
    "H-Matrix Entry Extraction Worksheet",
    "H(\\gamma,\\gamma';t)",
    "Theorem 8",
    "Exact source formula",
    "Boundary-condition effect",
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
print("PHASE 8T H-MATRIX WORKSHEET AUDIT: PASS")
print("H-MATRIX EXTRACTION WORKSHEET: CREATED")
print("THEOREM 8 TEMPLATE: CREATED")
print("H-MATRIX IMPLEMENTATION: BLOCKED")
print("EIGENVALUE COMPUTATION: BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
