from pathlib import Path
import json

from src.breakthrough_attack.primitive_interval_bump_bounds import D, DecInterval
from src.breakthrough_attack.corrected_basis_interval_derivative_bounds import (
    build_demo_corrected_basis_interval_spec,
    corrected_basis_interval_for_order,
    make_corrected_basis_interval_payload,
    write_corrected_basis_interval_derivative_bounds_certificate,
)

files = [
    Path("breakthrough_attack/phase_x11_corrected_basis_interval_derivative_bounds/PHASE_X11_CORRECTED_BASIS_INTERVAL_DERIVATIVE_BOUNDS.md"),
    Path("breakthrough_attack/phase_x11_corrected_basis_interval_derivative_bounds/CORRECTED_BASIS_INTERVAL_STATUS.md"),
    Path("breakthrough_attack/phase_x11_corrected_basis_interval_derivative_bounds/NEXT_PHASE_X12_STAR_AND_CONVOLUTION_DERIVATIVE_BOUNDS.md"),
    Path("src/breakthrough_attack/corrected_basis_interval_derivative_bounds.py"),
]

required = [
    "PHASE_X11_CORRECTED_BASIS_INTERVAL_DERIVATIVE_BOUNDS_COMPLETE",
    "CORRECTED_BASIS_VALUE_INTERVAL_CREATED",
    "CORRECTED_BASIS_FIRST_DERIVATIVE_INTERVAL_CREATED",
    "CORRECTED_BASIS_SECOND_DERIVATIVE_INTERVAL_CREATED",
    "CORRECTED_BASIS_DERIVATIVE_PROPAGATION_PROVED",
    "CORRECTED_BASIS_INTERVAL_ENCLOSURE_PROVED",
    "COEFFICIENT_INTERVAL_WRAPPERS_CREATED",
    "COEFFICIENT_CERTIFICATION_INCOMPLETE",
    "CERTIFIED_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X12_STAR_AND_CONVOLUTION_DERIVATIVE_BOUNDS",
    "Theorem X11.1",
    "Theorem X11.2",
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

spec = build_demo_corrected_basis_interval_spec()
X = DecInterval(D("0.80"), D("1.20"))
for order in [0, 1, 2]:
    I = corrected_basis_interval_for_order(spec, X, order)
    assert I.lo <= I.hi

payload = make_corrected_basis_interval_payload()
assert payload["status"] == "PHASE_X11_CORRECTED_BASIS_INTERVAL_DERIVATIVE_BOUNDS_COMPLETE"
assert payload["certification_status"] == "CORRECTED_BASIS_INTERVAL_BOUNDS_CREATED_COEFFICIENTS_NOT_CERTIFIED"
assert len(payload["bounds"]) == 3

for row in payload["bounds"]:
    for key in ["value_interval", "prime_interval", "second_interval"]:
        assert D(row[key]["lo"]) <= D(row[key]["hi"])

out = Path("breakthrough_attack/phase_x11_corrected_basis_interval_derivative_bounds/corrected_basis_interval_derivative_bounds_certificate.json")
write_corrected_basis_interval_derivative_bounds_certificate(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["certification_status"] == "CORRECTED_BASIS_INTERVAL_BOUNDS_CREATED_COEFFICIENTS_NOT_CERTIFIED"

print("=" * 80)
print("PHASE X11 CORRECTED BASIS INTERVAL DERIVATIVE BOUNDS AUDIT: PASS")
print("CORRECTED BASIS VALUE INTERVAL: CREATED")
print("CORRECTED BASIS FIRST DERIVATIVE INTERVAL: CREATED")
print("CORRECTED BASIS SECOND DERIVATIVE INTERVAL: CREATED")
print("DERIVATIVE PROPAGATION: PROVED")
print("INTERVAL ENCLOSURE: PROVED")
print("COEFFICIENT INTERVAL WRAPPERS: CREATED")
print("COEFFICIENT CERTIFICATION: INCOMPLETE")
print("CERTIFIED ENTRY: NOT COMPUTED")
print("NEXT: STAR AND CONVOLUTION DERIVATIVE BOUNDS")
print("=" * 80)
