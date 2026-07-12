from pathlib import Path

files = [
    Path("weil_reconstruction/symbolic/PHASE_8L_SYMBOLIC_POSITIVITY_MECHANISM.md"),
    Path("weil_reconstruction/symbolic/POSITIVITY_MECHANISM_CARD.md"),
    Path("weil_reconstruction/symbolic/OFF_CRITICAL_FAILURE_MECHANISM.md"),
]

required = [
    "Symbolic Positivity Mechanism",
    "g^*_{\\mathrm{pos}}",
    "1-\\overline{\\rho}=\\rho",
    "|g(\\rho)|^2",
    "off-critical",
    "does not prove the converse",
    "No RH proof",
    "No new Weil criterion",
    "No novelty claim",
    "No finite-rank Weil matrix yet",
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
print("PHASE 8L SYMBOLIC POSITIVITY MECHANISM AUDIT: PASS")
print("RH-IMPLIES-SQUARE-NORM MECHANISM: RECORDED")
print("OFF-CRITICAL FAILURE MECHANISM: RECORDED")
print("CONVERSE DIRECTION: NOT CLAIMED")
print("FINITE-RANK WEIL MATRICES: STILL BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
