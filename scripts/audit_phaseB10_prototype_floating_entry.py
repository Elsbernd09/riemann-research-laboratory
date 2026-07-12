from pathlib import Path
import json
import math

from src.level4.prototype_floating_entry import (
    corrected_constant_component,
    compute_m00_prototype_value,
    make_m00_prototype_entry,
    write_m00_prototype_entry,
)
from src.level4.certified_entry_metadata import EntryCertificationStatus

files = [
    Path("breakthrough_push/phase_b10_prototype_floating_entry/PHASE_B10_PROTOTYPE_FLOATING_ENTRY.md"),
    Path("breakthrough_push/phase_b10_prototype_floating_entry/PROTOTYPE_FLOATING_ENTRY_STATUS.md"),
    Path("breakthrough_push/phase_b10_prototype_floating_entry/NEXT_PHASE_B11_INTERVAL_CANDIDATE_ENTRY.md"),
    Path("src/level4/prototype_floating_entry.py"),
]

required = [
    "PHASE_B10_PROTOTYPE_FLOATING_ENTRY_COMPLETE",
    "M_00_ARITH_PROTOTYPE_FLOATING_ENTRY_CREATED",
    "BOMBIERI_LAGARIAS_CONSTANT_USED",
    "LOG_PI_GAMMA_NORMALIZATION_USED",
    "EARLIER_LOG_4PI_GAMMA_NOT_USED",
    "PROTOTYPE_FLOATING_POINT_ENTRY_NOT_CERTIFIED",
    "NUMERICAL_VALUE_COMPUTED_BUT_NOT_CERTIFIED",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "READY_FOR_PHASE_B11_INTERVAL_CANDIDATE_ENTRY",
    "Theorem B10.1",
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

assert corrected_constant_component(1.0) < 0.0

components = compute_m00_prototype_value(integral_steps=30, conv_steps=30)
for key, value in components.items():
    assert math.isfinite(value), key

payload = make_m00_prototype_entry()
assert payload["status"] == "PHASE_B10_PROTOTYPE_FLOATING_ENTRY_COMPLETE"
entry = payload["entry_metadata"]
assert entry["entry_id"] == "M_00_arith"
assert entry["certification_status"] == EntryCertificationStatus.PROTOTYPE_FLOATING_POINT.value
assert entry["normalization_label"] == "bombieri_lagarias_normalization"
assert "log(pi)" in entry["constant_term"]
assert payload["entry_is_certified"] is False

out = Path("breakthrough_push/phase_b10_prototype_floating_entry/M_00_prototype_floating_entry.json")
write_m00_prototype_entry(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["status"] == "PHASE_B10_PROTOTYPE_FLOATING_ENTRY_COMPLETE"
assert saved["normalization_check"]["used"] == "LOG_PI_GAMMA_NORMALIZATION_USED"
assert saved["normalization_check"]["not_used"] == "EARLIER_LOG_4PI_GAMMA_NOT_USED"

print("=" * 80)
print("PHASE B10 PROTOTYPE FLOATING ENTRY AUDIT: PASS")
print("M_00 PROTOTYPE FLOATING ENTRY: CREATED")
print("BOMBIERI-LAGARIAS CONSTANT: USED")
print("LOG_PI_GAMMA NORMALIZATION: USED")
print("EARLIER LOG_4PI_GAMMA: NOT USED")
print("NUMERICAL VALUE: COMPUTED BUT NOT CERTIFIED")
print("ENTRY CERTIFIED: FALSE")
print("BREAKTHROUGH: NOT ACHIEVED")
print("=" * 80)
