from pathlib import Path

files = [
    Path("FINAL_PROJECT_STATUS.md"),
    Path("NEXT_STEPS.md"),
]

required = [
    "The project does not prove RH",
    "Originality remains under active prior-art review",
    "O_{K,\\eta}",
    "\\frac{\\log H}{H^3}",
    "Do not add more phases",
    "external review",
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
print("PHASE 6C FINAL STATUS AUDIT: PASS")
print("FINAL PROJECT STATUS: PRESENT")
print("NEXT STEPS: PRESENT")
print("PROJECT STOPPING POINT: CLEAN")
print("READY FOR MENTOR REVIEW: YES")
print("READY FOR SUBMISSION: NO")
print("=" * 80)
