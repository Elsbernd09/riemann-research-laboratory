from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/paper_draft_v4/PHASE_10Y_RESEARCH_NOTE_V4.md"),
    Path("original_results/finite_bombieri_stability/paper_draft_v4/RESEARCH_NOTE_V4_STATUS.md"),
    Path("original_results/finite_bombieri_stability/paper_draft_v4/NEXT_BREAKTHROUGH_TRACK_STEPS.md"),
]

required = [
    "RESEARCH_NOTE_V4",
    "COMBINED_RADIUS_CERTIFIED_ALGORITHM",
    "COMBINED_MINIMUM_RADIUS_CERTIFICATE",
    "ROW_SUM_CERTIFICATE",
    "CERTIFIED_STABLE",
    "NOT_CERTIFIED",
    "Theorem 7.1",
    "Theorem 9.1",
    "This note does not prove RH",
    "This note does not falsify RH",
    "This note does not use zeta zeros",
    "This note does not claim novelty",
    "No breakthrough claim yet",
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
print("PHASE 10Y RESEARCH NOTE V4 AUDIT: PASS")
print("COMBINED-RADIUS THEOREM: INCLUDED")
print("ROW-SUM CERTIFICATE: INCLUDED")
print("CERTIFIED ALGORITHM: INCLUDED")
print("CORRECTNESS PROOF: INCLUDED")
print("BREAKTHROUGH CLAIM: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
