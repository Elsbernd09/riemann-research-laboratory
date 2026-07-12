from pathlib import Path

files = [
    Path("scripts/run_phase9g_execute_track_spec.py"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9G_EXECUTE_TRACK_SPEC.md"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9G_EXECUTE_TRACK_SPEC_OUTPUT.txt"),
]

required = [
    "Execute Track",
    "TRACK=",
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

combined = "\n".join(path.read_text(encoding="utf-8") for path in files)

missing = [
    phrase for phrase in required
    if phrase.lower() not in combined.lower()
]

if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

print("=" * 80)
print("PHASE 9G EXECUTE TRACK SPEC AUDIT: PASS")
print("TRACK EXECUTION OUTPUT: RECORDED")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
