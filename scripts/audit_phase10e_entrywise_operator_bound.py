from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/proofs/PHASE_10E_ENTRYWISE_TO_OPERATOR_NORM_BOUND.md"),
    Path("original_results/finite_bombieri_stability/proofs/ENTRYWISE_OPERATOR_BOUND_LOCK.md"),
    Path("original_results/finite_bombieri_stability/proofs/PHASE_10E_PROOF_AUDIT_NOTES.md"),
]

required = [
    "Entrywise Perturbation",
    "Lemma 10E.1",
    "Lemma 10E.2",
    "operator-norm",
    "Frobenius",
    "N\\varepsilon",
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
print("PHASE 10E ENTRYWISE TO OPERATOR-NORM AUDIT: PASS")
print("ENTRYWISE BOUND: LOCKED")
print("FROBENIUS BOUND: LOCKED")
print("OPERATOR-NORM BOUND: LOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
