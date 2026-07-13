from pathlib import Path
import json
import math

from src.breakthrough_attack.single_entry_pipeline import (
    is_prime,
    von_mangoldt,
    build_phi0,
    compute_single_entry_pipeline,
    write_single_entry_pipeline_certificate,
)

files = [
    Path("breakthrough_attack/phase_x7_single_entry_certification_pipeline/PHASE_X7_SINGLE_ENTRY_CERTIFICATION_PIPELINE.md"),
    Path("breakthrough_attack/phase_x7_single_entry_certification_pipeline/SINGLE_ENTRY_PIPELINE_STATUS.md"),
    Path("breakthrough_attack/phase_x7_single_entry_certification_pipeline/NEXT_PHASE_X8_DERIVATIVE_BOUND_CERTIFICATION.md"),
    Path("src/breakthrough_attack/single_entry_pipeline.py"),
]

required = [
    "PHASE_X7_SINGLE_ENTRY_CERTIFICATION_PIPELINE_COMPLETE",
    "SINGLE_ENTRY_PIPELINE_CREATED",
    "LOCKED_T_BL_COMPONENTS_ASSEMBLED",
    "FINITE_PRIME_SIDE_COMPUTABLE_PROVED",
    "ARCHIMEDEAN_CONTINUOUS_EXTENSION_USED",
    "QUADRATURE_CERTIFICATION_PATTERN_USED",
    "CERTIFICATION_INCOMPLETE_STATUS_ASSIGNED",
    "DERIVATIVE_BOUND_BLOCKER_IDENTIFIED",
    "CERTIFIED_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X8_DERIVATIVE_BOUND_CERTIFICATION",
    "Theorem X7.1",
    "Theorem X7.2",
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

assert is_prime(2)
assert is_prime(3)
assert not is_prime(1)
assert not is_prime(4)
assert abs(von_mangoldt(4) - math.log(2)) < 1e-14
assert abs(von_mangoldt(8) - math.log(2)) < 1e-14
assert von_mangoldt(12) == 0.0

phi0 = build_phi0()
lo, hi = phi0.support_x()
assert lo > 0
assert lo < hi

result = compute_single_entry_pipeline(integral_steps=80, conv_steps=80)
assert result.status == "PHASE_X7_SINGLE_ENTRY_CERTIFICATION_PIPELINE_COMPLETE"
assert result.certification_status == "CERTIFICATION_INCOMPLETE"
assert result.derivative_bounds_available is False
assert result.finite_prime_cutoff >= 1
assert math.isfinite(result.entry_value_prototype)
assert len(result.unresolved_blockers) >= 3

out = Path("breakthrough_attack/phase_x7_single_entry_certification_pipeline/single_entry_pipeline_certificate.json")
write_single_entry_pipeline_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "PHASE_X7_SINGLE_ENTRY_CERTIFICATION_PIPELINE_COMPLETE"
assert payload["certification_status"] == "CERTIFICATION_INCOMPLETE"

print("=" * 80)
print("PHASE X7 SINGLE ENTRY CERTIFICATION PIPELINE AUDIT: PASS")
print("SINGLE ENTRY PIPELINE: CREATED")
print("LOCKED T_BL COMPONENTS: ASSEMBLED")
print("FINITE PRIME SIDE: COMPUTABLE")
print("ARCHIMEDEAN CONTINUOUS EXTENSION: USED")
print("QUADRATURE CERTIFICATION PATTERN: USED")
print("CERTIFICATION STATUS: INCOMPLETE")
print("DERIVATIVE BOUND BLOCKER: IDENTIFIED")
print("CERTIFIED ENTRY: NOT COMPUTED")
print("NEXT: DERIVATIVE BOUND CERTIFICATION")
print("=" * 80)
