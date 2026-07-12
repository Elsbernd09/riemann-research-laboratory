# Phase B1 — Provisional Primary-Source Lock

## Purpose

Phase B1 begins the breakthrough-push branch.

The goal is to lock the exact Weil/Bombieri conventions needed for the project:

\[
g^*(x)=x^{-1}\overline{g(1/x)}
\]

\[
F_g=g*g^*
\]

\[
Q_W(g)=T[F_g]
\]

\[
T[F_g]\ge0
\]

as the RH-equivalent positivity condition.

This phase is marked provisional because the current source package is a search-summary guide, not yet a primary-source extraction from the original papers.

---

# 1. Imported convention candidates

The uploaded source summary states the standard arithmetic involution as

\[
g^*(x)=x^{-1}\overline{g(1/x)}.
\]

It gives multiplicative convolution with Haar measure \(dy/y\):

\[
F_g(x)=(g*g^*)(x).
\]

It records the Mellin transform identity:

\[
\widehat{F_g}(s)
=
\widehat g(s)\overline{\widehat g(1-\bar s)}.
\]

On the critical line \(s=1/2+it\), this becomes

\[
\widehat{F_g}(1/2+it)
=
|\widehat g(1/2+it)|^2.
\]

It also records the positivity target:

\[
T[F_g]\ge0
\]

for all admissible \(g\), equivalent to RH under the stated Weil criterion.

---

# 2. Admissible function candidates

The uploaded source summary gives the test-function space as

\[
g\in C_c^\infty(0,\infty).
\]

It also lists orthogonality/pole-removal conditions:

\[
\int_0^\infty g(x)\,dx=0,
\]

and

\[
\int_0^\infty g(x)x^{-1}\,dx=0.
\]

Equivalently, the Mellin transform should vanish at the pole locations:

\[
\widehat g(1)=0,
\qquad
\widehat g(0)=0.
\]

This is important because the earlier project did not enforce these pole-removal constraints.

---

# 3. Important correction to project status

The Level 4 project used compactly supported log-smooth test functions, but did not enforce:

\[
\widehat g(0)=0,
\qquad
\widehat g(1)=0.
\]

Therefore the prior finite spectral detection theorem should now be relabeled:

\[
\boxed{
\text{finite spectral detection theorem on provisional finite test classes}
}
\]

not yet:

\[
\boxed{
\text{finite spectral detection theorem on fully admissible Weil test classes}
}
\]

To enter the real Weil criterion, the finite test class must be restricted to the pole-orthogonal subspace.

---

# 4. Breakthrough relevance

This is a major gate.

If the admissibility constraints are required, then a true breakthrough-push version must modify the finite test class:

\[
\mathcal F_R^{(m)}
\]

to

\[
\mathcal F_{R,\mathrm{adm}}^{(m)}
=
\left\{
g=\sum_{j=1}^{m}a_j\phi_j:
\|a\|_2\le R,\ 
\widehat g(0)=0,\ 
\widehat g(1)=0
\right\}.
\]

This becomes a linear constraint on coefficient vectors:

\[
\sum_{j=1}^m a_j\widehat{\phi_j}(0)=0,
\]

\[
\sum_{j=1}^m a_j\widehat{\phi_j}(1)=0.
\]

That means the finite-dimensional matrix problem should be projected onto the nullspace of two pole-removal constraints.

---

# 5. Theorem B1.1 — finite admissible subspace construction

Let

\[
\phi_1,\dots,\phi_m
\]

be basis functions with Mellin transforms defined at \(0\) and \(1\).

Define the constraint matrix

\[
C=
\begin{pmatrix}
\widehat{\phi_1}(0)&\cdots&\widehat{\phi_m}(0)\\
\widehat{\phi_1}(1)&\cdots&\widehat{\phi_m}(1)
\end{pmatrix}.
\]

Let

\[
\mathcal N=\ker C.
\]

Then every coefficient vector

\[
a\in\mathcal N
\]

defines a finite test function

\[
g=\sum_{j=1}^m a_j\phi_j
\]

satisfying

\[
\widehat g(0)=0,
\qquad
\widehat g(1)=0.
\]

## Proof

By linearity of the Mellin transform,

\[
\widehat g(0)=\sum_{j=1}^m a_j\widehat{\phi_j}(0),
\]

and

\[
\widehat g(1)=\sum_{j=1}^m a_j\widehat{\phi_j}(1).
\]

The condition

\[
a\in\ker C
\]

says exactly that both sums vanish.

Therefore

\[
\widehat g(0)=\widehat g(1)=0.
\]

\[
\square
\]

---

# 6. Updated breakthrough target

The new serious target is no longer just a finite spectral detection theorem.

The upgraded target is:

\[
\boxed{
\text{finite spectral detection theorem on pole-orthogonal admissible finite subspaces}
}
\]

and then:

\[
\boxed{
\text{certified arithmetic matrix on the same pole-orthogonal subspace}
}
\]

This is closer to the real Weil criterion.

---

# 7. Still not source-locked

This phase does not fully source-lock the conventions because primary-source excerpts are still required from:

1. Weil;
2. Bombieri;
3. Bombieri-Lagarias;
4. Connes;
5. Suzuki or modern Galerkin matrix papers.

The uploaded source summary is a strong guide but not a substitute for primary extraction.

---

# 8. Next phase

Phase B2 should build the admissible finite subspace machinery:

1. compute Mellin constraints at \(0\) and \(1\);
2. build the constraint matrix \(C\);
3. compute a nullspace basis;
4. restrict finite matrices to the admissible subspace.

This is a real upgrade over the previous project.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a breakthrough.

This phase does not prove novelty.

This phase does not fully source-lock the project.

Exact audit strings:

PHASE_B1_PROVISIONAL_SOURCE_LOCK_COMPLETE

WEIL_STAR_CONVENTION_IMPORTED_PROVISIONALLY

MULTIPLICATIVE_CONVOLUTION_IMPORTED_PROVISIONALLY

MELLIN_PRODUCT_IDENTITY_SOURCE_CONFIRMED_PROVISIONALLY

POSITIVITY_CONDITION_IMPORTED_PROVISIONALLY

POLE_ORTHOGONALITY_CONSTRAINTS_IDENTIFIED

FINITE_ADMISSIBLE_SUBSPACE_THEOREM_PROVED

PRIMARY_SOURCE_EXTRACTION_STILL_REQUIRED

BREAKTHROUGH_NOT_ACHIEVED

READY_FOR_PHASE_B2_ADMISSIBLE_SUBSPACE

