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


---

## Phase 1E — Entire Finite-Factor Directional Repair

Status: COMPLETE

### What we built

We replaced the rational signed-factor interpretation with a comparison between two degree-four reflection- and conjugation-invariant zero configurations.

The horizontal configuration spreads four zeros away from the critical line.

The vertical configuration spreads four zeros along the critical line.

Both preserve total zero multiplicity.

We derived the matched directional contrast

\[
\mathcal A_f(\delta,\gamma)
=
\sum_{\rho\in H_{\delta,\gamma}}f(\rho)
-
\sum_{\rho\in V_{\delta,\gamma}}f(\rho).
\]

For analytic conjugation-compatible \(f\),

\[
\mathcal A_f(\delta,\gamma)
=
2\delta^2\chi_f(\gamma)
+
O(\delta^4).
\]

Thus

\[
\chi_f(\gamma)
=
\lim_{\delta\to0}
\frac{
\mathcal A_f(\delta,\gamma)
}{
2\delta^2
}.
\]

### Mathematical claim supported

A direct Taylor expansion supports the horizontal–vertical analytic contrast proposition.

The result has not yet been promoted to PROVED IN PROJECT.

### What remains unproved or unaudited

Independent symbolic validation.

Arbitrary-precision numerical validation.

Originality.

Whether the directional contrast has meaningful structure beyond standard harmonicity when applied to RH diagnostics.

Any connection to a global xi-like deformation.

### Largest current weakness

The degree-four factors are entire finite models but remain analytically and arithmetically remote from the full Riemann xi-function.


---

## Phase 1F — Quarter-Turn Directional Contrast Validation

Status: COMPLETE

### What we built

We refined the horizontal-versus-vertical contrast expansion.

The original \(O(\delta^4)\) contrast remainder was not sharp.

The quarter-turn relation between horizontal and vertical displacement cancels derivative orders congruent to zero modulo four.

Only derivative orders

\[
4k+2
\]

survive.

For conjugation-compatible analytic kernels,

\[
\mathcal A_f(\delta,\gamma)
=
8
\sum_{k\ge0}
\frac{
\delta^{4k+2}
}{
(4k+2)!
}
\Re
f^{(4k+2)}
\left(
\frac12+i\gamma
\right).
\]

Hence

\[
\mathcal A_f(\delta,\gamma)
=
2\delta^2\chi_f(\gamma)
+
\frac{\delta^6}{90}
\Re
f^{(6)}
\left(
\frac12+i\gamma
\right)
+
O(\delta^{10}).
\]

### Mathematical claim supported

The quarter-turn directional contrast expansion is now PROVED IN PROJECT.

The Li-kernel sixth-order residual law is also PROVED IN PROJECT.

### What remains unproved or unaudited

Novelty relative to the literature.

Whether the higher derivative hierarchy contains arithmetic information rather than only generic analytic geometry.

Whether comparison with a second RH-related diagnostic produces a nontrivial distinction.

Any implication for RH.

### Largest current weakness

The strongest structural result is still generic complex analysis applied to the project response geometry.

The project must now determine whether a diagnostic-specific distinction survives after the generic analytic mechanism is factored out.


---

## Phase 2A — Explicit-Formula Kernel Susceptibility

Status: COMPLETE

### What we derived

For the individual explicit-formula zero kernel

\[
p_L(z)
=
-\frac{e^{Lz}}{z},
\]

we derived

\[
p_L''(z)
=
-e^{Lz}
\left(
\frac{L^2}{z}
-
\frac{2L}{z^2}
+
\frac2{z^3}
\right).
\]

The critical-line native amplitude is

\[
e^{L/2}.
\]

After exact removal of this amplitude, define

\[
\widetilde\chi_L^{\mathrm{EF}}
=
e^{-L/2}
\chi_L^{\mathrm{EF}}.
\]

A candidate phase-preserving scaling result is:

if

\[
L\gamma\to c>0,
\]

then

\[
\gamma^3
\widetilde\chi_L^{\mathrm{EF}}(\gamma)
\to
-4c\cos c
+
2(2-c^2)\sin c.
\]

### Cross-diagnostic comparison

The Li kernel uses phase coordinate

\[
n/\gamma
\]

and height exponent \(2\).

The explicit-formula kernel uses phase coordinate

\[
L\gamma
\]

and candidate height exponent \(3\) after native amplitude normalization.

A provisional susceptibility scaling taxonomy

\[
(\Phi,\alpha,\Psi)
\]

has been formulated.

### Mathematical claim supported

A manual exact derivative calculation and asymptotic derivation support the explicit-formula scaling candidate.

The result has not yet been promoted to PROVED IN PROJECT.

### What remains unproved or unaudited

Independent symbolic differentiation.

Independent arbitrary-precision validation.

Current literature originality.

Usefulness of the proposed taxonomy.

Whether a third RH-related kernel fits or destroys the taxonomy.

Any implication for RH.

### Largest current weakness

With only two kernel families, the proposed taxonomy may be a retrospective description tailored to the examples already analyzed.

A third out-of-sample diagnostic family will eventually be required.


---

## Phase 2B — Explicit-Formula Susceptibility Validation

Status: COMPLETE

### What we built

We implemented the individual explicit-formula zero kernel using arbitrary-precision arithmetic.

We independently validated the second derivative symbolically and numerically.

We recovered the exact quadratic susceptibility using the finite four-zero quarter-turn directional contrast.

We validated exact removal of the critical-line exponential amplitude

\[
e^{L/2}.
\]

We ran a reproducible mesoscopic scaling campaign for

\[
L\gamma=c.
\]

We also identified that fixed normalization-exponent errors are asymptotically invisible at leading order because

\[
L\to0
\]

in the phase-preserving scaling regime.

### Mathematical claim supported

The explicit-formula mesoscopic susceptibility scaling law is now PROVED IN PROJECT:

if

\[
\gamma_j\to\infty
\]

and

\[
L_j\gamma_j\to c>0,
\]

then

\[
\gamma_j^3
e^{-L_j/2}
\chi_{L_j}^{\mathrm{EF}}(\gamma_j)
\to
-4c\cos c
+
2(2-c^2)\sin c.
\]

### Cross-diagnostic state

The project now has two validated families:

