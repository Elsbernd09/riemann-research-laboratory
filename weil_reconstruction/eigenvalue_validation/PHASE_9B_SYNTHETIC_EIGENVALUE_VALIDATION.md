# Phase 9B — Synthetic Eigenvalue Validation with Strict Gates

## Purpose

Phase 9A created the eigenvalue validation audit plan.

Phase 9B runs the first synthetic eigenvalue validation attempt with strict Hermitian gates.

This phase uses synthetic finite \(\Gamma\)-multisets only.

This phase does not use zeta zeros.

This phase does not prove RH.

This phase does not claim novelty.

---

# 1. What this phase does

The script

\[
\texttt{scripts/run\_phase9b\_synthetic\_eigenvalue\_validation.py}
\]

checks candidate matrix representations:

1. full raw multiset matrix;
2. distinct weighted raw matrix;
3. distinct similarity candidate matrix.

For each synthetic case, it computes Hermitian residuals first.

Eigenvalues are computed only if a representation passes the Hermitian residual gate.

---

# 2. Synthetic cases

The validation uses:

1. all real \(\gamma\)-values;
2. one non-real conjugate-pair configuration;
3. two non-real conjugate-pair configuration;
4. repeated real values;
5. repeated non-real pair values.

No zeta zeros are used.

---

# 3. Theorem 8 target

The synthetic target is:

\[
\#\{\lambda<-\tau\}
=
\#\{\text{distinct complex conjugate pairs in }\Gamma\}.
\]

This is tested only when the Hermitian gate passes.

---

# 4. Failure policy

Failures are not hidden.

If no representation passes the Hermitian gate, the case is marked:

\[
\texttt{STRICT\_GATE\_RESULT=BLOCKED}.
\]

If a representation passes but the negative count does not match, the mismatch is recorded.

---

# 5. Boundary

This is synthetic finite validation only.

This is not a zeta-zero experiment.

This is not a proof of RH.

This is not a novelty claim.

This is not a publication result.

