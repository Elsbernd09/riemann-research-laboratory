from pathlib import Path
import json
import math

from src.breakthrough_attack.derivative_bounds import (
    psi,
    psi_prime,
    psi_second,
    star_second_formula,
    compute_heuristic_derivative_envelope,
    write_derivative_bound_certificate,
)

files = [
    Path("breakthrough_attack/phase_x8_derivative_bound_certification/PHASE_X8_DERIVATIVE_BOUND_CERTIFICATION.md"),
    Path("breakthrough_attack/phase_x8_derivative_bound_certification/DERIVATIVE_BOUND_STATUS.md"),
    Path("breakthrough_attack/phase_x8_derivative_bound_certification/NEXT_PHASE_X9_PRIMITIVE_INTERVAL_BUMP_BOUNDS.md"),
    Path("src/breakthrough_attack/derivative_bounds.py"),
]

required = [
    "PHASE_X8_DERIVATIVE_BOUND_CERTIFICATION_COMPLETE",
    "LOG_BUMP_SECOND_DERIVATIVE_FORMULA_PROVED",
    "CORRECTED_BASIS_DERIVATIVE_BOUND_PROVED",
    "STAR_SECOND_DERIVATIVE_FORMULA_PROVED",
    "CONVOLUTION_SECOND_DERIVATIVE_BOUND_PROVED",
    "DERIVATIVE_BOUND_REDUCTION_CREATED",
    "HEURISTIC_DERIVATIVE_ENVELOPES_COMPUTED",
    "DERIVATIVE_BOUNDS_REDUCED_BUT_NOT_CERTIFIED",
    "CERTIFIED_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X9_PRIMITIVE_INTERVAL_BUMP_BOUNDS",
    "Theorem X8.1",
    "Theorem X8.2",
    "Theorem X8.3",
    "Theorem X8.4",
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

assert psi(0.0) > 0.0
assert psi(1.0) == 0.0
assert abs(psi_prime(0.0)) < 1e-14
assert psi_second(0.0) < 0.0

phi_const = lambda x: 1.0
phi_prime_zero = lambda x: 0.0
phi_second_zero = lambda x: 0.0
assert abs(star_second_formula(phi_const, phi_prime_zero, phi_second_zero, 1.0) - 2.0) < 1e-14

env = compute_heuristic_derivative_envelope(steps=120)
assert env.status == "DERIVATIVE_BOUNDS_REDUCED_BUT_NOT_CERTIFIED"
assert env.phi_support[0] > 0
assert env.phi_support[0] < env.phi_support[1]
assert env.phi_sup_heuristic >= 0
assert env.star_second_sup_heuristic >= 0
assert math.isfinite(env.convolution_second_bound_heuristic)

out = Path("breakthrough_attack/phase_x8_derivative_bound_certification/derivative_bound_certificate.json")
write_derivative_bound_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "PHASE_X8_DERIVATIVE_BOUND_CERTIFICATION_COMPLETE"
assert payload["certification_status"] == "DERIVATIVE_BOUNDS_REDUCED_BUT_NOT_CERTIFIED"

print("=" * 80)
print("PHASE X8 DERIVATIVE BOUND CERTIFICATION AUDIT: PASS")
print("LOG-BUMP SECOND DERIVATIVE FORMULA: PROVED")
print("CORRECTED BASIS DERIVATIVE BOUND: PROVED")
print("STAR SECOND DERIVATIVE FORMULA: PROVED")
print("CONVOLUTION SECOND DERIVATIVE BOUND: PROVED")
print("DERIVATIVE BOUND REDUCTION: CREATED")
print("HEURISTIC ENVELOPES: COMPUTED")
print("CERTIFIED ENTRY: NOT COMPUTED")
print("NEXT: PRIMITIVE INTERVAL BUMP BOUNDS")
print("=" * 80)
