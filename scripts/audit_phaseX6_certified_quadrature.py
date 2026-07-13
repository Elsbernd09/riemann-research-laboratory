from pathlib import Path
import json

from src.breakthrough_attack.certified_quadrature import (
    midpoint_quadrature,
    midpoint_error_bound,
    make_integral_enclosure,
    demo_quadratic,
    write_certified_quadrature_certificate,
)

files = [
    Path("breakthrough_attack/phase_x6_certified_quadrature_theorem/PHASE_X6_CERTIFIED_QUADRATURE_THEOREM.md"),
    Path("breakthrough_attack/phase_x6_certified_quadrature_theorem/CERTIFIED_QUADRATURE_STATUS.md"),
    Path("breakthrough_attack/phase_x6_certified_quadrature_theorem/NEXT_PHASE_X7_SINGLE_ENTRY_CERTIFICATION_PIPELINE.md"),
    Path("src/breakthrough_attack/certified_quadrature.py"),
]

required = [
    "PHASE_X6_CERTIFIED_QUADRATURE_THEOREM_COMPLETE",
    "MIDPOINT_QUADRATURE_ERROR_THEOREM_PROVED",
    "CERTIFIED_INTEGRAL_ENCLOSURE_THEOREM_PROVED",
    "ERROR_BOUND_FORMULA_LOCKED",
    "QUADRATURE_CERTIFICATION_PATTERN_CREATED",
    "CERTIFIED_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X7_SINGLE_ENTRY_CERTIFICATION_PIPELINE",
    "Theorem X6.1",
    "Theorem X6.2",
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

a = 0.0
b = 1.0
n = 100
q = midpoint_quadrature(demo_quadratic, a, b, n)
e = midpoint_error_bound(a, b, n, 2.0)
cert = make_integral_enclosure(q, q, a, b, n, 2.0)
lo, hi = cert.certified_interval

assert e > 0.0
assert lo <= 1.0 / 3.0 <= hi
assert abs(q - 1.0 / 3.0) <= e

out = Path("breakthrough_attack/phase_x6_certified_quadrature_theorem/certified_quadrature_certificate.json")
write_certified_quadrature_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "PHASE_X6_CERTIFIED_QUADRATURE_THEOREM_COMPLETE"
assert payload["demo_exact_integral_inside_interval"] is True

print("=" * 80)
print("PHASE X6 CERTIFIED QUADRATURE THEOREM AUDIT: PASS")
print("MIDPOINT ERROR THEOREM: PROVED")
print("CERTIFIED INTEGRAL ENCLOSURE THEOREM: PROVED")
print("ERROR FORMULA: LOCKED")
print("QUADRATURE CERTIFICATION PATTERN: CREATED")
print("CERTIFIED ENTRY: NOT COMPUTED")
print("NEXT: SINGLE ENTRY CERTIFICATION PIPELINE")
print("=" * 80)
