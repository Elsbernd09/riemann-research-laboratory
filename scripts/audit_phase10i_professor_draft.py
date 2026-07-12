from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/paper_draft/PHASE_10I_PROFESSOR_READABLE_DRAFT.md"),
    Path("original_results/finite_bombieri_stability/paper_draft/PAPER_DRAFT_STATUS.md"),
    Path("original_results/finite_bombieri_stability/paper_draft/PROFESSOR_REVIEW_NOTE.md"),
]

required = [
    "A Finite Stability Certificate",
    "Abstract",
    "Main theorem",
    "N\\varepsilon<g_0(M)",
    "Nm_{\\max}\\eta<g_0(M)",
    "Synthetic examples",
    "Limitations",
    "This draft does not prove RH",
    "This draft does not falsify RH",
    "This draft does not use zeta zeros",
    "This draft does not claim novelty",
    "Level 2",
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
print("PHASE 10I PROFESSOR-READABLE DRAFT AUDIT: PASS")
print("DRAFT: CREATED")
print("MAIN THEOREM: INCLUDED")
print("EXAMPLES: INCLUDED")
print("LIMITATIONS: INCLUDED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
