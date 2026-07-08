# Phase 1B Validation Report

## Objective

Independently test the Phase 1A derivation of the individual Li-kernel quadratic susceptibility and its candidate mesoscopic scaling profile.

---

# Validation Route 1: Symbolic Differentiation

The original kernel

\[
f_n(z)
=
1-
\left(
1-\frac1z
\right)^n
\]

was differentiated independently using SymPy.

The symbolic derivative was compared with the manually derived formula

\[
f_n''(z)
=
n
\left(
1-\frac1z
\right)^{n-2}
\frac{2z-n-1}{z^4}.
\]

## Initial validation failure

The first validator used

`factor(together(expression))`

as the final symbolic identity test.

For the symbolic integer exponent \(n\), SymPy did not fully reduce the difference to zero even though the remaining expression was algebraically zero.

The unreduced expression required the relation

\[
\left(1-\frac1z\right)^n
=
\left(1-\frac1z\right)^{n-2}
\left(1-\frac1z\right)^2
\]

to expose the cancellation.

This was classified as:

FAILED VALIDATION IMPLEMENTATION

and not as a failed mathematical claim.

## Repair

The validator was replaced with stronger symbolic simplification and a fixed-integer adversarial fallback.

The general symbolic difference simplified exactly to zero.

Status:

VALIDATED.

---

# Validation Route 2: Arbitrary-Precision Direct Differentiation

The manually derived second derivative was compared against direct numerical differentiation of the original kernel using mpmath at 100 decimal digits of working precision.

Multiple values of \(n\) and \(\gamma\) were tested.

The trigonometric susceptibility formula was also compared against

\[
2\Re f_n''\left(\frac12+i\gamma\right).
\]

The numerical validation protocol uses an explicit relative-error threshold of

\[
10^{-70}.
\]

Status:

VALIDATED BY IMPLEMENTED CHECK.

---

# Automated-Test Tolerance Failure

The first pytest implementation used

`mp.almosteq(left, right)`

for the exact-formula comparison.

One case,

\[
n=100,
\qquad
\gamma=1,
\]

failed despite the two values agreeing to many tens of decimal digits.

The failure arose because `mp.almosteq` used an implicit context-dependent tolerance stricter than the previously declared numerical validation standard.

This created an inconsistency between the standalone validation script and the automated test suite.

This was classified as:

FAILED TEST CRITERION

and not as a failed mathematical claim.

## Repair

The pytest comparison was changed to use the explicit relative-error threshold

\[
10^{-70},
\]

matching the declared Phase 1B numerical protocol.

After repair, the automated test suite completed with zero failures.

---

# Validation Route 3: Finite-Displacement Recovery

The exact susceptibility was compared with

\[
\frac{
\mathcal R_{f_n}(\delta,\gamma)
}{
\delta^2
}
\]

for decreasing positive values of \(\delta\).

The response was evaluated directly from the original Li kernel.

The finite-displacement estimate converged toward the exact susceptibility in the pre-cancellation range.

Status:

VALIDATED.

---

# Mesoscopic Scaling Experiment

The candidate profile

\[
\Psi_{\mathrm{Li}}(c)
=
-2c(c\cos c+2\sin c)
\]

was compared with

\[
\gamma^2
\chi_n^{\mathrm{Li}}(\gamma)
\]

for sequences with

\[
n/\gamma
\]

near prescribed values of \(c\).

The experiment records:

- target \(c\);
- \(\gamma\);
- integer \(n\);
- actual ratio \(n/\gamma\);
- scaled susceptibility;
- target profile;
- profile at the actual ratio;
- absolute errors.

The experiment uses 100 decimal digits of working precision.

A CSV and metadata record are stored under

`results/li_mesoscopic_scaling/`.

The observed scaling behavior matched the analytically derived profile to decreasing error across the tested large-height ranges.

This experiment validates the implementation of the derived limit.

It is not the source of the theorem.

---

# Research Interpretation

The validation results support the algebraic correctness of the exact individual-kernel susceptibility formula.

The numerical scaling experiment is a reproduction check of an analytically derived limit.

It is not independent evidence for the Riemann Hypothesis.

It is not evidence that the susceptibility formalism is original.

It is not evidence that the individual-kernel scaling law extends directly to the globally interpreted Li coefficient zero sum.

---

# Recorded Validation Failures

## VF-001

Type:

FAILED VALIDATION IMPLEMENTATION

Description:

SymPy's initial `factor(together(...))` route failed to expose a true symbolic cancellation involving a symbolic integer exponent.

Impact on mathematics:

None after independent algebraic analysis and repaired symbolic validation.

---

## VF-002

Type:

FAILED TEST CRITERION

Description:

The initial pytest suite used an implicit `mp.almosteq` tolerance inconsistent with the explicit \(10^{-70}\) numerical validation threshold already adopted elsewhere in the project.

Impact on mathematics:

None after the automated test was aligned with the predeclared validation protocol.

---

# Remaining Main Obstruction

The individual Li kernel and the full Li coefficient are not the same mathematical object.

The next theoretical stages must address:

- zero-sum interpretation;
- convergence or summation convention;
- whether finite signed zero perturbation can be inserted consistently into the zero-side representation;
- whether the response of a finite modified orbit is meaningful relative to the global coefficient;
- whether collective zero contributions swamp or structurally alter the local susceptibility scale.
