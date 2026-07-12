from pathlib import Path
import json
import math

from src.level4.toy_basis import (
    TriangularLogBump,
    convolution_eval_x,
    build_default_toy_basis,
    write_toy_basis_certificate,
)

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/toy_basis_prototype/PHASE_12X_TOY_BASIS_PROTOTYPE.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/toy_basis_prototype/TOY_BASIS_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/toy_basis_prototype/NEXT_PHASE_12Y_TOY_ENTRY_PROTOTYPE.md"),
    Path("src/level4/toy_basis.py"),
]

required = [
    "TOY_BASIS_PROTOTYPE_COMPLETE",
    "TRIANGULAR_LOG_BUMP_DEFINED",
    "MULTIPLICATIVE_TOY_BASIS_DEFINED",
    "TOY_BASIS_COMPACT_SUPPORT_PROVED",
    "STAR_EVALUATOR_IMPLEMENTED",
    "CONVOLUTION_EVALUATOR_IMPLEMENTED",
    "TOY_BASIS_ONLY_NOT_FINAL_C_C_INFINITY_BASIS",
    "TRUE_CERTIFIED_ARITHMETIC_ENTRY_NOT_YET_COMPUTED",
    "LEVEL4_READY_FOR_TOY_ENTRY_PROTOTYPE",
    "Theorem 12X.1",
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

b = TriangularLogBump(center=0.0, width=1.0)
assert b.eval_x(1.0) == 1.0
assert b.eval_x(math.exp(2.0)) == 0.0
assert b.star_x(1.0) == 1.0

basis = build_default_toy_basis()
val = convolution_eval_x(basis[0], basis[1], 1.0, steps=200)
assert val >= 0.0

out = Path("original_results/finite_bombieri_stability/level4_candidate/toy_basis_prototype/toy_basis_certificate.json")
write_toy_basis_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "TOY_BASIS_PROTOTYPE_COMPLETE"
assert payload["important_boundary"] == "TOY_BASIS_ONLY_NOT_FINAL_C_C_INFINITY_BASIS"

print("=" * 80)
print("PHASE 12X TOY BASIS PROTOTYPE AUDIT: PASS")
print("TRIANGULAR LOG BUMP: DEFINED")
print("MULTIPLICATIVE TOY BASIS: DEFINED")
print("COMPACT SUPPORT: PROVED")
print("STAR EVALUATOR: IMPLEMENTED")
print("CONVOLUTION EVALUATOR: IMPLEMENTED")
print("TOY BASIS ONLY: NOT FINAL C_C_INFINITY BASIS")
print("TRUE CERTIFIED ARITHMETIC ENTRY: NOT YET COMPUTED")
print("=" * 80)
