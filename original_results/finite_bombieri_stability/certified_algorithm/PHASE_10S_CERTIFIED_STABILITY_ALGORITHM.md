# Phase 10S — Certified Stability Algorithm

## Purpose

Phase 10Q proved the sharper weighted support-stability theorem.

Phase 10R showed that the sharper certificate is not cosmetic.

Phase 10S turns the theorem into a certified algorithm.

The algorithm takes finite support data, multiplicities, displacement sizes, a Lipschitz constant, and a zero spectral gap. It returns either:

\[
\texttt{CERTIFIED\_STABLE}
\]

or

\[
\texttt{NOT\_CERTIFIED}.
\]

---

# 1. Inputs

The algorithm receives:

1. \(N\), the number of distinct support points;
2. multiplicities \(m_1,\ldots,m_N\);
3. support displacement sizes \(d_1,\ldots,d_N\);
4. a local Lipschitz constant \(L_t(U)\);
5. a zero spectral gap \(g_0(M)>0\).

---

# 2. Weighted perturbation radius

Compute

\[
\mathcal R
=
L_t(U)
\left(
\sum_{j=1}^N\sum_{k=1}^N
m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

---

# 3. Certification rule

If

\[
\mathcal R<g_0(M),
\]

return

\[
\texttt{CERTIFIED\_STABLE}.
\]

Otherwise, return

\[
\texttt{NOT\_CERTIFIED}.
\]

---

# 4. Meaning of CERTIFIED_STABLE

If the algorithm returns

\[
\texttt{CERTIFIED\_STABLE},
\]

then Theorem 10Q guarantees

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

---

# 5. Meaning of NOT_CERTIFIED

If the algorithm returns

\[
\texttt{NOT\_CERTIFIED},
\]

that does not mean the negative eigenvalue count changes.

It means this certificate cannot prove stability.

This distinction is crucial.

---

# Algorithm 10S.1 — Weighted Support Stability Certification

## Input

\[
(m_1,\ldots,m_N),\quad
(d_1,\ldots,d_N),\quad
L_t(U),\quad
g_0(M).
\]

## Steps

1. Verify all multiplicities are positive.
2. Verify all displacements are nonnegative.
3. Verify \(L_t(U)\geq0\).
4. Verify \(g_0(M)>0\).
5. Compute

\[
\mathcal R
=
L_t(U)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

6. If \(\mathcal R<g_0(M)\), output \(\texttt{CERTIFIED\_STABLE}\).
7. Otherwise, output \(\texttt{NOT\_CERTIFIED}\).

---

# Correctness statement

If Algorithm 10S.1 outputs

\[
\texttt{CERTIFIED\_STABLE},
\]

then

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

This follows directly from Theorem 10Q.

---

# Boundary

This algorithm is finite-dimensional.

This algorithm does not prove RH.

This algorithm does not falsify RH.

This algorithm does not use zeta zeros.

This algorithm does not verify the zeta case.

This algorithm does not claim novelty.

