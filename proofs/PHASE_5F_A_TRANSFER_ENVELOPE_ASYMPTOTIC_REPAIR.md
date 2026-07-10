# Phase 5F-A — Adversarial Repair of the Transfer-Envelope Asymptotic

## Status

PROOF-DEPENDENCY REPAIR.

## Trigger

CL-0173 was originally labeled PROVED IN PROJECT using an underjustified dependency.

The previously established susceptibility asymptotic

\[
\chi_n(\gamma)
=
\gamma^{-2}\Psi_{Li}(n/\gamma)
+
O(\gamma^{-4})
\]

does not, by itself, justify differentiation of the remainder term inside a total-variation argument.

Numerical convergence observed in Phase 5G cannot repair this proof gap.

The transfer-envelope asymptotic is therefore rederived directly from the exact gamma derivative of the Li susceptibility.

---

# Exact derivative setup

Let

\[
q=\frac n\gamma
\]

and

\[
x=\frac1\gamma.
\]

Then formally

\[
n=\frac qx.
\]

Define

\[
d(x)
=
1+\frac{x^2}{4}.
\]

Since

\[
D
=
\gamma^2+\frac14
=
x^{-2}d(x),
\]

and

\[
\theta(\gamma)
=
2\arctan\left(\frac1{2\gamma}\right)
=
2\arctan\left(\frac x2\right),
\]

the phase is

\[
\phi(q,x)
=
n\theta
=
\frac qx
2\arctan\left(\frac x2\right).
\]

Define the analytic continuation at \(x=0\) by

\[
\phi(q,0)=q.
\]

Because

\[
\frac{2\arctan(x/2)}x
=
1-\frac{x^2}{12}
+\frac{x^4}{80}
-\cdots,
\]

the function

\[
\frac{2\arctan(x/2)}x
\]

is analytic and even in \(x\) near zero.

Hence

\[
\phi(q,x)
\]

is analytic in \(q\) and \(x^2\) near \(x=0\).

---

# Exact scaled derivative representation

The exact Li susceptibility derivative is

\[
\chi_n'(\gamma)
=
\frac{8n\gamma}{D^3}A
-
\frac{2n}{D^2}A',
\]

where

\[
A
=
n\cos(n\theta)
+
2\gamma\sin(n\theta)
\]

and

\[
A'
=
\frac{n^2}{D}\sin(n\theta)
+
2\sin(n\theta)
-
\frac{2n\gamma}{D}\cos(n\theta).
\]

Using

\[
n=\frac qx,
\qquad
\gamma=\frac1x,
\qquad
D=x^{-2}d(x),
\]

we obtain

\[
A
=
x^{-1}
\left(
q\cos\phi
+
2\sin\phi
\right)
\]

and

\[
A'
=
\left(
\frac{q^2}{d}
+
2
\right)
\sin\phi
-
\frac{2q}{d}\cos\phi.
\]

Therefore

\[
\boxed{
\gamma^3\chi_n'(\gamma)
=
G(q,x)
}
\]

with

\[
G(q,x)
=
\frac{8q}{d^3}
\left(
q\cos\phi
+
2\sin\phi
\right)
-
\frac{2q}{d^2}
\left[
\left(
\frac{q^2}{d}
+
2
\right)
\sin\phi
-
\frac{2q}{d}\cos\phi
\right].
\]

Every occurrence of \(x\) enters through \(x^2\) or through the analytic even function

\[
2\arctan(x/2)/x.
\]

Thus \(G(q,x)\) is analytic in \(q\) and \(x^2\) on a neighborhood of every compact set

\[
K\times\{0\}
\]

with

\[
K\subset(0,\infty)
\]

compact.

---

# Limiting derivative profile

At

\[
x=0,
\]

we have

\[
d(0)=1
\]

and

\[
\phi(q,0)=q.
\]

Hence

\[
G(q,0)
=
8q
\left(
q\cos q
+
2\sin q
\right)
-
2q
\left[
(q^2+2)\sin q
-
2q\cos q
\right].
\]

Collecting terms,

\[
G(q,0)
=
12q^2\cos q
+
12q\sin q
-
2q^3\sin q.
\]

The Phase 5F derivative-response profile is

\[
J_{Li}(q)
=
2q^3\sin q
-
12q^2\cos q
-
12q\sin q.
\]

Therefore

\[
\boxed{
G(q,0)=-J_{Li}(q).
}
\]

---

# Uniform compact derivative asymptotic

Let

\[
K\subset(0,\infty)
\]

be compact.

Because \(G(q,x)\) is analytic in \(q\) and \(x^2\) near

\[
K\times\{0\},
\]

there exist a neighborhood in \(x\) and a constant

\[
C_K<\infty
\]

such that

\[
|
G(q,x)-G(q,0)
|
\le
C_Kx^2
\]

uniformly for

\[
q\in K.
\]

Since

\[
x=\gamma^{-1},
\]

we obtain

