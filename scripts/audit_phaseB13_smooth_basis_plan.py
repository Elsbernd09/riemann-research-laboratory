from pathlib import Path
import json
import math

from src.level4.smooth_basis_plan import (
    SmoothLogBumpSpec,
    smooth_bump_value,
    smooth_log_bump_value,
    write_smooth_basis_plan_certificate,
)

files = [
    Path("breakthrough_push/phase_b13_smooth_basis_certification_plan/PHASE_B13_SMOOTH_BASIS_CERTIFICATION_PLAN.md"),
    Path("breakthrough_push/phase_b13_smooth_basis_certification_plan/SMOOTH_BASIS_PLAN_STATUS.md"),
    Path("breakthrough_push/phase_b13_smooth_basis_certification_plan/NEXT_PHASE_B14_SMOOTH_BASIS_IMPLEMENTATION.md"),
    Path("src/level4/smooth_basis_plan.py"),
]

required = [
    "PHASE_B13_SMOOTH_BASIS_CERTIFICATION_PLAN_COMPLETE",
    "SMOOTH_BUMP_DEFINED",
    "LOG_SMOOTH_BASIS_DEFINED",
    "SMOOTH_BASIS_IN_CC_INFINITY_PROVED",
    "STAR_SUPPORT_BOUND_PROVED",
    "CONVOLUTION_SUPPORT_BOUND_PROVED",
    "FINITE_PRIME_CUTOFF_FROM_SUPPORT_IDENTIFIED",
    "TRIANGULAR_TOY_BASIS_REPLACEMENT_PLAN_CREATED",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "READY_FOR_PHASE_B14_SMOOTH_BASIS_IMPLEMENTATION",
    "Theorem B13.1",
    "Theorem B13.2",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a breakthrough",
    "This phase does not prove novelty",
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

spec = SmoothLogBumpSpec(center=0.0, width=0.75)
lo, hi = spec.support_x()
assert lo < 1.0 < hi
slo, shi = spec.star_support_x()
assert slo < 1.0 < shi
clo, chi = spec.convolution_support_x()
assert abs(clo - math.exp(-1.5)) < 1e-12
assert abs(chi - math.exp(1.5)) < 1e-12
assert spec.prime_cutoff() == int(math.floor(math.exp(1.5)))

assert smooth_bump_value(0.0) > 0.0
assert smooth_bump_value(1.0) == 0.0
assert smooth_bump_value(-1.0) == 0.0
assert smooth_log_bump_value(1.0, spec) > 0.0

out = Path("breakthrough_push/phase_b13_smooth_basis_certification_plan/smooth_basis_plan_certificate.json")
write_smooth_basis_plan_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "PHASE_B13_SMOOTH_BASIS_CERTIFICATION_PLAN_COMPLETE"

print("=" * 80)
print("PHASE B13 SMOOTH BASIS CERTIFICATION PLAN AUDIT: PASS")
print("SMOOTH BUMP: DEFINED")
print("LOG-SMOOTH BASIS: DEFINED")
print("C_C_INFINITY PROOF: RECORDED")
print("STAR SUPPORT BOUND: RECORDED")
print("CONVOLUTION SUPPORT BOUND: RECORDED")
print("FINITE PRIME CUTOFF: IDENTIFIED")
print("TRIANGULAR TOY BASIS REPLACEMENT: PLANNED")
print("BREAKTHROUGH: NOT ACHIEVED")
print("=" * 80)