1. Li kernel:
   phase coordinate \(n/\gamma\),
   height exponent \(2\);

2. explicit-formula kernel:
   phase coordinate \(L\gamma\),
   height exponent \(3\) after exact native amplitude removal.

### What remains unproved or unaudited

Originality.

General validity of the proposed susceptibility scaling taxonomy.

Whether the taxonomy survives a third out-of-sample diagnostic family.

Any shared detection-cost comparison.

Any implication for RH.

### Largest current weakness

The taxonomy has been inferred from exactly two kernel families.

A third diagnostic must be selected before the project can claim that the framework has predictive rather than retrospective value.


---

## Phase 2C — Third-Family Out-of-Sample Prediction Freeze

Status: COMPLETE

### What we selected

The third kernel family is the resolvent kernel

\[
r_a(z)
=
\frac1{a-z},
\qquad
a>\frac12.
\]

### Frozen pre-derivation predictions

The project predicts the similarity coordinate

\[
\frac{a-\frac12}{\gamma}.
\]

Under

\[
\frac{a-\frac12}{\gamma}\to c>0,
\]

the project predicts a height exponent

\[
3
\]

and a rational limiting susceptibility profile.

For fixed \(a\), the project predicts

\[
O_a(\gamma^{-4})
\]

decay with a leading coefficient proportional to

\[
a-\frac12.
\]

The project also predicts that the taxonomy must replace the phrase

"phase coordinate"

with

"asymptotic similarity coordinate."

### Mathematical claim supported

None yet.

This phase intentionally freezes predictions before exact derivation.

### What remains unknown

Whether any prediction is correct.

The exact second derivative has not been derived in the project at the time of this commit.

### Largest current risk

The prediction may be largely dimensional analysis and may fail to reveal anything deeper than homogeneity of the resolvent kernel.


---

## Phase 2D — Resolvent Out-of-Sample Derivation

Status: COMPLETE

### Exact result

For

\[
r_a(z)
=
\frac1{a-z},
\]

with

\[
d=a-\frac12,
\]

the quadratic susceptibility is

\[
\chi_a^{\mathrm{Res}}(\gamma)
=
\frac{
4d(d^2-3\gamma^2)
}{
(d^2+\gamma^2)^3
}.
\]

### Generic similarity law

If

\[
d/\gamma\to c>0,
\]

then

\[
\gamma^3
\chi_a^{\mathrm{Res}}(\gamma)
\to
\frac{
4c(c^2-3)
}{
(c^2+1)^3
}.
\]

### Frozen prediction score

P-RES-001: PASS.

P-RES-002: PASS.

P-RES-003: PASS as methodological prediction.

P-RES-004: PASS.

### Taxonomy refinement

The resolvent family exposes a distinction between:

1. the generic family height exponent;
2. profile vanishing at a boundary or interior coordinate;
3. the decay rate of the parameter path toward that profile zero;
4. the effective exponent observed in the resulting subregime.

For fixed \(a\),

\[
d/\gamma\to0
\]

and

\[
\Psi_{\mathrm{Res}}(c)
\sim-12c.
\]

This converts the generic exponent \(3\) into the fixed-\(a\) exponent \(4\).

### Mathematical claim supported

The exact susceptibility formula and both asymptotic regimes have direct analytic proofs.

They have not yet undergone independent symbolic or arbitrary-precision validation.

### Largest current weakness

The third-family predictions were strongly informed by homogeneity and dimensional analysis.

The successful scorecard supports the taxonomy as an organizing framework, but does not yet show that it extracts deep RH-specific structure.


---

## Phase 2E — Resolvent Out-of-Sample Validation

Status: COMPLETE

### What we validated

Independent symbolic differentiation validated

\[
r_a''(z)
=
2(a-z)^{-3}.
\]

The exact rational susceptibility formula was independently reduced and checked using arbitrary-precision arithmetic.

The generic similarity profile

\[
\Psi_{\mathrm{Res}}(c)
=
\frac{
4c(c^2-3)
}{
(c^2+1)^3
}
\]

was validated.

The fixed-\(a\) boundary law

\[
\gamma^4
\chi_a^{\mathrm{Res}}(\gamma)
\to
-12
\left(
a-\frac12
\right)
\]

was validated.

The exact profile zero and susceptibility sign transition at

\[
c=\sqrt3
\]

were validated.

### Frozen prediction result

P-RES-001: PASS.

P-RES-002: PASS.

P-RES-003: PASS as methodological prediction.

P-RES-004: PASS.

Validated score:

\[
4/4.
\]

### Taxonomy state

The susceptibility scaling framework has now survived a frozen third-family out-of-sample test inside the project.

The term

"asymptotic similarity coordinate"

replaces the narrower term

"phase coordinate"

in the working taxonomy.

Profile degeneracy is now recognized as a distinct structural issue because zeros and vanishing orders of the limiting profile can alter effective decay exponents on special parameter paths.

### What remains unproved or unaudited

Literature originality.

A general theorem guaranteeing susceptibility signatures for a broad kernel class.

A shared cost model across diagnostics.

A transition from individual zero kernels to complete RH-equivalent criteria.

Any implication for RH.

### Largest current weakness

The three-family taxonomy may still be a repackaging of elementary scaling and homogeneity principles.

The next stage must perform a serious prior-art audit before the project presents the taxonomy as a potential mathematical contribution.


---

## Phase 3A — Prior-Art Audit Protocol and Novelty Quarantine

Status: COMPLETE

### Why this phase exists

The project has accumulated exact analytic and computational results across three individual RH-related zero-kernel families.

However, several central mechanisms resemble standard mathematics:

- complex Taylor expansion;
- harmonicity;
- roots-of-unity filtering;
- dimensional analysis;
- similarity scaling.

The project therefore freezes seven prior-art questions before drawing originality conclusions.

### Audit targets

Q1: quarter-turn finite-difference operator.

Q2: derivative-order filter selecting orders congruent to 2 modulo 4.

Q3: horizontal-versus-vertical displacement of functional-equation-symmetric zero quartets.

Q4: Li coefficient response to hypothetical zero displacement.

Q5: quadratic second-directional sensitivity of RH-related zero kernels.

Q6: comparative scaling signatures for zero kernels or RH diagnostics.

Q7: profile degeneracy and enhanced decay on special parameter paths.

