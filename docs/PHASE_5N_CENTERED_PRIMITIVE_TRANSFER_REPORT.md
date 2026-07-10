# Phase 5N — Centered-Primitive Cancellation Transfer Report

## Status

COMPLETE.

## Objective

Test whether the strong signed cancellation observed in the Phase 5M interior response is quantitatively captured by deterministic transfer through the centered primitive of the empirical zero-counting discrepancy.

No novelty claim is made.

No RH consequence is claimed.

---

# Exact transfer structure

Let

\[
f(t)=\chi_n^{Li}(t).
\]

Define

\[
\overline E
=
\frac1{B-H}
\int_H^B E_D(s)ds
\]

and

\[
F(t)
=
\int_H^t
(E_D(s)-\overline E)ds.
\]

Then

\[
F(H)=F(B)=0.
\]

The exact identity is

\[
R_{\mathrm{int}}
=
-\overline E
(f(B)-f(H))
+
\int_H^B F(t)f''(t)dt.
\]

Define

\[
C_2
=
|\overline E|
|f(B)-f(H)|
+
\|F\|_\infty
\int_H^B|f''(t)|dt.
\]

Then

\[
|R_{\mathrm{int}}|\le C_2.
\]

The first absolute-integral scale is

\[
C_1
=
\int_H^B|E_D(t)f'(t)|dt.
\]

Define

\[
Q_{21}
=
C_2/C_1.
\]

---

# P-PRM-001 — decomposition bookkeeping closure

Maximum hybrid closure error:

\[
4.75\times10^{-66}.
\]

Result:

PASS.

Qualification:

The primitive response term was reconstructed from the already-proved identity by

\[
R_{\mathrm{prim}}
=
R_{\mathrm{int}}
-
R_{\mathrm{mean}}.
\]

Therefore P-PRM-001 is bookkeeping closure and not independent numerical proof of the integration-by-parts identity.

---

# P-PRM-002 — deterministic certificate validation

Certificate pass count:

\[
780/780.
\]

Result:

PASS.

Interpretation:

All computed finite points satisfied the proved deterministic second-order certificate under the numerical implementation.

The inequality itself was proved before execution.

---

# P-PRM-003 — compression relative to first absolute scale

## First-500 block

Median

\[
Q_{21}
=
C_2/C_1
\]

was approximately

\[
0.08798.
\]

Mean:

\[
0.10142.
\]

## Higher-zero block

Median:

\[
0.03731.
\]

Mean:

\[
0.04184.
\]

Result:

PASS strongly.

Interpretation:

The centered-primitive second-order certificate recovers substantial cancellation discarded by the first absolute-integral scale in both tested finite blocks.

Median retained certificate scale was approximately 8.8 percent and 3.7 percent of \(C_1\).

No universal ordering \(C_2\le C_1\) is claimed.

---

# P-PRM-004 — descriptive response association

## First-500 block

\[
\operatorname{corr}
(
\log|R_{\mathrm{int}}|,
\log C_2
)
\approx
0.87661.
\]

Height-only comparison:

\[
\operatorname{corr}
(
\log|R_{\mathrm{int}}|,
\log H^{-2}
)
\approx
0.38399.
\]

Difference:

\[
0.49262.
\]

## Higher-zero block

Primitive certificate correlation:

\[
0.87006.
\]

Height-only correlation:

\[
0.31352.
\]

Difference:

\[
0.55654.
\]

Result:

PASS strongly.

Qualification:

These are in-sample descriptive correlations.

The certificate contains discrepancy quantities measured from the same finite windows.

No predictive or forecasting interpretation is claimed.

---

# P-PRM-005 — certificate tightness

Median

\[
T_2
=
|R_{\mathrm{int}}|/C_2
\]

was approximately

\[
0.12852
\]

in the first-500 block and

\[
0.25028
\]

in the higher-zero block.

Result:

PASS strongly.

Interpretation:

The second-order certificate is not uniformly quantitatively vacuous in the tested populations.

It remains an upper bound and is not pointwise sharp in general.

---

# P-PRM-006 — mean channel versus primitive channel

