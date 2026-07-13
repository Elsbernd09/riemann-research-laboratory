# Phase X13 — Partial Single-Entry Interval Certificate

## Purpose

Phase X12 produced an \(F''\) bound for:

\[
F=\Phi*\Phi^*.
\]

Phase X13 feeds that bound into the X6 midpoint quadrature theorem to create a partial interval certificate for the central integral:

\[
\int F(x)\,dx.
\]

This is a partial certificate for the single-entry pipeline:

\[
M_{00}=T_{BL}[F].
\]

It is not yet a full certified arithmetic entry.

---

# 1. Certified quadrature input

The X6 theorem states:

\[
\left|
\int_a^b h(x)\,dx-Q_N(h)
\right|
\le
\frac{(b-a)^3}{24N^2}
\sup_{x\in[a,b]}|h''(x)|.
\]

For \(h=F\), X12 provides a candidate upper bound:

\[
\|F''\|_\infty \le B_2.
\]

Therefore:

\[
\int_a^b F(x)\,dx
\in
[Q_N(F)-E,\ Q_N(F)+E],
\]

where:

\[
E=\frac{(b-a)^3}{24N^2}B_2.
\]

---

# 2. What is certified partially

This phase creates a proof-pattern interval for:

\[
\int F(x)\,dx.
\]

It uses:

1. compact support from X4;
2. singularity-free central integral;
3. midpoint quadrature theorem from X6;
4. \(F''\) bound from X12.

---

# 3. What is not certified yet

The full entry:

\[
M_{00}=T_{BL}[F]
\]

also needs:

1. tilde integral certificate;
2. finite prime-side certificate;
3. constant term certificate;
4. archimedean continuous-extension certificate;
5. coefficient-solve certificate for \(\alpha,\beta\);
6. outward-rounded arithmetic review.

Therefore the final status is:

\[
\boxed{
\texttt{PARTIAL\_SINGLE\_ENTRY\_INTERVAL\_CERTIFICATE}
}
\]

not:

\[
\texttt{CERTIFIED\_ARITHMETIC\_ENTRY}.
\]

---

# Theorem X13.1 — central integral partial certificate

Assume:

\[
\operatorname{supp}(F)\subset[a,b],
\]

and:

\[
\|F''\|_\infty\le B_2.
\]

Let \(Q_N(F)\) be midpoint quadrature on \([a,b]\). Then:

\[
\int_a^b F(x)\,dx
\in
\left[
Q_N(F)-\frac{(b-a)^3B_2}{24N^2},
Q_N(F)+\frac{(b-a)^3B_2}{24N^2}
\right].
\]

## Proof

Apply the midpoint quadrature theorem from Phase X6 with \(h=F\).

\[
\square
\]

---

# Theorem X13.2 — partial certificate is not full entry certification

A certificate for only:

\[
\int F(x)\,dx
\]

does not certify:

\[
T_{BL}[F].
\]

## Proof

The locked Bombieri–Lagarias functional contains additional terms:

1. \(\int \widetilde F(x)\,dx\);
2. the finite prime sum;
3. the constant term;
4. the archimedean integral.

If only the central integral is interval-certified, the total functional is not yet interval-certified.

\[
\square
\]

---

# 4. Breakthrough relevance

This is the first phase that creates a genuine partial interval certificate inside the \(M_{00}\) pipeline.

That is progress toward the breakthrough target.

But it is still not a breakthrough.

The next target is to extend this interval-certificate pattern to every term of \(T_{BL}[F]\).

---

# 5. Next phase

Phase X14 should certify the tilde integral:

\[
\int \widetilde F(x)\,dx.
\]

This should be structurally similar to X13 but uses the transformed support:

\[
\operatorname{supp}(\widetilde F)\subset [B^{-1},A^{-1}].
\]

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not compute a fully certified arithmetic entry.

It creates a partial interval certificate for the central integral term only.

Exact audit strings:

PHASE_X13_PARTIAL_SINGLE_ENTRY_INTERVAL_CERTIFICATE_COMPLETE

CENTRAL_INTEGRAL_INTERVAL_CERTIFICATE_CREATED

MIDPOINT_QUADRATURE_THEOREM_APPLIED_TO_F

F_SECOND_DERIVATIVE_BOUND_USED

PARTIAL_SINGLE_ENTRY_INTERVAL_CERTIFICATE_CREATED

FULL_T_BL_ENTRY_NOT_CERTIFIED

CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED

READY_FOR_PHASE_X14_TILDE_INTEGRAL_INTERVAL_CERTIFICATE

