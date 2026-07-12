from __future__ import annotations

from pathlib import Path
import importlib.util
import re
import math

base = Path("weil_reconstruction/eigenvalue_validation")
out_path = base / "PHASE_9G_EXECUTE_TRACK_SPEC_OUTPUT.txt"

final_spec = base / "PHASE_9G_FINAL_SYNTHETIC_VALIDATION_SPEC.md"
repair_spec = base / "PHASE_9G_REPRESENTATION_REPAIR_SPEC.md"
manual_spec = base / "PHASE_9G_MANUAL_AUDIT_SPEC.md"
unknown_spec = base / "PHASE_9G_UNKNOWN_TRACK_STOP.md"

def write(lines: list[str]) -> None:
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

if final_spec.exists():
    track = "FINAL_SYNTHETIC_VALIDATION_SUITE"

    phase9b = load_module(
        "phase9b",
        Path("scripts/run_phase9b_synthetic_eigenvalue_validation.py"),
    )
    hma = phase9b.hma

    cases = {
        "all_real_small": hma.SyntheticGamma.from_values([-2, 0, 2]),
        "all_real_larger": hma.SyntheticGamma.from_values([-3, -1, 0, 1, 3]),
        "one_nonreal_pair": hma.SyntheticGamma.from_values([
            1 + 0.3j, 1 - 0.3j, -1 + 0.3j, -1 - 0.3j,
        ]),
        "two_nonreal_pairs": hma.SyntheticGamma.from_values([
            1 + 0.3j, 1 - 0.3j, -1 + 0.3j, -1 - 0.3j,
            2 + 0.2j, 2 - 0.2j, -2 + 0.2j, -2 - 0.2j,
        ]),
        "repeated_real": hma.SyntheticGamma.from_values([1, 1, -1, -1]),
        "repeated_nonreal_pair": hma.SyntheticGamma.from_values([
            1 + 0.3j, 1 + 0.3j, 1 - 0.3j, 1 - 0.3j,
        ]),
        "mixed_real_nonreal": hma.SyntheticGamma.from_values([
            -2, 0, 2, 1 + 0.25j, 1 - 0.25j,
        ]),
        "near_real_nonreal_stress": hma.SyntheticGamma.from_values([
            1 + 1e-3j, 1 - 1e-3j, -1 + 1e-3j, -1 - 1e-3j,
        ]),
    }

    t_values = [0.75, 1.25, 2.0]
    rows = []
    total = 0
    passed = 0
    blocked = 0
    mismatched = 0

    for case_name, gamma in cases.items():
        expected = gamma.distinct_conjugate_pair_count()
        for t in t_values:
            total += 1
            best_name = None
            best_matrix = None
            best_residual = float("inf")

            for candidate_name, matrix in phase9b.candidate_matrices(gamma, t):
                residual = phase9b.hermitian_residual(matrix)
                if residual < best_residual:
                    best_name = candidate_name
                    best_matrix = matrix
                    best_residual = residual

            if best_matrix is None or best_residual > phase9b.HERMITIAN_TOL:
                blocked += 1
                rows.append(
                    f"{case_name} | t={t} | selected=NONE | residual={best_residual:.6e} "
                    f"| status=BLOCKED | expected={expected}"
                )
                continue

            eigs = phase9b.hermitian_eigenvalues(best_matrix)
            nneg = phase9b.negative_count(eigs)
            nzero = phase9b.zero_count(eigs)
            ok = nneg == expected

            if ok:
                passed += 1
            else:
                mismatched += 1

            rows.append(
                f"{case_name} | t={t} | selected={best_name} | residual={best_residual:.6e} "
                f"| negative_count={nneg} | numerical_zero_count={nzero} | expected={expected} "
                f"| match={ok} | eigenvalues={[format(v, '.6e') for v in eigs]}"
            )

    status = "FINAL_SYNTHETIC_VALIDATION_COMPLETE"
    if blocked or mismatched:
        conclusion = "FINAL_SYNTHETIC_VALIDATION_HAS_BLOCKS_OR_MISMATCHES"
    else:
        conclusion = "FINAL_SYNTHETIC_VALIDATION_PASSED_ALL_TESTED_CASES"

    write([
        "PHASE 9G EXECUTE TRACK SPEC OUTPUT",
        f"TRACK={track}",
        f"STATUS={status}",
        f"CONCLUSION={conclusion}",
        "",
        f"total_case_t_pairs={total}",
        f"passed={passed}",
        f"blocked={blocked}",
        f"mismatched={mismatched}",
        "",
        "Rows:",
        *rows,
        "",
        "Boundary:",
        "  Synthetic finite Gamma cases only.",
        "  No zeta zeros used.",
        "  No RH claim.",
        "  No novelty claim.",
        "  No zeta-case Bombieri-Weil verification claim.",
    ])

