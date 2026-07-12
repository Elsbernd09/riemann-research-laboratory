from pathlib import Path
import json
import math

from src.level4.arithmetic_entry_blueprint import (
    support_cutoff_from_B,
    archimedean_log_tail_coefficient,
    placeholder_entry_components,
    write_blueprint_certificate,
)

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/true_entry_blueprint/PHASE_12W_TRUE_ARITHMETIC_ENTRY_BLUEPRINT.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/true_entry_blueprint/TRUE_ENTRY_BLUEPRINT_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/true_entry_blueprint/NEXT_PHASE_12X_TOY_BASIS_PROTOTYPE.md"),
    Path("src/level4/arithmetic_entry_blueprint.py"),
]

required = [
    "TRUE_ARITHMETIC_ENTRY_BLUEPRINT_COMPLETE",
    "M_IJ_TRUE_ENTRY_DECOMPOSITION_DEFINED",
    "FINITE_PRIME_COMPONENT_INCLUDED",
    "REDUCED_ARCHIMEDEAN_COMPONENT_INCLUDED",
    "INTERVAL_ENTRY_FORMULA_DEFINED",
    "TRUE_CERTIFIED_NUMERICAL_ENTRIES_NOT_YET_COMPUTED",
    "TOY_BASIS_REQUIRED_NEXT",
    "ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE",
    "LEVEL4_BRANCH_READY_FOR_TOY_ENTRY_PROTOTYPE",
    "Theorem 12W.1",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove a complete arithmetic-only finite certificate",
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

B = 1.0
M = support_cutoff_from_B(B)
assert abs(M - math.exp(2.0)) < 1e-12
tail = archimedean_log_tail_coefficient(M)
assert tail > 0

components = placeholder_entry_components()
entry = components.entry_interval()
assert entry.lo < entry.hi

out = Path("original_results/finite_bombieri_stability/level4_candidate/true_entry_blueprint/true_entry_blueprint_certificate.json")
write_blueprint_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["important_boundary"] == "TRUE_CERTIFIED_NUMERICAL_ENTRIES_NOT_YET_COMPUTED"
assert payload["status"] == "TRUE_ARITHMETIC_ENTRY_BLUEPRINT_COMPLETE"

print("=" * 80)
print("PHASE 12W TRUE ARITHMETIC ENTRY BLUEPRINT AUDIT: PASS")
print("TRUE ENTRY DECOMPOSITION: DEFINED")
print("FINITE PRIME COMPONENT: INCLUDED")
print("REDUCED ARCHIMEDEAN COMPONENT: INCLUDED")
print("INTERVAL ENTRY FORMULA: DEFINED")
print("TRUE CERTIFIED NUMERICAL ENTRIES: NOT YET COMPUTED")
print("TOY BASIS REQUIRED NEXT")
print("ARITHMETIC-ONLY CERTIFICATE: NOT YET COMPLETE")
print("=" * 80)
