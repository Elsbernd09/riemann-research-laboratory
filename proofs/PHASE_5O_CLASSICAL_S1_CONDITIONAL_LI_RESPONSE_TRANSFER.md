# Phase 5O — Classical S1 Bridge and Conditional Li-Response Transfer

## Status

CONDITIONAL THEOREM UNDER THE RIEMANN HYPOTHESIS — ALGEBRA REPAIRED AFTER FAILED VALIDATOR.

## Prior-art boundary

The primitive

\[
S_1(T)
=
\int_0^T S(t)\,dt
+
\text{constant}
\]

and bounds for it are classical.

The use of an antiderivative to transfer cancellation through integration by parts is also a standard analytic mechanism.

No originality claim is made for the primitive or for integration by parts.

The project-specific object is the specialization to the Li zero-coordinate susceptibility response architecture.

Originality of the combined specialization remains under prior-art review.

---

# 1. Classical zero-counting bridge

Let

\[
N(t)
\]

denote the classical zero-counting function for nontrivial zeros of the Riemann zeta function.

Write

\[
M(t)
=
\frac{t}{2\pi}
\log\frac{t}{2\pi}
-
\frac{t}{2\pi}
+
\frac78.
\]

The classical Riemann-von Mangoldt formula gives

\[
N(t)
=
M(t)
+
S(t)
+
r(t),
\]

where

\[
r(t)=O(1/t)
\]

in the standard asymptotic convention.

Define

\[
E(t)
=
N(t)-M(t).
\]

Then

\[
E(t)=S(t)+r(t).
\]

Let

\[
S_1(t)
=
C
+
\int_0^tS(u)\,du.
\]

Define an antiderivative of the remainder on a positive-height range by

\[
R_1(t)
=
\int_{t_0}^t r(u)\,du.
\]

Then, on any interval avoiding the irrelevant lower-origin convention,

\[
A(t)
:=
\int_{t_0}^t E(u)\,du
=
S_1(t)
+
R_1(t)
+
C_0
\]

for a constant \(C_0\).

---

# 2. Exact secant-detrended primitive identity

Fix

\[
B>H>t_0.
\]

Define

\[
\overline E
=
\frac1{B-H}
\int_H^B E(s)\,ds
\]

and

\[
F(t)
=
\int_H^t
(E(s)-\overline E)\,ds.
\]

Then

\[
F(H)=F(B)=0.
\]

Since

\[
\int_H^tE(s)\,ds
=
A(t)-A(H)
\]

and

\[
(B-H)\overline E
=
A(B)-A(H),
\]

we obtain the exact identity

\[
\boxed{
F(t)
=
A(t)-A(H)
-
\frac{t-H}{B-H}
\left(
A(B)-A(H)
\right).
}
\]

Substituting

\[
A=S_1+R_1+C_0
\]

gives

\[
\boxed{
\begin{aligned}
F(t)
={}&
S_1(t)-S_1(H)
-
\frac{t-H}{B-H}
\left(
S_1(B)-S_1(H)
\right)
\\
&+
R_1(t)-R_1(H)
-
\frac{t-H}{B-H}
\left(
R_1(B)-R_1(H)
\right).
\end{aligned}
}
\]

The additive convention constant in \(S_1\) cancels identically.

Thus the project centered primitive is a secant-detrended increment of the classical \(S_1\)-type primitive plus the corresponding detrended integrated Riemann-von Mangoldt remainder.

---

# 3. Conditional bound for the centered primitive

Assume the Riemann Hypothesis.

Use the classical conditional estimate

\[
S_1(t)
=
O\left(
\frac{\log t}
{(\log\log t)^2}
\right).
\]

Fix

\[
\eta>0
\]

and set

\[
B=(1+\eta)H.
\]

For

\[
t\in[H,B],
\]

we have

\[
\log t\asymp_\eta\log H
\]

and

\[
\log\log t\asymp_\eta\log\log H.
\]

Therefore

