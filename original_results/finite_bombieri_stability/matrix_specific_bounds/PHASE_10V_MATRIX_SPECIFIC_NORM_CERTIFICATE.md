# Phase 10V — Matrix-Specific Norm Improvement Branch

## Purpose

Phase 10Q proved the weighted Frobenius-radius certificate

\[
\mathcal R_F
=
L_t(U)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

This gives

\[
\|E\|_2\leq \|E\|_F\leq \mathcal R_F.
\]

Phase 10V adds a matrix-specific row/column norm certificate using

\[
\|E\|_2\leq\sqrt{\|E\|_1\|E\|_\infty}.
\]

This may be sharper than the Frobenius certificate for structured perturbations.

---

# 1. Setup

Let

\[
E=M(\widetilde\Gamma,t)-M(\Gamma,t).
\]

As before,

\[
|E_{jk}|
\leq
\sqrt{m_jm_k}L_t(U)(d_j+d_k).
\]

Define the entrywise majorant matrix

\[
B_{jk}
=
\sqrt{m_jm_k}L_t(U)(d_j+d_k).
\]

Then

\[
|E_{jk}|\leq B_{jk}.
\]

---

# 2. Row and column majorants

Define

\[
R_{\max}
=
\max_j\sum_{k=1}^N B_{jk},
\]

and

\[
C_{\max}
=
\max_k\sum_{j=1}^N B_{jk}.
\]

Then

\[
\|E\|_\infty
\leq R_{\max},
\]

and

\[
\|E\|_1
\leq C_{\max}.
\]

Therefore,

\[
\|E\|_2
\leq
\sqrt{\|E\|_1\|E\|_\infty}
\leq
\sqrt{C_{\max}R_{\max}}.
\]

---

# Theorem 10V.1 — Matrix-specific row/column stability certificate

Assume:

1. \(M(\Gamma,t)\) and \(M(\widetilde\Gamma,t)\) are Hermitian;
2. \(g_0(M(\Gamma,t))>0\);
3. the kernel satisfies the local Lipschitz bound with constant \(L_t(U)\);
4. support displacements are \(d_j=|\widetilde\alpha_j-\alpha_j|\);
5. \(B_{jk}=\sqrt{m_jm_k}L_t(U)(d_j+d_k)\);
6. \(R_{\max}=\max_j\sum_kB_{jk}\);
7. \(C_{\max}=\max_k\sum_jB_{jk}\).

If

\[
\sqrt{R_{\max}C_{\max}}<g_0(M(\Gamma,t)),
\]

then

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

---

# Proof

Let

\[
E=M(\widetilde\Gamma,t)-M(\Gamma,t).
\]

The entrywise Lipschitz argument gives

\[
|E_{jk}|\leq B_{jk}.
\]

Thus,

\[
\|E\|_\infty
=
\max_j\sum_k|E_{jk}|
\leq
\max_j\sum_kB_{jk}
=
R_{\max}.
\]

Similarly,

\[
\|E\|_1
=
\max_k\sum_j|E_{jk}|
\leq
\max_k\sum_jB_{jk}
=
C_{\max}.
\]

For any matrix,

\[
\|E\|_2\leq\sqrt{\|E\|_1\|E\|_\infty}.
\]

Therefore,

\[
\|E\|_2
\leq
\sqrt{R_{\max}C_{\max}}.
\]

If

\[
\sqrt{R_{\max}C_{\max}}<g_0(M(\Gamma,t)),
\]

then

\[
\|E\|_2<g_0(M(\Gamma,t)).
\]

By spectral-gap stability,

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

\[
\square
\]

---

# Corollary 10V.2 — Hermitian symmetric row-sum certificate

If the majorant matrix \(B\) is symmetric, then

\[
R_{\max}=C_{\max}.
\]

Therefore the certificate becomes

\[
R_{\max}<g_0(M(\Gamma,t)).
\]

Since

\[
B_{jk}
=
\sqrt{m_jm_k}L_t(U)(d_j+d_k)
\]

is symmetric, the support-stability setting admits the simpler certificate

\[
\max_j\sum_k
\sqrt{m_jm_k}L_t(U)(d_j+d_k)
<
g_0(M(\Gamma,t)).
\]

This is the matrix-specific row-sum certificate.

---

# 3. Comparison with Frobenius certificate

The Frobenius certificate is

\[
\mathcal R_F<g_0(M).
\]

The row-sum certificate is

\[
R_{\max}<g_0(M).
\]

Neither universally dominates the other in all finite matrices.

But the row-sum certificate can be sharper when perturbation mass is spread across entries in a way that makes the maximum row sum smaller than the Frobenius radius.

Therefore the certified algorithm should compute both and use the smaller certified upper bound:

\[
\mathcal R_{\min}
=
\min\{\mathcal R_F,R_{\max}\}.
\]

If

\[
\mathcal R_{\min}<g_0(M),
\]

then stability is certified.

---

# Theorem 10V.3 — Combined minimum-radius certificate

Let

\[
\mathcal R_F
=
L_t(U)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2},
\]

and

\[
\mathcal R_{\mathrm{row}}
=
\max_j\sum_k
\sqrt{m_jm_k}L_t(U)(d_j+d_k).
\]

Define

\[
\mathcal R_{\min}
=
\min\{\mathcal R_F,\mathcal R_{\mathrm{row}}\}.
\]

If

\[
\mathcal R_{\min}<g_0(M(\Gamma,t)),
\]

then

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

---

# Proof

Both \(\mathcal R_F\) and \(\mathcal R_{\mathrm{row}}\) are valid upper bounds for \(\|E\|_2\). Therefore their minimum is also a valid upper bound:

\[
\|E\|_2\leq \mathcal R_{\min}.
\]

If

\[
\mathcal R_{\min}<g_0(M(\Gamma,t)),
\]

then

\[
\|E\|_2<g_0(M(\Gamma,t)).
\]

Spectral-gap stability applies.

\[
\square
\]

---

# Boundary

This theorem is finite-dimensional.

This theorem does not prove RH.

This theorem does not falsify RH.

This theorem does not use zeta zeros.

This theorem does not verify the zeta case.

This theorem does not claim novelty.

Exact audit strings:

MATRIX_SPECIFIC_NORM_CERTIFICATE

ROW_SUM_CERTIFICATE

COMBINED_MINIMUM_RADIUS_CERTIFICATE

