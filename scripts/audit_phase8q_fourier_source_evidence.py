from pathlib import Path

files = [
    Path("weil_reconstruction/fourier_side/PHASE_8Q_FOURIER_SIDE_SOURCE_EVIDENCE_LEDGER.md"),
    Path("weil_reconstruction/fourier_side/FOURIER_SIDE_SOURCE_EVIDENCE_TABLE.md"),
    Path("weil_reconstruction/fourier_side/FOURIER_EXTRACTION_BLOCKERS.md"),
    Path("weil_reconstruction/fourier_side/FOURIER_SIDE_TERM_TABLE.md"),
]

required = [
    "Fourier-Side Source Evidence Ledger",
    "SOURCE-LOCATED",
    "Formula status: UNLOCKED",
    "finite approximations",
    "Theorem 8",
    "Sections 10 and 11",
    "FOURIER-SIDE IMPLEMENTATION: DENIED",
    "FINITE MATRIX IMPLEMENTATION: DENIED",
    "EIGENVALUE COMPUTATION: DENIED",
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
print("PHASE 8Q FOURIER-SIDE SOURCE EVIDENCE AUDIT: PASS")
print("SOURCE EVIDENCE CHAIN: RECORDED")
print("EXACT FORMULAS: STILL UNLOCKED")
print("FOURIER IMPLEMENTATION: BLOCKED")
print("FINITE MATRIX IMPLEMENTATION: BLOCKED")
print("EIGENVALUE COMPUTATION: BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
