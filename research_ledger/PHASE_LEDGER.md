# Phase Ledger

## Phase 0A — Repository and Research Constitution

Status: COMPLETE

### What we built

A reproducible repository structure, claim-status protocol, phase ledger, and research constitution.

### Mathematical claim supported

None.

### What remains unproved

All project-specific mathematical claims.

### Largest weakness at completion

The synthetic zero perturbation had not been mathematically specified.

---

## Phase 0B — Zero Surgery Specification

Status: COMPLETE

### What we built

A three-level taxonomy:

1. zero-orbit surgery;
2. canonical-product surgery;
3. arithmetic-structural surgery.

We specified the symmetry-preserving quartet

\[
Q_{\delta,\gamma}.
\]

We identified Question ZS-001 concerning zero-count conservation and orbit degeneration.

### Mathematical claim supported

Only standard xi-function symmetry facts are currently used.

No new theorem is claimed.

### What remains unproved

Whether finite factor-ratio surgery provides a useful or mathematically natural comparison model for the selected diagnostics.

Whether a zero-count-preserving perturbation model should replace pair-to-quartet surgery.

### Largest current weakness

The critical-line symmetry orbit has two distinct points while a generic off-critical orbit has four.

The naive pair-to-quartet operation therefore changes zero count and may contaminate diagnostic-response measurements.


---

## Phase 0C — Perturbation Model Selection

Status: COMPLETE

### What we built

We compared four perturbation models:

1. pair-to-quartet bifurcation;
2. double-pair splitting;
3. two-pair transport;
4. signed symmetry-breaking response.

Model A was rejected as the primary perturbation model because its response generally fails to vanish as delta tends to zero.

Model C was rejected as the primary sensitivity model because horizontal displacement and vertical gap compression are confounded at second order.

Model B was retained as a local geometric model.

Model D was selected as the primary response formalism.

### Primary mathematical object

\[
\chi_f(\gamma)
=
\lim_{\delta\to0}
\frac{
\mathcal R_f(\delta,\gamma)
}{
\delta^2
}.
\]

For analytic conjugation-compatible kernels,

\[
\chi_f(\gamma)
=
2\Re
f''\left(
\frac12+i\gamma
\right).
\]

### Mathematical claim supported

The even-power cancellation follows from symmetric Taylor expansion.

A precise project lemma has been formulated but has not yet been promoted to PROVED IN PROJECT.

### What remains unproved

Whether susceptibility comparison reveals a mathematically useful distinction among RH diagnostics.

Whether the proposed framework or its relevant quantitative consequences are already present in the literature.

Whether an intrinsic normalization exists for comparing different diagnostic families.

### Largest current weakness

Raw response magnitudes across different diagnostics are not directly comparable because normalization and baseline scale may dominate the measured susceptibility.


---

## Phase 0D — Normalization and Susceptibility Signature

Status: COMPLETE

### What we built

We tested several cross-diagnostic normalization strategies.

Baseline-value normalization was rejected because cancellation can create artificial singularities.

Absolute-pair normalization was rejected as intrinsic because additive kernel shifts preserve susceptibility while changing the denominator.

We retained:

\[
\Omega_f
=
\frac{|\Re f''|}{|f''|}
\]

as a response-orientation coefficient,

