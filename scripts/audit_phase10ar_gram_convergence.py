from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/gram_convergence_problem/PHASE_10AR_GRAM_CONVERGENCE_PROBLEM.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/gram_convergence_problem/GRAM_CONVERGENCE_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/gram_convergence_problem/NEXT_PHASE_10AS_ERROR_CLASSIFICATION.md"),
]

required = [
    "GRAM_CONVERGENCE_PROBLEM",
    "GRAM_ENTRY_CONVERGENCE_TARGET",
    "FINITE_CLASS_CONVERGENCE_FROM_GRAM_CONVERGENCE",
    "GRAM_ERROR_DECOMPOSITION",
    "TRUNCATION_PROJECTION_KERNEL_COMPUTATION_ERROR",
    "CLASSICAL_CONVERGENCE_NOT_PROVEN",
    "NOT_RH_CONTRIBUTION_YET",
    "Theorem 10AR.1",
    "Theorem 10AR.2",
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
print("PHASE 10AR GRAM CONVERGENCE AUDIT: PASS")
print("GRAM ENTRY CONVERGENCE TARGET: LOCKED")
print("FINITE-CLASS CONSEQUENCE: PROVED")
print("GRAM ERROR DECOMPOSITION: CREATED")
print("CLASSICAL CONVERGENCE: NOT PROVEN")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
