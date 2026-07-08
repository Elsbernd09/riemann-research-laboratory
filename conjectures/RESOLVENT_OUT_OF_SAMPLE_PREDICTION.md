# Resolvent Kernel Out-of-Sample Prediction

## Phase 2C

## Status

FROZEN PRE-DERIVATION PREDICTION

This document must be committed before the exact second derivative of the third diagnostic kernel is derived inside the project.

The purpose is to test whether the emerging susceptibility scaling taxonomy has predictive rather than purely retrospective value.

---

# 1. Third kernel family

For real

\[
a>\frac12,
\]

define

\[
r_a(z)
=
\frac1{a-z}.
\]

This kernel is motivated by zero-resolvent terms occurring in logarithmic-derivative and partial-fraction structures associated with zeta-type functions.

The present project studies the individual kernel only.

---

# 2. Geometric parameter

Define

\[
d
=
a-\frac12.
\]

At

\[
\rho_\gamma
=
\frac12+i\gamma,
\]

the denominator is

\[
a-\rho_\gamma
=
d-i\gamma.
\]

The dimensionless ratio

\[
\frac d\gamma
\]

is the obvious scale-invariant local coordinate.

Unlike the Li and explicit-formula families, the resolvent kernel has no obvious external oscillatory phase parameter.

---

# 3. Prediction P-RES-001

Suppose

\[
\gamma\to\infty
\]

and

\[
\frac{
a-\frac12
}{
\gamma
}
\to c>0.
\]

The project predicts that the quadratic susceptibility has a nontrivial scaling limit of the form

\[
\boxed{
\gamma^3
\chi_a^{\mathrm{Res}}(\gamma)
\to
\Psi_{\mathrm{Res}}(c).
}
\]

Predicted height exponent:

\[
\boxed{
\alpha_{\mathrm{Res}}=3.
}
\]

Reason for prediction:

The reciprocal kernel has denominator degree one. Two derivatives are expected to produce denominator degree three. Under

\[
a-\rho_\gamma
\sim
\gamma(c-i),
\]

this suggests cubic height decay.

No exact derivative has yet been derived in the project at the time this prediction is frozen.

---

# 4. Prediction P-RES-002

The project predicts that

\[
\Psi_{\mathrm{Res}}(c)
\]

will be a rational function of \(c\).

No trigonometric factors are expected.

Reason:

After extraction of the height scale,

\[
a-\rho_\gamma
=
\gamma
\left(
\frac{a-\frac12}{\gamma}-i
\right).
\]

The limiting geometry is algebraic in

\[
c-i.
\]

---

# 5. Prediction P-RES-003

The third family is predicted to invalidate the phrase

"phase coordinate"

as a universal component of the susceptibility taxonomy.

The project predicts that the more appropriate general concept is an

ASYMPTOTIC SIMILARITY COORDINATE.

Under this revision, a kernel-family scaling signature would be

\[
\boxed{
(\Phi,\alpha,\Psi),
}
\]

where:

- \(\Phi\) is a dimensionless asymptotic similarity coordinate;
- \(\alpha\) is the generic height exponent in the selected similarity regime;
- \(\Psi\) is the limiting susceptibility profile.

The similarity coordinate may be oscillatory, geometric, or otherwise dictated by the kernel family.

---

# 6. Prediction P-RES-004

For fixed real

\[
a>\frac12,
\]

the project predicts faster decay than the generic similarity regime.

Specifically,

\[
\boxed{
\chi_a^{\mathrm{Res}}(\gamma)
=
O_a(\gamma^{-4}).
}
\]

The project further predicts that the leading fixed-\(a\) coefficient is proportional to

\[
a-\frac12.
\]

Reason:

At the critical-line-aligned value

\[
a=\frac12,
\]

the denominator is purely imaginary:

\[
a-\rho_\gamma=-i\gamma.
\]

An inverse odd power of this quantity is purely imaginary.

The project susceptibility takes the real part.

Therefore the leading cubic channel is expected to vanish in the fixed-\(a\) limit, exposing a next-order term.

---

# 7. Falsification criteria

The predictive framework is damaged if any of the following occur:

1. the generic moving-observation scaling requires a height exponent other than 3;
2. no nontrivial profile exists under
   \[
   (a-\frac12)/\gamma\to c;
   \]
3. the profile contains a genuinely oscillatory structure unexplained by algebraic resolvent geometry;
4. fixed \(a\) does not exhibit the predicted extra decay;
5. the dimensionless ratio
   \[
   (a-\frac12)/\gamma
   \]
   is not the natural similarity coordinate.

A failed prediction must remain in the repository.

---

# 8. No originality claim

The resolvent kernel and reciprocal-power scaling are elementary analytic objects.

The purpose of this phase is to test the project's comparative framework.

No claim is made that the predicted asymptotics are new.
