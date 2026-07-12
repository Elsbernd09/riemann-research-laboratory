from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/breakthrough_audit/PHASE_10AH_BREAKTHROUGH_STATUS_AND_PROFESSOR_READINESS.md"),
    Path("original_results/finite_bombieri_stability/breakthrough_audit/PROFESSOR_READINESS_LOCK.md"),
    Path("original_results/finite_bombieri_stability/breakthrough_audit/NEXT_ACTION_DECISION.md"),
]

required = [
    "BREAKTHROUGH_STATUS_AUDIT",
    "NOT_A_BREAKTHROUGH_YET",
    "SERIOUS_FINITE_RESEARCH_NOTE_CANDIDATE",
    "READY_FOR_PROFESSOR_FEEDBACK_AFTER_POLISH",
    "NOVELTY_NOT_ESTABLISHED",
    "Stop theorem stacking",
    "polished professor review package",
    "This audit does not prove RH",
    "This audit does not falsify RH",
    "This audit does not use zeta zeros",
    "This audit does not claim novelty",
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
print("PHASE 10AH BREAKTHROUGH STATUS AUDIT: PASS")
print("STATUS: SERIOUS FINITE RESEARCH NOTE CANDIDATE")
print("BREAKTHROUGH: NOT YET")
print("PROFESSOR FEEDBACK: READY AFTER POLISH")
print("NOVELTY: NOT ESTABLISHED")
print("NEXT ACTION: POLISH PACKAGE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
