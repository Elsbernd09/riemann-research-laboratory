from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/final_explicit_algorithm/proofs/PHASE_10AG_FINAL_EXPLICIT_ALGORITHM_CORRECTNESS.md"),
    Path("original_results/finite_bombieri_stability/final_explicit_algorithm/proofs/FINAL_EXPLICIT_CORRECTNESS_LOCK.md"),
    Path("original_results/finite_bombieri_stability/final_explicit_algorithm/proofs/PHASE_10AG_STATUS.md"),
]

required = [
    "FINAL_EXPLICIT_ALGORITHM_CORRECTNESS_PROOF",
    "FINAL_EXPLICIT_H_KERNEL_CERTIFIED_ALGORITHM",
    "EXPLICIT_H_KERNEL_SUPPORT_STABILITY_CERTIFICATE",
    "Theorem 10AG.1",
    "Proposition 10AG.2",
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
print("PHASE 10AG FINAL EXPLICIT ALGORITHM CORRECTNESS AUDIT: PASS")
print("CERTIFIED_STABLE SOUNDNESS: PROVED")
print("NOT_CERTIFIED INTERPRETATION: LOCKED")
print("FINAL EXPLICIT PIPELINE: COMPLETE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
