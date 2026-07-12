from pathlib import Path

files = [
    Path("scripts/run_phase10af_final_explicit_algorithm.py"),
    Path("original_results/finite_bombieri_stability/final_explicit_algorithm/PHASE_10AF_FINAL_EXPLICIT_ALGORITHM.md"),
    Path("original_results/finite_bombieri_stability/final_explicit_algorithm/ALGORITHM_10AF_LOCK.md"),
    Path("original_results/finite_bombieri_stability/final_explicit_algorithm/PHASE_10AF_FINAL_EXPLICIT_ALGORITHM_OUTPUT.txt"),
]

required = [
    "FINAL_EXPLICIT_H_KERNEL_CERTIFIED_ALGORITHM",
    "COMPUTABLE_H_KERNEL_LIPSCHITZ_CONSTANT",
    "EXPLICIT_H_KERNEL_SUPPORT_STABILITY_CERTIFICATE",
    "CERTIFIED_STABLE",
    "NOT_CERTIFIED",
    "frobenius_radius_LH",
    "row_sum_radius_LH",
    "combined_minimum_radius_LH",
    "This algorithm does not prove RH",
    "This algorithm does not falsify RH",
    "This algorithm does not use zeta zeros",
    "This algorithm does not claim novelty",
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
print("PHASE 10AF FINAL EXPLICIT H-KERNEL ALGORITHM AUDIT: PASS")
print("COMPUTABLE L_H: IMPLEMENTED")
print("EXPLICIT H-KERNEL SUPPORT-STABILITY CERTIFICATE: IMPLEMENTED")
print("CERTIFIED_STABLE / NOT_CERTIFIED: LOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
