# Phase X17 — Archimedean Integral Interval Certificate

## Purpose

Phase X17 creates the interval-certificate structure for the archimedean term:

\[
A(F)=
\int_1^\infty
\left(F(x)+\widetilde F(x)-2x^{-2}F(1)\right)
\frac{x}{x^2-1}\,dx.
\]

Phase X5 proved the removable value at \(x=1\):

\[
A_F(1)=\frac32F(1).
\]

Thus the integrand is evaluated through its continuous extension.

---

# 1. Support truncation

If:

\[
\operatorname{supp}(F)\subset[A,B],
\]

then the archimedean integrand vanishes outside the combined support of \(F(x)\), \(\widetilde F(x)\), and \(F(1)\)-term interaction.

For the implemented certificate, we integrate over the finite interval:

\[
[1,\max(B,A^{-1})].
\]

---

# 2. Interval certificate structure

Let:

\[
H_F(x)=
\left(F(x)+\widetilde F(x)-2x^{-2}F(1)\right)
\frac{x}{x^2-1}
\]

for \(x\ne1\), and:

\[
H_F(1)=\frac32F(1).
\]

If:

\[
\|H_F''\|_\infty\le B_2^A,
\]

then midpoint quadrature gives:

\[
\int_1^R H_F(x)\,dx
\in
\left[
Q_N(H_F)-\frac{(R-1)^3B_2^A}{24N^2},
Q_N(H_F)+\frac{(R-1)^3B_2^A}{24N^2}
\right].
\]

---

# 3. Honest blocker

This phase uses a conservative archimedean derivative-bound placeholder built from the existing convolution derivative-bound scale.

The singularity is structurally removed.

But the exact bound for:

\[
\|H_F''\|_\infty
\]

is not yet rigorously derived.

Therefore the status is:

\[
\boxed{
\texttt{ARCHIMEDEAN_INTERVAL_CERTIFICATE_DERIVATIVE_BOUND_INCOMPLETE}
}
\]

---

# Theorem X17.1 — archimedean interval certificate theorem

Assume the continuous extension \(H_F\) satisfies:

\[
\|H_F''\|_\infty\le B_2^A
\]

on \([1,R]\). Then midpoint quadrature gives:

\[
\int_1^R H_F(x)\,dx
\in
\left[
Q_N(H_F)-\frac{(R-1)^3B_2^A}{24N^2},
Q_N(H_F)+\frac{(R-1)^3B_2^A}{24N^2}
\right].
\]

## Proof

Apply the X6 midpoint quadrature theorem to \(h=H_F\) on \([1,R]\).

\[
\square
\]

---

# Theorem X17.2 — archimedean certificate remains incomplete without a rigorous \(H_F''\) bound

If the bound for \(\|H_F''\|_\infty\) is only a conservative placeholder and not derived from interval-enclosed formulas, then the archimedean interval is not fully certified.

## Proof

The X6 certified quadrature theorem requires a proven upper bound for the second derivative.

A placeholder bound does not establish the theorem hypothesis.

Therefore the archimedean certificate structure exists, but full certification remains incomplete.

\[
\square
\]

---

# 4. Remaining path

After X17, every term of \(T_{BL}[F]\) has a certificate structure:

1. central integral;
2. tilde integral;
3. prime side;
4. constant term;
5. archimedean integral.

The next phase should assemble these into a full \(M_{00}\) interval-certificate object, while honestly marking unresolved gates.

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not compute a fully certified arithmetic entry.

It creates the archimedean integral interval-certificate structure.

Exact audit strings:

PHASE_X17_ARCHIMEDEAN_INTEGRAL_INTERVAL_CERTIFICATE_COMPLETE

ARCHIMEDEAN_CONTINUOUS_EXTENSION_USED

ARCHIMEDEAN_SUPPORT_TRUNCATION_CREATED

ARCHIMEDEAN_INTERVAL_CERTIFICATE_CREATED

MIDPOINT_QUADRATURE_THEOREM_APPLIED_TO_ARCHIMEDEAN_TERM

ARCHIMEDEAN_DERIVATIVE_BOUND_INCOMPLETE

FULL_T_BL_ENTRY_NOT_CERTIFIED

CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED

READY_FOR_PHASE_X18_ASSEMBLE_FULL_M00_INTERVAL_CERTIFICATE

