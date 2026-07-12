from pathlib import Path
import json
import math

from src.level4.toy_matrix_prototype import (
    assemble_toy_matrix,
    symmetrize,
    interval_wrap,
    scan_negative_directions,
    write_toy_matrix_certificate,
)

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/toy_matrix_prototype/PHASE_12Z_TOY_ARITHMETIC_MATRIX_PROTOTYPE.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/toy_matrix_prototype/TOY_MATRIX_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/toy_matrix_prototype/NEXT_PHASE_13A_FINAL_RESULTS_AUDIT.md"),
    Path("src/level4/toy_matrix_prototype.py"),
]

required = [
    "TOY_ARITHMETIC_MATRIX_PROTOTYPE_COMPLETE",
    "TOY_ARITHMETIC_MATRIX_ASSEMBLED",
    "TOY_MATRIX_INTERVAL_WRAPPER_CREATED",
    "TOY_HERMITIAN_SYMMETRIZATION_PERFORMED",
    "TOY_RAYLEIGH_INTERVAL_COMPUTED",
    "TOY_NEGATIVE_DIRECTION_LOGIC_TESTED",
    "FLOATING_POINT_TOY_PIPELINE_ONLY",
    "CERTIFIED_ARITHMETIC_MATRIX_NOT_YET_PROVED",
    "READY_FOR_FINAL_RESULTS_AUDIT",
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

raw = assemble_toy_matrix(integral_steps=60, conv_steps=60)
assert len(raw) == 2 and len(raw[0]) == 2
assert all(math.isfinite(x) for row in raw for x in row)

sym = symmetrize(raw)
assert abs(sym[0][1] - sym[1][0]) < 1e-12

imat = interval_wrap(sym, radius=0.5)
results = scan_negative_directions(imat)
assert len(results) >= 2
assert all("rayleigh_interval" in r for r in results)

out = Path("original_results/finite_bombieri_stability/level4_candidate/toy_matrix_prototype/toy_matrix_certificate.json")
write_toy_matrix_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "TOY_ARITHMETIC_MATRIX_PROTOTYPE_COMPLETE"
assert payload["important_boundary"] == "FLOATING_POINT_TOY_PIPELINE_ONLY"

print("=" * 80)
print("PHASE 12Z TOY ARITHMETIC MATRIX AUDIT: PASS")
print("TOY ARITHMETIC MATRIX: ASSEMBLED")
print("INTERVAL WRAPPER: CREATED")
print("HERMITIAN SYMMETRIZATION: PERFORMED")
print("RAYLEIGH INTERVAL: COMPUTED")
print("NEGATIVE DIRECTION LOGIC: TESTED")
print("FLOATING POINT TOY PIPELINE ONLY")
print("CERTIFIED ARITHMETIC MATRIX: NOT YET PROVED")
print("READY FOR FINAL RESULTS AUDIT")
print("=" * 80)
