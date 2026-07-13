from pathlib import Path
from decimal import Decimal
import json

from src.breakthrough_attack.constant_term_interval_certificate import (
    DecimalInterval,
    log_pi_gamma_interval,
    constant_term_interval,
    compute_constant_term_interval_certificate,
    write_constant_term_interval_certificate,
)

files = [
    Path("breakthrough_attack/phase_x16_constant_term_interval_certificate/PHASE_X16_CONSTANT_TERM_INTERVAL_CERTIFICATE.md"),
    Path("breakthrough_attack/phase_x16_constant_term_interval_certificate/CONSTANT_TERM_STATUS.md"),
    Path("breakthrough_attack/phase_x16_constant_term_interval_certificate/NEXT_PHASE_X17_ARCHIMEDEAN_INTEGRAL_INTERVAL_CERTIFICATE.md"),
    Path("src/breakthrough_attack/constant_term_interval_certificate.py"),
]

required = [
    "PHASE_X16_CONSTANT_TERM_INTERVAL_CERTIFICATE_COMPLETE",
    "LOG_PI_GAMMA_INTERVAL_CREATED",
    "F_AT_ONE_INTERVAL_CREATED",
    "CONSTANT_TERM_INTERVAL_CREATED",
    "CONSTANT_TERM_INTERVAL_ENCLOSURE_PROVED",
    "POINTWISE_CONVOLUTION_CERTIFICATION_BLOCKER_IDENTIFIED",
    "CONSTANT_TERM_CERTIFICATE_POINTWISE_CONVOLUTION_NOT_CERTIFIED",
    "FULL_T_BL_ENTRY_NOT_CERTIFIED",
    "CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X17_ARCHIMEDEAN_INTEGRAL_INTERVAL_CERTIFICATE",
    "Theorem X16.1",
    "Theorem X16.2",
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

K = log_pi_gamma_interval()
assert K.lo <= K.hi
assert K.lo > 0

F1 = DecimalInterval(Decimal("2"), Decimal("3"))
C = constant_term_interval(K, F1)
assert C.lo <= C.hi
assert C.hi < 0

cert = compute_constant_term_interval_certificate(conv_steps=60, f1_radius=Decimal("1e-5"))
assert cert.certification_status == "CONSTANT_TERM_INTERVAL_CERTIFICATE_POINTWISE_CONVOLUTION_NOT_CERTIFIED"
assert Decimal(cert.constant_term_interval[0]) <= Decimal(cert.constant_term_interval[1])

out = Path("breakthrough_attack/phase_x16_constant_term_interval_certificate/constant_term_interval_certificate.json")
write_constant_term_interval_certificate(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["status"] == "PHASE_X16_CONSTANT_TERM_INTERVAL_CERTIFICATE_COMPLETE"
assert saved["full_entry_certified"] is False
assert saved["pointwise_convolution_certified"] is False

print("=" * 80)
print("PHASE X16 CONSTANT-TERM INTERVAL CERTIFICATE AUDIT: PASS")
print("LOG PI + GAMMA INTERVAL: CREATED")
print("F(1) INTERVAL: CREATED")
print("CONSTANT TERM INTERVAL: CREATED")
print("POINTWISE CONVOLUTION CERTIFICATION: BLOCKER IDENTIFIED")
print("FULL T_BL ENTRY: NOT CERTIFIED")
print("CERTIFIED ARITHMETIC ENTRY: NOT COMPUTED")
print("NEXT: ARCHIMEDEAN INTEGRAL INTERVAL CERTIFICATE")
print("=" * 80)
