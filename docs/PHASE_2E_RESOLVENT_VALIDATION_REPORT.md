# Phase 2E Resolvent Out-of-Sample Validation Report

## Objective

Independently validate the exact resolvent susceptibility derivation and grade the predictions frozen before derivation in Phase 2C.

---

# Frozen prediction integrity

The pre-derivation prediction document is

`conjectures/RESOLVENT_OUT_OF_SAMPLE_PREDICTION.md`.

The project preserved this document through the derivation and validation stages.

Its cryptographic hash was recorded in the validation campaign metadata.

The prediction file was not rewritten to match the derived result.

---

# 1. Symbolic second derivative validation

For

\[
r_a(z)
=
\frac1{a-z},
\]

independent symbolic differentiation produced

\[
\boxed{
r_a''(z)
=
\frac2{(a-z)^3}.
}
\]

Status:

VALIDATED.

---

# 2. Exact rational susceptibility

Let

\[
d=a-\frac12.
\]

The susceptibility

\[
\chi_a^{\mathrm{Res}}(\gamma)
=
2\Re r_a''
\left(
\frac12+i\gamma
\right)
\]

was symbolically reduced to

\[
\boxed{
\chi_a^{\mathrm{Res}}(\gamma)
=
\frac{
4d(d^2-3\gamma^2)
}{
(d^2+\gamma^2)^3
}.
}
\]

The exact rational expression was compared against the derivative-side implementation using arbitrary-precision arithmetic.

Status:

VALIDATED.

---

# 3. Generic similarity profile

Define

\[
c
=
\frac{
a-\frac12
}{
\gamma
}.
\]

On a path satisfying

\[
a-\frac12
=
c\gamma,
\]

the scaled susceptibility satisfies the exact identity

\[
\boxed{
\gamma^3
\chi_a^{\mathrm{Res}}(\gamma)
=
\frac{
4c(c^2-3)
}{
(c^2+1)^3
}.
}
\]

Thus if

\[
\frac{
a-\frac12
}{
\gamma
}
\to c>0,
\]

then

\[
\boxed{
\gamma^3
\chi_a^{\mathrm{Res}}(\gamma)
\to
\Psi_{\mathrm{Res}}(c),
}
\]

where

\[
\boxed{
\Psi_{\mathrm{Res}}(c)
=
\frac{
4c(c^2-3)
}{
(c^2+1)^3
}.
}
\]

Status:

VALIDATED.

---

# 4. Fixed-observation boundary regime

For fixed real

\[
a>\frac12,
\]

the similarity coordinate tends to zero:

\[
\frac{
a-\frac12
}{
\gamma
}
\to0.
\]

The project proved and numerically validated

\[
\boxed{
\gamma^4
\chi_a^{\mathrm{Res}}(\gamma)
\to
-12
\left(
a-\frac12
\right).
}
\]

Equivalently,

\[
\chi_a^{\mathrm{Res}}(\gamma)
\sim
-12
\left(
a-\frac12
\right)
\gamma^{-4}.
\]

Status:

VALIDATED.

---

# 5. Exact profile zero and sign transition

The limiting profile satisfies

\[
\Psi_{\mathrm{Res}}(c)=0
\]

at

\[
\boxed{
c=\sqrt3.
}
\]

The numerical validation confirmed opposite signs immediately to the left and right of this coordinate.

Thus the similarity coordinate controls an exact susceptibility sign transition.

Status:

VALIDATED.

---

# 6. Frozen prediction grades

## P-RES-001

Predicted:

Similarity coordinate

\[
(a-\tfrac12)/\gamma,
\]

nontrivial scaled profile, and generic height exponent \(3\).

Grade:

\[
\boxed{\text{PASS}}
\]

---

## P-RES-002

Predicted:

Rational, nontrigonometric limiting profile.

Grade:

\[
\boxed{\text{PASS}}
\]

---

## P-RES-003

Predicted:

The universal phrase "phase coordinate" is too restrictive and should be replaced by "asymptotic similarity coordinate."

Grade:

\[
\boxed{\text{PASS AS METHODOLOGICAL PREDICTION}}
\]

The resolvent family has a nonoscillatory geometric similarity coordinate controlling its exact scaled response and sign transition.

---

## P-RES-004

Predicted:

Fixed-\(a\) decay of order

\[
\gamma^{-4},
\]

with leading coefficient proportional to

\[
a-\frac12.
\]

Exact result:

\[
-12
\left(
a-\frac12
\right)
\gamma^{-4}.
\]

Grade:

\[
\boxed{\text{PASS}}
\]

The numerical coefficient \(-12\) was not predicted before derivation.

---

# 7. Validated prediction score

\[
\boxed{
4/4
}
\]

frozen qualitative predictions survived analytic derivation and independent validation.

This score does not constitute evidence for the Riemann Hypothesis.

The predictions were informed by homogeneity, dimensional analysis, and complex geometry.

The result supports the internal predictive usefulness of the susceptibility scaling framework.

---

# 8. Taxonomy refinement

The resolvent family exposes profile degeneracy as a separate structural component.

The generic family exponent is

\[
\alpha=3.
\]

But

\[
\Psi_{\mathrm{Res}}(0)=0
\]

and

\[
\Psi_{\mathrm{Res}}(c)
\sim-12c
\]

near zero.

A fixed-\(a\) parameter path approaches the profile zero at rate

\[
c\asymp\gamma^{-1}.
\]

This produces one additional height power and the effective fixed-\(a\) exponent

\[
4.
\]

Future diagnostic comparisons must track profile zeros, vanishing orders, and the rate at which parameter paths approach those zeros.

---

# 9. Current three-family signatures

## Li kernel

\[
\Phi_{\mathrm{Li}}
=
n/\gamma,
\qquad
\alpha_{\mathrm{Li}}=2.
\]

## Explicit-formula zero kernel

\[
\Phi_{\mathrm{EF}}
=
L\gamma,
\qquad
\alpha_{\mathrm{EF}}=3
\]

after exact native amplitude removal.

## Resolvent kernel

\[
\Phi_{\mathrm{Res}}
=
(a-\tfrac12)/\gamma,
\qquad
\alpha_{\mathrm{Res}}=3.
\]

The three profiles have distinct analytic forms.

---

# 10. Remaining limitation

The current framework classifies individual zero-kernel susceptibilities.

It has not yet compared complete RH-equivalent criteria under a common cost, noise, or truncation model.

No implication for RH is claimed.

No literature novelty claim has yet been established.
