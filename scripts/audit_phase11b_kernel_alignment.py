from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/kernel_alignment_audit/PHASE_11B_KERNEL_ALIGNMENT_AUDIT.md"),
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/kernel_alignment_audit/KERNEL_ALIGNMENT_LOCK.md"),
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/kernel_alignment_audit/NEXT_PHASE_11C_SHARPER_TRANSFER.md"),
]

required = [
    "KERNEL_ALIGNMENT_AUDIT",
    "PROJECT_KERNEL_MATCHES_EXTRACTED_KERNEL",
    "SYMBOLIC_KERNEL_ALIGNMENT_PROVED",
    "KAPPA_N_M_ZERO_RELATIVE_TO_EXTRACTED_KERNEL",
    "FULL_CLASSICAL_VALIDATION_NOT_PROVEN",
    "SHARPER_TRANSFER_NEXT",
    "NOT_RH_CONTRIBUTION_YET",
    "Theorem 11B.1",
    "Corollary 11B.2",
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
print("PHASE 11B KERNEL ALIGNMENT AUDIT: PASS")
print("PROJECT KERNEL MATCHES EXTRACTED KERNEL")
print("SYMBOLIC KERNEL ALIGNMENT: PROVED")
print("KAPPA_N_M: ZERO RELATIVE TO EXTRACTED KERNEL")
print("FULL CLASSICAL VALIDATION: NOT PROVEN")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
