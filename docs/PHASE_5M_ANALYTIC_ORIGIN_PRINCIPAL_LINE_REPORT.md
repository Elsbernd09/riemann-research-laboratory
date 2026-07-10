# Phase 5M — Analytic Origin of the Replicated Principal Line

## Status

COMPLETE.

## Scientific role

Phase 5M was a post-replication mechanism audit.

Small interior component shares were already visible before the protocol was frozen.

The phase therefore did not treat small interior share as a blind discovery prediction.

The objective was to determine whether the replicated Phase 5J/5L principal line was primarily explained by:

1. raw height-power suppression of the interior response;
2. signed cancellation inside the weighted discrepancy integral;
3. elementary small-interior simplex geometry.

No RH consequence is claimed.

---

# Response channels

Define

\[
A=|R_{\mathrm{atom}}|,
\qquad
E=|R_{\mathrm{end}}|,
\qquad
I=|R_{\mathrm{int}}|.
\]

The normalized interior share is

\[
i
=
\frac{I}{A+E+I}.
\]

Define

\[
I_{\mathrm{abs}}
=
\int_H^B
|E_D(t)\chi_n'(t)|dt
\]

and

\[
C_{\mathrm{int}}
=
\frac{|R_{\mathrm{int}}|}{I_{\mathrm{abs}}}.
\]

By the triangle inequality,

\[
0\le C_{\mathrm{int}}\le1.
\]

---

# Numerical-method adversary

The original high-precision direct absolute-value quadrature was too slow for the full 780-point mechanism population.

A first vectorized single-panel Gauss-Legendre implementation failed the frozen \(10^{-7}\) self-convergence threshold on the first point.

Observed relative discrepancy:

\[
7.62\times10^{-5}.
\]

No mechanism result was accepted.

A composite-subpanel repair also failed the unchanged \(10^{-7}\) threshold.

Observed first-point relative discrepancy:

\[
7.61\times10^{-7}.
\]

No mechanism result was accepted.

The threshold was not loosened.

The final accepted numerical engine explicitly split every empirical zero-count interval at product sign changes.

On each open empirical interval,

\[
E_D(t)=k-M(t).
\]

At the positive heights used in the experiment,

\[
M'(t)
=
\frac1{2\pi}
\log\frac{t}{2\pi}
>
0,
\]

so \(E_D\) is strictly decreasing and has at most one zero on each interval.

The final engine split at:

