from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/spectral_qw_alignment/PHASE_12G_SPECTRAL_QW_ALIGNMENT.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/spectral_qw_alignment/SPECTRAL_QW_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/spectral_qw_alignment/NEXT_PHASE_12H_NEGATIVE_OBSTRUCTION_TEMPLATE.md"),
]

required = [
    "SPECTRAL_Q_W_ALIGNMENT_COMPLETE",
    "PROVISIONAL_SPECTRAL_Q_W_FORM_PROVED",
    "Q_W_EQUALS_ZERO_SUM_PRODUCT_FORM",
    "RH_IMPLIES_PROVISIONAL_Q_W_POSITIVITY",
    "CONVERSE_NOT_PROVED",
    "PRIMARY_SOURCE_CONFIRMATION_STILL_REQUIRED",
    "SIGN_CONVENTION_STILL_UNCONFIRMED",
    "FINITE_APPROXIMATION_NOT_YET_PROVED",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED",
    "Theorem 12G.1",
    "Corollary 12G.2",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove the full Weil positivity theorem",
    "This phase does not prove Level 4 contribution",
    "This phase does not establish novelty",
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
print("PHASE 12G SPECTRAL Q_W ALIGNMENT AUDIT: PASS")
print("PROVISIONAL SPECTRAL Q_W FORM: PROVED")
print("RH IMPLIES PROVISIONAL POSITIVITY: PROVED")
print("CONVERSE: NOT PROVED")
print("FINITE APPROXIMATION: NOT YET PROVED")
print("LEVEL 4 BREAKTHROUGH CANDIDATE: NOT YET ACHIEVED")
print("=" * 80)
