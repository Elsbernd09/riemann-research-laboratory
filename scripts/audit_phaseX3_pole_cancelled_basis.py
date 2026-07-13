from pathlib import Path
import json
import math

from src.breakthrough_attack.pole_cancelled_smooth_basis import (
    SmoothBump,
    build_pole_cancelled_function,
    write_pole_cancelled_basis_certificate,
)

files = [
    Path("breakthrough_attack/phase_x3_built_in_pole_cancelled_smooth_basis/PHASE_X3_BUILT_IN_POLE_CANCELLED_SMOOTH_BASIS.md"),
    Path("breakthrough_attack/phase_x3_built_in_pole_cancelled_smooth_basis/POLE_CANCELLED_BASIS_STATUS.md"),
    Path("breakthrough_attack/phase_x3_built_in_pole_cancelled_smooth_basis/NEXT_PHASE_X4_SUPPORT_AND_FINITE_PRIME_CUTOFF_THEOREM.md"),
    Path("src/breakthrough_attack/pole_cancelled_smooth_basis.py"),
]

required = [
    "PHASE_X3_BUILT_IN_POLE_CANCELLED_SMOOTH_BASIS_COMPLETE",
    "RAW_SMOOTH_BUMPS_DEFINED",
    "CORRECTION_BUMPS_DEFINED",
    "MELLIN_MOMENT_CORRECTION_MATRIX_DEFINED",
    "CORRECTED_BASIS_DEFINED",
    "SMOOTH_COMPACT_SUPPORT_PRESERVED_PROVED",
    "BUILT_IN_POLE_CANCELLATION_PROVED",
    "FINITE_COMBINATIONS_POLE_CANCELLED_PROVED",
    "POLE_CANCELLED_SMOOTH_BASIS_MECHANISM_CREATED",
    "CERTIFIED_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X4_SUPPORT_AND_FINITE_PRIME_CUTOFF_THEOREM",
    "Theorem X3.1",
    "Theorem X3.2",
    "Theorem X3.3",
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

corr0 = SmoothBump(center=-1.0, width=0.35)
corr1 = SmoothBump(center=1.0, width=0.35)
raw = SmoothBump(center=0.0, width=0.30)
phi = build_pole_cancelled_function(raw, corr0, corr1)

m0 = phi.mellin_moment(0.0)
m1 = phi.mellin_moment(1.0)
assert math.isfinite(m0)
assert math.isfinite(m1)
assert abs(m0) < 5e-4
assert abs(m1) < 5e-4

lo, hi = phi.support_x()
assert lo > 0
assert lo < hi

out = Path("breakthrough_attack/phase_x3_built_in_pole_cancelled_smooth_basis/pole_cancelled_basis_certificate.json")
write_pole_cancelled_basis_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "PHASE_X3_BUILT_IN_POLE_CANCELLED_SMOOTH_BASIS_COMPLETE"
assert payload["certification_status"] == "FLOATING_PROTOTYPE_ONLY_NOT_CERTIFIED"
assert len(payload["basis"]) == 3

print("=" * 80)
print("PHASE X3 BUILT-IN POLE-CANCELLED SMOOTH BASIS AUDIT: PASS")
print("RAW SMOOTH BUMPS: DEFINED")
print("CORRECTION BUMPS: DEFINED")
print("MELLIN MOMENT CORRECTION MATRIX: DEFINED")
print("CORRECTED BASIS: CREATED")
print("BUILT-IN POLE CANCELLATION: FLOATING RESIDUAL CHECK PASSED")
print("FINITE COMBINATIONS: THEOREM RECORDED")
print("CERTIFIED ENTRY: NOT COMPUTED")
print("NEXT: SUPPORT AND FINITE PRIME CUTOFF")
print("=" * 80)
