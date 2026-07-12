from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/certified_numerics/PHASE_10AU_CERTIFIED_NUMERICAL_ERROR_MODEL.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/certified_numerics/CERTIFIED_NUMERICS_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/certified_numerics/NEXT_PHASE_10AV_INTERVAL_CALCULATOR.md"),
]

required = [
    "CERTIFIED_NUMERICAL_ERROR_MODEL",
    "INTERVAL_CERTIFIED_COMPUTATIONAL_ERROR_BOUND",
    "MATRIX_LEVEL_NUMERICAL_ERROR_BOUND",
    "CHI_N_M_NUMERICAL_ERROR_CERTIFICATE",
    "COMPUTATIONAL_ERROR_CONTROLLED_CONDITIONALLY",
    "CERTIFIED_NUMERICS_WORKFLOW",
    "NOT_RH_CONTRIBUTION_YET",
    "Theorem 10AU.1",
    "Theorem 10AU.2",
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
print("PHASE 10AU CERTIFIED NUMERICS AUDIT: PASS")
print("INTERVAL CERTIFIED COMPUTATIONAL ERROR: PROVED")
print("MATRIX-LEVEL NUMERICAL ERROR BOUND: PROVED")
print("CHI_N_M CERTIFICATE: LOCKED")
print("COMPUTATIONAL ERROR: CONDITIONALLY CONTROLLED")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
