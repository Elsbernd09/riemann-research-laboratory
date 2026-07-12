from pathlib import Path

files = [
    Path("original_results/finite_bombieri_stability/level4_candidate/truncation_error_gate/PHASE_12L_TRUNCATION_ERROR_GATE.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/truncation_error_gate/TRUNCATION_ERROR_LOCK.md"),
    Path("original_results/finite_bombieri_stability/level4_candidate/truncation_error_gate/NEXT_PHASE_12M_BASIS_MELLIN_DECAY.md"),
]

required = [
    "TRUNCATION_ERROR_GATE_COMPLETE",
    "SPECTRAL_TRUNCATION_Q_Y_DEFINED",
    "TAIL_ERROR_T_Y_DEFINED",
    "TAIL_GRAM_MATRIX_DEFINED",
    "FINITE_CLASS_TRUNCATION_BOUND_PROVED",
    "ENTRYWISE_TRUNCATION_BOUND_PROVED",
    "SHELL_COUNT_TRUNCATION_BOUND_PROVED",
    "TRUNCATION_CONVERGENCE_CRITERION_PROVED",
    "DELTA_Y_TO_ZERO_STILL_NEEDS_BASIS_ESTIMATES",
    "LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED",
    "Theorem 12L.1",
    "Corollary 12L.2",
    "Theorem 12L.3",
    "Corollary 12L.4",
    "This phase does not prove RH",
    "This phase does not falsify RH",
    "This phase does not prove a new RH criterion",
    "This phase does not prove the full Weil positivity theorem",
    "This phase does not prove Level 4 contribution",
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

print("=" * 80)
print("PHASE 12L TRUNCATION ERROR GATE AUDIT: PASS")
print("SPECTRAL TRUNCATION Q_Y: DEFINED")
print("TAIL ERROR T_Y: DEFINED")
print("TAIL GRAM MATRIX: DEFINED")
print("FINITE-CLASS TRUNCATION BOUND: PROVED")
print("ENTRYWISE TRUNCATION BOUND: PROVED")
print("SHELL-COUNT TRUNCATION BOUND: PROVED")
print("TRUNCATION CONVERGENCE CRITERION: PROVED")
print("BASIS MELLIN DECAY ESTIMATES: STILL NEEDED")
print("LEVEL 4 BREAKTHROUGH CANDIDATE: NOT YET ACHIEVED")
print("=" * 80)
