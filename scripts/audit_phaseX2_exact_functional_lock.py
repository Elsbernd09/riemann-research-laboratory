from pathlib import Path
import json

from src.breakthrough_attack.exact_functional_lock import (
    ExactFunctionalLock,
    write_exact_functional_lock_certificate,
)

files = [
    Path("breakthrough_attack/phase_x2_exact_functional_lock/PHASE_X2_EXACT_FUNCTIONAL_LOCK.md"),
    Path("breakthrough_attack/phase_x2_exact_functional_lock/EXACT_FUNCTIONAL_LOCK_STATUS.md"),
    Path("breakthrough_attack/phase_x2_exact_functional_lock/NEXT_PHASE_X3_BUILT_IN_POLE_CANCELLED_SMOOTH_BASIS.md"),
    Path("src/breakthrough_attack/exact_functional_lock.py"),
]

required = [
    "PHASE_X2_EXACT_FUNCTIONAL_LOCK_COMPLETE",
    "BOMBIERI_LAGARIAS_FUNCTIONAL_LOCKED",
    "LOG_PI_GAMMA_CONSTANT_LOCKED",
    "LOG_4PI_GAMMA_REJECTED_FOR_LOCKED_BRANCH",
    "TILDE_INVOLUTION_LOCKED",
    "HERMITIAN_STAR_DICTIONARY_LOCKED",
    "F_POLE_REMOVAL_TARGET_LOCKED",
    "G_POLE_CONSTRAINTS_MARKED_SUFFICIENT_NOT_NECESSARY",
    "FINITE_ARITHMETIC_MATRIX_TARGET_DEFINED",
    "CERTIFIED_MATRIX_GAP_TARGET_IDENTIFIED",
    "READY_FOR_PHASE_X3_BUILT_IN_POLE_CANCELLED_SMOOTH_BASIS",
    "Theorem X2.1",
    "Theorem X2.2",
    "This phase does not prove RH",
    "This phase does not prove a breakthrough",
    "This phase does not establish novelty",
    "This phase does not create a certified matrix",
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

lock = ExactFunctionalLock()
assert lock.name == "T_BL"
assert "log(pi)" in lock.constant_term
assert "log(4*pi)" in lock.rejected_constant
assert "tilde_f" in lock.tilde_involution
assert "f_star" in lock.hermitian_star
assert "hat_f(0)=hat_f(1)=0" == lock.official_pole_target

out = Path("breakthrough_attack/phase_x2_exact_functional_lock/exact_functional_lock_certificate.json")
write_exact_functional_lock_certificate(out)
payload = json.loads(out.read_text(encoding="utf-8"))
assert payload["status"] == "PHASE_X2_EXACT_FUNCTIONAL_LOCK_COMPLETE"
assert payload["allowed_constant"] == "log(pi)+EulerGamma"

print("=" * 80)
print("PHASE X2 EXACT FUNCTIONAL LOCK AUDIT: PASS")
print("FUNCTIONAL: BOMBIERI-LAGARIAS LOCKED")
print("CONSTANT: LOG PI + GAMMA LOCKED")
print("LOG 4PI + GAMMA: REJECTED FOR LOCKED BRANCH")
print("TILDE INVOLUTION: LOCKED")
print("HERMITIAN STAR DICTIONARY: LOCKED")
print("F-POLE TARGET: LOCKED")
print("G-POLE CONSTRAINTS: SUFFICIENT NOT NECESSARY")
print("FINITE ARITHMETIC MATRIX TARGET: DEFINED")
print("NEXT: BUILT-IN POLE-CANCELLED SMOOTH BASIS")
print("=" * 80)
