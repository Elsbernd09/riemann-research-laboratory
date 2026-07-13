from pathlib import Path
import json

from src.breakthrough_attack.primitive_interval_bump_bounds import D, DecInterval
from src.breakthrough_attack.log_bump_interval_derivative_bounds import (
    log_interval,
    u_interval_for_log_bump,
    log_bump_value_interval,
    log_bump_prime_interval,
    log_bump_second_interval,
    make_log_bump_bounds_payload,
    write_log_bump_interval_derivative_bounds_certificate,
)

files = [
    Path("breakthrough_attack/phase_x10_log_bump_interval_derivative_bounds/PHASE_X10_LOG_BUMP_INTERVAL_DERIVATIVE_BOUNDS.md"),
    Path("breakthrough_attack/phase_x10_log_bump_interval_derivative_bounds/LOG_BUMP_INTERVAL_STATUS.md"),
    Path("breakthrough_attack/phase_x10_log_bump_interval_derivative_bounds/NEXT_PHASE_X11_CORRECTED_BASIS_INTERVAL_DERIVATIVE_BOUNDS.md"),
    Path("src/breakthrough_attack/log_bump_interval_derivative_bounds.py"),
]

required = [
    "PHASE_X10_LOG_BUMP_INTERVAL_DERIVATIVE_BOUNDS_COMPLETE",
    "LOG_INTERVAL_ENCLOSURE_CREATED",
    "LOG_BUMP_VALUE_INTERVAL_CREATED",
    "LOG_BUMP_FIRST_DERIVATIVE_INTERVAL_CREATED",
    "LOG_BUMP_SECOND_DERIVATIVE_INTERVAL_CREATED",
    "LOG_BUMP_DERIVATIVE_FORMULAS_PROVED",
    "LOG_BUMP_INTERVAL_PROPAGATION_PROVED",
    "LOG_BUMP_INTERVAL_BOUNDS_CREATED_NOT_FORMALLY_VERIFIED",
    "CERTIFIED_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X11_CORRECTED_BASIS_INTERVAL_DERIVATIVE_BOUNDS",
    "Theorem X10.1",
    "Theorem X10.2",
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

X = DecInterval(D("0.95"), D("1.05"))
L = log_interval(X)
U = u_interval_for_log_bump(X, D("0.0"), D("0.75"))
V = log_bump_value_interval(X, D("0.0"), D("0.75"))
P = log_bump_prime_interval(X, D("0.0"), D("0.75"))
S = log_bump_second_interval(X, D("0.0"), D("0.75"))

for I in [L, U, V, P, S]:
    assert I.lo <= I.hi

payload = make_log_bump_bounds_payload()
assert payload["status"] == "PHASE_X10_LOG_BUMP_INTERVAL_DERIVATIVE_BOUNDS_COMPLETE"
assert payload["certification_status"] == "LOG_BUMP_INTERVAL_BOUNDS_CREATED_NOT_FORMALLY_VERIFIED"
assert len(payload["bounds"]) == 3

for row in payload["bounds"]:
    for key in ["value_interval", "prime_interval", "second_interval"]:
        assert D(row[key]["lo"]) <= D(row[key]["hi"])

out = Path("breakthrough_attack/phase_x10_log_bump_interval_derivative_bounds/log_bump_interval_derivative_bounds_certificate.json")
write_log_bump_interval_derivative_bounds_certificate(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["certification_status"] == "LOG_BUMP_INTERVAL_BOUNDS_CREATED_NOT_FORMALLY_VERIFIED"

print("=" * 80)
print("PHASE X10 LOG-BUMP INTERVAL DERIVATIVE BOUNDS AUDIT: PASS")
print("LOG INTERVAL ENCLOSURE: CREATED")
print("LOG-BUMP VALUE INTERVAL: CREATED")
print("LOG-BUMP FIRST DERIVATIVE INTERVAL: CREATED")
print("LOG-BUMP SECOND DERIVATIVE INTERVAL: CREATED")
print("DERIVATIVE FORMULAS: PROVED")
print("INTERVAL PROPAGATION: PROVED")
print("FORMAL VERIFICATION: NOT COMPLETE")
print("CERTIFIED ENTRY: NOT COMPUTED")
print("NEXT: CORRECTED BASIS INTERVAL DERIVATIVE BOUNDS")
print("=" * 80)
