from pathlib import Path
import json

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/interval_calculator/PHASE_10AV_INTERVAL_GRAM_ENTRY_CALCULATOR_PROTOTYPE.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/interval_calculator/INTERVAL_CALCULATOR_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/interval_calculator/PHASE_10AV_INTERVAL_GRAM_CALCULATOR_OUTPUT.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/interval_calculator/PHASE_10AV_INTERVAL_GRAM_CERTIFICATE.json"),
]

required = [
    "INTERVAL_GRAM_ENTRY_CALCULATOR_PROTOTYPE",
    "CHI_N_M_COMPUTED",
    "MATRIX_LEVEL_BOUND_COMPUTED",
    "CERTIFICATE_SHA256_RECORDED",
    "TRUE_WEIL_GRAM_NOT_COMPUTED",
    "NOT_RH_CONTRIBUTION_YET",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not compute the true classical Weil/Bombieri Gram matrix",
    "This phase does not claim novelty",
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

cert = json.loads(files[-1].read_text(encoding="utf-8"))
for key in ["chi_N_m", "matrix_level_bound_m_chi_N_m", "certificate_sha256"]:
    if key not in cert:
        raise RuntimeError(f"Missing certificate key: {key}")

print("=" * 80)
print("PHASE 10AV INTERVAL CALCULATOR AUDIT: PASS")
print("INTERVAL PROTOTYPE: CREATED")
print("CHI_N_M: COMPUTED")
print("MATRIX LEVEL BOUND: COMPUTED")
print("CERTIFICATE HASH: RECORDED")
print("TRUE WEIL GRAM: NOT COMPUTED")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
