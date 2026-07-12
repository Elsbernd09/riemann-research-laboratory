# Phase 10X — Combined-Radius Algorithm Correctness Proof

## Purpose

Phase 10W implemented the Combined-Radius Stability Certification algorithm.

Phase 10X proves the correctness of that upgraded algorithm.

The goal is to certify the implication:

\[
\texttt{CERTIFIED\_STABLE}
\Longrightarrow
n_-(M(\widetilde\Gamma,t))=n_-(M(\Gamma,t)).
\]

---

# 1. Algorithm recalled

Algorithm 10W.1 receives:

1. multiplicities \(m_1,\ldots,m_N\);
2. displacement sizes \(d_1,\ldots,d_N\);
3. local Lipschitz constant \(L_t(U)\);
4. zero spectral gap \(g_0(M)>0\).

It computes:

\[
\mathcal R_F
=
L_t(U)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2},
\]

\[
\mathcal R_{\mathrm{row}}
=
\max_j
\sum_k
\sqrt{m_jm_k}L_t(U)(d_j+d_k),
\]

and

\[
\mathcal R_{\min}
=
\min\{\mathcal R_F,\mathcal R_{\mathrm{row}}\}.
\]

It returns:

CERTIFIED_STABLE

if

\[
\mathcal R_{\min}<g_0(M),
\]

and otherwise returns:

NOT_CERTIFIED

---

# Theorem 10X.1 — Correctness of Combined-Radius Stability Certification

Assume the hypotheses of Theorem 10V.3:

1. \(M(\Gamma,t)\) and \(M(\widetilde\Gamma,t)\) are Hermitian;
2. \(g_0(M(\Gamma,t))>0\);
3. the kernel satisfies the local Lipschitz bound with constant \(L_t(U)\);
4. support displacements satisfy
\[
d_j=|\widetilde\alpha_j-\alpha_j|.
\]

If Algorithm 10W.1 returns

CERTIFIED_STABLE

then

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

---

# Proof

Algorithm 10W.1 returns

CERTIFIED_STABLE

only when

\[
\mathcal R_{\min}<g_0(M(\Gamma,t)).
\]

By definition,

\[
\mathcal R_{\min}
=
\min\{\mathcal R_F,\mathcal R_{\mathrm{row}}\}.
\]

Theorem 10V.3 states that if

\[
\mathcal R_{\min}<g_0(M(\Gamma,t)),
\]

then

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

Therefore, whenever Algorithm 10W.1 outputs

CERTIFIED_STABLE

under the hypotheses of Theorem 10V.3, the negative eigenvalue count is certified stable.

\[
\square
\]

---

# Proposition 10X.2 — Soundness of NOT_CERTIFIED Interpretation

If Algorithm 10W.1 returns

NOT_CERTIFIED

then no instability claim is made.

In particular,

NOT_CERTIFIED

does not imply

\[
n_-(M(\widetilde\Gamma,t))
\neq
n_-(M(\Gamma,t)).
\]

---

# Proof

Algorithm 10W.1 returns

NOT_CERTIFIED

when

\[
\mathcal R_{\min}\geq g_0(M(\Gamma,t)).
\]

Theorem 10V.3 gives a sufficient condition for stability, not a necessary condition.

Therefore, failure of the certificate does not imply failure of stability.

So the algorithm correctly interprets

NOT_CERTIFIED

as lack of certification rather than proof of instability.

\[
\square
\]

---

# 2. Soundness hierarchy

The project now has a theorem-backed certification chain:

\[
\text{support displacement data}
\]

\[
\Downarrow
\]

\[
\mathcal R_F,\quad \mathcal R_{\mathrm{row}},\quad \mathcal R_{\min}
\]

\[
\Downarrow
\]

\[
\mathcal R_{\min}<g_0(M)
\]

\[
\Downarrow
\]

\[
\texttt{CERTIFIED\_STABLE}
\]

\[
\Downarrow
\]

\[
n_-(M(\widetilde\Gamma,t))=n_-(M(\Gamma,t)).
\]

---

# 3. Algorithmic validity requirements

The algorithm is theorem-backed only when:

1. all multiplicities are positive;
2. all displacements are nonnegative;
3. \(L_t(U)\geq0\);
4. \(g_0(M)>0\);
5. the original and perturbed matrices are Hermitian;
6. the local Lipschitz bound holds on the chosen neighborhood \(U\);
7. the displacement data correctly represent the support perturbation.

---

# 4. Research-note significance

The upgraded algorithm is stronger than the Phase 10S algorithm because it uses two independent valid spectral-norm upper bounds:

1. Frobenius radius;
2. row-sum radius.

It certifies stability whenever either bound is strong enough.

This makes the finite audit framework more useful and less dependent on one crude norm estimate.

---

# Boundary

This correctness proof is finite-dimensional.

This proof does not prove RH.

This proof does not falsify RH.

This proof does not use zeta zeros.

This proof does not verify the zeta case.

This proof does not claim novelty.

Exact audit strings:

COMBINED_RADIUS_CORRECTNESS_PROOF

COMBINED_RADIUS_CERTIFIED_ALGORITHM

COMBINED_MINIMUM_RADIUS_CERTIFICATE

CERTIFIED_STABLE

NOT_CERTIFIED

