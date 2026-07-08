# Phase 2D Resolvent Prediction Scorecard

## Prediction protocol

The resolvent susceptibility predictions were frozen in Git before exact differentiation.

Frozen source:

`conjectures/RESOLVENT_OUT_OF_SAMPLE_PREDICTION.md`

The source prediction file remains unmodified.

---

# Results

| Prediction | Frozen expectation | Exact result | Grade |
|---|---|---|---|
| P-RES-001 | similarity coordinate \((a-1/2)/\gamma\), exponent 3 | exact scaled profile under the predicted coordinate with exponent 3 | PASS |
| P-RES-002 | rational nontrigonometric profile | \(4c(c^2-3)/(c^2+1)^3\) | PASS |
| P-RES-003 | "phase coordinate" is too restrictive | resolvent uses a nonoscillatory geometric similarity ratio | PASS — methodological |
| P-RES-004 | fixed-\(a\) decay \(O_a(\gamma^{-4})\), leading coefficient proportional to \(a-1/2\) | \(-12(a-1/2)\gamma^{-4}\) | PASS |

---

# Score

\[
\boxed{
4/4
}
\]

frozen qualitative predictions passed the analytic derivation.

The project did not predict the exact profile coefficients or the numerical fixed-\(a\) coefficient \(-12\).

Those were obtained only after the prediction freeze.

---

# Interpretation

The out-of-sample test increases internal confidence that the susceptibility scaling language is not purely retrospective.

It does not establish originality.

The frozen predictions were substantially motivated by dimensional analysis, homogeneity, and complex geometry.

The test therefore supports the framework as an organizing methodology rather than demonstrating a surprising theorem about RH.

---

# New structural issue

The generic similarity exponent need not equal the exponent observed on every parameter path.

For the resolvent family,

\[
\alpha=3
\]

generically, but

\[
\Psi_{\mathrm{Res}}(0)=0.
\]

The fixed-\(a\) path drives the similarity coordinate to zero at rate

\[
\gamma^{-1}.
\]

Since

\[
\Psi_{\mathrm{Res}}(c)
\sim-12c,
\]

the observed decay acquires one additional power:

\[
\gamma^{-4}.
\]

Future cross-diagnostic comparisons must account for zeros and vanishing orders of the limiting profile.
