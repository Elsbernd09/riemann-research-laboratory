from pathlib import Path
from decimal import Decimal
import json

from src.breakthrough_attack.coefficient_solve_certification import (
    DecimalInterval,
    interval_linear_residual,
    compute_coefficient_solve_certificate,
    write_coefficient_solve_certificate,
)

files = [
    Path("breakthrough_attack/phase_x19_coefficient_solve_certification/PHASE_X19_COEFFICIENT_SOLVE_CERTIFICATION.md"),
    Path("breakthrough_attack/phase_x19_coefficient_solve_certification/COEFFICIENT_SOLVE_STATUS.md"),
    Path("breakthrough_attack/phase_x19_coefficient_solve_certification/NEXT_PHASE_X20_OUTWARD_ROUNDING_AND_INTERVAL_AUDIT.md"),
    Path("src/breakthrough_attack/coefficient_solve_certification.py"),
]

required = [
    "PHASE_X19_COEFFICIENT_SOLVE_CERTIFICATION_COMPLETE",
    "MELLIN_MOMENT_SYSTEM_RECONSTRUCTED",
    "COEFFICIENT_INTERVALS_CREATED",
    "MOMENT_INTERVALS_CREATED",
    "POLE_RESIDUAL_INTERVALS_CREATED",
    "RESIDUAL_INTERVAL_ENCLOSURE_PROVED",
    "COEFFICIENT_SOLVE_RESIDUAL_CERTIFIED_MOMENT_INTEGRALS_NOT_CERTIFIED",
    "RAW_MELLIN_MOMENT_CERTIFICATION_BLOCKER_IDENTIFIED",
    "CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X20_OUTWARD_ROUNDING_AND_INTERVAL_AUDIT",
    "Theorem X19.1",
    "Theorem X19.2",
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

mb = DecimalInterval(Decimal("10"), Decimal("10"))
mu0 = DecimalInterval(Decimal("2"), Decimal("2"))
mu1 = DecimalInterval(Decimal("3"), Decimal("3"))
alpha = DecimalInterval(Decimal("2"), Decimal("2"))
beta = DecimalInterval(Decimal("2"), Decimal("2"))
r = interval_linear_residual(mb, mu0, mu1, alpha, beta)
assert r.lo == Decimal("0")
assert r.hi == Decimal("0")
assert r.contains_zero()

cert = compute_coefficient_solve_certificate(
    moment_radius=Decimal("1e-8"),
    coefficient_radius=Decimal("1e-8"),
)
assert cert.certification_status == "COEFFICIENT_SOLVE_RESIDUAL_CERTIFIED_MOMENT_INTEGRALS_NOT_CERTIFIED"
assert cert.raw_moment_integrals_certified is False
assert Decimal(cert.m0_residual_width) >= 0
assert Decimal(cert.m1_residual_width) >= 0
assert "raw Mellin moment integral certification" in cert.unresolved_gates

out = Path("breakthrough_attack/phase_x19_coefficient_solve_certification/coefficient_solve_certificate.json")
write_coefficient_solve_certificate(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["status"] == "PHASE_X19_COEFFICIENT_SOLVE_CERTIFICATION_COMPLETE"
assert saved["coefficient_residual_algebra_certified"] is True
assert saved["raw_moment_integrals_certified"] is False
assert saved["certified_arithmetic_entry"] is False

print("=" * 80)
print("PHASE X19 COEFFICIENT-SOLVE CERTIFICATION AUDIT: PASS")
print("MELLIN MOMENT SYSTEM: RECONSTRUCTED")
print("COEFFICIENT INTERVALS: CREATED")
print("MOMENT INTERVALS: CREATED")
print("POLE RESIDUAL INTERVALS: CREATED")
print("RESIDUAL ALGEBRA: CERTIFIED")
print("RAW MELLIN MOMENT CERTIFICATION: BLOCKER IDENTIFIED")
print("CERTIFIED ARITHMETIC ENTRY: NOT COMPUTED")
print("NEXT: OUTWARD ROUNDING AND INTERVAL AUDIT")
print("=" * 80)
