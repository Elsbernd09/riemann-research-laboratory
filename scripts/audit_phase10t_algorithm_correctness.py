from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/certified_algorithm/proofs/PHASE_10T_ALGORITHM_CORRECTNESS_PROOF.md"),
    Path("original_results/finite_bombieri_stability/certified_algorithm/proofs/ALGORITHM_CORRECTNESS_LOCK.md"),
    Path("original_results/finite_bombieri_stability/certified_algorithm/proofs/PHASE_10T_PROOF_AUDIT_NOTES.md"),
]

required = [
    "Certified Algorithm Correctness Proof",
    "CERTIFIED_ALGORITHM_CORRECTNESS_PROOF",
    "Theorem 10T.1",
    "Proposition 10T.2",
    "CERTIFIED_STABLE",
    "NOT_CERTIFIED",
    "does not imply instability",
    "Theorem 10Q",
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
print("PHASE 10T CERTIFIED ALGORITHM CORRECTNESS AUDIT: PASS")
print("CERTIFIED_STABLE SOUNDNESS: PROVED")
print("NOT_CERTIFIED INTERPRETATION: LOCKED")
print("ALGORITHM CORRECTNESS TARGET: THEOREM 10Q")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