\[
\boxed{
\gamma^3\chi_n'(\gamma)
=
-J_{Li}(q)
+
O_K(\gamma^{-2}),
\qquad
q=\frac n\gamma,
}
\]

uniformly for

\[
q\in K.
\]

This statement is first established on the continuous matched-scale representation in \((q,x)\).

Integer-valued \(n\) matched-scale sequences are restrictions of this representation to

\[
q=n/\gamma.
\]

Therefore the same uniform estimate applies to such sequences whenever

\[
n/\gamma\in K.
\]

---

# Endpoint susceptibility asymptotic

The exact susceptibility is

\[
\chi_n(\gamma)
=
-\frac{2n}{D^2}
\left[
n\cos(n\theta)
+
2\gamma\sin(n\theta)
\right].
\]

With the same variables,

\[
\gamma^2\chi_n(\gamma)
=
-\frac{2q}{d(x)^2}
\left(
q\cos\phi(q,x)
+
2\sin\phi(q,x)
\right).
\]

The right-hand side is analytic in \(q\) and \(x^2\).

At \(x=0\),

\[
\gamma^2\chi_n(\gamma)
\longrightarrow
-2q
\left(
q\cos q
+
2\sin q
\right).
\]

Thus

\[
\Psi_{Li}(q)
=
-2q
\left(
q\cos q
+
2\sin q
\right)
\]

and uniformly for \(q\) in compact positive sets,

\[
\boxed{
\gamma^2\chi_n(\gamma)
=
\Psi_{Li}(q)
+
O_K(\gamma^{-2}).
}
\]

---

# Repaired transfer-envelope asymptotic

Define

\[
\Lambda_n(H,\eta)
=
|\chi_n(H)|
+
|\chi_n((1+\eta)H)|
+
\int_H^{(1+\eta)H}
|\chi_n'(t)|dt.
\]

Let

\[
c_H=\frac nH.
\]

Fix

\[
\eta>0
\]

and assume

\[
c_H\in[c_-,c_+]
\]

for fixed

\[
0<c_-<c_+<\infty.
\]

Set

\[
t=Hu.
\]

Then

\[
1\le u\le1+\eta
\]

and

\[
q
=
\frac nt
=
\frac{c_H}{u}
\]

lies in the compact positive interval

\[
K'
=
\left[
\frac{c_-}{1+\eta},
c_+
\right].
\]

The direct derivative asymptotic gives

\[
t^3\chi_n'(t)
=
-J_{Li}(n/t)
+
O_{K'}(t^{-2}).
\]

Because

\[
t=Hu
\]

with \(u\) in a fixed compact interval,

\[
\chi_n'(Hu)
=
-H^{-3}u^{-3}
J_{Li}(c_H/u)
+
O(H^{-5})
\]

uniformly in \(u\) and \(c_H\).

Therefore

\[
H^2
\int_H^{(1+\eta)H}
|\chi_n'(t)|dt
=
\int_1^{1+\eta}
u^{-3}
\left|
-J_{Li}(c_H/u)
+
O(H^{-2})
\right|du.
\]

Using

\[
\bigl||a+r|-|a|\bigr|
\le|r|,
\]

the difference between this integral and

\[
\int_1^{1+\eta}
u^{-3}
|J_{Li}(c_H/u)|du
\]

is

\[
O(H^{-2})
\]

uniformly for

\[
c_H\in[c_-,c_+].
\]

The endpoint susceptibility asymptotic gives

\[
H^2|\chi_n(H)|
=
|\Psi_{Li}(c_H)|
+
O(H^{-2})
\]

and

\[
H^2
|\chi_n((1+\eta)H)|
=
(1+\eta)^{-2}
\left|
\Psi_{Li}
\left(
\frac{c_H}{1+\eta}
\right)
\right|
+
O(H^{-2}).
\]

Define

\[
\mathcal L_\eta(c)
=
|\Psi_{Li}(c)|
+
(1+\eta)^{-2}
\left|
\Psi_{Li}
\left(
\frac c{1+\eta}
\right)
\right|
+
\int_1^{1+\eta}
u^{-3}
|J_{Li}(c/u)|du.
\]

Summing the endpoint and variation contributions yields

\[
\boxed{
H^2\Lambda_n(H,\eta)
=
\mathcal L_\eta(c_H)
+
O(H^{-2})
}
\]

uniformly for

\[
c_H\in[c_-,c_+].
\]

If

\[
c_H\to c>0,
\]

continuity of

\[
\mathcal L_\eta
\]

gives

\[
\boxed{
H^2\Lambda_n(H,\eta)
\to
\mathcal L_\eta(c).
}
\]

---

# Adversarial conclusion

The transfer-envelope asymptotic is now derived directly from the exact susceptibility derivative.

The repaired proof does not differentiate a previously stated big-O remainder.

Phase 5G numerical convergence was validation evidence only and was not used to close the proof gap.

No explicit numerical remainder constant is claimed.

No RH consequence follows.