### Novelty status

All originality-sensitive central claims are quarantined.

No novelty conclusion has been reached.

### Level IV RH consequence

None established.

### Largest current weakness

A current-literature prior-art campaign has not yet been completed.

Until that campaign is performed, the mathematical originality of the project-specific construction and taxonomy remains unresolved.


---

## Phase 3B — Reproducible Prior-Art Search Campaign Design

Status: COMPLETE

### What we built

The project translated the seven frozen prior-art questions into exact-object, mathematical-ancestor, and RH-application search families.

A query matrix was created for:

- Google Scholar;
- arXiv;
- MathSciNet;
- zbMATH Open.

A source-capture template now requires precise mathematical comparison between retained prior art and project claims.

A terminology risk register was created for:

- mesoscopic;
- susceptibility;
- scaling signature;
- similarity coordinate;
- zero surgery.

### Important pre-search predictions

The project expects strong prior art for the generic quarter-turn derivative filter.

The project also expects the generic profile-degeneracy principle to be standard asymptotic analysis.

The Li zero-displacement literature is treated as the highest-priority threat to project-specific framing.

### Novelty status

Unresolved.

No literature conclusions were drawn in this phase.

### Largest current weakness

The current chat environment cannot execute a current July 2026 literature search.

The search campaign must be run externally and the retained primary sources brought back into the repository for claim disposition.


---

## Phase 4A — Li Quadratic-Response Blind-Scale Theory

Status: COMPLETE

### What we derived

The leading Li susceptibility profile

\[
\Psi_{\mathrm{Li}}(c)
=
-2c(c\cos c+2\sin c)
\]

has infinitely many positive simple zeros.

There is exactly one root

\[
c_k
\]

in each interval

\[
\left(
\left(k+\frac12\right)\pi,
(k+1)\pi
\right),
\]

and the roots satisfy

\[
\tan c_k=-c_k/2.
\]

A candidate two-term coupled susceptibility expansion was derived:

\[
\chi_n^{\mathrm{Li}}(\gamma)
=
\gamma^{-2}
\Psi_{\mathrm{Li}}(q)
+
\gamma^{-4}
K_{\mathrm{Li}}(q)
+
O_q(\gamma^{-6}),
\qquad
q=n/\gamma.
\]

At an exact profile zero,

\[
q=c_k,
\]

the generic gamma^-2 term vanishes and the gamma^-4 term survives.

The exact candidate blind-scale coefficient is

\[
\frac{
c_k^2(c_k^2+4)
}{
12
}
\cos c_k.
\]

### Near-blind transition hierarchy

If

\[
n/\gamma-c_k
\sim
\beta\gamma^{-r},
\]

the candidate effective response exponent is

\[
2+\min(r,2),
\]

subject to a possible further coefficient cancellation at the critical approach rate r=2.

### Negative result

The profile magnitude is unbounded.

There is no unconstrained globally optimal response coordinate.

### Mathematical claim supported

Direct analytic derivations support the blind-scale location theorem, two-term susceptibility expansion, exact matched blind-scale asymptotic, and near-blind transition hierarchy.

These claims have not yet undergone independent symbolic or arbitrary-precision validation.

### Largest current weakness

The blind-scale theory remains local to the individual Li zero-kernel quadratic response.

No global Li coefficient blind-scale theorem has been established.


---

## Phase 4B — Li Blind-Scale Adversarial Validation

Status: COMPLETE

### What we validated

The positive nonzero profile zeros were computed with arbitrary-precision monotone bisection and found in the analytically predicted intervals.

The large-index blind-scale asymptotic was validated.

Independent symbolic coefficient extraction reproduced the gamma^-2 and gamma^-4 coupled susceptibility profiles.

Exact matched paths

\[
\gamma=n/c_k
\]

validated the gamma^-4 blind-scale law.

Near-blind paths were enforced by solving

\[
n/\gamma-c_k
=
\beta\gamma^{-r}
\]

for gamma with integer n fixed.

The transition exponents

\[
2.5,\ 3,\ 3.5,\ 4,\ 4
\]

were reproduced for

\[
r=1/2,\ 1,\ 3/2,\ 2,\ 3.
\]

### Mathematical claim supported

The Li individual-kernel quadratic-response blind-scale hierarchy is now PROVED IN PROJECT.

### Current research frontier

The major unresolved question is whether the local blind-scale cancellation survives any mathematically controlled passage to a finite or truncated global Li zero sum.

### Largest current weakness

The present theorem concerns one kernel contribution and a synthetic finite orbit geometry.

Global Li coefficients aggregate contributions from the entire zero multiset.

Collective phase structure may erase, shift, or qualitatively alter the local blind-scale phenomenon.


---

## Phase 4C — Finite-Orbit Blind-Scale Aggregation

Status: COMPLETE

### What we derived

For a finite family of critical-line orbit heights

\[
a_j\Gamma,
\]

the aggregate quadratic response has leading coupled profile

\[
\Psi_{\mathbf a,\mathbf w}^{\mathrm{agg}}(c)
=
\sum_j
w_j a_j^{-2}
\Psi_{\mathrm{Li}}(c/a_j).
\]

Thus the individual blind-scale profile does not simply persist under aggregation.

### Two-orbit resonance

For equal-weight relative heights \(1\) and \(a\), an individual blind coordinate \(c_k\) remains aggregate-blind at leading order if and only if

\[
a=c_k/c_m
\]

for another individual profile zero \(c_m\).

The project calls this blind-scale ratio resonance.

### Fourth-order response

At resonance,

\[
K_{k,m}^{(2)}
=
K(c_k)
+
(c_m/c_k)^4K(c_m).
\]

Same-parity resonant pairs have correction terms of the same sign and therefore cannot cancel at fourth order.

### Mathematical claim supported

Direct finite-sum asymptotics support the aggregate profile and resonance theorems.

The claims have not yet undergone independent symbolic or arbitrary-precision validation.

### Current frontier

Opposite-parity resonances may permit stronger fourth-order cancellation.

The existence, nonexistence, or asymptotic density of such near-cancellations is unknown inside the project.

### Largest current weakness

The relative orbit heights are synthetic parameters.

The project has not connected blind-scale ratio resonance to actual zeta zero-height ratios or to the infinite Li zero sum.


