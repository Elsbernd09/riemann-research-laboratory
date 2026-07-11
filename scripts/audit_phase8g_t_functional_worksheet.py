from pathlib import Path

files = [
    Path("weil_reconstruction/sources/extractions/PHASE_8G_T_FUNCTIONAL_EXTRACTION_WORKSHEET.md"),
    Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_LOCK_REQUIREMENTS.md"),
    Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_TERM_TABLE.md"),
]

required = [
    "Full T[f] Functional Extraction Worksheet",
    "does not fill the formula from memory",
    "Prime-side term",
    "Archimedean term",
    "UNLOCKED",
    "T_FUNCTIONAL_IMPLEMENTATION_PERMISSION: DENIED",
    "Do not implement a Weil matrix yet",
    "not a proof of RH",
    "not a new Weil criterion",
    "not a novelty claim",
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
print("PHASE 8G T[f] FUNCTIONAL WORKSHEET AUDIT: PASS")
print("FULL FUNCTIONAL EXTRACTION WORKSHEET: CREATED")
print("TERM TABLE: CREATED")
print("LOCK REQUIREMENTS: CREATED")
print("IMPLEMENTATION PERMISSION: DENIED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
