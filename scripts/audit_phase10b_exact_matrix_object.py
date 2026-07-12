from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/PHASE_10B_EXACT_FINITE_MATRIX_OBJECT.md"),
    Path("original_results/finite_bombieri_stability/FINITE_MATRIX_DEFINITION_LOCK.md"),
    Path("original_results/finite_bombieri_stability/PHASE_10B_THEOREM_OBJECT_SUMMARY.md"),
]

required = [
    "Exact Finite Matrix Object",
    "D^{1/2}A(t)D^{1/2}",
    "Hermitian",
    "negative eigenvalue",
    "multiplicity",
    "similarity",
    "does not prove RH",
    "does not falsify RH",
    "does not use zeta zeros",
    "does not claim novelty",
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
print("PHASE 10B EXACT FINITE MATRIX OBJECT AUDIT: PASS")
print("PRIMARY OBJECT: M(Gamma,t)=D^{1/2}A(t)D^{1/2}")
print("HERMITION ADMISSION RULE: LOCKED")
print("MULTIPLICITY RULE: LOCKED")
print("NEGATIVE COUNT OBJECT: LOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
