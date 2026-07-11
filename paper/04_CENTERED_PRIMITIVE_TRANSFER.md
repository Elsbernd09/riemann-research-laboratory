# 4. Centered-Primitive Transfer

## 4.1 Window mean

Set

\[
B=(1+\eta)H.
\]

Define

\[
\overline E
=
\frac1{B-H}
\int_H^B
E(s)\,ds.
\]

From

\[
E=S+R,
\qquad
R(t)=O(1/t),
\]

and

\[
S_1(t)=O(\log t),
\]

we obtain

\[
\boxed{
\overline E
=
O_\eta
\left(
\frac{\log H}{H}
\right).
}
\]

---

## 4.2 Centered primitive

Define

\[
F(t)
=
\int_H^t
\left(
E(s)-\overline E
\right)ds.
\]

Then

\[
F(H)=F(B)=0.
\]

If

\[
A(t)
=
\int_{t_0}^tE(s)\,ds,
\]

then

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

Thus \(F\) is the secant-detrended increment of an antiderivative of the zero-counting discrepancy.

Since

\[
A(t)
=
S_1(t)
+
\int_{t_0}^tR(s)\,ds
+
C_0,
\]

we obtain

\[
\boxed{
\|F\|_{\infty,[H,B]}
=
O_\eta(\log H).
}
\]

---

## 4.3 Exact transfer identity

Define

\[
R_{\mathrm{int}}
=
-
\int_H^B
E(t)\chi_n'(t)\,dt.
\]

Since

\[
E(t)
=
\overline E+F'(t)
\]

almost everywhere,

\[
\begin{aligned}
R_{\mathrm{int}}
&=
-\overline E
\int_H^B
\chi_n'(t)dt
-
\int_H^B
F'(t)\chi_n'(t)dt.
\end{aligned}
\]

Using

\[
F(H)=F(B)=0,
\]

integration by parts gives

\[
\boxed{
R_{\mathrm{int}}
=
-\overline E
\left(
\chi_n(B)-\chi_n(H)
\right)
+
\int_H^B
F(t)\chi_n''(t)\,dt.
}
\]

Define

\[
R_{\mathrm{mean}}
=
-\overline E
\left(
\chi_n(B)-\chi_n(H)
\right)
\]

and

\[
R_{\mathrm{prim}}
=
\int_H^B
F(t)\chi_n''(t)\,dt.
\]

Then

\[
\boxed{
R_{\mathrm{int}}
=
R_{\mathrm{mean}}
+
R_{\mathrm{prim}}.
}
\]

This exact identity is the structural engine of the paper.

