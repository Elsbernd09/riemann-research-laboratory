# Phase 8H — Full Bombieri T[f] Formula Extraction

## Purpose

Phase 8G created the extraction worksheet for Bombieri's full linear functional

\[
T[f].
\]

Phase 8H fills the worksheet from Bombieri's source text.

This is not a proof of RH.

This is not a new Weil criterion.

This is a source-grounded extraction of a known classical formula.

---

# 1. Source

Enrico Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**, Section 2 and Section 3.

Bombieri states the Guinand-Weil explicit formula for

\[
f\in C_0^\infty((0,\infty)).
\]

He defines

\[
f^*(x)=\frac1x f\left(\frac1x\right).
\]

He defines the Mellin transform

\[
f(s)=\int_0^\infty f(x)x^{s-1}\,dx.
\]

---

# 2. Extracted full functional

Bombieri Theorem 2 defines the linear functional

\[
T[f]
\]

by

\[
T[f]
=
\int_0^\infty f(x)\,dx
+
\int_0^\infty f^*(x)\,dx
-
\sum_{n=1}^{\infty}
\Lambda(n)\{f(n)+f^*(n)\}
-
(\log 4\pi+\gamma_E)f(1)
-
\int_1^\infty
\left(
f(x)+f^*(x)-\frac{2}{x}f(1)
\right)
\frac{x\,dx}{x^2-1}.
\]

Here \(\gamma_E\) denotes Euler's constant.

---

# 3. Zero-side identity

Bombieri states

\[
T[f]=T[f^*]=\sum_\rho f(\rho),
\]

where the sum ranges over all complex zeros of the Riemann zeta function.

This is the source-grounded zero-side identity for the selected reconstruction path.

---

# 4. Quadratic object

Bombieri's quadratic object is

\[
T[f*f^*].
\]

The Riemann Hypothesis is equivalent to

\[
T[f*f^*]\ge0
\]

on

\[
C_0^\infty((0,\infty)),
\]

with equality only if

\[
f\equiv0.
\]

---

# 5. Term-by-term decomposition

## Test-function class

\[
f\in C_0^\infty((0,\infty)).
\]

Status: LOCKED.

## Involution

\[
f^*(x)=\frac1x f\left(\frac1x\right).
\]

Status: LOCKED.

## Mellin transform

\[
f(s)=\int_0^\infty f(x)x^{s-1}\,dx.
\]

Status: LOCKED.

## Integral mass terms

\[
\int_0^\infty f(x)\,dx
+
\int_0^\infty f^*(x)\,dx.
\]

Status: LOCKED.

## Prime-side term

\[
-\sum_{n=1}^{\infty}
\Lambda(n)\{f(n)+f^*(n)\}.
\]

Status: LOCKED.

## Constant/pole/gamma normalization term

\[
-(\log 4\pi+\gamma_E)f(1).
\]

Status: LOCKED.

## Archimedean integral term

\[
-
\int_1^\infty
\left(
f(x)+f^*(x)-\frac{2}{x}f(1)
\right)
\frac{x\,dx}{x^2-1}.
\]

Status: LOCKED.

## Zero-side identity

\[
T[f]=\sum_\rho f(\rho).
\]

Status: LOCKED.

---

# 6. Alternative gamma-factor representation

Bombieri also gives the last two terms in an alternative complex-integral form involving

\[
-\log(\pi)f(1)
+
\frac{1}{2\pi}
\int_{-\infty}^{\infty}
\Re
\frac{\Gamma'}{\Gamma}
\left(
\frac14+\frac{iv}{2}
\right)
f\left(\frac12+iv\right)\,dv.
\]

This alternative form is useful for Fourier-side reconstruction but is not yet used for code.

Status: PARTIAL for future transform work.

---

# 7. Implementation status

The full symbolic formula for \(T[f]\) is now source-extracted.

However, exact finite-rank Weil code remains blocked because the following are still not locked:

1. exact finite truncation model;
2. Fourier-side infinite quadratic matrix;
3. finite matrix entries;
4. eigenvalue theorem dependencies;
5. convergence from finite truncations to the infinite object.

Thus:

\[
\text{T-functional formula: LOCKED}
\]

but

\[
\text{finite-rank Weil implementation: STILL BLOCKED}.
\]

---

# 8. Boundary

This phase reconstructs a known formula from Bombieri.

No RH proof.

No new Weil criterion.

No novelty claim.

