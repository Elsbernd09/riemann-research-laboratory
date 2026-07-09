# Phase 5J — Component-Share Simplex Geometry

## Objective

Study normalized magnitude geometry of the three signed response channels

\[
R_{\mathrm{atom}},
\qquad
R_{\mathrm{end}},
\qquad
R_{\mathrm{int}}.
\]

Phase 5H found frequent scalar cancellation.

Phase 5I found that coarse sign-chamber identity alone did not strongly discriminate cancellation severity.

Phase 5J therefore retains relative component magnitudes.

No RH consequence is claimed.

No novelty claim is made.

---

# Component shares

Define

\[
S
=
|R_{\mathrm{atom}}|
+
|R_{\mathrm{end}}|
+
|R_{\mathrm{int}}|.
\]

For \(S>0\), define

\[
a
=
\frac{|R_{\mathrm{atom}}|}{S},
\qquad
e
=
\frac{|R_{\mathrm{end}}|}{S},
\qquad
i
=
\frac{|R_{\mathrm{int}}|}{S}.
\]

Then

\[
a+e+i=1.
\]

Every point lies on the 2-simplex.

---

# Balance geometry

For a mixed-sign point define

\[
P_+
=
\sum_{j:s_j=+1}w_j,
\qquad
P_-
=
\sum_{j:s_j=-1}w_j.
\]

Since

\[
P_++P_-=1,
\]

define

\[
d_{\mathrm{bal}}
=
|P_+-1/2|.
\]

For mixed-sign points,

\[
C_{\mathrm{scalar}}
=
2d_{\mathrm{bal}}.
\]

This identity is algebraic and cannot be counted as empirical discovery.

---

# Frozen predictions

## P-SIM-001 — simplex closure

PASS rule:

Maximum

\[
|a+e+i-1|
\]

is below \(10^{-45}\).

---

## P-SIM-002 — nontrivial simplex occupancy

Define

\[
D=\max(a,e,i).
\]

PASS rule:

Fewer than 90 percent of points satisfy

\[
D>0.8.
\]

---

## P-SIM-003 — dominant in-plane principal direction

Center the share vectors and compute the covariance matrix.

One eigenvalue is structurally zero because

\[
a+e+i=1.
\]

Let the two positive in-plane covariance eigenvalues satisfy

\[
\lambda_1\ge\lambda_2.
\]

Define

\[
F_1
=
\frac{\lambda_1}{\lambda_1+\lambda_2}.
\]

PASS rule:

\[
F_1>0.90.
\]

---

## P-SIM-004 — extreme cancellation occupies the balance neighborhood

Define extreme cancellation by

\[
C_{\mathrm{scalar}}<0.25.
\]

PASS rule:

At least 90 percent of extreme-cancellation points satisfy

\[
d_{\mathrm{bal}}<0.125.
\]

This is an algebraic validation consequence of the mixed-sign balance identity and is not independent evidence.

---

## P-SIM-005 — shares add descriptive information beyond chamber identity

Target:

\[
\log C_{\mathrm{scalar}}.
\]

Model A:

sign-chamber one-hot indicators.

Model B:

sign-chamber indicators plus component shares

\[
a,e,i.
\]

PASS rule:

\[
R_B^2-R_A^2>0.20.
\]

In-sample descriptive comparison only.

---

## P-SIM-006 — opposing-share concentration in dominant mixed chambers

For each mixed chamber with at least 50 points, define

\[
w_{\mathrm{opp}}
\]

as the normalized magnitude share of the single component whose sign opposes the other two.

PASS rule:

At least three of the four dominant mixed chambers satisfy

\[
\operatorname{IQR}(w_{\mathrm{opp}})<0.25.
\]

---

## P-SIM-007 — share geometry is smoother than chamber labels suggest

For adjacent frozen c-grid coordinates in each window, define

\[
\Delta_{\mathrm{simp}}
=
\sqrt{
(\Delta a)^2+
(\Delta e)^2+
(\Delta i)^2
}.
\]

Split adjacent steps into chamber-transition and same-chamber steps.

PASS rule:

\[
\operatorname{median}
\Delta_{\mathrm{transition}}
<
2.5
\operatorname{median}
\Delta_{\mathrm{same}}.
\]

---

# Required outputs

The experiment must report:

- point count;
- maximum simplex closure error;
- dominant-share median;
- fraction with dominant share above 0.8;
- covariance eigenvalues;
- in-plane explained fraction F1;
- extreme-cancellation point count;
- extreme-cancellation balance-neighborhood fraction;
- chamber-only R2;
- chamber-plus-shares R2;
- R2 improvement;
- opposing-share IQR by eligible mixed chamber;
- count of eligible chambers with IQR below 0.25;
- transition-step count;
- same-chamber-step count;
- median transition simplex distance;
- median same-chamber simplex distance;
- transition-to-same median ratio;
- P-SIM-001 through P-SIM-007 scorecard.

Point-level simplex coordinates must be written to CSV.

A chamber-level opposing-share summary must be written separately.

A JSON summary must be written separately.

---

# Failure-prevention rules

1. The simplex closure relation is definitional.

2. The zero covariance direction induced by \(a+e+i=1\) is structural.

3. The mixed-sign identity

\[
C_{\mathrm{scalar}}=2d_{\mathrm{bal}}
\]

is algebraic.

4. Exact reconstruction of cancellation from opposing share is not predictive evidence.

5. OLS comparisons are in-sample descriptive analyses.

6. PCA concentration does not prove a dynamical law.

7. No asymptotic theorem follows.

8. No RH consequence follows.

