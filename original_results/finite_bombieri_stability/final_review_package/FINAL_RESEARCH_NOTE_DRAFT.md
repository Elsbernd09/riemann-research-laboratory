# Support-Stability Certificates for Negative Eigenvalue Counts in Finite Bombieri-Style Matrix Models

## Abstract

We study finite normalized matrix models inspired by Bombieri/Weil-style positivity frameworks. Given a finite support \(\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}\), multiplicities \(m_j\), and a finite kernel \(H_t\), we form

\[
M(\Gamma,t)=D^{1/2}A(\Gamma,t)D^{1/2},
\qquad
A(\Gamma,t)_{jk}=H_t(\alpha_j,\alpha_k).
\]

We prove two finite stability certificates for the negative eigenvalue count \(n_-(M)\). First, if a Hermitian perturbation \(\widetilde M\) satisfies

\[
|\widetilde M_{jk}-M_{jk}|\leq\varepsilon
\]

and

\[
N\varepsilon<g_0(M),
\]

then

\[
n_-(\widetilde M)=n_-(M).
\]

Second, and more specifically for finite kernel models, if the support points move by at most \(\delta\),

\[
|\widetilde\alpha_j-\alpha_j|\leq\delta,
\]

and \(H_t\) is locally Lipschitz with constant \(L_t(U)\), then the support-level certificate

\[
2Nm_{\max}L_t(U)\delta<g_0(M(\Gamma,t))
\]

implies

\[
n_-(M(\widetilde\Gamma,t))=n_-(M(\Gamma,t)).
\]

These results are finite-dimensional stability statements. They do not prove, falsify, or verify the Riemann Hypothesis. Their purpose is to give explicit audit certificates for finite RH-adjacent matrix computations: negative eigenvalue counts should be interpreted only when protected by a spectral gap.

---

# 1. Introduction

Finite matrix computations appear naturally in reconstructions, toy models, and finite approximations of positivity criteria related to analytic number theory. In such computations, eigenvalue counts are often tempting to interpret. But negative eigenvalue counts can be unstable when eigenvalues lie close to zero.

This note isolates a finite-dimensional stability principle for normalized Bombieri-style matrix models. The main contribution is an explicit support-level certificate: if the finite support is perturbed slightly, and the kernel is locally Lipschitz, then the negative eigenvalue count is stable whenever the perturbation is smaller than the zero spectral gap.

The note is deliberately finite. It does not address the infinite zeta limit, zeta zeros, or the truth of RH.

---

# 2. Finite normalized matrix model

Let

\[
\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}
\]

be a finite support with positive integer multiplicities

\[
m_1,\ldots,m_N.
\]

Let

\[
D=\operatorname{diag}(m_1,\ldots,m_N),
\qquad
m_{\max}=\max_jm_j.
\]

Given a kernel

\[
H_t:\Gamma_{\mathrm{dist}}\times\Gamma_{\mathrm{dist}}\to\mathbb C,
\]

define

\[
A(\Gamma,t)_{jk}=H_t(\alpha_j,\alpha_k)
\]

and

\[
M(\Gamma,t)=D^{1/2}A(\Gamma,t)D^{1/2}.
\]

Equivalently,

\[
M(\Gamma,t)_{jk}
=
\sqrt{m_j}H_t(\alpha_j,\alpha_k)\sqrt{m_k}.
\]

The matrix is admitted into the theorem only when it is Hermitian.

---

# 3. Hermitian admission condition

## Lemma 1

The matrix

\[
M(\Gamma,t)=D^{1/2}A(\Gamma,t)D^{1/2}
\]

is Hermitian if and only if

\[
H_t(\alpha_j,\alpha_k)
=
\overline{H_t(\alpha_k,\alpha_j)}
\]

for all \(j,k\).

## Proof

The entries are

\[
M_{jk}=\sqrt{m_j}H_t(\alpha_j,\alpha_k)\sqrt{m_k}.
\]

The Hermitian condition is

\[
M_{jk}=\overline{M_{kj}}.
\]

Since \(m_j,m_k\) are positive real integers,

\[
\overline{M_{kj}}
=
\sqrt{m_j}\overline{H_t(\alpha_k,\alpha_j)}\sqrt{m_k}.
\]

Dividing by the positive scalar \(\sqrt{m_jm_k}\) gives the result.

\[
\square
\]

---

# 4. Entrywise stability certificate

For a Hermitian matrix \(M\), define

\[
n_-(M)=\#\{j:\lambda_j(M)<0\},
\]

and

\[
g_0(M)=\min_j|\lambda_j(M)|.
\]

## Theorem 1 — Entrywise negative-count stability

Let \(M,\widetilde M\in\mathbb C^{N\times N}\) be Hermitian. Suppose

\[
|\widetilde M_{jk}-M_{jk}|\leq\varepsilon
\]

for all \(j,k\), and

\[
N\varepsilon<g_0(M).
\]

Then

\[
n_-(\widetilde M)=n_-(M).
\]

## Proof

Let

\[
E=\widetilde M-M.
\]

Then \(E\) is Hermitian, and the entrywise bound gives

\[
\|E\|_F
=
\left(\sum_{j,k}|E_{jk}|^2\right)^{1/2}
\leq
N\varepsilon.
\]

Since

\[
\|E\|_2\leq\|E\|_F,
\]

we have

\[
\|E\|_2\leq N\varepsilon<g_0(M).
\]

For Hermitian matrices, eigenvalues satisfy the perturbation bound

\[
|\lambda_j(M+E)-\lambda_j(M)|\leq \|E\|_2.
\]

