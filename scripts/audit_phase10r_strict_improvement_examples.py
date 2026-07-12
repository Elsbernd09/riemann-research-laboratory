from pathlib import Path

files = [
    Path("scripts/run_phase10r_strict_improvement_examples.py"),
    Path("original_results/finite_bombieri_stability/sharper_bounds/examples/PHASE_10R_STRICT_IMPROVEMENT_EXAMPLES.md"),
    Path("original_results/finite_bombieri_stability/sharper_bounds/examples/STRICT_IMPROVEMENT_INTERPRETATION_LOCK.md"),
    Path("original_results/finite_bombieri_stability/sharper_bounds/examples/PHASE_10R_STRICT_IMPROVEMENT_EXAMPLES_OUTPUT.txt"),
]

required = [
    "Strict-Improvement Examples",
    "STRICT_IMPROVEMENT_EXAMPLES",
    "old certificate fails",
    "new certificate passes",
    "weighted radius",
    "not merely cosmetic",
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
print("PHASE 10R STRICT-IMPROVEMENT EXAMPLES AUDIT: PASS")
print("OLD FAILS / NEW PASSES: RECORDED")
print("WEIGHTED RADIUS ADVANTAGE: RECORDED")
print("HONEST NON-CERTIFICATION: RECORDED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
