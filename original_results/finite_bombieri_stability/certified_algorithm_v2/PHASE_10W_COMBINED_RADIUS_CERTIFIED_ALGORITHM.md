# Phase 10W — Combined-Radius Certified Stability Algorithm

## Purpose

Phase 10S implemented the first certified stability algorithm using only the Frobenius weighted radius.

Phase 10V proved a second matrix-specific row-sum certificate.

Phase 10W upgrades the algorithm to compute both radii and use the better one.

---

# 1. Frobenius radius

\[
\mathcal R_F
=
L_t(U)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

---

# 2. Row-sum radius

\[
\mathcal R_{\mathrm{row}}
=
\max_j
\sum_k
\sqrt{m_jm_k}L_t(U)(d_j+d_k).
\]

---

# 3. Combined minimum radius

\[
\mathcal R_{\min}
=
\min\{\mathcal R_F,\mathcal R_{\mathrm{row}}\}.
\]

---

# Algorithm 10W.1 — Combined-Radius Stability Certification

## Input

\[
(m_1,\ldots,m_N),
\quad
(d_1,\ldots,d_N),
\quad
L_t(U),
\quad
g_0(M).
\]

## Steps

1. Verify all multiplicities are positive.
2. Verify all displacements are nonnegative.
3. Verify \(L_t(U)\geq0\).
4. Verify \(g_0(M)>0\).
5. Compute \(\mathcal R_F\).
6. Compute \(\mathcal R_{\mathrm{row}}\).
7. Compute

\[
\mathcal R_{\min}
=
\min\{\mathcal R_F,\mathcal R_{\mathrm{row}}\}.
\]

8. If

\[
\mathcal R_{\min}<g_0(M),
\]

return

CERTIFIED_STABLE

9. Otherwise return

NOT_CERTIFIED

---

# Correctness statement

If Algorithm 10W.1 returns CERTIFIED_STABLE, then

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

This follows from Theorem 10V.3.

---

# Interpretation

CERTIFIED_STABLE means the negative eigenvalue count is theorem-certified stable.

NOT_CERTIFIED means this algorithm did not certify stability.

NOT_CERTIFIED does not mean instability.

---

# Boundary

This algorithm is finite-dimensional.

This algorithm does not prove RH.

This algorithm does not falsify RH.

This algorithm does not use zeta zeros.

This algorithm does not verify the zeta case.

This algorithm does not claim novelty.

Exact audit strings:

COMBINED_RADIUS_CERTIFIED_ALGORITHM

COMBINED_MINIMUM_RADIUS_CERTIFICATE

CERTIFIED_STABLE

NOT_CERTIFIED

