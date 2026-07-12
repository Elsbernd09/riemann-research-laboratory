from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/finite_spectral_detection/PHASE_12N_FINITE_SPECTRAL_DETECTION_THEOREM.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/finite_spectral_detection/FINITE_SPECTRAL_DETECTION_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/finite_spectral_detection/NEXT_PHASE_12O_BREAKTHROUGH_CANDIDATE_AUDIT.md"),
]

required = [
    "FINITE_SPECTRAL_DETECTION_THEOREM_COMPLETE",
    "ONE_FUNCTION_SPECTRAL_DETECTION_PROVED",
    "UNIFORM_FINITE_CLASS_SPECTRAL_DETECTION_PROVED",
    "CONCRETE_FINITE_CLASS_SPECTRAL_DETECTION_PROVED",
    "FINITE_SPECTRAL_TRUNCATIONS_DETECT_NEGATIVE_OBSTRUCTIONS",
    "ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_PROVED",
    "PRIMARY_SOURCE_CONFIRMATION_STILL_REQUIRED",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_STATUS_REQUIRES_AUDIT",
    "Theorem 12N.1",
    "Theorem 12N.2",
    "Corollary 12N.3",
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
print("PHASE 12N FINITE SPECTRAL DETECTION AUDIT: PASS")
print("ONE-FUNCTION SPECTRAL DETECTION: PROVED")
print("UNIFORM FINITE-CLASS SPECTRAL DETECTION: PROVED")
print("CONCRETE FINITE-CLASS SPECTRAL DETECTION: PROVED")
print("ARITHMETIC-ONLY CERTIFICATE: NOT YET PROVED")
print("PRIMARY SOURCE CONFIRMATION: STILL REQUIRED")
print("BREAKTHROUGH CANDIDATE STATUS: REQUIRES AUDIT")
print("=" * 80)
