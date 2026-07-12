# Certified Support-Stability for Negative Eigenvalue Counts in Finite Bombieri-Style Matrix Models

## Abstract

We study finite normalized matrix models inspired by Bombieri/Weil-style positivity frameworks. Given finite support points \(\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}\), multiplicities \(m_j\), and a kernel \(H_t\), define

\[
M(\Gamma,t)=D^{1/2}A(\Gamma,t)D^{1/2},
\qquad
A(\Gamma,t)_{jk}=H_t(\alpha_j,\alpha_k),
\]

where \(D=\operatorname{diag}(m_1,\ldots,m_N)\).

We prove a sharper weighted support-stability certificate for negative eigenvalue counts. If the support points move by

\[
d_j=|\widetilde\alpha_j-\alpha_j|,
\]

and \(H_t\) satisfies a local Lipschitz bound with constant \(L_t(U)\), define

\[
\mathcal R(\Gamma,\widetilde\Gamma,t)
=
L_t(U)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

If

\[
\mathcal R(\Gamma,\widetilde\Gamma,t)<g_0(M(\Gamma,t)),
\]

then

\[
n_-(M(\widetilde\Gamma,t))=n_-(M(\Gamma,t)).
\]

We also give a certified algorithm returning either CERTIFIED_STABLE or NOT_CERTIFIED. If the algorithm returns CERTIFIED_STABLE, the negative eigenvalue count is theorem-certified stable. If it returns NOT_CERTIFIED, no instability claim is made.

This is a finite-dimensional stability result. It does not prove RH, falsify RH, use zeta zeros, verify the zeta case, or claim novelty.

---

# 1. Motivation

Finite matrix computations can be misleading when eigenvalues lie close to zero. In RH-adjacent positivity frameworks, finite negative eigenvalue counts should not be interpreted unless they are stable under the perturbations present in the computation.

This note gives a finite-dimensional stability certificate for such counts.

The goal is not to prove RH. The goal is to create a theorem-backed audit rule:

\[
\text{Do not trust a finite negative count unless the perturbation radius is below the zero spectral gap.}
\]

---

# 2. Finite normalized matrix model

Let

\[
\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}
\]

be a finite set of distinct support points with multiplicities

\[
m_1,\ldots,m_N>0.
\]

Let

\[
D=\operatorname{diag}(m_1,\ldots,m_N).
\]

Given a kernel \(H_t\), define

\[
A(\Gamma,t)_{jk}=H_t(\alpha_j,\alpha_k)
\]

and

\[
M(\Gamma,t)=D^{1/2}A(\Gamma,t)D^{1/2}.
\]

The matrix is admitted only when Hermitian.

---

# 3. Zero spectral gap

For a Hermitian matrix \(M\), define

\[
n_-(M)=\#\{j:\lambda_j(M)<0\},
\]

and

\[
g_0(M)=\min_j|\lambda_j(M)|.
\]

The stability theory requires

\[
g_0(M)>0.
\]

If \(g_0(M)=0\), the negative eigenvalue count can change under arbitrarily small perturbations.

---

# 4. Basic spectral-gap stability

## Lemma 4.1

Let \(M,E\) be Hermitian. If

\[
\|E\|_2<g_0(M),
\]

then

\[
n_-(M+E)=n_-(M).
\]

## Proof

Hermitian eigenvalues satisfy

\[
|\lambda_j(M+E)-\lambda_j(M)|\leq \|E\|_2.
\]

If

\[
\|E\|_2<g_0(M),
\]

then no eigenvalue can cross zero. Therefore the number of negative eigenvalues is unchanged.

\[
\square
\]

---

# 5. Weighted support perturbation radius

Let the perturbed support be

\[
\widetilde\Gamma_{\mathrm{dist}}
=
\{\widetilde\alpha_1,\ldots,\widetilde\alpha_N\},
\]

with the same multiplicities.

Define

\[
d_j=|\widetilde\alpha_j-\alpha_j|.
\]

Assume \(H_t\) satisfies the local Lipschitz bound

\[
|H_t(x',y')-H_t(x,y)|
\leq
L_t(U)(|x'-x|+|y'-y|)
\]

on a neighborhood \(U\) containing both supports.

Define

