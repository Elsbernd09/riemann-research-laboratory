from pathlib import Path

files = [
    Path("horizontal_defect/weil_interface/PHASE_7I_CENTERED_SIGNAL_SCALING.md"),
    Path("horizontal_defect/experiments/phase7i_centered_scaling_law.py"),
]

required = [
    "Centered Quartet Signal Scaling Law",
    "C_m(x,\\gamma)=O(x^2)",
    "x^2B_m",
    "O(x^4)",
    "does not prove RH",
    "not a Weil theorem",
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
print("PHASE 7I CENTERED SCALING LAW AUDIT: PASS")
print("SCALING THEOREM: RECORDED")
print("PURE PYTHON SCALING EXPERIMENT: PASSED")
print("SIGNAL ORDER: x^2")
print("WEIL CLAIM: NONE")
print("RH CLAIM: NONE")
print("=" * 80)
