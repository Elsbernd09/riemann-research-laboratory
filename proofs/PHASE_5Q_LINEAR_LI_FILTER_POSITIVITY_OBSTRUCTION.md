# Phase 5Q — Linear Li-Filter Positivity Obstruction

## Status

PROVED IN PROJECT — STRUCTURAL OBSTRUCTION.

## Objective

Test whether a fixed linear combination of symmetric quartet Li contrasts can extract a universally nonnegative horizontal zero-defect quantity.

The answer is negative.

---

# 1. Li conformal coordinate

For a nontrivial zero coordinate

\[
\rho=\beta+i\gamma,
\]

define

\[
w(\rho)
=
1-\frac1\rho
=
\frac{\rho-1}{\rho}.
\]

Write

\[
w=re^{i\theta}
=
e^{u+i\theta},
\]

where

\[
u=\log r.
\]

We have

\[
|w|^2
=
\frac{(\beta-1)^2+\gamma^2}
{\beta^2+\gamma^2}.
\]

Therefore

\[
|w|^2-1
=
\frac{1-2\beta}
{\beta^2+\gamma^2}.
\]

Hence

\[
\boxed{
|w|=1
\iff
\beta=\frac12.
}
\]

Equivalently,

\[
\boxed{
u=0
\iff
\Re\rho=\frac12.
}
\]

Thus \(u\) is a horizontal-defect coordinate in the Li conformal variable.

---

# 2. Symmetric quartet in the Li coordinate

The zeta zero symmetries generate

\[
\rho,
\qquad
\bar\rho,
\qquad
1-\rho,
\qquad
1-\bar\rho.
\]

Under the map

\[
w(\rho)=1-\frac1\rho,
\]

the corresponding Li coordinates are

\[
w,
\qquad
\bar w,
\qquad
w^{-1},
\qquad
\bar w^{-1},
\]

up to permutation.

The zero-side Li kernel is

\[
1-w^n.
\]

Therefore the quartet contribution is

\[
L_n(u,\theta)
=
4-
\left(
w^n+\bar w^n+w^{-n}+\bar w^{-n}
\right).
\]

Since

\[
w=e^{u+i\theta},
\]

we have

\[
w^n+\bar w^n+w^{-n}+\bar w^{-n}
=
4\cos(n\theta)\cosh(nu).
\]

Thus

\[
\boxed{
L_n(u,\theta)
=
4-
4\cos(n\theta)\cosh(nu).
}
\]

---

# 3. Exact horizontal quartet contrast

The critical-line reference at the same angular coordinate has

\[
u=0.
\]

Hence

\[
L_n(0,\theta)
=
4-
4\cos(n\theta).
\]

Define

\[
\Delta_n(u,\theta)
=
L_n(u,\theta)
-
L_n(0,\theta).
\]

Then

\[
\boxed{
\Delta_n(u,\theta)
=
-4\cos(n\theta)
\left(
\cosh(nu)-1
\right).
}
\]

For small \(u\),

\[
\cosh(nu)-1
=
\frac{n^2u^2}{2}
+
O(n^4u^4).
\]

Therefore

\[
\boxed{
\Delta_n(u,\theta)
=
-2n^2u^2\cos(n\theta)
+
O(n^4u^4).
}
\]

The leading horizontal-defect amplitude is multiplied by the angular phase

\[
\cos(n\theta).
\]

---

# 4. Finite linear-filter obstruction

Let

\[
a_1,\ldots,a_N
\]

be fixed real coefficients.

Define

\[
\mathcal D_a(u,\theta)
=
\sum_{n=1}^N
a_n\Delta_n(u,\theta).
\]

For fixed

\[
u\ne0,
\]

we have

\[
\mathcal D_a(u,\theta)
=
-4
\sum_{n=1}^N
a_n
\left(
\cosh(nu)-1
\right)
\cos(n\theta).
\]

This is a real trigonometric polynomial with no constant Fourier term.

Therefore

\[
\int_0^{2\pi}
\mathcal D_a(u,\theta)
\,d\theta
=
0.
\]

Suppose

\[
\mathcal D_a(u,\theta)
\ge0
\]

for every real \(\theta\).

Continuity and zero integral imply

\[
\mathcal D_a(u,\theta)
\equiv0.
\]

By uniqueness of Fourier coefficients,

\[
a_n
\left(
\cosh(nu)-1
\right)
=
0
\]

for every

\[
1\le n\le N.
\]

Since

\[
u\ne0
\]

implies

\[
\cosh(nu)-1>0,
\]

we obtain

\[
a_n=0
\]

for every \(n\).

Therefore:

\[
\boxed{
\text{A fixed finite linear Li filter that is nonnegative for every }
\theta
\text{ and fixed }
u\ne0
\text{ must be trivial.}
}
\]

---

# 5. Absolutely convergent infinite-filter extension

Let