elif repair_spec.exists():
    track = "REPRESENTATION_REPAIR_REQUIRED"

    phase9b_path = base / "PHASE_9B_SYNTHETIC_EIGENVALUE_OUTPUT.txt"
    phase9c_path = base / "PHASE_9C_REPRESENTATION_NORMALIZATION_AUDIT_OUTPUT.txt"

    phase9b_text = phase9b_path.read_text(encoding="utf-8") if phase9b_path.exists() else ""
    phase9c_text = phase9c_path.read_text(encoding="utf-8") if phase9c_path.exists() else ""

    residuals = re.findall(r"candidate=(.*?) hermitian_residual=([0-9.eE+-]+)", phase9b_text)
    blocked_cases = re.findall(r"CASE:\s*(.*?)\n(?:.*?\n)*?\s+STRICT_GATE_RESULT=BLOCKED", phase9b_text)
    mismatches = re.findall(r"CASE:\s*(.*?)\n(?:.*?\n)*?\s+theorem8_synthetic_match=False", phase9b_text)

    best_candidate = "UNRESOLVED"
    best_value = float("inf")
    for cand, val in residuals:
        try:
            numeric = float(val)
        except ValueError:
            continue
        if numeric < best_value:
            best_candidate = cand
            best_value = numeric

    repair_file = base / "PHASE_9G_REPRESENTATION_REPAIR_EXECUTION.md"
    repair_file.write_text(
        f"""# Phase 9G — Representation Repair Execution

## Track

\[
\texttt{{REPRESENTATION\_REPAIR\_REQUIRED}}
\]

## Diagnostic result

The current representation is not locked.

Best parsed Hermitian residual candidate:

\[
\texttt{{{best_candidate}}}
\]

with residual

\[
{best_value}
\]

## Parsed blocked cases

{chr(10).join('- ' + c.strip() for c in blocked_cases) if blocked_cases else '- No blocked cases parsed.'}

## Parsed mismatched cases

{chr(10).join('- ' + c.strip() for c in mismatches) if mismatches else '- No mismatches parsed.'}

## Repair conclusion

The next mathematical/software step is not broader validation.

The next step is a source-normalization repair focused on:

1. the \(K^*(x,y;t)\) formula;
2. the closed-form \(H(x,y;t)\) formula;
3. the denominator convention \(1/4+y^2\);
4. weighted inner-product interpretation;
5. similarity symmetrization;
6. repeated-\(\gamma\) handling.

## Boundary

No new eigenvalues computed in Phase 9G repair execution.

No zeta zeros used.

No RH proof.

No novelty claim.

No zeta-case Bombieri-Weil verification claim.
""",
        encoding="utf-8",
    )

    write([
        "PHASE 9G EXECUTE TRACK SPEC OUTPUT",
        f"TRACK={track}",
        "STATUS=REPRESENTATION_REPAIR_EXECUTION_COMPLETE",
        "CONCLUSION=REPRESENTATION_REMAINS_NOT_LOCKED",
        "",
        f"best_residual_candidate={best_candidate}",
        f"best_residual_value={best_value}",
        f"blocked_cases_parsed={len(blocked_cases)}",
        f"mismatches_parsed={len(mismatches)}",
        "",
        "Next target:",
        "  Source-normalization repair before broader validation.",
        "",
        "Boundary:",
        "  No new eigenvalues computed in Phase 9G repair execution.",
        "  No zeta zeros used.",
        "  No RH claim.",
        "  No novelty claim.",
        "  No zeta-case Bombieri-Weil verification claim.",
    ])

elif manual_spec.exists() or unknown_spec.exists():
    track = "MANUAL_OR_UNKNOWN"
    write([
        "PHASE 9G EXECUTE TRACK SPEC OUTPUT",
        f"TRACK={track}",
        "STATUS=STOP_FOR_MANUAL_AUDIT",
        "",
        "No automatic execution was performed.",
        "Inspect Phase 9B through Phase 9F outputs manually.",
        "",
        "Boundary:",
        "  No eigenvalues computed in Phase 9G.",
        "  No zeta zeros used.",
        "  No RH claim.",
        "  No novelty claim.",
    ])

else:
    track = "NO_SPEC_FOUND"
    write([
        "PHASE 9G EXECUTE TRACK SPEC OUTPUT",
        f"TRACK={track}",
        "STATUS=NO_PHASE_9G_SPEC_FOUND",
        "",
        "No Phase 9G spec file was detected.",
        "Stop and inspect Phase 9F.",
        "",
        "Boundary:",
        "  No eigenvalues computed in Phase 9G.",
        "  No zeta zeros used.",
        "  No RH claim.",
        "  No novelty claim.",
    ])

print("=" * 80)
print("PHASE 9G EXECUTE TRACK SPEC: COMPLETE")
print(f"TRACK: {track}")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
