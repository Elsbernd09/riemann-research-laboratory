# Phase 5A Actual-Zero Bridge Protocol

## Objective

Move from freely designed synthetic orbit-height ratios to finite windows of numerically computed Riemann zeta zero ordinates.

## Discrete object

For a finite critical-line zero data set, define

\[
\mathcal W_n(H,\eta)
=
\sum_{H\le\gamma_j\le(1+\eta)H}
\chi_n^{\mathrm{Li}}(\gamma_j).
\]

## Data provenance

The initial project data set will be generated reproducibly with mpmath.zetazero.

For every returned ordinate gamma_j, the pipeline will evaluate

\[
|\zeta(1/2+i\gamma_j)|
\]

at high precision and record the residual.

The repository will record:

- zero index;
- zero ordinate;
- zeta residual;
- decimal precision;
- mpmath version;
- Python version;
- repository commit at generation time;
- output file hash.

## Interpretation rule

The data set is a finite computational critical-line zero data set.

Its use does not assume or prove that all nontrivial Riemann zeta zeros lie on the critical line.

The experiment must not convert backend nomenclature into a theorem-level completeness claim.

## Frozen continuum prediction

The smooth-density window profile is

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

## Validation order

1. generate zero ordinates;
2. validate zeta residuals;
3. freeze and hash the zero-data file;
4. test window occupancy;
5. compute exact finite window susceptibility sums;
6. compare normalized window curves with the frozen continuum profile;
7. compare empirical response-zero locations with window-profile zeros and individual blind scales;
8. grade P-ZETA-001 through P-ZETA-003.

## Prohibited conclusion

Agreement with the smooth-density profile is not progress toward proving RH.

Disagreement is not evidence against RH.

The experiment concerns the response statistic defined by the project on a finite zero data set.
