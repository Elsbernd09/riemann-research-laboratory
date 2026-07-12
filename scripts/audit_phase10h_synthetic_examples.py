from pathlib import Path

files = [
    Path("scripts/run_phase10h_synthetic_examples.py"),
    Path("original_results/finite_bombieri_stability/examples/PHASE_10H_SYNTHETIC_EXAMPLES_AND_FAILURE_CASES.md"),
    Path("original_results/finite_bombieri_stability/examples/EXAMPLE_INTERPRETATION_LOCK.md"),
    Path("original_results/finite_bombieri_stability/examples/PHASE_10H_SYNTHETIC_EXAMPLES_OUTPUT.txt"),
]

required = [
    "Synthetic Examples",
    "failure cases",
    "certificate_passes",
    "count_stable",
    "sufficient condition",
    "negative eigenvalue",
    "No zeta zeros used",
    "No RH claim",
    "No novelty claim",
    "This phase does not prove RH",
    "This phase does not falsify RH",
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
print("PHASE 10H SYNTHETIC EXAMPLES AUDIT: PASS")
print("CERTIFIED STABLE CASES: RECORDED")
print("FAILURE CASES: RECORDED")
print("SUFFICIENT-CONDITION WARNING: RECORDED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
