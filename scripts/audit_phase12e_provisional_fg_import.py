from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/provisional_fg_import/PHASE_12E_PROVISIONAL_FG_IMPORT.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/provisional_fg_import/PROVISIONAL_FG_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/provisional_fg_import/NEXT_PHASE_12F_MELLIN_IDENTITY_PROOF.md"),
]

required = [
    "PROVISIONAL_F_G_IMPORT",
    "F_G_EQUALS_G_CONVOLVE_G_STAR",
    "G_STAR_INVOLUTION_IMPORTED",
    "MULTIPLICATIVE_CONVOLUTION_IMPORTED",
    "PROVISIONAL_Q_W_DEFINED",
    "Q_W_EQUALS_T_OF_G_CONVOLVE_G_STAR",
    "MELLIN_PRODUCT_TARGET_IDENTIFIED",
    "PRIMARY_SOURCE_CONFIRMATION_STILL_REQUIRED",
    "SIGN_CONVENTION_STILL_UNCONFIRMED",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
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
print("PHASE 12E PROVISIONAL F_G IMPORT AUDIT: PASS")
print("F_g = g * g^*: PROVISIONALLY IMPORTED")
print("g^* INVOLUTION: IMPORTED")
print("MULTIPLICATIVE CONVOLUTION: IMPORTED")
print("Q_W(g)=T[g*g^*]: PROVISIONALLY DEFINED")
print("PRIMARY SOURCE CONFIRMATION: STILL REQUIRED")
print("SIGN CONVENTION: STILL UNCONFIRMED")
print("LEVEL 4 BREAKTHROUGH CANDIDATE: NOT YET ACHIEVED")
print("=" * 80)
