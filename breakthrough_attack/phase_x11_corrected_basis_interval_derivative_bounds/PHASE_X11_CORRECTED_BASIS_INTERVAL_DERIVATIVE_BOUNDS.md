# Phase X11 — Corrected Basis Interval Derivative Bounds

## Purpose

Phase X10 created interval derivative bounds for individual log-bumps.

Phase X11 propagates those bounds to corrected pole-cancelled basis functions:

\[
\Phi=b-\alpha u_0-\beta u_1.
\]

The goal is interval bounds for:

\[
\Phi,\quad \Phi',\quad \Phi''.
\]

---

# 1. Corrected basis formula

Recall the corrected basis construction:

\[
\Phi=b-\alpha u_0-\beta u_1.
\]

Here:

\[
b,u_0,u_1\in C_c^\infty(0,\infty).
\]

The coefficients \(\alpha,\beta\) are chosen to cancel Mellin moments at \(0\) and \(1\).

---

# 2. Derivative formulas

By linearity:

\[
\Phi'=b'-\alpha u_0'-\beta u_1',
\]

and:

\[
\Phi''=b''-\alpha u_0''-\beta u_1''.
\]

Thus interval enclosures for \(b,u_0,u_1\) and their derivatives propagate directly to interval enclosures for \(\Phi,\Phi',\Phi''\).

---

# 3. Coefficient warning

The current \(\alpha,\beta\) values were computed numerically.

This phase wraps them in small conservative Decimal intervals.

That is stronger than plain floating point, but not a full proof of the Mellin-moment solve.

Therefore the status is:

\[
\boxed{
\texttt{CORRECTED\_BASIS\_INTERVAL\_BOUNDS\_CREATED\_COEFFICIENTS\_NOT\_CERTIFIED}
}
\]

---

# Theorem X11.1 — corrected basis derivative propagation

If:

\[
\Phi=b-\alpha u_0-\beta u_1,
\]

then:

\[
\Phi^{(k)}=b^{(k)}-\alpha u_0^{(k)}-\beta u_1^{(k)}
\]

for:

\[
k=0,1,2.
\]

## Proof

Differentiation is linear.

For \(k=0\), this is the definition.

For \(k=1\) and \(k=2\), differentiate once or twice.

\[
\square
\]

---

# Theorem X11.2 — interval enclosure for corrected basis derivatives

Assume intervals enclose:

\[
b^{(k)}(X),\quad u_0^{(k)}(X),\quad u_1^{(k)}(X),
\]

and intervals enclose:

\[
\alpha,\quad \beta.
\]

Then interval arithmetic applied to:

\[
b^{(k)}-\alpha u_0^{(k)}-\beta u_1^{(k)}
\]

encloses:

\[
\Phi^{(k)}(X)
\]

for \(k=0,1,2\).

## Proof

This follows from Theorem X11.1 and the interval enclosure principle.

\[
\square
\]

---

# 4. Breakthrough relevance

This phase transfers interval derivative machinery from primitive bumps to the actual corrected pole-cancelled basis.

This removes another layer between the project and a certified single-entry bound.

But it still does not certify \(M_{00}\).

---

# 5. Next phase

Phase X12 should propagate corrected-basis derivative bounds through:

\[
\Phi^*(x)=x^{-1}\Phi(1/x),
\]

and then to the convolution:

\[
F=\Phi*\Phi^*.
\]

The target is an actual interval upper bound for:

\[
\|F''\|_\infty.
\]

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not compute a certified arithmetic entry.

It creates corrected-basis interval derivative bounds with coefficient-certification still incomplete.

Exact audit strings:

PHASE_X11_CORRECTED_BASIS_INTERVAL_DERIVATIVE_BOUNDS_COMPLETE

CORRECTED_BASIS_VALUE_INTERVAL_CREATED

CORRECTED_BASIS_FIRST_DERIVATIVE_INTERVAL_CREATED

CORRECTED_BASIS_SECOND_DERIVATIVE_INTERVAL_CREATED

CORRECTED_BASIS_DERIVATIVE_PROPAGATION_PROVED

CORRECTED_BASIS_INTERVAL_ENCLOSURE_PROVED

COEFFICIENT_INTERVAL_WRAPPERS_CREATED

COEFFICIENT_CERTIFICATION_INCOMPLETE

CERTIFIED_ENTRY_NOT_COMPUTED

READY_FOR_PHASE_X12_STAR_AND_CONVOLUTION_DERIVATIVE_BOUNDS

