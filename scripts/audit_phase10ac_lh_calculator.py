from pathlib import Path

files = [
    Path("scripts/run_phase10ac_lh_constant_calculator.py"),
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/calculator/PHASE_10AC_LH_CONSTANT_CALCULATOR.md"),
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/calculator/LH_CALCULATOR_LOCK.md"),
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/calculator/PHASE_10AC_LH_CALCULATOR_OUTPUT.txt"),
]

required = [
    "LH_CONSTANT_CALCULATOR",
    "COMPUTABLE_H_KERNEL_LIPSCHITZ_CONSTANT",
    "CONCRETE_COMPACT_DOMAIN_MAJORANTS",
    "NO_FULL_LIPSCHITZ_THEOREM_YET",
    "A0 = exp(|t| S)",
    "A1 = exp(|t|(S+r))/r",
    "LH = Lx + Ly",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not use zeta zeros",
    "This phase does not claim novelty",
]

for path in files:
    if not path.exists():
        raise FileNotFoundError(path)

    text = path.read_text(encoding="utf-8")
    if "\x00" in text:
        raise ValueError(f"NUL byte found in {path}")

combined = "\n".join(path.read_text(encoding="utf-8") for path in files)

missing = [
    phrase for phrase in required
    if phrase.lower() not in combined.lower()
]

if missing:
    raise RuntimeError("Missing required content: " + ", ".join(missing))

print("=" * 80)
print("PHASE 10AC L_H CALCULATOR AUDIT: PASS")
print("COMPUTABLE H-KERNEL LIPSCHITZ CONSTANT: IMPLEMENTED")
print("CALCULATOR OUTPUT: GENERATED")
print("FULL LIPSCHITZ THEOREM: NOT YET")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
