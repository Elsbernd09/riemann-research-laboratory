from pathlib import Path
from decimal import Decimal
import json

from src.breakthrough_attack.archimedean_integral_interval_certificate import (
    decimal_error_radius,
    compute_archimedean_integral_certificate,
    write_archimedean_integral_interval_certificate,
)

files = [
    Path("breakthrough_attack/phase_x17_archimedean_integral_interval_certificate/PHASE_X17_ARCHIMEDEAN_INTEGRAL_INTERVAL_CERTIFICATE.md"),
    Path("breakthrough_attack/phase_x17_archimedean_integral_interval_certificate/ARCHIMEDEAN_INTEGRAL_STATUS.md"),
    Path("breakthrough_attack/phase_x17_archimedean_integral_interval_certificate/NEXT_PHASE_X18_ASSEMBLE_FULL_M00_INTERVAL_CERTIFICATE.md"),
    Path("src/breakthrough_attack/archimedean_integral_interval_certificate.py"),
]

required = [
    "PHASE_X17_ARCHIMEDEAN_INTEGRAL_INTERVAL_CERTIFICATE_COMPLETE",
    "ARCHIMEDEAN_CONTINUOUS_EXTENSION_USED",
    "ARCHIMEDEAN_SUPPORT_TRUNCATION_CREATED",
    "ARCHIMEDEAN_INTERVAL_CERTIFICATE_CREATED",
    "MIDPOINT_QUADRATURE_THEOREM_APPLIED_TO_ARCHIMEDEAN_TERM",
    "ARCHIMEDEAN_DERIVATIVE_BOUND_INCOMPLETE",
    "FULL_T_BL_ENTRY_NOT_CERTIFIED",
    "CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X18_ASSEMBLE_FULL_M00_INTERVAL_CERTIFICATE",
    "Theorem X17.1",
    "Theorem X17.2",
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

e = decimal_error_radius(Decimal("1"), Decimal("2"), 10, Decimal("3"))
expected = Decimal("3") / (Decimal("24") * Decimal("100"))
assert abs(e - expected) < Decimal("1e-70")

cert = compute_archimedean_integral_certificate(n_subintervals=50, conv_steps=60)
assert cert.certification_status == "ARCHIMEDEAN_INTERVAL_CERTIFICATE_DERIVATIVE_BOUND_INCOMPLETE"
assert cert.integration_interval[0] == 1.0
assert cert.integration_interval[1] >= 1.0
assert Decimal(cert.error_radius) >= 0
assert Decimal(cert.interval_lower) <= Decimal(cert.interval_upper)

out = Path("breakthrough_attack/phase_x17_archimedean_integral_interval_certificate/archimedean_integral_interval_certificate.json")
write_archimedean_integral_interval_certificate(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["status"] == "PHASE_X17_ARCHIMEDEAN_INTEGRAL_INTERVAL_CERTIFICATE_COMPLETE"
assert saved["full_entry_certified"] is False
assert saved["archimedean_derivative_bound_fully_certified"] is False

print("=" * 80)
print("PHASE X17 ARCHIMEDEAN INTEGRAL INTERVAL CERTIFICATE AUDIT: PASS")
print("ARCHIMEDEAN CONTINUOUS EXTENSION: USED")
print("ARCHIMEDEAN SUPPORT TRUNCATION: CREATED")
print("ARCHIMEDEAN INTERVAL CERTIFICATE: CREATED")
print("DERIVATIVE BOUND: INCOMPLETE")
print("FULL T_BL ENTRY: NOT CERTIFIED")
print("CERTIFIED ARITHMETIC ENTRY: NOT COMPUTED")
print("NEXT: ASSEMBLE FULL M00 INTERVAL CERTIFICATE")
print("=" * 80)
