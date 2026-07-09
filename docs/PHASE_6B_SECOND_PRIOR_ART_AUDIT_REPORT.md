# Phase 6B Second Prior-Art Audit Report

## Status

PROVISIONALLY COMPLETE.

The audit reviewed the project architecture

\[
(\Psi_{Li},\Phi_\eta,\mathcal L_\eta,Q_\eta)
\]

against Li/Keiper, generalized Li, explicit-formula, zero-statistic, bounded-variation, signal-detection, and adjacent degeneracy literature supplied during the audit.

This report records source-set dispositions only.

It is not a universal novelty certificate.

## Architecture-level disposition

### 1. Broad Li/Keiper sensitivity to off-critical zero geometry

Prior art status:

PA-3.

Voros and related Keiper-Li asymptotic literature explicitly study the large-index effect of off-critical zeros and zero-location geometry.

Project disposition:

No originality claim.

### 2. Symmetric horizontal zero displacement and quadratic response

Prior art status:

PA-3 at the broad structural level.

Prior sources study horizontal displacement of symmetric zero-pair geometry and quadratic small-displacement effects.

Project disposition:

No broad originality claim.

### 3. Parameterized Li-type zero kernels and shifted zero sets

Prior art status:

PA-3.

Generalized Li and tau-Li literature contains parameterized zero kernels and symmetrically shifted product constructions.

Project disposition:

No broad deformation claim.

### 4. Li index/zero-height coupled phase

Prior art status:

PA-3.

Classical and generalized Li representations contain phases equivalent to

\[
n\arctan(1/(2\gamma)),
\]

which exhibit the high-zero ratio \(n/\gamma\).

Project disposition:

No claim of discovering the generic Li index/height similarity variable.

### 5. Li kernels integrated against zero-counting functions or measures

Prior art status:

PA-3.

Stieltjes and Chebyshev representations of Li coefficients against \(N(t)\) or \(dN(t)\) are established.

Project disposition:

No originality claim.

### 6. Finite-height Li truncation

Prior art status:

PA-2 to PA-3.

Incomplete Li coefficients and height-truncated zero sums exist.

Project disposition:

No broad finite-height Li-sum claim.

### 7. Bounded-variation and total-variation transfer machinery

Prior art status:

PA-4 for the generic mechanism.

Explicit-formula and zeta-zero-statistic literature uses bounded-variation test classes and variation-controlled estimates.

Project disposition:

No originality claim for the inequality

\[
|\mathcal T[E]|
\le
\|E\|_\infty
\left(
|f(H)|+|f(B)|+\operatorname{Var}(f)
\right).
\]

### 8. Signal/noise, visibility, matched-response, and main-term/error comparison

Prior art status:

broad conceptual prior art.

Project disposition:

No broad signal-to-noise, matched-filter, visibility, or main-term/error novelty language.

### 9. Generic degeneracy and vanishing-leading-term sensitivity

Prior art status:

standard asymptotic phenomenon.

Project disposition:

No originality claim.

## Precision objects still unresolved in the inspected source set

### A. Local zero-coordinate Hessian of the fixed classical Li kernel

\[
f_n(\rho)
=
1-
\left(
1-\frac1\rho
\right)^n
\]

and

\[
f_n''(\rho)
=
\lim_{\delta\to0}
\frac{
f_n(\rho+\delta)+f_n(\rho-\delta)-2f_n(\rho)
}{
\delta^2
}.
\]

The symmetry-completed critical-line specialization is

\[
\chi_n^{Li}(\gamma)
=
2\Re f_n''(1/2+i\gamma).
\]

No PA-4 source was identified for this exact object in the inspected source set.

### B. Matched susceptibility profile

\[
\gamma^2\chi_n^{Li}(\gamma)
\to
\Psi_{Li}(c),
\qquad
n/\gamma\to c.
\]

The generic Li index/height phase is prior art.

The differentiated-kernel susceptibility profile remains originality unresolved.

### C. Positive-width multiplicative susceptibility aggregation

\[
\sum_{H\le\gamma_j\le(1+\eta)H}
\chi_n^{Li}(\gamma_j)
\]

under

\[
n/H\to c.
\]

No equivalent construction was identified.

### D. Smooth susceptibility profile

\[
\Phi_\eta(c)
=
\frac1{2\pi}
\int_1^{1+\eta}
u^{-2}\Psi_{Li}(c/u)du
\]

with closed form

\[
\Phi_\eta(c)
=
\frac c\pi
\left[
(1+\eta)^{-2}
\sin(c/(1+\eta))
-
\sin c
\right].
\]

No PA-4 source was identified in the inspected source set.

### E. Li-susceptibility transfer envelope

\[
\mathcal L_\eta(c)
\]

as the matched-scale limit of endpoint magnitude plus total variation of the local Li susceptibility kernel.

The generic BV/TV mechanism is standard.

The Li-specific specialization remains originality unresolved.

### F. Profile-to-transfer quotient

\[
Q_\eta(c)
=
\frac{|\Phi_\eta(c)|}{\mathcal L_\eta(c)}.
\]

Generic signal/error and conditioning ratios are not new.

No equivalent Li-susceptibility specialization was identified.

## Adversarial corrections made during audit

1. Broad Li zero-location sensitivity was downgraded after Voros.
2. Broad symmetric zero-displacement response was downgraded after pair-geometry prior art.
3. Generic \(n/\gamma\) Li scaling language was removed after Arias de Reyna and Chebyshev Li literature.
4. Generic bounded-variation transfer language was classified as standard prior art.
5. CL-0173 was proof-audited and its derivative dependency repaired directly from the exact susceptibility derivative.
6. P-TRN-004 was narrowed because small \(Q_\eta\) near \(\Phi_\eta\)-roots is partly definition-driven and tautology-adjacent.

## Current contribution language

Permitted:

"The repository develops a project-specific comparative formalism based on the local zero-coordinate Hessian of the classical Li kernel, its matched susceptibility profile, positive-width multiplicative aggregation, and a deterministic comparison with counting-discrepancy transfer."

Permitted:

"No mathematically equivalent construction was identified in the source set inspected during the second prior-art audit."

Required:

"Originality remains unresolved."

Required:

"The current results do not imply the Riemann Hypothesis."

Prohibited:

- novel response theory;
- new theory of Riemann zeros;
- first-ever Li susceptibility framework;
- new approach to proving RH;
- progress toward solving RH;
- breakthrough.

## RH consequence status

None.

The repository currently contains no new:

- RH-equivalent criterion;
- unconditional Li positivity theorem;
- zero-free region;
- exclusion theorem for off-critical zeros;
- proof of RH.

## Audit limitation

The second audit is source-set bounded.

Failure to identify a PA-4 source is not proof of novelty.

A publication-stage literature review and expert mathematical review remain necessary.
