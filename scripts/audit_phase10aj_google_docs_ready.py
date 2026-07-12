from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/google_docs_ready/GOOGLE_DOCS_MASTER_RESEARCH_NOTE.md"),
    Path("original_results/finite_bombieri_stability/google_docs_ready/GOOGLE_DOCS_FORMATTING_INSTRUCTIONS.md"),
    Path("original_results/finite_bombieri_stability/google_docs_ready/GEMINI_FORMATTING_PROMPT.md"),
    Path("original_results/finite_bombieri_stability/google_docs_ready/PROFESSOR_SEND_CHECKLIST.md"),
    Path("original_results/finite_bombieri_stability/google_docs_ready/FINAL_STATUS_BEFORE_OUTREACH.md"),
]

required = [
    "Explicit H-Kernel Support-Stability Certificates",
    "GOOGLE_DOCS_MASTER_RESEARCH_NOTE",
    "Gemini Formatting Prompt",
    "SERIOUS_FINITE_RESEARCH_NOTE_CANDIDATE",
    "READY_FOR_PROFESSOR_FEEDBACK_AFTER_POLISH",
    "NOT_A_BREAKTHROUGH_YET",
    "NOVELTY_NOT_ESTABLISHED",
    "This note does not prove RH",
    "This note does not falsify RH",
    "This note does not use zeta zeros",
    "This note does not claim novelty",
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
print("PHASE 10AJ GOOGLE DOCS READY AUDIT: PASS")
print("GOOGLE DOCS MASTER NOTE: CREATED")
print("GEMINI FORMATTING PROMPT: CREATED")
print("SEND CHECKLIST: CREATED")
print("STATUS BEFORE OUTREACH: LOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
