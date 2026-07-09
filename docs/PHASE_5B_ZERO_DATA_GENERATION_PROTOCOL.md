# Phase 5B Finite Zeta-Zero Data Generation Protocol

## Objective

Generate the first moderate computational zero-ordinate data set for the project's actual-zero window response experiments.

## Backend

The initial dataset uses

\[
\texttt{mpmath.zetazero}
\]

at 80 decimal digits.

## Dataset size

The first campaign requests indices

\[
1,\ldots,500.
\]

The project intentionally begins with a moderate data set before scaling zero generation.

## Per-ordinate validation

For every returned ordinate

\[
\gamma_j,
\]

the generator evaluates

\[
\left|
\zeta\left(
\frac12+i\gamma_j
\right)
\right|.
\]

A numerical residual threshold of

\[
10^{-40}
\]

is used as a computational quality gate.

Passing this gate is not a theorem-level certification of RH, zero completeness, or simplicity.

## Provenance

The dataset metadata records:

- mpmath version;
- decimal precision;
- zero-index range;
- first and last ordinates;
- maximum zeta residual;
- Git commit at generation start;
- repository cleanliness at generation start;
- Python version;
- platform;
- runtime;
- CSV SHA-256 hash.

## Window occupancy audit

Before computing susceptibility curves, the project measures the number of generated ordinates in relative-height windows

\[
[H,(1+\eta)H]
\]

for

\[
\eta\in
\{0.05,0.10,0.20,0.50\}.
\]

The occupancy audit determines whether 500 zeros are sufficient for an initial Phase 5C comparison.

## Interpretation boundary

The generated file is a finite numerical critical-line zero-ordinate dataset.

It must not be described as a proof that all nontrivial zeta zeros lie on the critical line.
