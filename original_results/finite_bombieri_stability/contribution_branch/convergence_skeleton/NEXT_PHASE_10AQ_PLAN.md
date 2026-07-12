# Next Phase 10AQ Plan — Choose a Tractable Convergence Model

## Goal

Phase 10AQ should choose the first tractable convergence model.

## Candidate models

1. Pointwise convergence model.
2. Uniform finite test-class model.
3. Matrix-entry convergence model.
4. Kernel truncation convergence model.
5. Toy explicit-formula truncation model.

## Recommended next target

Start with a finite test-class model:

\[
\mathcal F_R=\{f\in\mathcal D_W:\|f\|_{\mathcal X}\leq R\}.
\]

Then define what bound would be needed:

\[
\sup_{f\in\mathcal F_R}
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
\varepsilon_N(R).
\]

This is easier to reason about than full operator-norm convergence.

## Boundary

No RH proof.

No RH contribution yet.

No novelty claim yet.

