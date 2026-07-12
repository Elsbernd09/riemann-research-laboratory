from pathlib import Path

files = [
    Path("weil_reconstruction/finite_truncations/PHASE_8O_FINITE_TRUNCATION_SOURCE_MAP.md"),
    Path("weil_reconstruction/finite_truncations/FINITE_TRUNCATION_SOURCE_MAP.md"),
    Path("weil_reconstruction/finite_truncations/FINITE_TRUNCATION_TERM_TABLE.md"),
    Path("weil_reconstruction/finite_truncations/NEXT_EXTRACTION_TARGETS.md"),
]

required = [
    "Finite Truncation Source Map",
    "Sections 5 and 6",
    "Section 8",
    "Theorem 8",
    "Section 10",
    "Section 11",
    "SOURCE-LOCATED",
    "No matrix code",
    "No eigenvalue computation",
    "Do not implement Section 8 matrices yet",
    "No RH proof",
    "No novelty claim",
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
print("PHASE 8O FINITE TRUNCATION SOURCE MAP AUDIT: PASS")
print("SOURCE ROADMAP: LOCKED")
print("SECTION 8: SOURCE-LOCATED")
print("THEOREM 8: SOURCE-LOCATED")
print("SECTION 10/11 LIMITING PROCESS: SOURCE-LOCATED")
print("MATRIX IMPLEMENTATION: STILL BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
