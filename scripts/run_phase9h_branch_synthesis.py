from __future__ import annotations

from pathlib import Path

base = Path("weil_reconstruction/eigenvalue_validation")
out = Path("weil_reconstruction/synthesis/PHASE_9H_FINITE_VALIDATION_BRANCH_STATUS.txt")

phase9g = base / "PHASE_9G_EXECUTE_TRACK_SPEC_OUTPUT.txt"
phase9e = base / "PHASE_9E_FOLLOW_RECORDED_TRACK_OUTPUT.txt"
phase9d = base / "PHASE_9D_REPRESENTATION_DECISION_OUTPUT.txt"
phase9c = base / "PHASE_9C_REPRESENTATION_NORMALIZATION_AUDIT_OUTPUT.txt"
phase9b = base / "PHASE_9B_SYNTHETIC_EIGENVALUE_OUTPUT.txt"

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""

texts = {
    "9G": read(phase9g),
    "9E": read(phase9e),
    "9D": read(phase9d),
    "9C": read(phase9c),
    "9B": read(phase9b),
}

if "REPRESENTATION_REPAIR_REQUIRED" in texts["9G"] or "REPRESENTATION_REMAINS_NOT_LOCKED" in texts["9G"]:
    branch_status = "REPRESENTATION_REPAIR_REQUIRED"
elif "FINAL_SYNTHETIC_VALIDATION_PASSED_ALL_TESTED_CASES" in texts["9G"]:
    branch_status = "FINAL_SYNTHETIC_VALIDATION_PASSED"
elif "FINAL_SYNTHETIC_VALIDATION_HAS_BLOCKS_OR_MISMATCHES" in texts["9G"]:
    branch_status = "FINAL_SYNTHETIC_VALIDATION_HAS_BLOCKS_OR_MISMATCHES"
elif "STOP_FOR_MANUAL_AUDIT" in texts["9G"]:
    branch_status = "MANUAL_AUDIT_REQUIRED"
else:
    branch_status = "UNRESOLVED"

lines = [
    "PHASE 9H FINITE VALIDATION BRANCH STATUS",
    "",
    f"BRANCH_STATUS={branch_status}",
    "",
    "What is source-extracted:",
    "  - Bombieri T[f] functional.",
    "  - Bombieri Hermitian positivity mechanism.",
    "  - Section 8 finite approximation skeleton.",
    "  - H-kernel formula at source-note level.",
    "  - Bombieri Theorem 8 statement.",
    "  - Repeated-gamma zero-eigenvalue warning.",
    "",
    "What is implemented:",
    "  - Scalar K, K_t, K*, H kernel functions.",
    "  - Synthetic Gamma multiset model.",
    "  - Full multiset matrix assembly.",
    "  - Distinct weighted matrix assembly.",
    "  - Synthetic eigenvalue validation attempt with strict gates.",
    "  - Representation decision workflow.",
    "",
    "What is not done:",
    "  - No zeta zeros used.",
    "  - No Bombieri Sections 10-11 zeta limiting theorem extracted.",
    "  - No zeta-case finite truncation claim.",
    "  - No RH proof.",
    "  - No novelty claim.",
    "",
]

if branch_status == "REPRESENTATION_REPAIR_REQUIRED":
    lines.extend([
        "Interpretation:",
        "  The synthetic finite validation branch exposed a representation/convention issue.",
        "  This is not a contradiction of Bombieri's theorem.",
        "  The next technical target would be source-normalization repair.",
        "",
        "Recommended stop point:",
        "  Stop the finite eigenvalue branch here unless continuing into repair.",
        "  The branch is useful as a carefully documented reconstruction and implementation audit.",
    ])
elif branch_status == "FINAL_SYNTHETIC_VALIDATION_PASSED":
    lines.extend([
        "Interpretation:",
        "  The synthetic finite validation suite passed the tested cases.",
        "  This remains finite synthetic validation only.",
        "  It does not transfer to zeta zeros without Sections 10-11 source extraction.",
        "",
        "Recommended stop point:",
        "  Stop here before zeta-zero experiments.",
        "  The next serious step would be extracting Bombieri Sections 10-11.",
    ])
else:
    lines.extend([
        "Interpretation:",
        "  The branch status is unresolved or mixed.",
        "  Manual audit is recommended before more computation.",
        "",
        "Recommended stop point:",
        "  Stop here and inspect Phase 9B-9G outputs.",
    ])

lines.extend([
    "",
    "Boundary:",
    "  No zeta zeros used.",
    "  No RH claim.",
    "  No novelty claim.",
    "  No zeta-case Bombieri-Weil verification claim.",
    "",
])

out.write_text("\n".join(lines), encoding="utf-8")

print("=" * 80)
print("PHASE 9H FINITE VALIDATION BRANCH SYNTHESIS: COMPLETE")
print(f"BRANCH_STATUS: {branch_status}")
print("NO ZETA ZEROS USED")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
