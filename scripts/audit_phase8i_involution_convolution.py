from pathlib import Path

files = [
    Path("weil_reconstruction/symbolic/PHASE_8I_INVOLUTION_CONVOLUTION_AUDIT.md"),
    Path("weil_reconstruction/symbolic/INVOLUTION_CONVENTION_NOTE.md"),
    Path("weil_reconstruction/symbolic/CONVOLUTION_IDENTITY_CARD.md"),
]

required = [
    "Involution and Convolution Identity Audit",
    "f^*(s)=f(1-s)",
    "(f*g)(s)=f(s)g(s)",
    "(f*f^*)(s)=f(s)f(1-s)",
    "Complex-valued caution",
    "complex conjugation",
    "Finite-rank positivity implementation",
    "BLOCKED",
    "No RH proof",
    "No new Weil criterion",
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
print("PHASE 8I INVOLUTION/CONVOLUTION AUDIT: PASS")
print("MELLIN INVOLUTION IDENTITY: RECORDED")
print("MULTIPLICATIVE CONVOLUTION IDENTITY: RECORDED")
print("COMPLEX CONJUGATION CONVENTION: FLAGGED")
print("FINITE-RANK POSITIVITY IMPLEMENTATION: BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
