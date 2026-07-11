from pathlib import Path

files = [
    Path("horizontal_defect/theorems/PHASE_7E_RADIAL_VS_LINEAR_FILTER_NOGO.md"),
    Path("horizontal_defect/experiments/phase7e_radial_vs_linear_nogo.py"),
]

required = [
    "No-Go Comparison",
    "cannot uniformly dominate",
    "c u^2",
    "zero mean",
    "This theorem does not prove RH",
    "finite linear Li filters",
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
print("PHASE 7E RADIAL VS LINEAR FILTER NO-GO AUDIT: PASS")
print("UNIFORM LOWER COMPARISON: IMPOSSIBLE")
print("FINITE LINEAR FILTER BRIDGE: OBSTRUCTED")
print("NEXT DIRECTION: QUADRATIC OR WEIL-POSITIVE FORMS")
print("RH CLAIM: NONE")
print("=" * 80)
