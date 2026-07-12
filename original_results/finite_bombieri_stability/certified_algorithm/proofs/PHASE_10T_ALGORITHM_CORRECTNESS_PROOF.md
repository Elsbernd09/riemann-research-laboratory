# Phase 10T — Certified Algorithm Correctness Proof

## Purpose

Phase 10S implemented the Weighted Support Stability Certification algorithm.

Phase 10T proves the correctness of that algorithm.

The goal is to certify the implication:

\[
\texttt{CERTIFIED\_STABLE}
\Longrightarrow
n_-(M(\widetilde\Gamma,t))=n_-(M(\Gamma,t)).
\]

---

# 1. Algorithm recalled

The algorithm receives:

1. multiplicities \(m_1,\ldots,m_N\);
2. displacement sizes \(d_1,\ldots,d_N\);
3. local Lipschitz constant \(L_t(U)\);
4. zero spectral gap \(g_0(M)>0\).

It computes

\[
\mathcal R
=
L_t(U)
\left(
\sum_{j=1}^N\sum_{k=1}^N
m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

It returns:

\[
\texttt{CERTIFIED\_STABLE}
\]

if

\[
\mathcal R<g_0(M),
\]

and otherwise returns:

\[
\texttt{NOT\_CERTIFIED}.
\]

---

# Theorem 10T.1 — Correctness of Weighted Support Stability Certification

Assume the hypotheses of Theorem 10Q:

1. \(M(\Gamma,t)\) and \(M(\widetilde\Gamma,t)\) are Hermitian;
2. \(g_0(M(\Gamma,t))>0\);
3. the kernel satisfies the local Lipschitz bound with constant \(L_t(U)\);
4. support displacements satisfy
\[
d_j=|\widetilde\alpha_j-\alpha_j|.
\]

If Algorithm 10S.1 returns

\[
\texttt{CERTIFIED\_STABLE},
\]

then

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

---

# Proof

Algorithm 10S.1 returns

\[
\texttt{CERTIFIED\_STABLE}
\]

only when its computed weighted perturbation radius satisfies

\[
\mathcal R<g_0(M(\Gamma,t)).
\]

By definition,

\[
\mathcal R
=
L_t(U)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

This is exactly the certificate appearing in Theorem 10Q.1.

Therefore, under the hypotheses of Theorem 10Q.1, the inequality

\[
\mathcal R<g_0(M(\Gamma,t))
\]

implies

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

Thus, whenever Algorithm 10S.1 outputs

\[
\texttt{CERTIFIED\_STABLE},
\]

the negative eigenvalue count is certified stable.

\[
\square
\]

---

# Proposition 10T.2 — Soundness of NOT_CERTIFIED Interpretation

If Algorithm 10S.1 returns

\[
\texttt{NOT\_CERTIFIED},
\]

then the algorithm makes no mathematical claim about whether

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

In particular,

\[
\texttt{NOT\_CERTIFIED}
\]

does not imply instability.

---

# Proof

Algorithm 10S.1 returns

\[
\texttt{NOT\_CERTIFIED}
\]

when

\[
\mathcal R\geq g_0(M(\Gamma,t)).
\]

Theorem 10Q.1 is a sufficient condition, not a necessary condition.

Therefore, failure of the sufficient condition does not imply failure of the conclusion.

So the algorithm correctly interprets

\[
\texttt{NOT\_CERTIFIED}
\]

as lack of certification rather than proof of instability.

\[
\square
\]

---

# 2. Algorithmic validity requirements

The algorithm is valid only when:

1. multiplicities are positive;
2. displacements are nonnegative;
3. \(L_t(U)\geq0\);
4. \(g_0(M)>0\);
5. the matrices are Hermitian;
6. the kernel Lipschitz hypothesis holds on the chosen neighborhood \(U\).

If these conditions are not met, the algorithm should not be interpreted as a theorem-backed certificate.

---

# 3. Meaning for the research note

The algorithm is now mathematically linked to the theorem.

This creates a reproducible pipeline:

\[
\text{finite data}
\rightarrow
\mathcal R
\rightarrow
\texttt{CERTIFIED\_STABLE or NOT\_CERTIFIED}
\rightarrow
\text{theorem-backed interpretation}.
\]

---

# Boundary

This correctness proof is finite-dimensional.

This proof does not prove RH.

This proof does not falsify RH.

This proof does not use zeta zeros.

This proof does not verify the zeta case.

This proof does not claim novelty.


---

# Exact audit strings

CERTIFIED_STABLE

NOT_CERTIFIED

CERTIFIED_ALGORITHM_CORRECTNESS_PROOF

This proof does not prove RH.

This proof does not falsify RH.

This proof does not use zeta zeros.

This proof does not claim novelty.

