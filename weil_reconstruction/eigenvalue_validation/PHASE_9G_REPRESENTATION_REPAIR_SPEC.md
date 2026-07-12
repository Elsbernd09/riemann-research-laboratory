# Phase 9G Representation Repair Specification

## Purpose

The next phase must repair the finite representation before any broader synthetic validation.

## Required repair sequence

1. Re-read the Phase 9B residuals.
2. Identify which candidate had the smallest Hermitian residual.
3. Re-check the source formula for \(K^*(x,y;t)\).
4. Re-check the source formula for \(H(x,y;t)\).
5. Compare the \(K^*\)-based implementation against the closed-form \(H\)-kernel if source confidence permits.
6. Re-check whether the denominator \(1/4+y^2\) should be attached to the column variable.
7. Re-check weighted inner-product interpretation.
8. Re-check similarity symmetrization.
9. Re-run synthetic validation only after an explicit repair.

## Required output

The next phase must produce:

- a repair diagnosis;
- the suspected source of mismatch or blocked gates;
- the exact repair attempted;
- a before/after Hermitian residual table;
- a statement that no zeta zeros were used.

## Forbidden

No zeta zeros.

No RH claims.

No novelty claims.

No zeta-case Bombieri-Weil verification claims.
