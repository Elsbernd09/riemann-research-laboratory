# Phase X9 — Primitive Interval Bump Bounds

## Purpose

Phase X8 reduced derivative certification to primitive bounds for:

\[
\psi,\quad \psi',\quad \psi''.
\]

Phase X9 creates an interval arithmetic engine for the standard smooth bump:

\[
\psi(u)=
\begin{cases}
\exp(-1/(1-u^2)), & |u|<1,\\
0, & |u|\ge1.
\end{cases}
\]

This phase creates primitive interval enclosures for:

\[
\psi(I),\quad \psi'(I),\quad \psi''(I)
\]

on compact subintervals:

\[
I\subset(-1,1).
\]

---

# 1. Derivative formulas

Let:

\[
d=1-u^2.
\]

For \(|u|<1\),

\[
\psi(u)=e^{-1/d}.
\]

Define:

\[
p(u)=\frac{-2u}{d^2}.
\]

Then:

\[
\psi'(u)=\psi(u)p(u).
\]

Also:

\[
p'(u)=-\frac{2}{d^2}-\frac{8u^2}{d^3}.
\]

Therefore:

\[
\psi''(u)=\psi(u)(p(u)^2+p'(u)).
\]

---

# 2. Interval method

For an interval:

\[
I=[a,b]\subset(-1,1),
\]

the code computes interval enclosures for:

\[
u,\quad u^2,\quad d=1-u^2,\quad d^{-1},\quad e^{-d^{-1}},
\]

then propagates the formulas for \(\psi,\psi',\psi''\).

The arithmetic uses conservative interval operations.

---

# 3. Theorem X9.1 — primitive derivative formulas

For \(|u|<1\), with \(d=1-u^2\),

\[
\psi'(u)=\psi(u)\frac{-2u}{d^2},
\]

and:

\[
\psi''(u)=\psi(u)
\left[
\left(\frac{-2u}{d^2}\right)^2
-\frac{2}{d^2}
-\frac{8u^2}{d^3}
\right].
\]

## Proof

Since:

\[
\psi(u)=e^{-1/d},
\]

we compute:

\[
\frac{d}{du}\left(-\frac1d\right)
=
-\frac{2u}{d^2}.
\]

Thus:

\[
\psi'(u)=\psi(u)\frac{-2u}{d^2}.
\]

Let:

\[
p(u)=\frac{-2u}{d^2}.
\]

Then:

\[
\psi''(u)=\psi'(u)p(u)+\psi(u)p'(u)
=
\psi(u)(p(u)^2+p'(u)).
\]

Differentiating \(p(u)\) gives:

\[
p'(u)=-\frac{2}{d^2}-\frac{8u^2}{d^3}.
\]

Therefore the stated formula follows.

\[
\square
\]

---

# 4. Theorem X9.2 — interval enclosure principle

If every arithmetic operation in a formula is replaced by a valid interval operation containing the exact image of that operation, then the resulting interval contains the exact value of the full expression.

## Proof

This follows by structural induction on the expression tree.

At each primitive operation, the computed interval contains the exact result of that operation applied to values from the input intervals.

Composing valid enclosures preserves containment.

\[
\square
\]

---

# 5. Certification status

This phase creates primitive interval enclosures under a directed-rounding decimal model.

However, because this is not verified inside a formal proof assistant, the status is:

\[
\boxed{
\texttt{PRIMITIVE\_INTERVAL\_BOUNDS\_CREATED\_NOT\_FORMALLY\_VERIFIED}
}
\]

This is stronger than heuristic grid bounds, but still not a final certified arithmetic entry.

---

# 6. Next phase

Phase X10 should propagate these primitive interval bump bounds into interval bounds for:

\[
\phi,\quad \phi',\quad \phi''
\]

for log-bumps:

\[
\phi(x)=\psi((\log x-c)/w).
\]

Then it should propagate to the corrected pole-cancelled basis.

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not compute a certified arithmetic entry.

It creates primitive interval bump bounds needed for derivative certification.

Exact audit strings:

PHASE_X9_PRIMITIVE_INTERVAL_BUMP_BOUNDS_COMPLETE

DECIMAL_INTERVAL_ARITHMETIC_CREATED

PSI_INTERVAL_BOUND_CREATED

PSI_PRIME_INTERVAL_BOUND_CREATED

PSI_SECOND_INTERVAL_BOUND_CREATED

PRIMITIVE_DERIVATIVE_FORMULAS_PROVED

INTERVAL_ENCLOSURE_PRINCIPLE_RECORDED

PRIMITIVE_INTERVAL_BOUNDS_CREATED_NOT_FORMALLY_VERIFIED

CERTIFIED_ENTRY_NOT_COMPUTED

READY_FOR_PHASE_X10_LOG_BUMP_INTERVAL_DERIVATIVE_BOUNDS