\[
\mathcal K_f
=
\frac{ff''}{(f')^2}
\]

as a local multiplicative-scale-invariant shape quantity,

and

\[
\mathcal C_f
=
\frac{f''}{f}
-
\left(\frac{f'}{f}\right)^2
\]

as logarithmic curvature.

The primary comparison object is now the susceptibility signature

\[
\Sigma_f
=
(
\chi_f,
\Omega_f,
\mathcal K_f,
\mathcal C_f
).
\]

### Mathematical claim supported

The stated scaling and additive-shift properties follow by direct differentiation and algebra.

No RH-related theorem is claimed.

### What remains unproved

Whether the susceptibility signature reveals mathematically useful structure for any standard RH diagnostic family.

Whether the formalism or an equivalent formulation already exists in the literature.

Whether the chosen components are the correct long-term invariants.

### Largest current weakness

The project has not yet analyzed a single concrete standard RH diagnostic kernel.

Until that happens, the framework remains methodology rather than substantive analytic-number-theory research.


---

## Phase 1A — Exact Li-Kernel Susceptibility

Status: COMPLETE

### What we derived

For

\[
f_n(z)
=
1-
\left(
1-\frac1z
\right)^n,
\]

we derived

\[
f_n''(z)
=
n
\left(
1-\frac1z
\right)^{n-2}
\frac{2z-n-1}{z^4}.
\]

At

\[
\rho_\gamma
=
\frac12+i\gamma,
\]

with

\[
\theta_\gamma
=
2\arctan\left(\frac1{2\gamma}\right),
\]

the individual Li-kernel susceptibility is

\[
\chi_n^{\mathrm{Li}}(\gamma)
=
-
\frac{
2n
}{
\left(\gamma^2+\frac14\right)^2
}
\left[
n\cos(n\theta_\gamma)
+
2\gamma\sin(n\theta_\gamma)
\right].
\]

For fixed \(n\),

\[
\chi_n^{\mathrm{Li}}(\gamma)
=
-\frac{6n^2}{\gamma^4}
+
O_n(\gamma^{-6}).
\]

A candidate mesoscopic scaling proposition has been formulated:

\[
\frac n\gamma\to c
\]

implies

\[
\gamma^2
\chi_n^{\mathrm{Li}}(\gamma)
\to
-2c(c\cos c+2\sin c).
\]

### Mathematical claim supported

A manual algebraic derivation supports the exact susceptibility formula.

The mesoscopic scaling result appears to follow directly from the exact formula.

Neither has yet been promoted to PROVED IN PROJECT.

### What remains unproved or unaudited

Independent symbolic verification.

Independent finite-difference verification.

Precise proof formatting for the scaling limit.

Current literature originality.

Relevance of the individual-kernel scaling law to full Li coefficients or RH.

### Largest current weakness

The project has analyzed an individual Li zero kernel, not the globally regularized zero sum defining Li coefficients.

No passage from local kernel susceptibility to a perturbation statement about the full Li coefficient sequence has been justified.


---

## Phase 1B — Independent Li Susceptibility Validation

Status: COMPLETE

### What we built

We implemented the individual Li zero kernel and its manually derived second derivative using arbitrary-precision arithmetic.

We independently validated the derivative identity with symbolic differentiation.

We compared the exact susceptibility formula with direct arbitrary-precision differentiation.

We recovered the susceptibility from finite signed orbit responses divided by delta squared.

We ran a reproducible mesoscopic scaling experiment and stored both CSV output and computational metadata.

We also preserved two validation-system failures:

1. an insufficient SymPy simplification route;
2. an automated-test tolerance inconsistent with the declared numerical protocol.

### Mathematical claim supported

The project now treats the following scaling statement as PROVED IN PROJECT:

If

\[
\gamma_j\to\infty
\]

and

\[
n_j/\gamma_j\to c>0,
\]

then

\[
\gamma_j^2
\chi_{n_j}^{\mathrm{Li}}(\gamma_j)
\to
-2c(c\cos c+2\sin c).
\]

This statement concerns the individual Li kernel susceptibility defined by the project.

No originality claim is made.

### What remains unproved or unaudited

Novelty relative to the literature.

Any implication for RH.

Any justified passage from individual-kernel susceptibility to the full globally interpreted Li coefficient sequence.

Any cross-diagnostic comparison.

### Largest current weakness

The current exact result is local to a single analytic kernel contribution.

The main mathematical risk is that the global Li zero sum requires a summation interpretation that prevents naive local-to-global perturbation arguments.


---

## Phase 1C — Local-to-Global Li Response Audit

Status: COMPLETE

### What we discovered

The finite Li-type derivative functional applied to an individual zero factor does not produce the project's zero kernel at the same zero.

Instead,

\[
g_n(\rho)
=
1-
\left(
1-\frac1\rho
\right)^{-n}
=
f_n(1-\rho).
\]

Thus a naive termwise bridge fails.

However, the project's signed orbit-splitting measure is invariant under

\[
\rho\mapsto1-\rho.
\]

For every finite reflection-invariant signed measure,

\[
\int g_n\,d\nu
=
\int f_n\,d\nu.
\]

This yields a candidate exact bridge between the finite-factor Li-type derivative response and the project's signed zero-kernel response.

### Mathematical claim supported

A direct algebraic proof supports the reflection-invariant finite response identity.

The proposition has not yet been promoted to PROVED IN PROJECT.

### What remains unproved or unaudited

Independent symbolic validation.

Arbitrary-precision numerical validation across nontrivial parameter families.

Novelty.

Any realization of the signed factor ratio as an entire arithmetic zeta-like deformation.

Any implication for RH.

### Largest current weakness

The finite factor ratio contains negative zero multiplicities and is generally rational.

The project still lacks an admissible entire or arithmetic deformation corresponding to its signed response model.


---

## Phase 1D — Reflection-Mediated Li Bridge Validation

Status: COMPLETE

### What we built

We independently validated the identity

\[
g_n(z)
=
f_n(1-z),
\]

where \(g_n\) is the finite-factor derivative-side kernel and \(f_n\) is the standard Li zero kernel used in the project.

We validated the single-factor derivative formula symbolically for fixed integer indices as an adversarial check of the written general proof.

We compared the standard and inverse-phase orbit responses using arbitrary-precision arithmetic.

We deliberately removed reflection symmetry and observed that the response equality generally broke.

### Mathematical claim supported

The project promotes the reflection-invariant finite Li response proposition to PROVED IN PROJECT.

For every finite signed point measure \(\nu\) invariant under

\[
z\mapsto1-z
\]

and supported away from \(0\) and \(1\),

\[
\int g_n\,d\nu
=
\int f_n\,d\nu.
\]

### What remains unproved or unaudited

Originality relative to the literature.

Necessity of reflection invariance for broader classes of response identities.

Any realization of the signed perturbation as an entire arithmetic deformation.

Any implication for RH.

### Largest current weakness

The current bridge is exact for a finite signed response and corresponding rational factor.

The project still lacks a natural entire-function deformation preserving enough xi-like structure to make the perturbation more than a response-functional model.
