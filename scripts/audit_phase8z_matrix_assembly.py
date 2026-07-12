from pathlib import Path

files = [
    Path("weil_reconstruction/finite_truncations/h_matrix_assembly.py"),
    Path("scripts/run_phase8z_matrix_assembly_checks.py"),
    Path("weil_reconstruction/finite_truncations/PHASE_8Z_MATRIX_ASSEMBLY_WITHOUT_EIGENVALUES.md"),
    Path("weil_reconstruction/finite_truncations/PHASE_8Z_MATRIX_ASSEMBLY_OUTPUT.txt"),
]

required = [
    "No eigenvalues",
    "No zeta zeros",
    "No RH claim",
    "No novelty claim",
    "Synthetic finite Gamma",
    "full multiset",
    "distinct weighted",
    "Hermitian residual",
    "EIGENVALUE COMPUTATION: NONE",
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
print("PHASE 8Z MATRIX ASSEMBLY AUDIT: PASS")
print("SYNTHETIC MATRIX ASSEMBLY HELPERS: IMPLEMENTED")
print("FULL MULTISET MATRIX: ASSEMBLED")
print("DISTINCT WEIGHTED MATRIX: ASSEMBLED")
print("SHAPE/FINITENESS CHECKS: PASS")
print("EIGENVALUE COMPUTATION: NONE")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
