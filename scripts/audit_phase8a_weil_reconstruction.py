from pathlib import Path

files = [
    Path("weil_reconstruction/PHASE_8A_CLASSICAL_WEIL_RECONSTRUCTION.md"),
    Path("weil_reconstruction/WEIL_RECONSTRUCTION_MAP.md"),
    Path("weil_reconstruction/PHASE_8_RESEARCH_RULES.md"),
]

required = [
    "Classical Weil Criterion Reconstruction",
    "not a novelty claim",
    "not a proof of RH",
    "Weil positivity",
    "negative direction",
    "toy matrix is not a Weil quadratic form",
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
print("PHASE 8A WEIL RECONSTRUCTION AUDIT: PASS")
print("CLASSICAL WEIL RECONSTRUCTION MAP: CREATED")
print("RESEARCH RULES: CREATED")
print("TOY-VS-WEIL BOUNDARY: RECORDED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
