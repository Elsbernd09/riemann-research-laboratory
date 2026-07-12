from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/compact_majorants/PHASE_10AB_CONCRETE_COMPACT_DOMAIN_MAJORANTS.md"),
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/compact_majorants/COMPACT_MAJORANT_LOCK.md"),
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/compact_majorants/PHASE_10AB_STATUS.md"),
]

required = [
    "CONCRETE_COMPACT_DOMAIN_MAJORANTS",
    "A0_EXP_MAJORANT",
    "A1_CAUCHY_MAJORANT",
    "RATIONAL_FACTOR_MAJORANTS",
    "COMPUTABLE_H_KERNEL_MAJORANT_PACKAGE",
    "NO_FULL_LIPSCHITZ_THEOREM_YET",
    "A_0=e^{|t|S}",
    "A_1=\\frac{\\exp(|t|(S+r))}{r}",
    "B_0=\\frac{1}{\\Delta_Y}",
    "B_1=\\frac{2\\rho_y}{\\Delta_Y^2}",
    "C_0=\\frac12+\\rho_y",
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
print("PHASE 10AB COMPACT MAJORANTS AUDIT: PASS")
print("A0 EXP MAJORANT: LOCKED")
print("A1 CAUCHY MAJORANT: LOCKED")
print("RATIONAL FACTOR MAJORANTS: LOCKED")
print("COMPUTABLE H-KERNEL MAJORANT PACKAGE: LOCKED")
print("FULL LIPSCHITZ THEOREM: NOT YET")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
