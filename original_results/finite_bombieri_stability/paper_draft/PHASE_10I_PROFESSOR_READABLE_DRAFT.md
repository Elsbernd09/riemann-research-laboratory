# A Finite Stability Certificate for Negative Eigenvalue Counts in Bombieri-Style Matrix Models

## Abstract

We study a finite-dimensional matrix model inspired by Bombieri/Weil-style positivity frameworks. Given a finite multiset \(\Gamma\), a finite kernel \(H_t\), and a multiplicity diagonal matrix \(D\), we consider normalized matrices of the form

\[
M=D^{1/2}AD^{1/2},
\qquad
A_{jk}=H_t(\alpha_j,\alpha_k).
\]

For Hermitian matrices in this class, we prove a simple but useful finite stability certificate: if a perturbed matrix \(\widetilde M\) differs entrywise from \(M\) by at most \(\varepsilon\), and

\[
N\varepsilon<g_0(M),
\]

where \(g_0(M)\) is the distance from the spectrum of \(M\) to zero, then the number of negative eigenvalues is unchanged:

\[
n_-(\widetilde M)=n_-(M).
\]

We also record a kernel-level sufficient condition involving multiplicity weights:

\[
Nm_{\max}\eta<g_0(M).
\]

The result is finite-dimensional and does not prove, falsify, or verify the Riemann Hypothesis. Its purpose is to isolate a stability requirement for finite RH-adjacent matrix computations: negative eigenvalue counts are meaningful only when protected by a certified spectral gap.

---

# 1. Introduction

Several criteria related to the Riemann Hypothesis can be phrased in terms of positivity, spectral behavior, or finite approximations of quadratic forms. In computational explorations of such frameworks, one often encounters finite matrices whose eigenvalue counts are interpreted as evidence about a finite model.

However, eigenvalue counts near zero are fragile. A small perturbation in the kernel, normalization, multiplicity convention, or implementation can change the number of negative eigenvalues if the matrix has eigenvalues close to zero.

This note isolates a finite-dimensional stability principle for Bombieri-style matrix models. The result does not address the zeta function directly. Instead, it gives a precise certificate for when a finite negative eigenvalue count is stable under controlled perturbation.

---

# 2. Finite matrix model

Let

\[
\Gamma
\]

be a finite multiset with distinct support

\[
\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}.
\]

Let

\[
m_j=m(\alpha_j)\in\mathbb N
\]

be the multiplicity of \(\alpha_j\), and define

\[
D=\operatorname{diag}(m_1,\ldots,m_N).
\]

Let

\[
H_t:\Gamma_{\mathrm{dist}}\times\Gamma_{\mathrm{dist}}\to\mathbb C
\]

be a finite kernel, and define

\[
A_{jk}=H_t(\alpha_j,\alpha_k).
\]

The normalized finite matrix is

\[
M=D^{1/2}AD^{1/2}.
\]

Equivalently,

\[
M_{jk}=\sqrt{m_j}H_t(\alpha_j,\alpha_k)\sqrt{m_k}.
\]

This matrix is admitted into the stability theorem only when it is Hermitian.

---

# 3. Hermitian admission condition

## Lemma 1

The normalized matrix

\[
M=D^{1/2}AD^{1/2}
\]

is Hermitian if and only if

\[
H_t(\alpha_j,\alpha_k)=\overline{H_t(\alpha_k,\alpha_j)}
\]

for all \(j,k\).

## Proof

The entries of \(M\) are

\[
M_{jk}=\sqrt{m_j}H_t(\alpha_j,\alpha_k)\sqrt{m_k}.
\]

The Hermitian condition is

\[
M_{jk}=\overline{M_{kj}}.
\]

Since the multiplicities are positive real integers,

\[
\overline{M_{kj}}
=
\sqrt{m_j}\overline{H_t(\alpha_k,\alpha_j)}\sqrt{m_k}.
\]

Thus

\[
M_{jk}=\overline{M_{kj}}
\]

if and only if

\[
H_t(\alpha_j,\alpha_k)=\overline{H_t(\alpha_k,\alpha_j)}.
\]

\[
\square
\]

---

# 4. Entrywise perturbation bound

## Lemma 2

Let

\[
E\in\mathbb C^{N\times N}
\]

satisfy

\[
|E_{jk}|\leq\varepsilon
\]

for all \(j,k\). Then

\[
\|E\|_2\leq N\varepsilon.
\]

## Proof

The Frobenius norm satisfies

\[
\|E\|_F
=
\left(\sum_{j,k}|E_{jk}|^2\right)^{1/2}
\leq
\left(N^2\varepsilon^2\right)^{1/2}
=
N\varepsilon.
\]

Since

\[
\|E\|_2\leq\|E\|_F,
\]

we obtain

\[
\|E\|_2\leq N\varepsilon.
\]

\[
\square
\]

---

# 5. Spectral-gap stability

For a Hermitian matrix \(M\), define

\[
n_-(M)=\#\{j:\lambda_j(M)<0\},
\]

where eigenvalues are counted with multiplicity.

Define the zero spectral gap by

\[
g_0(M)=\min_j|\lambda_j(M)|.
\]

## Lemma 3

Let \(M,E\in\mathbb C^{N\times N}\) be Hermitian. If

\[
\|E\|_2<g_0(M),
\]

then

\[
n_-(M+E)=n_-(M).
\]

## Proof

For Hermitian matrices, the standard eigenvalue perturbation bound gives

