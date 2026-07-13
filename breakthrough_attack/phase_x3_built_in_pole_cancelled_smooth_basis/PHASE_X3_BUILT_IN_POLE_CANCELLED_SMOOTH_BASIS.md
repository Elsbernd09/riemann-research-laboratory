# Phase X3 — Built-In Pole-Cancelled Smooth Basis

## Purpose

Phase X2 locked the exact Bombieri–Lagarias functional:

\[
T_{BL}[f].
\]

Phase X3 builds smooth compactly supported basis functions \(\phi_j\) satisfying:

\[
\widehat{\phi_j}(0)=0,
\qquad
\widehat{\phi_j}(1)=0.
\]

This gives built-in stronger pole cancellation on \(g\), which implies the locked \(f\)-pole cancellation target for:

\[
f=g*g^*.
\]

---

# 1. Raw smooth bumps

Start with smooth log-bumps:

\[
b_j(x)=\psi\left(\frac{\log x-c_j}{w_j}\right),
\]

where

\[
\psi(u)=
\begin{cases}
\exp(-1/(1-u^2)), & |u|<1,\\
0, & |u|\ge1.
\end{cases}
\]

Each \(b_j\in C_c^\infty(0,\infty)\).

---

# 2. Correction functions

Choose two correction bumps:

\[
u_0,u_1\in C_c^\infty(0,\infty)
\]

such that the \(2\times2\) Mellin moment matrix

\[
A=
\begin{pmatrix}
\widehat{u_0}(0) & \widehat{u_1}(0)\\
\widehat{u_0}(1) & \widehat{u_1}(1)
\end{pmatrix}
\]

is invertible.

---

# 3. Corrected basis

For each raw bump \(b_j\), define:

\[
\phi_j=b_j-\alpha_j u_0-\beta_j u_1.
\]

Choose \(\alpha_j,\beta_j\) by solving:

\[
A
\begin{pmatrix}
\alpha_j\\
\beta_j
\end{pmatrix}
=
\begin{pmatrix}
\widehat{b_j}(0)\\
\widehat{b_j}(1)
\end{pmatrix}.
\]

Then:

\[
\widehat{\phi_j}(0)=0,
\qquad
\widehat{\phi_j}(1)=0.
\]

---

# Theorem X3.1 — correction preserves smooth compact support

If \(b_j,u_0,u_1\in C_c^\infty(0,\infty)\), then:

\[
\phi_j=b_j-\alpha_j u_0-\beta_j u_1
\]

also belongs to:

\[
C_c^\infty(0,\infty).
\]

## Proof

The space \(C_c^\infty(0,\infty)\) is closed under finite linear combinations.

Therefore \(\phi_j\in C_c^\infty(0,\infty)\).

\[
\square
\]

---

# Theorem X3.2 — built-in pole cancellation

Assume \(A\) is invertible and \(\alpha_j,\beta_j\) are chosen by:

\[
A
\begin{pmatrix}
\alpha_j\\
\beta_j
\end{pmatrix}
=
\begin{pmatrix}
\widehat{b_j}(0)\\
\widehat{b_j}(1)
\end{pmatrix}.
\]

Then:

\[
\widehat{\phi_j}(0)=0,
\qquad
\widehat{\phi_j}(1)=0.
\]

## Proof

By linearity of the Mellin transform:

\[
\widehat{\phi_j}(s)
=
\widehat{b_j}(s)
-
\alpha_j\widehat{u_0}(s)
-
\beta_j\widehat{u_1}(s).
\]

At \(s=0\), the first row of the linear system gives:

\[
\widehat{b_j}(0)
-
\alpha_j\widehat{u_0}(0)
-
\beta_j\widehat{u_1}(0)
=
0.
\]

At \(s=1\), the second row gives:

\[
\widehat{b_j}(1)
-
\alpha_j\widehat{u_0}(1)
-
\beta_j\widehat{u_1}(1)
=
0.
\]

Therefore:

\[
\widehat{\phi_j}(0)=\widehat{\phi_j}(1)=0.
\]

\[
\square
\]

---

# Theorem X3.3 — finite combinations remain pole-cancelled

If every \(\phi_j\) satisfies:

\[
\widehat{\phi_j}(0)=0,
\qquad
\widehat{\phi_j}(1)=0,
\]

then every finite combination:

\[
g_a=\sum_j a_j\phi_j
\]

satisfies:

\[
\widehat{g_a}(0)=0,
\qquad
\widehat{g_a}(1)=0.
\]

## Proof

By linearity:

\[
\widehat{g_a}(s)=\sum_j a_j\widehat{\phi_j}(s).
\]

At \(s=0\) and \(s=1\), every summand is zero.

Thus the sums are zero.

\[
\square
\]

---

# 4. Breakthrough relevance

This phase removes one major blocker.

Instead of projecting into a pole-admissible nullspace after the fact, the basis itself is built inside the stronger admissible subspace.

This is cleaner for certified finite arithmetic matrices.

However, this still does not compute a certified arithmetic entry.

---

# 5. Next phase

Phase X4 should prove support and finite-prime cutoff theorems for the corrected basis.

Because correction functions enlarge support, we need exact support bookkeeping:

\[
\operatorname{supp}(\phi_j)\subset S_j\cup S_{u_0}\cup S_{u_1}.
\]

Then for matrix entries:

\[
M_{ij}=T_{BL}[\phi_j*\phi_i^*],
\]

we need:

\[
\operatorname{supp}(\phi_j*\phi_i^*)\subset [A_{ij},B_{ij}],
\]

so the prime sum is finite.

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not compute a certified arithmetic entry.

It builds the pole-cancelled smooth basis mechanism needed for the certified matrix attack.

Exact audit strings:

PHASE_X3_BUILT_IN_POLE_CANCELLED_SMOOTH_BASIS_COMPLETE

RAW_SMOOTH_BUMPS_DEFINED

CORRECTION_BUMPS_DEFINED

MELLIN_MOMENT_CORRECTION_MATRIX_DEFINED

CORRECTED_BASIS_DEFINED

SMOOTH_COMPACT_SUPPORT_PRESERVED_PROVED

BUILT_IN_POLE_CANCELLATION_PROVED

FINITE_COMBINATIONS_POLE_CANCELLED_PROVED

POLE_CANCELLED_SMOOTH_BASIS_MECHANISM_CREATED

CERTIFIED_ENTRY_NOT_COMPUTED

READY_FOR_PHASE_X4_SUPPORT_AND_FINITE_PRIME_CUTOFF_THEOREM

