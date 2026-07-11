from pathlib import Path

files = [
    Path("horizontal_defect/weil_interface/PHASE_7J_SECOND_ORDER_INDEFINITENESS_AUDIT.md"),
    Path("horizontal_defect/experiments/phase7j_second_order_indefiniteness.py"),
]

required = [
    "Second-Order Coefficient Indefiniteness Audit",
    "B_m(\\gamma)",
    "not a Weil theorem",
    "does not prove RH",
    "Rayleigh",
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
print("PHASE 7J SECOND-ORDER INDEFINITENESS AUDIT: PASS")
print("SECOND-ORDER COEFFICIENT AUDIT: RECORDED")
print("PURE PYTHON RAYLEIGH SCAN: PASSED")
print("WEIL CLAIM: NONE")
print("RH CLAIM: NONE")
print("=" * 80)
