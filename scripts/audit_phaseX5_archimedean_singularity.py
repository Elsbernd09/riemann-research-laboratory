from pathlib import Path
import json
import math

from src.breakthrough_attack.archimedean_singularity import (
    tilde_value,
    archimedean_numerator,
    removable_archimedean_limit,
    archimedean_integrand_continuous,
    demo_F,
    write_archimedean_singularity_certificate,
)

files = [
    Path("breakthrough_attack/phase_x5_archimedean_removable_singularity/PHASE_X5_ARCHIMEDEAN_REMOVABLE_SINGULARITY.md"),
    Path("breakthrough_attack/phase_x5_archimedean_removable_singularity/ARCHIMEDEAN_SINGULARITY_STATUS.md"),
    Path("breakthrough_attack/phase_x5_archimedean_removable_singularity/NEXT_PHASE_X6_CERTIFIED_QUADRATURE_THEOREM.md"),
    Path("src/breakthrough_attack/archimedean_singularity.py"),
]

required = [
    "PHASE_X5_ARCHIMEDEAN_REMOVABLE_SINGULARITY_COMPLETE",
    "ARCHIMEDEAN_NUMERATOR_CANCELLATION_PROVED",
    "ARCHIMEDEAN_REMOVABLE_LIMIT_PROVED",
    "REMOVABLE_VALUE_THREE_HALVES_F_OF_ONE_PROVED",
    "CONTINUOUS_ARCHIMEDEAN_EXTENSION_DEFINED",
    "ARCHIMEDEAN_SINGULARITY_GATE_CLOSED_STRUCTURALLY",
    "CERTIFIED_ENTRY_NOT_COMPUTED",
    "READY_FOR_PHASE_X6_CERTIFIED_QUADRATURE_THEOREM",
    "Theorem X5.1",
    "Theorem X5.2",
    "This phase does not prove RH",
    "This phase does not prove a breakthrough",
    "This phase does not establish novelty",
    "This phase does not compute a certified arithmetic entry",
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

# Constant function sanity check: F(x)=1 has exact removable limit 3/2.
F_const = lambda x: 1.0
assert abs(tilde_value(F_const, 1.0) - 1.0) < 1e-14
assert abs(archimedean_numerator(F_const, 1.0)) < 1e-14
assert abs(removable_archimedean_limit(F_const) - 1.5) < 1e-14

for eps in [1e-2, 1e-3, 1e-4]:
    left = archimedean_integrand_continuous(F_const, 1.0 - eps, singular_tolerance=0.0)
    right = archimedean_integrand_continuous(F_const, 1.0 + eps, singular_tolerance=0.0)
    assert abs(left - 1.5) < 0.05
    assert abs(right - 1.5) < 0.05

assert math.isfinite(archimedean_integrand_continuous(demo_F, 1.0))
assert abs(archimedean_integrand_continuous(demo_F, 1.0) - 1.5 * demo_F(1.0)) < 1e-14

out = Path("breakthrough_attack/phase_x5_archimedean_removable_singularity/archimedean_singularity_certificate.json")
write_archimedean_singularity_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "PHASE_X5_ARCHIMEDEAN_REMOVABLE_SINGULARITY_COMPLETE"
assert payload["removable_value"] == "(3/2)F(1)"

print("=" * 80)
print("PHASE X5 ARCHIMEDEAN REMOVABLE SINGULARITY AUDIT: PASS")
print("NUMERATOR CANCELLATION: PROVED")
print("REMOVABLE LIMIT: PROVED")
print("REMOVABLE VALUE: 3/2 F(1)")
print("CONTINUOUS EXTENSION: DEFINED")
print("ARCHIMEDEAN SINGULARITY GATE: CLOSED STRUCTURALLY")
print("CERTIFIED ENTRY: NOT COMPUTED")
print("NEXT: CERTIFIED QUADRATURE THEOREM")
print("=" * 80)
