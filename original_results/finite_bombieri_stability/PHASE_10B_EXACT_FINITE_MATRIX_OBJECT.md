# Phase 10B — Exact Finite Matrix Object

## Purpose

Phase 10A launched the original-result branch.

Phase 10B defines the exact finite matrix object for the stability theorem.

The object is not the full zeta-function Weil form.

The object is a finite synthetic Hermitian matrix model inspired by the Bombieri/Weil finite \(H\)-matrix framework.

---

# 1. Object name

We define the working object:

\[
\mathcal M(\Gamma,t)
\]

called the finite normalized Bombieri-style matrix.

---

# 2. Input data

The input consists of:

1. a finite multiset \(\Gamma=\{\gamma_1,\ldots,\gamma_n\}\subset\mathbb C\);
2. a positive scale parameter \(t>0\);
3. a kernel function

\[
H_t:\mathbb C\times\mathbb C\to\mathbb C;
\]

4. a multiplicity function

\[
m:\Gamma_{\mathrm{dist}}\to\mathbb N.
\]

---

# 3. Distinct support

Let

\[
\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}
\]

be the distinct support of \(\Gamma\).

For each \(\alpha_j\), define

\[
m_j=m(\alpha_j).
\]

---

# 4. Raw finite kernel matrix

The raw distinct kernel matrix is

\[
A_{jk}(t)=H_t(\alpha_j,\alpha_k).
\]

This matrix is not automatically treated as the final object because the Bombieri finite system may include multiplicity weights and inner-product conventions.

---

# 5. Weighted operator matrix

The column-weighted matrix is

\[
B_{jk}(t)=H_t(\alpha_j,\alpha_k)m_k.
\]

This is the natural matrix of a weighted finite operator in unnormalized coordinates.

However, it may not be Hermitian under the ordinary Euclidean inner product.

---

# 6. Similarity-normalized matrix

Define the diagonal multiplicity matrix

\[
D=\operatorname{diag}(m_1,\ldots,m_N).
\]

The similarity-normalized candidate is

\[
\mathcal M(\Gamma,t)
=
D^{1/2}A(t)D^{1/2}.
\]

Equivalently,

\[
\mathcal M_{jk}(\Gamma,t)
=
\sqrt{m_j}\,H_t(\alpha_j,\alpha_k)\sqrt{m_k}.
\]

This is the primary finite matrix object for the original-result branch.

---

# 7. Hermitian condition

The object is admitted into the stability theorem only if

\[
\mathcal M(\Gamma,t)=\mathcal M(\Gamma,t)^*.
\]

Equivalently,

\[
\mathcal M_{jk}=\overline{\mathcal M_{kj}}.
\]

Since \(m_j,m_k\) are positive real integers, this reduces to the kernel symmetry condition

\[
H_t(\alpha_j,\alpha_k)=\overline{H_t(\alpha_k,\alpha_j)}.
\]

The theorem branch will assume this Hermitian condition explicitly.

---

# 8. Why this object is chosen

The raw weighted matrix \(B=A D\) represents the finite weighted operator.

The normalized matrix

\[
D^{1/2}AD^{1/2}
\]

is similar to \(AD\) when \(D\) is positive definite:

\[
AD
=
D^{-1/2}
\left(D^{1/2}AD^{1/2}\right)
D^{1/2}.
\]

Therefore, \(AD\) and \(D^{1/2}AD^{1/2}\) have the same eigenvalues.

The normalized matrix has the advantage of living in the ordinary Euclidean Hermitian matrix setting.

---

# 9. Admitted matrix class

Define the class

\[
\mathfrak B_N
\]

to consist of all matrices of the form

\[
\mathcal M(\Gamma,t)=D^{1/2}A(t)D^{1/2}
\]

such that:

1. \(\Gamma\) is finite;
2. all multiplicities are positive integers;
3. \(t>0\);
4. \(H_t\) is defined on \(\Gamma_{\mathrm{dist}}\times\Gamma_{\mathrm{dist}}\);
5. \(\mathcal M(\Gamma,t)\) is Hermitian.

---

# 10. Stability theorem target

The original theorem will not depend on the full analytic structure of \(H_t\).

It will prove a finite-dimensional stability fact for matrices in \(\mathfrak B_N\):

If

\[
\widetilde{\mathcal M}
=
\mathcal M+E
\]

with \(E=E^*\) and \(\|E\|_2\) sufficiently small relative to the spectral gap around zero, then

\[
n_-(\widetilde{\mathcal M})=n_-(\mathcal M),
\]

where \(n_-(M)\) is the number of strictly negative eigenvalues of \(M\).

---

# 11. Boundary

This object is finite and synthetic.

This does not prove RH.

This does not falsify RH.

This does not use zeta zeros.

This does not claim novelty yet.

