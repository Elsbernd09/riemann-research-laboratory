# Frozen Zeta-Window Discrepancy Predictions

## Phase 5D

These predictions are frozen before the empirical decomposition experiment.

---

## P-DEC-001

Prediction:

The numerical decomposition

\[
\mathcal W_n-S_{\mathrm{profile}}
=
R_{\mathrm{count}}
+
R_{\mathrm{kernel}}
\]

will close to the declared arbitrary-precision quadrature tolerance.

Interpretation:

This is primarily an implementation and identity validation prediction.

---

## P-DEC-002

Prediction:

In dense and high-occupancy windows, the empirical counting-remainder component will generally exceed the kernel-asymptotic remainder in RMS size.

Rationale:

The candidate normalized scales are O(H^-1) for counting fluctuation and O(H^-2) for kernel truncation.

---

## P-DEC-003

Prediction:

Across increasing window height, the normalized kernel remainder will exhibit a steeper decay trend than the normalized counting remainder.

The project does not require fitted exponents to equal exactly -2 and -1 in the first-500-zero height range.

The prediction concerns relative steepness.

---

## P-DEC-004

Prediction:

Removing the explicit left-endpoint atom from the zero-anchored discrete statistic will improve smooth-model agreement slightly but will not explain most of the remaining finite-height benchmark residual in high-occupancy windows.

---

## Prediction integrity rule

This file must not be modified after the Phase 5E decomposition experiment begins.

Failed predictions remain recorded.
