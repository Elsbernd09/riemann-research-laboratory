from pathlib import Path

files = [
    Path("horizontal_defect/weil_interface/PHASE_7K_STABILITY_AUDIT.md"),
    Path("horizontal_defect/experiments/phase7k_stability_audit.py"),
]

required = [
    "Stability Audit",
    "basis-dependent",
    "not a Weil theorem",
    "not a proof of RH",
    "mixed result",
    "basis-dependence obstruction",
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
print("PHASE 7K STABILITY AUDIT: PASS")
print("HEIGHT/BASIS/DEGREE STRESS TEST: RECORDED")
print("OUTCOME: MIXED")
print("BASIS-DEPENDENCE OBSTRUCTION: RECORDED")
print("WEIL CLAIM: NONE")
print("RH CLAIM: NONE")
print("=" * 80)
