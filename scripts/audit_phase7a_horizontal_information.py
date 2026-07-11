from pathlib import Path

files = [
    Path("horizontal_defect/PHASE_7A_HORIZONTAL_INFORMATION_AUDIT.md"),
    Path("horizontal_defect/HORIZONTAL_DEFECT_PROGRAM.md"),
    Path("horizontal_defect/CANDIDATE_OBJECTS.md"),
]

required = [
    "horizontal",
    "beta",
    "Horizontally blind",
    "Explicit-formula compatible",
    "Linear Li-filter horizontal-defect obstruction",
    "log^2 |w",
    "Weil quadratic",
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
print("PHASE 7A HORIZONTAL INFORMATION AUDIT: PASS")
print("HORIZONTAL DEFECT PROGRAM: CREATED")
print("CANDIDATE OBJECTS: CLASSIFIED")
print("SCALAR COUNTING LIMITATION: RECORDED")
print("NEXT TARGET: LINEAR LI-FILTER OBSTRUCTION")
print("=" * 80)
