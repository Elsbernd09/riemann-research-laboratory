# Zero Surgery Specification

## Phase 0B

This document defines the mathematical meaning of synthetic zero surgery used in the Riemann Research Laboratory.

No numerical implementation is permitted to use the phrase "move a zeta zero" without identifying which surgery level is being performed.

---

# 1. Background symmetry

Let

\[
\xi(s)
=
\frac12 s(s-1)\pi^{-s/2}
\Gamma(s/2)\zeta(s).
\]

The completed Riemann xi-function satisfies

\[
\xi(s)=\xi(1-s)
\]

and

\[
\xi(\overline{s})
=
\overline{\xi(s)}.
\]

Therefore a generic nonreal zero

\[
\rho=\beta+i\gamma
\]

has the symmetry orbit

\[
\mathcal O(\rho)
=
\{
\rho,
1-\rho,
\overline{\rho},
1-\overline{\rho}
\}.
\]

Equivalently,

\[
\mathcal O(\beta+i\gamma)
=
\{
\beta+i\gamma,
1-\beta-i\gamma,
\beta-i\gamma,
1-\beta+i\gamma
\}.
\]

For a critical-line zero with

\[
\beta=\frac12,
\]

the orbit degenerates to the conjugate pair

\[
\left\{
\frac12+i\gamma,
\frac12-i\gamma
\right\}.
\]

---

# 2. Symmetry-preserving quartet surgery

For parameters

\[
0<\delta<\frac12
\]

and

\[
\gamma>0,
\]

define the synthetic off-critical quartet

\[
Q_{\delta,\gamma}
=
\left\{
\frac12+\delta+i\gamma,
\frac12-\delta+i\gamma,
\frac12+\delta-i\gamma,
\frac12-\delta-i\gamma
\right\}.
\]

The baseline critical-line pair is

\[
P_{\gamma}
=
\left\{
\frac12+i\gamma,
\frac12-i\gamma
\right\}.
\]

A formal symmetry-preserving zero-orbit surgery is the multiset operation

\[
\mathfrak S_{\delta,\gamma}:
\mathcal Z
\mapsto
(\mathcal Z\setminus P_\gamma)
\cup
Q_{\delta,\gamma}.
\]

Multiplicity must be tracked explicitly.

This definition acts on a zero multiset only.

It does not, by itself, define a modified zeta function or modified xi-function.

---

# 3. Surgery Level I: zero-orbit surgery

## Definition

Level I surgery modifies only a specified zero multiset.

Input:

- a baseline zero multiset;
- a target critical-line conjugate pair;
- a displacement parameter delta.

Output:

- a new symmetry-preserving zero multiset.

## Permitted claims

A Level I experiment may describe:

- functions defined directly from finite zero sets;
- statistics of the zero configuration;
- finite sums over zeros;
- controlled regularized zero expressions when the regularization is explicitly defined.

## Prohibited claims

A Level I experiment must not claim that the altered zero multiset is the zero set of a new zeta function.

A Level I experiment must not infer an Euler product, Dirichlet series, prime sequence, or explicit formula unless those structures have independently been constructed.

---

# 4. Surgery Level II: canonical-product surgery

## Motivation

A zero set alone does not uniquely determine a general entire function without normalization information.

Multiplication by a zero-free entire factor can preserve the zero set.

For example,

\[
\widetilde F(s)
=
e^{g(s)}F(s)
\]

has the same zeros as \(F\).

However,

