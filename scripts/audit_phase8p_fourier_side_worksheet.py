from pathlib import Path

files = [
    Path("weil_reconstruction/fourier_side/PHASE_8P_FOURIER_SIDE_EXTRACTION_WORKSHEET.md"),
    Path("weil_reconstruction/fourier_side/FOURIER_SIDE_TERM_TABLE.md"),
    Path("weil_reconstruction/fourier_side/FOURIER_SIDE_DANGER_NOTE.md"),
]

required = [
    "Fourier-Side Infinite Quadratic Form Extraction Worksheet",
    "does not implement a matrix",
    "does not compute eigenvalues",
    "Fourier transform convention",
    "Infinite quadratic form",
    "Eigenvalue problem",
    "FOURIER_SIDE_IMPLEMENTATION_PERMISSION: DENIED",
    "FINITE_MATRIX_IMPLEMENTATION_PERMISSION: DENIED",
    "No matrix code",
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
print("PHASE 8P FOURIER-SIDE WORKSHEET AUDIT: PASS")
print("FOURIER-SIDE EXTRACTION WORKSHEET: CREATED")
print("TERM TABLE: CREATED")
print("DANGER NOTE: CREATED")
print("FOURIER IMPLEMENTATION: BLOCKED")
print("FINITE MATRIX IMPLEMENTATION: BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
