# Combined-Radius Support-Stability Certificates for Negative Eigenvalue Counts in Finite Bombieri-Style Matrix Models

## Abstract

We study finite normalized matrix models inspired by Bombieri/Weil-style positivity frameworks. Given support points \(\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}\), multiplicities \(m_j\), and a kernel \(H_t\), define

\[
M(\Gamma,t)=D^{1/2}A(\Gamma,t)D^{1/2},
\qquad
A(\Gamma,t)_{jk}=H_t(\alpha_j,\alpha_k).
\]

For support perturbations \(\widetilde\alpha_j\) with displacement sizes

\[
d_j=|\widetilde\alpha_j-\alpha_j|,
\]

we define two certified perturbation radii:

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
\max_j
\sum_k
\sqrt{m_jm_k}L_t(U)(d_j+d_k).
\]

The combined radius is

\[
\mathcal R_{\min}
=
\min\{\mathcal R_F,\mathcal R_{\mathrm{row}}\}.
\]

We prove that if

\[
\mathcal R_{\min}<g_0(M(\Gamma,t)),
\]

then

\[
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
\]

We also give a certified algorithm returning CERTIFIED_STABLE or NOT_CERTIFIED and prove its soundness.

This is a finite-dimensional stability framework. It does not prove RH, falsify RH, use zeta zeros, verify the zeta case, or claim novelty.

---

# 1. Motivation

Finite eigenvalue computations are unstable near zero. If a finite model produces a negative eigenvalue count, that count should not be interpreted unless it is stable under the perturbations present in the model.

This note develops a finite audit framework:

\[
\text{support perturbation}
\rightarrow
\text{certified norm upper bound}
\rightarrow
\text{spectral-gap check}
\rightarrow
\text{stable negative eigenvalue count}.
\]

The project is motivated by Bombieri/Weil-style finite matrix models, but the result remains finite-dimensional and does not establish any statement about RH.

---

# 2. Finite normalized matrix model

Let

\[
\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}
\]

be a finite set of support points with multiplicities

\[
m_1,\ldots,m_N>0.
\]

Let

\[
D=\operatorname{diag}(m_1,\ldots,m_N).
\]

Given a kernel \(H_t\), define

\[
A(\Gamma,t)_{jk}=H_t(\alpha_j,\alpha_k),
\]

and

\[
M(\Gamma,t)=D^{1/2}A(\Gamma,t)D^{1/2}.
\]

The model is theorem-admitted only when \(M(\Gamma,t)\) and the perturbed matrix are Hermitian.

---

# 3. Spectral-gap principle

For Hermitian \(M\), define

\[
n_-(M)=\#\{j:\lambda_j(M)<0\},
\]

and

\[
g_0(M)=\min_j|\lambda_j(M)|.
\]

If

\[
g_0(M)>0
\]

and

\[
\|E\|_2<g_0(M),
\]

then

\[
n_-(M+E)=n_-(M).
\]

This is the core finite stability principle.

---

# 4. Support perturbation setup

Let

\[
\widetilde\Gamma_{\mathrm{dist}}
=
\{\widetilde\alpha_1,\ldots,\widetilde\alpha_N\}
\]

with the same multiplicities, and define

\[
d_j=|\widetilde\alpha_j-\alpha_j|.
\]

Assume \(H_t\) satisfies a local Lipschitz bound on a neighborhood \(U\):

\[
|H_t(x',y')-H_t(x,y)|
\leq
L_t(U)(|x'-x|+|y'-y|).
\]

Then the perturbation entries satisfy

\[
|E_{jk}|
\leq
\sqrt{m_jm_k}L_t(U)(d_j+d_k).
\]

---

# 5. Frobenius certificate

Define

\[
\mathcal R_F
=
L_t(U)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2}.
\]

Then

\[
\|E\|_2\leq\|E\|_F\leq\mathcal R_F.
\]

Therefore, if

\[
\mathcal R_F<g_0(M(\Gamma,t)),
\]

then

\[
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
\]

---

# 6. Row-sum certificate

Define

