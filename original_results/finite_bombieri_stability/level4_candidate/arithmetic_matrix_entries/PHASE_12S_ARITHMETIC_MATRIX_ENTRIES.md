# Phase 12S — Arithmetic Matrix Entries

## Purpose

Phase 12Q proved the prime sums are finite on the compactly supported finite test class.

Phase 12R reduced the archimedean integral to a finite interval plus an explicit analytic tail.

Phase 12S defines the arithmetic matrix entries

\[
M_{ij}^{arith}=T[\phi_i*\phi_j^*].
\]

This is the finite matrix object needed for an arithmetic-side certificate.

---

# 1. Basis functions

Let

\[
\phi_j(x)=\psi_j(\log x),
\qquad
\psi_j\in C_c^\infty(\mathbb R),
\]

with common support

\[
\operatorname{supp}(\phi_j)\subset[e^{-B},e^B].
\]

Let

\[
M=e^{2B}.
\]

---

# 2. Pairwise convolution profile

For basis indices \(i,j\), define

\[
F_{ij}=\phi_i*\phi_j^*.
\]

The star is

\[
\phi_j^*(x)=x^{-1}\overline{\phi_j(1/x)}.
\]

The convolution is

\[
F_{ij}(x)=\int_0^\infty \phi_i(y)\phi_j^*(x/y)\frac{dy}{y}.
\]

By Phase 12Q,

\[
\operatorname{supp}(F_{ij})\subset[e^{-2B},e^{2B}]=[M^{-1},M].
\]

Likewise,

\[
\operatorname{supp}(F_{ij}^*)\subset[M^{-1},M].
\]

---

# 3. Arithmetic matrix entry definition

Define

\[
M_{ij}^{arith}=T[F_{ij}],
\]

where the extracted arithmetic functional is

\[
T[F]
=
\int_0^\infty F(x)\,dx
+
\int_0^\infty F^*(x)\,dx
-
\sum_{n=1}^{\infty}\Lambda(n)\{F(n)+F^*(n)\}
-
(\log 4\pi+\gamma_E)F(1)
-
\int_1^\infty
\left(
F(x)+F^*(x)-\frac{2F(1)}{x}
\right)
\frac{x\,dx}{x^2-1}.
\]

Since \(F_{ij}\) and \(F_{ij}^*\) are compactly supported, the prime sum is finite and the archimedean integral is reducible.

---

# 4. Finite arithmetic expansion

For \(F_{ij}\), define:

\[
I_0(F_{ij})=\int_0^\infty F_{ij}(x)\,dx,
\]

\[
I_0(F_{ij}^*)=\int_0^\infty F_{ij}^*(x)\,dx,
\]

\[
P(F_{ij})=\sum_{1\le n\le M}\Lambda(n)\{F_{ij}(n)+F_{ij}^*(n)\},
\]

\[
C(F_{ij})=(\log 4\pi+\gamma_E)F_{ij}(1),
\]

and

\[
A(F_{ij})
=
\int_1^M
\left(
F_{ij}(x)+F_{ij}^*(x)-\frac{2F_{ij}(1)}{x}
\right)
\frac{x\,dx}{x^2-1}
-
F_{ij}(1)\log\left(\frac{M+1}{M-1}\right).
\]

Then

\[
M_{ij}^{arith}
=
I_0(F_{ij})
+
I_0(F_{ij}^*)
-
P(F_{ij})
-
C(F_{ij})
-
A(F_{ij}).
\]

---

# Theorem 12S.1 — Arithmetic matrix entry finite expansion

For every basis pair \(i,j\),

\[
M_{ij}^{arith}
=
I_0(F_{ij})
+
I_0(F_{ij}^*)
-
P(F_{ij})
-
C(F_{ij})
-
A(F_{ij}),
\]

where \(P(F_{ij})\) is a finite sum over

\[
1\le n\le M=e^{2B}
\]

and \(A(F_{ij})\) is a finite interval integral over

\[
[1,M]
\]

plus an explicit logarithmic tail.

## Proof