1. the discrepancy zero when present;
2. every detected sign-changing zero of \(\chi_n'(t)\).

On each resulting sign-constant segment,

\[
\int|E_D\chi_n'|
=
\left|
\int E_D\chi_n'
\right|.
\]

The engine compared derivative sign-change root scans using 65 and 129 samples per empirical zero interval and required identical sign-change root counts.

It also retained the frozen \(10^{-7}\) coarse/fine integral discrepancy threshold.

The accepted 780-point run completed under these guards.

---

# Independent mp.quad reference audit

A frozen eight-point subset was selected before computing high-precision reference values.

First-500 point indices:

\[
1,120,240,360.
\]

Higher-zero point indices:

\[
1,140,280,420.
\]

The accepted sign-split integral was compared with the original 60-digit piecewise `mp.quad` absolute-integral method.

The external reference threshold was frozen at

\[
10^{-6}
\]

before reference values were computed.

Audit result:

\[
8/8
\]

points passed.

Maximum relative error:

\[
9.8282776547\times10^{-7}.
\]

The maximum error is close to the frozen threshold.

Therefore the reference audit is accepted as a pass but is not described as having a large numerical margin.

The eight-point audit validates selected numerical values.

It does not prove all 780 accepted integrals have relative error below \(10^{-6}\).

---

# Interior-share observations

## First-500 response block

Point count:

\[
360.
\]

Median interior share:

\[
0.00212888.
\]

Mean interior share:

\[
0.00543094.
\]

## Higher-zero response block

Point count:

\[
420.
\]

Median interior share:

\[
0.001368996.
\]

Mean interior share:

\[
0.00277583.
\]

Interpretation:

The interior response channel carries a small normalized magnitude share in both tested finite blocks.

---

# Height-trend audit

## First-500 block

Fitted log-log slopes:

\[
\beta_A
\approx
-1.99977,
\]

\[
\beta_E
\approx
-1.30487,
\]

\[
\beta_I
\approx
-2.12680.
\]

Interior-share versus height slope:

\[
-0.30324.
\]

The corresponding interior-share height-only \(R^2\) was approximately

\[
0.00754.
\]

## Higher-zero block

Fitted log-log slopes:

\[
\beta_A
\approx
-1.99946,
\]

\[
\beta_E
\approx
-0.92123,
\]

\[
\beta_I
\approx
-3.09549.
\]

Interior-share versus height slope:

\[
-1.45636.
\]

The corresponding interior-share height-only \(R^2\) was approximately

\[
0.04974.
\]

Interpretation:

The atom magnitude slopes are consistent with the previously derived matched-scale \(H^{-2}\) susceptibility scale.

The interior magnitude fits are steeper than the atom and endpoint fits in both finite blocks.

However, the height-only explanatory fits are weak.

The project therefore does not infer a simple asymptotic power law for interior share from these regressions.

Pure height-only power suppression is not accepted as a sufficient mechanism explanation.

---

# Interior signed-cancellation result

## First-500 block

Median interior signed-cancellation ratio:

\[
\operatorname{median}C_{\mathrm{int}}
\approx
0.010434.
\]

Fraction satisfying

\[
C_{\mathrm{int}}<0.25:
\]

\[
1.0.
\]

Fraction satisfying

\[
C_{\mathrm{int}}<0.10:
\]

\[
1.0.
\]

## Higher-zero block

Median interior signed-cancellation ratio:

\[
\operatorname{median}C_{\mathrm{int}}
\approx
0.008867.
\]

Fraction satisfying

\[
C_{\mathrm{int}}<0.25:
\]

\[
1.0.
\]

Fraction satisfying

\[
C_{\mathrm{int}}<0.10:
\]

\[
1.0.
\]

Across all 780 tested points,

\[
C_{\mathrm{int}}<0.10.
\]

Interpretation:

The signed interior response retains less than 10 percent of its absolute weighted-integral mass at every tested coordinate.

Median retained magnitude is near 1 percent in both blocks.

This is a strong finite numerical cancellation observation.

It does not prove asymptotic cancellation, statistical independence, randomness, or a zero-counting theorem.

---

# Elementary simplex-edge mechanism

The frozen first-500 principal axis has sign-invariant alignment

\[
0.999984978
\]

with the atom-endpoint exchange direction

\[
\frac1{\sqrt2}(1,-1,0).
\]

On the higher-zero replication population, the frozen first-500 PCA line explains

\[
0.9994484361
\]

of centered energy.

The elementary simplex edge

\[
i=0,
\qquad
a+e=1
\]

explains

\[
0.9994777126.
\]

The shared-denominator explained-fraction difference is

\[
F_{\mathrm{PCA}}-F_{i=0}
\approx
-2.92765\times10^{-5}.
\]

Under the frozen Phase 5M mechanism rule,

\[
|\Delta F|<0.01
\]

means the elementary edge captures nearly all of the frozen PCA energy explanation.

Observed:

\[
|\Delta F|
\approx
2.93\times10^{-5}.
\]

Therefore the elementary \(i=0\) edge captures nearly all of the replicated principal-line geometry under the frozen diagnostic.

The elementary edge slightly outperforms the frozen learned line under the shared denominator convention.

---

# Main mechanism conclusion

The near-one-dimensional component-share geometry observed in Phases 5J through 5L is best interpreted as the geometric consequence of a small interior response share.

When

\[
i\approx0,
\]

simplex closure gives

\[
a+e\approx1.
\]

The natural tangent direction is therefore the atom-endpoint exchange direction

\[
(1,-1,0).
\]

The tested small interior channel is strongly associated with cancellation inside

\[
\int_H^B
E_D(t)\chi_n'(t)dt.
\]

Across all 780 tested finite coordinates, the signed integral retained less than 10 percent of the corresponding absolute-integral mass.

Median retention was near 1 percent.

This cancellation evidence is substantially more uniform than the weak height-only regression evidence.

---

# Research redirection

The principal-line PCA phenomenon is no longer the primary mathematical mystery.

The primary open question is now:

\[
\boxed{
\text{What analytic mechanism forces or explains persistent cancellation in }
\int_H^B E_D(t)\chi_n'(t)dt?
}
\]

The next phase should study the oscillatory interaction between the zero-counting discrepancy

\[
E_D(t)
\]

and the matched-scale derivative profile

\[
t^{-3}J(n/t).
\]

The project should seek a deterministic cancellation identity, oscillatory-integral estimate, or conditional transfer theorem before performing further PCA analysis.

---

# Restrictions

1. Phase 5M was a post-replication mechanism audit.

2. Small interior share was known before the protocol.

3. Height regressions are finite-data descriptive fits.

4. No asymptotic power law for interior share is established.

5. The eight-point mp.quad audit does not prove all 780 integrals accurate below \(10^{-6}\).

6. Small \(C_{\mathrm{int}}\) does not establish randomness or independence.

7. No new zero-counting bound is proved.

8. No off-critical-zero constraint is obtained.

9. No RH consequence follows.

