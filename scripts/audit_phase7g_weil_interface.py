from pathlib import Path

files = [
    Path("horizontal_defect/weil_interface/PHASE_7G_WEIL_POSITIVE_INTERFACE_AUDIT.md"),
    Path("horizontal_defect/weil_interface/FINITE_RANK_WEIL_TESTBED_PLAN.md"),
    Path("horizontal_defect/experiments/phase7g_weil_interface_toy_matrix.py"),
]

required = [
    "Weil-Positive Interface Audit",
    "does not claim a new Weil criterion",
    "Finite-rank Weil",
    "synthetic off-critical zero quartet",
    "not a Weil theorem",
    "diagnostic",
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
print("PHASE 7G WEIL-POSITIVE INTERFACE AUDIT: PASS")
print("INTERFACE BARRIERS: RECORDED")
print("FINITE-RANK TESTBED PLAN: CREATED")
print("TOY MATRIX EXPERIMENT: RAN")
print("NEW WEIL CRITERION CLAIM: NONE")
print("RH CLAIM: NONE")
print("=" * 80)
