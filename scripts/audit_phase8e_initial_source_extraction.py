from pathlib import Path

files = [
    Path("weil_reconstruction/sources/extractions/PHASE_8E_INITIAL_SOURCE_EXTRACTION.md"),
    Path("weil_reconstruction/sources/extractions/BOMBIERI_SOURCE_CARD.md"),
    Path("weil_reconstruction/sources/extractions/SUZUKI_SOURCE_CARD.md"),
    Path("weil_reconstruction/sources/CONVENTION_LOCK_TABLE.md"),
]

required = [
    "Initial Source Extraction Notes",
    "Bombieri",
    "Suzuki",
    "positive semidefinite if and only if RH",
    "finite truncations",
    "Q_W",
    "PARTIAL",
    "UNLOCKED",
    "No exact Weil-code phase",
    "No novelty claim",
    "No RH proof claim",
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
print("PHASE 8E INITIAL SOURCE EXTRACTION AUDIT: PASS")
print("BOMBIERI SOURCE CARD: CREATED")
print("SUZUKI SOURCE CARD: CREATED")
print("CONVENTION LOCK TABLE: UPDATED")
print("EXACT FORMULA ROWS: STILL LOCKED OUT")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
