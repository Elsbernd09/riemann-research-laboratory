from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/kernel_model_error/PHASE_11A_KERNEL_MODEL_ERROR_ATTACK.md"),
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/kernel_model_error/KERNEL_MODEL_ERROR_LOCK.md"),
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/kernel_model_error/NEXT_PHASE_11B_KERNEL_ALIGNMENT_AUDIT.md"),
]

required = [
    "KERNEL_MODEL_ERROR_ATTACK",
    "EXACT_KERNEL_ALIGNMENT_IMPLIES_ZERO_MODEL_ERROR",
    "UNIFORM_KERNEL_MISMATCH_BOUND",
    "WEIGHTED_KERNEL_MISMATCH_BOUND",
    "KAPPA_N_M_TARGET",
    "KERNEL_ALIGNMENT_NOT_YET_PROVEN",
    "NOT_RH_CONTRIBUTION_YET",
    "Theorem 11A.1",
    "Theorem 11A.2",
    "Theorem 11A.3",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove exact classical kernel alignment",
    "This phase does not establish novelty",
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
print("PHASE 11A KERNEL/MODEL ERROR ATTACK AUDIT: PASS")
print("EXACT ALIGNMENT THEOREM: PROVED CONDITIONALLY")
print("UNIFORM MISMATCH THEOREM: PROVED CONDITIONALLY")
print("WEIGHTED MISMATCH THEOREM: PROVED CONDITIONALLY")
print("KERNEL ALIGNMENT: NOT YET PROVEN")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
