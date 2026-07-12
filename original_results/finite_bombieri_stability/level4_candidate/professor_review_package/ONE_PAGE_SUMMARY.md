# One-Page Summary

## Project

I developed a conditional finite-dimensional framework around a provisional Weil/Bombieri quadratic form connected to the Riemann Hypothesis.

The project studies how an infinite Weil-form obstruction could be detected by finite approximations on controlled finite test classes.

## Main theorem-level result

Let

\[
\mathcal F_R^{(m)}
=
\left\{
g=\sum_{j=1}^{m}a_j\phi_j:\|a\|_2\le R
\right\},
\]

where

\[
\phi_j(x)=\psi_j(\log x),
\qquad
\psi_j\in C_c^\infty(\mathbb R).
\]

Under provisional Weil/Bombieri conventions, define

\[
Q_W(g)=T[g*g^*].
\]

The project proves that finite spectral truncations

\[
Q_Y(g)
=
\sum_{|\operatorname{Im}\rho|\le Y}
\widehat g(\rho)\overline{\widehat g(1-\bar\rho)}
\]

converge uniformly to \(Q_W(g)\) on \(\mathcal F_R^{(m)}\), assuming a classical zero-count shell bound.

Therefore, if

\[
Q_W(g)\le-\eta,
\]

then for sufficiently large \(Y\),

\[
Q_Y(g)<-\eta/2.
\]

## Arithmetic-side work

The project also develops an arithmetic-side certificate roadmap using the explicit formula.

For compactly supported test functions, it proves:

1. \(F_g=g*g^*\) has compact support;
2. the prime sum has an exact finite cutoff;
3. the archimedean tail has an explicit logarithmic form;
4. arithmetic matrix entries can be decomposed into finite prime, central, constant, and reduced archimedean components.

A toy floating-point arithmetic matrix prototype was implemented, but certified interval arithmetic for the true entries is not yet complete.

## Honest boundary

This project does not prove RH, disprove RH, prove a new equivalent RH criterion, prove the full Weil positivity theorem, or establish novelty.

It is a conditional research framework and prototype intended for expert review.

