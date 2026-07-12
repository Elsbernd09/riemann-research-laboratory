# Phase 10AG — Final Explicit Algorithm Correctness Proof

## Purpose

Phase 10AF implemented the final explicit \(H\)-kernel certified stability algorithm.

Phase 10AG proves its correctness.

The goal is to certify:

\[
\texttt{CERTIFIED\_STABLE}
\Longrightarrow
n_-(M(\widetilde\Gamma,t))=n_-(M(\Gamma,t)).
\]

---

# 1. Algorithm recalled

Algorithm 10AF.1 takes:

1. multiplicities \(m_1,\ldots,m_N\);
2. support displacements \(d_1,\ldots,d_N\);
3. zero spectral gap \(g_0(M)>0\);
4. compact-domain parameters \(R,S,R_y,S_y,\Delta_Y,r,t\).

It computes:

\[
L_H(U,t),
\]

then computes

\[
\mathcal R_F(L_H),
\]

\[
\mathcal R_{\mathrm{row}}(L_H),
\]

and

\[
\mathcal R_{\min}(L_H)
=
\min\{\mathcal R_F(L_H),\mathcal R_{\mathrm{row}}(L_H)\}.
\]

It returns:

CERTIFIED_STABLE

if

\[
\mathcal R_{\min}(L_H)<g_0(M),
\]

and returns:

NOT_CERTIFIED

otherwise.

---

# Theorem 10AG.1 — Correctness of the final explicit \(H\)-kernel certified algorithm

Assume:

1. the compact-domain hypotheses of the explicit \(H\)-kernel Lipschitz theorem hold;
2. \(M(\Gamma,t)\) and \(M(\widetilde\Gamma,t)\) are Hermitian;
3. \(g_0(M(\Gamma,t))>0\);
4. the displacement data satisfy
\[
d_j=|\widetilde\alpha_j-\alpha_j|;
\]
5. Algorithm 10AF.1 computes \(L_H(U,t)\), \(\mathcal R_F(L_H)\), \(\mathcal R_{\mathrm{row}}(L_H)\), and \(\mathcal R_{\min}(L_H)\) according to the locked formulas.

If Algorithm 10AF.1 returns:

CERTIFIED_STABLE

then

\[
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
\]

---

# Proof

Algorithm 10AF.1 returns:

CERTIFIED_STABLE

only when

\[
\mathcal R_{\min}(L_H)<g_0(M(\Gamma,t)).
\]

By the explicit \(H\)-kernel Lipschitz theorem,

\[
L_H(U,t)
\]

is a valid Lipschitz constant for the finite \(H\)-kernel on the compact domain.

Therefore the explicit \(H\)-kernel support-stability certificate applies.

That certificate states that if

\[
\mathcal R_{\min}(L_H)<g_0(M(\Gamma,t)),
\]

then

\[
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
\]

Thus, whenever the algorithm returns:

CERTIFIED_STABLE

under the stated hypotheses, the negative eigenvalue count is theorem-certified stable.

\[
\square
\]

---

# Proposition 10AG.2 — Sound interpretation of NOT_CERTIFIED

If Algorithm 10AF.1 returns:

NOT_CERTIFIED

then no instability claim is made.

In particular:

\[
\texttt{NOT\_CERTIFIED}
\]

does not imply

\[
n_-(M(\widetilde\Gamma,t))\neq n_-(M(\Gamma,t)).
\]

---

# Proof

Algorithm 10AF.1 returns:

NOT_CERTIFIED

when

\[
\mathcal R_{\min}(L_H)\geq g_0(M(\Gamma,t)).
\]

The explicit \(H\)-kernel support-stability certificate is sufficient, not necessary.

Therefore failure of the certificate does not imply instability.

So the algorithm correctly interprets NOT_CERTIFIED as lack of certification rather than proof of instability.

\[
\square
\]

---

# 2. Final certified pipeline

The final explicit certified pipeline is:

\[
\text{compact-domain data}
\]

\[
\Downarrow
\]

\[
L_H(U,t)
\]

\[
\Downarrow
\]

\[
\mathcal R_F(L_H),\quad
\mathcal R_{\mathrm{row}}(L_H)
\]

\[
\Downarrow
\]

\[
\mathcal R_{\min}(L_H)
\]

\[
\Downarrow
\]

\[
\mathcal R_{\min}(L_H)<g_0(M)
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

# 3. Validity requirements

The final algorithm is theorem-backed only when:

1. the compact-domain hypotheses are valid;
2. \(\Delta_Y>0\);
3. \(r>0\);
4. \(t\neq0\);
5. multiplicities are positive;
6. displacements are nonnegative and correct;
7. \(g_0(M)>0\);
8. original and perturbed matrices are Hermitian.

---

# 4. What is now complete

The project now has:

1. explicit \(H\)-kernel Lipschitz theorem;
2. explicit \(H\)-kernel support-stability certificate;
3. final explicit certified algorithm;
4. final explicit algorithm correctness proof;
5. honest NOT_CERTIFIED interpretation.

---

# Boundary

This proof is finite-dimensional.

This proof does not prove RH.

This proof does not falsify RH.

This proof does not use zeta zeros.

This proof does not verify the zeta case.

This proof does not claim novelty.

Exact audit strings:

FINAL_EXPLICIT_ALGORITHM_CORRECTNESS_PROOF

FINAL_EXPLICIT_H_KERNEL_CERTIFIED_ALGORITHM

EXPLICIT_H_KERNEL_SUPPORT_STABILITY_CERTIFICATE

CERTIFIED_STABLE

NOT_CERTIFIED