Thus no eigenvalue can cross zero, and the negative eigenvalue count is unchanged.

\[
\square
\]

---

# 5. Kernel-entry certificate

Suppose the kernel values satisfy

\[
|\widetilde H_t(\alpha_j,\alpha_k)-H_t(\alpha_j,\alpha_k)|\leq\eta.
\]

Then

\[
|\widetilde M_{jk}-M_{jk}|
\leq
m_{\max}\eta.
\]

Therefore

\[
Nm_{\max}\eta<g_0(M)
\]

is a sufficient certificate for

\[
n_-(\widetilde M)=n_-(M).
\]

---

# 6. Support-perturbation model

Now suppose the support itself is perturbed.

Let

\[
\widetilde\Gamma_{\mathrm{dist}}
=
\{\widetilde\alpha_1,\ldots,\widetilde\alpha_N\}
\]

with the same multiplicities and

\[
|\widetilde\alpha_j-\alpha_j|\leq\delta
\]

for all \(j\).

Assume \(H_t\) is defined on a neighborhood \(U\subset\mathbb C\) containing both supports and satisfies the Lipschitz bound

\[
|H_t(x',y')-H_t(x,y)|
\leq
L_t(U)(|x'-x|+|y'-y|)
\]

for all \(x,y,x',y'\in U\).

---

# 7. Main support-stability theorem

## Theorem 2 — Support-perturbation stability

Under the support-perturbation setup above, assume

\[
M(\Gamma,t)
\]

and

\[
M(\widetilde\Gamma,t)
\]

are Hermitian and

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

## Proof

For each entry,

\[
M(\Gamma,t)_{jk}
=
\sqrt{m_j}H_t(\alpha_j,\alpha_k)\sqrt{m_k},
\]

and

\[
M(\widetilde\Gamma,t)_{jk}
=
\sqrt{m_j}H_t(\widetilde\alpha_j,\widetilde\alpha_k)\sqrt{m_k}.
\]

Thus

\[
|M(\widetilde\Gamma,t)_{jk}-M(\Gamma,t)_{jk}|
=
\sqrt{m_jm_k}
\left|
H_t(\widetilde\alpha_j,\widetilde\alpha_k)
-
H_t(\alpha_j,\alpha_k)
\right|.
\]

The Lipschitz assumption gives

\[
\left|
H_t(\widetilde\alpha_j,\widetilde\alpha_k)
-
H_t(\alpha_j,\alpha_k)
\right|
\leq
L_t(U)
\left(
|\widetilde\alpha_j-\alpha_j|
+
|\widetilde\alpha_k-\alpha_k|
\right)
\leq
2L_t(U)\delta.
\]

Therefore

\[
|M(\widetilde\Gamma,t)_{jk}-M(\Gamma,t)_{jk}|
\leq
2m_{\max}L_t(U)\delta.
\]

Set

\[
\varepsilon=2m_{\max}L_t(U)\delta.
\]

Theorem 1 applies if

\[
N\varepsilon<g_0(M(\Gamma,t)).
\]

This is exactly

\[
2Nm_{\max}L_t(U)\delta<g_0(M(\Gamma,t)).
\]

Hence

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

\[
\square
\]

---

# 8. Maximum allowed support displacement

The support-stability theorem gives the explicit sufficient bound

\[
\delta<
\frac{g_0(M(\Gamma,t))}
{2Nm_{\max}L_t(U)}.
\]

When this holds, the negative eigenvalue count is stable under all support perturbations of size at most \(\delta\).

---

# 9. Synthetic examples

The examples use the toy kernel

\[
H(x,y)=x+y.
\]

This kernel is used only to demonstrate the stability theorem. It is not a zeta kernel.

The examples show:

1. a case where the support-level certificate passes and stability is guaranteed;
2. a case where the certificate fails but the count happens to remain stable;
3. a case where the certificate fails and the count changes;
4. a case showing that multiplicity weights reduce the allowed perturbation budget.

The main lesson is that the support-level certificate is sufficient, not necessary.

---

# 10. Relation to RH-adjacent computation

This result does not prove RH or say anything directly about zeta zeros.

Its relevance is methodological. In finite matrix computations inspired by RH-adjacent positivity criteria, a negative eigenvalue count is not automatically meaningful. It should be accompanied by a stability certificate.

This note provides such a certificate at two levels:

\[
N\varepsilon<g_0(M)
\]

for entrywise matrix perturbations, and

\[
2Nm_{\max}L_t(U)\delta<g_0(M)
\]

for support perturbations under Lipschitz kernel control.

---

# 11. Limitations

This note does not address:

1. the infinite-dimensional zeta Weil form;
2. Bombieri Sections 10 and 11;
3. convergence from finite synthetic models to the zeta case;
4. actual zeta zeros;
5. the truth of RH;
6. novelty relative to the perturbation theory and numerical linear algebra literature.

---

# 12. Conclusion

We proved finite stability certificates for negative eigenvalue counts in normalized Bombieri-style matrix models. The support-perturbation theorem is the stronger certificate: it derives matrix-entry control from finite support displacement and local Lipschitz control of the kernel.

The result is finite and synthetic, but it gives a clean audit rule for finite RH-adjacent computations: do not trust negative eigenvalue counts unless they are protected by a spectral gap relative to the relevant perturbation model.

---

# Boundary statement

This draft does not prove RH.

This draft does not falsify RH.

This draft does not use zeta zeros.

This draft does not verify the zeta case.

This draft does not claim novelty.

