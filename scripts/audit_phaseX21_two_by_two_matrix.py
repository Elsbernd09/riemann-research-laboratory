from pathlib import Path
from decimal import Decimal
import json

from src.breakthrough_attack.two_by_two_matrix_certificate_candidate import (
    DecimalInterval,
    determinant_2x2,
    compute_two_by_two_matrix_certificate_candidate,
    write_two_by_two_matrix_certificate_candidate,
)

files = [
    Path("breakthrough_attack/phase_x21_two_by_two_matrix_certificate_candidate/PHASE_X21_TWO_BY_TWO_MATRIX_CERTIFICATE_CANDIDATE.md"),
    Path("breakthrough_attack/phase_x21_two_by_two_matrix_certificate_candidate/TWO_BY_TWO_MATRIX_STATUS.md"),
    Path("breakthrough_attack/phase_x21_two_by_two_matrix_certificate_candidate/NEXT_PHASE_X22_FINAL_BREAKTHROUGH_CANDIDATE_VERDICT.md"),
    Path("src/breakthrough_attack/two_by_two_matrix_certificate_candidate.py"),
]

required = [
    "PHASE_X21_TWO_BY_TWO_MATRIX_CERTIFICATE_CANDIDATE_COMPLETE",
    "FULL_M00_INTERVAL_IMPORTED",
    "TWO_BY_TWO_INTERVAL_MATRIX_CREATED",
    "HERMITIAN_CONSISTENCY_CHECK_CREATED",
    "TRACE_INTERVAL_CREATED",
    "DETERMINANT_INTERVAL_CREATED",
    "TWO_BY_TWO_MATRIX_CERTIFICATE_CANDIDATE_NOT_FULLY_CERTIFIED",
    "CERTIFIED_FINITE_WEIL_MATRIX_NOT_COMPUTED",
    "NO_BREAKTHROUGH_YET",
    "READY_FOR_PHASE_X22_FINAL_BREAKTHROUGH_CANDIDATE_VERDICT",
    "Theorem X21.1",
    "Theorem X21.2",
    "This phase does not prove RH",
    "This phase does not prove a breakthrough",
    "This phase does not establish novelty",
    "This phase does not compute a certified finite Weil matrix",
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

one = DecimalInterval.point(1)
two = DecimalInterval.point(2)
three = DecimalInterval.point(3)
four = DecimalInterval.point(4)
det = determinant_2x2(one, two, three, four)
assert det.lo == Decimal("-2")
assert det.hi == Decimal("-2")

cert = compute_two_by_two_matrix_certificate_candidate()
assert cert.certification_status == "TWO_BY_TWO_MATRIX_CERTIFICATE_CANDIDATE_NOT_FULLY_CERTIFIED"
assert cert.hermitian_consistency is True
assert len(cert.matrix_entries) == 2
assert len(cert.matrix_entries[0]) == 2
assert "finite-to-Weil positivity theorem" in cert.unresolved_gates

out = Path("breakthrough_attack/phase_x21_two_by_two_matrix_certificate_candidate/two_by_two_matrix_certificate_candidate.json")
write_two_by_two_matrix_certificate_candidate(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["status"] == "PHASE_X21_TWO_BY_TWO_MATRIX_CERTIFICATE_CANDIDATE_COMPLETE"
assert saved["certified_finite_weil_matrix"] is False
assert saved["breakthrough_status"] == "NO_BREAKTHROUGH_YET"

print("=" * 80)
print("PHASE X21 TWO-BY-TWO MATRIX CERTIFICATE CANDIDATE AUDIT: PASS")
print("FULL M00 INTERVAL: IMPORTED")
print("TWO-BY-TWO INTERVAL MATRIX: CREATED")
print("HERMITIAN CONSISTENCY CHECK: CREATED")
print("TRACE INTERVAL: CREATED")
print("DETERMINANT INTERVAL: CREATED")
print("CERTIFIED FINITE WEIL MATRIX: NOT COMPUTED")
print("BREAKTHROUGH STATUS: NO BREAKTHROUGH YET")
print("NEXT: FINAL BREAKTHROUGH-CANDIDATE VERDICT")
print("=" * 80)
