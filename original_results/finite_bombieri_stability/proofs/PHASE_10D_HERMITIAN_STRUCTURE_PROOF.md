# Phase 10D — Hermitian Structure Proof

## Purpose

Phase 10B locked the finite matrix object

\[
\mathcal M(\Gamma,t)=D^{1/2}A(t)D^{1/2},
\]

where

\[
A_{jk}(t)=H_t(\alpha_j,\alpha_k),
\]

and \(D=\operatorname{diag}(m_1,\ldots,m_N)\).

Phase 10D proves the basic Hermitian/self-adjoint structure lemma for this object.

---

# Lemma 10D.1 — Hermitian Structure of the Normalized Finite Matrix

Let

\[
\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}
\]

be a finite distinct support with positive integer multiplicities

\[
m_1,\ldots,m_N.
\]

Let

\[
D=\operatorname{diag}(m_1,\ldots,m_N)
\]

and let

\[
A(t)_{jk}=H_t(\alpha_j,\alpha_k).
\]

Define

\[
\mathcal M(\Gamma,t)=D^{1/2}A(t)D^{1/2}.
\]

Then

\[
\mathcal M(\Gamma,t)
\]

is Hermitian if and only if

\[
H_t(\alpha_j,\alpha_k)
=
\overline{H_t(\alpha_k,\alpha_j)}
\]

for all

\[
1\leq j,k\leq N.
\]

---

# Proof

The entries of the normalized matrix are

\[
\mathcal M_{jk}
=
\sqrt{m_j}\,H_t(\alpha_j,\alpha_k)\sqrt{m_k}.
\]

The conjugate transpose condition for Hermitian matrices is

\[
\mathcal M_{jk}
=
\overline{\mathcal M_{kj}}.
\]

Now

\[
\mathcal M_{kj}
=
\sqrt{m_k}\,H_t(\alpha_k,\alpha_j)\sqrt{m_j}.
\]

Taking complex conjugates gives

\[
\overline{\mathcal M_{kj}}
=
\sqrt{m_k}\,\overline{H_t(\alpha_k,\alpha_j)}\sqrt{m_j},
\]

because \(m_j,m_k\) are positive real integers.

Since real scalar multiplication commutes,

\[
\overline{\mathcal M_{kj}}
=
\sqrt{m_j}\,\overline{H_t(\alpha_k,\alpha_j)}\sqrt{m_k}.
\]

Therefore,

\[
\mathcal M_{jk}
=
\overline{\mathcal M_{kj}}
\]

if and only if

\[
\sqrt{m_j}\,H_t(\alpha_j,\alpha_k)\sqrt{m_k}
=
\sqrt{m_j}\,\overline{H_t(\alpha_k,\alpha_j)}\sqrt{m_k}.
\]

Because

\[
\sqrt{m_j}\sqrt{m_k}>0,
\]

we may divide by this positive scalar and obtain

\[
H_t(\alpha_j,\alpha_k)
=
\overline{H_t(\alpha_k,\alpha_j)}.
\]

This proves the equivalence.

\[
\square
\]

---

# Corollary 10D.2 — Self-adjoint finite operator representative

If the kernel satisfies

\[
H_t(\alpha_j,\alpha_k)
=
\overline{H_t(\alpha_k,\alpha_j)}
\]

on the finite support, then

\[
\mathcal M(\Gamma,t)
\]

is self-adjoint as an operator on

\[
\mathbb C^N
\]

with the ordinary Euclidean inner product.

---

# Proof

A finite complex matrix is self-adjoint on

\[
\mathbb C^N
\]

with the ordinary Euclidean inner product if and only if it is Hermitian.

By Lemma 10D.1, the kernel symmetry condition implies that

\[
\mathcal M=\mathcal M^*.
\]

Therefore \(\mathcal M\) is self-adjoint.

\[
\square
\]

---

# Why this matters

The later perturbation theorem will count negative eigenvalues.

Negative eigenvalue counting is stable and meaningful only for Hermitian/self-adjoint matrices.

Therefore the theorem branch must explicitly assume or verify the finite kernel symmetry condition before applying spectral perturbation theory.

---

# Boundary

This is a finite-dimensional linear algebra lemma.

This phase does not prove RH.

This phase does not falsify RH.

This phase does not use zeta zeros.

This phase does not claim novelty.

