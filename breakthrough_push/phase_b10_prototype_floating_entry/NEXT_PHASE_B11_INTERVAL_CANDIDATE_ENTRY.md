# Next Phase B11 — Interval Candidate Entry

## Goal

Upgrade \(M_{00}^{arith}\) from prototype floating-point to interval candidate.

## Required

Create conservative interval radii for:

1. central integral approximation;
2. star-central integral approximation;
3. prime component approximation;
4. convolution approximation;
5. archimedean approximation;
6. rounding;
7. normalization.

## Target status

\[
\texttt{INTERVAL\_CANDIDATE}
\]

## Boundary

Interval candidate is still not certified unless every error bound is rigorously justified.
