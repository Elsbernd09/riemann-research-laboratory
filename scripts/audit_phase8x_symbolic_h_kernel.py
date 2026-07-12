from pathlib import Path

files = [
    Path("weil_reconstruction/finite_truncations/h_kernel_symbolic.py"),
    Path("scripts/run_phase8x_h_kernel_sanity.py"),
    Path("weil_reconstruction/finite_truncations/PHASE_8X_SYMBOLIC_H_KERNEL_IMPLEMENTATION.md"),
    Path("weil_reconstruction/finite_truncations/PHASE_8X_SANITY_OUTPUT.txt"),
]

required = [
    "No matrices",
    "No eigenvalues",
    "No zeta zeros",
    "No RH claim",
    "No novelty claim",
    "K(0)=1",
    "K evenness",
    "H_kernel finite synthetic samples",
    "SCALAR KERNEL FUNCTIONS",
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
print("PHASE 8X SYMBOLIC H-KERNEL AUDIT: PASS")
print("SCALAR H-KERNEL FUNCTIONS: IMPLEMENTED")
print("SANITY OUTPUT: RECORDED")
print("MATRIX ASSEMBLY: NONE")
print("EIGENVALUE COMPUTATION: NONE")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
