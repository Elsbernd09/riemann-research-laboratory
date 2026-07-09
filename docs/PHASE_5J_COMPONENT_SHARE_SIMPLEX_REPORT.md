# Phase 5J — Component-Share Simplex Geometry Report

## Status

COMPLETE.

## Population

360 frozen Phase 5H signed-transfer points.

The experiment used the Phase 5I classified dataset.

No zeta zeros were recomputed.

No quadrature was recomputed.

No RH consequence is claimed.

---

# Component-share representation

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

The normalized magnitude shares are

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

Therefore

\[
a+e+i=1.
\]

---

# Simplex closure

Maximum closure error:

\[
1.56\times10^{-61}.
\]

P-SIM-001:

PASS.

Interpretation:

Implementation validation only.

---

# Dominant-share occupancy

Median dominant share:

\[
0.61132.
\]

Fraction satisfying

\[
\max(a,e,i)>0.8:
\]

\[
0.15.
\]

P-SIM-002:

PASS.

Interpretation:

The tested simplex population is not concentrated almost entirely at component-dominant vertices.

The median point retains material magnitude in multiple response channels.

---

# In-plane covariance concentration

Observed covariance eigenvalues were approximately

\[
0.0404516,
\]

\[
0.000102624,
\]

and a numerical zero of order

\[
10^{-63}.
\]

The null direction is structurally induced by

\[
a+e+i=1.
\]

Among the two positive in-plane covariance eigenvalues, the leading explained fraction was

\[
\boxed{
0.997469.
}
\]

P-SIM-003:

PASS strongly.

Interpretation:

In the tested finite population, the normalized component-share cloud exhibits extremely strong concentration along one dominant affine direction inside the two-dimensional simplex plane.

This is a finite-data PCA observation.

It does not establish an exact one-dimensional law.

It does not establish asymptotic persistence.

---

# Balance-neighborhood validation

Extreme-cancellation point count:

\[
185.
\]

Fraction in the frozen balance neighborhood:

\[
1.0.
\]

P-SIM-004:

PASS.

Qualification:

For mixed-sign points,

\[
C_{\mathrm{scalar}}
=
2d_{\mathrm{bal}}.
\]

Therefore the frozen extreme-cancellation and balance-neighborhood thresholds are algebraically equivalent.

This result is identity validation and not independent empirical evidence.

---

# Chamber versus magnitude-share descriptive models

Chamber-only in-sample model:

\[
R_A^2
\approx
0.128757.
\]

Chamber-plus-shares model:

\[
R_B^2
\approx
0.474840.
\]

Improvement:

\[
\boxed{
\Delta R^2
\approx
0.346083.
}
\]

P-SIM-005:

PASS strongly.

Interpretation:

Relative component magnitudes add substantial in-sample descriptive information about log scalar cancellation beyond coarse sign-chamber identity.

No out-of-sample generalization is established.

---

# Opposing-share concentration

The four dominant mixed chambers had opposing-share IQRs approximately

\[
0.1315,
\quad
0.1371,
\quad
0.1575,
\quad
0.2006.
\]

All four were below

\[
0.25.
\]

P-SIM-006:

PASS strongly.

Interpretation:

Within each dominant mixed-sign chamber, the magnitude share carried by the single opposing component occupies a substantially narrower central range than the full unit interval.

This concentration is consistent with constrained component-share geometry.

No exact functional law is established.

---

# Adjacent-grid share geometry

Chamber-transition step count:

\[
222.
\]

Same-chamber step count:

\[
120.
\]

Median transition-step simplex distance:

\[
0.124728.
\]

Median same-chamber simplex distance:

\[
0.058909.
\]

Ratio:

\[
2.1173.
\]

P-SIM-007:

PASS.

Interpretation:

The normalized magnitude geometry moves more on chamber-transition steps, but the median displacement remains below 2.5 times the same-chamber median.

The frequent chamber switching observed in Phase 5I is therefore compatible with a more structured underlying simplex geometry whose coarse sign label changes when component signs cross chamber boundaries.

No smooth dynamical law is yet proved.

---

# Frozen scorecard

\[
\begin{array}{ll}
\mathrm{P\mbox{-}SIM\mbox{-}001} & \mathrm{PASS},\\
\mathrm{P\mbox{-}SIM\mbox{-}002} & \mathrm{PASS},\\
\mathrm{P\mbox{-}SIM\mbox{-}003} & \mathrm{PASS\ STRONGLY},\\
\mathrm{P\mbox{-}SIM\mbox{-}004} & \mathrm{PASS\ —\ ALGEBRAIC\ VALIDATION},\\
\mathrm{P\mbox{-}SIM\mbox{-}005} & \mathrm{PASS\ STRONGLY},\\
\mathrm{P\mbox{-}SIM\mbox{-}006} & \mathrm{PASS\ STRONGLY},\\
\mathrm{P\mbox{-}SIM\mbox{-}007} & \mathrm{PASS}.
\end{array}
\]

---

# Main finite-data conclusion

The Phase 5H response components exhibit a strongly concentrated normalized magnitude geometry.

After the structurally null simplex direction is removed, approximately

\[
99.7469\%
\]

of observed in-plane covariance is carried by one principal direction.

Component shares also add substantial descriptive information beyond chamber identity.

The current finite-data evidence therefore motivates direct study of the dominant simplex principal coordinate and its stability across windows.

---

# Adversarial open questions

1. Is the PCA concentration driven by a simple shared scaling law in the three response components?

2. Does the dominant principal axis remain stable under window-level holdout?

3. Is the concentration robust across eta and H subsets?

4. Does a principal axis learned on one group of windows explain held-out component-share geometry?

5. Are the 360 point-level observations strongly pseudoreplicated within windows?

6. Does the near-one-dimensional geometry persist beyond the first 500 computed critical-line zeros?

---

# Restrictions

The null covariance direction induced by simplex closure is structural.

PCA concentration is finite-data and descriptive.

OLS results are in-sample.

The balance identity is algebraic.

No exact one-dimensional law is proved.

No out-of-sample predictive result is established.

No asymptotic theorem is established.

No off-critical-zero constraint is obtained.

No RH consequence follows.

