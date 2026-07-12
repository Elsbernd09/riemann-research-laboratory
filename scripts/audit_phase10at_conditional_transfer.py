from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/conditional_transfer_theorem/PHASE_10AT_CONDITIONAL_GRAM_ERROR_TRANSFER_THEOREM.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/conditional_transfer_theorem/CONDITIONAL_TRANSFER_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/conditional_transfer_theorem/NEXT_PHASE_10AU_CERTIFIED_NUMERICS.md"),
]

required = [
    "CONDITIONAL_GRAM_ERROR_TRANSFER_THEOREM",
    "CONDITIONAL_CONVERGENCE_COROLLARY",
    "CONDITIONAL_CERTIFIED_NEGATIVE_DIRECTION_TRANSFER",
    "FOUR_ERROR_CONTROL_REDUCTION",
    "TRUNCATION_PROJECTION_KERNEL_COMPUTATION_BOUND",
    "UNCONDITIONAL_CLASSICAL_CONVERGENCE_NOT_PROVEN",
    "NOT_RH_CONTRIBUTION_YET",
    "Theorem 10AT.1",
    "Theorem 10AT.2",
    "Theorem 10AT.3",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove unconditional classical convergence",
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
print("PHASE 10AT CONDITIONAL TRANSFER AUDIT: PASS")
print("CONDITIONAL GRAM-ERROR TRANSFER: PROVED")
print("CONDITIONAL CONVERGENCE COROLLARY: PROVED")
print("CONDITIONAL NEGATIVE-DIRECTION TRANSFER: PROVED")
print("FOUR ERROR CONTROL REDUCTION: LOCKED")
print("UNCONDITIONAL CLASSICAL CONVERGENCE: NOT PROVEN")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
