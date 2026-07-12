# Phase 10AV — Interval Gram-Entry Calculator Prototype

## Purpose

Phase 10AU proved the certified numerical error model.

Phase 10AV implements the interval-certificate structure:

\[
[\ell,u],
\qquad
\widetilde G=\frac{\ell+u}{2},
\qquad
r=\frac{u-\ell}{2},
\qquad
\chi_N^{(m)}=\max_{i,j}r_{ij}.
\]

## Important boundary

This prototype does not compute the true classical Weil/Bombieri Gram matrix.

It only demonstrates the certified numerical infrastructure.

## Implemented objects

The script implements:

1. interval lower and upper bounds;
2. midpoint;
3. radius;
4. interval addition;
5. interval subtraction;
6. interval multiplication;
7. toy interval dot product;
8. toy interval Gram matrix;
9. global numerical certificate \(\chi_N^{(m)}\);
10. matrix-level bound \(m\chi_N^{(m)}\);
11. SHA-256 certificate hash.

## Theorem-backed meaning

By Phase 10AU, if each interval truly encloses the exact finite Gram entry, then

\[
|C_{ij}^{(N)}|\leq \chi_N^{(m)}.
\]

The prototype shows how such a certificate would be recorded.

## Current status

INTERVAL_GRAM_ENTRY_CALCULATOR_PROTOTYPE

CHI_N_M_COMPUTED

MATRIX_LEVEL_BOUND_COMPUTED

CERTIFICATE_SHA256_RECORDED

TRUE_WEIL_GRAM_NOT_COMPUTED

NOT_RH_CONTRIBUTION_YET

## Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not compute the true classical Weil/Bombieri Gram matrix.

This phase does not prove classical convergence.

This phase does not claim novelty.

