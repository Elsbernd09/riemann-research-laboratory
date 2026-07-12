from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/bombieri_weil_template/PHASE_10AL_BOMBIIERI_WEIL_SPECIALIZATION_TEMPLATE.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/bombieri_weil_template/SPECIALIZATION_TEMPLATE_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/bombieri_weil_template/NEXT_MISSING_OBJECTS.md"),
]

required = [
    "BOMBIIERI_WEIL_SPECIALIZATION_TEMPLATE",
    "WEIL_FORM_TRANSFER_TEMPLATE",
    "NEGATIVE_DIRECTION_DETECTION_TEMPLATE",
    "CERTIFIED_BOMBIIERI_WEIL_NEGATIVITY_TEMPLATE",
    "CONVERGENCE_THEOREM_MISSING",
    "NOT_RH_CONTRIBUTION_YET",
    "Theorem 10AL.1",
    "Theorem 10AL.2",
    "Theorem 10AL.3",
    "Q_N(P_Nf)\\to Q_W(f)",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
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
print("PHASE 10AL BOMBIIERI/WEIL TEMPLATE AUDIT: PASS")
print("WEIL FORM TRANSFER TEMPLATE: LOCKED")
print("NEGATIVE DIRECTION DETECTION TEMPLATE: LOCKED")
print("CERTIFIED FINITE NEGATIVITY TEMPLATE: LOCKED")
print("CONVERGENCE THEOREM: MISSING")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
