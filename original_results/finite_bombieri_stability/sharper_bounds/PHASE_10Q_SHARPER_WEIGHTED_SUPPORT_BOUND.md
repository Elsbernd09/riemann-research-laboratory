# Phase 10Q — Sharper Weighted Support-Stability Bound

## Purpose

Phase 10L proved the support-perturbation stability certificate

\[
2Nm_{\max}L_t(U)\delta<g_0(M).
\]

This certificate is correct but crude.

Phase 10Q proves a sharper weighted certificate that depends on the actual multiplicities and actual support displacements, rather than only on \(N\), \(m_{\max}\), and a uniform displacement bound.

---

# 1. Setup

Let

\[
\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}
\]

be a finite support with multiplicities

\[
m_1,\ldots,m_N.
\]

Let

\[
D=\operatorname{diag}(m_1,\ldots,m_N)
\]

and

\[
M(\Gamma,t)=D^{1/2}A(\Gamma,t)D^{1/2},
\]

where

\[
A(\Gamma,t)_{jk}=H_t(\alpha_j,\alpha_k).
\]

Let the perturbed support be

\[
\widetilde\Gamma_{\mathrm{dist}}
=
\{\widetilde\alpha_1,\ldots,\widetilde\alpha_N\}
\]

with the same multiplicities.

Define individual displacement sizes

\[
d_j=|\widetilde\alpha_j-\alpha_j|.
\]

Assume the kernel satisfies the local Lipschitz bound

\[
|H_t(x',y')-H_t(x,y)|
\leq
L_t(U)(|x'-x|+|y'-y|)
\]

on a neighborhood \(U\) containing the original and perturbed supports.

---

# 2. Entrywise support perturbation bound

The normalized matrix entries are

\[
M_{jk}
=
\sqrt{m_j}H_t(\alpha_j,\alpha_k)\sqrt{m_k},
\]

and

\[
\widetilde M_{jk}
=
\sqrt{m_j}H_t(\widetilde\alpha_j,\widetilde\alpha_k)\sqrt{m_k}.
\]

Therefore

\[
|\widetilde M_{jk}-M_{jk}|
\leq
\sqrt{m_jm_k}L_t(U)(d_j+d_k).
\]

This is sharper than the uniform bound

\[
2m_{\max}L_t(U)\delta.
\]

---

# 3. Weighted Frobenius perturbation radius

Define the weighted support perturbation radius

\[
\mathcal R(\Gamma,\widetilde\Gamma,t)
=
L_t(U)
\left(
\sum_{j=1}^N\sum_{k=1}^N
m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

Then

\[
\|\widetilde M-M\|_2
\leq
\|\widetilde M-M\|_F
\leq
\mathcal R(\Gamma,\widetilde\Gamma,t).
\]

---

# Theorem 10Q.1 — Weighted Support-Stability Certificate

Assume:

1. \(M(\Gamma,t)\) and \(M(\widetilde\Gamma,t)\) are Hermitian;
2. \(g_0(M(\Gamma,t))>0\);
3. \(H_t\) satisfies the local Lipschitz bound with constant \(L_t(U)\);
4. the weighted perturbation radius satisfies

\[
\mathcal R(\Gamma,\widetilde\Gamma,t)<g_0(M(\Gamma,t)).
\]

Then

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

For each entry,

\[
|E_{jk}|
=
\sqrt{m_jm_k}
\left|
H_t(\widetilde\alpha_j,\widetilde\alpha_k)
-
H_t(\alpha_j,\alpha_k)
\right|.
\]

By the Lipschitz assumption,

\[
\left|
H_t(\widetilde\alpha_j,\widetilde\alpha_k)
-
H_t(\alpha_j,\alpha_k)
\right|
\leq
L_t(U)(d_j+d_k).
\]

Therefore,

\[
|E_{jk}|
\leq
\sqrt{m_jm_k}L_t(U)(d_j+d_k).
\]

Squaring and summing over \(j,k\),

\[
\|E\|_F^2
=
\sum_{j,k}|E_{jk}|^2
\leq
L_t(U)^2
\sum_{j,k}m_jm_k(d_j+d_k)^2.
\]

Taking square roots,

\[
\|E\|_F
\leq
L_t(U)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

Thus

\[
\|E\|_2\leq\|E\|_F\leq\mathcal R(\Gamma,\widetilde\Gamma,t).
\]

If

\[
\mathcal R(\Gamma,\widetilde\Gamma,t)<g_0(M(\Gamma,t)),
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

# Corollary 10Q.2 — Total multiplicity uniform-displacement certificate

Let

\[
M_{\mathrm{tot}}=\sum_{j=1}^N m_j.
\]

If

\[
d_j\leq\delta
\]

for all \(j\), then

\[
\mathcal R(\Gamma,\widetilde\Gamma,t)
\leq
2L_t(U)M_{\mathrm{tot}}\delta.
\]

Therefore, the certificate

\[
2L_t(U)M_{\mathrm{tot}}\delta<g_0(M(\Gamma,t))
\]

implies

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

---

# Proof

If \(d_j\leq\delta\), then

\[
d_j+d_k\leq2\delta.
\]

Therefore,

\[
\sum_{j,k}m_jm_k(d_j+d_k)^2
\leq
\sum_{j,k}m_jm_k(2\delta)^2
=
4\delta^2
\left(\sum_jm_j\right)
\left(\sum_km_k\right).
\]

Thus

\[
\mathcal R(\Gamma,\widetilde\Gamma,t)
\leq
L_t(U)\sqrt{4\delta^2M_{\mathrm{tot}}^2}
=
2L_t(U)M_{\mathrm{tot}}\delta.
\]

Theorem 10Q.1 now applies.

\[
\square
\]

---

# 4. Comparison with the previous crude bound

The old Phase 10L certificate was

\[
2Nm_{\max}L_t(U)\delta<g_0(M).
\]

Since

\[
M_{\mathrm{tot}}=\sum_jm_j\leq Nm_{\max},
\]

the new uniform-displacement certificate

\[
2L_t(U)M_{\mathrm{tot}}\delta<g_0(M)
\]

is always at least as sharp and can be strictly sharper.

The fully weighted certificate

\[
\mathcal R(\Gamma,\widetilde\Gamma,t)<g_0(M)
\]

is sharper still, because it uses the actual displacement vector \(d_1,\ldots,d_N\).

---

# 5. Why this is more serious

The previous result used a worst-case bound.

This phase introduces:

1. actual multiplicity weights;
2. actual displacement magnitudes;
3. a Frobenius-weighted perturbation radius;
4. a strictly sharper certificate than \(2Nm_{\max}L_t(U)\delta\).

This moves the project closer to a useful computational audit theorem rather than a generic perturbation restatement.

Novelty is still not claimed.

---

# Boundary

This theorem does not prove RH.

This theorem does not falsify RH.

This theorem does not use zeta zeros.

This theorem does not verify the zeta case.

This theorem does not claim novelty.

