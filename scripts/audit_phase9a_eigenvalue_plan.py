from pathlib import Path

files = [
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9A_EIGENVALUE_VALIDATION_AUDIT_PLAN.md"),
    Path("weil_reconstruction/eigenvalue_validation/EIGENVALUE_VALIDATION_CHECKLIST.md"),
    Path("weil_reconstruction/eigenvalue_validation/EIGENVALUE_VALIDATION_BOUNDARY.md"),
]

required = [
    "Eigenvalue Validation Audit Plan",
    "This phase does not compute eigenvalues",
    "Synthetic finite multisets only",
    "Hermitian convention lock",
    "negative eigenvalue",
    "ZETA_ZERO_EXPERIMENTS: DENIED",
    "SYNTHETIC_EIGENVALUE_VALIDATION_NEXT_PHASE: ALLOWED",
    "No zeta zeros",
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
print("PHASE 9A EIGENVALUE VALIDATION AUDIT PLAN: PASS")
print("EIGENVALUE VALIDATION PLAN: CREATED")
print("SYNTHETIC-FIRST RULE: RECORDED")
print("HERMITION GATE: REQUIRED")
print("ZETA ZERO EXPERIMENTS: BLOCKED")
print("NEXT PHASE MAY VALIDATE SYNTHETIC EIGENVALUE COUNTS")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
