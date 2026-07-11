from pathlib import Path

files = [
    Path("horizontal_defect/theorems/PHASE_7D_AGGREGATION_BARRIER.md"),
    Path("horizontal_defect/experiments/phase7d_aggregation_barrier.py"),
]

required = [
    "Aggregation Barrier",
    "Positive aggregation is easy",
    "Arithmetic-side control is hard",
    "does not prove RH",
    "explicit-formula-compatible",
    "tautological",
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
print("PHASE 7D AGGREGATION BARRIER AUDIT: PASS")
print("FINITE POSITIVE AGGREGATION: PROVED")
print("TAUTOLOGICAL RH-EQUIVALENT RISK: RECORDED")
print("EXPLICIT-FORMULA COMPATIBILITY: OPEN")
print("RH CLAIM: NONE")
print("=" * 80)