\[
\sup_{H\le t\le B}
|S_1(t)|
=
O_\eta\left(
\frac{\log H}
{(\log\log H)^2}
\right).
\]

The secant-detrended \(S_1\) increment satisfies

\[
\begin{aligned}
&
\left|
S_1(t)-S_1(H)
-
\frac{t-H}{B-H}
\left(
S_1(B)-S_1(H)
\right)
\right|
\\
&\le
|S_1(t)|
+
|S_1(H)|
+
|S_1(B)|
+
|S_1(H)|.
\end{aligned}
\]

Hence

\[
\boxed{
\|F_S\|_\infty
=
O_\eta\left(
\frac{\log H}
{(\log\log H)^2}
\right).
}
\]

Because

\[
r(t)=O(1/t),
\]

on the fixed relative window

\[
[H,(1+\eta)H]
\]

we have

\[
\int_H^B|r(t)|dt
=
O_\eta(1).
\]

The secant-detrended integrated remainder therefore satisfies

\[
\|F_r\|_\infty
=
O_\eta(1).
\]

Consequently,

\[
\boxed{
\|F\|_{\infty,[H,B]}
=
O_\eta\left(
\frac{\log H}
{(\log\log H)^2}
\right)
}
\]

under RH.

---

# 4. Conditional bound for the window-mean discrepancy

By definition,

\[
\overline E
=
\frac1{B-H}
\int_H^B E(s)\,ds.
\]

Using

\[
E=S+r,
\]

we obtain

\[
\int_H^B E(s)\,ds
=
S_1(B)-S_1(H)
+
O_\eta(1).
\]

Under RH,

\[
S_1(B)-S_1(H)
=
O_\eta\left(
\frac{\log H}
{(\log\log H)^2}
\right).
\]

Since

\[
B-H=\eta H,
\]

we obtain

\[
\boxed{
\overline E
=
O_\eta\left(
\frac{\log H}
{H(\log\log H)^2}
\right)
}
\]

under RH.

---

# 5. Direct second-derivative matched-scale profile

Recall

\[
\chi_n'(t)
=
-t^{-3}
J_{Li}(n/t)
+
O_{K}(t^{-5})
\]

uniformly whenever

\[
q=n/t
\]

lies in a fixed compact positive set \(K\).

The second derivative must not be obtained merely by differentiating the displayed big-O statement.

Instead use the exact scaled derivative representation from Phase 5F-A:

\[
t^3\chi_n'(t)
=
G(q,x),
\qquad
q=\frac nt,
\qquad
x=\frac1t,
\]

where

\[
G(q,x)
\]

is analytic in \(q\) and \(x^2\) near compact positive \(q\)-sets and

\[
G(q,0)=-J_{Li}(q).
\]

Write

\[
G(q,x)
=
-J_{Li}(q)
+
x^2G_2(q,x)
\]

with

\[
G_2
\]

analytic and uniformly bounded together with its first derivatives on compact neighborhoods.

Then

\[
\chi_n'(t)
=
t^{-3}
G(n/t,1/t).
\]

Differentiate the exact right-hand side:

\[
\chi_n''(t)
=
-3t^{-4}G(q,x)
+
t^{-3}
\left(
G_q(q,x)\frac{dq}{dt}
+
G_x(q,x)\frac{dx}{dt}
\right).
\]

Since

\[
\frac{dq}{dt}
=
-\frac qt
\]

and

\[
\frac{dx}{dt}
=
-\frac1{t^2},
\]

we get

\[
t^4\chi_n''(t)
=
-3G(q,x)
-
qG_q(q,x)
-
xG_x(q,x).
\]

At

\[
x=0,
\]

using

\[
G(q,0)=-J_{Li}(q)
\]

and

\[
G_q(q,0)=-J_{Li}'(q),
\]

while evenness in \(x\) gives

\[
xG_x(q,x)=O_K(x^2),
\]

we obtain

\[
t^4\chi_n''(t)
=
3J_{Li}(q)
+
qJ_{Li}'(q)
+
O_K(t^{-2}).
\]

