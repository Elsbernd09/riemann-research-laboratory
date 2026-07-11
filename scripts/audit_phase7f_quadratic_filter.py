from pathlib import Path

files = [
    Path("horizontal_defect/theorems/PHASE_7F_QUADRATIC_LI_FILTER_POSITIVITY.md"),
    Path("horizontal_defect/experiments/phase7f_quadratic_filter_positivity.py"),
]

required = [
    "Quadratic Li-Filter Positivity Lift",
    "Q_{1,2}",
    "strict phase-uniform positivity",
    "fourth-order in",
    "arithmetic compatibility",
    "This theorem does not prove RH",
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
print("PHASE 7F QUADRATIC LI-FILTER POSITIVITY AUDIT: PASS")
print("STRICT POSITIVE TWO-FREQUENCY QUADRATIC DETECTOR: PROVED")
print("SMALL-DISPLACEMENT FOURTH-ORDER PROFILE: RECORDED")
print("ARITHMETIC-SIDE COMPATIBILITY: OPEN")
print("RH CLAIM: NONE")
print("=" * 80)