\[
\{a_n\}_{n\ge1}
\]

be a real coefficient sequence such that, for a fixed

\[
u\ne0,
\]

the series

\[
\sum_{n\ge1}
|a_n|
\left(
\cosh(nu)-1
\right)
\]

converges.

Then

\[
\mathcal D_a(u,\theta)
=
-4
\sum_{n\ge1}
a_n
\left(
\cosh(nu)-1
\right)
\cos(n\theta)
\]

converges absolutely and uniformly in \(\theta\).

Thus it is continuous and termwise integration is valid.

Again,

\[
\int_0^{2\pi}
\mathcal D_a(u,\theta)
\,d\theta
=
0.
\]

If

\[
\mathcal D_a(u,\theta)\ge0
\]

for every \(\theta\), then

\[
\mathcal D_a(u,\theta)\equiv0.
\]

Uniqueness of Fourier coefficients gives

\[
a_n
\left(
\cosh(nu)-1
\right)
=
0
\]

for every \(n\).

Hence

\[
a_n=0
\]

for every \(n\).

Therefore the obstruction extends to absolutely convergent fixed linear filters.

---

# 6. Consequence for positive horizontal-defect extraction

The positive horizontal amplitude

\[
\cosh(nu)-1
\]

is modulated by

\[
\cos(n\theta).
\]

A fixed linear combination of the quartet Li contrasts cannot remove this angular phase while remaining universally nonnegative.

Therefore no nontrivial fixed linear filter of the symmetric quartet Li contrasts yields a universally nonnegative horizontal-defect quantity for all angular phases.

This rules out the simplest proposed route from Li coefficients to a positive horizontal zero-displacement moment.

---

# 7. Single-quartet nonlinear energy

For a single quartet,

\[
\Delta_n(u,\theta)^2
=
16
\cos^2(n\theta)
\left(
\cosh(nu)-1
\right)^2
\ge0.
\]

Let

\[
b_n>0
\]

for every positive integer \(n\), and suppose

\[
\sum_{n\ge1}
b_n
\Delta_n(u,\theta)^2
\]

converges.

Define

\[
\mathcal E_b(u,\theta)
=
\sum_{n\ge1}
b_n
\Delta_n(u,\theta)^2.
\]

Then

\[
\mathcal E_b(u,\theta)\ge0.
\]

If

\[
u=0,
\]

then

\[
\Delta_n(0,\theta)=0
\]

for every \(n\), so

\[
\mathcal E_b(0,\theta)=0.
\]

Conversely, suppose

\[
u\ne0.
\]

Then

\[
\cosh(nu)-1>0
\]

for every positive integer \(n\).

The sequence

\[
\cos(n\theta)
\]

cannot vanish for every positive integer \(n\).

Indeed, if

\[
\cos\theta=0,
\]

then

\[
\cos(2\theta)=-1.
\]

Therefore at least one

\[
\Delta_n(u,\theta)
\]

is nonzero.

Since every \(b_n>0\),

\[
\mathcal E_b(u,\theta)>0.
\]

Hence, for a single quartet,

\[
\boxed{
\mathcal E_b(u,\theta)=0
\iff
u=0.
}
\]

This is a positive and faithful single-quartet horizontal-defect energy.

---

# 8. Global aggregation obstruction

The ordinary Li coefficients aggregate contributions from all zeros or symmetric zero orbits.

If

\[
\Delta_n^{\mathrm{agg}}
=
\sum_j
\Delta_{n,j},
\]

then

\[
\left(
\Delta_n^{\mathrm{agg}}
\right)^2
=
\sum_j
\Delta_{n,j}^2
+
2
\sum_{j<k}
\Delta_{n,j}
\Delta_{n,k}.
\]

The cross terms need not be nonnegative.

Distinct zero quartets may cancel before the aggregate is squared.

Therefore the positivity and faithfulness of the single-quartet energy do not automatically descend to a nonlinear functional of the ordinary aggregated Li sequence.

No global RH-equivalent energy criterion is proved here.

---

# 9. Research bottleneck

A globally faithful continuation would need a mechanism that separates or orthogonalizes zero-orbit contributions before nonlinear energy aggregation.

Candidate analytic structures include:

1. angular averaging;
2. radial averaging in the Li conformal disk;
3. Parseval identities for a Li generating transform;
4. Hardy-space norms;
5. reproducing-kernel transforms;
6. a two-parameter zero transform retaining angular and radial coordinates.

Before pursuing these, prior art on the analytic radius and singularity structure of the Li generating function must be audited.

---

# 10. Restrictions

The linear-filter obstruction does not prove RH.

The single-quartet nonlinear energy is not a global RH criterion.

No positive horizontal moment has been recovered from the ordinary aggregated Li coefficients.

No originality claim is made.

The exact relationship to classical Li, Bombieri-Lagarias, Keiper, and Voros analytic-generating-function formulations remains under prior-art review.

