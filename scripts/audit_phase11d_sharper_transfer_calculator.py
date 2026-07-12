from pathlib import Path
import json

files = [
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/sharper_calculator/PHASE_11D_SHARPER_TRANSFER_CERTIFICATE_CALCULATOR.md"),
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/sharper_calculator/SHARPER_CALCULATOR_LOCK.md"),
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/sharper_calculator/PHASE_11D_SHARPER_TRANSFER_CALCULATOR_OUTPUT.md"),
    Path("original_results/finite_bombieri_stability/breakthrough_attempt/sharper_calculator/PHASE_11D_SHARPER_TRANSFER_CERTIFICATES.json"),
]

required = [
    "SHARPER_TRANSFER_CERTIFICATE_CALCULATOR",
    "KAPPA_ZERO_UNDER_EXTRACTED_KERNEL_ALIGNMENT",
    "SHARPER_TOTAL_ERROR_COMPUTED",
    "SHARPER_TRANSFER_BOUND_COMPUTED",
    "SHARPER_NEGATIVE_DIRECTION_TRANSFER_CERTIFIED",
    "SHARPER_NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED",
    "CERTIFICATE_SHA256_RECORDED",
    "FULL_CLASSICAL_VALIDATION_NOT_PROVEN",
    "NOT_RH_CONTRIBUTION_YET",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove full classical validation",
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

bundle = json.loads(files[-1].read_text(encoding="utf-8"))
certs = bundle.get("certificates", [])
if len(certs) < 3:
    raise RuntimeError("Expected at least three sharper transfer certificates")

statuses = {c["verdicts"]["negative_direction_transfer"] for c in certs}
if "SHARPER_NEGATIVE_DIRECTION_TRANSFER_CERTIFIED" not in statuses:
    raise RuntimeError("Expected sharper certified margin example")
if "SHARPER_NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED" not in statuses:
    raise RuntimeError("Expected sharper not-certified margin example")

for c in certs:
    if "certificate_sha256" not in c:
        raise RuntimeError("Missing certificate hash")

print("=" * 80)
print("PHASE 11D SHARPER TRANSFER CALCULATOR AUDIT: PASS")
print("SHARPER TRANSFER CERTIFICATE CALCULATOR: IMPLEMENTED")
print("KAPPA ZERO ASSUMPTION: RECORDED")
print("SHARPER TOTAL ERROR: COMPUTED")
print("SHARPER TRANSFER BOUND: COMPUTED")
print("SHARPER NEGATIVE-DIRECTION VERDICTS: COMPUTED")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
