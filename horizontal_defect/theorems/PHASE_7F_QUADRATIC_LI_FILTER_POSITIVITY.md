# Phase 7F — Quadratic Li-Filter Positivity Lift

## Purpose

Phase 7B and Phase 7E proved that finite linear Li horizontal-defect filters cannot serve as universal positive phase-independent detectors.

This phase shows that quadratic lifting fixes the phase-sign problem.

The price is that the resulting object is nonlinear and no longer automatically compatible with the classical linear explicit formula.

This phase does not prove RH.

It constructs a positive finite quadratic detector and records the remaining arithmetic-side obstruction.

---

# 1. Linear horizontal contrast features

Write the Li coordinate as

\[
w=e^{u+i\theta}.
\]

The critical line corresponds to

\[
u=0.
\]

Define the model Li horizontal contrast features

\[
\Delta_n(u,\theta)
=
\cos(n\theta)(\cosh(nu)-1).
\]

For small \(u\),

\[
\Delta_n(u,\theta)
=
\frac{n^2u^2}{2}\cos(n\theta)
+
O(u^4).
\]

Each individual \(\Delta_n\) is sign-changing in \(\theta\).

---

# 2. Quadratic lift

Define

\[
Q_{1,2}(u,\theta)
=
\Delta_1(u,\theta)^2
+
\Delta_2(u,\theta)^2.
\]

Since this is a sum of squares,

\[
Q_{1,2}(u,\theta)\ge0.
\]

The key question is whether it can vanish for \(u\ne0\).

---

# 3. Phase-uniform positivity theorem

## Theorem

For

\[
u\ne0,
\]

one has

\[
Q_{1,2}(u,\theta)>0
\]

for every real \(\theta\).

Equivalently, the two-frequency quadratic Li-filter lift is a positive phase-uniform horizontal-displacement detector.

## Proof

If

\[
Q_{1,2}(u,\theta)=0,
\]

then both squares vanish:

\[
\Delta_1(u,\theta)=0
\]

and

\[
\Delta_2(u,\theta)=0.
\]

For \(u\ne0\),

\[
\cosh(u)-1>0
\]

and

\[
\cosh(2u)-1>0.
\]

Therefore

\[
\Delta_1(u,\theta)=0
\]

implies

\[
\cos\theta=0.
\]

But if

\[
\cos\theta=0,
\]

then

\[
\theta=\frac{\pi}{2}+k\pi.
\]

Hence

\[
\cos(2\theta)=\cos(\pi+2k\pi)=-1.
\]

So

\[
\Delta_2(u,\theta)
=
-\left(\cosh(2u)-1\right)
\ne0.
\]

Contradiction.

Therefore \(Q_{1,2}(u,\theta)>0\) for all \(u\ne0\) and all \(\theta\).

---

# 4. Small-displacement profile

Using

\[
\Delta_n(u,\theta)
=
\frac{n^2u^2}{2}\cos(n\theta)
+
O(u^4),
\]

we get

\[
Q_{1,2}(u,\theta)
=
\frac{u^4}{4}
\left(
\cos^2\theta
+
16\cos^2(2\theta)
\right)
+
O(u^6).
\]

The leading factor

\[
\cos^2\theta+16\cos^2(2\theta)
\]

is strictly positive for all \(\theta\).

Therefore the quadratic detector is faithful but fourth-order in \(u\).

---

# 5. General quadratic form version

Let

\[
\Delta(u,\theta)
=
(\Delta_1(u,\theta),\ldots,\Delta_N(u,\theta))^T.
\]

For any positive semidefinite matrix

\[
A\succeq0,
\]

the quadratic form

\[
Q_A(u,\theta)
=
\Delta(u,\theta)^T A\Delta(u,\theta)
\]

is nonnegative.

If \(A\) is positive definite and the vector \(\Delta(u,\theta)\) is never zero for \(u\ne0\), then \(Q_A\) is strictly positive.

The case \(N=2\) with \(A=I\) already gives strict phase-uniform positivity.

---

# 6. What this solves

This solves the phase-sign obstruction for finite model Li horizontal contrasts.

Linear filters fail because their leading phase polynomial has zero mean.

Quadratic filters succeed because squaring removes sign cancellation at the single-quartet level.

---

# 7. What remains unsolved

The new obstruction is arithmetic compatibility.

Classical explicit formulae are linear in zero-side test functions:

\[
\sum_\rho h(\rho).
\]

The quadratic detector involves products and squares:

\[
\Delta_m\Delta_n.
\]

Such terms do not automatically appear as a standard Weil/Guinand zero-side expression.

Therefore the next serious problem is:

\[
\boxed{
\text{Can the quadratic Li-filter lift be represented, bounded, or approximated by Weil-positive machinery?}
}
\]

---

# 8. RH relevance

This theorem does not prove RH.

It shows that quadratic information can defeat the finite linear phase obstruction.

It identifies the next barrier: connecting quadratic positivity to arithmetic-side control.

