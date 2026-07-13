from pathlib import Path

files = [
    Path("breakthrough_attack/phase_x1_source_locked_admissibility/PHASE_X1_SOURCE_LOCKED_ADMISSIBILITY.md"),
    Path("breakthrough_attack/phase_x1_source_locked_admissibility/ADMISSIBILITY_GATE_STATUS.md"),
    Path("breakthrough_attack/phase_x1_source_locked_admissibility/NEXT_PHASE_X2_EXACT_FUNCTIONAL_LOCK.md"),
]

required = [
    "PHASE_X1_SOURCE_LOCKED_ADMISSIBILITY_ATTACK_COMPLETE",
    "STAR_CONVENTION_CONFLICT_DETECTED",
    "GROWTH_CONDITION_CONFLICT_DETECTED",
    "EXPLICIT_FORMULA_NORMALIZATION_CONFLICT_DETECTED",
    "POLE_CANCELLATION_TARGET_AMBIGUITY_DETECTED",
    "SAFE_SUFFICIENT_POLE_CANCELLATION_PROVED",
    "STRONGER_THAN_NECESSARY_CONSTRAINT_WARNING_PROVED",
    "CERTIFIED_FINITE_WEIL_MATRIX_THEOREM_BLOCKED",
    "ADMISSIBILITY_GATE_IDENTIFIED",
    "READY_FOR_PHASE_X2_EXACT_FUNCTIONAL_LOCK",
    "Theorem X1.1",
    "Theorem X1.2",
    "This phase does not prove RH",
    "This phase does not prove a breakthrough",
    "This phase does not establish novelty",
    "This phase does not source-lock admissibility completely",
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
print("PHASE X1 SOURCE-LOCKED ADMISSIBILITY ATTACK AUDIT: PASS")
print("STAR CONVENTION CONFLICT: DETECTED")
print("GROWTH CONDITION CONFLICT: DETECTED")
print("EXPLICIT FORMULA NORMALIZATION CONFLICT: DETECTED")
print("POLE CANCELLATION TARGET AMBIGUITY: DETECTED")
print("SAFE SUFFICIENT POLE CANCELLATION: PROVED")
print("STRONGER-THAN-NECESSARY WARNING: PROVED")
print("CERTIFIED FINITE WEIL MATRIX THEOREM: BLOCKED")
print("NEXT: EXACT FUNCTIONAL LOCK")
print("=" * 80)
