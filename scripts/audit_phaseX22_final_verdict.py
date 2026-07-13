from pathlib import Path
import json

from src.breakthrough_attack.final_breakthrough_candidate_verdict import (
    build_final_verdict,
    write_final_verdict,
)

files = [
    Path("breakthrough_attack/phase_x22_final_breakthrough_candidate_verdict/PHASE_X22_FINAL_BREAKTHROUGH_CANDIDATE_VERDICT.md"),
    Path("breakthrough_attack/phase_x22_final_breakthrough_candidate_verdict/PROFESSOR_REVIEW_PACKET.md"),
    Path("breakthrough_attack/phase_x22_final_breakthrough_candidate_verdict/FINAL_VERDICT_STATUS.md"),
    Path("breakthrough_attack/phase_x22_final_breakthrough_candidate_verdict/NEXT_CERTIFICATION_HARDENING_BRANCH.md"),
    Path("src/breakthrough_attack/final_breakthrough_candidate_verdict.py"),
]

required = [
    "PHASE_X22_FINAL_BREAKTHROUGH_CANDIDATE_VERDICT_COMPLETE",
    "FINAL_VERDICT_CONTRIBUTION_CANDIDATE_REQUIRING_EXPERT_REVIEW",
    "PROOF_OF_RH_NOT_CLAIMED",
    "CONFIRMED_BREAKTHROUGH_NOT_CLAIMED",
    "CERTIFIED_FINITE_WEIL_MATRIX_NOT_COMPUTED",
    "CERTIFICATION_GATES_EXPLICITLY_LISTED",
    "PROFESSOR_REVIEW_PACKET_CREATED",
    "NO_NOVELTY_CLAIM_BEFORE_PRIOR_ART_REVIEW",
    "BREAKTHROUGH_ATTACK_BRANCH_COMPLETE",
    "READY_FOR_PROFESSOR_REVIEW_OR_NEXT_CERTIFICATION_HARDENING_BRANCH",
    "Theorem X22.1",
    "Theorem X22.2",
    "This phase does not prove RH",
    "This phase does not prove a confirmed breakthrough",
    "This phase does not establish novelty",
    "This phase does not compute a certified finite Weil matrix",
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

verdict = build_final_verdict()
assert verdict.final_verdict == "CONTRIBUTION_CANDIDATE_REQUIRING_EXPERT_REVIEW"
assert verdict.proof_of_rh_claimed is False
assert verdict.confirmed_breakthrough_claimed is False
assert verdict.novelty_claimed is False
assert verdict.certified_finite_weil_matrix_computed is False
assert verdict.contribution_candidate is True
assert verdict.required_expert_review is True
assert "certified pointwise convolution enclosures" in verdict.unresolved_gates

out = Path("breakthrough_attack/phase_x22_final_breakthrough_candidate_verdict/final_breakthrough_candidate_verdict.json")
write_final_verdict(out)
saved = json.loads(out.read_text(encoding="utf-8"))
assert saved["status"] == "PHASE_X22_FINAL_BREAKTHROUGH_CANDIDATE_VERDICT_COMPLETE"
assert saved["verdict"]["final_verdict"] == "CONTRIBUTION_CANDIDATE_REQUIRING_EXPERT_REVIEW"
assert saved["verdict"]["proof_of_rh_claimed"] is False
assert saved["verdict"]["confirmed_breakthrough_claimed"] is False

print("=" * 80)
print("PHASE X22 FINAL BREAKTHROUGH-CANDIDATE VERDICT AUDIT: PASS")
print("FINAL VERDICT: CONTRIBUTION CANDIDATE REQUIRING EXPERT REVIEW")
print("PROOF OF RH: NOT CLAIMED")
print("CONFIRMED BREAKTHROUGH: NOT CLAIMED")
print("CERTIFIED FINITE WEIL MATRIX: NOT COMPUTED")
print("PROFESSOR REVIEW PACKET: CREATED")
print("BREAKTHROUGH ATTACK BRANCH: COMPLETE")
print("=" * 80)
