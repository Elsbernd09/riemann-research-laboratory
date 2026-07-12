from __future__ import annotations

from pathlib import Path
import json
from typing import Any, Dict

from src.level4.certified_entry_metadata import (
    EntryCertificationStatus,
    make_metadata_only_entry,
    matrix_is_certified,
)


def create_m00_metadata_only_payload() -> Dict[str, Any]:
    entry = make_metadata_only_entry("M_00_arith", 0, 0)
    return {
        "phase": "B9",
        "status": "PHASE_B9_METADATA_ONLY_ENTRY_COMPLETE",
        "entry": entry.to_dict(),
        "entry_is_certified": entry.is_certified_interval_entry(),
        "matrix_with_this_entry_is_certified": matrix_is_certified([entry]),
        "boundary": "NO_CERTIFIED_VALUE_COMPUTED",
        "audit_strings": [
            "PHASE_B9_METADATA_ONLY_ENTRY_COMPLETE",
            "M_00_ARITH_METADATA_OBJECT_CREATED",
            "BOMBIERI_LAGARIAS_NORMALIZATION_USED",
            "METADATA_ONLY_ENTRY_NOT_CERTIFIED",
            "CERTIFIED_MATRIX_CANNOT_USE_METADATA_ONLY_ENTRY",
            "NO_CERTIFIED_VALUE_COMPUTED",
            "BREAKTHROUGH_NOT_ACHIEVED",
            "READY_FOR_PHASE_B10_PROTOTYPE_FLOATING_ENTRY",
        ],
    }


def write_m00_metadata_only_entry(path: Path) -> None:
    payload = create_m00_metadata_only_payload()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    write_m00_metadata_only_entry(
        Path("breakthrough_push/phase_b9_metadata_only_entry/M_00_metadata_only_entry.json")
    )
    print("Wrote M_00 metadata-only entry")
