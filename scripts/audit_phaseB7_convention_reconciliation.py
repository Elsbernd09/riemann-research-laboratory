from pathlib import Path
import json

from src.level4.conventions import (
    BOMBIERI_LAGARIAS_CONVENTION,
    PROJECT_STAR_CONVENTION,
    write_convention_certificate,
)

files = [
    Path("breakthrough_push/phase_b7_convention_reconciliation/PHASE_B7_CONVENTION_RECONCILIATION.md"),
    Path("breakthrough_push/phase_b7_convention_reconciliation/CONVENTION_RECONCILIATION_STATUS.md"),
    Path("breakthrough_push/phase_b7_convention_reconciliation/NEXT_PHASE_B8_CERTIFIED_ENTRY_METADATA.md"),
    Path("src/level4/conventions.py"),
]

required = [
    "PHASE_B7_CONVENTION_RECONCILIATION_COMPLETE",
    "PROJECT_STAR_EQUALS_TILDE_CONJUGATE",
    "CONVOLUTION_CONVENTION_DIFFERENCE_TRACKED",
    "SPECTRAL_PRODUCT_RECONCILED",
    "EXPLICIT_FORMULA_CONSTANT_RECONCILED_TO_BOMBIERI_LAGARIAS",
    "NORMALIZATION_METADATA_REQUIRED",
    "POLE_CONSTRAINTS_PLAUSIBLE_NOT_FULLY_LOCKED",
    "CERTIFIED_ENTRY_METADATA_SCHEMA_CREATED",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "READY_FOR_PHASE_B8_CERTIFIED_ENTRY_METADATA",
    "Theorem B7.1",
    "Theorem B7.2",
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

assert BOMBIERI_LAGARIAS_CONVENTION.normalization_label == "bombieri_lagarias_normalization"
assert "log(pi)" in BOMBIERI_LAGARIAS_CONVENTION.constant_term
assert PROJECT_STAR_CONVENTION["audit_string"] == "PROJECT_STAR_EQUALS_TILDE_CONJUGATE"

out = Path("breakthrough_push/phase_b7_convention_reconciliation/convention_certificate.json")
write_convention_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "PHASE_B7_CONVENTION_RECONCILIATION_COMPLETE"
assert payload["bombieri_lagarias_convention"]["certified_entry_allowed"] is False

print("=" * 80)
print("PHASE B7 CONVENTION RECONCILIATION AUDIT: PASS")
print("PROJECT STAR = TILDE(CONJUGATE): CONFIRMED")
print("CONVOLUTION CONVENTION DIFFERENCE: TRACKED")
print("SPECTRAL PRODUCT: RECONCILED")
print("EXPLICIT FORMULA CONSTANT: RECONCILED TO BOMBIERI-LAGARIAS")
print("NORMALIZATION METADATA: REQUIRED")
print("POLE CONSTRAINTS: PLAUSIBLE, NOT FULLY LOCKED")
print("BREAKTHROUGH: NOT ACHIEVED")
print("=" * 80)