---

## Phase 4D — Two-Orbit Resonance Noncancellation

Status: COMPLETE

### What we proved

The blind-scale fourth-order correction admits the exact form

\[
K(c_k)
=
(-1)^{k+1}
\frac{
c_k^2\sqrt{c_k^2+4}
}{
6
}.
\]

After rescaling the two-orbit resonant coefficient, the cancellation problem is controlled by

\[
F(x)=x^6\sqrt{x^2+4}.
\]

The function F is strictly increasing.

Therefore no two distinct blind scales can produce exact opposite-parity fourth-order cancellation.

Every equal-weight two-orbit blind-scale ratio resonance has exact aggregate response exponent 4.

### Relative near-cancellation

Adjacent opposite-parity resonances satisfy

\[
R_{k,k+1}
\sim
\frac{7\pi}{2c_k}
\to0.
\]

Thus normalized relative cancellation becomes arbitrarily strong.

However,

\[
|K_{k,k+1}^{(2)}|
\sim
\frac{7\pi}{6}c_k^2,
\]

so the absolute aggregate coefficient grows.

### Validation

Independent symbolic derivation passed.

An arbitrary-precision scan of 40,000 ordered resonant pairs found no exact cancellation.

The minimum observed normalized cancellation ratio was approximately

\[
0.0175859577499984
\]

at ordered pair

\[
(199,198).
\]

Adjacent asymptotic laws were numerically validated.

Direct finite-orbit scaling experiments reproduced:

- Gamma^-2 response restoration for a nonresonant second orbit;
- Gamma^-4 response survival for a resonant second orbit.

The complete automated test suite passed:

\[
107\text{ passed},\quad0\text{ failed}.
\]

### Current frontier

Exact fourth-order cancellation is impossible with two equal-weight resonant orbit contributions.

The next structural question is whether three or more resonant orbit contributions can balance exactly at fourth order.

### Largest current weakness

All orbit-height ratios remain synthetic.

No arithmetic connection to actual zeta zero-height ratios has been established.


---

## Phase 4E — Multi-Orbit Signed-Moment Reduction

Status: COMPLETE

### Exact reduction

For a fully aligned resonant family, define

\[
A_k
=
c_k^6\sqrt{c_k^2+4}.
\]

Then the fourth-order aggregate coefficient satisfies

\[
6c_{k_1}^4K_{\mathrm{agg}}
=
\sum_j
w_j(-1)^{k_j+1}A_{k_j}.
\]

Thus multi-orbit cancellation is exactly a signed weighted-moment problem separated by blind-scale parity.

### Continuous weights

Same-parity positive-weight families cannot cancel.

Every mixed-parity index family admits positive real weights with exact cancellation.

For normalized positive weights, the cancellation set is a codimension-one affine slice of the weight simplex.

A transverse weight perturbation restores the fourth-order coefficient linearly.

### Research correction

Arbitrary positive real weight optimization is not a meaningful rigid-cancellation frontier.

It can manufacture exact cancellation by solving one linear equation.

### Equal-weight three-orbit frontier

For three equal-weight orbits, exact cancellation requires

\[
A_r=A_p+A_q,
\]

where the unique-parity index obeys

\[
r>\max(p,q).
\]

At large indices,

\[
A_k
\sim
\pi^7(k+1/2)^7,
\]

which gives an asymptotic candidate geometry but not a Fermat equation.

### Current frontier

Search the equal-weight three-orbit equation using parity and monotonicity reductions.

Near-cancellation must be judged using a normalized defect and compared against the natural local spacing scale of the sequence A_k.

### Largest current weakness

The rigid signed-moment problem remains entirely inside a synthetic blind-scale orbit model.

No connection to actual zeta zero heights is established.


---

## Phase 4F — Equal-Weight Three-Orbit Search

Status: COMPLETE

### Search

The project searched the rigid equal-weight equation

\[
A_r=A_p+A_q
\]

subject to the required blind-scale parity and ordering constraints.

The search reached blind-scale index 2999 and recorded 3,357,233 candidate records at the full checkpoint.

Binary search in the opposite-parity moment subsequence replaced cubic triple enumeration.

### Strongest candidate

The strongest parity-local candidate was

\[
(p,q,r)=(1995,2225,2350).
\]

Its global normalized defect was approximately

\[
4.4321\times10^{-11}.
\]

Its parity-local spacing defect was approximately

\[
1.49203844\times10^{-7}.
\]

### Search prediction score

The four frozen qualitative predictions all passed.

### Limitation

No exact equality was certified.

Finite search does not prove global nonexistence.

---

## Phase 4G — Three-Orbit High-Precision and Extreme-Value Audit

Status: COMPLETE

### High-precision audit

The top 15 candidates were independently recomputed at 500 decimal digits.

The strongest candidate remained nonzero and its normalized defects were stable to extreme relative accuracy.

### Extreme-value benchmark

The full search contained

\[
M=3,357,233
\]

candidate records.

Under the declared crude iid Uniform(0,1/2) benchmark, the expected minimum parity-local defect is approximately

\[
1.4893\times10^{-7}.
\]

The observed minimum was approximately

\[
1.4920\times10^{-7}.
\]

The observed-to-expected ratio was

\[
1.00182443666\ldots.
\]

The crude benchmark probability of obtaining a minimum no larger than the observed value was approximately

\[
0.632791065.
\]

### Research conclusion

The search found no evidence of anomalous equal-weight three-orbit additive resonance in the searched range.

The extremely small global normalized defect was explained as non-anomalous after parity-local spacing normalization and search-multiplicity comparison under the declared heuristic benchmark.

### Mathematical claim supported

Negative computational result:

No additive blind-scale moment conjecture is promoted from the Phase 4F search.

### Current weakness

The extreme-value benchmark is heuristic.

No deterministic distribution theorem for parity-local defects has been proved.

### Strategic frontier

The project must decide whether to continue studying synthetic finite-orbit signed-moment spacing or redirect toward actual zeta zero data and controlled truncated Li zero sums.


---

## Phase 5A — Actual Zeta-Zero Window Bridge

Status: COMPLETE

### Strategic redirection

The project stopped the synthetic three-orbit additive-resonance branch after Phase 4G found no anomalous additive structure in the searched range.

