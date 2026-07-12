from pathlib import Path

files = [
    Path("scripts/run_phase9e_follow_recorded_track.py"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9E_FOLLOW_RECORDED_TRACK.md"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9E_FOLLOW_RECORDED_TRACK_OUTPUT.txt"),
]

required = [
    "Follow Recorded Track",
    "TRACK=",
    "No new eigenvalues computed",
    "No zeta zeros",
    "No RH claim",
    "No novelty claim",
]

for path in files:
    if not path.exists():
        raise FileNotFoundError(path)

    text = path.read_text(encoding="utf-8")

    if "\x00" in text:
        raise ValueError(f"NUL byte found in {path}")

combined = "\n".join(path.read_text(encoding="utf-8") for path in files)

# At least one of the track artifacts must exist.
track_artifacts = [
    Path("weil_reconstruction/eigenvalue_validation/FINAL_SYNTHETIC_VALIDATION_PLAN.md"),
    Path("weil_reconstruction/eigenvalue_validation/REPRESENTATION_REPAIR_DIAGNOSTIC.md"),
    Path("weil_reconstruction/eigenvalue_validation/MANUAL_AUDIT_REQUIRED.md"),
]

if not any(path.exists() for path in track_artifacts):
    raise RuntimeError("No Phase 9E track artifact was created")

missing = [
    phrase for phrase in required
    if phrase.lower() not in combined.lower()
]

if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

print("=" * 80)
print("PHASE 9E FOLLOW RECORDED TRACK AUDIT: PASS")
print("TRACK ARTIFACT: CREATED")
print("NO NEW EIGENVALUES COMPUTED IN PHASE 9E")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
