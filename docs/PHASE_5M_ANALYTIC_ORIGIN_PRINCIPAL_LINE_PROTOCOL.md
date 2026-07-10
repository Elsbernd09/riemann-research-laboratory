# Phase 5M — Analytic Origin of the Replicated Principal Line

## Status

MECHANISM-AUDIT PROTOCOL FROZEN.

## Trigger

Phase 5L externally replicated the first-500 component-share principal line on disjoint zero-index windows.

The frozen first-500 axis is approximately an atom-versus-endpoint exchange direction with a small interior coordinate.

Higher-zero share outputs also visibly contain many small interior shares.

Therefore Phase 5M is not a blind discovery test of small interior share.

It is a mechanism audit.

No novelty claim is made.

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

---

# Interior absolute-integral scale

Define

\[
I_{\mathrm{abs}}
=
\int_H^B
|E_D(t)\chi_n'(t)|dt.
\]

Since

\[
R_{\mathrm{int}}
=
-\int_H^B
E_D(t)\chi_n'(t)dt,
\]

define the interior signed-cancellation ratio

\[
C_{\mathrm{int}}
=
\frac{
|R_{\mathrm{int}}|
}{
I_{\mathrm{abs}}
}
\]

whenever \(I_{\mathrm{abs}}>0\).

By the triangle inequality,

\[
0\le C_{\mathrm{int}}\le1.
\]

Small values indicate cancellation within the signed weighted interior integral.

---

# M-001 — interior-share height trend

For the first-500 response population and higher-zero replication population separately, fit

\[
\log i
=
\alpha+\beta\log H
\]

over positive interior-share observations.

Report the fitted slope beta.

No binary PASS/FAIL score is assigned.

This analysis was motivated after small interior shares were already visible.

---

# M-002 — raw component height scaling

For each data block separately, fit

\[
\log A
=
\alpha_A+\beta_A\log H,
\]

\[
\log E
=
\alpha_E+\beta_E\log H,
\]

and

\[
\log I
=
\alpha_I+\beta_I\log H.
\]

No binary score is assigned.

Interpretive question:

Does the raw interior component exhibit materially steeper negative height scaling than the atom and endpoint channels?

---

# M-003 — internal signed-cancellation diagnostic

Compute

\[
C_{\mathrm{int}}
=
|R_{\mathrm{int}}|/I_{\mathrm{abs}}.
\]

Frozen descriptive categories:

Strong internal cancellation:

\[
C_{\mathrm{int}}<0.25.
\]

Very strong internal cancellation:

\[
C_{\mathrm{int}}<0.10.
\]

Report the median and both category frequencies in each zero-index block.

No asymptotic conclusion follows.

---

# M-004 — frozen PCA line versus elementary i=0 simplex edge

Define the elementary affine edge

\[
L_0
=
\{
(a,e,i):
a+e=1,\ i=0
\}.
\]

On the higher-zero external population compute explained fraction relative to the same frozen first-500 centroid convention for the PCA line and the fixed geometric edge \(L_0\).

Define

\[
\Delta F
=
F_{\mathrm{PCA}}-F_{i=0}.
\]

Frozen interpretation:

If

\[
|\Delta F|<0.01,
\]

the elementary \(i=0\) edge captures nearly all of the frozen PCA line's centered-energy explanation.

If

\[
\Delta F\ge0.01,
\]

the learned principal line contains materially more finite-data geometry than merely small interior share.

This is a mechanism diagnostic.

---

# M-005 — atom-endpoint exchange axis

Define

\[
v_0
=
\frac1{\sqrt2}(1,-1,0).
\]

Compute the sign-invariant alignment

\[
A_0
=
|
\langle
v_{500},v_0
\rangle
|.
\]

This formalizes a geometry already visible in the frozen axis.

It is not a blind prediction.

---

# Analytical scaling caution

The matched-scale susceptibility asymptotics give

\[
\chi_n(H)
=
H^{-2}\Psi(c)+O(H^{-4})
\]

and

\[
\chi_n'(Hu)
=
-H^{-3}u^{-3}J(c/u)+O(H^{-5}).
\]

Therefore

\[
R_{\mathrm{atom}}
=
H^{-2}\Psi(c)+O(H^{-4}).
\]

For the interior channel,

\[
R_{\mathrm{int}}
=
-\int_H^{(1+\eta)H}
E_D(t)\chi_n'(t)dt.
\]

After \(t=Hu\),

\[
R_{\mathrm{int}}
=
H^{-2}
\int_1^{1+\eta}
E_D(Hu)u^{-3}J(c/u)du
+
\text{kernel-remainder contribution}.
\]

Thus the \(H^{-3}\) derivative scale does not by itself make the integrated interior channel lower order, because the window length is \(O(H)\).

Pure power-order suppression of \(R_{\mathrm{int}}\) is therefore not assumed.

Signed cancellation within the weighted discrepancy integral is a competing mechanism.

---

# Failure-prevention rules

1. Small interior share was visible before Phase 5M and is not a blind prediction.

2. Height regressions are descriptive fits on finite data.

3. The 360 first-500 points are clustered within 18 windows.

4. The higher-zero points are also clustered within frozen windows.

5. A negative fitted height slope does not prove an asymptotic power law.

6. Small C_int does not prove probabilistic independence or randomness.

7. The i=0 edge comparison is a geometric mechanism diagnostic.

8. No off-critical-zero constraint follows.

9. No RH consequence follows.

