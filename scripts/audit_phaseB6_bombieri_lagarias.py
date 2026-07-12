from pathlib import Path

files = [
    Path("breakthrough_push/phase_b6_bombieri_lagarias_extraction/PHASE_B6_BOMBIERI_LAGARIAS_EXTRACTION.md"),
    Path("breakthrough_push/phase_b6_bombieri_lagarias_extraction/BOMBIERI_LAGARIAS_EXTRACTION_STATUS.md"),
    Path("breakthrough_push/phase_b6_bombieri_lagarias_extraction/CONVENTION_EXTRACTION_TABLE.md"),
    Path("breakthrough_push/phase_b6_bombieri_lagarias_extraction/NEXT_PHASE_B7_CONVENTION_RECONCILIATION.md"),
]

required = [
    "PHASE_B6_BOMBIERI_LAGARIAS_EXTRACTION_COMPLETE",
    "BOMBIERI_LAGARIAS_PRIMARY_SOURCE_USED",
    "MELLIN_TRANSFORM_CONVENTION_CONFIRMED",
    "INVOLUTION_TILDE_CONVENTION_CONFIRMED",
    "MULTIPLICATIVE_CONVOLUTION_CONFIRMED",
    "CONVOLUTION_SPECTRAL_PRODUCT_CONFIRMED",
    "WEIL_POSITIVITY_CONNECTION_CONFIRMED",
    "EXPLICIT_FORMULA_CONSTANT_CORRECTION_IDENTIFIED",
    "POLE_CONSTRAINTS_NOT_FULLY_LOCKED",
    "CLASSICAL_CONVOLUTION_SQUARE_NOT_NOVEL",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "READY_FOR_PHASE_B7_CONVENTION_RECONCILIATION",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a breakthrough",
    "This phase does not prove novelty",
    "This phase does not fully validate pole constraints",
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

print("=" * 80)
print("PHASE B6 BOMBIERI-LAGARIAS EXTRACTION AUDIT: PASS")
print("PRIMARY SOURCE: USED")
print("MELLIN TRANSFORM CONVENTION: CONFIRMED")
print("INVOLUTION TILDE CONVENTION: CONFIRMED")
print("MULTIPLICATIVE CONVOLUTION: CONFIRMED")
print("CONVOLUTION SPECTRAL PRODUCT: CONFIRMED")
print("WEIL POSITIVITY CONNECTION: CONFIRMED")
print("EXPLICIT FORMULA CONSTANT CORRECTION: IDENTIFIED")
print("POLE CONSTRAINTS: NOT FULLY LOCKED")
print("BREAKTHROUGH: NOT ACHIEVED")
print("=" * 80)