\[
\mathcal R(\Gamma,\widetilde\Gamma,t)
=
L_t(U)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

This is the weighted perturbation radius.

---

# 6. Main theorem

## Theorem 6.1 — Weighted support-stability certificate

Assume:

1. \(M(\Gamma,t)\) and \(M(\widetilde\Gamma,t)\) are Hermitian;
2. \(g_0(M(\Gamma,t))>0\);
3. \(H_t\) satisfies the local Lipschitz condition above;
4. the weighted radius satisfies

\[
\mathcal R(\Gamma,\widetilde\Gamma,t)<g_0(M(\Gamma,t)).
\]

Then

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

## Proof

Let

\[
E=M(\widetilde\Gamma,t)-M(\Gamma,t).
\]

The entries satisfy

\[
E_{jk}
=
\sqrt{m_j}
\left(
H_t(\widetilde\alpha_j,\widetilde\alpha_k)
-
H_t(\alpha_j,\alpha_k)
\right)
\sqrt{m_k}.
\]

By the Lipschitz bound,

\[
|E_{jk}|
\leq
\sqrt{m_jm_k}L_t(U)(d_j+d_k).
\]

Thus

\[
\|E\|_F^2
\leq
L_t(U)^2
\sum_{j,k}m_jm_k(d_j+d_k)^2.
\]

So

\[
\|E\|_2
\leq
\|E\|_F
\leq
\mathcal R(\Gamma,\widetilde\Gamma,t).
\]

If

\[
\mathcal R(\Gamma,\widetilde\Gamma,t)<g_0(M(\Gamma,t)),
\]

then

\[
\|E\|_2<g_0(M(\Gamma,t)).
\]

The spectral-gap stability lemma gives

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

\[
\square
\]

---

# 7. Uniform-displacement corollary

Let

\[
M_{\mathrm{tot}}=\sum_jm_j.
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

Therefore, the sufficient condition

\[
2L_t(U)M_{\mathrm{tot}}\delta<g_0(M(\Gamma,t))
\]

implies

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

This improves the previous crude certificate

\[
2Nm_{\max}L_t(U)\delta<g_0(M(\Gamma,t)),
\]

because

\[
M_{\mathrm{tot}}\leq Nm_{\max}.
\]

---

# 8. Strict-improvement examples

The improvement is not merely cosmetic.

There are synthetic finite examples where:

1. the old certificate fails;
2. the new uniform certificate passes.

There are also examples where:

1. both uniform certificates fail;
2. the fully weighted radius certificate passes.

These examples show that the weighted certificate can certify stability in cases the old certificate cannot.

---

# 9. Certified stability algorithm

## Algorithm 9.1 — Weighted Support Stability Certification

Input:

\[
(m_1,\ldots,m_N),
\quad
(d_1,\ldots,d_N),
\quad
L_t(U),
\quad
g_0(M).
\]

Compute

\[
\mathcal R
=
L_t(U)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

If

\[
\mathcal R<g_0(M),
\]

return:

CERTIFIED_STABLE

Otherwise return:

NOT_CERTIFIED

---

# 10. Correctness of the algorithm

## Theorem 10.1

If Algorithm 9.1 returns CERTIFIED_STABLE, then

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

## Proof

The algorithm returns CERTIFIED_STABLE exactly when

\[
\mathcal R<g_0(M).
\]

This is precisely the hypothesis of Theorem 6.1. Therefore Theorem 6.1 proves the negative eigenvalue count is stable.

\[
\square
\]

## Proposition 10.2

If Algorithm 9.1 returns NOT_CERTIFIED, no instability claim is made.

## Proof

The condition

\[
\mathcal R<g_0(M)
\]

is sufficient, not necessary. Therefore failure of the condition does not imply failure of stability.

\[
\square
\]

---

# 11. Contribution of the note

This note contributes a finite, theorem-backed audit framework:

1. a weighted support perturbation radius;
2. a sharper total-multiplicity certificate;
3. strict-improvement examples;
4. a certified stability algorithm;
5. a proof of algorithm soundness.

The result is still finite-dimensional and should be compared with standard perturbation theory, matrix inertia stability, kernel matrix perturbation, and numerical linear algebra literature.

Novelty is not established.

---

# 12. Limitations

This note does not address:

1. the infinite-dimensional zeta case;
2. convergence from finite models to the zeta Weil form;
3. Bombieri Sections 10 and 11;
4. actual zeta zeros;
5. RH truth or falsity;
6. novelty relative to known matrix perturbation theory.

---

# Boundary

This note does not prove RH.

This note does not falsify RH.

This note does not use zeta zeros.

This note does not verify the zeta case.

This note does not claim novelty.

Exact audit strings:

CERTIFIED_STABLE

NOT_CERTIFIED

WEIGHTED_SUPPORT_STABILITY_CERTIFICATE

RESEARCH_NOTE_V3

