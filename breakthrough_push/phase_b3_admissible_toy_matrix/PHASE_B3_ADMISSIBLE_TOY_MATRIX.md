# Phase B3 — Admissible Toy Matrix

## Purpose

Phase B1 identified the missing pole-removal constraints:

\[
\widehat g(0)=0,
\qquad
\widehat g(1)=0.
\]

Phase B2 built the nullspace restriction machinery:

\[
M_{\mathrm{adm}}=N^*MN.
\]

Phase B3 applies that machinery to a toy arithmetic matrix.

---

# 1. Toy arithmetic matrix

Let

\[
M_{\mathrm{toy}}
\]

be the floating-point toy arithmetic matrix assembled from toy entries

\[
T[\phi_j*\phi_i^*].
\]

This matrix is not certified.

It is used only to test the admissible-subspace pipeline.

---

# 2. Pole constraint matrix

For basis functions

\[
\phi_1,\dots,\phi_m,
\]

define:

\[
C
=
\begin{pmatrix}
\widehat{\phi_1}(0)&\cdots&\widehat{\phi_m}(0)\\
\widehat{\phi_1}(1)&\cdots&\widehat{\phi_m}(1)
\end{pmatrix}.
\]

The admissible coefficient space is:

\[
\ker C.
\]

Let

\[
N
\]

be a matrix whose columns span

\[
\ker C.
\]

---

# 3. Admissible toy matrix

Define:

\[
M_{\mathrm{toy,adm}}=N^TM_{\mathrm{toy}}N.
\]

This is the toy arithmetic form restricted to finite test functions satisfying:

\[
\widehat g(0)=0,
\qquad
\widehat g(1)=0.
\]

---

# Theorem B3.1 — admissible toy matrix restriction

Assume \(N\) has columns spanning \(\ker C\). Then every coefficient vector \(b\) in the restricted coordinate space defines an admissible coefficient vector:

\[
a=Nb
\]

satisfying

\[
Ca=0.
\]

Moreover,

\[
a^TM_{\mathrm{toy}}a
=
b^TM_{\mathrm{toy,adm}}b.
\]

## Proof

Since columns of \(N\) span \(\ker C\), for every \(b\),

\[
a=Nb\in\ker C.
\]

Therefore:

\[
Ca=0.
\]

The quadratic form becomes:

\[
a^TM_{\mathrm{toy}}a
=
(Nb)^TM_{\mathrm{toy}}(Nb)
=
b^TN^TM_{\mathrm{toy}}Nb.
\]

By definition:

\[
M_{\mathrm{toy,adm}}=N^TM_{\mathrm{toy}}N.
\]

Thus:

\[
a^TM_{\mathrm{toy}}a
=
b^TM_{\mathrm{toy,adm}}b.
\]

\[
\square
\]

---

# 4. Certificate logic

Phase B3 wraps the restricted matrix in crude intervals and runs Rayleigh interval tests.

If a negative direction appears, it is only a toy result.

It does not imply RH failure.

It only verifies that the admissible-subspace certificate pipeline works.

---

# 5. What this phase achieves

Phase B3 proves and implements the pipeline:

\[
\text{toy arithmetic matrix}
\to
\text{pole-admissible nullspace}
\to
\text{restricted matrix}
\to
\text{interval Rayleigh test}.
\]

This is a genuine structural improvement over the earlier toy matrix prototype because it now respects the pole-removal constraints.

---

# 6. What remains

Still needed for a true breakthrough attempt:

1. primary-source convention validation;
2. theorem-level \(C_c^\infty\) basis with pole constraints;
3. certified arithmetic entries;
4. certified quadrature;
5. complex interval arithmetic;
6. prior-art comparison;
7. expert review.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a breakthrough.

This phase does not prove novelty.

This phase does not prove a certified arithmetic-only matrix.

Exact audit strings:

PHASE_B3_ADMISSIBLE_TOY_MATRIX_COMPLETE

TOY_ARITHMETIC_MATRIX_ASSEMBLED_FOR_ADMISSIBLE_TEST

POLE_CONSTRAINT_MATRIX_USED

ADMISSIBLE_NULLSPACE_USED

TOY_ADMISSIBLE_MATRIX_COMPUTED

TOY_ADMISSIBLE_RAYLEIGH_LOGIC_TESTED

POLE_ORTHOGONAL_PIPELINE_IMPLEMENTED

BREAKTHROUGH_NOT_ACHIEVED

READY_FOR_PHASE_B4_PRIOR_ART_COLLISION

