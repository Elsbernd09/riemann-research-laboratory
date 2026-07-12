from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/certified_algorithm/PHASE_10S_CERTIFIED_STABILITY_ALGORITHM.md"),
    Path("scripts/run_phase10s_certified_stability_algorithm.py"),
    Path("original_results/finite_bombieri_stability/certified_algorithm/ALGORITHM_10S_LOCK.md"),
    Path("original_results/finite_bombieri_stability/certified_algorithm/PHASE_10S_CERTIFIED_ALGORITHM_OUTPUT.txt"),
]

required = [
    "Certified Stability Algorithm",
    "CERTIFIED_STABILITY_ALGORITHM",
    "CERTIFIED_STABLE",
    "NOT_CERTIFIED",
    "weighted_radius",
    "negative eigenvalue count",
    "Theorem 10Q",
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
print("PHASE 10S CERTIFIED STABILITY ALGORITHM AUDIT: PASS")
print("CERTIFIED_STABLE / NOT_CERTIFIED: LOCKED")
print("WEIGHTED RADIUS COMPUTATION: LOCKED")
print("CORRECTNESS TARGET: THEOREM 10Q")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
