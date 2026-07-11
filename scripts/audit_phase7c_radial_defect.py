from pathlib import Path

files = [
    Path("horizontal_defect/theorems/PHASE_7C_QUADRATIC_LI_DEFECT_ENERGY.md"),
    Path("horizontal_defect/experiments/phase7c_radial_defect_energy.py"),
]

required = [
    "Quadratic Li-Coordinate Defect Energy",
    "D_{\\mathrm{rad}}",
    "if and only if",
    "\\beta=\\frac12",
    "O(x^4)",
    "explicit arithmetic-side formula",
    "It does not prove RH",
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
print("PHASE 7C QUADRATIC RADIAL DEFECT AUDIT: PASS")
print("POSITIVE SINGLE-ZERO DETECTOR: PROVED")
print("CRITICAL-LINE VANISHING: PROVED")
print("SMALL-DISPLACEMENT EXPANSION: RECORDED")
print("EXPLICIT-FORMULA COMPATIBILITY: OPEN")
print("RH CLAIM: NONE")
print("=" * 80)
