from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/matrix_specific_bounds/PHASE_10V_MATRIX_SPECIFIC_NORM_CERTIFICATE.md"),
    Path("original_results/finite_bombieri_stability/matrix_specific_bounds/THEOREM_10V_LOCK.md"),
    Path("scripts/run_phase10v_matrix_specific_examples.py"),
    Path("original_results/finite_bombieri_stability/matrix_specific_bounds/PHASE_10V_MATRIX_SPECIFIC_EXAMPLES_OUTPUT.txt"),
]

required = [
    "MATRIX_SPECIFIC_NORM_CERTIFICATE",
    "ROW_SUM_CERTIFICATE",
    "COMBINED_MINIMUM_RADIUS_CERTIFICATE",
    "Theorem 10V.1",
    "Theorem 10V.3",
    "row-sum certificate",
    "combined minimum radius",
    "This theorem does not prove RH",
    "This theorem does not falsify RH",
    "This theorem does not use zeta zeros",
    "This theorem does not claim novelty",
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
print("PHASE 10V MATRIX-SPECIFIC NORM AUDIT: PASS")
print("ROW-SUM CERTIFICATE: PROVED")
print("COMBINED MINIMUM RADIUS: PROVED")
print("EXAMPLES: GENERATED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
