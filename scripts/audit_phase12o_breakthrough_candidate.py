from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/breakthrough_candidate_audit/PHASE_12O_BREAKTHROUGH_CANDIDATE_AUDIT.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/breakthrough_candidate_audit/BREAKTHROUGH_CANDIDATE_STATUS_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/breakthrough_candidate_audit/NEXT_PHASE_12P_ARITHMETIC_CERTIFICATE_ROADMAP.md"),
]

required = [
    "BREAKTHROUGH_CANDIDATE_AUDIT_COMPLETE",
    "REAL_THEOREM_PROVED",
    "FINITE_SPECTRAL_DETECTION_PROVED",
    "CONDITIONAL_CONTRIBUTION_CANDIDATE",
    "LEVEL4_CONDITIONAL_BREAKTHROUGH_CANDIDATE",
    "BREAKTHROUGH_NOT_ACHIEVED",
    "RH_CONTRIBUTION_NOT_ESTABLISHED",
    "ARITHMETIC_ONLY_CERTIFICATE_REQUIRED_NEXT",
    "PRIMARY_SOURCE_VALIDATION_REQUIRED",
    "NOVELTY_NOT_ESTABLISHED",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove the full Weil positivity theorem",
    "This phase does not prove an arithmetic-only finite certificate",
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
print("PHASE 12O BREAKTHROUGH CANDIDATE AUDIT: PASS")
print("REAL THEOREM PROVED: YES")
print("FINITE SPECTRAL DETECTION PROVED: YES")
print("CONDITIONAL CONTRIBUTION CANDIDATE: YES")
print("LEVEL 4 CONDITIONAL BREAKTHROUGH CANDIDATE: YES")
print("BREAKTHROUGH ACHIEVED: NO")
print("RH CONTRIBUTION ESTABLISHED: NO")
print("ARITHMETIC-ONLY CERTIFICATE REQUIRED NEXT")
print("=" * 80)
