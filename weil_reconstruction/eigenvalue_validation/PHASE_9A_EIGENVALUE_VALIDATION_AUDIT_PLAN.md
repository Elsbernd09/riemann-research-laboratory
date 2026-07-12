# Phase 9A — Eigenvalue Validation Audit Plan

## Purpose

Phase 8Z implemented synthetic matrix assembly for Bombieri's source-derived \(H\)-kernel without computing eigenvalues.

Phase 9A creates the audit plan for the first eigenvalue validation phase.

This phase does not compute eigenvalues.

This phase does not use zeta zeros.

This phase does not prove RH.

This phase does not claim novelty.

---

# 1. Current status

The project now has:

1. source-extracted \(H\)-kernel formulas;
2. scalar kernel functions \(K,K_t,K^*,H\);
3. synthetic \(\Gamma\)-multiset data model;
4. full multiset matrix assembly;
5. distinct weighted matrix assembly;
6. shape checks;
7. finite-entry checks;
8. Hermitian residual inspection;
9. no eigenvalue computation so far.

---

# 2. Theorem 8 validation target

Bombieri Theorem 8 states, at source-extracted statement level, that the number of negative eigenvalues of

\[
H(\Gamma;t)
\]

equals the number of distinct complex conjugate pairs

\[
(\gamma,\overline{\gamma})
\]

in \(\Gamma\).

Phase 9 validation must test this only on synthetic finite multisets first.

---

# 3. Why an audit plan is still required

Eigenvalue computation is dangerous because incorrect matrix normalization can produce wrong counts.

Before computing spectra, the project must decide:

1. raw full multiset matrix or distinct weighted matrix;
2. whether a Hermitian similarity transform is needed;
3. how to count numerical negative eigenvalues;
4. how to handle near-zero eigenvalues;
5. how to handle repeated \(\gamma\)-values;
6. how to avoid treating unstable output as a theorem.

---

# 4. Candidate matrix representations

## Representation A — Full multiset raw matrix

\[
A_{jk}=H(\gamma_j,\gamma_k;t).
\]

Pros:

- directly preserves repeated values.

Cons:

- may have repeated rows/columns;
- may not be Hermitian in standard coordinates;
- zero eigenvalues from repetitions must be expected.

## Representation B — Distinct weighted matrix

\[
B_{jk}=H(\gamma_j,\gamma_k;t)m(\gamma_k).
\]

Pros:

- matches source-recorded reduction of repeated values.

Cons:

- column-weighted form may not be Hermitian in the ordinary Euclidean inner product.

## Representation C — Similarity symmetrized weighted matrix

Candidate:

\[
\widetilde H_{jk}
=
\sqrt{m(\gamma_j)}
H(\gamma_j,\gamma_k;t)
\sqrt{m(\gamma_k)}.
\]

Purpose:

- preserve eigenvalues of the weighted operator while improving Hermitian structure.

Status:

Audit target only.

Not yet validated.

---

# 5. Required validation stages

## Stage A — Hermitian convention lock

Before eigenvalues are counted, the project must identify which representation is numerically Hermitian enough to support real eigenvalue counting.

Validation metric:

\[
\max_{j,k}|M_{jk}-\overline{M_{kj}}|.
\]

If this residual is large, the representation is not acceptable for Hermitian eigenvalue validation.

## Stage B — Synthetic cases

Use synthetic finite multisets only.

Required cases:

1. all real \(\gamma\)-values;
2. one non-real conjugate pair;
3. two non-real conjugate pairs;
4. repeated real values;
5. repeated non-real pair values.

## Stage C — Numerical negative count rule

Define a tolerance

\[
\tau.
\]

Count

\[
\lambda<-\tau
\]

as negative.

Count

\[
|\lambda|\le\tau
\]

as numerical zero/ambiguous.

Never count near-zero numerical noise as theorem evidence.

## Stage D — Theorem 8 validation

For each synthetic case, compare:

\[
\#\{\lambda<-\tau\}
\]

against

\[
\#\{\text{distinct complex conjugate pairs in }\Gamma\}.
\]

Failures must be recorded honestly.

## Stage E — No zeta rule

No zeta zeros may be used in Phase 9A or the first validation phase.

The zeta limiting transition belongs to Bombieri Sections 10 and 11, which are not yet source-extracted.

---

# 6. Permission status after Phase 9A

## Still denied in this phase

Eigenvalue computation.

Zeta-zero experiments.

Bombieri-Weil numerical verification claims.

RH claims.

Novelty claims.

## Allowed next phase

A future phase may compute eigenvalues on synthetic finite matrices only, after implementing:

1. Hermitian residual gate;
2. real-spectrum check;
3. negative-count tolerance;
4. synthetic Theorem 8 comparison table;
5. explicit failure logging.

---

# 7. Boundary

This is an audit-plan phase.

No eigenvalues are computed here.

No zeta zeros are used.

No RH proof.

No novelty claim.

