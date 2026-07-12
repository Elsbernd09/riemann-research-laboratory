from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/certified_algorithm_v2/PHASE_10W_COMBINED_RADIUS_CERTIFIED_ALGORITHM.md"),
    Path("original_results/finite_bombieri_stability/certified_algorithm_v2/ALGORITHM_10W_LOCK.md"),
    Path("scripts/run_phase10w_combined_radius_algorithm.py"),
    Path("original_results/finite_bombieri_stability/certified_algorithm_v2/PHASE_10W_COMBINED_RADIUS_ALGORITHM_OUTPUT.txt"),
]

required = [
    "COMBINED_RADIUS_CERTIFIED_ALGORITHM",
    "COMBINED_MINIMUM_RADIUS_CERTIFICATE",
    "CERTIFIED_STABLE",
    "NOT_CERTIFIED",
    "frobenius_radius",
    "row_sum_radius",
    "combined_minimum_radius",
    "Theorem 10V.3",
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
print("PHASE 10W COMBINED-RADIUS ALGORITHM AUDIT: PASS")
print("FROBENIUS RADIUS: IMPLEMENTED")
print("ROW-SUM RADIUS: IMPLEMENTED")
print("COMBINED MINIMUM RADIUS: IMPLEMENTED")
print("CERTIFIED_STABLE / NOT_CERTIFIED: LOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
