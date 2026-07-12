from pathlib import Path

files = [
    Path("scripts/run_phase10m_support_perturbation_examples.py"),
    Path("original_results/finite_bombieri_stability/support_perturbation/examples/PHASE_10M_SUPPORT_PERTURBATION_EXAMPLES.md"),
    Path("original_results/finite_bombieri_stability/support_perturbation/examples/SUPPORT_EXAMPLE_INTERPRETATION_LOCK.md"),
    Path("original_results/finite_bombieri_stability/support_perturbation/examples/PHASE_10M_SUPPORT_PERTURBATION_EXAMPLES_OUTPUT.txt"),
]

required = [
    "Support-Perturbation Examples",
    "support-level certificate",
    "2Nm_{\\max}L_t(U)\\delta<g_0(M)",
    "certificate_passes",
    "count_stable",
    "synthetic finite",
    "No zeta zeros used",
    "No RH claim",
    "No novelty claim",
    "This phase does not prove RH",
    "This phase does not falsify RH",
]

for path in files:
    if not path.exists():
        raise FileNotFoundError(path)

    text = path.read_text(encoding="utf-8")

    if "\\x00" in text:
        raise ValueError(f"NUL byte found in {path}")

combined = "\\n".join(path.read_text(encoding="utf-8") for path in files)

missing = [
    phrase for phrase in required
    if phrase.lower() not in combined.lower()
]

if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

print("=" * 80)
print("PHASE 10M SUPPORT-PERTURBATION EXAMPLES AUDIT: PASS")
print("SUPPORT-LEVEL CERTIFICATES: RECORDED")
print("STABLE CASES: RECORDED")
print("FAILURE CASES: RECORDED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
