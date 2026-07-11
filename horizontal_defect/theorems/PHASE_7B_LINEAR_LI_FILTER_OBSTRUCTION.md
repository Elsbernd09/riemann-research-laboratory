# Phase 7B — Linear Li-Filter Obstruction Theorem

## Purpose

This phase proves the first theorem in the horizontal defect program.

The theorem explains why finite linear combinations of Li horizontal contrasts cannot create a universal positive detector of horizontal zero displacement.

This is not a proof of RH.

It is an obstruction theorem: it identifies a class of attacks that cannot work without nonlinear or quadratic information.

---

# 1. Li-coordinate geometry

For a zero

\[
\rho=\beta+i\gamma,
\]

define the Li coordinate

\[
w(\rho)=1-\frac1\rho.
\]

Write

\[
w=e^{u+i\theta}.
\]

Then

\[
u=\log |w|.
\]

Critical-line zeros satisfy

\[
u=0.
\]

Off-critical zeros satisfy

\[
u\ne0.
\]

Thus horizontal displacement can be detected through radial displacement in Li coordinates.

---

# 2. Single-quartet Li contrast

For a symmetric quartet, the Li-coordinate contribution contains terms of the form

\[
\cos(n\theta)\cosh(nu).
\]

The horizontal contrast relative to the critical line has the model form

\[
\Delta_n(u,\theta)
=
\cos(n\theta)(\cosh(nu)-1).
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
\Delta_n(u,\theta)
=
\frac{n^2u^2}{2}\cos(n\theta)
+
O(u^4).
\]

The horizontal defect appears, but it is multiplied by an oscillatory phase factor.

---

# 3. Finite linear filter

Consider a finite real linear filter

\[
L(u,\theta)
=
\sum_{n=1}^N a_n\Delta_n(u,\theta),
\]

where \(a_n\in\mathbb R\).

Then

\[
L(u,\theta)
=
\sum_{n=1}^N
a_n\cos(n\theta)(\cosh(nu)-1).
\]

For small \(u\),

\[
L(u,\theta)
=
\frac{u^2}{2}
\sum_{n=1}^N
a_nn^2\cos(n\theta)
+
O(u^4).
\]

Define the trigonometric polynomial

\[
P(\theta)
=
\sum_{n=1}^N
a_nn^2\cos(n\theta).
\]

---

# 4. Key lemma

## Lemma

If

\[
P(\theta)
=
\sum_{n=1}^N b_n\cos(n\theta)
\]

is a real cosine polynomial with no constant term and

\[
P(\theta)\ge0
\]

for every \(\theta\), then

\[
P(\theta)\equiv0.
\]

## Proof

Integrate over one period:

\[
\int_0^{2\pi}P(\theta)d\theta
=
\sum_{n=1}^N
b_n
\int_0^{2\pi}\cos(n\theta)d\theta
=
0.
\]

If \(P(\theta)\ge0\) everywhere and its integral is zero, then \(P(\theta)=0\) almost everywhere.

Since \(P\) is continuous, it follows that

\[
P(\theta)\equiv0.
\]

---

# 5. Main obstruction theorem

## Theorem

Let

\[
L(u,\theta)
=
\sum_{n=1}^N
a_n\cos(n\theta)(\cosh(nu)-1)
\]

with real coefficients \(a_n\).

If \(L(u,\theta)\ge0\) for all sufficiently small \(u\ne0\) and all \(\theta\), then

\[
\sum_{n=1}^N
a_nn^2\cos(n\theta)
\equiv0.
\]

In particular, unless the leading horizontal-defect term vanishes identically, the linear filter cannot be a universal nonnegative detector of horizontal displacement.

## Proof

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
P(\theta)
=
\sum_{n=1}^N
a_nn^2\cos(n\theta).
\]

If \(P\) takes a negative value at some \(\theta_0\), then by continuity

\[
P(\theta)<0
\]

on a neighborhood of \(\theta_0\). For sufficiently small nonzero \(u\), the \(u^2P(\theta)/2\) term dominates the \(O(u^4)\) remainder, so

\[
L(u,\theta)<0
\]

there.

Therefore universal nonnegativity of \(L\) for all sufficiently small \(u\ne0\) forces

\[
P(\theta)\ge0
\]

for every \(\theta\).

By the key lemma, since \(P\) has no constant term,

\[
P\equiv0.
\]

This proves the theorem.

---

# 6. Consequence

A finite linear combination of Li horizontal contrasts cannot provide a universal positive horizontal-defect detector at leading order.

To obtain positivity, one must introduce at least one of:

1. a constant term;
2. nonlinear squaring;
3. a quadratic form;
4. a signed/indefinite criterion such as classical Weil machinery;
5. additional arithmetic constraints.

---

# 7. RH relevance

This theorem does not prove RH.

It clarifies why a broad family of naive linear Li-filter attacks cannot prove RH.

This is useful because it narrows the search space.

