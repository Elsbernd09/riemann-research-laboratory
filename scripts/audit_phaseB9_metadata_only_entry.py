from pathlib import Path
import json

from src.level4.metadata_only_entry import (
    create_m00_metadata_only_payload,
    write_m00_metadata_only_entry,
)
from src.level4.certified_entry_metadata import EntryCertificationStatus

files = [
    Path("breakthrough_push/phase_b9_metadata_only_entry/PHASE_B9_METADATA_ONLY_ENTRY.md"),
    Path("breakthrough_push/phase_b9_metadata_only_entry/METADATA_ONLY_ENTRY_STATUS.md"),
    Path("breakthrough_push/phase_b9_metadata_only_entry/NEXT_PHASE_B10_PROTOTYPE_FLOATING_ENTRY.md"),
    Path("src/level4/metadata_only_entry.py"),
]

required = [
    "PHASE_B9_METADATA_ONLY_ENTRY_COMPLETE",
    "M_00_ARITH_METADATA_OBJECT_CREATED",
    "BOMBIERI_LAGARIAS_NORMALIZATION_USED",
    "METADATA_ONLY_ENTRY_NOT_CERTIFIED",
    "CERTIFIED_MATRIX_CANNOT_USE_METADATA_ONLY_ENTRY",
    "NO_CERTIFIED_VALUE_COMPUTED",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "READY_FOR_PHASE_B10_PROTOTYPE_FLOATING_ENTRY",
    "Theorem B9.1",
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

payload = create_m00_metadata_only_payload()
entry = payload["entry"]
assert payload["status"] == "PHASE_B9_METADATA_ONLY_ENTRY_COMPLETE"
assert entry["entry_id"] == "M_00_arith"
assert entry["basis_i"] == 0 and entry["basis_j"] == 0
assert entry["certification_status"] == EntryCertificationStatus.METADATA_ONLY.value
assert entry["normalization_label"] == "bombieri_lagarias_normalization"
assert "log(pi)" in entry["constant_term"]
assert payload["entry_is_certified"] is False
assert payload["matrix_with_this_entry_is_certified"] is False

out = Path("breakthrough_push/phase_b9_metadata_only_entry/M_00_metadata_only_entry.json")
write_m00_metadata_only_entry(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["status"] == "PHASE_B9_METADATA_ONLY_ENTRY_COMPLETE"
assert saved["boundary"] == "NO_CERTIFIED_VALUE_COMPUTED"

print("=" * 80)
print("PHASE B9 METADATA-ONLY ENTRY AUDIT: PASS")
print("M_00 ARITH METADATA OBJECT: CREATED")
print("BOMBIERI-LAGARIAS NORMALIZATION: USED")
print("ENTRY STATUS: METADATA_ONLY")
print("ENTRY CERTIFIED: FALSE")
print("MATRIX WITH ENTRY CERTIFIED: FALSE")
print("CERTIFIED VALUE COMPUTED: NO")
print("BREAKTHROUGH: NOT ACHIEVED")
print("=" * 80)
