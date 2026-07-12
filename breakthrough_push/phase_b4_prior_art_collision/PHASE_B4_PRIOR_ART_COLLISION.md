# Phase B4 — Prior-Art Collision Audit

## Purpose

Phase B4 compares the breakthrough-push branch against known literature directions.

The central question is:

\[
\boxed{
\text{Is the finite spectral/admissible matrix framework new, standard, or overlapping prior art?}
}
\]

This phase uses the currently uploaded source summary as a provisional prior-art guide. It is not yet a full literature review because primary papers still need to be read directly.

---

# 1. Prior-art signals from source summary

The uploaded source summary identifies several major frameworks:

1. Weil's original explicit formula and positivity criterion.
2. Bombieri's streamlined presentation of Weil's explicit formula.
3. Bombieri-Lagarias connection between Weil positivity and Li-type criteria.
4. Connes trace-formula/spectral geometry viewpoint.
5. Suzuki screw-function formulation.
6. Connes/Consani/Moscovici/van Suijlekom finite Galerkin matrix approaches.
7. Burnol/Yoshida finite-range or local positivity frameworks.

The most important collision warning is the finite Galerkin matrix direction.

If prior work already builds exact finite-dimensional Galerkin matrices for Weil's quadratic form, then our finite matrix framework is likely not novel as a general idea.

---

# 2. Collision table

| Project component | Prior-art collision risk | Notes |
|---|---:|---|
| Weil positivity \(T[g*g^*]\ge0\) | Very high | Classical Weil criterion. |
| Multiplicative convolution \(g*g^*\) | Very high | Classical setup; appears in Bombieri-Lagarias-style formulations. |
| Mellin product identity | Very high | Standard convolution/Mellin identity. |
| Finite spectral truncation \(Q_Y\) | High | Natural truncation; likely standard or implicit. |
| Finite detection by convergence | High | Basic analysis: if \(Q_Y\to Q_W\), negative margin is eventually detected. |
| Pole-admissible finite subspace \(Ca=0\) | Medium-high | Natural finite-dimensional enforcement of pole cancellation. |
| Compact-support prime-tail cutoff | Medium | Straightforward from support, but useful in this framework. |
| Archimedean finite-interval reduction | Medium | Likely known or straightforward, but still useful. |
| Toy arithmetic matrix prototype | Low as theorem, medium as implementation | Prototype only, not a research novelty. |
| Certified arithmetic matrix future plan | Medium | Could become contribution if fully rigorous and not already done. |

---

# 3. Honest novelty assessment

The following are not novel:

\[
g^*(x)=x^{-1}\overline{g(1/x)}.
\]

\[
F_g=g*g^*.
\]

\[
\widehat{g*g^*}(s)=\widehat g(s)\overline{\widehat g(1-\bar s)}.
\]

\[
T[F_g]\ge0
\]

as an RH-equivalent positivity condition.

The following are likely standard or immediate:

1. if \(Q_Y(g)\to Q_W(g)\), then negative margin is eventually detected;
2. finite-dimensional nullspace restriction for linear constraints;
3. \(M_{\mathrm{adm}}=N^*MN\);
4. compact support implying finite prime support;
5. interval Rayleigh quotient logic.

The potentially useful contribution is not a single famous theorem yet.

The useful contribution is the integrated framework:

\[
\boxed{
\text{pole-admissible finite test spaces + arithmetic matrix blueprint + certificate pipeline}
}
\]

But this must be compared against exact Galerkin matrix work before novelty can be claimed.

---

# 4. Theorem B4.1 — novelty cannot be claimed before primary comparison

Given the uploaded prior-art summary reports modern finite-dimensional Galerkin matrix approximations of the Weil form, the project cannot honestly claim novelty for finite-dimensional Weil matrices until those works are compared directly.

## Proof

A novelty claim requires showing that the claimed object, theorem, or method is not already present in prior work.

The uploaded summary explicitly states that recent frameworks transform the global Weil form into finite-dimensional Galerkin matrices.

Since the present project also constructs finite-dimensional matrix restrictions of a Weil/Bombieri form, there is direct conceptual overlap.

Therefore novelty is unresolved until direct paper-by-paper comparison is completed.

\[
\square
\]

---

# 5. Updated breakthrough status

Before B4, the project status was:

\[
\text{breakthrough candidate pathway}.
\]

After B4, the honest status is sharper:

\[
\boxed{
\text{conditional framework with serious prior-art collision risk}
}
\]

This is not bad.

It means the project is entering the real research zone: not just building, but comparing.

However:

\[
\boxed{
\text{BREAKTHROUGH\_NOT\_ACHIEVED}
}
\]

and

\[
\boxed{
\text{NOVELTY\_NOT\_ESTABLISHED}.
}
\]

---

# 6. What could still become a contribution

A contribution may still be possible if one of these survives comparison:

## 6.1 Explicit pole-admissible certificate pipeline

A clean finite-dimensional pipeline:

\[
C a=0,\qquad M_{\mathrm{adm}}=N^*MN,
\]

combined with certified arithmetic entries.

## 6.2 Compact-support arithmetic finite-entry method

The support cutoff:

\[
\operatorname{supp}(F_g)\subset[e^{-2B},e^{2B}]
\]

giving finite prime sums, plus reduced archimedean certification.

## 6.3 Certified implementation

A reproducible interval-certified arithmetic matrix implementation for admissible finite test spaces.

## 6.4 Educational/professor-review contribution

Even if the math is known, the project can still be a strong research reconstruction if framed honestly.

---

# 7. Required next literature targets

The next breakthrough-push step is to obtain exact excerpts or PDFs for:

1. Bombieri-Lagarias, “Complements to Li's Criterion for the Riemann Hypothesis.”
2. Weil explicit formula / Weil criterion source.
3. Connes trace formula paper.
4. Connes/Consani/Moscovici/van Suijlekom Galerkin matrix paper.
5. Suzuki screw-function papers.
6. Burnol/Yoshida local positivity papers.

The most important collision target is the finite Galerkin matrix paper.

---

# 8. Next phase

Phase B5 should be:

\[
\boxed{
\text{Primary Paper Extraction Pack}
}
\]

It should create a folder structure and extraction templates for each source:

1. exact definitions;
2. exact theorem statement;
3. exact matrix object;
4. overlap with our project;
5. gap remaining.

No breakthrough claim until that is done.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a breakthrough.

This phase does not prove novelty.

This phase does not complete prior-art review.

Exact audit strings:

PHASE_B4_PRIOR_ART_COLLISION_COMPLETE

FINITE_GALERKIN_COLLISION_RISK_IDENTIFIED

CLASSICAL_WEIL_COMPONENTS_NOT_NOVEL

FINITE_DETECTION_BY_CONVERGENCE_LIKELY_STANDARD

POLE_ADMISSIBLE_PIPELINE_POSSIBLE_CONTRIBUTION

ARITHMETIC_CERTIFICATE_PIPELINE_POSSIBLE_CONTRIBUTION

NOVELTY_NOT_ESTABLISHED

BREAKTHROUGH_NOT_ACHIEVED

READY_FOR_PHASE_B5_PRIMARY_PAPER_EXTRACTION

