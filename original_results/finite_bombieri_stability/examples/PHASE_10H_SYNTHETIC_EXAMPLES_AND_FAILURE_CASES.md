# Phase 10H — Synthetic Examples and Failure Cases

## Purpose

Phase 10G proved the finite Bombieri-style perturbation stability theorem.

Phase 10H creates examples showing:

1. when the theorem applies;
2. when the theorem does not certify stability;
3. when the negative eigenvalue count can actually change;
4. why the spectral-gap condition is necessary.

---

# Example type 1 — Certified stable case

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
N\varepsilon=0.2<2=g_0(M).
\]

Therefore Theorem 10G certifies

\[
n_-(M+E)=n_-(M)
\]

for every Hermitian perturbation satisfying

\[
|E_{jk}|\leq0.1.
\]

---

# Example type 2 — Certificate fails but count happens to stay stable

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

The theorem does not certify stability.

However, a particular small perturbation may still leave the count unchanged.

This shows the theorem gives a sufficient condition, not a necessary condition.

---

# Example type 3 — Certificate fails and count flips

Using the same near-zero matrix, a perturbation can push the eigenvalue

\[
-0.05
\]

across zero.

Then

\[
n_-(M+E)\neq n_-(M).
\]

This shows why the gap condition is mathematically necessary for a uniform guarantee.

---

# Example type 4 — Non-diagonal Hermitian case

The theorem also applies to non-diagonal Hermitian matrices.

For example,

\[
M=\begin{pmatrix}-2&0.2\\0.2&3\end{pmatrix}
\]

has one negative and one positive eigenvalue with a substantial gap around zero.

Small Hermitian entrywise perturbations preserve the negative count when the certificate

\[
N\varepsilon<g_0(M)
\]

holds.

---

# Interpretation

The examples show that the theorem is a stability certificate.

It does not predict the negative count from the finite configuration.

It certifies when the negative count cannot change under bounded perturbation.

---

# Boundary

These are synthetic finite examples.

This phase does not prove RH.

This phase does not falsify RH.

This phase does not use zeta zeros.

This phase does not claim novelty.

