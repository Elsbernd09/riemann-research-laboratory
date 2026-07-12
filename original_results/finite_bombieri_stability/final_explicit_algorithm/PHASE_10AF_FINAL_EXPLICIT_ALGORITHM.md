# Phase 10AF — Final Explicit \(H\)-Kernel Certified Algorithm

## Purpose

Phase 10AF implements the final explicit certified algorithm.

The algorithm computes:

\[
L_H(U,t),
\]

then computes:

\[
\mathcal R_F(L_H),
\]

\[
\mathcal R_{\mathrm{row}}(L_H),
\]

and

\[
\mathcal R_{\min}(L_H).
\]

It returns:

CERTIFIED_STABLE

or

NOT_CERTIFIED

---

# Algorithm 10AF.1 — Explicit \(H\)-Kernel Stability Certification

## Input

1. multiplicities \(m_1,\ldots,m_N\);
2. support displacements \(d_1,\ldots,d_N\);
3. zero spectral gap \(g_0(M)\);
4. compact-domain parameters \(R,S,R_y,S_y,\Delta_Y,r,t\).

## Steps

1. Compute the concrete majorants:

\[
A_0,A_1,B_0,B_1,C_0.
\]

2. Compute:

\[
M_0,M_x,M_y.
\]

3. Compute:

\[
L_H(U,t)=2|t|B_0M_x+2|t|(B_1M_0+B_0M_y).
\]

4. Compute:

\[
\mathcal R_F(L_H)
=
L_H(U,t)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

5. Compute:

\[
\mathcal R_{\mathrm{row}}(L_H)
=
\max_j
\sum_k
\sqrt{m_jm_k}L_H(U,t)(d_j+d_k).
\]

6. Compute:

\[
\mathcal R_{\min}(L_H)
=
\min\{\mathcal R_F(L_H),\mathcal R_{\mathrm{row}}(L_H)\}.
\]

7. If

\[
\mathcal R_{\min}(L_H)<g_0(M),
\]

return:

CERTIFIED_STABLE

8. Otherwise return:

NOT_CERTIFIED

---

# Meaning

CERTIFIED_STABLE means the negative eigenvalue count is theorem-certified stable by the explicit \(H\)-kernel support-stability certificate.

NOT_CERTIFIED means this certificate did not prove stability.

NOT_CERTIFIED does not imply instability.

---

# Boundary

This algorithm is finite-dimensional.

This algorithm does not prove RH.

This algorithm does not falsify RH.

This algorithm does not use zeta zeros.

This algorithm does not verify the zeta case.

This algorithm does not claim novelty.

Exact audit strings:

FINAL_EXPLICIT_H_KERNEL_CERTIFIED_ALGORITHM

COMPUTABLE_H_KERNEL_LIPSCHITZ_CONSTANT

EXPLICIT_H_KERNEL_SUPPORT_STABILITY_CERTIFICATE

CERTIFIED_STABLE

NOT_CERTIFIED

