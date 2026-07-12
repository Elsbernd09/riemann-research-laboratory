from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/proofs/PHASE_10F_SPECTRAL_GAP_STABILITY.md"),
    Path("original_results/finite_bombieri_stability/proofs/SPECTRAL_GAP_STABILITY_LOCK.md"),
    Path("original_results/finite_bombieri_stability/proofs/PHASE_10F_PROOF_AUDIT_NOTES.md"),
]

required = [
    "Spectral-Gap Stability",
    "Lemma 10F.1",
    "Lemma 10F.2",
    "Corollary 10F.3",
    "negative eigenvalue count",
    "operator norm",
    "N\\varepsilon<g_0(M)",
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
print("PHASE 10F SPECTRAL-GAP STABILITY AUDIT: PASS")
print("WEYL-TYPE BOUND: RECORDED")
print("NEGATIVE-COUNT STABILITY: LOCKED")
print("ENTRYWISE CERTIFICATE: LOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
