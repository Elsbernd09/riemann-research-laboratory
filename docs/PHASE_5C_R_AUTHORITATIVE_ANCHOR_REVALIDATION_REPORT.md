# Phase 5C-R Authoritative-Anchor Revalidation Report

## Objective

Revalidate the Phase 5C actual zeta-zero window response experiment after the Phase 5E-R endpoint provenance audit showed that rounded occupancy-file height values were unsafe for reconstructing atomic zero-window endpoints.

---

# 1. Endpoint correction

The original experiment reconstructed

\[
H
\]

from a 60-digit display serialization in the occupancy CSV.

The corrected experiment uses

\[
\texttt{anchor\_zero\_index}
\]

as the provenance key and reconstructs

\[
H
=
\gamma_{\text{anchor zero index}}
\]

directly from the frozen zero dataset.

The original Phase 5C experimental design, coordinate grid, continuum models, metrics, root interpolation, occupancy thresholds, and prediction language were preserved.

No metric was changed after discovering the endpoint bug.

---

# 2. High-occupancy corrected results

For windows with occupancy at least

\[
50,
\]

the corrected experiment contained:

\[
10
\]

windows and

\[
60
\]

empirical response roots.

The corrected mean frozen-profile NRMSE was approximately

\[
\boxed{
0.2996280740.
}
\]

The corrected mean finite-height NRMSE was approximately

\[
\boxed{
0.03598349127.
}
\]

The corrected mean frozen-profile correlation was approximately

\[
\boxed{
0.9986389173.
}
\]

The corrected mean finite-height correlation was approximately

\[
\boxed{
0.9983810756.
}
\]

The corrected mean frozen-profile sign agreement was

\[
\boxed{
0.9975.
}
\]

The corrected mean finite-height sign agreement was

\[
\boxed{
0.9975.
}
\]

The frozen window-profile root win rate versus individual Li blind scales remained

\[
\boxed{
1.0.
}
\]

The finite-height root win rate versus individual Li blind scales remained

\[
\boxed{
1.0.
}
\]

---

# 3. Comparison with original Phase 5C metrics

## Frozen-profile NRMSE

Original:

\[
0.3040702534.
\]

Corrected:

\[
0.2996280740.
\]

Delta:

\[
-0.0044444601.
\]

## Finite-height NRMSE

Original:

\[
0.0362570433.
\]

Corrected:

\[
0.0359834913.
\]

Delta:

\[
-0.0002735520.
\]

## Frozen-profile correlation

Original:

\[
0.9982160059.
\]

Corrected:

\[
0.9986389173.
\]

Delta:

\[
+0.0004229114.
\]

## Finite-height correlation

Original:

\[
0.9986595037.
\]

Corrected:

\[
0.9983810756.
\]

Delta:

approximately

\[
-0.0002784281.
\]

## Frozen-profile sign agreement

Original:

\[
0.9925.
\]

Corrected:

\[
0.9975.
\]

Delta:

\[
+0.005.
\]

## Root-win rate

Original:

\[
1.0.
\]

Corrected:

\[
1.0.
\]

No change.

---

# 4. Finite-height amplitude correction

The corrected high-occupancy finite-height NRMSE was approximately

\[
0.03598349127
\]

compared with frozen-profile NRMSE approximately

\[
0.2996280740.
\]

The NRMSE improvement factor is approximately

\[
\boxed{
8.33.
}
\]

Thus retaining the finite-height logarithmic density factor continues to explain a large fraction of the accessible-height amplitude discrepancy.

---

# 5. Correlation versus amplitude accuracy

After endpoint correction, the frozen leading profile had slightly higher mean high-occupancy correlation than the finite-height benchmark:

\[
0.9986389
\]

versus

\[
0.9983811.
\]

However, the finite-height benchmark had approximately 8.33 times lower NRMSE.

Therefore correlation alone does not determine the superior numerical approximation.

The corrected interpretation is:

- the frozen leading profile captures oscillatory curve shape extremely well;
- the finite-height density model is substantially more accurate in amplitude.

---

# 6. P-ZETA-001

Prediction:

Positive-width actual-zero windows generically smear individual Li response blind scales.

Corrected result:

\[
\boxed{
\text{PASS}
}
\]

The protocol root-win rate versus individual blind scales remained 1.0 at every reported occupancy threshold.

---

# 7. P-ZETA-002

Prediction:

After H/log H normalization, high-zero truncated window susceptibility broadly agrees with the frozen smooth-density profile.

Corrected result:

\[
\boxed{
\text{PASS WITH FINITE-HEIGHT AMPLITUDE QUALIFICATION}
}
\]

Corrected high-occupancy evidence:

\[
\rho
\approx
0.998639,
\]

sign agreement

\[
0.9975,
\]

and NRMSE

\[
0.299628.
\]

The frozen profile reproduces curve shape and sign geometry strongly while retaining material amplitude discrepancy.

---

# 8. P-ZETA-003

Prediction:

Empirical response-zero locations track window-profile zeros more closely than individual Li blind scales once windows contain sufficiently many computed zero ordinates.

Corrected result:

\[
\boxed{
\text{PASS}
}
\]

The high-occupancy subset retained 60 empirical roots and a frozen window-profile root win rate of 1.0 against individual blind scales.

---

# 9. Main revalidation conclusion

The endpoint provenance defect changed exact Phase 5C numerical metrics but did not reverse the principal finite-data conclusion.

After authoritative-anchor correction, the actual-zero window response remains strongly consistent in curve shape and response-zero geometry with the smooth-density window profile.

The finite computational data continue to support the response transformation

\[
\Psi_{\mathrm{Li}}
\longrightarrow
\Phi_\eta
\]

when passing from individual zero-coordinate susceptibility to positive-width computed-zero windows.

---

# 10. Revalidation disposition

The earlier Phase 5C status

REVALIDATION REQUIRED

is resolved.

Corrected prediction grades:

P-ZETA-001:

PASS.

P-ZETA-002:

PASS WITH FINITE-HEIGHT AMPLITUDE QUALIFICATION.

P-ZETA-003:

PASS.

The pre-repair metrics remain archived as historical validation data and must not be used as the final reported Phase 5C measurements.

---

# 11. Interpretation boundary

The experiment uses the frozen first-500-zero computational dataset.

No discrete convergence theorem is established.

No claim about off-critical zeros is established.

No new Li positivity theorem, zero-free region, or RH criterion follows.

The corrected experiment does not constitute evidence proving RH.
