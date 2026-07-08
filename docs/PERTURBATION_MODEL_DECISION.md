# Perturbation Model Decision

## Phase 0C

This document records the adversarial comparison of four synthetic zero-surgery models and freezes the primary perturbation formalism.

---

# 1. Model A: Pair-to-Quartet Bifurcation

Define

\[
P_\gamma
=
\left\{
\frac12+i\gamma,
\frac12-i\gamma
\right\}
\]

and

\[
Q_{\delta,\gamma}
=
\left\{
\frac12+\epsilon\delta+i\eta\gamma:
\epsilon,\eta\in\{-1,+1\}
\right\}.
\]

Model A performs

\[
P_\gamma\to Q_{\delta,\gamma}.
\]

For a zero-sum diagnostic

\[
\mathcal D_f(\mathcal Z)
=
\sum_{\rho\in\mathcal Z}f(\rho),
\]

the response is

\[
\Delta_A
=
\sum_{\rho\in Q_{\delta,\gamma}}f(\rho)
-
\sum_{\rho\in P_\gamma}f(\rho).
\]

As

\[
\delta\to0,
\]

the quartet converges as a multiset to

\[
2P_\gamma.
\]

Therefore, in general,

\[
\lim_{\delta\to0}\Delta_A
=
\sum_{\rho\in P_\gamma}f(\rho),
\]

not zero.

## Decision

REJECTED AS PRIMARY PERTURBATION MODEL.

Reason: the response contains a zeroth-order multiplicity jump.

Model A may later be studied as a bifurcation model.

---

# 2. Model B: Double-Pair Splitting

Model B performs

\[
2P_\gamma\to Q_{\delta,\gamma}.
\]

Define

\[
\Delta_B
=
\sum_{\rho\in Q_{\delta,\gamma}}f(\rho)
-
2\sum_{\rho\in P_\gamma}f(\rho).
\]

Let

\[
\rho_\eta
=
\frac12+i\eta\gamma,
\qquad
\eta\in\{-1,+1\}.
\]

Then

\[
\Delta_B
=
\sum_{\eta=\pm1}
\left[
f(\rho_\eta+\delta)
+
f(\rho_\eta-\delta)
-
2f(\rho_\eta)
\right].
\]

For \(f\) analytic near both centers,

\[
f(\rho+\delta)+f(\rho-\delta)-2f(\rho)
=
\delta^2f''(\rho)
+
\frac{\delta^4}{12}f^{(4)}(\rho)
+
O(\delta^6).
\]

Hence

\[
\Delta_B
=
\delta^2
\sum_{\eta=\pm1}
f''(\rho_\eta)
+
O(\delta^4).
\]

If

\[
f(\bar z)=\overline{f(z)},
\]

then

\[
\Delta_B
=
2\delta^2
\Re
f''\left(\frac12+i\gamma\right)
+
O(\delta^4).
\]

## Decision

RETAINED AS LOCAL SYMMETRY MODEL.

Reason: the response vanishes continuously as delta tends to zero and admits an even-power local expansion.

Warning: the baseline is a multiplicity-two critical-line pair and is not asserted to model a simple zeta zero literally.

---

# 3. Model C: Two-Pair Transport

Model C compares

\[
P_{\gamma-h}\cup P_{\gamma+h}
\]

with

\[
Q_{\delta,\gamma}.
\]

For an analytic kernel \(f\), horizontal symmetric perturbation gives

\[
f(\rho+\delta)+f(\rho-\delta)
=
2f(\rho)+\delta^2f''(\rho)+O(\delta^4),
\]

whereas vertical symmetric perturbation gives

\[
f(\rho+ih)+f(\rho-ih)
=
2f(\rho)-h^2f''(\rho)+O(h^4).
\]

Therefore the difference contains the combined second-order scale

\[
\delta^2+h^2.
\]

## Decision

REJECTED AS PRIMARY SENSITIVITY MODEL.

Reason: horizontal off-line displacement is confounded with vertical zero-spacing compression.

Potential future use: confounding-control experiments comparing horizontal and vertical perturbations.

---

# 4. Model D: Signed Symmetry-Breaking Response

Let \(\mathfrak d_z\) denote the Dirac point mass at \(z\).

Define the signed zero response measure

