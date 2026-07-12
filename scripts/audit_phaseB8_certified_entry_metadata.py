from pathlib import Path
import json

from src.level4.certified_entry_metadata import (
    EntryCertificationStatus,
    ErrorDecomposition,
    make_metadata_only_entry,
    matrix_is_certified,
    write_metadata_schema_certificate,
)

files = [
    Path("breakthrough_push/phase_b8_certified_entry_metadata/PHASE_B8_CERTIFIED_ENTRY_METADATA.md"),
    Path("breakthrough_push/phase_b8_certified_entry_metadata/CERTIFIED_ENTRY_METADATA_STATUS.md"),
    Path("breakthrough_push/phase_b8_certified_entry_metadata/NEXT_PHASE_B9_METADATA_ONLY_ENTRY.md"),
    Path("src/level4/certified_entry_metadata.py"),
]

required = [
    "PHASE_B8_CERTIFIED_ENTRY_METADATA_COMPLETE",
    "CERTIFIED_ENTRY_METADATA_SCHEMA_CREATED",
    "ENTRY_CERTIFICATION_STATUS_LEVELS_DEFINED",
    "METADATA_ONLY_STATUS_DEFINED",
    "PROTOTYPE_FLOATING_POINT_STATUS_DEFINED",
    "INTERVAL_CANDIDATE_STATUS_DEFINED",
    "CERTIFIED_INTERVAL_ENTRY_STATUS_DEFINED",
    "CERTIFIED_MATRIX_REQUIRES_ALL_CERTIFIED_ENTRIES",
    "NORMALIZATION_REQUIRED_FOR_CERTIFICATION",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "READY_FOR_PHASE_B9_METADATA_ONLY_ENTRY",
    "Theorem B8.1",
    "Theorem B8.2",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a breakthrough",
    "This phase does not prove novelty",
    "This phase does not compute certified arithmetic entries",
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

assert EntryCertificationStatus.METADATA_ONLY.value == "METADATA_ONLY"
assert EntryCertificationStatus.PROTOTYPE_FLOATING_POINT.value == "PROTOTYPE_FLOATING_POINT"
assert EntryCertificationStatus.INTERVAL_CANDIDATE.value == "INTERVAL_CANDIDATE"
assert EntryCertificationStatus.CERTIFIED_INTERVAL_ENTRY.value == "CERTIFIED_INTERVAL_ENTRY"

entry = make_metadata_only_entry("M_00_arith", 0, 0)
assert entry.certification_status == EntryCertificationStatus.METADATA_ONLY
assert not entry.is_certified_interval_entry()
assert not matrix_is_certified([entry])
assert entry.normalization_label == "bombieri_lagarias_normalization"
assert "log(pi)" in entry.constant_term

out = Path("breakthrough_push/phase_b8_certified_entry_metadata/metadata_schema_certificate.json")
write_metadata_schema_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "PHASE_B8_CERTIFIED_ENTRY_METADATA_COMPLETE"
assert payload["example_is_certified"] is False
assert payload["certified_matrix_rule_example"] is False

print("=" * 80)
print("PHASE B8 CERTIFIED ENTRY METADATA AUDIT: PASS")
print("METADATA SCHEMA: CREATED")
print("STATUS LEVELS: DEFINED")
print("CERTIFIED MATRIX RULE: ENFORCED")
print("NORMALIZATION METADATA: REQUIRED")
print("EXAMPLE METADATA-ONLY ENTRY: CREATED")
print("BREAKTHROUGH: NOT ACHIEVED")
print("=" * 80)
