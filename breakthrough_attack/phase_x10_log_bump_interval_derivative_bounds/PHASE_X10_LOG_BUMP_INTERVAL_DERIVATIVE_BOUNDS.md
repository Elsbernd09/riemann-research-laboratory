# Phase X10 — Log-Bump Interval Derivative Bounds

## Purpose

Phase X9 created primitive interval bounds for:

\[
\psi,\quad \psi',\quad \psi''.
\]

Phase X10 propagates those bounds to log-bumps:

\[
\phi(x)=\psi\left(\frac{\log x-c}{w}\right).
\]

The target is interval bounds for:

\[
\phi,\quad \phi',\quad \phi''.
\]

---

# 1. Log-bump formulas

Let:

\[
u(x)=\frac{\log x-c}{w}.
\]

Then:

\[
\phi(x)=\psi(u(x)).
\]

By the chain rule:

\[
\phi'(x)=\psi'(u(x))\frac1{wx}.
\]

Also:

\[
\phi''(x)
=
\psi''(u(x))\frac{1}{w^2x^2}
-
\psi'(u(x))\frac{1}{wx^2}.
\]

---

# 2. Interval propagation

For an \(x\)-interval:

\[
X=[a,b]\subset(0,\infty),
\]

we compute an interval enclosure for:

\[
U=\frac{\log X-c}{w}.
\]

Then we use X9 to enclose:

\[
\psi(U),\quad \psi'(U),\quad \psi''(U).
\]

Finally we propagate:

\[
\phi(X)\subset\psi(U),
\]

\[
\phi'(X)\subset\psi'(U)\frac1{wX},
\]

\[
\phi''(X)
\subset
\psi''(U)\frac1{w^2X^2}
-
\psi'(U)\frac1{wX^2}.
\]

---

# 3. Log interval warning

This phase uses Decimal endpoints and monotonicity of \(\log x\):

\[
\log([a,b])=[\log a,\log b].
\]

The implementation is conservative, but it is still not formally verified in a proof assistant.

Therefore the status remains:

\[
\boxed{
\texttt{LOG\_BUMP\_INTERVAL\_BOUNDS\_CREATED\_NOT\_FORMALLY\_VERIFIED}
}
\]

---

# Theorem X10.1 — log-bump derivative formulas

For:

\[
\phi(x)=\psi((\log x-c)/w),
\]

with \(w>0\), we have:

\[
\phi'(x)=\psi'(u(x))\frac1{wx},
\]

and:

\[
\phi''(x)
=
\psi''(u(x))\frac{1}{w^2x^2}
-
\psi'(u(x))\frac{1}{wx^2}.
\]

## Proof

This is the chain rule.

\[
u'(x)=\frac1{wx},
\qquad
u''(x)=-\frac1{wx^2}.
\]

Thus:

\[
\phi'(x)=\psi'(u(x))u'(x),
\]

and:

\[
\phi''(x)=\psi''(u(x))(u'(x))^2+\psi'(u(x))u''(x).
\]

Substituting \(u'\) and \(u''\) gives the formula.

\[
\square
\]

---

# Theorem X10.2 — interval propagation principle for log-bump derivatives

If interval arithmetic encloses \(U=u(X)\), and X9 encloses:

\[
\psi(U),\quad \psi'(U),\quad \psi''(U),
\]

then the formulas in Theorem X10.1 produce interval enclosures for:

\[
\phi(X),\quad \phi'(X),\quad \phi''(X).
\]

## Proof

The expressions for \(\phi,\phi',\phi''\) are composed from arithmetic operations, \(\log\), and the primitive bump functions.

If each primitive operation is replaced by a containing interval operation, the final interval contains the true expression value by the interval enclosure principle from X9.

\[
\square
\]

---

# 4. Breakthrough relevance

This phase propagates primitive bump bounds into actual smooth log-bump derivative bounds.

It is a necessary step toward certified bounds for the corrected pole-cancelled basis.

It still does not certify a matrix entry.

---

# 5. Next phase

Phase X11 should propagate log-bump interval derivative bounds to the corrected pole-cancelled basis:

\[
\Phi=b-\alpha u_0-\beta u_1.
\]

The needed bounds are:

\[
\Phi,\quad \Phi',\quad \Phi''.
\]

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not compute a certified arithmetic entry.

It creates log-bump interval derivative bounds needed for the corrected-basis certification step.

Exact audit strings:

PHASE_X10_LOG_BUMP_INTERVAL_DERIVATIVE_BOUNDS_COMPLETE

LOG_INTERVAL_ENCLOSURE_CREATED

LOG_BUMP_VALUE_INTERVAL_CREATED

LOG_BUMP_FIRST_DERIVATIVE_INTERVAL_CREATED

LOG_BUMP_SECOND_DERIVATIVE_INTERVAL_CREATED

LOG_BUMP_DERIVATIVE_FORMULAS_PROVED

LOG_BUMP_INTERVAL_PROPAGATION_PROVED

LOG_BUMP_INTERVAL_BOUNDS_CREATED_NOT_FORMALLY_VERIFIED

CERTIFIED_ENTRY_NOT_COMPUTED

READY_FOR_PHASE_X11_CORRECTED_BASIS_INTERVAL_DERIVATIVE_BOUNDS