Phase 5A redirects toward finite windows of numerically computed Riemann zeta zero ordinates.

### Discrete response object

The truncated window susceptibility is

\[
\mathcal W_n(H,\eta)
=
\sum_{H\le\gamma_j\le(1+\eta)H}
\chi_n^{\mathrm{Li}}(\gamma_j).
\]

### Smooth-density prediction

Under the leading smooth zero-density model and n/H -> c,

\[
\frac H{\log H}
\mathcal W_n(H,\eta)
\]

is heuristically predicted to follow

\[
\Phi_\eta(c)
=
\frac{c}{\pi}
\left[
(1+\eta)^{-2}
\sin(c/(1+\eta))
-
\sin c
\right].
\]

### Structural consequence

A positive-width height window samples individual susceptibility coordinates over

\[
[c/(1+\eta),c].
\]

Therefore individual blind-scale cancellation should generically be smeared.

### Consistency law

The continuum profile satisfies

\[
\lim_{\eta\to0^+}
\frac{\Phi_\eta(c)}{\eta}
=
\frac{\Psi_{\mathrm{Li}}(c)}{2\pi}.
\]

### Frozen predictions

P-ZETA-001:

Positive-width windows smear individual blind scales.

P-ZETA-002:

H/log H normalized high-zero window susceptibility broadly follows the smooth-density window profile.

P-ZETA-003:

Empirical window-response zeros track smooth-density window-profile zeros more closely than individual blind scales when windows contain sufficiently many computed zero ordinates.

### Current frontier

Generate a reproducible finite zeta-zero data set and test the frozen window-profile predictions.

### Largest current weakness

The continuum profile is heuristic.

Discrete zero fluctuations and finite-height corrections may dominate at computationally accessible heights.


---

## Phase 5B — Finite Zeta-Zero Data Generation and Occupancy Audit

Status: COMPLETE

### Dataset

The project generated a finite computational dataset containing 500 critical-line zeta zero ordinates returned by the selected mpmath backend.

The ordinates span approximately

\[
14.1347
\]

through

\[
811.1844.
\]

Per-ordinate direct zeta residual evaluation was performed under the declared numerical gate.

### Occupancy audit

The project audited relative-height windows for

\[
\eta=0.05,\ 0.10,\ 0.20,\ 0.50.
\]

Among complete windows, occupancy ranged from 1 to 170 zeros.

There were:

\[
29
\]

complete windows with at least 10 zeros,

\[
18
\]

with at least 25 zeros,

and

\[
10
\]

with at least 50 zeros.

### Phase decision

The first-500-zero dataset is sufficient for an initial Phase 5C comparison.

The project will stratify comparisons by window occupancy.

Dense and high-occupancy windows are the primary continuum-profile tests.

### Finite-height diagnostic

Because the dataset reaches heights only through approximately 811, Phase 5C will compare the frozen leading profile with a finite-height smooth-density benchmark retaining the full logarithmic density factor.

The frozen prediction remains the official P-ZETA-002 target.

### Largest current weakness

The accessible heights are low relative to the asymptotic regime.

Finite-height corrections and discrete zero fluctuations may remain substantial.


---

## Phase 5C — Actual Zeta-Zero Window Response Test

Status: COMPLETE

### Experiment

The project evaluated the exact finite Li quadratic-response sum over complete windows of the first-500-zero computational data set.

The normalized discrete response

\[
\frac H{\log H}
\mathcal W_n(H,\eta)
\]

was compared with:

1. the frozen Phase 5A smooth-density profile;
2. a finite-height benchmark retaining the logarithmic zero-density factor.

### Occupancy trend

Frozen-profile mean correlation increased from approximately

\[
0.995056
\]

to

\[
0.997805
\]

to

\[
0.998216
\]

across occupancy thresholds of at least 10, 25, and 50 zeros.

### High-occupancy frozen-profile result

For occupancy at least 50:

- window count: 10;
- empirical response-root count: 60;
- mean frozen correlation: approximately 0.998216;
- mean frozen sign agreement: 0.9925;
- mean frozen NRMSE: approximately 0.304070.

The frozen profile reproduced curve shape and sign geometry strongly but retained substantial amplitude discrepancy.

### Finite-height result

For occupancy at least 50, retaining the full logarithmic density factor reduced mean NRMSE to approximately

\[
0.036257.
\]

This is an improvement factor of approximately

\[
8.39.
\]

### Root geometry

At all reported occupancy thresholds, every empirical response root was closer to a window-profile root than to an individual Li blind scale under the protocol nearest-root metric.

### Frozen prediction score

P-ZETA-001:

PASS.

P-ZETA-002:

PASS WITH FINITE-HEIGHT AMPLITUDE QUALIFICATION.

P-ZETA-003:

PASS.

### Main research interpretation

The individual profile does not remain pointwise intact under positive-width actual-zero aggregation.

The aggregate response exhibits a window-level profile consistent with similarity-coordinate averaging under the smooth zero-density model.

At accessible heights, finite-height logarithmic-density corrections are essential for amplitude accuracy.

### Current frontier

Scale the actual-zero experiment to higher zero heights and directly test whether the frozen leading profile closes the amplitude gap with increasing height.

Separately derive a deterministic discrepancy formula tied to the zero-counting error term.

### Largest current weakness

The current experiment reaches only the first 500 computed critical-line zero ordinates, through height approximately 811.

No discrete convergence theorem is established.


---

## Phase 5D — Exact Window-Response Discrepancy Decomposition

Status: COMPLETE

### Exact finite-dataset identity

For the empirical counting function

\[
N_D(T)
=
\#\{\gamma_j\le T\},
\]

the project defines

\[
E_D(T)
=
N_D(T)-M(T),
\]

where

\[
M'(T)
=
\frac{1}{2\pi}\log(T/(2\pi)).
\]

The discrete zero-window response admits an exact Stieltjes decomposition into an exact smooth-density response and an empirical counting remainder.

### Phase 5C residual decomposition

The finite-height profile benchmark uses the leading Li susceptibility profile inside the smooth density integral.

Thus

\[
\mathcal W_n-S_{\mathrm{profile}}
=
R_{\mathrm{count}}
+
R_{\mathrm{kernel}}.
\]

The two terms separately represent:

