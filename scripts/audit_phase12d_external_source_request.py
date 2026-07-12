from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/external_source_request/PHASE_12D_EXTERNAL_SOURCE_REVIEW_PACKAGE.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/external_source_request/PROFESSOR_EMAIL_DRAFT.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/external_source_request/SOURCE_REVIEW_CHECKLIST.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/external_source_request/NEXT_PHASE_AFTER_SOURCE_REVIEW.md"),
]

required = [
    "EXTERNAL_SOURCE_REVIEW_PACKAGE_CREATED",
    "F_G_SOURCE_REQUEST_CREATED",
    "TRUE_Q_W_SOURCE_REQUEST_CREATED",
    "ADMISSIBLE_DOMAIN_SOURCE_REQUEST_CREATED",
    "SIGN_CONVENTION_SOURCE_REQUEST_CREATED",
    "FINITE_APPROXIMATION_MAP_REQUEST_CREATED",
    "SOURCE_REVIEW_REQUIRED_BEFORE_LEVEL4",
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
print("PHASE 12D EXTERNAL SOURCE REVIEW PACKAGE AUDIT: PASS")
print("SOURCE REVIEW PACKAGE: CREATED")
print("F_g REQUEST: CREATED")
print("Q_W REQUEST: CREATED")
print("DOMAIN REQUEST: CREATED")
print("SIGN CONVENTION REQUEST: CREATED")
print("FINITE APPROXIMATION MAP REQUEST: CREATED")
print("LEVEL 4 BREAKTHROUGH CANDIDATE: NOT YET ACHIEVED")
print("=" * 80)