Therefore

\[
\boxed{
t^4\chi_n''(t)
=
K_{Li}^{(2)}(q)
+
O_K(t^{-2}),
\qquad
q=\frac nt,
}
\]

where

\[
\boxed{
K_{Li}^{(2)}(q)
=
3J_{Li}(q)
+
qJ_{Li}'(q).
}
\]

Recall

\[
J_{Li}(q)
=
2q^3\sin q
-
12q^2\cos q
-
12q\sin q.
\]

Direct differentiation gives

\[
J_{Li}'(q)
=
2q^3\cos q
+
18q^2\sin q
-
36q\cos q
-
12\sin q.
\]

Hence

\[
\boxed{
K_{Li}^{(2)}(q)
=
2q^4\cos q
+
24q^3\sin q
-
72q^2\cos q
-
48q\sin q.
}
\]

The \(q^3\sin q\) terms do not cancel.

Indeed,

\[
3J_{Li}(q)
\]

contributes

\[
6q^3\sin q,
\]

while

\[
qJ_{Li}'(q)
\]

contributes

\[
18q^3\sin q.
\]

The total contribution is therefore

\[
24q^3\sin q.
\]

Thus, uniformly for \(q\) in compact positive sets,

\[
\boxed{
\chi_n''(t)
=
t^{-4}
K_{Li}^{(2)}(n/t)
+
O_K(t^{-6}).
}
\]

---

# 6. Total second-derivative variation scale

Fix

\[
\eta>0
\]

and suppose

\[
c_H=\frac nH
\]

lies in a fixed compact positive interval

\[
[c_-,c_+].
\]

For

\[
t=Hu,
\qquad
1\le u\le1+\eta,
\]

the coordinate

\[
\frac nt
=
\frac{c_H}{u}
\]

lies in the compact interval

\[
\left[
\frac{c_-}{1+\eta},
c_+
\right].
\]

Therefore

\[
|\chi_n''(Hu)|
\le
C_{K,\eta}H^{-4}
\]

for sufficiently large \(H\).

Hence

\[
\boxed{
\int_H^{(1+\eta)H}
|\chi_n''(t)|dt
=
O_{K,\eta}(H^{-3}).
}
\]

More precisely,

\[
H^3
\int_H^{(1+\eta)H}
|\chi_n''(t)|dt
\to
\int_1^{1+\eta}
u^{-4}
\left|
K_{Li}^{(2)}
\left(
\frac c u
\right)
\right|du
\]

along matched-scale sequences

\[
c_H\to c>0.
\]

The convergence follows from the uniform compact asymptotic and

\[
\bigl||a+r|-|a|\bigr|
\le|r|.
\]

---

# 7. Conditional Li interior-response transfer theorem

The exact centered-primitive identity from Phase 5N is

\[
R_{\mathrm{int}}
=
-\overline E
\left(
\chi_n(B)-\chi_n(H)
\right)
+
\int_H^B
F(t)\chi_n''(t)dt.
\]

Assume RH.

The window-mean discrepancy satisfies

\[
\overline E
=
O_\eta\left(
\frac{\log H}
{H(\log\log H)^2}
\right).
\]

The endpoint susceptibility asymptotic gives

\[
|\chi_n(B)-\chi_n(H)|
=
O_{K,\eta}(H^{-2}).
\]

Therefore the mean channel satisfies

\[
\boxed{
R_{\mathrm{mean}}
=
O_{K,\eta}\left(
\frac{\log H}
{H^3(\log\log H)^2}
\right).
}
\]

Also,

\[
\|F\|_\infty
=
O_\eta\left(
\frac{\log H}
{(\log\log H)^2}
\right)
\]

and

\[
\int_H^B
|\chi_n''(t)|dt
=
O_{K,\eta}(H^{-3}).
\]

Thus the primitive channel satisfies

\[
\boxed{
R_{\mathrm{prim}}
=
O_{K,\eta}\left(
\frac{\log H}
{H^3(\log\log H)^2}
\right).
}
\]

