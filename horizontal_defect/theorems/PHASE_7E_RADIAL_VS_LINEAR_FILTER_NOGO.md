# Phase 7E — No-Go Comparison: Radial Defect vs Linear Li Filters

## Purpose

Phase 7C constructed the positive radial Li-coordinate defect

\[
D_{\mathrm{rad}}(\rho)=\left(\log |1-1/\rho|\right)^2.
\]

Phase 7D showed that positive aggregation is easy but arithmetic-side compatibility is hard.

This phase proves a sharper obstruction:

\[
\boxed{
\text{No finite linear Li horizontal-defect filter can uniformly dominate the radial defect near the critical line.}
}
\]

This is not a proof of RH.

It is a no-go theorem showing why one cannot simply compare the positive radial defect to finite linear Li filters.

---

# 1. Model setup

Write the Li coordinate as

\[
w=e^{u+i\theta}.
\]

The critical line corresponds to

\[
u=0.
\]

The radial defect is

\[
D_{\mathrm{rad}}=u^2.
\]

A finite linear Li horizontal-defect filter has the model form

\[
L(u,\theta)
=
\sum_{n=1}^{N}
a_n\cos(n\theta)(\cosh(nu)-1),
\]

where

\[
a_n\in\mathbb R.
\]

For small \(u\),

\[
\cosh(nu)-1
=
\frac{n^2u^2}{2}
+
O(u^4).
\]

Therefore

\[
L(u,\theta)
=
\frac{u^2}{2}
P(\theta)
+
O(u^4),
\]

where

\[
P(\theta)
=
\sum_{n=1}^{N}
a_nn^2\cos(n\theta).
\]

The function \(P\) is a finite real cosine polynomial with no constant term.

---

# 2. Zero-mean obstruction

For every integer \(n\ge1\),

\[
\int_0^{2\pi}\cos(n\theta)d\theta=0.
\]

Therefore

\[
\int_0^{2\pi}P(\theta)d\theta=0.
\]

If \(P\) were strictly positive everywhere, its integral would be positive.

Thus \(P\) cannot be strictly positive everywhere.

This creates a comparison obstruction.

---

# 3. Main theorem

## Theorem

Let

\[
L(u,\theta)
=
\sum_{n=1}^{N}
a_n\cos(n\theta)(\cosh(nu)-1)
\]

be a finite real linear Li horizontal-defect filter.

There is no constant

\[
c>0
\]

such that, for all sufficiently small nonzero \(u\) and all \(\theta\),

\[
L(u,\theta)\ge c u^2.
\]

Equivalently, no finite linear Li horizontal-defect filter can uniformly dominate the positive radial defect \(u^2\) near the critical line.

## Proof

Assume for contradiction that such a constant \(c>0\) exists.

For small \(u\),

\[
L(u,\theta)
=
\frac{u^2}{2}P(\theta)
+
O(u^4),
\]

where

\[
P(\theta)=\sum_{n=1}^{N}a_nn^2\cos(n\theta).
\]

Dividing by \(u^2\) gives

\[
\frac{L(u,\theta)}{u^2}
=
\frac12 P(\theta)+O(u^2).
\]

The assumed lower bound gives

\[
\frac{L(u,\theta)}{u^2}\ge c.
\]

Letting \(u\to0\), we obtain

\[
\frac12 P(\theta)\ge c
\]

for every \(\theta\).

Thus

\[
P(\theta)\ge2c>0
\]

for every \(\theta\).

But \(P\) has zero mean:

\[
\int_0^{2\pi}P(\theta)d\theta=0.
\]

A continuous function that is strictly positive everywhere cannot have zero integral.

Contradiction.

Therefore no such \(c>0\) exists.

---

# 4. Stronger consequence

A two-sided comparison

\[
c u^2
\le
L(u,\theta)
\le
C u^2
\]

with

\[
c>0
\]

is also impossible.

Thus finite linear Li filters cannot be used as positive lower models for the radial defect energy.

---

# 5. Interpretation

The radial defect energy

\[
u^2
\]

is positive and phase-independent.

Finite linear Li horizontal filters have leading behavior

\[
u^2P(\theta),
\]

where \(P\) is zero-mean in the phase variable.

That zero-mean phase dependence prevents uniform positive domination.

This explains why the path from positive radial defect to arithmetic-side explicit formula cannot go through ordinary finite linear Li filters.

A successful path must use something outside this class, such as:

1. nonlinear squaring;
2. positive quadratic forms;
3. classical Weil positivity;
4. infinite limiting constructions with a genuine constant mode;
5. arithmetic constraints that restrict the allowed phase set.

---

# 6. RH relevance

This theorem does not prove RH.

It rules out a tempting bridge from a positive horizontal-defect energy to finite linear Li filters.

The obstruction is useful because it narrows the search space.

