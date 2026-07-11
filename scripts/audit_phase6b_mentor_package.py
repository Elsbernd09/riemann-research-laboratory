from pathlib import Path

files = [
    Path("paper/MENTOR_REVIEW_NOTE.md"),
    Path("paper/PROJECT_SUMMARY_FOR_READER.md"),
    Path("paper/WHAT_TO_REVIEW_FIRST.md"),
]

required = [
    "No assumption of the Riemann Hypothesis is used",
    "Originality remains under active prior-art review",
    "O_{K,\\eta}",
    "\\frac{\\log H}{H^3}",
    "ordinary integration by parts",
    "not claim",
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
print("PHASE 6B MENTOR PACKAGE AUDIT: PASS")
print("MENTOR REVIEW NOTE: PRESENT")
print("PROJECT SUMMARY: PRESENT")
print("REVIEW ORDER GUIDE: PRESENT")
print("CLAIM BOUNDARIES: PRESENT")
print("=" * 80)