\[
\nu_{\delta,\gamma}
=
\sum_{\rho\in Q_{\delta,\gamma}}
\mathfrak d_\rho
-
2\mathfrak d_{\frac12+i\gamma}
-
2\mathfrak d_{\frac12-i\gamma}.
\]

For a test kernel \(f\), define

\[
\mathcal R_f(\delta,\gamma)
=
\int f(z)\,d\nu_{\delta,\gamma}(z).
\]

Equivalently,

\[
\mathcal R_f(\delta,\gamma)
=
\sum_{\rho\in Q_{\delta,\gamma}}f(\rho)
-
2f\left(\frac12+i\gamma\right)
-
2f\left(\frac12-i\gamma\right).
\]

Define the quadratic susceptibility, when the limit exists, by

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

For \(f\) analytic near both baseline points,

\[
\chi_f(\gamma)
=
f''\left(\frac12+i\gamma\right)
+
f''\left(\frac12-i\gamma\right).
\]

If

\[
f(\bar z)=\overline{f(z)},
\]

then

\[
\chi_f(\gamma)
=
2\Re
f''\left(\frac12+i\gamma\right).
\]

## Decision

SELECTED AS PRIMARY RESEARCH FORMALISM.

Model B supplies the geometric interpretation.

Model D supplies the response-functional language.

---

# 5. Primary Research Object

The primary object of the laboratory is

\[
\boxed{
\chi_f(\gamma)
=
\lim_{\delta\to0}
\frac{
\mathcal R_f(\delta,\gamma)
}{
\delta^2
}
}
\]

for explicitly defined diagnostic kernels \(f\).

For indexed diagnostics \(f_n\), write

\[
\chi_n(\gamma)
=
\chi_{f_n}(\gamma).
\]

The laboratory will investigate:

- magnitude of \(\chi_n(\gamma)\);
- sign of \(\chi_n(\gamma)\);
- sign changes;
- growth in diagnostic index \(n\);
- dependence on zero height \(\gamma\);
- finite-delta corrections;
- comparison among rigorously classified diagnostics.

---

# 6. Candidate Detection Scale

For threshold \(\tau>0\), define provisionally

\[
n_*(\delta,\gamma;\tau)
=
\inf
\left\{
n:
|\mathcal R_{f_n}(\delta,\gamma)|
\ge\tau
\right\}.
\]

This definition is provisional.

A threshold based on absolute magnitude may be normalization-dependent.

Possible alternatives include:

- relative response;
- signal-to-baseline ratio;
- response normalized by local diagnostic scale;
- condition-number-aware response.

No detection scale is frozen yet.

---

# 7. Candidate Lemma

## Symmetric Orbit-Splitting Response Lemma

Let \(f\) be analytic in neighborhoods of

\[
\frac12+i\gamma
\]

and

\[
\frac12-i\gamma.
\]

Define

\[
\mathcal R_f(\delta,\gamma)
=
\sum_{\epsilon=\pm1}
\sum_{\eta=\pm1}
f\left(
\frac12+\epsilon\delta+i\eta\gamma
\right)
-
2
\sum_{\eta=\pm1}
f\left(
\frac12+i\eta\gamma
\right).
\]

Then

\[
\mathcal R_f(\delta,\gamma)
=
\delta^2
\sum_{\eta=\pm1}
f''\left(
\frac12+i\eta\gamma
\right)
+
O(\delta^4).
\]

If

\[
f(\bar z)=\overline{f(z)},
\]

then

\[
\mathcal R_f(\delta,\gamma)
=
2\delta^2
\Re
f''\left(
\frac12+i\gamma
\right)
+
O(\delta^4).
\]

## Current status

CANDIDATE PROJECT LEMMA.

The underlying Taylor-expansion mechanism is elementary and not asserted to be original.

The lemma must be written with a precise remainder statement before being marked PROVED IN PROJECT.

Its relevance to RH diagnostics has not been established.

---

# 8. Research Decision

The laboratory will initially study signed quadratic susceptibility under symmetry-preserving double-orbit splitting.

It will not claim to deform the Riemann zeta function itself.

It will not infer prime-side data from the synthetic signed response.

The first diagnostic family to be analyzed will be chosen only after its kernel representation and normalization dependence are derived explicitly.
