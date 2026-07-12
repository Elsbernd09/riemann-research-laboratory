# Phase 12Z — Toy Arithmetic Matrix Prototype

## Purpose

Phase 12X implemented a toy basis.

Phase 12Y implemented a toy arithmetic entry prototype.

Phase 12Z assembles a small toy arithmetic matrix and runs the interval matrix certificate logic.

This completes the toy pipeline:

\[
\text{basis}
\to
\text{entry}
\to
\text{matrix}
\to
\text{interval wrapper}
\to
\text{Rayleigh test}.
\]

---

# 1. Toy matrix definition

For the toy basis

\[
\phi_1,\dots,\phi_m,
\]

define approximate floating-point entries

\[
\widetilde M_{ij}^{arith}
\approx
T[\phi_j*\phi_i^*].
\]

The matrix is assembled as

\[
\widetilde M^{arith}
=
(\widetilde M_{ij}^{arith})_{i,j=1}^{m}.
\]

---

# 2. Crude interval wrapper

Since Phase 12Y is floating-point only, Phase 12Z wraps each approximate entry in a crude interval:

\[
\widetilde M_{ij}^{arith}\in
[\widetilde M_{ij}^{arith}-r,\widetilde M_{ij}^{arith}+r].
\]

This is not rigorous certification.

It only tests the interval-matrix pipeline.

---

# 3. Symmetrization option

Because the prototype entries are floating-point and not rigorously Hermitian, Phase 12Z constructs a toy symmetric matrix by replacing

\[
\widetilde M
\]

with

\[
\widetilde M_H=\frac12(\widetilde M+\widetilde M^T).
\]

This is a prototype engineering step.

It is not a theorem about the exact arithmetic matrix.

---

# 4. Rayleigh test

Given a vector \(v\), compute the interval Rayleigh quotient

\[
v^T\mathbf M_Hv.
\]

If the upper endpoint is negative, the toy interval matrix has a certified negative direction relative to the crude interval wrapper.

This does not imply RH failure or success.

It only validates the certificate machinery.

---

# 5. What this phase achieves

Phase 12Z proves the toy arithmetic matrix pipeline is executable.

It creates a small finite matrix from toy arithmetic entries and runs the interval certificate logic.

This is the final computational prototype before audit and packaging.

---

# 6. What this phase does not achieve

It does not produce a certified arithmetic-only RH certificate.

It does not compute theorem-level \(C_c^\infty\) entries.

It does not prove Hermitian symmetry of the true arithmetic matrix.

It does not prove or disprove RH.

It does not establish novelty.

---

# 7. Next target

Phase 13A should perform the final honest results audit.

It should classify:

1. proven theorems;
2. conditional theorems;
3. provisional source imports;
4. toy computations;
5. missing source validation;
6. missing certified quadrature;
7. what is ready for professor review.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove a complete arithmetic-only finite certificate.

This phase does not establish novelty.

Exact audit strings:

TOY_ARITHMETIC_MATRIX_PROTOTYPE_COMPLETE

TOY_ARITHMETIC_MATRIX_ASSEMBLED

TOY_MATRIX_INTERVAL_WRAPPER_CREATED

TOY_HERMITIAN_SYMMETRIZATION_PERFORMED

TOY_RAYLEIGH_INTERVAL_COMPUTED

TOY_NEGATIVE_DIRECTION_LOGIC_TESTED

FLOATING_POINT_TOY_PIPELINE_ONLY

CERTIFIED_ARITHMETIC_MATRIX_NOT_YET_PROVED

READY_FOR_FINAL_RESULTS_AUDIT

