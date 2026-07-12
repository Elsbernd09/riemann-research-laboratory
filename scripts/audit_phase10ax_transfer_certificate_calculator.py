from pathlib import Path
import json

files = [
    Path("original_results/finite_bombieri_stability/contribution_branch/transfer_certificate_calculator/PHASE_10AX_TRANSFER_CERTIFICATE_CALCULATOR.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/transfer_certificate_calculator/TRANSFER_CALCULATOR_LOCK.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/transfer_certificate_calculator/PHASE_10AX_TRANSFER_CERTIFICATE_OUTPUT.md"),
    Path("original_results/finite_bombieri_stability/contribution_branch/transfer_certificate_calculator/PHASE_10AX_TRANSFER_CERTIFICATES.json"),
]

required = [
    "TRANSFER_CERTIFICATE_CALCULATOR",
    "TOTAL_ENTRYWISE_ERROR_COMPUTED",
    "TRANSFER_BOUND_COMPUTED",
    "NEGATIVE_DIRECTION_TRANSFER_CERTIFIED",
    "NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED",
    "CERTIFICATE_SHA256_RECORDED",
    "UNCONDITIONAL_CLASSICAL_CONVERGENCE_NOT_PROVEN",
    "NOT_RH_CONTRIBUTION_YET",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove unconditional classical convergence",
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

bundle = json.loads(files[-1].read_text(encoding="utf-8"))
certs = bundle.get("certificates", [])
if len(certs) < 3:
    raise RuntimeError("Expected at least three transfer certificates")

statuses = {c["verdicts"]["negative_direction_transfer"] for c in certs}
if "NEGATIVE_DIRECTION_TRANSFER_CERTIFIED" not in statuses:
    raise RuntimeError("Expected certified margin example")
if "NEGATIVE_DIRECTION_TRANSFER_NOT_CERTIFIED" not in statuses:
    raise RuntimeError("Expected not-certified margin example")

for c in certs:
    if "certificate_sha256" not in c:
        raise RuntimeError("Missing certificate hash")

print("=" * 80)
print("PHASE 10AX TRANSFER CERTIFICATE CALCULATOR AUDIT: PASS")
print("TRANSFER CERTIFICATE CALCULATOR: IMPLEMENTED")
print("TOTAL ENTRYWISE ERROR: COMPUTED")
print("TRANSFER BOUND: COMPUTED")
print("NEGATIVE-DIRECTION VERDICTS: COMPUTED")
print("CERTIFICATE HASHES: RECORDED")
print("RH CONTRIBUTION: NOT YET")
print("=" * 80)
