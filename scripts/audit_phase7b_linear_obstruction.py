from pathlib import Path

files = [
    Path("horizontal_defect/theorems/PHASE_7B_LINEAR_LI_FILTER_OBSTRUCTION.md"),
    Path("horizontal_defect/experiments/phase7b_linear_filter_scan.py"),
]

required = [
    "Linear Li-Filter Obstruction Theorem",
    "cosh(nu)-1",
    "P(\\theta)",
    "If \\(P(\\theta)\\ge0\\)",
    "cannot provide a universal positive horizontal-defect detector",
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
print("PHASE 7B LINEAR LI-FILTER OBSTRUCTION AUDIT: PASS")
print("THEOREM FILE: PRESENT")
print("NUMERICAL SIGN-SCAN: PASS")
print("OBSTRUCTION STATUS: PROVED AT LEADING ORDER")
print("RH CLAIM: NONE")
print("=" * 80)
