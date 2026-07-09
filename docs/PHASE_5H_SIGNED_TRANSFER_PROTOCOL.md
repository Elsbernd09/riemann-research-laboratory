# Phase 5H — Cancellation-Aware Signed Transfer Protocol

## Objective

Study why the actual signed counting-response residual can be much smaller than the deterministic absolute-value transfer envelope.

The Phase 5F inequality

\[
|\mathcal T[E]|
\le
\Lambda_n(H,\eta)\|E\|_\infty
\]

is a worst-case certificate.

It discards all sign cancellation.

Phase 5H decomposes the empirical counting response into signed components and studies alignment between the empirical zero-counting discrepancy and the Li susceptibility derivative.

No RH consequence is claimed.

No novelty claim is made.

---

# Exact decomposition

Let

\[
f(t)=\chi_n^{Li}(t),
\qquad
B=(1+\eta)H.
\]

The non-atomic counting transform is

\[
\mathcal T[E_D]
=
f(B)E_D(B)
-
f(H)E_D(H)
-
\int_H^B E_D(t)f'(t)dt.
\]

Define

\[
R_{\mathrm{end}}
=
f(B)E_D(B)-f(H)E_D(H),
\]

and

\[
R_{\mathrm{int}}
=
-\int_H^B E_D(t)f'(t)dt.
\]

The lower endpoint atom is

\[
R_{\mathrm{atom}}
=
f(H)\Delta N_D(H).
\]

Therefore

\[
R_{\mathrm{count}}
=
R_{\mathrm{atom}}
+
R_{\mathrm{end}}
+
R_{\mathrm{int}}.
\]

---

# Interior alignment coefficient

When

\[
\|E_D\|_2\|\chi_n'\|_2>0,
\]

define

\[
\kappa_{n,H,\eta}
=
\frac{
\int_H^B E_D(t)\chi_n'(t)dt
}{
\|E_D\|_2\|\chi_n'\|_2
}.
\]

By Cauchy-Schwarz,

\[
-1\le\kappa_{n,H,\eta}\le1.
\]

Since

\[
R_{\mathrm{int}}
=
-\int_H^B E_D(t)\chi_n'(t)dt,
\]

we have the exact identity

\[
R_{\mathrm{int}}
=
-\kappa_{n,H,\eta}
\|E_D\|_2
\|\chi_n'\|_2.
\]

This identity is definitional and must not be scored as empirical evidence.

---

# Scalar cancellation coefficient

Define

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
}
\]

when the denominator is nonzero.

Then

\[
0\le C_{\mathrm{scalar}}\le1.
\]

Small values indicate cancellation among the atom, endpoint, and interior signed components.

---

# Deterministic certificate tightness

Let

\[
B_{\sup}
=
|R_{\mathrm{atom}}|
+
\Lambda_n(H,\eta)\|E_D\|_\infty.
\]

Define

\[
T_{\sup}
=
\frac{|R_{\mathrm{count}}|}{B_{\sup}}
\]

when the denominator is positive.

---

# Frozen predictions

## P-SGN-001 — exact signed closure

Prediction:

\[
R_{\mathrm{count}}
=
R_{\mathrm{atom}}
+
R_{\mathrm{end}}
+
R_{\mathrm{int}}.
\]

PASS rule:

Maximum absolute closure error below \(10^{-45}\).

---

## P-SGN-002 — nontrivial interior alignment

Prediction:

The empirical absolute alignment coefficient is not concentrated numerically at zero.

PASS rule:

\[
\operatorname{median}|\kappa|>0.05.
\]

The threshold is exploratory and project-defined.

---

## P-SGN-003 — alignment magnitude improves descriptive association

Define

\[
P_{\mathrm{abs}}
=
\|E_D\|_2\|\chi_n'\|_2
\]

and

\[
P_\kappa
=
|\kappa|
\|E_D\|_2
\|\chi_n'\|_2
+
|R_{\mathrm{atom}}|
+
|R_{\mathrm{end}}|.
\]

Let

\[
Y=|R_{\mathrm{count}}|.
\]

PASS rule:

\[
\operatorname{corr}(\log Y,\log P_\kappa)
>
\operatorname{corr}(\log Y,\log P_{\mathrm{abs}}).
\]

This is an in-sample descriptive comparison.

It is not predictive generalization.

---

## P-SGN-004 — scalar cancellation is materially common

PASS rule:

At least 25 percent of dense-window coordinates satisfy

\[
C_{\mathrm{scalar}}<0.5.
\]

---

## P-SGN-005 — scalar cancellation is more associated with certificate tightness than height alone

PASS rule:

\[
|
\operatorname{corr}
(
\log T_{\sup},
\log C_{\mathrm{scalar}}
)
|
>
|
\operatorname{corr}
(
\log T_{\sup},
\log(1/H)
)
|.
\]

This is descriptive association only.

No causal interpretation is permitted.

---

# Failure-prevention rules

1. The identity

\[
R_{\mathrm{int}}
=
-\kappa\|E_D\|_2\|\chi_n'\|_2
\]

is definitional.

A perfect fit to the interior residual is not evidence.

2. The full signed reconstruction

\[
|R_{\mathrm{atom}}+R_{\mathrm{end}}+R_{\mathrm{int}}|
\]

is the target itself after exact closure and cannot be called a predictor.

3. Quantities using the same empirical \(E_D\) window are in-sample descriptive statistics.

They are not out-of-sample forecasts.

4. Correlation does not establish causation.

5. Phase 5H has no implication for RH.

---

# Experimental population

Use the authoritative-anchor repaired Phase 5E dataset and the same dense-window population used in Phase 5G:

- occupancy at least 25;
- all validated \(c\)-coordinates from the decomposition experiment;
- authoritative zero-index reconstruction of H;
- piecewise-exact empirical counting remainder.

Expected population from the frozen dataset:

- 18 dense windows;
- 20 coordinates per window;
- 360 decomposition points.

---

# Required outputs

The experiment must report:

- number of points;
- maximum signed closure error;
- minimum and maximum kappa;
- median absolute kappa;
- mean absolute kappa;
- fraction with absolute kappa below 0.05;
- fraction with absolute kappa above 0.25;
- correlation log count residual versus log P_abs;
- correlation log count residual versus log P_kappa;
- correlation improvement;
- median scalar cancellation coefficient;
- fraction C_scalar below 0.5;
- fraction C_scalar below 0.25;
- median sup-certificate tightness;
- correlation log T_sup versus log C_scalar;
- correlation log T_sup versus log 1/H;
- absolute-correlation comparison;
- frozen prediction scorecard.

All raw point-level results must be written to CSV.

A JSON summary must be written separately.

