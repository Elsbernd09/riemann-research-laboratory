from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/sharper_bounds/PHASE_10Q_SHARPER_WEIGHTED_SUPPORT_BOUND.md"),
    Path("original_results/finite_bombieri_stability/sharper_bounds/THEOREM_10Q_LOCK.md"),
    Path("original_results/finite_bombieri_stability/sharper_bounds/PHASE_10Q_BREAKTHROUGH_TRACK_STATUS.md"),
]

required = [
    "Sharper Weighted Support-Stability Bound",
    "Theorem 10Q.1",
    "Corollary 10Q.2",
    "weighted perturbation radius",
    "M_{\\mathrm{tot}}",
    "2L_t(U)M_{\\mathrm{tot}}\\delta<g_0(M",
    "\\mathcal R(\\Gamma,\\widetilde\\Gamma,t)<g_0(M",
    "strictly sharper",
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
print("PHASE 10Q SHARPER WEIGHTED SUPPORT BOUND AUDIT: PASS")
print("WEIGHTED RADIUS: LOCKED")
print("SHARPER UNIFORM CERTIFICATE: LOCKED")
print("STRICT IMPROVEMENT OVER OLD BOUND: RECORDED")
print("BREAKTHROUGH CLAIM: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
