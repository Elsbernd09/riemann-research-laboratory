from pathlib import Path

files = [
    Path("weil_reconstruction/sources/PHASE_8D_SOURCE_GROUNDED_EXTRACTION_PROTOCOL.md"),
    Path("weil_reconstruction/sources/BOMBIERI_WEIL_READING_TEMPLATE.md"),
    Path("weil_reconstruction/sources/CONVENTION_LOCK_TABLE.md"),
    Path("weil_reconstruction/sources/SOURCE_EXTRACTION_TODO.md"),
]

required = [
    "Source-Grounded Weil Extraction Protocol",
    "Do not reconstruct exact Weil formulae from memory",
    "Test-function class",
    "Transform convention",
    "Zero-side expression",
    "Quadratic form",
    "UNLOCKED",
    "No exact Weil formula has been implemented yet",
    "does not prove RH",
    "does not claim a new Weil criterion",
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
print("PHASE 8D SOURCE EXTRACTION PROTOCOL AUDIT: PASS")
print("SOURCE-GROUNDED PROTOCOL: CREATED")
print("READING TEMPLATE: CREATED")
print("CONVENTION LOCK TABLE: CREATED")
print("EXACT WEIL IMPLEMENTATION: BLOCKED UNTIL SOURCES LOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