- empirical counting fluctuation;
- local Li-kernel asymptotic truncation.

### Candidate scale hierarchy

The validated susceptibility expansion predicts normalized smooth kernel remainder scale

\[
O(H^{-2}).
\]

Under a logarithmic counting-remainder scale, the normalized counting contribution is predicted at

\[
O(H^{-1}).
\]

### Endpoint correction

Because Phase 5C uses zero ordinates as left window anchors and includes the left endpoint, the exact discrete statistic contains an atom contribution

\[
\chi_n^{Li}(H).
\]

This contribution must be separately quantified.

### Frozen predictions

P-DEC-001:

Exact numerical decomposition closes.

P-DEC-002:

Counting remainder dominates kernel remainder in RMS size for dense windows.

P-DEC-003:

Kernel remainder exhibits steeper height decay than counting remainder.

P-DEC-004:

Removing the left atom improves agreement slightly but does not explain most high-occupancy residual.

### Current frontier

Compute every discrepancy component independently on the frozen Phase 5C windows and grade the four predictions.

### Largest current weakness

The O(H^-1) counting-remainder scale is conditional on a logarithmic-size remainder heuristic or known classical-type scale.

The project has not proved a new bound for zero-counting error.


---

## Phase 5E-R — Atomic Endpoint Provenance Repair

Status: COMPLETE

### Initial failure

The independent Stieltjes evaluator failed with maximum discrepancy approximately

\[
0.0354075785.
\]

A first attempt to repair discontinuous staircase quadrature did not resolve the issue.

### Root cause

The occupancy CSV serialized H to 60 displayed decimal digits.

The zero dataset stored ordinates to 75 displayed decimal digits.

The numerical H reconstructed from the occupancy file was therefore not exactly the authoritative zero ordinate.

For an atomic counting measure, this changes endpoint membership.

The experiment nevertheless assumed

\[
\Delta N_D(H)=1.
\]

This produced inconsistent endpoint semantics.

### Audit

Among 40 complete occupancy rows:

- 0 serialized anchors were exact;
- 12 were rounded below the zero;
- 28 were rounded above the zero.

Every authoritative dataset anchor had unit empirical counting jump.

### Repair

H is now recovered from the stored anchor zero index and the authoritative frozen zero dataset.

The E_D-weighted derivative integral is evaluated piecewise on intervals with constant empirical count.

### Validation

Six targeted adversarial cases closed with maximum error approximately

\[
4.08\times10^{-82}.
\]

### Mathematical disposition

The Stieltjes identity survived.

The failed first run is classified as an endpoint-provenance implementation failure.

### Consequence for Phase 5C

The original Phase 5C experiment used the same rounded-H reconstruction pattern.

Its exact numerical metrics are marked REVALIDATION REQUIRED.

The profile conclusion is not withdrawn but must be rerun with authoritative anchors.


---

## Phase 5E — Corrected Independent Discrepancy Decomposition

Status: COMPLETE

### Validation status

The initial Phase 5E execution failed because of atomic endpoint provenance.

After Phase 5E-R repaired the endpoint semantics, the full 360-point dense-window decomposition experiment was rerun.

Maximum decomposition closure error was approximately

\[
6.19\times10^{-61}.
\]

Maximum direct-versus-Stieltjes counting-remainder discrepancy was approximately

\[
6.19\times10^{-61}.
\]

### Component hierarchy

Counting-remainder RMS exceeded kernel-remainder RMS in every tested dense and high-occupancy window.

For high-occupancy windows, the ratio of mean normalized component RMS sizes was approximately

\[
3115.3.
\]

Thus empirical zero-counting fluctuation dominates the local Li-kernel asymptotic truncation component in the tested finite data.

### Height trends

The descriptive finite-range slopes were approximately

\[
-1.734
\]

for the counting component and

\[
-1.857
\]

for the kernel component.

The kernel trend was steeper, as predicted.

The observed slopes are not treated as identification of asymptotic exponents.

### Endpoint atom prediction failure

Removing the explicit left zero-anchor atom worsened high-occupancy residual RMS.

The mean open-to-closed residual RMS ratio was approximately

\[
2.435.
\]

P-DEC-004 therefore failed.

### Prediction score

P-DEC-001:

PASS.

P-DEC-002:

PASS.

P-DEC-003:

PASS WITH FINITE-RANGE QUALIFICATION.

P-DEC-004:

FAIL.

### Main research interpretation

The Phase 5C finite-height profile residual is decomposed into mathematically distinct mechanisms.

In the tested finite data, the empirical counting-remainder component overwhelmingly exceeds the Li-kernel asymptotic truncation component.

### Immediate revalidation requirement

Phase 5C must now be rerun with authoritative zero anchors before its exact correlation, NRMSE, sign-agreement, and root-win metrics are retained.

### Largest current weakness

The project has not proved an asymptotic theorem connecting the finite empirical counting-remainder hierarchy to the complete zeta zero sequence.


---

## Phase 5C-R — Authoritative-Anchor Revalidation

Status: COMPLETE

### Reason for revalidation

Phase 5E-R established that rounded occupancy-file H values were not safe for reconstructing atomic zero-window endpoints.

The original Phase 5C experiment used those rounded values.

Its metrics were therefore placed under REVALIDATION REQUIRED status.

### Corrected execution

Phase 5C was rerun with H recovered from the authoritative frozen zero dataset using anchor_zero_index.

All original experimental metrics and protocol choices were preserved.

### Corrected high-occupancy metrics

For occupancy at least 50:

- window count: 10;
- empirical root count: 60;
- frozen-profile NRMSE: approximately 0.299628;
- finite-height NRMSE: approximately 0.0359835;
- frozen correlation: approximately 0.998639;
- finite-height correlation: approximately 0.998381;
- frozen sign agreement: 0.9975;
- finite-height sign agreement: 0.9975;
- frozen window-root win rate versus individual blind scales: 1.0;
- finite-height root-win rate versus individual blind scales: 1.0.

### Comparison with pre-repair results

The corrected frozen NRMSE improved slightly.

The corrected finite-height NRMSE improved slightly.

Frozen-profile correlation and sign agreement increased.

The finite-height mean correlation decreased slightly.

The root-win results were unchanged.

### Corrected prediction grades

P-ZETA-001:

PASS.

