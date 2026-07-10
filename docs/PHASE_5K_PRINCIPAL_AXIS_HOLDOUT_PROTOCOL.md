# Phase 5K — Window-Level Principal-Axis Holdout Stability

## Objective

Adversarially test the strong Phase 5J component-share PCA concentration under holdout of entire zero-height windows.

Phase 5J observed that approximately

\[
99.7469\%
\]

of in-plane component-share covariance was carried by one principal direction.

Because 20 c-coordinates are sampled from each of only 18 windows, point-level PCA may be affected by within-window pseudoreplication.

Phase 5K trains a one-dimensional simplex principal axis on whole-window subsets and evaluates orthogonal reconstruction on unseen windows.

No RH consequence is claimed.

No novelty claim is made.

---

# Component-share vectors

For each Phase 5J point define

\[
x=(a,e,i),
\]

where

\[
a+e+i=1.
\]

---

# Training affine principal line

For a training population define the centroid

\[
\mu_{\mathrm{train}}
\]

and leading covariance eigenvector

\[
v_{\mathrm{train}},
\qquad
\|v_{\mathrm{train}}\|=1.
\]

The training affine principal line is

\[
\mu_{\mathrm{train}}
+
\operatorname{span}(v_{\mathrm{train}}).
\]

For held-out point x define the orthogonal projection

\[
\Pi_{\mathrm{train}}x
=
\mu_{\mathrm{train}}
+
\langle
x-\mu_{\mathrm{train}},
v_{\mathrm{train}}
\rangle
v_{\mathrm{train}}.
\]

Define squared reconstruction error

\[
r^2(x)
=
\|x-\Pi_{\mathrm{train}}x\|^2.
\]

Define total centered energy

\[
d^2(x)
=
\|x-\mu_{\mathrm{train}}\|^2.
\]

Held-out explained fraction:

\[
F_{\mathrm{holdout}}
=
1-
\frac{
\sum r^2(x)
}{
\sum d^2(x)
}.
\]

---

# Frozen sixfold window split

The 18 dense windows are partitioned deterministically into six held-out groups:

\[
\{1,2,3\},
\{4,5,6\},
\{7,8,9\},
\{10,11,12\},
\{13,14,15\},
\{16,17,18\}.
\]

For each fold:

- 15 training windows;
- 300 training points;
- 3 held-out windows;
- 60 test points.

No random split search is permitted.

---

# Secondary leave-one-window-out audit

A separate descriptive robustness analysis trains on 17 windows and tests on one held-out window for each of the 18 windows.

The six three-window holdout folds drive the primary frozen predictions.

---

# Frozen predictions

## P-HLD-001 — training concentration survives window deletion

For every primary fold let

\[
F_{\mathrm{train}}
=
\frac{\lambda_1}{\lambda_1+\lambda_2}.
\]

PASS rule:

All six training folds satisfy

\[
F_{\mathrm{train}}>0.99.
\]

---

## P-HLD-002 — high held-out explained fraction

PASS rule:

Median primary-fold held-out explained fraction satisfies

\[
\operatorname{median}F_{\mathrm{holdout}}>0.95.
\]

---

## P-HLD-003 — no catastrophic primary fold

PASS rule:

\[
\min F_{\mathrm{holdout}}>0.85.
\]

---

## P-HLD-004 — principal direction stability

Let

\[
v_{\mathrm{full}}
\]

be the full-sample leading in-plane principal direction.

For each primary fold define sign-invariant alignment

\[
A_{\mathrm{fold}}
=
|
\langle
v_{\mathrm{fold}},
v_{\mathrm{full}}
\rangle
|.
\]

PASS rule:

\[
\min A_{\mathrm{fold}}>0.995.
\]

---

## P-HLD-005 — small point-level normalized held-out residual

For held-out points with nonzero centered distance define

\[
\rho(x)
=
\frac{
\|x-\Pi_{\mathrm{train}}x\|
}{
\|x-\mu_{\mathrm{train}}\|
}.
\]

PASS rule:

Median held-out rho across all primary folds is below

\[
0.20.
\]

---

## P-HLD-006 — leave-one-window-out robustness

For each of 18 leave-one-window-out folds compute held-out explained fraction.

PASS rule:

At least 16 of 18 windows satisfy

\[
F_{\mathrm{holdout}}>0.90.
\]

---

## P-HLD-007 — held-out geometry is not vertex dominated

Within each primary held-out fold compute the fraction of points satisfying

\[
\max(a,e,i)>0.8.
\]

PASS rule:

Every primary fold has vertex-dominant fraction below

\[
0.40.
\]

---

# Required outputs

The experiment must report:

- six primary fold definitions;
- training in-plane explained fraction by fold;
- held-out explained fraction by fold;
- minimum, median, and mean held-out explained fraction;
- principal-axis alignment with the full-sample axis by fold;
- minimum axis alignment;
- held-out normalized residual median by fold;
- global held-out normalized residual median;
- held-out vertex-dominant fraction by fold;
- leave-one-window-out explained fraction for all 18 windows;
- leave-one-window-out count above 0.90;
- P-HLD-001 through P-HLD-007 scorecard.

Point-level held-out residuals must be written to CSV.

Primary-fold metrics must be written to CSV.

Leave-one-window-out metrics must be written to CSV.

A JSON summary must be written separately.

---

# Failure-prevention rules

1. Test windows must not contribute to their training centroid or principal direction.

2. Splits are frozen by window number.

3. PCA direction sign is arbitrary; use absolute inner-product alignment.

4. The simplex null direction is structural and excluded from in-plane concentration interpretation.

5. Window-level holdout is not external dataset replication.

6. All windows still arise from the first-500-zero dataset.

7. No asymptotic theorem follows.

8. No off-critical-zero constraint follows.

9. No RH consequence follows.