\[
\frac{\widetilde F'(s)}
{\widetilde F(s)}
=
g'(s)
+
\frac{F'(s)}
{F(s)}.
\]

Therefore zero-sensitive diagnostics must be separated from normalization-sensitive diagnostics.

## Baseline local pair factor

For a target critical-line pair

\[
\rho_0=\frac12+i\gamma,
\qquad
\overline{\rho_0}=\frac12-i\gamma,
\]

define

\[
B_\gamma(s)
=
\left(1-\frac{s}{\rho_0}\right)
\left(1-\frac{s}{\overline{\rho_0}}\right).
\]

## Synthetic quartet factor

Let

\[
\rho_{+,+}
=
\frac12+\delta+i\gamma,
\]

\[
\rho_{-,+}
=
\frac12-\delta+i\gamma,
\]

\[
\rho_{+,-}
=
\frac12+\delta-i\gamma,
\]

and

\[
\rho_{-,-}
=
\frac12-\delta-i\gamma.
\]

Define

\[
Q_{\delta,\gamma}^{\mathrm{fac}}(s)
=
\prod_{\rho\in Q_{\delta,\gamma}}
\left(1-\frac{s}{\rho}\right).
\]

## Raw surgery multiplier

Define

\[
R_{\delta,\gamma}^{\mathrm{raw}}(s)
=
\frac{
Q_{\delta,\gamma}^{\mathrm{fac}}(s)
}{
B_\gamma(s)
}.
\]

A raw canonical-product surgery applied to a baseline function \(F\) is

\[
F_{\delta,\gamma}^{\mathrm{raw}}(s)
=
F(s)
R_{\delta,\gamma}^{\mathrm{raw}}(s).
\]

This replaces the specified baseline pair with the quartet at the level of the finite factor ratio.

## Warning

The raw multiplier introduces two zeros while removing two zeros.

Therefore the resulting zero-counting geometry differs globally from a pure displacement model.

The project must investigate whether a pair-to-quartet surgery is the correct comparison object or whether a four-zero baseline orbit should instead be used.

This issue is unresolved at Phase 0B.

---

# 5. Multiplicity and zero-count conservation problem

A critical-line orbit under conjugation and the functional equation contains two distinct points.

A generic off-critical orbit contains four distinct points.

Therefore moving a critical-line pair off the critical line while preserving both symmetries changes the number of distinct zero locations from two to four.

This creates a fundamental modeling question.

## Question ZS-001

What is the mathematically correct finite perturbation model for comparing critical-line and off-critical zero configurations while controlling zero count?

Candidate models include:

### Model A: pair-to-quartet bifurcation

Replace one critical-line pair by one off-critical quartet.

Advantage:

- respects the degeneration of a generic symmetry orbit at delta = 0.

Danger:

- distinct-zero count changes for every nonzero delta.

### Model B: doubled critical-line baseline

Start with a multiplicity-two critical-line pair and split it into a generic quartet.

Symbolically,

\[
2P_\gamma
\longrightarrow
Q_{\delta,\gamma}.
\]

Advantage:

- total zero multiplicity is conserved.

Danger:

- actual simple zeta zeros are not multiplicity-two baseline zeros.

### Model C: two-pair transport

Begin with two nearby critical-line pairs

\[
P_{\gamma-h}
\cup
P_{\gamma+h}
\]

and move four zeros into a symmetry-preserving off-line quartet.

Advantage:

- preserves total zero multiplicity.

Danger:

- changes imaginary parts and local spacing geometry.

### Model D: signed response perturbation

Do not construct a literal altered zero set.

Instead define the formal response of a diagnostic by subtracting the baseline pair contribution and adding the off-line quartet contribution with an explicit normalization.

Advantage:

- isolates diagnostic sensitivity.

Danger:

- may not correspond to an entire function in the original class.

No model is selected yet.

---

# 6. Surgery Level III: arithmetic-structural surgery

A Level III construction would require the modified analytic object to preserve additional zeta-like or L-function-like structures.

Possible requirements include:

- functional equation;
- reality/conjugation symmetry;
- prescribed order and growth;
- Dirichlet-series representation;
- Euler-product structure;
- arithmetic coefficients;
- explicit-formula compatibility.

At Phase 0B, no Level III construction is claimed.

The project explicitly rejects the assumption that an arbitrary symmetry-preserving zero displacement can be realized inside the class of zeta-like arithmetic functions.

---

# 7. Diagnostic classification

Every candidate diagnostic must be labeled as one of:

## Zero-determined

Defined solely from the zero multiset under an explicitly stated convergence or regularization convention.

## Normalization-sensitive

Changes under

\[
F(s)\mapsto e^{g(s)}F(s).
\]

## Arithmetic-structure-sensitive

Depends on prime-side, Dirichlet-series, Euler-product, or explicit-formula data not determined by an arbitrary finite synthetic zero perturbation.

Cross-diagnostic comparison is permitted only after this classification is completed.

---

# 8. Current research obstruction

The phrase "move one zeta zero off the critical line" conceals two problems:

1. symmetry-orbit degeneration causes a two-point critical-line orbit to become a four-point off-line orbit;
2. a perturbed zero set does not automatically define a unique zeta-like analytic object.

These are active research-design problems.

No perturbation engine should be written until Question ZS-001 is resolved provisionally.

---

# 9. Phase 0B claim status

No new theorem is claimed.

The symmetry observations are standard consequences of the functional equation and conjugation symmetry of xi.

The surgery taxonomy is project methodology.

Question ZS-001 is an open project design question, not a recognized open problem in analytic number theory.
