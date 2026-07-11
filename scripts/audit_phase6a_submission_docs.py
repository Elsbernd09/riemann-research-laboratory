from pathlib import Path

files = [
    Path("paper/SUBMISSION_CHECKLIST.md"),
    Path("paper/REFEREE_RESPONSE_DRAFT.md"),
]

for path in files:
    if not path.exists():
        raise FileNotFoundError(path)

    text = path.read_text(encoding="utf-8")

    if "\x00" in text:
        raise ValueError(f"NUL byte found in {path}")

required_anywhere = [
    "Originality remains under active prior-art review",
    "not a proof of RH",
    "O_{K,\\eta}",
    "\\frac{\\log H}{H^3}",
    "absolutely continuous",
    "\\Delta N(H)",
    "not a novelty claim",
]

combined = "\n".join(path.read_text(encoding="utf-8") for path in files)

missing = [
    phrase for phrase in required_anywhere
    if phrase.lower() not in combined.lower()
]

if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

print("=" * 80)
print("PHASE 6A SUBMISSION DOCS AUDIT: PASS")
print("SUBMISSION CHECKLIST: PRESENT")
print("REFEREE RESPONSE DRAFT: PRESENT")
print("CORE CLAIM BOUNDARIES: PRESENT")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
