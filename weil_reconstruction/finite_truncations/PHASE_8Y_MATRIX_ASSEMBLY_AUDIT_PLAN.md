# Phase 8Y — Matrix Assembly Audit Plan

## Purpose

Phase 8X implemented scalar source-derived \(H\)-kernel functions with sanity checks only.

Phase 8Y creates the audit plan for matrix assembly.

This phase does not assemble matrices.

This phase does not compute eigenvalues.

This phase does not use zeta zeros.

This phase does not prove RH.

This phase does not claim novelty.

---

# 1. Current status

The project has implemented scalar functions:

\[
K(z)=\frac{\sin z}{z},
\]

\[
K_t(z)=K(tz),
\]

\[
K^*(x,y;t),
\]

and

\[
H(x,y;t)=\frac{2tK^*(x,y;t)}{1/4+y^2}.
\]

These functions passed scalar sanity checks.

---

# 2. Why matrix assembly needs its own audit

Bombieri Theorem 8 is about the spectrum of

\[
H(\Gamma;t).
\]

However, matrix assembly is delicate because \(\Gamma\) is a multiset and repeated values affect zero eigenvalues.

The source records two related representations:

1. full multiset representation;
2. distinct-\(\gamma\) weighted representation.

The project must not confuse them.

---

# 3. Full multiset representation

In the full multiset representation, every element of \(\Gamma\) appears as a row and column, including repetitions.

If

\[
\Gamma=(\gamma_1,\ldots,\gamma_N),
\]

then the raw matrix would be

\[
A_{jk}=H(\gamma_j,\gamma_k;t).
\]

This representation preserves repeated rows/columns directly.

Expected issue:

Repeated \(\gamma\)-values create zero eigenvalues.

---

# 4. Distinct weighted representation

Let

\[
\gamma_1,\ldots,\gamma_r
\]

be the distinct elements of \(\Gamma\), with multiplicities

\[
m(\gamma_k).
\]

The source records that the remaining nonzero spectrum is represented through the weighted matrix

\[
H(\gamma_j,\gamma_k;t)m(\gamma_k).
\]

This representation removes duplicated columns but introduces weights.

Important warning:

This weighted matrix may not be Hermitian in the usual Euclidean inner product.

A similarity-symmetrized candidate is

\[
\widetilde H_{jk}
=
\sqrt{m(\gamma_j)}
H(\gamma_j,\gamma_k;t)
\sqrt{m(\gamma_k)}.
\]

This is an audit candidate, not yet an implemented theorem claim.

---

# 5. Assembly stages required

## Stage A — Data model

Define a synthetic \(\Gamma\)-multiset object.

It must record:

1. full ordered values;
2. distinct values;
3. multiplicities;
4. conjugate-pair structure;
5. expected negative-pair count.

No zeta zeros.

## Stage B — Raw matrix assembly

Assemble

\[
A_{jk}=H(\gamma_j,\gamma_k;t)
\]

for a synthetic finite multiset.

No eigenvalues.

Only inspect shape, finite entries, and repeated-row behavior.

## Stage C — Weighted distinct matrix assembly

Assemble

\[
B_{jk}=H(\gamma_j,\gamma_k;t)m(\gamma_k)
\]

for distinct values.

No eigenvalues.

Only inspect shape, finite entries, and consistency with multiplicity table.

## Stage D — Symmetry audit

Inspect whether:

\[
A_{jk}\approx\overline{A_{kj}}
\]

or whether a similarity transform is required.

No eigenvalues.

## Stage E — Permission gate

Only after Stage A-D pass may the project create a separate eigenvalue-validation phase.

---

# 6. Synthetic test cases

The first matrix assembly test cases must be synthetic.

## Case 1 — all real gamma values

Example:

\[
\Gamma=\{-2,0,2\}.
\]

Expected non-real conjugate pair count:

\[
0.
\]

## Case 2 — one non-real conjugate pair

Example:

\[
\Gamma=\{a+ib,a-ib,-a+ib,-a-ib\}
\]

with \(b\ne0\).

Expected distinct complex conjugate pair count:

source-theorem target to be counted by the test helper.

## Case 3 — repeated gamma value

Example:

\[
\Gamma=\{1,1,-1,-1\}.
\]

Expected repeated-\(\gamma\) zero-eigenvalue warning:

\[
\sum_\gamma'(m(\gamma)-1)>0.
\]

No eigenvalues yet.

---

# 7. Forbidden in Phase 8Y

Do not assemble matrices in this phase.

Do not compute eigenvalues in this phase.

Do not use zeta zeros.

Do not claim Bombieri-Weil numerical verification.

Do not claim RH progress.

---

# 8. Boundary

This is an audit-plan phase.

No implementation.

No eigenvalue computation.

No zeta-zero experiment.

No RH proof.

No novelty claim.

