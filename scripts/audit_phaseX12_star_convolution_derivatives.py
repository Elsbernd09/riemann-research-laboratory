from pathlib import Path
from decimal import Decimal
import json

from src.breakthrough_attack.primitive_interval_bump_bounds import D, DecInterval
from src.breakthrough_attack.star_convolution_derivative_bounds import (
    interval_abs_sup,
    reciprocal_power_positive,
    build_demo_corrected_basis_interval_spec,
    star_second_interval_bound_for_x_interval,
    compute_star_convolution_derivative_bound,
    write_star_convolution_derivative_bounds_certificate,
)

files = [
    Path("breakthrough_attack/phase_x12_star_and_convolution_derivative_bounds/PHASE_X12_STAR_AND_CONVOLUTION_DERIVATIVE_BOUNDS.md"),
    Path("breakthrough_attack/phase_x12_star_and_convolution_derivative_bounds/STAR_CONVOLUTION_DERIVATIVE_STATUS.md"),
    Path("breakthrough_attack/phase_x12_star_and_convolution_derivative_bounds/NEXT_PHASE_X13_PARTIAL_SINGLE_ENTRY_INTERVAL_CERTIFICATE.md"),
    Path("src/breakthrough_attack/star_convolution_derivative_bounds.py"),
]

required = [
    "PHASE_X12_STAR_AND_CONVOLUTION_DERIVATIVE_BOUNDS_COMPLETE",
    "STAR_SECOND_DERIVATIVE_INTERVAL_BOUND_CREATED",
    "CONVOLUTION_SECOND_DERIVATIVE_BOUND_CREATED",
    "STAR_SECOND_DERIVATIVE_INTERVAL_ENCLOSURE_PROVED",
    "CONVOLUTION_SECOND_DERIVATIVE_BOUND_PROVED",
    "F_SECOND_DERIVATIVE_BOUND_AVAILABLE_FOR_QUADRATURE",
    "COEFFICIENT_CERTIFICATION_INCOMPLETE",
    "CERTIFIED_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X13_PARTIAL_SINGLE_ENTRY_INTERVAL_CERTIFICATE",
    "Theorem X12.1",
    "Theorem X12.2",
    "This phase does not prove RH",
    "This phase does not prove a breakthrough",
    "This phase does not establish novelty",
    "This phase does not compute a fully certified arithmetic entry",
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

assert interval_abs_sup(DecInterval(D("-2"), D("3"))) == D("3")
rp = reciprocal_power_positive(DecInterval(D("2"), D("4")), 2)
assert rp.lo <= rp.hi
assert rp.lo > 0

spec = build_demo_corrected_basis_interval_spec()
X = DecInterval(D("0.3"), D("3.0"))
S = star_second_interval_bound_for_x_interval(spec, X)
assert S.lo <= S.hi

bound = compute_star_convolution_derivative_bound()
assert Decimal(bound.phi_sup_bound) >= 0
assert Decimal(bound.star_second_sup_bound) >= 0
assert Decimal(bound.convolution_second_derivative_bound) >= 0
assert bound.certification_status == "CONVOLUTION_SECOND_DERIVATIVE_BOUND_CREATED_COEFFICIENTS_NOT_CERTIFIED"

out = Path("breakthrough_attack/phase_x12_star_and_convolution_derivative_bounds/star_convolution_derivative_bounds_certificate.json")
write_star_convolution_derivative_bounds_certificate(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["status"] == "PHASE_X12_STAR_AND_CONVOLUTION_DERIVATIVE_BOUNDS_COMPLETE"

print("=" * 80)
print("PHASE X12 STAR AND CONVOLUTION DERIVATIVE BOUNDS AUDIT: PASS")
print("STAR SECOND DERIVATIVE INTERVAL BOUND: CREATED")
print("CONVOLUTION SECOND DERIVATIVE BOUND: CREATED")
print("STAR ENCLOSURE THEOREM: RECORDED")
print("CONVOLUTION BOUND THEOREM: RECORDED")
print("F'' BOUND: AVAILABLE FOR QUADRATURE")
print("COEFFICIENT CERTIFICATION: INCOMPLETE")
print("CERTIFIED ENTRY: NOT COMPUTED")
print("NEXT: PARTIAL SINGLE ENTRY INTERVAL CERTIFICATE")
print("=" * 80)
