from pathlib import Path
import json
from src.level4.interval_matrix import Interval, IntervalMatrix, write_placeholder_certificate

doc_files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/interval_matrix_implementation/PHASE_12V_INTERVAL_MATRIX_IMPLEMENTATION.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/interval_matrix_implementation/INTERVAL_MATRIX_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/interval_matrix_implementation/NEXT_PHASE_12W_TRUE_ENTRY_BLUEPRINT.md"),
    Path("src/level4/interval_matrix.py"),
]

required = [
    "INTERVAL_MATRIX_IMPLEMENTATION_COMPLETE",
    "REAL_INTERVAL_CLASS_IMPLEMENTED",
    "INTERVAL_MATRIX_CLASS_IMPLEMENTED",
    "HERMITIAN_RESIDUAL_INTERVAL_IMPLEMENTED",
    "RAYLEIGH_INTERVAL_IMPLEMENTED",
    "NEGATIVE_DIRECTION_CERTIFICATE_LOGIC_IMPLEMENTED",
    "PLACEHOLDER_ENTRIES_ONLY",
    "TRUE_ARITHMETIC_ENTRIES_NOT_YET_COMPUTED",
    "ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE",
    "Theorem 12V.1",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove a complete arithmetic-only finite certificate",
    "This phase does not establish novelty",
]

for path in doc_files:
    if not path.exists():
        raise FileNotFoundError(path)
    text = path.read_text(encoding="utf-8")
    if "\x00" in text:
        raise ValueError(f"NUL byte found in {path}")

combined = "\n".join(path.read_text(encoding="utf-8") for path in doc_files)
missing = [phrase for phrase in required if phrase.lower() not in combined.lower()]
if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

# Functional tests
a = Interval(1.0, 2.0)
b = Interval(-3.0, 4.0)
assert (a + b) == Interval(-2.0, 6.0)
assert (a - b) == Interval(-3.0, 5.0)
assert (a * b) == Interval(-6.0, 8.0)

matrix = IntervalMatrix([
    [Interval(-2.01, -1.99), Interval(0.49, 0.51)],
    [Interval(0.49, 0.51), Interval(0.99, 1.01)],
])

assert matrix.residual_exact_zero()
cert = matrix.negative_direction_certificate([1.0, 0.0])
assert cert["verdict"] == "CERTIFIED_NEGATIVE_DIRECTION"
assert cert["rayleigh_interval"]["hi"] < 0.0

out = Path("original_results/finite_bombieri_stability/level4_candidate/interval_matrix_implementation/placeholder_interval_certificate.json")
write_placeholder_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["important_boundary"] == "TRUE_ARITHMETIC_ENTRIES_NOT_YET_COMPUTED"
assert payload["negative_direction"]["verdict"] == "CERTIFIED_NEGATIVE_DIRECTION"

print("=" * 80)
print("PHASE 12V INTERVAL MATRIX IMPLEMENTATION AUDIT: PASS")
print("REAL INTERVAL CLASS: IMPLEMENTED")
print("INTERVAL MATRIX CLASS: IMPLEMENTED")
print("HERMITIAN RESIDUAL INTERVAL: IMPLEMENTED")
print("RAYLEIGH INTERVAL: IMPLEMENTED")
print("NEGATIVE DIRECTION LOGIC: IMPLEMENTED")
print("PLACEHOLDER ENTRIES ONLY")
print("TRUE ARITHMETIC ENTRIES: NOT YET COMPUTED")
print("ARITHMETIC-ONLY CERTIFICATE: NOT YET COMPLETE")
print("=" * 80)
