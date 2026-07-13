from pathlib import Path
from decimal import Decimal
import json

from src.breakthrough_attack.single_entry_pipeline import von_mangoldt
from src.breakthrough_attack.prime_side_interval_certificate import (
    DecimalInterval,
    point_value_interval_from_float,
    tilde_value_interval_from_f_at_inv_n,
    compute_prime_side_interval_certificate,
    write_prime_side_interval_certificate,
)

files = [
    Path("breakthrough_attack/phase_x15_prime_side_interval_certificate/PHASE_X15_PRIME_SIDE_INTERVAL_CERTIFICATE.md"),
    Path("breakthrough_attack/phase_x15_prime_side_interval_certificate/PRIME_SIDE_STATUS.md"),
    Path("breakthrough_attack/phase_x15_prime_side_interval_certificate/NEXT_PHASE_X16_CONSTANT_TERM_INTERVAL_CERTIFICATE.md"),
    Path("src/breakthrough_attack/prime_side_interval_certificate.py"),
]

required = [
    "PHASE_X15_PRIME_SIDE_INTERVAL_CERTIFICATE_COMPLETE",
    "FINITE_PRIME_CUTOFF_USED",
    "VON_MANGOLDT_FINITE_TERMS_CREATED",
    "PRIME_SIDE_INTERVAL_SUM_CREATED",
    "FINITE_PRIME_SIDE_INTERVAL_SUMMATION_PROVED",
    "POINTWISE_CONVOLUTION_CERTIFICATION_BLOCKER_IDENTIFIED",
    "PRIME_SIDE_CERTIFICATE_POINTWISE_CONVOLUTION_NOT_CERTIFIED",
    "FULL_T_BL_ENTRY_NOT_CERTIFIED",
    "CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X16_CONSTANT_TERM_INTERVAL_CERTIFICATE",
    "Theorem X15.1",
    "Theorem X15.2",
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

assert von_mangoldt(1) == 0.0
assert von_mangoldt(2) > 0.0
assert von_mangoldt(4) > 0.0
assert von_mangoldt(6) == 0.0

I = point_value_interval_from_float(2.0, Decimal("0.1"))
T = tilde_value_interval_from_f_at_inv_n(I, 2)
assert T.lo == Decimal("0.95")
assert T.hi == Decimal("1.05")

A = DecimalInterval(Decimal("0"), Decimal("1"))
B = DecimalInterval(Decimal("2"), Decimal("3"))
C = A + B
assert C.lo == Decimal("2")
assert C.hi == Decimal("4")

cert = compute_prime_side_interval_certificate(conv_steps=60, point_radius=Decimal("1e-5"))
assert cert.certification_status == "PRIME_SIDE_INTERVAL_CERTIFICATE_POINTWISE_CONVOLUTION_NOT_CERTIFIED"
assert cert.f_support[0] > 0
assert cert.f_support[0] < cert.f_support[1]
assert cert.finite_prime_cutoff >= 1
assert Decimal(cert.prime_side_interval[0]) <= Decimal(cert.prime_side_interval[1])

out = Path("breakthrough_attack/phase_x15_prime_side_interval_certificate/prime_side_interval_certificate.json")
write_prime_side_interval_certificate(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["status"] == "PHASE_X15_PRIME_SIDE_INTERVAL_CERTIFICATE_COMPLETE"
assert saved["full_entry_certified"] is False
assert saved["pointwise_convolution_certified"] is False

print("=" * 80)
print("PHASE X15 PRIME-SIDE INTERVAL CERTIFICATE AUDIT: PASS")
print("FINITE PRIME CUTOFF: USED")
print("VON MANGOLDT FINITE TERMS: CREATED")
print("PRIME-SIDE INTERVAL SUM: CREATED")
print("POINTWISE CONVOLUTION CERTIFICATION: BLOCKER IDENTIFIED")
print("FULL T_BL ENTRY: NOT CERTIFIED")
print("CERTIFIED ARITHMETIC ENTRY: NOT COMPUTED")
print("NEXT: CONSTANT-TERM INTERVAL CERTIFICATE")
print("=" * 80)
