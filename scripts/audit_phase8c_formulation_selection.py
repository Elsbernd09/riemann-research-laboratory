from pathlib import Path

files = [
    Path("weil_reconstruction/formulations/PHASE_8C_EXACT_FORMULATION_SELECTION.md"),
    Path("weil_reconstruction/formulations/SELECTED_FORMULATION.md"),
    Path("weil_reconstruction/formulations/REJECTED_STARTING_POINTS.md"),
]

required = [
    "Exact Classical Formulation Selection",
    "Bombieri-style Weil quadratic form reconstruction",
    "not a proof of RH",
    "not a new Weil criterion",
    "Rejected",
    "No more arbitrary toy models",
    "finite truncation model",
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
print("PHASE 8C FORMULATION SELECTION AUDIT: PASS")
print("SELECTED PATH: BOMBIERI-STYLE WEIL QUADRATIC FORM")
print("REJECTED STARTING POINTS: RECORDED")
print("TOY-MATRIX FREEZE: RECORDED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
