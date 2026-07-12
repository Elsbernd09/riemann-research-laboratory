# Phase 8Z — Matrix Assembly Without Eigenvalues

## Purpose

Phase 8Z implements synthetic matrix assembly helpers for the source-derived \(H\)-kernel.

This phase does not compute eigenvalues.

This phase does not use zeta zeros.

This phase does not prove RH.

This phase does not claim novelty.

---

# 1. Implemented objects

The file

\[
\texttt{weil\_reconstruction/finite\_truncations/h\_matrix\_assembly.py}
\]

implements:

1. a synthetic \(\Gamma\)-multiset data model;
2. full multiset matrix assembly;
3. distinct weighted matrix assembly;
4. shape checks;
5. finite-entry checks;
6. Hermitian-residual inspection.

---

# 2. Full multiset matrix

For a synthetic multiset

\[
\Gamma=(\gamma_1,\ldots,\gamma_N),
\]

the full matrix is

\[
A_{jk}=H(\gamma_j,\gamma_k;t).
\]

This keeps repeated \(\gamma\)-values as repeated rows and columns.

---

# 3. Distinct weighted matrix

For distinct values \(\gamma_j\) with multiplicities \(m(\gamma_j)\), the weighted matrix is

\[
B_{jk}=H(\gamma_j,\gamma_k;t)m(\gamma_k).
\]

This follows the source-recorded multiplicity warning.

---

# 4. Synthetic cases only

The checks use synthetic cases:

1. all real gamma values;
2. one non-real conjugate-pair configuration;
3. repeated real values.

No zeta zeros are used.

---

# 5. Checks performed

The script

\[
\texttt{scripts/run\_phase8z\_matrix\_assembly\_checks.py}
\]

checks:

1. full matrix shape;
2. distinct weighted matrix shape;
3. finite entries;
4. repeated-value warning count;
5. conjugate-pair bookkeeping count;
6. Hermitian residuals for inspection only.

No eigenvalues are computed.

---

# 6. Boundary

This is matrix assembly only.

It is not eigenvalue validation.

It is not a verification of Theorem 8.

It is not a zeta-zero experiment.

It is not an RH result.

No RH proof.

No novelty claim.

