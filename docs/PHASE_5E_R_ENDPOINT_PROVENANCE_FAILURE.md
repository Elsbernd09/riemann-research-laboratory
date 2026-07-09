# Phase 5E-R Endpoint Provenance Failure and Repair

## Failure discovered

The initial independent Stieltjes evaluator failed to reproduce the direct empirical counting remainder.

The initial maximum errors were

\[
0.0354075785\ldots
\]

for both:

- full decomposition closure;
- direct-versus-Stieltjes counting remainder agreement.

The equality of the two failure magnitudes localized the problem to the independently evaluated counting term.

---

# Initial repair attempt

The first repair replaced numerical integration of a discontinuous bisect-based staircase callback by piecewise integration on intervals where the empirical count is constant.

This was mathematically cleaner but did not repair the discrepancy.

A targeted six-case validation still produced maximum error approximately

\[
0.0195616614.
\]

Therefore discontinuous quadrature was not the primary failure mechanism.

---

# Root cause

The occupancy CSV stored the window anchor height H with 60 displayed decimal digits.

The authoritative frozen zero dataset stored zero ordinates with 75 displayed decimal digits.

Phase 5E reconstructed H from the rounded occupancy-file value.

For an ordinary continuous integral, the resulting coordinate perturbation of approximately \(10^{-58}\) to \(10^{-59}\) would be negligible.

For an atomic counting measure, it changes interval membership.

The discrete response used

\[
[H,B],
\]

and the theoretical decomposition assumed that H was itself a zero ordinate with

\[
\Delta N_D(H)=1.
\]

After rounded serialization, the reconstructed H could lie microscopically below or above the authoritative zero ordinate.

Thus the code could simultaneously:

- evaluate a window at a rounded endpoint;
- assume a unit atom at that rounded endpoint.

These endpoint conventions were inconsistent.

---

# Anchor audit

The complete-window occupancy records were audited against the authoritative frozen zero dataset.

Results:

- complete rows audited: 40;
- exact serialized anchors: 0;
- serialized anchors rounded below the authoritative zero: 12;
- serialized anchors rounded above the authoritative zero: 28.

Every authoritative zero anchor had empirical counting jump

\[
1.
\]

Thus every occupancy-file H value differed from the authoritative atomic endpoint.

---

# Repair

The anchor zero index stored in the occupancy CSV is now treated as the authoritative provenance key.

The experiment reconstructs

\[
H
=
\gamma_{\text{anchor index}}
\]

directly from the frozen zero dataset.

The rounded occupancy-file H value is not used to reconstruct an atomic endpoint.

The empirical counting-remainder integral is also evaluated piecewise between zero ordinates, with the integer empirical count frozen on each open interval.

---

# Repair validation

Six adversarial cases were selected across:

- multiple eta values;
- low and high window heights;
- multiple similarity coordinates.

The direct counting remainder

\[
W-S_{\mathrm{exact}}
\]

was compared with the independently evaluated Stieltjes expression.

After repair, the maximum targeted discrepancy was approximately

\[
4.08\times10^{-82}.
\]

Status:

REPAIR VALIDATED.

---

# Mathematical disposition

The Stieltjes decomposition did not fail.

The numerical implementation failed because an atomic interval endpoint was reconstructed from a rounded display serialization.

The failure is classified as:

FAILED VALIDATION IMPLEMENTATION — ENDPOINT PROVENANCE ERROR.

---

# Repository rule

A rounded display serialization must never be used to reconstruct the location of an atomic measure endpoint when interval inclusion depends on exact equality.

For zero-anchored windows, the authoritative zero index must be used to recover the endpoint from the frozen zero dataset.

---

# Phase 5C consequence

The Phase 5C actual-zero window experiment also reconstructed H from the rounded occupancy-file field.

Therefore its exact numerical metrics require endpoint-corrected revalidation.

The prior Phase 5C results are not declared false.

Their status is:

REVALIDATION REQUIRED.

The broad profile conclusion must not be finalized until the authoritative-anchor rerun is complete.
