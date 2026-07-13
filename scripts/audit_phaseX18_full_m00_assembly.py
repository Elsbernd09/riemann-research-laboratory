from pathlib import Path
from decimal import Decimal
import json

from src.breakthrough_attack.assemble_full_m00_interval_certificate import (
    DecimalInterval,
    assemble_m00_interval,
    compute_full_m00_interval_certificate,
    write_full_m00_interval_certificate,
)

files = [
    Path("breakthrough_attack/phase_x18_assemble_full_m00_interval_certificate/PHASE_X18_ASSEMBLE_FULL_M00_INTERVAL_CERTIFICATE.md"),
    Path("breakthrough_attack/phase_x18_assemble_full_m00_interval_certificate/FULL_M00_STATUS.md"),
    Path("breakthrough_attack/phase_x18_assemble_full_m00_interval_certificate/NEXT_PHASE_X19_COEFFICIENT_SOLVE_CERTIFICATION.md"),
    Path("src/breakthrough_attack/assemble_full_m00_interval_certificate.py"),
]

required = [
    "PHASE_X18_ASSEMBLE_FULL_M00_INTERVAL_CERTIFICATE_COMPLETE",
    "CENTRAL_TERM_IMPORTED",
    "TILDE_TERM_IMPORTED",
    "PRIME_SIDE_TERM_IMPORTED",
    "CONSTANT_TERM_IMPORTED",
    "ARCHIMEDEAN_TERM_IMPORTED",
    "FULL_M00_INTERVAL_ASSEMBLED",
    "FULL_M00_INTERVAL_CERTIFICATE_ASSEMBLED_BUT_NOT_FULLY_CERTIFIED",
    "CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X19_COEFFICIENT_SOLVE_CERTIFICATION",
    "Theorem X18.1",
    "Theorem X18.2",
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

central = DecimalInterval(Decimal("1"), Decimal("2"))
tilde = DecimalInterval(Decimal("3"), Decimal("4"))
prime = DecimalInterval(Decimal("0.5"), Decimal("1.0"))
constant = DecimalInterval(Decimal("-2"), Decimal("-1"))
arch = DecimalInterval(Decimal("0.25"), Decimal("0.5"))

assembled = assemble_m00_interval(central, tilde, prime, constant, arch)
assert assembled.lo <= assembled.hi
assert assembled.lo == Decimal("1") + Decimal("3") - Decimal("1.0") + Decimal("-2") - Decimal("0.5")
assert assembled.hi == Decimal("2") + Decimal("4") - Decimal("0.5") + Decimal("-1") - Decimal("0.25")

cert = compute_full_m00_interval_certificate()
assert cert.certification_status == "FULL_M00_INTERVAL_CERTIFICATE_ASSEMBLED_BUT_NOT_FULLY_CERTIFIED"
assert Decimal(cert.assembled_m00_interval[0]) <= Decimal(cert.assembled_m00_interval[1])
assert "coefficient-solve certification" in cert.unresolved_gates

out = Path("breakthrough_attack/phase_x18_assemble_full_m00_interval_certificate/full_m00_interval_certificate.json")
write_full_m00_interval_certificate(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["status"] == "PHASE_X18_ASSEMBLE_FULL_M00_INTERVAL_CERTIFICATE_COMPLETE"
assert saved["full_entry_certified"] is False
assert saved["certified_arithmetic_entry"] is False

print("=" * 80)
print("PHASE X18 FULL M00 INTERVAL ASSEMBLY AUDIT: PASS")
print("CENTRAL TERM: IMPORTED")
print("TILDE TERM: IMPORTED")
print("PRIME SIDE TERM: IMPORTED")
print("CONSTANT TERM: IMPORTED")
print("ARCHIMEDEAN TERM: IMPORTED")
print("FULL M00 INTERVAL: ASSEMBLED")
print("STATUS: ASSEMBLED BUT NOT FULLY CERTIFIED")
print("NEXT: COEFFICIENT-SOLVE CERTIFICATION")
print("=" * 80)
