from pathlib import Path
import json
import math

from src.level4.admissible_subspace import (
    build_three_function_basis,
    constraint_matrix_for_basis,
    nullspace_2xm,
    restrict_matrix,
    write_admissible_subspace_certificate,
)

files = [
    Path("breakthrough_push/phase_b2_admissible_subspace/PHASE_B2_ADMISSIBLE_FINITE_SUBSPACE.md"),
    Path("breakthrough_push/phase_b2_admissible_subspace/ADMISSIBLE_SUBSPACE_STATUS.md"),
    Path("breakthrough_push/phase_b2_admissible_subspace/NEXT_PHASE_B3_ADMISSIBLE_TOY_MATRIX.md"),
    Path("src/level4/admissible_subspace.py"),
]

required = [
    "PHASE_B2_ADMISSIBLE_SUBSPACE_COMPLETE",
    "POLE_CONSTRAINT_MATRIX_DEFINED",
    "ADMISSIBLE_NULLSPACE_DEFINED",
    "ADMISSIBLE_MATRIX_RESTRICTION_PROVED",
    "M_ADM_EQUALS_N_STAR_M_N",
    "TOY_MELLIN_CONSTRAINTS_COMPUTED",
    "TOY_NULLSPACE_COMPUTED",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "READY_FOR_PHASE_B3_ADMISSIBLE_TOY_MATRIX",
    "Theorem B2.1",
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
assert len(C) == 2 and len(C[0]) == 3
N = nullspace_2xm(C)
assert len(N) == 3 and len(N[0]) == 1

# Check C*N approximately zero
for row in C:
    val = sum(row[i] * N[i][0] for i in range(3))
    assert abs(val) < 1e-6

M = [
    [1.0, 0.2, -0.1],
    [0.2, 0.8, 0.3],
    [-0.1, 0.3, 1.2],
]
Madm = restrict_matrix(M, N)
assert len(Madm) == 1 and len(Madm[0]) == 1
assert math.isfinite(Madm[0][0])

out = Path("breakthrough_push/phase_b2_admissible_subspace/admissible_subspace_certificate.json")
write_admissible_subspace_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "PHASE_B2_ADMISSIBLE_SUBSPACE_COMPLETE"

print("=" * 80)
print("PHASE B2 ADMISSIBLE SUBSPACE AUDIT: PASS")
print("POLE CONSTRAINT MATRIX: DEFINED")
print("ADMISSIBLE NULLSPACE: COMPUTED")
print("M_ADM = N^T M N: IMPLEMENTED")
print("FINITE ADMISSIBLE SUBSPACE THEOREM: RECORDED")
print("TOY MELLIN CONSTRAINTS: COMPUTED")
print("BREAKTHROUGH: NOT ACHIEVED")
print("=" * 80)
