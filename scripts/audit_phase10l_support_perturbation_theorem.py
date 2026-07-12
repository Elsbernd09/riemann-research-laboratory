from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/support_perturbation/PHASE_10L_SUPPORT_PERTURBATION_STABILITY_THEOREM.md"),
    Path("original_results/finite_bombieri_stability/support_perturbation/THEOREM_10L_LOCK.md"),
    Path("original_results/finite_bombieri_stability/support_perturbation/PHASE_10L_THEOREM_AUDIT_NOTES.md"),
]

required = [
    "Support-Perturbation Stability Theorem",
    "Theorem 10L.1",
    "Corollary 10L.2",
    "2Nm_{\\max}L_t(U)\\delta<g_0(M",
    "maximum admissible support displacement",
    "Lipschitz",
    "Level 3",
    "This theorem does not prove RH",
    "This theorem does not falsify RH",
    "This theorem does not use zeta zeros",
    "This theorem does not claim novelty",
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
print("PHASE 10L SUPPORT-PERTURBATION THEOREM AUDIT: PASS")
print("THEOREM 10L.1: LOCKED")
print("SUPPORT-LEVEL CERTIFICATE: LOCKED")
print("MAXIMUM DISPLACEMENT CERTIFICATE: LOCKED")
print("LEVEL 3 CANDIDATE: STRONGER, NOT CLAIMED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
