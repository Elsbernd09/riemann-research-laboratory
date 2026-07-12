from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/symbolic_majorants/PHASE_10AA_KSTAR_DERIVATIVE_MAJORANTS.md"),
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/symbolic_majorants/SYMBOLIC_MAJORANT_LOCK.md"),
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/symbolic_majorants/PHASE_10AA_STATUS.md"),
]

required = [
    "KSTAR_DERIVATIVE_MAJORANTS",
    "SYMBOLIC_H_KERNEL_LIPSCHITZ_CANDIDATE",
    "COMPUTABLE_LIPSCHITZ_BOUND",
    "NO_FULL_LIPSCHITZ_THEOREM_YET",
    "M_0=A_0+2|c_t|C_0A_0^2",
    "M_x=A_1+2|c_t|C_0A_0A_1",
    "M_y=A_1+2|c_t|(A_0^2+C_0A_0A_1)",
    "L_x=2|t|B_0M_x",
    "L_y=2|t|(B_1M_0+B_0M_y)",
    "L_H(U,t)=L_x+L_y",
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
print("PHASE 10AA KSTAR DERIVATIVE MAJORANTS AUDIT: PASS")
print("KSTAR MAJORANTS: LOCKED")
print("H-KERNEL DERIVATIVE MAJORANTS: LOCKED")
print("SYMBOLIC LIPSCHITZ CANDIDATE: LOCKED")
print("FULL LIPSCHITZ THEOREM: NOT YET")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