Start with the extracted formula for \(T[F_{ij}]\).

By Phase 12Q, the prime sum has no terms beyond \(M=e^{2B}\). Therefore the infinite prime sum becomes the finite sum \(P(F_{ij})\).

By Phase 12R, the archimedean integral over \([1,\infty)\) equals the reduced finite interval expression plus the explicit logarithmic tail.

Substituting these two reductions into \(T[F_{ij}]\) gives the stated expansion.

\[
\square
\]

---

# 5. Matrix quadratic form

For a coefficient vector

\[
a=(a_1,\dots,a_m)\in\mathbb C^m,
\]

define

\[
g=\sum_{j=1}^{m}a_j\phi_j.
\]

The arithmetic matrix form is

\[
Q_m^{arith}(g)=a^*M^{arith}a.
\]

Under bilinearity/sesquilinearity of the convolution-star construction and the linearity of \(T\), this equals

\[
T[g*g^*]
\]

provided the matrix entry convention is aligned correctly.

Because complex conjugation conventions matter, the exact \(a^*M a\) indexing must be audited in the next phase.

---

# Theorem 12S.2 — Formal arithmetic matrix representation

Assume the entry convention is chosen so that

\[
F_{ij}=\phi_j*\phi_i^*
\]

matches the coefficient expansion of

\[
g*g^*
\]

for

\[
g=\sum_j a_j\phi_j.
\]

Then

\[
T[g*g^*]=a^*M^{arith}a.
\]

## Proof

Expand

\[
g*g^*
=
\left(\sum_j a_j\phi_j\right)
*
\left(\sum_i a_i\phi_i\right)^*.
\]

Using conjugate-linearity of star,

\[
g^*=\sum_i \overline{a_i}\phi_i^*.
\]

Thus

\[
g*g^*
=
\sum_{j,i}a_j\overline{a_i}(\phi_j*\phi_i^*).
\]

Applying linearity of \(T\),

\[
T[g*g^*]
=
\sum_{i,j}\overline{a_i}a_jT[\phi_j*\phi_i^*].
\]

With

\[
M_{ij}^{arith}=T[\phi_j*\phi_i^*],
\]

we get

\[
T[g*g^*]=a^*M^{arith}a.
\]

\[
\square
\]

---

# 6. Certification targets

To turn \(M^{arith}\) into a certified matrix, we need interval bounds for:

1. \(I_0(F_{ij})\);
2. \(I_0(F_{ij}^*)\);
3. finite prime values \(F_{ij}(n),F_{ij}^*(n)\);
4. \(F_{ij}(1)\);
5. archimedean finite interval integral;
6. removable singularity near \(x=1\);
7. logarithmic tail term.

---

# 7. What this achieves

Phase 12S defines the arithmetic finite matrix entries and proves their finite expansion.

This is a major step toward an arithmetic-only finite certificate.

---

# 8. What remains

Still needed:

1. convention audit for \(M_{ij}\) indexing;
2. Hermitian symmetry proof;
3. interval arithmetic implementation;
4. certified quadrature;
5. source validation;
6. numerical examples.

---

# 9. Next target

Phase 12T should prove the Hermitian/indexing convention:

\[
M_{ij}^{arith}=\overline{M_{ji}^{arith}}
\]

under the correct entry definition.

This is necessary before eigenvalue certificates can be trusted.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove a complete arithmetic-only finite certificate.

This phase does not establish novelty.

Exact audit strings:

ARITHMETIC_MATRIX_ENTRIES_COMPLETE

M_IJ_ARITH_DEFINED

FINITE_ARITHMETIC_EXPANSION_PROVED

FINITE_PRIME_SUM_IN_MATRIX_ENTRY_PROVED

REDUCED_ARCHIMEDEAN_TERM_IN_MATRIX_ENTRY_PROVED

FORMAL_MATRIX_REPRESENTATION_PROVED

HERMITIAN_CONVENTION_AUDIT_STILL_REQUIRED

CERTIFIED_INTERVAL_IMPLEMENTATION_STILL_REQUIRED

ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE

