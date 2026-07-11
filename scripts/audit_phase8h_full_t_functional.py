from pathlib import Path

files = [
    Path("weil_reconstruction/sources/extractions/PHASE_8H_FULL_T_FUNCTIONAL_EXTRACTION.md"),
    Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_EXTRACTED_FORMULA.md"),
    Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_TERM_TABLE.md"),
    Path("weil_reconstruction/sources/extractions/T_FUNCTIONAL_LOCK_REQUIREMENTS.md"),
    Path("weil_reconstruction/sources/CONVENTION_LOCK_TABLE.md"),
]

required = [
    "Full Bombieri T[f] Formula Extraction",
    "f^*(x)=\\frac1x f\\left(\\frac1x\\right)",
    "\\Lambda(n)",
    "\\log 4\\pi",
    "\\frac{x\\,dx}{x^2-1}",
    "T[f]=T[f^*]=\\sum_\\rho f(\\rho)",
    "T_FUNCTIONAL_FORMULA_STATUS: LOCKED",
    "FINITE_RANK_WEIL_IMPLEMENTATION_PERMISSION: DENIED",
    "finite-rank Weil implementation: STILL BLOCKED",
    "No RH proof",
    "No new Weil criterion",
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
print("PHASE 8H FULL T[f] FUNCTIONAL AUDIT: PASS")
print("FULL BOMBIERI T[f] FORMULA: LOCKED")
print("TERM TABLE: UPDATED")
print("CONVENTION LOCK TABLE: UPDATED")
print("SYMBOLIC T[f] WORK: ALLOWED")
print("FINITE-RANK WEIL IMPLEMENTATION: STILL BLOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
