# Phase 5F Response-Transfer Protocol

## Objective

Convert the dominant empirical counting-remainder mechanism identified in Phase 5E into a deterministic response-transfer inequality and a coordinate-dependent continuum transfer envelope.

## Exact transfer coefficient

\[
\Lambda_n(H,\eta)
=
|f_n(H)|
+
|f_n(B)|
+
\int_H^B|f_n'(t)|dt.
\]

## Sup-norm certificate

\[
|\mathcal T[E]|
\le
\Lambda_n(H,\eta)
\|E\|_\infty.
\]

## L2 certificate

\[
|\mathcal T[E]|
\le
|f(B)||E(B)|
+
|f(H)||E(H)|
+
\|E\|_2\|f'\|_2.
\]

## Continuum envelope

\[
\mathcal L_\eta(c)
=
|\Psi(c)|
+
(1+\eta)^{-2}
|\Psi(c/(1+\eta))|
+
\int_1^{1+\eta}
u^{-3}|J(c/u)|du.
\]

## Matched-scale prediction

\[
H^2\Lambda_n(H,\eta)
\to
\mathcal L_\eta(c).
\]

## Comparative quantity

\[
Q_\eta(c)
=
\frac{|\Phi_\eta(c)|}
{\mathcal L_\eta(c)}.
\]

## Phase 5G validation order

1. validate the explicit J_Li formula symbolically and numerically;
2. validate matched-scale transfer-envelope convergence;
3. compute exact Lambda on dense actual-zero windows;
4. compute empirical E_D sup and L2 norms;
5. test the L-infinity certificate pointwise;
6. test the L2 Holder certificate pointwise;
7. compare certificate tightness;
8. compute Q_eta on empirical-root and generic coordinates;
9. test coordinate-dependent residual prediction against a height-only benchmark;
10. grade P-TRN-001 through P-TRN-005.

## Interpretation boundary

A worst-case deterministic certificate may be mathematically valid but empirically loose.

Failure of P-TRN-003 or P-TRN-005 would not invalidate the transfer inequality.

No RH implication is attached to certificate tightness.
