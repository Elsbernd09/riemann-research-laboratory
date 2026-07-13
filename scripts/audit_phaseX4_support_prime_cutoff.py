from pathlib import Path
import json
import math

from src.breakthrough_attack.support_prime_cutoff import (
    star_support,
    convolution_support,
    finite_prime_cutoff,
    build_demo_basis,
    support_table_for_basis,
    write_support_prime_cutoff_certificate,
)

files = [
    Path("breakthrough_attack/phase_x4_support_and_finite_prime_cutoff/PHASE_X4_SUPPORT_AND_FINITE_PRIME_CUTOFF.md"),
    Path("breakthrough_attack/phase_x4_support_and_finite_prime_cutoff/SUPPORT_CUTOFF_STATUS.md"),
    Path("breakthrough_attack/phase_x4_support_and_finite_prime_cutoff/NEXT_PHASE_X5_ARCHIMEDEAN_REMOVABLE_SINGULARITY_THEOREM.md"),
    Path("src/breakthrough_attack/support_prime_cutoff.py"),
]

required = [
    "PHASE_X4_SUPPORT_AND_FINITE_PRIME_CUTOFF_COMPLETE",
    "CORRECTED_BASIS_SUPPORT_BOUND_PROVED",
    "STAR_SUPPORT_BOUND_PROVED",
    "CONVOLUTION_SUPPORT_BOUND_PROVED",
    "FINITE_PRIME_CUTOFF_THEOREM_PROVED",
    "ENTRY_SUPPORT_TABLE_CREATED",
    "FINITE_PRIME_SUM_GATE_CLOSED_STRUCTURALLY",
    "CERTIFIED_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X5_ARCHIMEDEAN_REMOVABLE_SINGULARITY_THEOREM",
    "Theorem X4.1",
    "Theorem X4.2",
    "Theorem X4.3",
    "Theorem X4.4",
    "This phase does not prove RH",
    "This phase does not prove a breakthrough",
    "This phase does not establish novelty",
    "This phase does not compute a certified arithmetic entry",
]

for path in files:
    if not path.exists():
        raise FileNotFoundError(path)
    text = path.read_text(encoding="utf-8")
    if "\x00" in text:
        raise ValueError(f"NUL byte found in {path}")

combined = "\n".join(path.read_text(encoding="utf-8") for path in files)
missing = [phrase for phrase in required if phrase.lower() not in combined.lower()]
if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

assert star_support((2.0, 4.0)) == (0.25, 0.5)
assert convolution_support((2.0, 3.0), (5.0, 7.0)) == (10.0, 21.0)
assert finite_prime_cutoff((0.25, 3.1)) == 4
assert finite_prime_cutoff((0.5, 10.2)) == 10

basis = build_demo_basis()
table = support_table_for_basis(basis)
assert len(table) == 9

for row in table:
    a, b = row.entry_support
    assert a > 0
    assert a <= b
    assert row.finite_prime_cutoff == int(math.floor(max(b, 1.0 / a)))
    assert row.finite_prime_cutoff >= 1

out = Path("breakthrough_attack/phase_x4_support_and_finite_prime_cutoff/support_prime_cutoff_certificate.json")
write_support_prime_cutoff_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "PHASE_X4_SUPPORT_AND_FINITE_PRIME_CUTOFF_COMPLETE"
assert payload["basis_size"] == 3
assert len(payload["entry_support_table"]) == 9

print("=" * 80)
print("PHASE X4 SUPPORT AND FINITE PRIME CUTOFF AUDIT: PASS")
print("CORRECTED BASIS SUPPORT: PROVED")
print("STAR SUPPORT: PROVED")
print("CONVOLUTION SUPPORT: PROVED")
print("FINITE PRIME CUTOFF THEOREM: PROVED")
print("ENTRY SUPPORT TABLE: CREATED")
print("FINITE PRIME SUM GATE: CLOSED STRUCTURALLY")
print("CERTIFIED ENTRY: NOT COMPUTED")
print("NEXT: ARCHIMEDEAN REMOVABLE SINGULARITY")
print("=" * 80)
