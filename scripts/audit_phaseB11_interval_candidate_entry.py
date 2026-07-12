from pathlib import Path
import json
import math

from src.level4.interval_candidate_entry import (
    conservative_radius_from_components,
    make_m00_interval_candidate_entry,
    write_m00_interval_candidate_entry,
)
from src.level4.certified_entry_metadata import EntryCertificationStatus

files = [
    Path("breakthrough_push/phase_b11_interval_candidate_entry/PHASE_B11_INTERVAL_CANDIDATE_ENTRY.md"),
    Path("breakthrough_push/phase_b11_interval_candidate_entry/INTERVAL_CANDIDATE_ENTRY_STATUS.md"),
    Path("breakthrough_push/phase_b11_interval_candidate_entry/NEXT_PHASE_B12_CERTIFIED_ERROR_BOUND_AUDIT.md"),
    Path("src/level4/interval_candidate_entry.py"),
]

required = [
    "PHASE_B11_INTERVAL_CANDIDATE_ENTRY_COMPLETE",
    "M_00_ARITH_INTERVAL_CANDIDATE_CREATED",
    "INTERVAL_CANDIDATE_STATUS_USED",
    "CONSERVATIVE_INTERVAL_WRAPPER_CREATED",
    "ERROR_GATES_RECORDED",
    "INTERVAL_CANDIDATE_ENTRY_NOT_CERTIFIED",
    "CERTIFIED_MATRIX_CANNOT_USE_INTERVAL_CANDIDATE",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "READY_FOR_PHASE_B12_CERTIFIED_ERROR_BOUND_AUDIT",
    "Theorem B11.1",
    "Theorem B11.2",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a breakthrough",
    "This phase does not prove novelty",
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

assert conservative_radius_from_components({"entry_value": 0.0}) >= 1.0

payload = make_m00_interval_candidate_entry()
assert payload["status"] == "PHASE_B11_INTERVAL_CANDIDATE_ENTRY_COMPLETE"
entry = payload["entry_metadata"]
assert entry["entry_id"] == "M_00_arith"
assert entry["certification_status"] == EntryCertificationStatus.INTERVAL_CANDIDATE.value
assert entry["normalization_label"] == "bombieri_lagarias_normalization"
assert "log(pi)" in entry["constant_term"]
assert payload["entry_is_certified"] is False
assert payload["matrix_with_this_entry_is_certified"] is False

interval = payload["candidate_interval"]
assert len(interval) == 2
assert interval[0] <= payload["prototype_value"] <= interval[1]
assert payload["candidate_radius"] > 0
assert all(math.isfinite(x) for x in interval)

out = Path("breakthrough_push/phase_b11_interval_candidate_entry/M_00_interval_candidate_entry.json")
write_m00_interval_candidate_entry(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["status"] == "PHASE_B11_INTERVAL_CANDIDATE_ENTRY_COMPLETE"
assert saved["entry_is_certified"] is False

print("=" * 80)
print("PHASE B11 INTERVAL CANDIDATE ENTRY AUDIT: PASS")
print("M_00 INTERVAL CANDIDATE: CREATED")
print("CONSERVATIVE INTERVAL: CREATED")
print("ERROR GATES: RECORDED")
print("ENTRY CERTIFIED: FALSE")
print("MATRIX WITH ENTRY CERTIFIED: FALSE")
print("BREAKTHROUGH: NOT ACHIEVED")
print("=" * 80)
