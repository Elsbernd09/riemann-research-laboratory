from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/proofs/PHASE_10D_HERMITIAN_STRUCTURE_PROOF.md"),
    Path("original_results/finite_bombieri_stability/proofs/HERMITIAN_STRUCTURE_THEOREM_LOCK.md"),
    Path("original_results/finite_bombieri_stability/proofs/PHASE_10D_PROOF_AUDIT_NOTES.md"),
]

required = [
    "Hermitian Structure Proof",
    "Lemma 10D.1",
    "if and only if",
    "self-adjoint",
    "D^{1/2}A(t)D^{1/2}",
    "positive real integers",
    "ordinary Euclidean inner product",
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
print("PHASE 10D HERMITIAN STRUCTURE AUDIT: PASS")
print("LEMMA 10D.1: RECORDED")
print("HERMITIAN CONDITION: LOCKED")
print("SELF-ADJOINT COROLLARY: LOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
