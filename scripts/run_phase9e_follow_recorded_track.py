from __future__ import annotations

from pathlib import Path
import re

decision_path = Path("weil_reconstruction/eigenvalue_validation/PHASE_9D_REPRESENTATION_DECISION_OUTPUT.txt")
phase9c_path = Path("weil_reconstruction/eigenvalue_validation/PHASE_9C_REPRESENTATION_NORMALIZATION_AUDIT_OUTPUT.txt")
phase9b_path = Path("weil_reconstruction/eigenvalue_validation/PHASE_9B_SYNTHETIC_EIGENVALUE_OUTPUT.txt")

out_path = Path("weil_reconstruction/eigenvalue_validation/PHASE_9E_FOLLOW_RECORDED_TRACK_OUTPUT.txt")

if not decision_path.exists():
    raise FileNotFoundError("Phase 9D decision output not found. Run Phase 9D first.")

decision_text = decision_path.read_text(encoding="utf-8")
phase9c_text = phase9c_path.read_text(encoding="utf-8") if phase9c_path.exists() else ""
phase9b_text = phase9b_path.read_text(encoding="utf-8") if phase9b_path.exists() else ""

if "NEXT_TRACK=FINAL_SYNTHETIC_VALIDATION_SUITE" in decision_text:
    track = "FINAL_SYNTHETIC_VALIDATION_SUITE"
elif "NEXT_TRACK=REPRESENTATION_REPAIR_REQUIRED" in decision_text:
    track = "REPRESENTATION_REPAIR_REQUIRED"
else:
    track = "MANUAL_AUDIT_REQUIRED"

lines = [
    "PHASE 9E FOLLOW RECORDED TRACK OUTPUT",
    "",
    f"TRACK={track}",
    "",
]

if track == "FINAL_SYNTHETIC_VALIDATION_SUITE":
    target_file = Path("weil_reconstruction/eigenvalue_validation/FINAL_SYNTHETIC_VALIDATION_PLAN.md")
    target_file.write_text(
        """# Final Synthetic Validation Plan

## Status

Phase 9D selected:

\[
\texttt{FINAL\_SYNTHETIC\_VALIDATION\_SUITE}
\]

This means the current synthetic representation passed the previous gate strongly enough to justify a broader synthetic validation phase.

## Next phase may do

The next phase may run a broader synthetic finite validation suite.

It may compute eigenvalues only for synthetic finite \(\Gamma\)-multisets.

It must keep:

1. Hermitian residual gates;
2. negative-eigenvalue tolerance;
3. numerical-zero tolerance;
4. honest mismatch logging;
5. no zeta-zero input.

## Next phase may not do

It may not use zeta zeros.

It may not claim RH progress.

It may not claim novelty.

It may not claim zeta-case Bombieri-Weil verification.

## Boundary

Synthetic finite validation is not the zeta limiting theorem.

Bombieri Sections 10 and 11 remain source-extraction targets before zeta-zero experiments.
""",
        encoding="utf-8",
    )

    lines.extend([
        "Created: FINAL_SYNTHETIC_VALIDATION_PLAN.md",
        "Next target: broader synthetic validation suite.",
        "No new eigenvalues computed in Phase 9E.",
        "No zeta zeros used.",
        "No RH claim.",
        "No novelty claim.",
    ])

elif track == "REPRESENTATION_REPAIR_REQUIRED":
    target_file = Path("weil_reconstruction/eigenvalue_validation/REPRESENTATION_REPAIR_DIAGNOSTIC.md")

    residual_lines = re.findall(
        r"candidate=(.*?) hermitian_residual=([0-9.eE+-]+)",
        phase9b_text,
    )

    blocked_cases = re.findall(
        r"CASE:\s*(.*?)\n(?:.*?\n)*?\s+STRICT_GATE_RESULT=BLOCKED",
        phase9b_text,
    )

    mismatches = re.findall(
        r"CASE:\s*(.*?)\n(?:.*?\n)*?\s+theorem8_synthetic_match=False",
        phase9b_text,
    )

    residual_summary = "\n".join(
        f"- {candidate}: {value}"
        for candidate, value in residual_lines
    ) or "- No residuals parsed."

    blocked_summary = "\n".join(f"- {case.strip()}" for case in blocked_cases) or "- No blocked cases parsed."
    mismatch_summary = "\n".join(f"- {case.strip()}" for case in mismatches) or "- No mismatches parsed."

    target_file.write_text(
        f"""# Representation Repair Diagnostic

## Status

Phase 9D selected:

\[
\texttt{{REPRESENTATION\_REPAIR\_REQUIRED}}
\]

This means the finite representation is not locked.

## Parsed Hermitian residuals

{residual_summary}

## Parsed blocked cases

{blocked_summary}

## Parsed mismatched cases

{mismatch_summary}

## Repair priorities

The next phase should repair the representation in this order:

1. Re-check the source extraction of \(K^*(x,y;t)\).
2. Re-check the source extraction of \(H(x,y;t)=2tK^*(x,y;t)/(1/4+y^2)\).
3. Re-check whether the closed form for \(H(x,y;t)\) should replace the \(K^*\)-formula for implementation.
4. Re-check the denominator convention: \(1/4+y^2\) versus source-variable normalization.
5. Re-check whether rows and columns require a weighted inner-product interpretation.
6. Re-check whether the similarity transform should be applied before the Hermitian gate.
7. Re-check repeated-\(\gamma\) handling.
8. Re-run synthetic validation only after the repair is explicit.

## Important interpretation

A failed synthetic validation is not a contradiction of Bombieri's theorem.

It means the project implementation or convention extraction is incomplete.

## Boundary

No new eigenvalues are computed in Phase 9E.

No zeta zeros are used.

No RH proof.

No novelty claim.

No zeta-case Bombieri-Weil verification claim.
""",
        encoding="utf-8",
    )

    lines.extend([
        "Created: REPRESENTATION_REPAIR_DIAGNOSTIC.md",
        "Next target: source-normalization repair before broader validation.",
        "No new eigenvalues computed in Phase 9E.",
        "No zeta zeros used.",
        "No RH claim.",
        "No novelty claim.",
    ])

else:
    target_file = Path("weil_reconstruction/eigenvalue_validation/MANUAL_AUDIT_REQUIRED.md")
    target_file.write_text(
        """# Manual Audit Required

Phase 9E could not parse the Phase 9D next track.

Do not proceed to validation.

Inspect:

- `PHASE_9D_REPRESENTATION_DECISION_OUTPUT.txt`
- `PHASE_9C_REPRESENTATION_NORMALIZATION_AUDIT_OUTPUT.txt`
- `PHASE_9B_SYNTHETIC_EIGENVALUE_OUTPUT.txt`

Boundary:

No new eigenvalues.

No zeta zeros.

No RH claim.

No novelty claim.
""",
        encoding="utf-8",
    )

    lines.extend([
        "Created: MANUAL_AUDIT_REQUIRED.md",
        "Next target: manual inspection.",
        "No new eigenvalues computed in Phase 9E.",
        "No zeta zeros used.",
        "No RH claim.",
        "No novelty claim.",
    ])

out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

print("=" * 80)
print("PHASE 9E FOLLOW RECORDED TRACK: COMPLETE")
print(f"TRACK: {track}")
print("NO NEW EIGENVALUES COMPUTED IN PHASE 9E")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
