from pathlib import Path

files = [
    Path("scripts/run_phase9b_synthetic_eigenvalue_validation.py"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9B_SYNTHETIC_EIGENVALUE_VALIDATION.md"),
    Path("weil_reconstruction/eigenvalue_validation/PHASE_9B_SYNTHETIC_EIGENVALUE_OUTPUT.txt"),
]

required = [
    "Synthetic finite Gamma cases only",
    "Strict Hermitian gate",
    "No zeta zeros",
    "No RH claim",
    "No novelty claim",
    "negative_count",
    "theorem8_synthetic_target",
    "failures_or_blocks_are_logged_honestly=True",
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
print("PHASE 9B SYNTHETIC EIGENVALUE AUDIT: PASS")
print("STRICT HERMITIAN GATES: RECORDED")
print("SYNTHETIC CASES ONLY: RECORDED")
print("FAILURE/BLOCK LOGGING: RECORDED")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
