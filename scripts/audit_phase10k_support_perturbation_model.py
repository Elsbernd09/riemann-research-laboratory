from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/support_perturbation/PHASE_10K_SUPPORT_PERTURBATION_MODEL.md"),
    Path("original_results/finite_bombieri_stability/support_perturbation/SUPPORT_PERTURBATION_DEFINITION_LOCK.md"),
    Path("original_results/finite_bombieri_stability/support_perturbation/PHASE_10K_LEVEL3_RATIONALE.md"),
]

required = [
    "Support-Perturbation Model",
    "Lipschitz",
    "2L_t(U)\\delta",
    "2m_{\\max}L_t(U)\\delta",
    "2Nm_{\\max}L_t(U)\\delta<g_0(M)",
    "SUPPORT_PERTURBATION_STABILITY_THEOREM",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not use zeta zeros",
    "This phase does not claim novelty",
]

for path in files:
    if not path.exists():
        raise FileNotFoundError(path)

    text = path.read_text(encoding="utf-8")

    if "\x00" in text:
        raise ValueError(f"NUL byte found in {path}")

combined = "\n".join(path.read_text(encoding="utf-8") for path in files)

missing = [
    phrase for phrase in required
    if phrase.lower() not in combined.lower()
]

if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

print("=" * 80)
print("PHASE 10K SUPPORT-PERTURBATION MODEL AUDIT: PASS")
print("SUPPORT PERTURBATION MODEL: LOCKED")
print("LIPSCHITZ KERNEL ASSUMPTION: LOCKED")
print("SUPPORT-LEVEL CERTIFICATE CANDIDATE: LOCKED")
print("NEXT TARGET: SUPPORT PERTURBATION STABILITY THEOREM")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
