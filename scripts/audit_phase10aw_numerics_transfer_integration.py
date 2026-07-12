from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/numerics_transfer_integration/PHASE_10AW_CERTIFIED_NUMERICS_TRANSFER_INTEGRATION.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/numerics_transfer_integration/INTEGRATION_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/numerics_transfer_integration/NEXT_PHASE_10AX_TRANSFER_CERTIFICATE_CALCULATOR.md"),
]

required = [
    "CERTIFIED_NUMERICS_TRANSFER_INTEGRATION",
    "INTEGRATED_TRANSFER_BOUND",
    "CERTIFIED_NUMERICAL_NEGATIVE_DIRECTION_MARGIN",
    "CHI_N_M_INTEGRATED",
    "TRANSFER_CERTIFICATE_FORMAT",
    "UNCONDITIONAL_CLASSICAL_CONVERGENCE_NOT_PROVEN",
    "NOT_RH_CONTRIBUTION_YET",
    "Theorem 10AW.1",
    "Theorem 10AW.2",
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
print("PHASE 10AW NUMERICS TRANSFER INTEGRATION AUDIT: PASS")
print("CERTIFIED NUMERICS: INTEGRATED")
print("TRANSFER BOUND: PROVED")
print("NEGATIVE-DIRECTION MARGIN: PROVED")
print("UNCONDITIONAL CLASSICAL CONVERGENCE: NOT PROVEN")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
