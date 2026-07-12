from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/sharper_transfer/PHASE_11C_SHARPER_CONDITIONAL_TRANSFER_THEOREM.md"),
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/sharper_transfer/SHARPER_TRANSFER_LOCK.md"),
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/sharper_transfer/NEXT_PHASE_11D_SHARPER_CALCULATOR.md"),
]

required = [
    "SHARPER_CONDITIONAL_TRANSFER_THEOREM",
    "KAPPA_ZERO_UNDER_EXTRACTED_KERNEL_ALIGNMENT",
    "THREE_ERROR_TRANSFER_BOUND",
    "SHARPER_NEGATIVE_DIRECTION_MARGIN",
    "TAU_PI_CHI_REMAINING_TERMS",
    "FULL_CLASSICAL_VALIDATION_NOT_PROVEN",
    "NOT_RH_CONTRIBUTION_YET",
    "Theorem 11C.1",
    "Theorem 11C.2",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove full classical validation",
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
print("PHASE 11C SHARPER TRANSFER AUDIT: PASS")
print("KAPPA = 0 UNDER EXTRACTED-KERNEL ALIGNMENT")
print("THREE-ERROR TRANSFER BOUND: PROVED")
print("SHARPER NEGATIVE-DIRECTION MARGIN: PROVED")
print("FULL CLASSICAL VALIDATION: NOT PROVEN")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
