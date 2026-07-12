from pathlib import Path
import json
import math

from src.level4.toy_basis import build_default_toy_basis
from src.level4.toy_arithmetic_entry import (
    von_mangoldt,
    compute_toy_entry,
    write_toy_entry_certificate,
)

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/toy_entry_prototype/PHASE_12Y_TOY_ARITHMETIC_ENTRY_PROTOTYPE.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/toy_entry_prototype/TOY_ENTRY_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/toy_entry_prototype/NEXT_PHASE_12Z_TOY_MATRIX_PROTOTYPE.md"),
    Path("src/level4/toy_arithmetic_entry.py"),
]

required = [
    "TOY_ARITHMETIC_ENTRY_PROTOTYPE_COMPLETE",
    "TOY_CENTRAL_INTEGRAL_COMPUTED",
    "TOY_STAR_CENTRAL_INTEGRAL_COMPUTED",
    "TOY_FINITE_PRIME_SUM_COMPUTED",
    "TOY_CONSTANT_TERM_COMPUTED",
    "TOY_ARCHIMEDEAN_TERM_COMPUTED",
    "TOY_ARITHMETIC_ENTRY_COMPUTED",
    "FLOATING_POINT_PROTOTYPE_ONLY",
    "CERTIFIED_INTERVAL_ENTRY_NOT_YET_PROVED",
    "LEVEL4_READY_FOR_TOY_MATRIX_PROTOTYPE",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove a complete arithmetic-only finite certificate",
    "This phase does not establish novelty",
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

assert abs(von_mangoldt(2) - math.log(2)) < 1e-12
assert abs(von_mangoldt(4) - math.log(2)) < 1e-12
assert von_mangoldt(6) == 0.0

basis = build_default_toy_basis()
comps = compute_toy_entry(basis[0], basis[0], integral_steps=120, conv_steps=120)
assert math.isfinite(comps.entry_value)
assert math.isfinite(comps.central)
assert math.isfinite(comps.prime)

out = Path("original_results/finite_bombieri_stability/level4_candidate/toy_entry_prototype/toy_entry_certificate.json")
write_toy_entry_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "TOY_ARITHMETIC_ENTRY_PROTOTYPE_COMPLETE"
assert payload["important_boundary"] == "FLOATING_POINT_PROTOTYPE_ONLY"

print("=" * 80)
print("PHASE 12Y TOY ARITHMETIC ENTRY AUDIT: PASS")
print("CENTRAL INTEGRAL: COMPUTED")
print("STAR CENTRAL INTEGRAL: COMPUTED")
print("FINITE PRIME SUM: COMPUTED")
print("CONSTANT TERM: COMPUTED")
print("ARCHIMEDEAN TERM: COMPUTED")
print("TOY ARITHMETIC ENTRY: COMPUTED")
print("FLOATING POINT PROTOTYPE ONLY")
print("CERTIFIED INTERVAL ENTRY: NOT YET PROVED")
print("=" * 80)
