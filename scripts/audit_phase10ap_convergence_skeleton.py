from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/convergence_skeleton/PHASE_10AP_CONVERGENCE_THEOREM_SKELETON.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/convergence_skeleton/CONVERGENCE_TARGET_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/convergence_skeleton/NEXT_PHASE_10AQ_PLAN.md"),
]

required = [
    "CONVERGENCE_THEOREM_SKELETON",
    "POINTWISE_CONVERGENCE_TARGET",
    "QUANTITATIVE_CONVERGENCE_TARGET",
    "UNIFORM_CONVERGENCE_TARGET",
    "FORM_CONVERGENCE_TARGET",
    "OPERATOR_NORM_CONVERGENCE_TARGET",
    "TARGET_THEOREM_10AP_T",
    "CONVERGENCE_NOT_PROVEN",
    "NOT_RH_CONTRIBUTION_YET",
    "Theorem 10AP.1",
    "Theorem 10AP.2",
    "Theorem 10AP.3",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove convergence",
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
print("PHASE 10AP CONVERGENCE SKELETON AUDIT: PASS")
print("POINTWISE TARGET: RECORDED")
print("QUANTITATIVE TARGET: RECORDED")
print("UNIFORM TARGET: RECORDED")
print("FORM TARGET: RECORDED")
print("OPERATOR-NORM TARGET: RECORDED")
print("TARGET THEOREM 10AP-T: LOCKED")
print("CONVERGENCE: NOT PROVEN")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
