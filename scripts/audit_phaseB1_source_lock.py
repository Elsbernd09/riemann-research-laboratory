from pathlib import Path

files = [
    Path("breakthrough_push/phase_b1_source_lock/PHASE_B1_PROVISIONAL_SOURCE_LOCK.md"),
    Path("breakthrough_push/phase_b1_source_lock/SOURCE_LOCK_STATUS.md"),
    Path("breakthrough_push/phase_b1_source_lock/NEXT_PHASE_B2_ADMISSIBLE_SUBSPACE.md"),
]

required = [
    "PHASE_B1_PROVISIONAL_SOURCE_LOCK_COMPLETE",
    "WEIL_STAR_CONVENTION_IMPORTED_PROVISIONALLY",
    "MULTIPLICATIVE_CONVOLUTION_IMPORTED_PROVISIONALLY",
    "MELLIN_PRODUCT_IDENTITY_SOURCE_CONFIRMED_PROVISIONALLY",
    "POSITIVITY_CONDITION_IMPORTED_PROVISIONALLY",
    "POLE_ORTHOGONALITY_CONSTRAINTS_IDENTIFIED",
    "FINITE_ADMISSIBLE_SUBSPACE_THEOREM_PROVED",
    "PRIMARY_SOURCE_EXTRACTION_STILL_REQUIRED",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "READY_FOR_PHASE_B2_ADMISSIBLE_SUBSPACE",
    "Theorem B1.1",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a breakthrough",
    "This phase does not prove novelty",
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
print("PHASE B1 PROVISIONAL SOURCE LOCK AUDIT: PASS")
print("WEIL STAR CONVENTION: IMPORTED PROVISIONALLY")
print("MULTIPLICATIVE CONVOLUTION: IMPORTED PROVISIONALLY")
print("MELLIN PRODUCT IDENTITY: CONFIRMED PROVISIONALLY")
print("POSITIVITY CONDITION: IMPORTED PROVISIONALLY")
print("POLE ORTHOGONALITY CONSTRAINTS: IDENTIFIED")
print("FINITE ADMISSIBLE SUBSPACE THEOREM: PROVED")
print("PRIMARY SOURCE EXTRACTION: STILL REQUIRED")
print("BREAKTHROUGH: NOT ACHIEVED")
print("=" * 80)