\[
\mathcal R_{\mathrm{row}}
=
\max_j
\sum_k
\sqrt{m_jm_k}L_t(U)(d_j+d_k).
\]

Since the majorant matrix is symmetric, the row-sum bound gives

\[
\|E\|_2\leq\mathcal R_{\mathrm{row}}.
\]

Therefore, if

\[
\mathcal R_{\mathrm{row}}<g_0(M(\Gamma,t)),
\]

then

\[
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
\]

---

# 7. Main combined-radius theorem

## Theorem 7.1 — Combined-radius stability certificate

Let

\[
\mathcal R_{\min}
=
\min\{\mathcal R_F,\mathcal R_{\mathrm{row}}\}.
\]

Assume:

1. \(M(\Gamma,t)\) and \(M(\widetilde\Gamma,t)\) are Hermitian;
2. \(g_0(M(\Gamma,t))>0\);
3. the local Lipschitz bound holds;
4. support displacements are correctly represented by \(d_j\).

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

## Proof

Both \(\mathcal R_F\) and \(\mathcal R_{\mathrm{row}}\) are valid upper bounds for \(\|E\|_2\). Therefore

\[
\|E\|_2\leq\mathcal R_{\min}.
\]

If

\[
\mathcal R_{\min}<g_0(M(\Gamma,t)),
\]

then

\[
\|E\|_2<g_0(M(\Gamma,t)).
\]

The spectral-gap principle gives

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

\[
\square
\]

---

# 8. Certified algorithm

## Algorithm 8.1 — Combined-Radius Stability Certification

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

Compute:

\[
\mathcal R_F,
\quad
\mathcal R_{\mathrm{row}},
\quad
\mathcal R_{\min}.
\]

If

\[
\mathcal R_{\min}<g_0(M),
\]

return:

CERTIFIED_STABLE

Otherwise return:

NOT_CERTIFIED

---

# 9. Algorithm correctness

## Theorem 9.1 — Soundness of Algorithm 8.1

If Algorithm 8.1 returns CERTIFIED_STABLE, then

\[
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
\]

## Proof

Algorithm 8.1 returns CERTIFIED_STABLE exactly when

\[
\mathcal R_{\min}<g_0(M).
\]

By Theorem 7.1, that condition certifies negative eigenvalue count stability.

\[
\square
\]

## Proposition 9.2 — Meaning of NOT_CERTIFIED

If Algorithm 8.1 returns NOT_CERTIFIED, no instability claim is made.

NOT_CERTIFIED means only that the current certificate did not prove stability.

---

# 10. Strict improvement over earlier certificates

The project began with the crude sufficient condition

\[
2Nm_{\max}L_t(U)\delta<g_0(M).
\]

The current combined-radius certificate can be strictly sharper because it uses:

1. actual multiplicities;
2. actual displacements;
3. Frobenius structure;
4. row-sum structure;
5. the smaller of two valid spectral-norm upper bounds.

This makes the framework more useful as a finite computational audit tool.

---

# 11. Current honest status

This is the strongest draft so far.

It contains:

1. a weighted support-stability theorem;
2. a matrix-specific row-sum theorem;
3. a combined-radius theorem;
4. strict-improvement examples;
5. a certified algorithm;
6. correctness proofs;
7. honest boundaries.

It is a serious finite-dimensional research-note candidate.

It is not yet a breakthrough.

Novelty is not established.

---

# 12. Limitations

This note does not address:

1. the infinite-dimensional zeta case;
2. convergence from finite models to the Weil criterion;
3. actual zeta zeros;
4. RH truth or falsity;
5. prior-art comparison against all matrix perturbation literature;
6. expert validation.

---

# Boundary

This note does not prove RH.

This note does not falsify RH.

This note does not use zeta zeros.

This note does not verify the zeta case.

This note does not claim novelty.

Exact audit strings:

RESEARCH_NOTE_V4

COMBINED_RADIUS_CERTIFIED_ALGORITHM

COMBINED_MINIMUM_RADIUS_CERTIFICATE

ROW_SUM_CERTIFICATE

CERTIFIED_STABLE

NOT_CERTIFIED

