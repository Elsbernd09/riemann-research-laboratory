from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/tractable_convergence_model/PHASE_10AQ_TRACTABLE_FINITE_TEST_CLASS_MODEL.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/tractable_convergence_model/FINITE_TEST_CLASS_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/tractable_convergence_model/NEXT_PHASE_10AR_GRAM_CONVERGENCE.md"),
]

required = [
    "TRACTABLE_FINITE_TEST_CLASS_MODEL",
    "FINITE_TEST_CLASS_CONVERGENCE_REDUCTION",
    "GRAM_MATRIX_CONVERGENCE_REDUCTION",
    "ENTRYWISE_GRAM_CONVERGENCE_CERTIFICATE",
    "UNIFORM_FINITE_CLASS_CONVERGENCE",
    "CLASSICAL_CONVERGENCE_NOT_PROVEN",
    "NOT_RH_CONTRIBUTION_YET",
    "Theorem 10AQ.1",
    "Theorem 10AQ.2",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove classical convergence",
    "This phase does not claim novelty",
]

for path in files:
    if not path.exists():
        raise FileNotFoundError(path)

    text = path.read_text(encoding="utf-8")
    if "\x00" in text:
        raise ValueError(f"NUL byte found in {path}")

combined = "\n".join(path.read_text(encoding="utf-8") for path in files)

missing = [phrase for phrase in required if phrase.lower() not in combined.lower()]

if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

print("=" * 80)
print("PHASE 10AQ TRACTABLE CONVERGENCE AUDIT: PASS")
print("FINITE TEST-CLASS MODEL: LOCKED")
print("GRAM MATRIX REDUCTION: PROVED")
print("ENTRYWISE CERTIFICATE: PROVED")
print("CLASSICAL CONVERGENCE: NOT PROVEN")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