P-ZETA-002:

PASS WITH FINITE-HEIGHT AMPLITUDE QUALIFICATION.

P-ZETA-003:

PASS.

### Main conclusion

The broad actual-zero response-profile conclusion survives authoritative endpoint reconstruction.

The finite data remain strongly consistent, in curve shape and response-zero geometry, with the smooth-density window profile.

The finite-height density factor remains essential for amplitude accuracy.

### Reporting rule

Archived pre-repair Phase 5C metrics are historical validation artifacts only.

All final project reporting must use corrected authoritative-anchor metrics.

### Largest current weakness

The experiment remains restricted to the first 500 computed critical-line zero ordinates and does not establish a discrete convergence theorem.


---

## Phase 5F — Deterministic Counting-Response Transfer Inequality

Status: COMPLETE

### Exact transfer transform

The empirical counting contribution is decomposed into an explicit left atom and a linear transform of the counting discrepancy.

For the non-atomic transform,

\[
\mathcal T[E]
=
f(B)E(B)
-
f(H)E(H)
-
\int_H^B E(t)f'(t)dt.
\]

### Sup-norm stability

The project proved

\[
|\mathcal T[E]|
\le
\Lambda_n(H,\eta)\|E\|_\infty,
\]

where

\[
\Lambda_n(H,\eta)
=
|f(H)|
+
|f(B)|
+
\operatorname{Var}_{[H,B]}(f).
\]

Thus counting-discrepancy transfer is controlled by endpoint kernel magnitude and kernel total variation.

### Holder-family stability

For conjugate p and q,

\[
|\mathcal T[E]|
\le
|f(B)||E(B)|
+
|f(H)||E(H)|
+
\|E\|_p\|f'\|_q.
\]

The L2 certificate is selected for empirical comparison with the sup-norm certificate.

### Derivative-response profile

The leading derivative profile is

\[
J_{Li}(q)
=
2q^3\sin q
-
12q^2\cos q
-
12q\sin q.
\]

### Continuum transfer envelope

The matched-scale transfer coefficient is predicted to satisfy

\[
H^2\Lambda_n(H,\eta)
\to
\mathcal L_\eta(c).
\]

The envelope combines:

- lower endpoint response magnitude;
- upper endpoint response magnitude;
- integrated derivative-response magnitude.

### Profile-to-transfer ratio

The project defines

\[
Q_\eta(c)
=
|\Phi_\eta(c)|/\mathcal L_\eta(c).
\]

At a smooth response-profile root,

\[
Q_\eta(c)=0.
\]

Therefore response blindness does not automatically imply counting stability.

### Frozen predictions

P-TRN-001:

Matched-scale transfer-envelope convergence.

P-TRN-002:

Pointwise validity of the exact sup-norm empirical transfer certificate.

P-TRN-003:

L2 certificate generally tighter than L-infinity certificate.

P-TRN-004:

Empirical root neighborhoods have lower profile-to-transfer ratio than generic coordinates.

P-TRN-005:

Coordinate-dependent transfer predictor explains empirical residual magnitude better than height alone.

### Current frontier

Validate the transfer envelope and determine whether the deterministic stability coefficient is merely a worst-case bound or an empirically explanatory statistic.

### Largest current weakness

The transfer coefficient uses absolute values and may erase signed cancellation responsible for actual counting-remainder behavior.


---

## Phase 5G — Transfer-Envelope Validation and Explanatory-Power Test

Status: COMPLETE

### Matched-scale envelope

The exact transfer coefficient H^2 Lambda converged numerically to the continuum transfer envelope in all frozen validation cases.

P-TRN-001:

PASS.

### Deterministic certificate

The sup-norm transfer certificate passed all 360 dense-window decomposition points.

P-TRN-002:

PASS.

### Certificate tightness

The L2 Holder certificate was tighter than the L-infinity variation certificate at all 360 tested points.

P-TRN-003:

PASS.

No universal ordering theorem is claimed.

### Root-neighborhood Q geometry

The median profile-to-transfer ratio at 108 empirical response roots was approximately

\[
7.37\times10^{-5}.
\]

The median at 1008 generic coordinates was approximately

\[
7.13\times10^{-3}.
\]

The root-to-generic median ratio was approximately

\[
0.01033.
\]

P-TRN-004:

PASS.

### Explanatory-power test

The natural-log correlation between normalized counting-remainder magnitude and the continuum transfer predictor was approximately

\[
0.848764.
\]

The corresponding height-only correlation was approximately

\[
0.394907.
\]

The transfer predictor exceeded the height-only baseline by approximately

\[
0.453858.
\]

P-TRN-005:

PASS.

### Prediction score

All five frozen Phase 5F transfer predictions passed.

### Main research interpretation

The project now distinguishes:

- local Li response geometry through Psi_Li;
- smooth positive-width window-response geometry through Phi_eta;
- deterministic counting-discrepancy transfer geometry through L_eta.

The project-defined ratio Q_eta compares smooth profile magnitude with worst-case transfer geometry.

Empirical response roots occupy substantially lower-Q regions than generic coordinates under the frozen protocol.

The transfer envelope also exhibited explanatory power for corrected counting-remainder magnitude beyond height alone.

### Immediate frontier

A signed transfer model should be investigated to determine whether preserving cancellation information improves explanatory power beyond the absolute-value envelope.

### Prior-art requirement

The three-object response architecture must undergo targeted prior-art review before any originality-sensitive language is permitted.

### Largest current weakness

All actual-zero transfer observations remain limited to the corrected first-500-zero computational dataset.


---

## Phase 6A — Second Prior-Art Audit Freeze

Status: COMPLETE

### Audit target

The project freezes originality-sensitive development around the response architecture

\[
(\Psi_{Li},\Phi_\eta,\mathcal L_\eta,Q_\eta).
\]

The exact Stieltjes discrepancy decomposition and deterministic transfer inequality are included in the audit.

### Standard-mechanism presumption

Stieltjes integration by parts, bounded variation, Holder duality, smooth zero-counting density, and generic matched-scale asymptotics are presumed standard mechanisms pending precise source attribution.

### Critical unresolved questions

The audit asks whether prior literature already contains:

