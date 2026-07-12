# Phase 12T — Hermitian Convention Audit

## Purpose

Phase 12S defined arithmetic matrix entries

\[
M_{ij}^{arith}=T[\phi_j*\phi_i^*].
\]

Before eigenvalue certificates can be trusted, we need the matrix to be Hermitian:

\[
M_{ij}^{arith}=\overline{M_{ji}^{arith}}.
\]

Phase 12T audits this convention.

---

# 1. Matrix entry convention

Use the coefficient-compatible convention:

\[
M_{ij}^{arith}=T[\phi_j*\phi_i^*].
\]

For

\[
g=\sum_j a_j\phi_j,
\]

Phase 12S showed formally:

\[
T[g*g^*]=a^*M^{arith}a.
\]

---

# 2. Required functional symmetry

The Hermitian proof requires the arithmetic functional to satisfy:

\[
T[F^*]=\overline{T[F]}.
\]

This is the key star-adjoint compatibility condition.

If this condition holds, then the arithmetic matrix is Hermitian.

If this condition is not confirmed from the source conventions, Hermitian status remains conditional.

---

# 3. Star of a convolution entry

Let

\[
F_{ij}=\phi_j*\phi_i^*.
\]

Then formally,

\[
F_{ij}^*=(\phi_j*\phi_i^*)^*.
\]

For multiplicative convolution with the chosen star operation, the expected identity is:

\[
(a*b)^*=b^**a^*.
\]

Since

\[
(\phi_i^*)^*=\phi_i,
\]

this gives:

\[
F_{ij}^*
=
\phi_i*\phi_j^*
=
F_{ji}.
\]

Thus:

\[
F_{ji}=F_{ij}^*.
\]

---

# Theorem 12T.1 — Star reverses convolution order

Assume the star operation satisfies

\[
(a*b)^*=b^**a^*
\]

and

\[
(f^*)^*=f.
\]

For

\[
F_{ij}=\phi_j*\phi_i^*,
\]

we have

\[
F_{ji}=F_{ij}^*.
\]

## Proof

Starting from

\[
F_{ij}=\phi_j*\phi_i^*,
\]

apply star:

\[
F_{ij}^*
=
(\phi_j*\phi_i^*)^*.
\]

Using the convolution-star identity,

\[
(\phi_j*\phi_i^*)^*
=
(\phi_i^*)^**\phi_j^*.
\]

Since

\[
(\phi_i^*)^*=\phi_i,
\]

we get

\[
F_{ij}^*=\phi_i*\phi_j^*.
\]

But by definition,

\[
F_{ji}=\phi_i*\phi_j^*.
\]

Therefore,

\[
F_{ji}=F_{ij}^*.
\]

\[
\square
\]

---

# Theorem 12T.2 — Conditional Hermitian arithmetic matrix

Assume:

1. \(M_{ij}^{arith}=T[\phi_j*\phi_i^*]\);
2. \(T[F^*]=\overline{T[F]}\);
3. \((a*b)^*=b^**a^*\);
4. \((f^*)^*=f\).

Then

\[
M_{ij}^{arith}=\overline{M_{ji}^{arith}}.
\]

## Proof

By definition,

\[
M_{ij}^{arith}=T[\phi_j*\phi_i^*].
\]

Also,

\[
M_{ji}^{arith}=T[\phi_i*\phi_j^*].
\]

By Theorem 12T.1,

\[
\phi_i*\phi_j^*=(\phi_j*\phi_i^*)^*.
\]

Therefore,

\[
M_{ji}^{arith}
=
T[(\phi_j*\phi_i^*)^*].
\]

Using the assumed functional symmetry,

\[
T[F^*]=\overline{T[F]},
\]

we get

\[
M_{ji}^{arith}
=
\overline{T[\phi_j*\phi_i^*]}
=
\overline{M_{ij}^{arith}}.
\]

Taking conjugates,

\[
M_{ij}^{arith}=\overline{M_{ji}^{arith}}.
\]

\[
\square
\]

---

# 4. Hermitian status

The project has proved:

\[
\boxed{
\text{If the star-adjoint identities hold, then }M^{arith}\text{ is Hermitian.}
}
\]

But the project has not yet fully validated from primary source that:

\[
T[F^*]=\overline{T[F]}
\]

holds for the extracted arithmetic functional with the exact chosen conventions.

Therefore the matrix Hermitian status is:

\[
\boxed{
\text{CONDITIONAL\_HERMITIAN\_PROVED}
}
\]

not:

\[
\boxed{
\text{UNCONDITIONAL\_HERMITIAN\_PROVED}
}
\]

---

# 5. Why this matters

Eigenvalue certificates require a Hermitian matrix.

If \(M^{arith}\) is Hermitian, then:

1. eigenvalues are real;
2. Rayleigh quotients are real;
3. negative-direction certificates are meaningful;
4. interval eigenvalue certification becomes possible.

Without Hermitian validation, a negative eigenvalue claim would be unsafe.

---

# 6. What remains

Still needed:

1. source validation of \(T[F^*]=\overline{T[F]}\);
2. direct symbolic audit of the extracted \(T\)-functional under star;
3. implementation of arithmetic matrix entries;
4. interval certification of matrix entries;
5. certified Hermitian symmetrization if needed.

---

# 7. Safe fallback

If exact Hermitian validation is not source-confirmed, define the Hermitian part:

\[
M_H=\frac12(M+M^*).
\]

But this changes the object unless one proves

\[
a^*M_Ha=a^*Ma
\]

for the relevant quadratic form.

So Hermitian symmetrization is only a fallback after careful audit.

---

# 8. Next target

Phase 12U should implement a symbolic star-functional audit for the extracted \(T\)-formula:

\[
T[F^*]\stackrel{?}{=}\overline{T[F]}.
\]

This is the next gate.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove a complete arithmetic-only finite certificate.

This phase does not establish novelty.

Exact audit strings:

HERMITIAN_CONVENTION_AUDIT_COMPLETE

COEFFICIENT_COMPATIBLE_MATRIX_CONVENTION_LOCKED

STAR_REVERSES_CONVOLUTION_ORDER_PROVED

CONDITIONAL_HERMITIAN_MATRIX_PROVED

T_STAR_ADJOINT_SYMMETRY_REQUIRED

UNCONDITIONAL_HERMITIAN_NOT_YET_PROVED

EIGENVALUE_CERTIFICATION_NOW_HAS_CONDITIONAL_GATE

SOURCE_VALIDATION_STILL_REQUIRED

ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE

