# Phase 12P — Arithmetic-Side Certificate Roadmap

## Purpose

Phase 12N proved a finite spectral negative-detection theorem.

Phase 12O audited it as a real theorem and a Level 4 conditional breakthrough candidate, but not a completed breakthrough.

The major weakness is that the finite object

\[
Q_Y(g)
\]

uses spectral zero truncation.

A stronger RH-adjacent framework should construct an arithmetic-side finite certificate:

\[
Q_X^{arith}(g)
\]

using only:

1. prime sums;
2. archimedean terms;
3. pole/central terms;
4. certified truncation tails.

---

# 1. Current spectral finite object

The current finite spectral object is

\[
Q_Y(g)
=
\sum_{|\operatorname{Im}\rho|\le Y}
\widehat g(\rho)
\overline{\widehat g(1-\bar\rho)}.
\]

This detects negative infinite obstructions once \(Y\) is sufficiently large.

But it uses zeros.

Therefore it is not yet an arithmetic-only finite certificate.

---

# 2. Desired arithmetic finite object

We want a finite arithmetic object

\[
Q_X^{arith}(g)
\]

such that

\[
|Q_X^{arith}(g)-Q_W(g)|
\le
\varepsilon_X^{arith}(g)
\]

and

\[
\varepsilon_X^{arith}(g)\to0.
\]

For finite test classes,

\[
\sup_{g\in\mathcal F_R^{(m)}}
|Q_X^{arith}(g)-Q_W(g)|
\le
\varepsilon_X^{arith}(R,m)
\to0.
\]

This would allow finite arithmetic certificates to detect negative infinite Weil-form obstructions.

---

# 3. Explicit formula decomposition

The project’s extracted Bombieri-style functional has the form

\[
T[F]
=
I_0[F]
+
I_0[F^*]
-
P[F]
-
C[F]
-
A[F],
\]

where the terms correspond to:

1. integral/central terms;
2. prime sum;
3. constant/pole term;
4. archimedean correction.

More concretely, the extracted expression is:

\[
T[F]
=
\int_0^\infty F(x)\,dx
+
\int_0^\infty F^*(x)\,dx
-
\sum_{n=1}^{\infty}\Lambda(n)\{F(n)+F^*(n)\}
-
(\log 4\pi+\gamma_E)F(1)
-
\int_1^\infty
\left(
F(x)+F^*(x)-\frac{2F(1)}{x}
\right)
\frac{x\,dx}{x^2-1}.
\]

For the Weil quadratic form,

\[
F=F_g=g*g^*.
\]

Thus

\[
Q_W(g)=T[g*g^*].
\]

---

# 4. Arithmetic truncation by prime cutoff

Let \(X>1\).

Define the truncated prime term:

\[
P_X[F]
=
\sum_{1\le n\le X}\Lambda(n)\{F(n)+F^*(n)\}.
\]

Define the prime tail:

\[
P_{>X}[F]
=
\sum_{n>X}\Lambda(n)\{F(n)+F^*(n)\}.
\]

Then

\[
P[F]=P_X[F]+P_{>X}[F].
\]

The arithmetic certificate must bound:

\[
|P_{>X}[F_g]|.
\]

---

# 5. Arithmetic finite certificate candidate

Define

\[
Q_X^{arith}(g)
=
\int_0^\infty F_g(x)\,dx
+
\int_0^\infty F_g^*(x)\,dx
-
P_X[F_g]
-
(\log 4\pi+\gamma_E)F_g(1)
-
\int_1^\infty
\left(
F_g(x)+F_g^*(x)-\frac{2F_g(1)}{x}
\right)
\frac{x\,dx}{x^2-1}.
\]

Then the only missing term relative to \(Q_W(g)\) is the prime tail:

\[
Q_W(g)-Q_X^{arith}(g)
=
-P_{>X}[F_g].
\]

Therefore

\[
|Q_W(g)-Q_X^{arith}(g)|
=
|P_{>X}[F_g]|.
\]

This is the first arithmetic-certificate target.

---

# 6. Compact-support advantage

For log-smooth compact basis functions,

\[
g(x)=\psi(\log x)
\]

with

\[
\psi\in C_c^\infty(\mathbb R),
\]

the support of \(g\) is compact in \((0,\infty)\).

If

\[
\operatorname{supp}(g)\subset[e^{-B},e^B],
\]

then \(g^*\) is also compactly supported.

The multiplicative convolution

\[
F_g=g*g^*
\]

is also compactly supported in a bounded multiplicative interval.

Therefore there exists \(M_g\) such that

\[
F_g(n)=0
\]

and

\[
F_g^*(n)=0
\]

for all integers

\[
n>M_g.
\]

This means the prime sum may actually become finite for compactly supported \(F_g\).

This is potentially powerful.

---

# Theorem 12P.1 — Compact support makes the prime sum finite

Assume \(g\) has compact support in

\[
[a,b]\subset(0,\infty).
\]

Then \(g^*\) has compact support in

\[
[1/b,1/a].
\]

Therefore

\[
F_g=g*g^*
\]

has compact support in

