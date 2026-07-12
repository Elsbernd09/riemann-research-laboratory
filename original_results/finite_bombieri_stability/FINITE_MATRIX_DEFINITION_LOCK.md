# Finite Matrix Definition Lock

## Locked primary object

\[
\mathcal M(\Gamma,t)=D^{1/2}A(t)D^{1/2}
\]

where

\[
A_{jk}(t)=H_t(\alpha_j,\alpha_k)
\]

and

\[
D=\operatorname{diag}(m_1,\ldots,m_N).
\]

---

# Hermitian admission rule

The matrix is admitted into the theorem only if

\[
\mathcal M=\mathcal M^*.
\]

This is not optional.

If the numerical implementation produces a non-Hermitian matrix, the theorem does not apply.

---

# Negative eigenvalue count

Define

\[
n_-(M)=\#\{j:\lambda_j(M)<0\}.
\]

This count is only defined for the theorem when \(M\) is Hermitian.

---

# Multiplicity rule

Repeated \(\gamma\)-values are absorbed into the multiplicities \(m_j\).

The theorem is stated on the distinct support with multiplicity weights.

---

# Similarity note

The column-weighted operator \(AD\) and the normalized matrix

\[
D^{1/2}AD^{1/2}
\]

are similar when \(D\) is positive definite.

Therefore they have the same eigenvalues.

The normalized matrix is preferred because it is the ordinary Hermitian representative.

