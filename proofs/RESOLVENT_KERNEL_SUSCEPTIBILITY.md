# Resolvent Kernel Susceptibility

## Phase 2D

This document derives the exact quadratic susceptibility of the third out-of-sample kernel family after the Phase 2C predictions were frozen in Git.

The frozen prediction document is not modified.

---

# 1. Kernel

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

Set

\[
d
=
a-\frac12
>
0.
\]

At

\[
\rho_\gamma
=
\frac12+i\gamma,
\]

one has

\[
a-\rho_\gamma
=
d-i\gamma.
\]

---

# 2. Exact second derivative

Starting from

\[
r_a(z)
=
(a-z)^{-1},
\]

one obtains

\[
r_a'(z)
=
(a-z)^{-2}
\]

and

\[
\boxed{
r_a''(z)
=
2(a-z)^{-3}.
}
\]

---

# 3. Exact quadratic susceptibility

Define

\[
\chi_a^{\mathrm{Res}}(\gamma)
=
2\Re r_a''(\rho_\gamma).
\]

Then

\[
\boxed{
\chi_a^{\mathrm{Res}}(\gamma)
=
4\Re
\frac1{(d-i\gamma)^3}.
}
\]

Since

\[
\frac1{(d-i\gamma)^3}
=
\frac{(d+i\gamma)^3}
{(d^2+\gamma^2)^3},
\]

and

\[
\Re(d+i\gamma)^3
=
d^3-3d\gamma^2,
\]

one obtains

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

Equivalently,

\[
\boxed{
\chi_a^{\mathrm{Res}}(\gamma)
=
\frac{
4\left(a-\frac12\right)
\left[
\left(a-\frac12\right)^2
-
3\gamma^2
\right]
}{
\left[
\left(a-\frac12\right)^2
+
\gamma^2
\right]^3
}.
}
\]

---

# 4. Similarity coordinate

Define

\[
c_\gamma
=
\frac d\gamma.
\]

Then the exact susceptibility can be written as

\[
\boxed{
\chi_a^{\mathrm{Res}}(\gamma)
=
\gamma^{-3}
\frac{
4c_\gamma(c_\gamma^2-3)
}{
(c_\gamma^2+1)^3
}.
}
\]

Thus the dimensionless local coordinate is

\[
\boxed{
\Phi_{\mathrm{Res}}
=
\frac{
a-\frac12
}{
\gamma
}.
}
\]

---

# 5. Generic similarity scaling

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

Then

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

The generic similarity-regime height exponent is therefore

\[
\boxed{
\alpha_{\mathrm{Res}}=3.
}
\]

---

# 6. Exact profile zero

The susceptibility vanishes when

\[
d^2-3\gamma^2=0.
\]

Since \(d>0\),

\[
d=\sqrt3\,\gamma.
\]

Therefore

\[
\boxed{
\Psi_{\mathrm{Res}}(\sqrt3)=0.
}
\]

The similarity coordinate controls an exact sign transition in the resolvent susceptibility.

---

# 7. Fixed-observation regime

For fixed \(a\), equivalently fixed \(d\),

\[
\frac d\gamma\to0.
\]

From the exact formula,

\[
\chi_a^{\mathrm{Res}}(\gamma)
=
-12d\gamma^{-4}
\frac{
1-\frac{d^2}{3\gamma^2}
}{
\left(
1+\frac{d^2}{\gamma^2}
\right)^3
}.
\]

Hence

\[
\boxed{
\chi_a^{\mathrm{Res}}(\gamma)
\sim
-12d\gamma^{-4}.
}
\]

Equivalently,

\[
\boxed{
\lim_{\gamma\to\infty}
\gamma^4
\chi_a^{\mathrm{Res}}(\gamma)
=
-12
\left(
a-\frac12
\right).
}
\]

---

# 8. Boundary-profile interpretation

The generic profile is

\[
\Psi_{\mathrm{Res}}(c)
=
\frac{
4c(c^2-3)
}{
(c^2+1)^3
}.
\]

Near

\[
c=0,
\]

one has

\[
\Psi_{\mathrm{Res}}(c)
=
-12c
+
O(c^3).
\]

Since fixed \(d\) gives

\[
c=\frac d\gamma,
\]

the generic law

\[
\chi
=
\gamma^{-3}\Psi(c)
\]

becomes

\[
\chi
\sim
\gamma^{-3}
\left(
-12\frac d\gamma
\right)
=
-12d\gamma^{-4}.
\]

Thus the fixed-\(a\) exponent \(4\) is a degenerate boundary subregime of the generic exponent-\(3\) similarity law.

---

# 9. Frozen prediction grading

## P-RES-001

Prediction:

Generic similarity coordinate \(d/\gamma\), nontrivial scaled limit, height exponent \(3\).

Grade:

PASS.

---

## P-RES-002

Prediction:

The limiting profile is rational in \(c\) and has no trigonometric phase factors.

Grade:

PASS.

---

## P-RES-003

Prediction:

The term "phase coordinate" is too restrictive and should be generalized to "asymptotic similarity coordinate."

Grade:

PASS AS METHODOLOGICAL PREDICTION.

The resolvent coordinate \(d/\gamma\) controls the exact scaled susceptibility and its sign transition without representing an oscillatory phase.

---

## P-RES-004

Prediction:

For fixed \(a>1/2\), susceptibility decays as \(O_a(\gamma^{-4})\), with leading coefficient proportional to \(a-1/2\).

Grade:

PASS.

The exact leading term is

\[
-12
\left(
a-\frac12
\right)
\gamma^{-4}.
\]

The numerical coefficient \(-12\) was not predicted before derivation.

---

# 10. Taxonomy refinement

The third family suggests that a susceptibility signature may require more than

\[
(\Phi,\alpha,\Psi).
\]

The limiting profile may vanish at important parameter boundaries or interior similarity coordinates.

A parameter path approaching a zero of

\[
\Psi
\]

can exhibit additional height decay beyond the generic exponent

\[
\alpha.
\]

The project therefore records profile degeneracy as a possible additional taxonomy component.

This refinement is heuristic and has not been generalized.

---

# 11. No RH implication

The derivation concerns an individual rational zero kernel.

It does not prove a new RH criterion.

It does not establish a new zero-free region.

It does not imply the Riemann Hypothesis.

No originality claim is made.