Summing the two channels yields the conditional theorem:

\[
\boxed{
\text{RH}
\Longrightarrow
R_{\mathrm{int}}
=
O_{K,\eta}\left(
\frac{\log H}
{H^3(\log\log H)^2}
\right)
}
\]

uniformly for fixed relative window width

\[
\eta>0
\]

and matched-scale coordinates

\[
n/H
\]

in compact positive sets.

---

# 8. Comparison with the atom susceptibility scale

Uniformly on compact positive matched-scale coordinates,

\[
\chi_n(H)
=
H^{-2}
\Psi_{Li}(n/H)
+
O(H^{-4}).
\]

Thus the natural individual atom response scale is

\[
H^{-2}.
\]

Under RH,

\[
R_{\mathrm{int}}
=
O_{K,\eta}\left(
\frac{\log H}
{H^3(\log\log H)^2}
\right).
\]

Therefore

\[
\boxed{
H^2R_{\mathrm{int}}
=
O_{K,\eta}\left(
\frac{\log H}
{H(\log\log H)^2}
\right)
\to0.
}
\]

Hence the interior discrepancy-response channel is lower order than the natural \(H^{-2}\) susceptibility scale under RH.

This proves a conditional asymptotic suppression mechanism consistent with the small-interior finite geometry observed in Phases 5J through 5N.

---

# 9. Important normalization qualification

The conclusion

\[
R_{\mathrm{int}}=o(H^{-2})
\]

does not by itself imply that the normalized interior simplex share

\[
i
=
\frac{|R_{\mathrm{int}}|}
{
|R_{\mathrm{atom}}|
+
|R_{\mathrm{end}}|
+
|R_{\mathrm{int}}|
}
\]

tends to zero on every parameter sequence.

The denominator may also degenerate through profile zeros or signed-channel special geometry.

A conclusion

\[
i\to0
\]

requires a nondegeneracy lower bound for at least one competing channel at the relevant normalized scale.

For example, if

\[
|\Psi_{Li}(c_H)|
\ge\delta>0
\]

along a matched-scale sequence, then

\[
|R_{\mathrm{atom}}|
\gg H^{-2}
\]

and the conditional interior estimate implies

\[
i\to0.
\]

No global nondegeneracy assertion is made.

---

# 10. Prior-art and RH restrictions

The \(S_1\) primitive is classical.

The Riemann-von Mangoldt remainder decomposition is classical.

The RH bound for \(S_1\) is classical.

The integration-by-parts transfer mechanism is standard.

No originality claim is made for these components.

The theorem proved here is conditional on RH.

It does not prove RH.

It does not exclude an off-critical zero.

It does not establish an RH-equivalent criterion.

It does not establish unconditional asymptotic suppression.

Originality of the exact Li-susceptibility specialization remains under active prior-art review.



---

# Phase 5O-A adversarial correction

The initial Phase 5O second-derivative validator failed before the
second-derivative theorem was accepted.

The failure exposed an algebra error in the displayed derivative of

\[
J_{Li}(q).
\]

The originally committed derivative was false.

The correct derivative is

\[
\boxed{
J_{Li}'(q)
=
2q^3\cos q
+
18q^2\sin q
-
36q\cos q
-
12\sin q.
}
\]

Therefore

\[
K_{Li}^{(2)}(q)
=
3J_{Li}(q)
+
qJ_{Li}'(q)
\]

equals

\[
\boxed{
K_{Li}^{(2)}(q)
=
2q^4\cos q
+
24q^3\sin q
-
72q^2\cos q
-
48q\sin q.
}
\]

The initial claim that the \(q^3\sin q\) terms cancel was false.

The original shell workflow also continued after the validator exception
and committed the unvalidated Phase 5O files.

Therefore the original Phase 5O completion banner was procedurally void.

The conditional theorem may be restored only after the corrected
second-derivative profile passes the unchanged numerical consistency
validator.

No numerical acceptance threshold is changed.
