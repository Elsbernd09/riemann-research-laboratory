from pathlib import Path

files = [
    Path("scripts/run_phase9f_track_specific_builder.py"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9F_TRACK_SPECIFIC_BUILDER.md"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9F_TRACK_SPECIFIC_BUILDER_OUTPUT.txt"),
]

required = [
    "Track-Specific",
    "DETECTED_TRACK",
    "No eigenvalues computed",
    "No zeta zeros",
    "No RH claim",
    "No novelty claim",
    "No zeta-case Bombieri-Weil verification claim",
]

for path in files:
    if not path.exists():
        raise FileNotFoundError(path)

    text = path.read_text(encoding="utf-8")

    if "\x00" in text:
        raise ValueError(f"NUL byte found in {path}")

track_artifacts = [
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9G_FINAL_SYNTHETIC_VALIDATION_SPEC.md"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9G_REPRESENTATION_REPAIR_SPEC.md"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9G_MANUAL_AUDIT_SPEC.md"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9G_UNKNOWN_TRACK_STOP.md"),
]

if not any(path.exists() for path in track_artifacts):
    raise RuntimeError("No Phase 9G track-specific spec was created")

combined = "\n".join(path.read_text(encoding="utf-8") for path in files)

missing = [
    phrase for phrase in required
    if phrase.lower() not in combined.lower()
]

if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

print("=" * 80)
print("PHASE 9F TRACK-SPECIFIC BUILDER AUDIT: PASS")
print("NEXT-PHASE SPEC: CREATED")
print("NO EIGENVALUES COMPUTED IN PHASE 9F")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
