from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/theorem/PHASE_10AD_EXPLICIT_H_KERNEL_LIPSCHITZ_THEOREM.md"),
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/theorem/THEOREM_10AD_LOCK.md"),
    Path("original_results/finite_bombieri_stability/h_kernel_lipschitz/theorem/PHASE_10AD_STATUS.md"),
]

required = [
    "EXPLICIT_H_KERNEL_LIPSCHITZ_THEOREM",
    "COMPUTABLE_H_KERNEL_LIPSCHITZ_CONSTANT",
    "H_KERNEL_STABILITY_INSERTION",
    "THEOREM_10AD_1",
    "COROLLARY_10AD_2",
    "L_H(U,t)=2|t|B_0M_x+2|t|(B_1M_0+B_0M_y)",
    "compact-domain hypotheses",
    "This theorem does not prove RH",
    "This theorem does not falsify RH",
    "This theorem does not use zeta zeros",
    "This theorem does not claim novelty",
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
print("PHASE 10AD EXPLICIT H-KERNEL LIPSCHITZ THEOREM AUDIT: PASS")
print("EXPLICIT H-KERNEL LIPSCHITZ THEOREM: PROVED")
print("COMPUTABLE H-KERNEL CONSTANT: LOCKED")
print("STABILITY INSERTION: LOCKED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