\[
[a/b,b/a].
\]

Consequently,

\[
F_g(n)=0
\]

for all integers

\[
n>b/a.
\]

Also, if \(F_g^*\) is compactly supported in the reciprocal interval, then

\[
F_g^*(n)=0
\]

for all sufficiently large \(n\).

Thus the prime sum

\[
\sum_{n=1}^{\infty}\Lambda(n)\{F_g(n)+F_g^*(n)\}
\]

has only finitely many nonzero terms.

## Proof

Since \(g\) is supported in \([a,b]\), \(g^*(x)=x^{-1}\overline{g(1/x)}\) is nonzero only when

\[
1/x\in[a,b].
\]

Thus

\[
x\in[1/b,1/a].
\]

So

\[
\operatorname{supp}(g^*)\subset[1/b,1/a].
\]

For multiplicative convolution,

\[
F_g(x)=\int_0^\infty g(y)g^*(x/y)\frac{dy}{y}.
\]

A nonzero contribution requires

\[
y\in[a,b]
\]

and

\[
x/y\in[1/b,1/a].
\]

Thus

\[
x\in y[1/b,1/a].
\]

As \(y\in[a,b]\), this implies

\[
x\in[a/b,b/a].
\]

Hence

\[
\operatorname{supp}(F_g)\subset[a/b,b/a].
\]

The same compact-support reasoning applies to \(F_g^*\).

Therefore only finitely many positive integers \(n\) can lie in the support of \(F_g\) or \(F_g^*\).

\[
\square
\]

---

# 7. Consequence for arithmetic certification

If the compact support is known exactly, then for

\[
X>\max \operatorname{supp}(F_g,F_g^*),
\]

the prime tail is zero:

\[
P_{>X}[F_g]=0.
\]

Therefore

\[
Q_X^{arith}(g)=Q_W(g)
\]

exactly, modulo:

1. source-normalization confirmation;
2. exact evaluation of archimedean integrals;
3. numerical integration certification;
4. primary-source convention validation.

This suggests a powerful route:

\[
\boxed{
\text{compact support can eliminate prime-tail error}
}
\]

for the chosen finite test class.

---

# 8. Remaining arithmetic-side difficulties

Even if the prime sum is finite, the arithmetic certificate still needs:

## 8.1 Archimedean integral certification

The term

\[
\int_1^\infty
\left(
F_g(x)+F_g^*(x)-\frac{2F_g(1)}{x}
\right)
\frac{x\,dx}{x^2-1}
\]

must be evaluated or bounded rigorously.

Because \(F_g\) and \(F_g^*\) are compactly supported, this integral may reduce to a finite interval plus a known tail from the subtraction term.

But the singular behavior near \(x=1\) must be handled carefully.

## 8.2 Source convention validation

The exact sign and normalization must still be confirmed from a primary source.

## 8.3 Numerical certification

If computed numerically, all integrals and prime sums must use certified error bounds.

## 8.4 Function-class construction

The basis functions must be explicitly represented, not just abstract \(C_c^\infty\) objects, if we want computable certificates.

---

# 9. Arithmetic roadmap

The arithmetic-side certificate requires the following phases:

## Phase 12Q — Compact Support Arithmetic Tail Theorem

Prove the prime tail is zero for compactly supported \(F_g\) above an explicit cutoff.

## Phase 12R — Archimedean Integral Reduction

Show the archimedean integral reduces to a finite, certified integral plus an explicit analytic term.

## Phase 12S — Certified Arithmetic Matrix Entries

Define matrix entries

\[
M_{ij}^{arith}=T[\phi_i*\phi_j^*]
\]

using prime sums and archimedean integrals.

## Phase 12T — Arithmetic Finite-Class Certificate

Prove that for

\[
g=\sum a_j\phi_j,
\]

\[
Q^{arith}(g)=a^*M^{arith}a
\]

matches \(Q_W(g)\) under source conventions.

## Phase 12U — Interval Arithmetic Implementation

Implement certified bounds for every matrix entry.

## Phase 12V — Arithmetic Negative-Obstruction Detection

If an interval-certified arithmetic matrix has a negative Rayleigh quotient below margin, prove a negative Weil-form obstruction.

---

# 10. Honest status

Phase 12P is a roadmap plus one useful theorem: compact support makes the prime sum finite.

It does not yet construct the full arithmetic certificate.

But it identifies the arithmetic path and shows that compact support removes one major infinite tail.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove a complete arithmetic-only finite certificate.

This phase does not establish novelty.

Exact audit strings:

ARITHMETIC_CERTIFICATE_ROADMAP_COMPLETE

ARITHMETIC_Q_X_DEFINED

PRIME_TRUNCATION_DEFINED

PRIME_TAIL_DEFINED

COMPACT_SUPPORT_PRIME_SUM_FINITE_PROVED

PRIME_TAIL_CAN_BE_ZERO_FOR_COMPACT_SUPPORT

ARCHIMEDEAN_CERTIFICATION_REMAINS

ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE

LEVEL4_BREAKTHROUGH_CANDIDATE_STILL_CONDITIONAL

