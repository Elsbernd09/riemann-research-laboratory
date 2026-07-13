# Phase X8 — Derivative Bound Certification Reduction

## Purpose

Phase X7 created the first single-entry pipeline for:

\[
M_{00}=T_{BL}[\phi_0*\phi_0^*].
\]

The blocker was:

\[
\sup |F_{00}''|,
\qquad
\sup |\widetilde F_{00}''|,
\qquad
\sup |(A_F^{cont})''|.
\]

Phase X8 attacks this by proving derivative-bound reduction theorems.

It does not yet produce a fully certified derivative bound.

It reduces the problem to primitive smooth-bump derivative bounds.

---

# 1. Smooth bump derivatives

Let:

\[
\psi(u)=\exp\left(-\frac1{1-u^2}\right)
\]

for \(|u|<1\), and \(0\) otherwise.

Let:

\[
\phi(x)=\psi\left(\frac{\log x-c}{w}\right).
\]

Define:

\[
u(x)=\frac{\log x-c}{w}.
\]

Then:

\[
\phi'(x)=\psi'(u(x))\frac{1}{wx}.
\]

Also:

\[
\phi''(x)
=
\psi''(u(x))\frac{1}{w^2x^2}
-
\psi'(u(x))\frac{1}{wx^2}.
\]

