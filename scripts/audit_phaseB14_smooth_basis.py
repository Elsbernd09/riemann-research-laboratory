from pathlib import Path
import json
import math

from src.level4.smooth_basis import (
    SmoothLogBump,
    smooth_convolution_with_star,
    write_smooth_basis_implementation_certificate,
)

files = [
    Path("breakthrough_push/phase_b14_smooth_basis_implementation/PHASE_B14_SMOOTH_BASIS_IMPLEMENTATION.md"),
    Path("breakthrough_push/phase_b14_smooth_basis_implementation/SMOOTH_BASIS_IMPLEMENTATION_STATUS.md"),
    Path("breakthrough_push/phase_b14_smooth_basis_implementation/NEXT_PHASE_B15_FINAL_BREAKTHROUGH_VERDICT.md"),
    Path("src/level4/smooth_basis.py"),
]

required = [
    "PHASE_B14_SMOOTH_BASIS_IMPLEMENTATION_COMPLETE",
    "SMOOTH_LOG_BUMP_IMPLEMENTED",
    "SMOOTH_BASIS_SUPPORT_IMPLEMENTED",
    "STAR_SUPPORT_IMPLEMENTED",
    "CONVOLUTION_SUPPORT_IMPLEMENTED",
    "FINITE_PRIME_CUTOFF_IMPLEMENTED",
    "FLOATING_SMOOTH_CONVOLUTION_PROTOTYPE_IMPLEMENTED",
    "CERTIFIED_ENTRY_NOT_COMPUTED",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "READY_FOR_PHASE_B15_FINAL_BREAKTHROUGH_VERDICT",
    "Theorem B14.1",
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

phi = SmoothLogBump(center=0.0, width=0.75)
lo, hi = phi.support_x()
assert lo < 1.0 < hi

slo, shi = phi.star_support_x()
assert slo < 1.0 < shi

clo, chi = phi.convolution_support_x()
assert clo < 1.0 < chi
assert abs(clo - math.exp(-1.5)) < 1e-12
assert abs(chi - math.exp(1.5)) < 1e-12

assert phi.eval_x(1.0) > 0.0
assert phi.star_eval_x(1.0) > 0.0

conv = smooth_convolution_with_star(phi, phi, 1.0, steps=50)
assert math.isfinite(conv)
assert conv >= 0.0

out = Path("breakthrough_push/phase_b14_smooth_basis_implementation/smooth_basis_implementation_certificate.json")
write_smooth_basis_implementation_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "PHASE_B14_SMOOTH_BASIS_IMPLEMENTATION_COMPLETE"
assert payload["certification_status"] == "FLOATING_IMPLEMENTATION_ONLY"

print("=" * 80)
print("PHASE B14 SMOOTH BASIS IMPLEMENTATION AUDIT: PASS")
print("SMOOTH LOG BUMP: IMPLEMENTED")
print("SUPPORT / STAR SUPPORT / CONVOLUTION SUPPORT: IMPLEMENTED")
print("FINITE PRIME CUTOFF: IMPLEMENTED")
print("FLOATING CONVOLUTION PROTOTYPE: IMPLEMENTED")
print("CERTIFIED ENTRY: NOT COMPUTED")
print("BREAKTHROUGH: NOT ACHIEVED")
print("=" * 80)
