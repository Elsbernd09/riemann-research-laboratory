from __future__ import annotations

from pathlib import Path
import re

input_path = Path("weil_reconstruction/eigenvalue_validation/PHASE_9B_SYNTHETIC_EIGENVALUE_OUTPUT.txt")
output_path = Path("weil_reconstruction/eigenvalue_validation/PHASE_9C_REPRESENTATION_NORMALIZATION_AUDIT_OUTPUT.txt")

if not input_path.exists():
    raise FileNotFoundError("Phase 9B output not found. Run Phase 9B first.")

text = input_path.read_text(encoding="utf-8")

case_blocks = re.split(r"\nCASE:\s+", text)
header = case_blocks[0]
cases = case_blocks[1:]

summary = {
    "total_cases": 0,
    "blocked_cases": 0,
    "passed_gate_cases": 0,
    "matched_cases": 0,
    "mismatched_cases": 0,
}

records = []

for block in cases:
    lines = block.strip().splitlines()
    if not lines:
        continue

    name = lines[0].strip()
    case_text = "\n".join(lines)

    summary["total_cases"] += 1

    blocked = "STRICT_GATE_RESULT=BLOCKED" in case_text
    passed_gate = "STRICT_GATE_RESULT=PASSED" in case_text
    matched = "theorem8_synthetic_match=True" in case_text
    mismatched = "theorem8_synthetic_match=False" in case_text

    if blocked:
        summary["blocked_cases"] += 1
    if passed_gate:
        summary["passed_gate_cases"] += 1
    if matched:
        summary["matched_cases"] += 1
    if mismatched:
        summary["mismatched_cases"] += 1

    selected = "NONE"
    m = re.search(r"selected_candidate=(.*)", case_text)
    if m:
        selected = m.group(1).strip()

    residuals = re.findall(r"candidate=(.*?) hermitian_residual=([0-9.eE+-]+)", case_text)

    records.append({
        "name": name,
        "blocked": blocked,
        "passed_gate": passed_gate,
        "matched": matched,
        "mismatched": mismatched,
        "selected": selected,
        "residuals": residuals,
    })

all_cases_clean = (
    summary["total_cases"] > 0
    and summary["blocked_cases"] == 0
    and summary["mismatched_cases"] == 0
    and summary["matched_cases"] == summary["total_cases"]
)

if all_cases_clean:
    lock_status = "PRELIMINARY_SYNTHETIC_LOCK_POSSIBLE"
    decision = (
        "All synthetic Phase 9B cases passed the strict gate and matched the Theorem 8 target. "
        "This supports a preliminary synthetic representation lock, but it is not yet a zeta-case conclusion."
    )
else:
    lock_status = "REPRESENTATION_NOT_LOCKED"
    decision = (
        "At least one synthetic case was blocked or mismatched. "
        "The finite representation is not locked. The next phase must repair normalization, Hermitian conversion, "
        "or multiplicity handling before any stronger validation."
    )

out_lines = [
    "PHASE 9C REPRESENTATION NORMALIZATION AUDIT OUTPUT",
    "",
    "Input:",
    str(input_path),
    "",
    "Summary:",
    f"  total_cases={summary['total_cases']}",
    f"  blocked_cases={summary['blocked_cases']}",
    f"  passed_gate_cases={summary['passed_gate_cases']}",
    f"  matched_cases={summary['matched_cases']}",
    f"  mismatched_cases={summary['mismatched_cases']}",
    "",
    f"REPRESENTATION_LOCK_STATUS={lock_status}",
    f"Decision: {decision}",
    "",
    "Case records:",
]

for rec in records:
    out_lines.extend([
        f"- case={rec['name']}",
        f"  blocked={rec['blocked']}",
        f"  passed_gate={rec['passed_gate']}",
        f"  matched={rec['matched']}",
        f"  mismatched={rec['mismatched']}",
        f"  selected_candidate={rec['selected']}",
        "  residuals:",
    ])

    for cand, residual in rec["residuals"]:
        out_lines.append(f"    {cand}: {residual}")

    out_lines.append("")

out_lines.extend([
    "Boundary:",
    "  No new eigenvalues computed in Phase 9C.",
    "  No zeta zeros used.",
    "  No RH claim.",
    "  No novelty claim.",
    "  No zeta-case Bombieri-Weil verification claim.",
    "",
])

output_path.write_text("\n".join(out_lines), encoding="utf-8")

print("=" * 80)
print("PHASE 9C REPRESENTATION NORMALIZATION AUDIT: COMPLETE")
print(f"REPRESENTATION_LOCK_STATUS: {lock_status}")
print(f"TOTAL CASES: {summary['total_cases']}")
print(f"BLOCKED CASES: {summary['blocked_cases']}")
print(f"MISMATCHED CASES: {summary['mismatched_cases']}")
print("NO NEW EIGENVALUES COMPUTED IN PHASE 9C")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
