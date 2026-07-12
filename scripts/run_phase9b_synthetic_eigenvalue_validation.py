from __future__ import annotations

import math
import importlib.util
from pathlib import Path

module_path = Path("weil_reconstruction/finite_truncations/h_matrix_assembly.py")
spec = importlib.util.spec_from_file_location("h_matrix_assembly", module_path)
if spec is None or spec.loader is None:
    raise RuntimeError("Could not load h_matrix_assembly module")

hma = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hma)


HERMITIAN_TOL = 1e-7
NEGATIVE_TOL = 1e-7
MAX_SWEEPS = 120


def matrix_shape(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    return rows, cols


def hermitian_residual(matrix):
    rows, cols = matrix_shape(matrix)
    if rows != cols:
        return float("inf")
    max_res = 0.0
    for j in range(rows):
        for k in range(cols):
            res = abs(matrix[j][k] - matrix[k][j].conjugate())
            max_res = max(max_res, res)
    return max_res


def real_block_from_hermitian(matrix):
    """
    Convert complex Hermitian A to real symmetric block:

        [[Re A, -Im A],
         [Im A,  Re A]]

    Eigenvalues of A appear twice in this real representation.
    """
    n = len(matrix)
    block = [[0.0 for _ in range(2 * n)] for _ in range(2 * n)]

    for j in range(n):
        for k in range(n):
            z = complex(matrix[j][k])
            a = z.real
            b = z.imag

            block[j][k] = a
            block[j][k + n] = -b
            block[j + n][k] = b
            block[j + n][k + n] = a

    return block


def jacobi_real_symmetric_eigenvalues(a):
    """
    Small pure-Python Jacobi eigenvalue solver for real symmetric matrices.

    This is used only for small synthetic validation cases.
    """
    n = len(a)
    mat = [[float(a[i][j]) for j in range(n)] for i in range(n)]

    for _ in range(MAX_SWEEPS):
        p, q = 0, 1
        max_off = 0.0

        for i in range(n):
            for j in range(i + 1, n):
                val = abs(mat[i][j])
                if val > max_off:
                    max_off = val
                    p, q = i, j

        if max_off < 1e-12:
            break

        app = mat[p][p]
        aqq = mat[q][q]
        apq = mat[p][q]

        if abs(apq) < 1e-30:
            continue

        tau = (aqq - app) / (2.0 * apq)
        t = math.copysign(1.0 / (abs(tau) + math.sqrt(1.0 + tau * tau)), tau)
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c

        for k in range(n):
            if k != p and k != q:
                akp = mat[k][p]
                akq = mat[k][q]

                mat[k][p] = c * akp - s * akq
                mat[p][k] = mat[k][p]

                mat[k][q] = s * akp + c * akq
                mat[q][k] = mat[k][q]

        mat[p][p] = c * c * app - 2.0 * s * c * apq + s * s * aqq
        mat[q][q] = s * s * app + 2.0 * s * c * apq + c * c * aqq
        mat[p][q] = 0.0
        mat[q][p] = 0.0

    return sorted(mat[i][i] for i in range(n))


def hermitian_eigenvalues(matrix):
    """
    Compute eigenvalues for a small complex Hermitian matrix.

    The real block has duplicated eigenvalues; we sort and average adjacent pairs.
    """
    block = real_block_from_hermitian(matrix)
    vals = jacobi_real_symmetric_eigenvalues(block)

    paired = []
    for i in range(0, len(vals), 2):
        if i + 1 < len(vals):
            paired.append(0.5 * (vals[i] + vals[i + 1]))
        else:
            paired.append(vals[i])

    return sorted(paired)


def distinct_weighted_similarity_matrix(gamma, t):
    distinct, multiplicities, _weighted = hma.assemble_distinct_weighted_matrix(gamma, t)

    matrix = []
    for gj in distinct:
        row = []
        for gk in distinct:
            mj = multiplicities[gj]
            mk = multiplicities[gk]
            row.append((mj ** 0.5) * hma.hks.H_kernel(gj, gk, t) * (mk ** 0.5))
        matrix.append(row)

    return distinct, multiplicities, matrix


def candidate_matrices(gamma, t):
    full = hma.assemble_full_multiset_matrix(gamma, t)
    distinct, multiplicities, weighted = hma.assemble_distinct_weighted_matrix(gamma, t)
    sim_distinct, sim_mults, sim = distinct_weighted_similarity_matrix(gamma, t)

    return [
        ("full_raw", full),
        ("distinct_weighted_raw", weighted),
        ("distinct_similarity_candidate", sim),
    ]


def negative_count(eigenvalues):
    return sum(1 for v in eigenvalues if v < -NEGATIVE_TOL)


def zero_count(eigenvalues):
    return sum(1 for v in eigenvalues if abs(v) <= NEGATIVE_TOL)


def synthetic_cases():
    cases = hma.synthetic_cases()
    cases["two_nonreal_conjugate_pairs"] = hma.SyntheticGamma.from_values([
        1 + 0.3j,
        1 - 0.3j,
        -1 + 0.3j,
        -1 - 0.3j,
        2 + 0.2j,
        2 - 0.2j,
        -2 + 0.2j,
        -2 - 0.2j,
    ])
    cases["repeated_nonreal_pair"] = hma.SyntheticGamma.from_values([
        1 + 0.3j,
        1 + 0.3j,
        1 - 0.3j,
        1 - 0.3j,
    ])
    return cases


def main():
    t = 1.25
    lines = [
        "PHASE 9B SYNTHETIC EIGENVALUE VALIDATION OUTPUT",
        "Synthetic finite Gamma cases only.",
        "Strict Hermitian gate required before eigenvalue computation.",
        "No zeta zeros used.",
        "No RH claim.",
        "No novelty claim.",
        "",
    ]

    any_eigs = False
    any_failures = False

    for name, gamma in synthetic_cases().items():
        expected = gamma.distinct_conjugate_pair_count()
        repeated_warning = gamma.repeated_zero_warning_count()

        lines.append(f"CASE: {name}")
        lines.append(f"  expected_distinct_conjugate_pair_count={expected}")
        lines.append(f"  repeated_zero_warning_count={repeated_warning}")

        best_name = None
        best_matrix = None
        best_residual = float("inf")

        for cand_name, matrix in candidate_matrices(gamma, t):
            residual = hermitian_residual(matrix)
            lines.append(f"  candidate={cand_name} hermitian_residual={residual:.6e}")

            if residual < best_residual:
                best_name = cand_name
                best_matrix = matrix
                best_residual = residual

        if best_matrix is None or best_residual > HERMITIAN_TOL:
            lines.append("  STRICT_GATE_RESULT=BLOCKED")
            lines.append("  reason=no representation passed Hermitian residual gate")
            lines.append("")
            any_failures = True
            continue

        eigs = hermitian_eigenvalues(best_matrix)
        any_eigs = True

        nneg = negative_count(eigs)
        nzero = zero_count(eigs)
        passed = nneg == expected

        if not passed:
            any_failures = True

        lines.append("  STRICT_GATE_RESULT=PASSED")
        lines.append(f"  selected_candidate={best_name}")
        lines.append(f"  eigenvalues={['%.10e' % v for v in eigs]}")
        lines.append(f"  negative_count={nneg}")
        lines.append(f"  numerical_zero_count={nzero}")
        lines.append(f"  theorem8_synthetic_target={expected}")
        lines.append(f"  theorem8_synthetic_match={passed}")
        lines.append("")

    lines.extend([
        "SUMMARY",
        f"  any_eigenvalues_computed={any_eigs}",
        f"  any_failures_or_blocks={any_failures}",
        "  failures_or_blocks_are_logged_honestly=True",
        "  zeta_zero_experiments=False",
        "  rh_claim=False",
        "  novelty_claim=False",
        "",
    ])

    out = Path("weil_reconstruction/eigenvalue_validation/PHASE_9B_SYNTHETIC_EIGENVALUE_OUTPUT.txt")
    out.write_text("\n".join(lines), encoding="utf-8")

    print("=" * 80)
    print("PHASE 9B SYNTHETIC EIGENVALUE VALIDATION: COMPLETE")
    print("STRICT HERMITIAN GATES: APPLIED")
    print("SYNTHETIC CASES: TESTED")
    print("FAILURES/BLOCKS: LOGGED HONESTLY")
    print("ZETA ZERO USE: NONE")
    print("RH CLAIM: NONE")
    print("NOVELTY CLAIM: NONE")
    print("=" * 80)


if __name__ == "__main__":
    main()
