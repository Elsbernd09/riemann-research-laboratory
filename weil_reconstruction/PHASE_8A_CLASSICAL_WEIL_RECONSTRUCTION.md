# Phase 8A — Classical Weil Criterion Reconstruction

## Purpose

Phase 7 showed that local horizontal-defect detection is possible, but the arithmetic-side or Weil-positive bridge remains open.

Phase 8 begins by reconstructing the classical Weil criterion framework inside the repository.

This is not a novelty claim.

This is not a proof of RH.

This is a literature-grounded reconstruction target.

---

# 1. Why Weil positivity matters

The Riemann Hypothesis is equivalent to several positivity statements.

One of the deepest classical forms is Weil positivity.

At a high level, Weil-type criteria connect:

1. zero-side sums over nontrivial zeros;
2. test functions;
3. Fourier/Mellin transforms;
4. prime-side arithmetic terms;
5. positivity of a quadratic functional.

This is exactly the kind of structure missing from the Phase 7 horizontal-defect detectors.

---

# 2. Central lesson from Phase 7

Phase 7 produced local detectors of horizontal displacement such as

\[
D_{\mathrm{rad}}(\rho)
=
\left(\log |1-1/\rho|\right)^2.
\]

It also produced quadratic Li-filter detectors such as

\[
Q_{1,2}(u,\theta)
=
\Delta_1(u,\theta)^2+\Delta_2(u,\theta)^2.
\]

These objects are positive and horizontally sensitive.

But they are not automatically connected to the explicit formula.

Therefore they are diagnostic, not RH criteria.

---

# 3. Classical Weil reconstruction target

The reconstruction target is:

\[
\boxed{
\text{Understand exactly how classical Weil positivity detects off-critical zeros.}
}
\]

The repository should build:

1. a notation map;
2. a zero-side formulation;
3. a test-function formulation;
4. a quadratic-form formulation;
5. a finite-rank approximation plan;
6. a clear boundary between known classical theory and project-specific experiments.

---

# 4. Basic conceptual structure

A Weil-type criterion has the form:

\[
\mathcal W(f)\ge0
\]

for all allowed test functions \(f\), where the validity of this positivity is equivalent to RH.

The zero-side portion morally involves sums over zeros.

If an off-critical zero exists, the criterion predicts that some test function should expose a negative direction.

Thus the real Phase 8 question is:

\[
\boxed{
\text{Can we reconstruct that negative-direction mechanism in finite controlled models?}
}
\]

---

# 5. What Phase 8A does

Phase 8A does not prove the criterion from scratch.

Phase 8A creates a reconstruction map:

- What are the objects?
- What is known?
- Where do off-critical zeros enter?
- What would a finite-rank model need to reproduce?
- What must not be claimed?

---

# 6. Known-vs-project boundary

## Classical

The following are classical and should not be claimed as new:

- Weil explicit formula;
- Weil positivity criterion;
- Li criterion;
- Bombieri-Lagarias formulations;
- equivalence between suitable positivity statements and RH;
- the idea that off-critical zeros create negative directions.

## Project-specific

The project-specific work may include:

- finite diagnostic models;
- comparison with Phase 7 horizontal-defect detectors;
- reproducible toy approximations;
- obstruction audits;
- careful mapping between toy models and classical structures.

---

# 7. Phase 8A conclusion

The next serious work is not to invent a new criterion immediately.

The next serious work is to reconstruct the classical Weil criterion carefully enough that future finite-rank experiments are no longer arbitrary toy models.

