# 1. Scope and Main Result

## 1.1 Problem

Consider the Li zero-coordinate kernel

\[
f_n(z)
=
1-
\left(
1-\frac1z
\right)^n.
\]

For a symmetric horizontal perturbation of a zero coordinate around the critical line, the quadratic response is governed by

\[
\chi_n^{Li}(\gamma)
=
2\Re
f_n''
\left(
\frac12+i\gamma
\right).
\]

The central problem of this paper is not to derive another RH criterion.

Instead, we study how the global zero-counting discrepancy transfers through the derivative of this matched-scale susceptibility.

Let

\[
N(t)
\]

be the classical nontrivial-zero counting function and define

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

Set

\[
E(t)=N(t)-M(t).
\]

For fixed relative width

\[
\eta>0,
\]

write

\[
B=(1+\eta)H.
\]

Define

\[
R_{\mathrm{int}}(n;H,\eta)
=
-
\int_H^B
E(t)
\chi_n'(t)
\,dt.
\]

The matched-scale regime is

\[
\frac nH\in K,
\]

where

\[
K\Subset(0,\infty)
\]

is fixed.

---

## 1.2 Main unconditional theorem

### Theorem A

Fix

\[
\eta>0
\]

and

\[
K\Subset(0,\infty).
\]

Uniformly for positive integers \(n\) satisfying

\[
n/H\in K,
\]

one has

\[
\boxed{
R_{\mathrm{int}}(n;H,\eta)
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right)
}
\]

as

\[
H\to\infty.
\]

Consequently,

\[
\boxed{
H^2R_{\mathrm{int}}(n;H,\eta)
\to0
}
\]

uniformly on compact positive matched-scale ranges.

No assumption of the Riemann Hypothesis is used.

---

## 1.3 Conditional logarithmic refinement

### Corollary B

Assume the Riemann Hypothesis.

Under the hypotheses of Theorem A,

\[
\boxed{
R_{\mathrm{int}}(n;H,\eta)
=
O_{K,\eta}
\left(
\frac{\log H}
{H^3(\log\log H)^2}
\right).
}
\]

Thus RH improves the logarithmic factor.

The asymptotic suppression itself is already unconditional.

---

## 1.4 Interpretation

The natural matched-scale susceptibility size is

\[
H^{-2}.
\]

Theorem A gives

\[
R_{\mathrm{int}}
=
o(H^{-2}).
\]

Thus the global interior discrepancy-response channel is lower order than the natural susceptibility scale.

This statement concerns response asymptotics.

It is not an RH criterion.