Thus bounds for \(\phi''\) reduce to bounds for \(\psi'\) and \(\psi''\).

---

# 2. Corrected basis derivative bounds

The pole-cancelled basis has:

\[
\Phi=b-\alpha u_0-\beta u_1.
\]

Therefore:

\[
\Phi''=b''-\alpha u_0''-\beta u_1''.
\]

Hence:

\[
\|\Phi''\|_\infty
\le
\|b''\|_\infty
+
|\alpha|\|u_0''\|_\infty
+
|\beta|\|u_1''\|_\infty.
\]

---

# 3. Star derivative bounds

The Hermitian star is:

\[
\Phi^*(x)=x^{-1}\overline{\Phi(1/x)}.
\]

For real-valued \(\Phi\), this is:

\[
\Phi^*(x)=x^{-1}\Phi(1/x).
\]

Differentiate:

\[
(\Phi^*)'(x)
=
-x^{-2}\Phi(1/x)
-
x^{-3}\Phi'(1/x).
\]

Differentiate again:

\[
(\Phi^*)''(x)
=
2x^{-3}\Phi(1/x)
+
4x^{-4}\Phi'(1/x)
+
x^{-5}\Phi''(1/x).
\]

Thus star derivative bounds reduce to bounds for \(\Phi,\Phi',\Phi''\).

---

# 4. Convolution second derivative bound

Let:

\[
F(x)=\Phi*\Phi^*(x)
=
\int_0^\infty \Phi(y)\Phi^*(x/y)\frac{dy}{y}.
\]

Then:

\[
F''(x)
=
\int_0^\infty \Phi(y)(\Phi^*)''(x/y)\frac{dy}{y^3}.
\]

Therefore:

\[
|F''(x)|
\le
\|\Phi\|_\infty
\|(\Phi^*)''\|_\infty
\int_{L}^{U}\frac{dy}{y^3},
\]

where:

\[
\operatorname{supp}(\Phi)\subset[L,U].
\]

The integral is:

\[
\int_L^U y^{-3}dy
=
\frac12(L^{-2}-U^{-2}).
\]

Thus:

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

# Theorem X8.1 — log-bump second derivative formula

For:

\[
\phi(x)=\psi((\log x-c)/w),
\]

with \(w>0\), we have:

\[
\phi''(x)
=
\psi''(u(x))\frac{1}{w^2x^2}
-
\psi'(u(x))\frac{1}{wx^2}.
\]

## Proof

By the chain rule:

\[
\phi'(x)=\psi'(u(x))u'(x)
=
\psi'(u(x))\frac1{wx}.
\]

Differentiating again:

\[
\phi''(x)
=
\psi''(u(x))(u'(x))^2+\psi'(u(x))u''(x).
\]

Since:

\[
u'(x)=\frac1{wx},
\qquad
u''(x)=-\frac1{wx^2},
\]

the result follows.

\[
\square
\]

---

# Theorem X8.2 — corrected basis derivative bound

If:

\[
\Phi=b-\alpha u_0-\beta u_1,
\]

then:

\[
\|\Phi''\|_\infty
\le
\|b''\|_\infty
+
|\alpha|\|u_0''\|_\infty
+
|\beta|\|u_1''\|_\infty.
\]

## Proof

Differentiate twice and apply the triangle inequality.

\[
\square
\]

---

# Theorem X8.3 — star second derivative formula

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

## Proof

Differentiate:

\[
(\Phi^*)'(x)
=
-x^{-2}\Phi(1/x)
-
x^{-3}\Phi'(1/x).
\]

Differentiate again:

\[
(\Phi^*)''(x)
=
2x^{-3}\Phi(1/x)
+
x^{-4}\Phi'(1/x)
+
3x^{-4}\Phi'(1/x)
+
x^{-5}\Phi''(1/x).
\]

Combining terms gives:

\[
(\Phi^*)''(x)
=
2x^{-3}\Phi(1/x)
+
4x^{-4}\Phi'(1/x)
+
x^{-5}\Phi''(1/x).
\]

\[
\square
\]

---

# Theorem X8.4 — convolution second derivative bound

Let:

\[
F(x)=\int_L^U \Phi(y)\Phi^*(x/y)\frac{dy}{y}.
\]

Assume \(\Phi\) is bounded and \((\Phi^*)''\) is bounded. Then:

\[
\|F''\|_\infty
\le
\frac12
\|\Phi\|_\infty
\|(\Phi^*)''\|_\infty
(L^{-2}-U^{-2}).
\]

## Proof

Differentiating twice under the integral gives:

\[
F''(x)=\int_L^U \Phi(y)(\Phi^*)''(x/y)\frac{dy}{y^3}.
\]

Taking absolute values:

\[
|F''(x)|
\le
\|\Phi\|_\infty\|(\Phi^*)''\|_\infty\int_L^U y^{-3}dy.
\]

Since:

\[
\int_L^U y^{-3}dy
=
\frac12(L^{-2}-U^{-2}),
\]

the result follows.

\[
\square
\]

---

# 5. Honest certification status

This phase proves the derivative-bound reduction formulas.

The code estimates bounds numerically on grids.

But grid estimates are not rigorous interval bounds.

Therefore the correct status is:

\[
\boxed{\texttt{DERIVATIVE\_BOUNDS\_REDUCED\_BUT\_NOT\_CERTIFIED}}
\]

---

# 6. Next phase

Phase X9 should implement primitive interval arithmetic or rational interval envelopes for:

\[
\psi,\quad \psi',\quad \psi''
\]

on subintervals of \((-1,1)\).

That is the path to real derivative certification.

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not compute a certified arithmetic entry.

It proves derivative-bound reduction theorems and identifies primitive bump interval bounds as the next blocker.

Exact audit strings:

PHASE_X8_DERIVATIVE_BOUND_CERTIFICATION_COMPLETE

LOG_BUMP_SECOND_DERIVATIVE_FORMULA_PROVED

CORRECTED_BASIS_DERIVATIVE_BOUND_PROVED

STAR_SECOND_DERIVATIVE_FORMULA_PROVED

CONVOLUTION_SECOND_DERIVATIVE_BOUND_PROVED

DERIVATIVE_BOUND_REDUCTION_CREATED

HEURISTIC_DERIVATIVE_ENVELOPES_COMPUTED

DERIVATIVE_BOUNDS_REDUCED_BUT_NOT_CERTIFIED

CERTIFIED_ENTRY_NOT_COMPUTED

READY_FOR_PHASE_X9_PRIMITIVE_INTERVAL_BUMP_BOUNDS