\[
|\lambda_j(M+E)-\lambda_j(M)|\leq\|E\|_2
\]

for each ordered eigenvalue.

If \(\lambda_j(M)>0\), then

\[
\lambda_j(M+E)
\geq
\lambda_j(M)-\|E\|_2
>
0.
\]

If \(\lambda_j(M)<0\), then

\[
\lambda_j(M+E)
\leq
\lambda_j(M)+\|E\|_2
<
0.
\]

Thus no eigenvalue crosses zero, and the number of negative eigenvalues is unchanged.

\[
\square
\]

---

# 6. Main theorem

## Theorem

Let

\[
M=D^{1/2}AD^{1/2},
\qquad
\widetilde M=D^{1/2}\widetilde A D^{1/2}
\]

be finite normalized matrices associated to kernels \(H_t\) and \(\widetilde H_t\) on the same finite support and with the same multiplicities.

Assume:

1. \(M\) and \(\widetilde M\) are Hermitian;
2. \(g_0(M)>0\);
3. \(|\widetilde M_{jk}-M_{jk}|\leq\varepsilon\) for all \(j,k\);
4. \(N\varepsilon<g_0(M)\).

Then

\[
n_-(\widetilde M)=n_-(M).
\]

## Proof

Let

\[
E=\widetilde M-M.
\]

Since both matrices are Hermitian, \(E\) is Hermitian.

By the entrywise assumption and Lemma 2,

\[
\|E\|_2\leq N\varepsilon.
\]

Since

\[
N\varepsilon<g_0(M),
\]

we have

\[
\|E\|_2<g_0(M).
\]

Lemma 3 implies

\[
n_-(M+E)=n_-(M).
\]

But

\[
M+E=\widetilde M.
\]

Therefore

\[
n_-(\widetilde M)=n_-(M).
\]

\[
\square
\]

---

# 7. Kernel-level certificate

Suppose the kernel-level perturbation obeys

\[
|\widetilde H_t(\alpha_j,\alpha_k)-H_t(\alpha_j,\alpha_k)|\leq\eta
\]

for all \(j,k\).

Then

\[
|\widetilde M_{jk}-M_{jk}|
=
\sqrt{m_jm_k}
|\widetilde H_t(\alpha_j,\alpha_k)-H_t(\alpha_j,\alpha_k)|.
\]

Let

\[
m_{\max}=\max_jm_j.
\]

Since

\[
\sqrt{m_jm_k}\leq m_{\max},
\]

we get

\[
|\widetilde M_{jk}-M_{jk}|
\leq
m_{\max}\eta.
\]

Thus the sufficient kernel-level certificate is

\[
Nm_{\max}\eta<g_0(M).
\]

When this holds,

\[
n_-(\widetilde M)=n_-(M).
\]

---

# 8. Synthetic examples

## Certified stable example

Let

\[
M=\begin{pmatrix}-2&0\\0&3\end{pmatrix}.
\]

Then

\[
g_0(M)=2.
\]

For \(N=2\) and \(\varepsilon=0.1\),

\[
N\varepsilon=0.2<2.
\]

Hence the negative eigenvalue count is certified stable for all Hermitian perturbations satisfying the entrywise bound.

## Certificate failure without count change

Let

\[
M=\begin{pmatrix}-0.05&0\\0&2\end{pmatrix}.
\]

Then

\[
g_0(M)=0.05.
\]

For \(N=2\) and \(\varepsilon=0.04\),

\[
N\varepsilon=0.08>0.05.
\]

The theorem does not apply. A particular perturbation may still leave the negative count unchanged, showing the condition is sufficient but not necessary.

## Certificate failure with count change

Using the same near-zero matrix, a perturbation can push the eigenvalue \(-0.05\) across zero. Then the negative eigenvalue count changes.

This shows why the gap condition is necessary for a uniform guarantee.

---

# 9. Relation to RH-adjacent finite computations

This theorem does not say anything directly about the Riemann Hypothesis.

Its relevance is methodological. In finite positivity or finite eigenvalue-count computations inspired by RH-adjacent criteria, numerical output is meaningful only if the eigenvalue count is stable under the relevant error model.

The theorem provides one explicit stability certificate:

\[
N\varepsilon<g_0(M)
\]

or, at the kernel level,

\[
Nm_{\max}\eta<g_0(M).
\]

If the certificate fails, a finite negative count may still be correct, but it is not certified by this theorem.

---

# 10. Limitations

This note does not address:

1. infinite-dimensional limiting forms;
2. zeta zeros;
3. Bombieri Sections 10 and 11;
4. RH itself;
5. whether the finite matrix model converges to any zeta-case object;
6. whether the theorem is novel beyond its packaging as a finite Bombieri-style stability certificate.

---

# 11. Conclusion

We proved a finite stability certificate for negative eigenvalue counts in normalized Bombieri-style matrix models. The theorem states that if a finite Hermitian matrix has a positive gap around zero, and the perturbation is small enough relative to that gap, then the negative eigenvalue count is stable.

The result is elementary finite-dimensional spectral perturbation theory, but it gives a clear audit rule for finite RH-adjacent matrix computations: eigenvalue-count claims should be accompanied by a spectral-gap certificate.

---

# Boundary statement

This draft does not prove RH.

This draft does not falsify RH.

This draft does not use zeta zeros.

This draft does not verify the zeta case.

This draft does not claim novelty.

