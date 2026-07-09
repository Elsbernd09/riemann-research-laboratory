# Phase 5G Transfer-Envelope Validation and Explanatory-Power Protocol

## P-TRN-001

Matched-scale convergence is tested by comparing

\[
H^2\Lambda_n(H,\eta)
\]

with

\[
\mathcal L_\eta(c)
\]

for three frozen (c, eta) cases over increasing H.

## P-TRN-002

At every dense-window decomposition point, test

\[
|R_{\mathrm{count}}-R_{\mathrm{atom}}|
\le
\Lambda_n(H,\eta)\|E_D\|_\infty.
\]

Pass rule:

Pointwise certificate pass rate must equal 1.

## P-TRN-003

Compare the L2 Holder certificate with the L-infinity variation certificate.

Pass rule:

The L2 certificate must be tighter at more than 50 percent of tested dense-window points.

## P-TRN-004

Evaluate

\[
Q_\eta(c)
=
|\Phi_\eta(c)|/\mathcal L_\eta(c)
\]

at corrected empirical response roots.

Generic coordinates are realized Phase 5C grid coordinates at least 0.5 away from every empirical response root in the same window.

Pass rule:

Median empirical-root Q must be less than median generic-coordinate Q.

## P-TRN-005

Empirical target:

\[
Y_{\mathrm{count}}
=
\left|
\frac H{\log H}
R_{\mathrm{count}}
\right|.
\]

Continuum transfer predictor:

\[
P_{\mathrm{tr}}
=
\frac{
|\Psi_{Li}(c)|
+
\mathcal L_\eta(c)\|E_D\|_\infty
}{
H\log H
}.
\]

Height-only baseline:

\[
P_H=1/H.
\]

Metric:

Pearson correlation after taking natural logarithms of positive magnitudes.

Pass rule:

The log residual correlation with P_tr must exceed the log residual correlation with 1/H.

## Interpretation boundary

A failed explanatory-power prediction does not invalidate the deterministic transfer inequality.

Absolute-value envelopes can be mathematically correct and empirically loose because they erase signed cancellation.
