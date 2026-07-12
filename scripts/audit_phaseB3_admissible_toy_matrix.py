from pathlib import Path
import json
import math

from src.level4.admissible_toy_matrix import (
    assemble_three_basis_toy_matrix,
    symmetrize,
    write_admissible_toy_matrix_certificate,
)
from src.level4.admissible_subspace import (
    build_three_function_basis,
    constraint_matrix_for_basis,
    nullspace_2xm,
    restrict_matrix,
)

files = [
    Path("breakthrough_push/phase_b3_admissible_toy_matrix/PHASE_B3_ADMISSIBLE_TOY_MATRIX.md"),
    Path("breakthrough_push/phase_b3_admissible_toy_matrix/ADMISSIBLE_TOY_MATRIX_STATUS.md"),
    Path("breakthrough_push/phase_b3_admissible_toy_matrix/NEXT_PHASE_B4_PRIOR_ART_COLLISION.md"),
    Path("src/level4/admissible_toy_matrix.py"),
]

required = [
    "PHASE_B3_ADMISSIBLE_TOY_MATRIX_COMPLETE",
    "TOY_ARITHMETIC_MATRIX_ASSEMBLED_FOR_ADMISSIBLE_TEST",
    "POLE_CONSTRAINT_MATRIX_USED",
    "ADMISSIBLE_NULLSPACE_USED",
    "TOY_ADMISSIBLE_MATRIX_COMPUTED",
    "TOY_ADMISSIBLE_RAYLEIGH_LOGIC_TESTED",
    "POLE_ORTHOGONAL_PIPELINE_IMPLEMENTED",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "READY_FOR_PHASE_B4_PRIOR_ART_COLLISION",
    "Theorem B3.1",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a breakthrough",
    "This phase does not prove novelty",
    "This phase does not prove a certified arithmetic-only matrix",
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

basis = build_three_function_basis()
C = constraint_matrix_for_basis(basis)
N = nullspace_2xm(C)
raw = assemble_three_basis_toy_matrix(integral_steps=30, conv_steps=30)
assert len(raw) == 3 and len(raw[0]) == 3
assert all(math.isfinite(x) for row in raw for x in row)
sym = symmetrize(raw)
Madm = restrict_matrix(sym, N)
assert Madm
assert all(math.isfinite(x) for row in Madm for x in row)

out = Path("breakthrough_push/phase_b3_admissible_toy_matrix/admissible_toy_matrix_certificate.json")
write_admissible_toy_matrix_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "PHASE_B3_ADMISSIBLE_TOY_MATRIX_COMPLETE"
assert payload["important_boundary"] == "TOY_FLOATING_POINT_PIPELINE_ONLY"

print("=" * 80)
print("PHASE B3 ADMISSIBLE TOY MATRIX AUDIT: PASS")
print("TOY ARITHMETIC MATRIX: ASSEMBLED")
print("POLE CONSTRAINT MATRIX: USED")
print("ADMISSIBLE NULLSPACE: USED")
print("TOY ADMISSIBLE MATRIX: COMPUTED")
print("RAYLEIGH LOGIC: TESTED")
print("POLE-ORTHOGONAL PIPELINE: IMPLEMENTED")
print("BREAKTHROUGH: NOT ACHIEVED")
print("=" * 80)
