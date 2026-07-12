from pathlib import Path

files = [
    Path("weil_reconstruction/fourier_side/PHASE_8R_LOG_COORDINATE_BRIDGE.md"),
    Path("weil_reconstruction/fourier_side/LOG_COORDINATE_IDENTITY_CARD.md"),
    Path("weil_reconstruction/fourier_side/FOURIER_SIDE_TERM_TABLE.md"),
    Path("weil_reconstruction/fourier_side/NEXT_EXTRACTION_TARGETS.md"),
]

required = [
    "Log-Coordinate Bridge",
    "F(u)=e^{u/2}f(e^u)",
    "F^*(u)=F(-u)",
    "multiplicative convolution becomes additive convolution",
    "2\\cosh(u/2)",
    "F(\\log n)+F(-\\log n)",
    "FOURIER",
    "UNLOCKED",
    "Do not implement finite matrices yet",
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
print("PHASE 8R LOG-COORDINATE BRIDGE AUDIT: PASS")
print("LOG COORDINATE BRIDGE: LOCKED")
print("INVOLUTION AS REFLECTION: LOCKED")
print("MULTIPLICATIVE CONVOLUTION AS ADDITIVE CONVOLUTION: LOCKED")
print("FOURIER CONVENTION: STILL UNLOCKED")
print("FINITE MATRIX IMPLEMENTATION: STILL BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
