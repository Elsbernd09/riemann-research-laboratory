# Phase 5C Actual Zeta-Zero Window Response Experiment Protocol

## Objective

Test the frozen Phase 5A smooth-density Li window-response profile against finite sums over the first-500-zero computational dataset.

## Discrete object

\[
\mathcal W_n(H,\eta)
=
\sum_{H\le\gamma_j\le(1+\eta)H}
\chi_n^{\mathrm{Li}}(\gamma_j).
\]

The normalized discrete response is

\[
Y(H,\eta,c)
=
\frac H{\log H}
\mathcal W_n(H,\eta).
\]

## Integer-index realization

For requested similarity coordinate \(c_{\mathrm{req}}\),

\[
n
=
\max(
1,
\operatorname{round}(c_{\mathrm{req}}H)
).
\]

The realized coordinate is

\[
c_{\mathrm{real}}
=
n/H.
\]

All continuum comparisons use \(c_{\mathrm{real}}\).

## Model A

Frozen Phase 5A leading profile:

\[
\Phi_\eta(c)
=
\frac{c}{\pi}
\left[
(1+\eta)^{-2}
\sin(c/(1+\eta))
-
\sin c
\right].
\]

P-ZETA-002 is graded against Model A.

## Model B

Finite-height smooth-density benchmark:

\[
\Phi_{\eta,H}^{FH}(c)
=
\frac{1}{2\pi\log H}
\int_1^{1+\eta}
u^{-2}
\Psi_{\mathrm{Li}}(c/u)
\log(uH/(2\pi))
\,du.
\]

Model B is diagnostic.

It does not replace the frozen prediction.

## c-grid

\[
0.25
\le
c_{\mathrm{req}}
\le
20
\]

with step

\[
0.25.
\]

## Metrics

For each complete window:

- normalized root mean squared error;
- Pearson correlation;
- sign agreement;
- interpolated empirical response roots.

## Root comparison

Empirical response roots are compared with:

1. frozen smooth-density window-profile roots;
2. finite-height benchmark roots;
3. individual-kernel blind scales.

P-ZETA-003 is tested by asking whether empirical roots lie closer to window-profile roots than to individual blind scales.

## Occupancy stratification

Primary summaries are reported for:

\[
N_{\mathrm{window}}\ge10,
\]

\[
N_{\mathrm{window}}\ge25,
\]

and

\[
N_{\mathrm{window}}\ge50.
\]

The strongest initial continuum test uses the final subset.

## Interpretation boundary

This is a finite computational experiment.

Agreement does not imply RH.

Disagreement does not imply failure of RH.

The experiment tests a project-defined response statistic against a frozen smooth-density approximation.
