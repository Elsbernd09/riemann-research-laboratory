# Phase 10E — Entrywise Perturbation to Operator-Norm Bound

## Purpose

Phase 10D proved the Hermitian/self-adjoint structure lemma.

Phase 10E proves the next finite-dimensional perturbation lemma.

The goal is to convert a simple entrywise perturbation bound into an operator-norm bound.

This is needed because spectral perturbation theorems are naturally stated using operator norm.

---

# Lemma 10E.1 — Entrywise Bound Implies Frobenius Bound

Let

\[
E\in\mathbb C^{N\times N}.
\]

Assume that for every pair \(j,k\),

\[
|E_{jk}|\leq \varepsilon.
\]

Then

\[
\|E\|_F\leq N\varepsilon.
\]

---

# Proof

The Frobenius norm is

\[
\|E\|_F
=
\left(\sum_{j=1}^N\sum_{k=1}^N |E_{jk}|^2\right)^{1/2}.
\]

Using the entrywise bound,

\[
|E_{jk}|^2\leq \varepsilon^2
\]

for all \(j,k\). Therefore,

\[
\sum_{j=1}^N\sum_{k=1}^N |E_{jk}|^2
\leq
\sum_{j=1}^N\sum_{k=1}^N \varepsilon^2
=
N^2\varepsilon^2.
\]

Taking square roots gives

\[
\|E\|_F\leq N\varepsilon.
\]

\[
\square
\]

---

# Lemma 10E.2 — Entrywise Bound Implies Operator-Norm Bound

Let

\[
E\in\mathbb C^{N\times N}.
\]

Assume that for every pair \(j,k\),

\[
|E_{jk}|\leq \varepsilon.
\]

Then

\[
\|E\|_2\leq N\varepsilon.
\]

---

# Proof

For every matrix,

\[
\|E\|_2\leq \|E\|_F.
\]

By Lemma 10E.1,

\[
\|E\|_F\leq N\varepsilon.
\]

Therefore,

\[
\|E\|_2\leq N\varepsilon.
\]

\[
\square
\]

---

# Corollary 10E.3 — Finite Bombieri-Style Matrix Perturbation Bound

Let

\[
\mathcal M,\widetilde{\mathcal M}\in\mathbb C^{N\times N}
\]

be finite matrices of the locked type

\[
\mathcal M=D^{1/2}A D^{1/2},
\qquad
\widetilde{\mathcal M}=D^{1/2}\widetilde A D^{1/2}.
\]

Let

\[
E=\widetilde{\mathcal M}-\mathcal M.
\]

If

\[
|E_{jk}|\leq \varepsilon
\]

for all \(j,k\), then

\[
\|\widetilde{\mathcal M}-\mathcal M\|_2
=
\|E\|_2
\leq N\varepsilon.
\]

---

# Proof

This is exactly Lemma 10E.2 applied to

\[
E=\widetilde{\mathcal M}-\mathcal M.
\]

\[
\square
\]

---

# Interpretation

If implementation error, rounding error, kernel-evaluation error, or input perturbation produces at most

\[
\varepsilon
\]

entrywise error in the final normalized finite matrix, then the spectral perturbation size is at most

\[
N\varepsilon.
\]

This gives the computable quantity that the later eigenvalue-gap theorem will compare against the gap around zero.

---

# Boundary

This is a finite-dimensional linear algebra bound.

This phase does not prove RH.

This phase does not falsify RH.

This phase does not use zeta zeros.

This phase does not claim novelty.

