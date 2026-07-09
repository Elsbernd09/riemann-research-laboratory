# Phase 5B Finite Zeta-Zero Data and Occupancy Report

## Dataset

The project generated the first 500 critical-line zeta zero ordinates returned by the selected mpmath backend.

The first recorded ordinate is approximately

\[
14.13472514173469379.
\]

The last recorded ordinate is approximately

\[
811.18435884650626034.
\]

The generation pipeline directly evaluated

\[
|\zeta(1/2+i\gamma_j)|
\]

for every returned ordinate under the declared numerical residual gate.

The dataset remains a finite computational critical-line zero-ordinate dataset.

It is not a proof of RH, global zero completeness, or zero simplicity.

---

# Window occupancy audit

Relative-height windows

\[
[H,(1+\eta)H]
\]

were audited for

\[
\eta
\in
\{0.05,0.10,0.20,0.50\}.
\]

The occupancy audit passed.

Among complete windows:

- minimum occupancy: 1;
- maximum occupancy: 170;
- windows with at least 10 zeros: 29;
- windows with at least 25 zeros: 18;
- windows with at least 50 zeros: 10.

---

# Experimental consequence

The first-500-zero dataset is sufficient for an initial discrete window-response comparison.

However, sparse windows are not treated as primary tests of the smooth-density continuum model.

The project uses the following experimental occupancy bands:

## Sparse

\[
N_{\mathrm{window}}<10.
\]

Exploratory only.

## Moderate

\[
10\le N_{\mathrm{window}}<25.
\]

Finite-window comparison.

## Dense

\[
N_{\mathrm{window}}\ge25.
\]

Primary continuum-profile comparison.

## High-occupancy subset

\[
N_{\mathrm{window}}\ge50.
\]

Strongest initial comparison for P-ZETA-002 and P-ZETA-003.

These thresholds are project protocol choices and are not universal mathematical constants.

---

# Finite-height benchmark requirement

The frozen Phase 5A prediction uses the leading normalization

\[
H/\log H.
\]

At the accessible heights in the first-500-zero dataset, finite-height logarithmic-density corrections may remain visible.

Phase 5C must therefore compare the discrete response to:

1. the frozen asymptotic profile \(\Phi_\eta\);
2. a finite-height smooth-density benchmark retaining
   \[
   \log(uH/(2\pi)).
   \]

The second benchmark is diagnostic and does not replace the frozen prediction in the prediction scorecard.
