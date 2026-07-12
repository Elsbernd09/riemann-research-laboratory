# Phase 10F — Spectral-Gap Stability

## Purpose

Phase 10E proved that entrywise perturbation bounds imply operator-norm perturbation bounds.

Phase 10F proves the spectral-gap stability lemma.

This is the key bridge:

\[
\|E\|_2\text{ small}
\Longrightarrow
\text{negative eigenvalue count is unchanged}.
\]

---

# Definition — Negative eigenvalue count

For a Hermitian matrix \(M\in\mathbb C^{N\times N}\), define

\[
n_-(M)
=
\#\{j:\lambda_j(M)<0\},
\]

where

\[
\lambda_1(M)\leq \cdots \leq \lambda_N(M)
\]

are the real eigenvalues of \(M\), counted with multiplicity.

---

# Definition — Zero spectral gap

Define the zero-gap of \(M\) by

\[
g_0(M)
=
\min_{1\leq j\leq N}|\lambda_j(M)|.
\]

If \(0\) is an eigenvalue, then

\[
g_0(M)=0.
\]

---

# Lemma 10F.1 — Weyl-type eigenvalue perturbation bound

Let \(M,E\in\mathbb C^{N\times N}\) be Hermitian.

Then for each \(j\),

\[
|\lambda_j(M+E)-\lambda_j(M)|
\leq
\|E\|_2.
\]

This is the standard Hermitian eigenvalue perturbation bound.

---

# Lemma 10F.2 — Spectral-gap stability of sign

Let \(M,E\in\mathbb C^{N\times N}\) be Hermitian.

Assume

\[
\|E\|_2<g_0(M).
\]

Then no eigenvalue of \(M+E\) crosses zero relative to the ordered eigenvalues of \(M\).

In particular,

\[
n_-(M+E)=n_-(M).
\]

---

# Proof

Let

\[
\lambda_1(M)\leq\cdots\leq\lambda_N(M)
\]

be the eigenvalues of \(M\), and let

\[
\lambda_1(M+E)\leq\cdots\leq\lambda_N(M+E)
\]

be the eigenvalues of \(M+E\).

By Lemma 10F.1,

\[
|\lambda_j(M+E)-\lambda_j(M)|
\leq
\|E\|_2
\]

for each \(j\).

Since

\[
\|E\|_2<g_0(M),
\]

we have

\[
\|E\|_2<|\lambda_j(M)|
\]

for every \(j\).

If

\[
\lambda_j(M)>0,
\]

then

\[
\lambda_j(M+E)
\geq
\lambda_j(M)-\|E\|_2
>
0.
\]

If

\[
\lambda_j(M)<0,
\]

then

\[
\lambda_j(M+E)
\leq
\lambda_j(M)+\|E\|_2
<
0.
\]

Thus every ordered eigenvalue keeps its sign.

Therefore the number of negative eigenvalues is unchanged:

\[
n_-(M+E)=n_-(M).
\]

\[
\square
\]

---

# Corollary 10F.3 — Entrywise certified negative-count stability

Let \(M,E\in\mathbb C^{N\times N}\) be Hermitian.

Assume

\[
|E_{jk}|\leq \varepsilon
\]

for all \(j,k\).

If

\[
N\varepsilon<g_0(M),
\]

then

\[
n_-(M+E)=n_-(M).
\]

---

# Proof

By Phase 10E,

\[
\|E\|_2\leq N\varepsilon.
\]

If

\[
N\varepsilon<g_0(M),
\]

then

\[
\|E\|_2<g_0(M).
\]

Lemma 10F.2 applies, so

\[
n_-(M+E)=n_-(M).
\]

\[
\square
\]

---

# Interpretation

This is the central finite stability certificate.

If the finite matrix has no eigenvalues too close to zero, and the entrywise perturbation is small enough, then the negative eigenvalue count is stable.

In computational language:

\[
\boxed{
N\varepsilon<g_0(M)
\implies
\text{negative eigenvalue count is certified stable}.
}
\]

---

# Boundary

This is a finite-dimensional spectral perturbation lemma.

This phase does not prove RH.

This phase does not falsify RH.

This phase does not use zeta zeros.

This phase does not claim novelty.

