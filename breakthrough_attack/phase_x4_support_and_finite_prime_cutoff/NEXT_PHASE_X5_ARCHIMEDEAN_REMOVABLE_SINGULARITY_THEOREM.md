# Next Phase X5 — Archimedean Removable Singularity Theorem

## Goal

Handle the archimedean integral singularity at \(x=1\):

\[
\left(F(x)+\widetilde F(x)-2x^{-2}F(1)\right)\frac{x}{x^2-1}.
\]

## Required

1. prove numerator vanishes at \(x=1\);
2. compute the removable limiting value;
3. rewrite the integral using a continuous integrand;
4. prepare it for rigorous interval quadrature.

## Why this matters

Without this theorem, certified interval arithmetic cannot safely integrate the archimedean term.
