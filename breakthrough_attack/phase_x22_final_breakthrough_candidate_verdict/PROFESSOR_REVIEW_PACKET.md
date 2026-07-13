# Professor Review Packet — Riemann Research Laboratory Breakthrough-Attack Branch

## Project classification

\[
\boxed{
\texttt{CONTRIBUTION\_CANDIDATE\_REQUIRING\_EXPERT\_REVIEW}
}
\]

## Short summary

This project constructs a source-normalized computational certificate framework for finite-dimensional approximations to the Bombieri–Lagarias/Weil positivity setting. It develops a pole-cancelled smooth test-function basis, support-aware finite prime truncation, interval derivative-bound machinery, term-level interval certificate structures for the Bombieri–Lagarias explicit formula, a full assembled \(M_{00}\) certificate candidate, and a prototype \(2\times2\) matrix candidate.

The work does not prove RH and does not yet produce a fully certified arithmetic entry, but it identifies precise certification gates.

## Main artifacts

1. `breakthrough_attack/phase_x18_assemble_full_m00_interval_certificate/full_m00_interval_certificate.json`
2. `breakthrough_attack/phase_x20_outward_rounding_and_interval_audit/outward_rounding_interval_audit_report.json`
3. `breakthrough_attack/phase_x21_two_by_two_matrix_certificate_candidate/two_by_two_matrix_certificate_candidate.json`
4. `research_ledger/CLAIM_LEDGER.md`
5. `research_ledger/PHASE_LEDGER.md`

## Main unresolved gates

1. raw Mellin moment integral certification;
2. certified pointwise convolution enclosures;
3. rigorous archimedean continuous-extension derivative bound;
4. formal outward rounding;
5. independent off-diagonal matrix entries;
6. finite-to-Weil positivity theorem;
7. independent source/prior-art review.

## What I am asking an expert to review

1. Are the Bombieri–Lagarias conventions normalized correctly?
2. Is the pole-cancelled basis construction mathematically sound?
3. Is the finite prime cutoff logic correct?
4. Are the term decompositions of \(T_{BL}[F]\) correct?
5. Are the stated certification gates complete?
6. Is there a known prior-art collision with finite Galerkin/Weil certificate methods?
7. Is any part of this framework potentially publishable after hardening?

## What I am not claiming

I am not claiming a proof of RH.

I am not claiming a confirmed breakthrough.

I am not claiming novelty before prior-art review.

I am not claiming a certified finite Weil matrix.

I am not claiming a completed finite-to-Weil theorem.
