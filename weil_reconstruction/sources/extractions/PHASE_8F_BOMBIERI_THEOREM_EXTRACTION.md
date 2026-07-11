# Phase 8F — Bombieri Theorem 1 and Theorem 2 Extraction

## Purpose

Phase 8E locked only high-level structural facts from Bombieri and Suzuki.

Phase 8F extracts the first exact theorem-level objects from Bombieri's Section 3.

This is not a proof of RH.

This is not a new Weil criterion.

This is a reconstruction of known classical source material.

---

# 1. Source

Enrico Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**, Rend. Mat. Acc. Lincei, Serie 9, Vol. 11, 183-233, 2000.

Relevant section:

Section 3, "A necessary and sufficient condition for the Riemann Hypothesis."

---

# 2. Extracted setup

Bombieri considers test functions

\[
f(x)\in C_0^\infty((0,\infty))
\]

that are multiplicative convolutions of a function \(g\) and its transpose conjugate \(g^*\).

The multiplicative convolution is written schematically as

\[
f(x)
=
\int_0^\infty
g(x/y)g^*(y)\frac{dy}{y}.
\]

Bombieri records the Mellin-side identity

\[
f(s)=g(s)g(1-s).
\]

This is the bridge from convolution positivity to zero-side products.

---

# 3. Bombieri Theorem 1 extraction

## Source theorem content

Bombieri states the following strengthening of Weil's criterion:

The Riemann Hypothesis holds if and only if

\[
\sum_\rho
g(\rho)g(1-\rho)>0
\]

for every complex-valued

\[
g(x)\in C_0^\infty((0,\infty)),
\]

not identically zero.

## Interpretation

Under RH,

\[
1-\rho=\overline{\rho}
\]

for each nontrivial zero, so

\[
g(\rho)g(1-\rho)
=
g(\rho)\overline{g(\rho)}
=
|g(\rho)|^2.
\]

Thus the zero-side expression becomes a sum of nonnegative terms.

The converse direction uses known criterion machinery, including Li-type ideas, to show that failure of RH creates negative values for suitable test functions.

## Project status

This is a known theorem reconstructed from Bombieri.

It is not project-original.

---

# 4. Bombieri Theorem 2 extraction

## Source theorem content

Bombieri defines a linear functional

\[
T[f]
\]

on

\[
C_0^\infty((0,\infty)).
\]

The functional satisfies the explicit-formula identity

\[
T[f]=T[f^*]=\sum_\rho f(\rho),
\]

where the sum ranges over all complex zeros of the Riemann zeta function.

Bombieri then states that RH is equivalent to

\[
T[f*f^*]\ge0
\]

on

\[
C_0^\infty((0,\infty)),
\]

with equality only if

\[
f\equiv0.
\]

## Interpretation

This is the Weil quadratic functional in Bombieri's multiplicative formulation.

The object

\[
T[f*f^*]
\]

is the source-grounded quadratic object Phase 8 must reconstruct before any exact finite-rank code.

## Project status

This is a known theorem reconstructed from Bombieri.

It is not project-original.

---

# 5. Locked conventions after Phase 8F

The following are now partially or fully locked:

## LOCKED

Primary test-function ambient space:

\[
C_0^\infty((0,\infty)).
\]

Primary source section:

Bombieri Section 3.

Primary positivity object:

\[
T[f*f^*]\ge0.
\]

Primary zero-side identity:

\[
T[f]=\sum_\rho f(\rho).
\]

Primary RH-equivalence statement:

RH is equivalent to positivity of the Bombieri-Weil quadratic functional on the stated test class.

## PARTIAL

Multiplicative convolution notation.

Transpose-conjugate convention \(f^*\).

Exact formula for \(T[f]\), including prime-side, pole, and archimedean terms.

Exact convergence convention for the zero sum.

Exact finite truncation matrices.

## UNLOCKED

Fourier transform convention for the later matrix formulation.

Exact matrix entries.

Finite-dimensional truncation definitions.

Eigenvalue theorem statements in later sections.

---

# 6. Relation to Phase 7

Phase 7 toy matrices were diagnostic.

Phase 8F identifies the actual classical quadratic object that future finite-rank models must approximate:

\[
T[f*f^*].
\]

This is the first real bridge away from toy matrices.

However, no finite-rank implementation is allowed yet, because the exact formula for \(T[f]\) and the matrix formulation remain unlocked.

---

# 7. Boundary

No RH proof.

No new Weil criterion.

No novelty claim.

No exact finite-rank Weil matrix yet.

