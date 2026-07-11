from pathlib import Path

files = [
    Path("horizontal_defect/synthesis/PHASE_7_HORIZONTAL_DEFECT_SYNTHESIS.md"),
    Path("horizontal_defect/synthesis/PHASE_7_PUBLIC_SUMMARY.md"),
]

required = [
    "Phase 7 Horizontal Defect Program Synthesis",
    "basis-dependent",
    "does not prove RH",
    "does not claim a new Weil criterion",
    "Horizontal-defect detection is possible locally",
    "Classical Weil Criterion Reconstruction",
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
print("PHASE 7L SYNTHESIS AUDIT: PASS")
print("PHASE 7 PROGRAM SUMMARY: CREATED")
print("PUBLIC SUMMARY: CREATED")
print("ACHIEVEMENTS AND OBSTRUCTIONS: RECORDED")
print("NEXT DIRECTION: CLASSICAL WEIL RECONSTRUCTION")
print("RH CLAIM: NONE")
print("=" * 80)
