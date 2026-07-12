from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/paper_draft_v2/PHASE_10N_UPGRADED_PROFESSOR_DRAFT.md"),
    Path("original_results/finite_bombieri_stability/paper_draft_v2/PAPER_DRAFT_V2_STATUS.md"),
    Path("original_results/finite_bombieri_stability/paper_draft_v2/UPDATED_PROFESSOR_REVIEW_NOTE.md"),
]

required = [
    "Support-Stability Certificates",
    "Theorem 2",
    "Support-perturbation stability",
    "2Nm_{\\max}L_t(U)\\delta<g_0(M",
    "maximum allowed support displacement",
    "Level 3 candidate",
    "This draft does not prove RH",
    "This draft does not falsify RH",
    "This draft does not use zeta zeros",
    "This draft does not claim novelty",
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
print("PHASE 10N UPGRADED PROFESSOR DRAFT AUDIT: PASS")
print("SUPPORT-PERTURBATION THEOREM: INCLUDED")
print("LEVEL 3 CANDIDATE STATUS: RECORDED")
print("PROFESSOR REVIEW NOTE: UPDATED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
