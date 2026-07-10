# Phase 5N — Centered-Primitive Cancellation Transfer Protocol

## Objective

Test whether the strong finite signed cancellation observed in Phase 5M is quantitatively captured by a second-order transfer through the centered primitive of the empirical zero-counting discrepancy.

No novelty claim is made.

No RH consequence is claimed.

---

# Core definitions

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

Define

\[
R_{\mathrm{mean}}
=
-\overline E
(f(B)-f(H))
\]

and

\[
R_{\mathrm{prim}}
=
\int_H^B F(t)f''(t)dt.
\]

The exact identity is

\[
R_{\mathrm{int}}
=
R_{\mathrm{mean}}
+
R_{\mathrm{prim}}.
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
Q_{21}=C_2/C_1.
\]

Define

\[
T_2
=
|R_{\mathrm{int}}|/C_2.
\]

Define

\[
S_{\mathrm{mean}}
=
\frac{
|\overline E||f(B)-f(H)|
}{
C_2
}.
\]

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

---

# Frozen predictions

## P-PRM-001

Exact second-order decomposition closure.

PASS rule:

Maximum hybrid closure error below

\[
10^{-40}.
\]

---

## P-PRM-002

Deterministic second-order certificate validity.

PASS rule:

All 780 points satisfy

\[
|R_{\mathrm{int}}|\le C_2
\]

within \(10^{-40}\) numerical tolerance.

---

## P-PRM-003

Second-order certificate materially improves on the first absolute-integral scale.

PASS rule:

Median

\[
Q_{21}<0.25
\]

in both zero-index blocks.

---

## P-PRM-004

Primitive-transfer scale has stronger in-sample descriptive log correlation with

\[
|R_{\mathrm{int}}|
\]

than height-only scale

\[
H^{-2}
\]

in both blocks.

---

## P-PRM-005

Second-order certificate is not uniformly uselessly loose.

PASS rule:

Median

\[
T_2>0.05
\]

in at least one block.

---

## P-PRM-006

Window-mean discrepancy is not the sole second-order mechanism.

PASS rule:

Median

\[
S_{\mathrm{mean}}<0.90
\]

in both blocks.

---

## P-PRM-007

Centered discrepancy primitive is compressed relative to its trivial raw sup-norm scale.

PASS rule:

Median

\[
G<0.25
\]

in both blocks.

---

# Failure-prevention rules

1. The transfer identity is elementary integration by parts.

2. No novelty claim follows from the identity.

3. P-PRM-001 and P-PRM-002 are primarily proof and implementation validations.

4. Correlation comparisons are in-sample descriptive analyses.

5. Small primitive compression does not prove randomness.

6. No asymptotic bound for the zero-counting discrepancy primitive is established.

7. No off-critical-zero constraint follows.

8. No RH consequence follows.

