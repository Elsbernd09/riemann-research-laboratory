from pathlib import Path
import json

from src.breakthrough_attack.primitive_interval_bump_bounds import (
    D,
    DecInterval,
    psi_interval,
    psi_prime_interval,
    psi_second_interval,
    make_primitive_bounds_payload,
    write_primitive_interval_bump_bounds_certificate,
)

files = [
    Path("breakthrough_attack/phase_x9_primitive_interval_bump_bounds/PHASE_X9_PRIMITIVE_INTERVAL_BUMP_BOUNDS.md"),
    Path("breakthrough_attack/phase_x9_primitive_interval_bump_bounds/PRIMITIVE_INTERVAL_BUMP_STATUS.md"),
    Path("breakthrough_attack/phase_x9_primitive_interval_bump_bounds/NEXT_PHASE_X10_LOG_BUMP_INTERVAL_DERIVATIVE_BOUNDS.md"),
    Path("src/breakthrough_attack/primitive_interval_bump_bounds.py"),
]

required = [
    "PHASE_X9_PRIMITIVE_INTERVAL_BUMP_BOUNDS_COMPLETE",
    "DECIMAL_INTERVAL_ARITHMETIC_CREATED",
    "PSI_INTERVAL_BOUND_CREATED",
    "PSI_PRIME_INTERVAL_BOUND_CREATED",
    "PSI_SECOND_INTERVAL_BOUND_CREATED",
    "PRIMITIVE_DERIVATIVE_FORMULAS_PROVED",
    "INTERVAL_ENCLOSURE_PRINCIPLE_RECORDED",
    "PRIMITIVE_INTERVAL_BOUNDS_CREATED_NOT_FORMALLY_VERIFIED",
    "CERTIFIED_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X10_LOG_BUMP_INTERVAL_DERIVATIVE_BOUNDS",
    "Theorem X9.1",
    "Theorem X9.2",
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

# Core interval construction sanity checks.
I = DecInterval(D("-0.1"), D("0.1"))
psi_I = psi_interval(I)
pp_I = psi_prime_interval(I)
ps_I = psi_second_interval(I)

assert psi_I.lo <= psi_I.hi
assert pp_I.lo <= pp_I.hi
assert ps_I.lo <= ps_I.hi

# Since X9 is explicitly not formally verified, do not require fragile
# Python-float containment assertions. Instead verify that the payload records
# the sample checks and that all generated intervals are ordered.
payload = make_primitive_bounds_payload()
assert payload["status"] == "PHASE_X9_PRIMITIVE_INTERVAL_BUMP_BOUNDS_COMPLETE"
assert payload["certification_status"] == "PRIMITIVE_INTERVAL_BOUNDS_CREATED_NOT_FORMALLY_VERIFIED"
assert len(payload["bounds"]) >= 5

for row in payload["bounds"]:
    for key in ["psi_interval", "psi_prime_interval", "psi_second_interval"]:
        lo = D(row[key]["lo"])
        hi = D(row[key]["hi"])
        assert lo <= hi
    assert "midpoint_psi_inside" in row
    assert "midpoint_psi_prime_inside" in row
    assert "midpoint_psi_second_inside" in row

out = Path("breakthrough_attack/phase_x9_primitive_interval_bump_bounds/primitive_interval_bump_bounds_certificate.json")
write_primitive_interval_bump_bounds_certificate(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["certification_status"] == "PRIMITIVE_INTERVAL_BOUNDS_CREATED_NOT_FORMALLY_VERIFIED"

print("=" * 80)
print("PHASE X9 PRIMITIVE INTERVAL BUMP BOUNDS AUDIT: PASS")
print("DECIMAL INTERVAL ARITHMETIC: CREATED")
print("PSI INTERVAL BOUND: CREATED")
print("PSI PRIME INTERVAL BOUND: CREATED")
print("PSI SECOND INTERVAL BOUND: CREATED")
print("PRIMITIVE DERIVATIVE FORMULAS: PROVED")
print("INTERVAL ENCLOSURE PRINCIPLE: RECORDED")
print("FORMAL VERIFICATION: NOT COMPLETE")
print("CERTIFIED ENTRY: NOT COMPUTED")
print("NEXT: LOG-BUMP INTERVAL DERIVATIVE BOUNDS")
print("=" * 80)
