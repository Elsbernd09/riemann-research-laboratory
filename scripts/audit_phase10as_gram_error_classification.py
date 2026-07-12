from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/gram_error_classification/PHASE_10AS_GRAM_ERROR_CLASSIFICATION.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/gram_error_classification/ERROR_CLASSIFICATION_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/gram_error_classification/NEXT_PHASE_10AT_CONDITIONAL_TRANSFER.md"),
]

required = [
    "GRAM_ERROR_CLASSIFICATION",
    "TRUNCATION_ERROR_CLASSICAL_SOURCE_DEPENDENT",
    "PROJECTION_ERROR_CLASSICAL_OR_PROJECT_DEPENDENT",
    "KERNEL_MODEL_ERROR_REQUIRES_CLASSICAL_VALIDATION",
    "COMPUTATIONAL_ERROR_PROJECT_CONTROLLABLE",
    "CERTIFIED_NUMERICS_POSSIBLE",
    "CONDITIONAL_TRANSFER_THEOREM_NEXT",
    "NOT_RH_CONTRIBUTION_YET",
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
print("PHASE 10AS GRAM ERROR CLASSIFICATION AUDIT: PASS")
print("TRUNCATION ERROR: CLASSICAL-SOURCE DEPENDENT")
print("PROJECTION ERROR: CLASSICAL OR PROJECT DEPENDENT")
print("KERNEL/MODEL ERROR: REQUIRES CLASSICAL VALIDATION")
print("COMPUTATIONAL ERROR: PROJECT-CONTROLLABLE")
print("NEXT TARGET: CONDITIONAL TRANSFER THEOREM")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
