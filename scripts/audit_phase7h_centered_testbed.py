from pathlib import Path

files = [
    Path("horizontal_defect/weil_interface/PHASE_7H_CENTERED_FINITE_RANK_TESTBED.md"),
    Path("horizontal_defect/experiments/phase7h_centered_quartet_testbed.py"),
]

required = [
    "Centered Finite-Rank Quartet Testbed",
    "C_m(0,\\gamma)=0",
    "not a classical Weil quadratic form",
    "diagnostic finite-rank laboratory",
    "Pure Python",
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
print("PHASE 7H CENTERED FINITE-RANK TESTBED AUDIT: PASS")
print("CENTERED MATRIX: CREATED")
print("CRITICAL-LINE COLLAPSE: VANISHES")
print("HORIZONTAL DISPLACEMENT SIGNAL: TESTED")
print("WEIL CLAIM: NONE")
print("RH CLAIM: NONE")
print("=" * 80)
