# Phase 5C Actual Zeta-Zero Window Response Report

## Objective

Test whether the individual Li quadratic zero-coordinate response survives aggregation over finite windows of numerically computed Riemann zeta zero ordinates through the smooth-density window profile frozen in Phase 5A.

---

# 1. Discrete response

For complete finite zero windows,

\[
\mathcal W_n(H,\eta)
=
\sum_{H\le\gamma_j\le(1+\eta)H}
\chi_n^{\mathrm{Li}}(\gamma_j).
\]

The normalized discrete response was

\[
Y(H,\eta,c)
=
\frac H{\log H}
\mathcal W_n(H,\eta).
\]

Requested real similarity coordinates were converted to integer Li indices by

\[
n
=
\max(
1,
\operatorname{round}(c_{\mathrm{req}}H)
),
\]

and all continuum comparisons used the realized coordinate

\[
c_{\mathrm{real}}=n/H.
\]

---

# 2. Frozen Model A

The Phase 5A prediction was

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

P-ZETA-002 was graded against this model.

---

# 3. Diagnostic Model B

The finite-height smooth-density benchmark retained the full leading logarithmic density factor:

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

Model B was diagnostic and did not replace the frozen prediction.

---

# 4. Occupancy at least 10

Window count:

\[
29.
\]

Empirical root count:

\[
174.
\]

Mean frozen-profile NRMSE:

\[
0.3142755225630183\ldots
\]

Mean finite-height NRMSE:

\[
0.0588750595187807\ldots
\]

Mean frozen-profile correlation:

\[
0.9950559882727908\ldots
\]

Mean finite-height correlation:

\[
0.9962909002400568\ldots
\]

Mean frozen-profile sign agreement:

\[
0.9896551724137931\ldots
\]

Mean finite-height sign agreement:

\[
0.9900862068965517\ldots
\]

Frozen window-root win rate versus individual blind scales:

\[
1.0.
\]

Finite-height window-root win rate versus individual blind scales:

\[
1.0.
\]

---

# 5. Occupancy at least 25

Window count:

\[
18.
\]

Empirical root count:

\[
108.
\]

Mean frozen-profile NRMSE:

\[
0.3090512445608752\ldots
\]

Mean finite-height NRMSE:

\[
0.0382322639415506\ldots
\]

Mean frozen-profile correlation:

\[
0.9978046431132978\ldots
\]

Mean finite-height correlation:

\[
0.9985902838731698\ldots
\]

Mean frozen-profile sign agreement:

\[
0.9916666666666667\ldots
\]

Mean finite-height sign agreement:

\[
0.9916666666666667\ldots
\]

Frozen window-root win rate versus individual blind scales:

\[
1.0.
\]

Finite-height window-root win rate versus individual blind scales:

\[
1.0.
\]

---

# 6. Occupancy at least 50

Window count:

\[
10.
\]

Empirical root count:

\[
60.
\]

Mean frozen-profile NRMSE:

\[
0.3040702534122135\ldots
\]

Mean finite-height NRMSE:

\[
0.0362570432765250\ldots
\]

Mean frozen-profile correlation:

\[
0.9982160058599440\ldots
\]

Mean finite-height correlation:

\[
0.9986595036992373\ldots
\]

Mean frozen-profile sign agreement:

\[
0.9925.
\]

Mean finite-height sign agreement:

\[
0.9925.
\]

Frozen window-root win rate versus individual blind scales:

\[
1.0.
\]

Finite-height window-root win rate versus individual blind scales:

\[
1.0.
\]

---

# 7. Occupancy trend

The mean frozen-profile correlation increased across the reported occupancy thresholds:

\[
0.995056
\rightarrow
0.997805
\rightarrow
0.998216.
\]

The finite-height benchmark correlation similarly increased:

\[
0.996291
\rightarrow
0.998590
\rightarrow
0.998660.
\]

Thus stronger profile-shape agreement was observed in more highly populated zero-window subsets.

This is a finite computational observation.

No asymptotic convergence theorem is claimed.

---

# 8. Frozen-profile amplitude qualification

The high-occupancy frozen-profile mean correlation was approximately

\[
0.998216
\]

and mean sign agreement was

\[
0.9925.
\]

However, mean NRMSE remained approximately

\[
0.304070.
\]

Therefore the frozen leading profile reproduced curve shape and sign structure very strongly while retaining substantial finite-height amplitude discrepancy.

P-ZETA-002 is graded:

PASS WITH FINITE-HEIGHT AMPLITUDE QUALIFICATION.

---

# 9. Finite-height density correction

For occupancy at least 50, the finite-height benchmark reduced mean NRMSE from

\[
0.3040702534\ldots
\]

to

\[
0.0362570433\ldots.
\]

The NRMSE improvement factor was approximately

\[
8.39.
\]

Thus retaining the finite-height logarithmic density factor explains a large fraction of the accessible-height amplitude discrepancy.

The finite-height benchmark also slightly improved mean correlation.

---

# 10. Response-zero geometry

Across all reported occupancy thresholds, empirical response roots preferred window-profile roots over individual Li blind scales at a protocol win rate of

\[
1.0.
\]

For the high-occupancy subset, all 60 recorded empirical response roots were closer to window-profile roots than to individual blind scales under the nearest-root metric.

Therefore the data support the window-smearing prediction.

The individual blind-scale structure is not preserved pointwise under positive-width zero-window aggregation.

Instead, empirical response-zero geometry tracks the window-level profile.

---

# 11. Frozen prediction scorecard

## P-ZETA-001

Prediction:

Positive-width actual-zero windows generically smear individual Li response blind scales.

Result:

PASS.

Evidence:

Window-profile roots beat individual blind scales under the nearest-root metric for every recorded empirical root in all reported occupancy subsets.

---

## P-ZETA-002

Prediction:

After H/log H normalization, high-zero truncated window susceptibility broadly agrees with the frozen smooth-density profile.

Result:

PASS WITH FINITE-HEIGHT AMPLITUDE QUALIFICATION.

Evidence:

High-occupancy mean correlation approximately 0.998216 and mean sign agreement 0.9925.

Qualification:

High-occupancy mean NRMSE remained approximately 0.304070.

---

## P-ZETA-003

Prediction:

Empirical response-zero locations track window-profile zeros more closely than individual blind scales once windows contain sufficiently many zero ordinates.

Result:

PASS.

Evidence:

Window-profile root win rate versus individual blind scales was 1.0 at all reported occupancy thresholds.

---

# 12. Main project conclusion

The individual Li quadratic-response profile does not survive positive-width actual-zero aggregation pointwise.

Instead, the aggregate discrete response exhibits shape and response-zero geometry strongly consistent with the smooth-density window profile

\[
\Phi_\eta.
\]

The project therefore observes the response transformation

\[
\Psi_{\mathrm{Li}}
\longrightarrow
\Phi_\eta
\]

when passing from one-orbit susceptibility to positive-width finite windows of computed critical-line zeta zero ordinates.

At accessible heights, the finite-height logarithmic density factor is required for accurate amplitude prediction.

---

# 13. Interpretation boundary

This experiment uses the first 500 critical-line zero ordinates in the project computational dataset.

No theorem of discrete convergence to the smooth-density profile has been established.

No off-critical zero response was tested.

No new RH criterion was derived.

No zero-free region or Li positivity theorem follows from the experiment.

Agreement with the response profile is not a proof of RH.
