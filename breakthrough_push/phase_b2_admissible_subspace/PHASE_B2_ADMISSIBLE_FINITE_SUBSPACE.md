# Phase B2 — Admissible Finite Subspace Machinery

## Purpose

Phase B1 identified a serious missing condition:

\[
\widehat g(0)=0,
\qquad
\widehat g(1)=0.
\]

These are pole-removal constraints needed for the true Weil criterion setting.

Phase B2 builds the finite-dimensional machinery that enforces these constraints.

---

# 1. Finite basis

Let

\[
\phi_1,\dots,\phi_m
\]

be finite test functions with Mellin transforms defined at \(0\) and \(1\).

For

\[
g=\sum_{j=1}^{m}a_j\phi_j,
\]

linearity gives:

\[
\widehat g(0)=\sum_{j=1}^{m}a_j\widehat{\phi_j}(0),
\]

\[
\widehat g(1)=\sum_{j=1}^{m}a_j\widehat{\phi_j}(1).
\]

---

# 2. Constraint matrix

Define the pole constraint matrix:

\[
C
=
\begin{pmatrix}
\widehat{\phi_1}(0)&\widehat{\phi_2}(0)&\cdots&\widehat{\phi_m}(0)\\
\widehat{\phi_1}(1)&\widehat{\phi_2}(1)&\cdots&\widehat{\phi_m}(1)
\end{pmatrix}.
\]

The admissible coefficient space is:

\[
\mathcal N=\ker C.
\]

Thus:

\[
a\in\mathcal N
\Longleftrightarrow
\widehat g(0)=0,\quad \widehat g(1)=0.
\]

---

# 3. Nullspace-restricted matrix

Let

\[
M
\]

be any finite matrix representing a quadratic form on the coefficient space.

Let

\[
N
\]

be a matrix whose columns form a basis for

\[
\ker C.
\]

Then every admissible coefficient vector has the form:

\[
a=Nb.
\]

The restricted quadratic form is:

\[
a^*Ma
=
b^*(N^*MN)b.
\]

Therefore the admissible finite matrix is:

\[
M_{\mathrm{adm}}=N^*MN.
\]

---

# Theorem B2.1 — admissible matrix restriction

Let \(C\) be the pole constraint matrix and let \(N\) have columns spanning \(\ker C\).

If \(M\) represents a finite quadratic form on coefficient vectors \(a\), then the restriction of this quadratic form to pole-admissible finite test functions is represented by:

\[
M_{\mathrm{adm}}=N^*MN.
\]

## Proof

Every admissible coefficient vector satisfies:

\[
Ca=0.
\]

Since the columns of \(N\) span \(\ker C\), every such vector can be written:

\[
a=Nb.
\]

Then:

\[
a^*Ma=(Nb)^*M(Nb)=b^*N^*MNb.
\]

Thus the restricted matrix is:

\[
M_{\mathrm{adm}}=N^*MN.
\]

\[
\square
\]

---

# 4. Breakthrough relevance

This is a real correction to the previous framework.

The earlier finite spectral detection theorem worked on generic compactly supported finite test classes.

The upgraded version must work on:

\[
\mathcal F_{R,\mathrm{adm}}^{(m)}
=
\left\{
g=\sum_{j=1}^{m}a_j\phi_j:
\|a\|_2\le R,\ Ca=0
\right\}.
\]

This aligns the finite-dimensional model more closely with the true Weil criterion.

---

# 5. Implementation

Phase B2 implements:

1. numerical Mellin values at \(s=0,1\) for toy basis functions;
2. constraint matrix \(C\);
3. numerical nullspace calculation;
4. matrix restriction \(M_{\mathrm{adm}}=N^TMN\);
5. certificate output.

This is still prototype-level for the toy basis, but the algebraic theorem is exact.

---

# 6. Next target

Phase B3 should combine the admissible subspace with the existing toy arithmetic matrix prototype.

The goal is:

\[
M_{\mathrm{toy,adm}}=N^TM_{\mathrm{toy}}N.
\]

Then run Rayleigh logic on the admissible subspace.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a breakthrough.

This phase does not prove novelty.

This phase does not prove a certified arithmetic-only matrix.

Exact audit strings:

PHASE_B2_ADMISSIBLE_SUBSPACE_COMPLETE

POLE_CONSTRAINT_MATRIX_DEFINED

ADMISSIBLE_NULLSPACE_DEFINED

ADMISSIBLE_MATRIX_RESTRICTION_PROVED

M_ADM_EQUALS_N_STAR_M_N

TOY_MELLIN_CONSTRAINTS_COMPUTED

TOY_NULLSPACE_COMPUTED

BREAKTHROUGH_NOT_ACHIEVED

READY_FOR_PHASE_B3_ADMISSIBLE_TOY_MATRIX

