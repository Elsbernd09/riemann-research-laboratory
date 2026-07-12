from __future__ import annotations

import importlib.util
from pathlib import Path

module_path = Path("weil_reconstruction/finite_truncations/h_matrix_assembly.py")
spec = importlib.util.spec_from_file_location("h_matrix_assembly", module_path)
if spec is None or spec.loader is None:
    raise RuntimeError("Could not load h_matrix_assembly module")

hma = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hma)

t = 1.25
rows: list[str] = []

for name, gamma in hma.synthetic_cases().items():
    full = hma.assemble_full_multiset_matrix(gamma, t)
    distinct, multiplicities, weighted = hma.assemble_distinct_weighted_matrix(gamma, t)

    full_shape = hma.matrix_shape(full)
    weighted_shape = hma.matrix_shape(weighted)

    if full_shape != (gamma.size, gamma.size):
        raise AssertionError(f"{name}: bad full shape {full_shape}")

    if weighted_shape != (len(distinct), len(distinct)):
        raise AssertionError(f"{name}: bad weighted shape {weighted_shape}")

    if not hma.all_entries_finite(full):
        raise AssertionError(f"{name}: non-finite full matrix entry")

    if not hma.all_entries_finite(weighted):
        raise AssertionError(f"{name}: non-finite weighted matrix entry")

    full_residual = hma.hermitian_residual(full)
    weighted_residual = hma.hermitian_residual(weighted)

    rows.extend([
        f"CASE: {name}",
        f"  full_size={gamma.size}",
        f"  distinct_size={len(distinct)}",
        f"  multiplicities={{{', '.join(f'{repr(k)}: {v}' for k, v in multiplicities.items())}}}",
        f"  repeated_zero_warning_count={gamma.repeated_zero_warning_count()}",
        f"  distinct_conjugate_pair_count={gamma.distinct_conjugate_pair_count()}",
        f"  full_shape={full_shape}",
        f"  weighted_shape={weighted_shape}",
        f"  full_entries_finite=True",
        f"  weighted_entries_finite=True",
        f"  full_hermitian_residual_inspection={full_residual:.6e}",
        f"  weighted_hermitian_residual_inspection={weighted_residual:.6e}",
        "",
    ])

out = Path("weil_reconstruction/finite_truncations/PHASE_8Z_MATRIX_ASSEMBLY_OUTPUT.txt")
out.write_text(
    "\n".join([
        "PHASE 8Z MATRIX ASSEMBLY OUTPUT",
        "Synthetic finite Gamma cases only.",
        "Matrices assembled for shape/finiteness/symmetry-residual inspection only.",
        "No eigenvalues computed.",
        "No zeta zeros used.",
        "No RH claim.",
        "No novelty claim.",
        "",
    ] + rows),
    encoding="utf-8",
)

print("=" * 80)
print("PHASE 8Z MATRIX ASSEMBLY CHECKS: PASS")
print("SYNTHETIC FULL MULTISET MATRICES: ASSEMBLED")
print("SYNTHETIC DISTINCT WEIGHTED MATRICES: ASSEMBLED")
print("SHAPE CHECKS: PASS")
print("FINITE ENTRY CHECKS: PASS")
print("HERMITIAN RESIDUALS: INSPECTED ONLY")
print("EIGENVALUE COMPUTATION: NONE")
print("ZETA ZERO USE: NONE")
print("RH CLAIM: NONE")
print("NOVELTY CLAIM: NONE")
print("=" * 80)
