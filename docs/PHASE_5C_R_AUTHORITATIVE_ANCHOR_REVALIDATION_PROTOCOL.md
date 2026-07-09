# Phase 5C-R Authoritative-Anchor Revalidation Protocol

## Objective

Revalidate the Phase 5C actual zeta-zero window response experiment after discovery of the atomic endpoint provenance error in Phase 5E-R.

## Original endpoint implementation

The original Phase 5C experiment reconstructed

\[
H
\]

from the 60-digit display serialization stored in the occupancy CSV.

The frozen zero dataset stores the authoritative zero ordinate to 75 displayed digits.

The anchor audit proved that none of the 40 complete occupancy-file H values were exactly equal to the authoritative zero ordinate.

Twelve rounded below the zero and twenty-eight rounded above.

## Consequence

For closed windows

\[
[H,(1+\eta)H],
\]

a rounded-above anchor may silently exclude the intended left endpoint zero.

Thus the original Phase 5C exact numerical metrics require revalidation.

## Repair

The occupancy-file field

\[
\texttt{anchor\_zero\_index}
\]

is used as the provenance key.

The authoritative endpoint is reconstructed as

\[
H
=
\gamma_{\text{anchor zero index}}
\]

from the frozen zero dataset.

## Frozen experimental design

The Phase 5C revalidation preserves:

- the same first-500-zero dataset;
- the same complete-window records;
- the same eta values;
- the same requested c-grid from 0.25 to 20 in steps of 0.25;
- the same integer-index realization rule;
- the same Model A and Model B profiles;
- the same NRMSE metric;
- the same correlation metric;
- the same sign-agreement metric;
- the same interpolated-root method;
- the same nearest-root win metric;
- the same occupancy thresholds.

No metric is changed after observing the endpoint failure.

## Comparison

The original pre-repair Phase 5C summary is archived.

The corrected summary is compared directly against the archived metrics.

## Decision rule

The previous Phase 5C prediction grades remain provisional until the authoritative-anchor rerun is complete.

The project will grade the corrected results from the frozen original prediction language.

## Interpretation boundary

The revalidation concerns numerical correctness of the finite computational experiment.

It does not prove a discrete asymptotic theorem or RH.