- differential Li/Keiper zero-coordinate response;
- positive-width aggregation of such response;
- an equivalent Phi_eta profile;
- a Li-specific transfer envelope equivalent to L_eta;
- a signal-to-transfer ratio equivalent to Q_eta;
- the combined response architecture.

### Originality status

UNRESOLVED.

### Novelty quarantine

The combined architecture must not be described as novel, a new theory of Riemann zeros, a new approach to RH, a breakthrough, or progress toward proving RH.

### RH consequence status

None.

The project has no new RH-equivalent criterion, positivity theorem, zero-free region, exclusion theorem for off-critical zeros, or proof of RH.

### Current frontier

Complete a targeted primary-source prior-art campaign and assign PA-0 through PA-4 dispositions to Q8 through Q13.

### Largest current limitation

A current primary-source literature search is required before originality-sensitive disposition can be completed.


---

## Phase 6B-A — Transfer-Envelope Proof Dependency Repair

Status: COMPLETE

### Trigger

Adversarial review identified that the original proof dependency for CL-0173 was underjustified.

The susceptibility asymptotic alone did not justify differentiating its big-O remainder in the total-variation term.

### Repair

Starting from the exact susceptibility derivative, introduce

\[
x=1/\gamma,
\qquad
q=n/\gamma.
\]

The scaled exact derivative

\[
G(q,x)=\gamma^3\chi_n'(\gamma)
\]

is smooth and even in \(x\) near \(x=0\), uniformly for \(q\) in compact positive sets.

Since

\[
G(q,0)=-J_{Li}(q),
\]

one obtains

\[
\gamma^3\chi_n'(\gamma)
=
-J_{Li}(q)+O_K(\gamma^{-2})
\]

uniformly.

Using

\[
\big||a+r|-|a|\big|\le|r|,
\]

the absolute derivative integral passes to the continuum profile with an \(O(H^{-2})\) scaled error.

Therefore

\[
H^2\Lambda_n(H,\eta)
=
\mathcal L_\eta(c_H)+O(H^{-2})
\]

uniformly on compact positive matched-scale sets.

### Claim correction

CL-0173 is retained only as a repaired proved claim with dependency on CL-0224 and CL-0225.

### Failure-prevention rule

Numerical convergence does not repair an analytical proof gap.

### RH consequence

None.


---

## Phase 6B — Q12 Signal-to-Transfer Prior-Art Audit

Status: PROVISIONALLY COMPLETE

### Audit object

\[
Q_\eta(c)
=
\frac{|\Phi_\eta(c)|}{\mathcal L_\eta(c)}.
\]

### Strong conceptual prior art

The audit identified:

- matched-filter scoring and direct frequency-selective projection of prime-derived signals at zeta ordinates;
- explicit-formula residue-amplification programs;
- signal-to-noise terminology in zeta-adjacent information-physics manuscripts;
- smoothing and numerical-robustness comparisons for claimed Li-related probes.

### Prior-art disposition

Broad signal/noise, matched-response, spectral visibility, and zero-signal amplification concepts are occupied prior-art territory.

### Precision unresolved object

No inspected source was identified that divides the smooth positive-width Li zero-coordinate susceptibility profile by the matched-scale endpoint-plus-total-variation count-discrepancy transfer envelope of the same kernel.

Originality remains unresolved.

### Adversarial interpretation correction

Because

\[
Q_\eta(c)=|\Phi_\eta(c)|/\mathcal L_\eta(c),
\]

an exact root of Phi_eta automatically yields Q_eta=0 whenever the denominator is positive.

The strong root-versus-generic Q separation in Phase 5G is therefore partly geometry-consistency and tautology-adjacent once empirical response roots are already known to track Phi_eta roots.

P-TRN-004 is not independent evidence of transfer stability or predictive power.

### Current permitted interpretation

Q_eta is a project comparative conditioning or relative-sensitivity descriptor.

### RH consequence

None.


---

## Phase 6B — Q13 Response-Root Sensitivity Prior-Art Audit

Status: PROVISIONALLY COMPLETE

### Precision question

Has prior Li, Keiper, explicit-formula, or zeta-zero-statistic literature explicitly identified roots of a smooth aggregate zero-kernel response as relative-sensitivity locations because the smooth contribution vanishes while a discrepancy-transfer envelope remains nonzero?

### Generic ancestry identified

The audit confirms broad prior-art ancestry for:

- leading-term degeneracy;
- changes of asymptotic order when the nominal leading coefficient vanishes;
- cancellation-induced numerical or analytic sensitivity;
- comparison of main terms with transferred error contributions.

These mechanisms are not project originality candidates.

### Precision unresolved object

No inspected source was identified that constructs the specific comparison

\[
\Phi_\eta(c)=0
\]

and

\[
\mathcal L_\eta(c)>0
\]

for the positive-width aggregate of the local Li zero-coordinate susceptibility.

The corresponding quotient

\[
Q_\eta(c)
=
|\Phi_\eta(c)|/\mathcal L_\eta(c)
\]

remains a project comparative quantity under originality quarantine.

### Current permitted interpretation

At a positive-width Li-susceptibility response root, the smooth-density contribution may vanish while the deterministic worst-case counting-discrepancy transfer envelope remains nonzero.

This is a specialization of standard degeneracy and conditioning ideas.

### RH consequence

None.

---

## Phase 5H — Cancellation-Aware Signed Transfer

Status: PROTOCOL FROZEN

### Research question

Why can the actual signed counting-response residual be much smaller than the absolute-value deterministic transfer envelope?

### New objects

Interior alignment coefficient:

\[
\kappa_{n,H,\eta}
=
\frac{
\int_H^B E_D(t)\chi_n'(t)dt
}{
\|E_D\|_2\|\chi_n'\|_2
}.
\]

Scalar cancellation coefficient:

\[
C_{\mathrm{scalar}}
=
\frac{
|R_{\mathrm{count}}|
}{
|R_{\mathrm{atom}}|
+
|R_{\mathrm{end}}|
+
|R_{\mathrm{int}}|
}.
\]

### Frozen predictions

P-SGN-001 through P-SGN-005.

### Interpretive restriction

The identity relating kappa to the interior residual is definitional.

The full signed component sum is the response target itself after closure.

Phase 5H studies distribution and descriptive cancellation geometry.

It does not establish predictive generalization.

### RH consequence

None.