Median mean-certificate share was approximately

\[
0.0655
\]

in the first-500 block and

\[
0.1850
\]

in the higher-zero block.

Result:

PASS strongly.

Interpretation:

The mechanism does not reduce to subtracting the window mean discrepancy.

The centered primitive term is materially involved in the second-order certificate.

---

# P-PRM-007 — centered primitive compression

Define

\[
G
=
\frac{
\|F\|_\infty
}{
(B-H)
\|E_D-\overline E\|_\infty
}.
\]

The trivial deterministic inequality gives

\[
0\le G\le1.
\]

Observed median values:

First-500 block:

\[
0.01157.
\]

Higher-zero block:

\[
0.00572.
\]

Result:

PASS extremely strongly.

Interpretation:

The cumulative centered discrepancy excursion is highly compressed relative to the trivial interval-length times raw sup-norm scale in both tested finite populations.

This is a finite computational observation.

It does not establish randomness, statistical independence, or an asymptotic primitive bound.

---

# Frozen scorecard

\[
\begin{array}{ll}
\mathrm{P\mbox{-}PRM\mbox{-}001} & \mathrm{PASS\ —\ BOOKKEEPING},\\
\mathrm{P\mbox{-}PRM\mbox{-}002} & \mathrm{PASS},\\
\mathrm{P\mbox{-}PRM\mbox{-}003} & \mathrm{PASS\ STRONGLY},\\
\mathrm{P\mbox{-}PRM\mbox{-}004} & \mathrm{PASS\ STRONGLY},\\
\mathrm{P\mbox{-}PRM\mbox{-}005} & \mathrm{PASS\ STRONGLY},\\
\mathrm{P\mbox{-}PRM\mbox{-}006} & \mathrm{PASS\ STRONGLY},\\
\mathrm{P\mbox{-}PRM\mbox{-}007} & \mathrm{PASS\ EXTREMELY\ STRONGLY}.
\end{array}
\]

---

# Main finite-data mechanism conclusion

The centered primitive of the zero-counting discrepancy gives a substantially sharper deterministic transfer certificate for the Li susceptibility interior response than the first absolute-integral scale.

Median second-order-to-first-order certificate ratios were approximately

\[
0.088
\]

and

\[
0.037
\]

in the two tested zero-index blocks.

The centered primitive itself was strongly compressed relative to its trivial raw sup-norm scale, with median compression ratios approximately

\[
0.0116
\]

and

\[
0.00572.
\]

The second-order certificate also had substantially greater in-sample descriptive log correlation with the signed interior-response magnitude than height alone.

---

# Mathematical interpretation

The exact transfer identity shows that control of

\[
\overline E
\]

and

\[
\|F\|_\infty
\]

transfers directly into control of the Li susceptibility interior response.

The Phase 5N finite experiment indicates that the centered primitive can capture a large portion of the cancellation discarded by direct absolute-value control of

\[
E_D(t)f'(t).
\]

The remaining theoretical question is not whether integration by parts is valid.

It is whether classical or new estimates for an integrated zero-counting remainder can provide rigorous asymptotic control of the relevant centered primitive.

---

# Next required action

Before deriving an asymptotic primitive estimate, perform a targeted prior-art audit of:

- the Riemann-von Mangoldt remainder;
- \(S(T)\);
- the antiderivative \(S_1(T)=\int_0^T S(t)dt\);
- integrated zero-counting remainders;
- Littlewood-type bounds;
- explicit-formula smoothing by repeated integration;
- Selberg and Titchmarsh treatments of integrated argument functions.

The project must determine whether the centered primitive \(F\) is directly reducible to classical \(S_1\)-type objects plus explicit smooth terms.

---

# Restrictions

1. The transfer identity is elementary.

2. P-PRM-001 is bookkeeping closure.

3. P-PRM-002 mainly validates implementation of a proved inequality.

4. Correlation results are in-sample descriptive.

5. No asymptotic estimate for \(\|F\|_\infty\) is established.

6. No new zero-counting bound is proved.

7. No off-critical-zero constraint is obtained.

8. No RH consequence follows.

