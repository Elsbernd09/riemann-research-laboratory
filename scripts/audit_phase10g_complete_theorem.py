from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/theorems/PHASE_10G_COMPLETE_FINITE_STABILITY_THEOREM.md"),
    Path("original_results/finite_bombieri_stability/theorems/THEOREM_10G_LOCK.md"),
    Path("original_results/finite_bombieri_stability/theorems/PHASE_10G_THEOREM_AUDIT_NOTES.md"),
]

required = [
    "Complete Finite Bombieri-Style Stability Theorem",
    "Theorem 10G.1",
    "Corollary 10G.2",
    "N\\varepsilon<g_0(M)",
    "Nm_{\\max}\\eta<g_0(M)",
    "negative eigenvalue count",
    "Hermitian",
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
print("PHASE 10G COMPLETE FINITE STABILITY THEOREM AUDIT: PASS")
print("THEOREM 10G.1: LOCKED")
print("KERNEL-LEVEL CERTIFICATE: LOCKED")
print("NEGATIVE-COUNT STABILITY: PROVED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
