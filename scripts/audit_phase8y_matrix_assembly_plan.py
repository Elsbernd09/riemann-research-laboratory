from pathlib import Path

files = [
    Path("weil_reconstruction/finite_truncations/PHASE_8Y_MATRIX_ASSEMBLY_AUDIT_PLAN.md"),
    Path("weil_reconstruction/finite_truncations/MATRIX_ASSEMBLY_CHECKLIST.md"),
    Path("weil_reconstruction/finite_truncations/MATRIX_ASSEMBLY_BOUNDARY.md"),
]

required = [
    "Matrix Assembly Audit Plan",
    "does not assemble matrices",
    "does not compute eigenvalues",
    "full multiset representation",
    "Distinct weighted representation",
    "Synthetic test cases",
    "MATRIX_ASSEMBLY_NEXT_PHASE: ALLOWED",
    "EIGENVALUE_COMPUTATION: DENIED",
    "ZETA_ZERO_EXPERIMENTS: DENIED",
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
print("PHASE 8Y MATRIX ASSEMBLY AUDIT PLAN: PASS")
print("MATRIX ASSEMBLY PLAN: CREATED")
print("FULL MULTISET REPRESENTATION: SPECIFIED")
print("DISTINCT WEIGHTED REPRESENTATION: SPECIFIED")
print("NEXT PHASE MAY ASSEMBLE MATRICES WITHOUT EIGENVALUES")
print("EIGENVALUE COMPUTATION: BLOCKED")
print("ZETA ZERO EXPERIMENTS: BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
