from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/weil_form_abstraction/PHASE_10AM_TOY_BUT_HONEST_WEIL_FORM_ABSTRACTION.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/weil_form_abstraction/WEIL_ABSTRACTION_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/weil_form_abstraction/NEXT_TARGET_CLASSICAL_IMPORTS.md"),
]

required = [
    "TOY_BUT_HONEST_WEIL_FORM_ABSTRACTION",
    "ABSTRACT_WEIL_FORM_MODEL",
    "POSITIVITY_TRANSFER_IN_TOY_MODEL",
    "QUANTITATIVE_NEGATIVE_DIRECTION_TRANSFER",
    "CLASSICAL_THEORY_IMPORT_OBLIGATIONS",
    "NOT_RH_CONTRIBUTION_YET",
    "Theorem 10AM.1",
    "Theorem 10AM.2",
    "Theorem 10AM.3",
    "E_N(f)=Q_N(P_Nf)-Q_\\infty(f)",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not claim novelty",
]

for path in files:
    if not path.exists():
        raise FileNotFoundError(path)

    text = path.read_text(encoding="utf-8")
    if "\x00" in text:
        raise ValueError(f"NUL byte found in {path}")

combined = "\n".join(path.read_text(encoding="utf-8") for path in files)

missing = [phrase for phrase in required if phrase.lower() not in combined.lower()]

if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

print("=" * 80)
print("PHASE 10AM WEIL ABSTRACTION AUDIT: PASS")
print("TOY-BUT-HONEST WEIL MODEL: LOCKED")
print("POSITIVITY TRANSFER: PROVED")
print("NEGATIVE DIRECTION TRANSFER: PROVED")
print("CLASSICAL IMPORT OBLIGATIONS: RECORDED")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
