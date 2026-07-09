# Phase 5D Zeta-Window Discrepancy Decomposition Protocol

## Objective

Decompose the Phase 5C discrete-minus-finite-height-profile residual into:

1. empirical zero-counting fluctuation;
2. Li susceptibility kernel-asymptotic truncation.

## Exact empirical counting function

\[
N_D(T)
=
\#\{
\gamma_j\in D:
\gamma_j\le T
\}.
\]

## Smooth counting model

\[
M(T)
=
\frac{T}{2\pi}\log(T/(2\pi))
-
\frac{T}{2\pi}
+
\frac78.
\]

## Empirical remainder

\[
E_D(T)
=
N_D(T)-M(T).
\]

## Exact smooth response

\[
S_{\mathrm{exact}}
=
\int_H^B
\chi_n^{Li}(t)
M'(t)\,dt.
\]

## Phase 5C profile response

\[
S_{\mathrm{profile}}
=
\int_H^B
t^{-2}
\Psi_{Li}(n/t)
M'(t)\,dt.
\]

## Kernel remainder

\[
R_{\mathrm{kernel}}
=
S_{\mathrm{exact}}
-
S_{\mathrm{profile}}.
\]

## Counting remainder

\[
R_{\mathrm{count}}
=
\mathcal W_n
-
S_{\mathrm{exact}}.
\]

The Stieltjes formula provides an independent evaluation through endpoint terms and the E_D-weighted derivative integral.

## Required validations

Phase 5E must:

1. compute the direct discrete sum;
2. compute S_exact;
3. compute S_profile;
4. compute direct R_count = W - S_exact;
5. compute Stieltjes R_count independently;
6. verify closure of the exact decomposition;
7. compute R_kernel;
8. stratify RMS component sizes by occupancy;
9. estimate height slopes on absolute normalized component magnitudes;
10. isolate the left-endpoint atom;
11. grade P-DEC-001 through P-DEC-004.

## Interpretation boundary

The decomposition is exact for the finite empirical dataset.

The asymptotic scale hierarchy is a theoretical prediction to be tested.

No new theorem about the classical zero-counting remainder is asserted.
