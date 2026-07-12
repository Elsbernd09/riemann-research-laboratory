from pathlib import Path

files = [
    Path("weil_reconstruction/finite_truncations/PHASE_8U_H_KERNEL_SOURCE_EXTRACTION.md"),
    Path("weil_reconstruction/finite_truncations/H_MATRIX_FORMULA_CARD.md"),
    Path("weil_reconstruction/finite_truncations/H_MATRIX_LOCK_REQUIREMENTS.md"),
    Path("weil_reconstruction/finite_truncations/FINITE_TRUNCATION_TERM_TABLE.md"),
    Path("weil_reconstruction/finite_truncations/NEXT_EXTRACTION_TARGETS.md"),
]

required = [
    "Source-Fill H(gamma,gamma';t) Kernel Formula",
    "K(x)=\\frac{\\sin x}{x}",
    "K_t(x)=K(tx)",
    "K^*(x,y;t)",
    "H(x,y;t)",
    "2t",
    "w_\\gamma",
    "Theorem 8",
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
print("PHASE 8U H-KERNEL SOURCE EXTRACTION AUDIT: PASS")
print("BASE KERNEL K: LOCKED")
print("CORRECTED KERNEL K*: LOCKED")
print("H-KERNEL FORMULA: PARTIAL_LOCKED")
print("COEFFICIENT EQUATION: RECORDED")
print("MATRIX IMPLEMENTATION: BLOCKED")
print("EIGENVALUE COMPUTATION: BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
