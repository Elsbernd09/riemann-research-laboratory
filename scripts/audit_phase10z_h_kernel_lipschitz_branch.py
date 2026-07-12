from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/PHASE_10Z_H_KERNEL_LIPSCHITZ_BRANCH.md"),
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/H_KERNEL_LIPSCHITZ_TARGET_LOCK.md"),
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/DERIVATIVE_MAJORANT_PLAN.md"),
]

required = [
    "H_KERNEL_LIPSCHITZ_BRANCH",
    "EXPLICIT_H_KERNEL_LIPSCHITZ_TARGET",
    "COMPUTABLE_LIPSCHITZ_BOUND",
    "NO_FULL_LIPSCHITZ_THEOREM_YET",
    "K_t'(z)",
    "A_0(U,t)",
    "A_1(U,t)",
    "B_0(U)",
    "B_1(U)",
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
print("PHASE 10Z H-KERNEL LIPSCHITZ BRANCH AUDIT: PASS")
print("EXPLICIT H-KERNEL LIPSCHITZ TARGET: LOCKED")
print("DERIVATIVE MAJORANT STRATEGY: LOCKED")
print("FULL THEOREM STATUS: NOT YET")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
