# Phase X12 — Star and Convolution Derivative Bounds

## Purpose

Phase X11 created interval derivative bounds for the corrected pole-cancelled basis:

\[
\Phi,\quad \Phi',\quad \Phi''.
\]

Phase X12 propagates those bounds through the Hermitian star:

\[
\Phi^*(x)=x^{-1}\Phi(1/x)
\]

and then through the convolution:

\[
F=\Phi*\Phi^*.
\]

The goal is an upper bound for:

\[
\|F''\|_\infty.
\]

---

# 1. Star derivative formula

For real-valued \(\Phi\):

\[
\Phi^*(x)=x^{-1}\Phi(1/x).
\]

Then:

\[
(\Phi^*)''(x)
=
2x^{-3}\Phi(1/x)
+
4x^{-4}\Phi'(1/x)
+
x^{-5}\Phi''(1/x).
\]

This formula was proved earlier and is now applied with interval bounds.

---

# 2. Convolution second derivative formula

Let:

\[
F(x)=\int_L^U \Phi(y)\Phi^*(x/y)\frac{dy}{y}.
\]

Then:

\[
F''(x)
=
\int_L^U
\Phi(y)(\Phi^*)''(x/y)
\frac{dy}{y^3}.
\]

Therefore:

\[
|F''(x)|
\le
\|\Phi\|_\infty
\|(\Phi^*)''\|_\infty
\int_L^U y^{-3}\,dy.
\]

Since:

\[
\int_L^U y^{-3}\,dy
=
\frac12(L^{-2}-U^{-2}),
\]

we get:

\[
\boxed{
\|F''\|_\infty
\le
\frac12
\|\Phi\|_\infty
\|(\Phi^*)''\|_\infty
(L^{-2}-U^{-2}).
}
\]

---

# 3. Certification status

This phase creates a structured interval upper bound.

However, because X11 coefficient intervals still wrap numerical \(\alpha,\beta\) values rather than proving the Mellin solve, the status is:

\[
\boxed{
\texttt{CONVOLUTION\_SECOND\_DERIVATIVE\_BOUND\_CREATED\_COEFFICIENTS\_NOT\_CERTIFIED}
}
\]

This is still useful because it produces the exact bound shape needed by the X6 certified quadrature theorem.

---

# Theorem X12.1 — star second derivative interval enclosure

Assume interval bounds enclose:

\[
\Phi(X^{-1}),\quad \Phi'(X^{-1}),\quad \Phi''(X^{-1}).
\]

Then interval arithmetic applied to:

\[
2x^{-3}\Phi(1/x)
+
4x^{-4}\Phi'(1/x)
+
x^{-5}\Phi''(1/x)
\]

encloses:

\[
(\Phi^*)''(X).
\]

## Proof

The formula for \((\Phi^*)''\) is exact.

If every term in the expression is interval-enclosed, then the full expression is enclosed by the interval enclosure principle.

\[
\square
\]

---

# Theorem X12.2 — convolution second derivative bound

If:

\[
\|\Phi\|_\infty\le B_0
\]

and:

\[
\|(\Phi^*)''\|_\infty\le B_2^*
\]

on the relevant supports, and:

\[
\operatorname{supp}(\Phi)\subset[L,U],
\]

then:

\[
\|F''\|_\infty
\le
\frac12B_0B_2^*(L^{-2}-U^{-2}).
\]

## Proof

By the convolution derivative formula:

\[
F''(x)=
\int_L^U
\Phi(y)(\Phi^*)''(x/y)
\frac{dy}{y^3}.
\]

Taking absolute values gives:

\[
|F''(x)|
\le
B_0B_2^*
\int_L^U y^{-3}\,dy.
\]

The integral equals:

\[
\frac12(L^{-2}-U^{-2}).
\]

Taking the supremum over \(x\) proves the result.

\[
\square
\]

---

# 4. Breakthrough relevance

This phase finally creates a usable candidate bound for:

\[
\|F''\|_\infty.
\]

That is the exact missing ingredient for the X6 midpoint quadrature theorem.

But because coefficient certification and formal interval verification are still incomplete, this is not yet a fully certified arithmetic entry.

---

# 5. Next phase

Phase X13 should feed this \(F''\) bound back into the single-entry pipeline and create a genuine interval enclosure for the central integral part of:

\[
M_{00}=T_{BL}[F].
\]

The status will likely be:

\[
\texttt{PARTIAL\_ENTRY\_INTERVAL\_CERTIFICATE}
\]

not yet full certification.

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not compute a fully certified arithmetic entry.

It creates the star and convolution derivative-bound machinery needed for the next certification step.

Exact audit strings:

PHASE_X12_STAR_AND_CONVOLUTION_DERIVATIVE_BOUNDS_COMPLETE

STAR_SECOND_DERIVATIVE_INTERVAL_BOUND_CREATED

CONVOLUTION_SECOND_DERIVATIVE_BOUND_CREATED

STAR_SECOND_DERIVATIVE_INTERVAL_ENCLOSURE_PROVED

CONVOLUTION_SECOND_DERIVATIVE_BOUND_PROVED

F_SECOND_DERIVATIVE_BOUND_AVAILABLE_FOR_QUADRATURE

COEFFICIENT_CERTIFICATION_INCOMPLETE

CERTIFIED_ENTRY_NOT_COMPUTED

READY_FOR_PHASE_X13_PARTIAL_SINGLE_ENTRY_INTERVAL_CERTIFICATE

