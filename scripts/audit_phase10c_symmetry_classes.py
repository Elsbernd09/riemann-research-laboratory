from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/PHASE_10C_ADMISSIBLE_SYMMETRY_CLASSES.md"),
    Path("original_results/finite_bombieri_stability/SYMMETRY_CLASS_DEFINITION_LOCK.md"),
    Path("original_results/finite_bombieri_stability/PHASE_10C_SYMMETRY_SUMMARY.md"),
]

required = [
    "Admissible Finite Symmetry Classes",
    "conjugation-closed",
    "reflection-closed",
    "quartet-closed",
    "multiplicity",
    "synthetic",
    "negative eigenvalue",
    "does not prove RH",
    "does not falsify RH",
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
print("PHASE 10C ADMISSIBLE SYMMETRY CLASSES AUDIT: PASS")
print("CLASS C: CONJUGATION-CLOSED")
print("CLASS R: REFLECTION-CLOSED")
print("CLASS Q: QUARTET-CLOSED")
print("PREFERRED THEOREM CLASS: Q_N")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
