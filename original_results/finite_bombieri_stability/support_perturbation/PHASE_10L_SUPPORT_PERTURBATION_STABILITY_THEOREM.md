# Phase 10L — Support-Perturbation Stability Theorem

## Purpose

Phase 10K defined the support-perturbation model and Lipschitz kernel assumption.

Phase 10L states and proves the stronger finite theorem:

Support perturbations imply controlled matrix perturbations, which imply preservation of the negative eigenvalue count under a computable spectral-gap certificate.

---

# Theorem 10L.1 — Support-Perturbation Stability

Let

\[
\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}
\]

be a finite distinct support with positive multiplicities

\[
m_1,\ldots,m_N.
\]

Let

\[
D=\operatorname{diag}(m_1,\ldots,m_N)
\]

and let

\[
m_{\max}=\max_{1\leq j\leq N}m_j.
\]

Let

\[
H_t:U\times U\to\mathbb C
\]

be a kernel defined on a neighborhood \(U\subset\mathbb C\) containing both the original support and the perturbed support.

Assume \(H_t\) is Lipschitz on \(U\times U\), meaning there exists a finite constant

\[
L_t(U)
\]

such that

\[
|H_t(x',y')-H_t(x,y)|
\leq
L_t(U)(|x'-x|+|y'-y|)
\]

for all \(x,y,x',y'\in U\).

Let the perturbed support be

\[
\widetilde\Gamma_{\mathrm{dist}}
=
\{\widetilde\alpha_1,\ldots,\widetilde\alpha_N\}
\]

with the same multiplicities and with

\[
|\widetilde\alpha_j-\alpha_j|\leq\delta
\]

for every \(j\).

Define

\[
M(\Gamma,t)=D^{1/2}A(\Gamma,t)D^{1/2},
\]

where

\[
A(\Gamma,t)_{jk}=H_t(\alpha_j,\alpha_k),
\]

and

\[
M(\widetilde\Gamma,t)=D^{1/2}A(\widetilde\Gamma,t)D^{1/2},
\]

where

\[
A(\widetilde\Gamma,t)_{jk}=H_t(\widetilde\alpha_j,\widetilde\alpha_k).
\]

Assume both matrices are Hermitian and that

\[
g_0(M(\Gamma,t))>0.
\]

If

\[
2Nm_{\max}L_t(U)\delta<g_0(M(\Gamma,t)),
\]

then

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

---

# Proof

Set

\[
M=M(\Gamma,t),
\qquad
\widetilde M=M(\widetilde\Gamma,t).
\]

The entries are

\[
M_{jk}
=
\sqrt{m_j}H_t(\alpha_j,\alpha_k)\sqrt{m_k}
\]

and

\[
\widetilde M_{jk}
=
\sqrt{m_j}H_t(\widetilde\alpha_j,\widetilde\alpha_k)\sqrt{m_k}.
\]

Subtracting gives

\[
\widetilde M_{jk}-M_{jk}
=
\sqrt{m_j}
\left[
H_t(\widetilde\alpha_j,\widetilde\alpha_k)-H_t(\alpha_j,\alpha_k)
\right]
\sqrt{m_k}.
\]

Taking absolute values,

\[
|\widetilde M_{jk}-M_{jk}|
=
\sqrt{m_jm_k}
\left|
H_t(\widetilde\alpha_j,\widetilde\alpha_k)-H_t(\alpha_j,\alpha_k)
\right|.
\]

By the Lipschitz condition,

\[
\left|
H_t(\widetilde\alpha_j,\widetilde\alpha_k)-H_t(\alpha_j,\alpha_k)
\right|
\leq
L_t(U)
\left(
|\widetilde\alpha_j-\alpha_j|
+
|\widetilde\alpha_k-\alpha_k|
\right).
\]

Since

\[
|\widetilde\alpha_j-\alpha_j|\leq\delta
\]

and

\[
|\widetilde\alpha_k-\alpha_k|\leq\delta,
\]

we obtain

\[
\left|
H_t(\widetilde\alpha_j,\widetilde\alpha_k)-H_t(\alpha_j,\alpha_k)
\right|
\leq
2L_t(U)\delta.
\]

Therefore,

\[
|\widetilde M_{jk}-M_{jk}|
\leq
2\sqrt{m_jm_k}L_t(U)\delta.
\]

Since

\[
\sqrt{m_jm_k}\leq m_{\max},
\]

we get the uniform normalized matrix-entry bound

\[
|\widetilde M_{jk}-M_{jk}|
\leq
2m_{\max}L_t(U)\delta.
\]

Define

\[
\varepsilon=2m_{\max}L_t(U)\delta.
\]

Then

\[
|\widetilde M_{jk}-M_{jk}|\leq\varepsilon
\]

for all \(j,k\).

By Theorem 10G.1, if

\[
N\varepsilon<g_0(M),
\]

then

\[
n_-(\widetilde M)=n_-(M).
\]

Substituting

\[
\varepsilon=2m_{\max}L_t(U)\delta
\]

gives exactly the assumed certificate

\[
2Nm_{\max}L_t(U)\delta<g_0(M(\Gamma,t)).
\]

Therefore,

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

\[
\square
\]

---

# Corollary 10L.2 — Maximum admissible support displacement

Under the assumptions of Theorem 10L.1, a sufficient upper bound for support perturbation stability is

\[
\delta
<
\frac{g_0(M(\Gamma,t))}
{2Nm_{\max}L_t(U)}.
\]

Whenever this holds,

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

---

# Interpretation

This theorem strengthens the Phase 10G result.

Phase 10G assumed matrix entries were already close.

Phase 10L proves that matrix entries are close when the support points are close and the kernel is Lipschitz.

This creates a support-level stability certificate:

\[
\boxed{
2Nm_{\max}L_t(U)\delta<g_0(M(\Gamma,t)).
}
\]

---

# Why this is closer to Level 3

This theorem is more specialized to finite kernel models than a generic matrix perturbation theorem.

It converts finite support perturbation into negative-count stability.

The possible research-note contribution is the explicit finite support-level audit certificate for Bombieri-style matrix computations.

Novelty is still not claimed until prior-art and expert review.

---

# Boundary

This is a finite synthetic theorem.

This theorem does not prove RH.

This theorem does not falsify RH.

This theorem does not use zeta zeros.

This theorem does not verify the zeta case.

This theorem does not claim novelty.

