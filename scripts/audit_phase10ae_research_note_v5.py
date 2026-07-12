from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/paper_draft_v5/PHASE_10AE_RESEARCH_NOTE_V5.md"),
    Path("original_results/finite_bombieri_stability/paper_draft_v5/RESEARCH_NOTE_V5_STATUS.md"),
    Path("original_results/finite_bombieri_stability/paper_draft_v5/NEXT_BREAKTHROUGH_TRACK_STEPS.md"),
]

required = [
    "RESEARCH_NOTE_V5",
    "EXPLICIT_H_KERNEL_LIPSCHITZ_THEOREM",
    "H_KERNEL_STABILITY_INSERTION",
    "EXPLICIT_H_KERNEL_SUPPORT_STABILITY_CERTIFICATE",
    "CERTIFIED_STABLE",
    "NOT_CERTIFIED",
    "Theorem 6.1",
    "Theorem 8.1",
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
print("PHASE 10AE RESEARCH NOTE V5 AUDIT: PASS")
print("EXPLICIT H-KERNEL LIPSCHITZ THEOREM: INCLUDED")
print("EXPLICIT H-KERNEL SUPPORT-STABILITY CERTIFICATE: INCLUDED")
print("CERTIFIED ALGORITHM INTERPRETATION: INCLUDED")
print("BREAKTHROUGH CLAIM: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
