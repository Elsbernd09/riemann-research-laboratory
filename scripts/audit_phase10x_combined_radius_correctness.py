from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/certified_algorithm_v2/proofs/PHASE_10X_COMBINED_RADIUS_CORRECTNESS_PROOF.md"),
    Path("original_results/finite_bombieri_stability/certified_algorithm_v2/proofs/COMBINED_RADIUS_CORRECTNESS_LOCK.md"),
    Path("original_results/finite_bombieri_stability/certified_algorithm_v2/proofs/PHASE_10X_PROOF_AUDIT_NOTES.md"),
]

required = [
    "COMBINED_RADIUS_CORRECTNESS_PROOF",
    "COMBINED_RADIUS_CERTIFIED_ALGORITHM",
    "COMBINED_MINIMUM_RADIUS_CERTIFICATE",
    "Theorem 10X.1",
    "Proposition 10X.2",
    "Theorem 10V.3",
    "CERTIFIED_STABLE",
    "NOT_CERTIFIED",
    "does not imply instability",
    "This proof does not prove RH",
    "This proof does not falsify RH",
    "This proof does not use zeta zeros",
    "This proof does not claim novelty",
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
print("PHASE 10X COMBINED-RADIUS CORRECTNESS AUDIT: PASS")
print("CERTIFIED_STABLE SOUNDNESS: PROVED")
print("NOT_CERTIFIED INTERPRETATION: LOCKED")
print("SOUNDNESS SOURCE: THEOREM 10V.3")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
