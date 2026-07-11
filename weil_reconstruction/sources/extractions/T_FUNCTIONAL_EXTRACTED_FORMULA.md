# Extracted Bombieri T[f] Formula

## Function class

\[
f\in C_0^\infty((0,\infty)).
\]

## Involution

\[
f^*(x)=\frac1x f\left(\frac1x\right).
\]

## Mellin transform

\[
f(s)=\int_0^\infty f(x)x^{s-1}\,dx.
\]

## Functional

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

## Zero-side identity

\[
T[f]=T[f^*]=\sum_\rho f(\rho).
\]

## Quadratic positivity object

\[
T[f*f^*].
\]

## RH-equivalence statement

RH is equivalent to

\[
T[f*f^*]\ge0
\]

on

\[
C_0^\infty((0,\infty)),
\]

with equality only if \(f\equiv0\).

## Status

Known theorem reconstructed from Bombieri.

No novelty claim.

No RH proof claim.

