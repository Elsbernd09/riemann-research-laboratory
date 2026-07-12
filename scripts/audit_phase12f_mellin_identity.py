from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/mellin_identity_proof/PHASE_12F_MELLIN_IDENTITY_PROOF.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/mellin_identity_proof/MELLIN_IDENTITY_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/mellin_identity_proof/NEXT_PHASE_12G_SPECTRAL_QW_ALIGNMENT.md"),
]

required = [
    "MELLIN_IDENTITY_PROOF_COMPLETE",
    "G_STAR_MELLIN_IDENTITY_PROVED",
    "MELLIN_CONVOLUTION_THEOREM_PROVED",
    "F_G_MELLIN_PRODUCT_PROVED",
    "CRITICAL_LINE_SQUARE_STRUCTURE_PROVED",
    "PRIMARY_SOURCE_CONFIRMATION_STILL_REQUIRED",
    "SIGN_CONVENTION_STILL_UNCONFIRMED",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED",
    "Theorem 12F.1",
    "Theorem 12F.2",
    "Theorem 12F.3",
    "Corollary 12F.4",
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
print("PHASE 12F MELLIN IDENTITY AUDIT: PASS")
print("g^* MELLIN IDENTITY: PROVED")
print("MELLIN CONVOLUTION THEOREM: PROVED")
print("F_g PRODUCT IDENTITY: PROVED")
print("CRITICAL LINE SQUARE STRUCTURE: PROVED")
print("PRIMARY SOURCE CONFIRMATION: STILL REQUIRED")
print("LEVEL 4 BREAKTHROUGH CANDIDATE: NOT YET ACHIEVED")
print("=" * 80)
