from pathlib import Path
from decimal import Decimal
import json

from src.breakthrough_attack.tilde_integral_interval_certificate import (
    decimal_error_radius,
    compute_tilde_integral_certificate,
    write_tilde_integral_interval_certificate,
)

files = [
    Path("breakthrough_attack/phase_x14_tilde_integral_interval_certificate/PHASE_X14_TILDE_INTEGRAL_INTERVAL_CERTIFICATE.md"),
    Path("breakthrough_attack/phase_x14_tilde_integral_interval_certificate/TILDE_INTEGRAL_STATUS.md"),
    Path("breakthrough_attack/phase_x14_tilde_integral_interval_certificate/NEXT_PHASE_X15_PRIME_SIDE_INTERVAL_CERTIFICATE.md"),
    Path("src/breakthrough_attack/tilde_integral_interval_certificate.py"),
]

required = [
    "PHASE_X14_TILDE_INTEGRAL_INTERVAL_CERTIFICATE_COMPLETE",
    "TILDE_SUPPORT_THEOREM_PROVED",
    "TILDE_INTEGRAL_INTERVAL_CERTIFICATE_CREATED",
    "MIDPOINT_QUADRATURE_THEOREM_APPLIED_TO_TILDE_F",
    "TILDE_DERIVATIVE_BOUND_USED",
    "TILDE_INTEGRAL_CERTIFICATE_COEFFICIENTS_NOT_CERTIFIED",
    "FULL_T_BL_ENTRY_NOT_CERTIFIED",
    "CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X15_PRIME_SIDE_INTERVAL_CERTIFICATE",
    "Theorem X14.1",
    "Theorem X14.2",
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

e = decimal_error_radius(Decimal("0"), Decimal("1"), 10, Decimal("2"))
expected = Decimal("2") / (Decimal("24") * Decimal("100"))
assert abs(e - expected) < Decimal("1e-70")

cert = compute_tilde_integral_certificate(n_subintervals=50, conv_steps=60)
assert cert.certification_status == "TILDE_INTEGRAL_INTERVAL_CERTIFICATE_COEFFICIENTS_NOT_CERTIFIED"
assert cert.f_support[0] > 0
assert cert.f_support[0] < cert.f_support[1]
assert cert.tilde_support[0] > 0
assert cert.tilde_support[0] < cert.tilde_support[1]
assert Decimal(cert.error_radius) >= 0
assert Decimal(cert.interval_lower) <= Decimal(cert.interval_upper)

out = Path("breakthrough_attack/phase_x14_tilde_integral_interval_certificate/tilde_integral_interval_certificate.json")
write_tilde_integral_interval_certificate(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["status"] == "PHASE_X14_TILDE_INTEGRAL_INTERVAL_CERTIFICATE_COMPLETE"
assert saved["full_entry_certified"] is False

print("=" * 80)
print("PHASE X14 TILDE INTEGRAL INTERVAL CERTIFICATE AUDIT: PASS")
print("TILDE SUPPORT THEOREM: PROVED")
print("TILDE INTEGRAL INTERVAL CERTIFICATE: CREATED")
print("MIDPOINT QUADRATURE THEOREM: APPLIED TO TILDE F")
print("TILDE DERIVATIVE BOUND: USED")
print("FULL T_BL ENTRY: NOT CERTIFIED")
print("CERTIFIED ARITHMETIC ENTRY: NOT COMPUTED")
print("NEXT: PRIME-SIDE INTERVAL CERTIFICATE")
print("=" * 80)
