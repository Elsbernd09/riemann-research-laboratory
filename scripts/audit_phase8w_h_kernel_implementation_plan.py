from pathlib import Path

files = [
    Path("weil_reconstruction/finite_truncations/PHASE_8W_H_KERNEL_IMPLEMENTATION_AUDIT_PLAN.md"),
    Path("weil_reconstruction/finite_truncations/H_KERNEL_IMPLEMENTATION_AUDIT_CHECKLIST.md"),
    Path("weil_reconstruction/finite_truncations/H_KERNEL_IMPLEMENTATION_BOUNDARY.md"),
]

required = [
    "H-Kernel Implementation Audit Plan",
    "does not implement the matrix",
    "does not compute eigenvalues",
    "K(z)=\\sin z/z",
    "K^*(x,y;t)",
    "H(x,y;t)",
    "Synthetic finite multisets first",
    "H_KERNEL_SYMBOLIC_IMPLEMENTATION_NEXT_PHASE: ALLOWED",
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
print("PHASE 8W H-KERNEL IMPLEMENTATION AUDIT PLAN: PASS")
print("IMPLEMENTATION PLAN: CREATED")
print("SANITY CHECKLIST: CREATED")
print("BOUNDARY FILE: CREATED")
print("NEXT PHASE MAY IMPLEMENT SYMBOLIC H-KERNEL FUNCTIONS")
print("EIGENVALUE COMPUTATION: STILL BLOCKED")
print("ZETA ZERO EXPERIMENTS: BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
