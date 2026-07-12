from pathlib import Path

files = [
    Path("breakthrough_push/phase_b4_prior_art_collision/PHASE_B4_PRIOR_ART_COLLISION.md"),
    Path("breakthrough_push/phase_b4_prior_art_collision/PRIOR_ART_COLLISION_STATUS.md"),
    Path("breakthrough_push/phase_b4_prior_art_collision/PRIOR_ART_TABLE.md"),
    Path("breakthrough_push/phase_b4_prior_art_collision/NEXT_PHASE_B5_PRIMARY_PAPER_EXTRACTION.md"),
]

required = [
    "PHASE_B4_PRIOR_ART_COLLISION_COMPLETE",
    "FINITE_GALERKIN_COLLISION_RISK_IDENTIFIED",
    "CLASSICAL_WEIL_COMPONENTS_NOT_NOVEL",
    "FINITE_DETECTION_BY_CONVERGENCE_LIKELY_STANDARD",
    "POLE_ADMISSIBLE_PIPELINE_POSSIBLE_CONTRIBUTION",
    "ARITHMETIC_CERTIFICATE_PIPELINE_POSSIBLE_CONTRIBUTION",
    "NOVELTY_NOT_ESTABLISHED",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "READY_FOR_PHASE_B5_PRIMARY_PAPER_EXTRACTION",
    "Theorem B4.1",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a breakthrough",
    "This phase does not prove novelty",
    "This phase does not complete prior-art review",
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
print("PHASE B4 PRIOR-ART COLLISION AUDIT: PASS")
print("FINITE GALERKIN COLLISION RISK: IDENTIFIED")
print("CLASSICAL WEIL COMPONENTS: NOT NOVEL")
print("FINITE DETECTION BY CONVERGENCE: LIKELY STANDARD")
print("POLE-ADMISSIBLE PIPELINE: POSSIBLE CONTRIBUTION")
print("ARITHMETIC CERTIFICATE PIPELINE: POSSIBLE CONTRIBUTION")
print("NOVELTY: NOT ESTABLISHED")
print("BREAKTHROUGH: NOT ACHIEVED")
print("READY FOR PRIMARY PAPER EXTRACTION")
print("=" * 80)
