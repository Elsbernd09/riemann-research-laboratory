# Phase 10G — Complete Finite Bombieri-Style Stability Theorem

## Purpose

Phases 10B through 10F built the components:

1. exact finite matrix object;
2. admissible finite symmetry classes;
3. Hermitian/self-adjoint admission rule;
4. entrywise perturbation to operator-norm bound;
5. spectral-gap stability.

Phase 10G states and proves the first complete finite Bombieri-style perturbation stability theorem.

---

# Theorem 10G.1 — Finite Bombieri-Style Negative-Count Stability

Let

\[
\Gamma
\]

be a finite multiset with distinct support

\[
\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}
\]

and positive multiplicities

\[
m_1,\ldots,m_N.
\]

Let

\[
D=\operatorname{diag}(m_1,\ldots,m_N).
\]

Let

\[
H_t,\widetilde H_t:
\Gamma_{\mathrm{dist}}\times\Gamma_{\mathrm{dist}}
\to
\mathbb C
\]

be two finite kernels.

Define

\[
A_{jk}=H_t(\alpha_j,\alpha_k),
\qquad
\widetilde A_{jk}=\widetilde H_t(\alpha_j,\alpha_k),
\]

and define normalized finite matrices

\[
M=D^{1/2}AD^{1/2},
\qquad
\widetilde M=D^{1/2}\widetilde A D^{1/2}.
\]

Assume:

1. \(M\) and \(\widetilde M\) are Hermitian;
2. \(g_0(M)>0\), where

\[
g_0(M)=\min_j|\lambda_j(M)|;
\]

3. the normalized entrywise perturbation satisfies

\[
|\widetilde M_{jk}-M_{jk}|\leq \varepsilon
\]

for all \(j,k\);

4. the certified perturbation size obeys

\[
N\varepsilon<g_0(M).
\]

Then

\[
n_-(\widetilde M)=n_-(M).
\]

---

# Proof

Let

\[
E=\widetilde M-M.
\]

By assumption,

\[
M=M^*,
\qquad
\widetilde M=\widetilde M^*.
\]

Therefore

\[
E^*=E,
\]

so \(E\) is Hermitian.

By the normalized entrywise perturbation assumption,

\[
|E_{jk}|\leq \varepsilon
\]

for all \(j,k\).

By Phase 10E, the operator norm satisfies

\[
\|E\|_2\leq N\varepsilon.
\]

By assumption,

\[
N\varepsilon<g_0(M).
\]

Hence

\[
\|E\|_2<g_0(M).
\]

By Phase 10F spectral-gap stability,

\[
n_-(M+E)=n_-(M).
\]

Since

\[
M+E=\widetilde M,
\]

we conclude that

\[
n_-(\widetilde M)=n_-(M).
\]

\[
\square
\]

---

# Corollary 10G.2 — Kernel-Entry Version With Multiplicity Weights

Under the same setup, suppose the kernel-level perturbation satisfies

\[
|\widetilde H_t(\alpha_j,\alpha_k)-H_t(\alpha_j,\alpha_k)|
\leq
\eta
\]

for all \(j,k\).

Then

\[
|\widetilde M_{jk}-M_{jk}|
=
\sqrt{m_jm_k}\,
|\widetilde H_t(\alpha_j,\alpha_k)-H_t(\alpha_j,\alpha_k)|.
\]

Therefore, if

\[
\sqrt{m_jm_k}\eta\leq\varepsilon
\]

for all \(j,k\), and

\[
N\varepsilon<g_0(M),
\]

then

\[
n_-(\widetilde M)=n_-(M).
\]

In particular, if

\[
m_{\max}=\max_j m_j,
\]

then

\[
|\widetilde H_t(\alpha_j,\alpha_k)-H_t(\alpha_j,\alpha_k)|
\leq
\eta
\]

implies

\[
|\widetilde M_{jk}-M_{jk}|
\leq
m_{\max}\eta.
\]

Thus the sufficient certificate

\[
Nm_{\max}\eta<g_0(M)
\]

implies

\[
n_-(\widetilde M)=n_-(M).
\]

---

# Proof

The entries of the normalized matrices are

\[
M_{jk}=\sqrt{m_j}H_t(\alpha_j,\alpha_k)\sqrt{m_k}
\]

and

\[
\widetilde M_{jk}=\sqrt{m_j}\widetilde H_t(\alpha_j,\alpha_k)\sqrt{m_k}.
\]

Subtracting gives

\[
\widetilde M_{jk}-M_{jk}
=
\sqrt{m_j}
\left(
\widetilde H_t(\alpha_j,\alpha_k)-H_t(\alpha_j,\alpha_k)
\right)
\sqrt{m_k}.
\]

Taking absolute values,

\[
|\widetilde M_{jk}-M_{jk}|
=
\sqrt{m_jm_k}
|\widetilde H_t(\alpha_j,\alpha_k)-H_t(\alpha_j,\alpha_k)|.
\]

If the right-hand side is bounded by \(\varepsilon\) for all \(j,k\), then Theorem 10G.1 applies.

Since

\[
\sqrt{m_jm_k}\leq m_{\max},
\]

a uniform kernel error bound \(\eta\) gives

\[
|\widetilde M_{jk}-M_{jk}|\leq m_{\max}\eta.
\]

Therefore

\[
Nm_{\max}\eta<g_0(M)
\]

is a sufficient condition for

\[
n_-(\widetilde M)=n_-(M).
\]

\[
\square
\]

---

# Interpretation

The theorem gives a finite stability certificate:

If a finite Bombieri-style normalized matrix has a nonzero spectral gap around zero, then sufficiently small kernel or implementation perturbations cannot change the negative eigenvalue count.

The computable certificate is:

\[
N\varepsilon<g_0(M)
\]

at the normalized matrix level, or

\[
Nm_{\max}\eta<g_0(M)
\]

at the uniform kernel-error level.

---

# What this theorem is

This is a finite-dimensional perturbation stability theorem specialized to the locked finite Bombieri-style matrix class.

It is suitable as the first theorem in the professor-readable research note.

---

# What this theorem is not

This theorem does not prove RH.

This theorem does not falsify RH.

This theorem does not use zeta zeros.

This theorem does not verify the zeta case.

This theorem does not claim novelty yet.

