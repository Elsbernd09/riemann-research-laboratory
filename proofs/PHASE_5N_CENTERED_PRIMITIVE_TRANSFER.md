# Phase 5N — Centered-Primitive Transfer Identity

## Setup

Let

\[
f(t)=\chi_n^{Li}(t)
\]

on

\[
[H,B],
\qquad
B>H.
\]

Let

\[
E(t)=E_D(t)
\]

denote the empirical zero-counting discrepancy used in the finite dataset.

Define the window length

\[
L=B-H
\]

and the discrepancy mean

\[
\overline E
=
\frac1L
\int_H^B E(s)\,ds.
\]

Define the centered discrepancy primitive

\[
F(t)
=
\int_H^t
(E(s)-\overline E)\,ds.
\]

Then

\[
F(H)=0.
\]

Also,

\[
F(B)
=
\int_H^B E(s)\,ds
-
(B-H)\overline E
=
0.
\]

Where differentiation is interpreted away from empirical counting jumps,

\[
F'(t)=E(t)-\overline E.
\]

The finite staircase structure permits intervalwise integration and summation.

---

# Exact second-order identity

Since

\[
E(t)=\overline E+F'(t),
\]

we have

\[
\int_H^B E(t)f'(t)\,dt
=
\overline E
\int_H^B f'(t)\,dt
+
\int_H^B F'(t)f'(t)\,dt.
\]

The first term is

\[
\overline E
(f(B)-f(H)).
\]

For the second term, integration by parts gives

\[
\int_H^B F'(t)f'(t)\,dt
=
[F(t)f'(t)]_H^B
-
\int_H^B F(t)f''(t)\,dt.
\]

Because

\[
F(H)=F(B)=0,
\]

the boundary term vanishes.

Therefore

\[
\boxed{
\int_H^B E(t)f'(t)\,dt
=
\overline E
(f(B)-f(H))
-
\int_H^B F(t)f''(t)\,dt
}.
\]

For the interior count-response channel

\[
R_{\mathrm{int}}
=
-\int_H^B E(t)f'(t)\,dt,
\]

we obtain

\[
\boxed{
R_{\mathrm{int}}
=
-\overline E
(f(B)-f(H))
+
\int_H^B F(t)f''(t)\,dt
}.
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
\int_H^B F(t)f''(t)\,dt.
\]

Then exactly

\[
\boxed{
R_{\mathrm{int}}
=
R_{\mathrm{mean}}
+
R_{\mathrm{prim}}
}.
\]

---

# Deterministic second-order transfer inequality

By the triangle inequality,

\[
|R_{\mathrm{int}}|
\le
|\overline E|
|f(B)-f(H)|
+
\left|
\int_H^B F(t)f''(t)\,dt
\right|.
\]

Also,

\[
\left|
\int_H^B F(t)f''(t)\,dt
\right|
\le
\|F\|_{\infty,[H,B]}
\int_H^B|f''(t)|dt.
\]

Therefore

\[
\boxed{
|R_{\mathrm{int}}|
\le
|\overline E|
|f(B)-f(H)|
+
\|F\|_\infty
\int_H^B|f''(t)|dt
}.
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
\boxed{
|R_{\mathrm{int}}|\le C_2.
}
\]

---

# Comparison with first absolute-integral scale

Define

\[
C_1
=
\int_H^B|E(t)f'(t)|dt.
\]

Define

\[
Q_{21}
=
\frac{C_2}{C_1}
\]

when \(C_1>0\).

A small value of \(Q_{21}\) means that the centered-primitive transfer inequality captures cancellation discarded by the first absolute-integral scale.

No claim that \(C_2\le C_1\) holds universally.

---

# Centered primitive compression

Define

\[
G
=
\frac{
\|F\|_\infty
}{
(B-H)
\|E-\overline E\|_\infty
}
\]

when the denominator is positive.

Since

\[
F(t)
=
\int_H^t
(E(s)-\overline E)ds,
\]

we have

\[
|F(t)|
\le
(t-H)
\|E-\overline E\|_\infty
\le
(B-H)
\|E-\overline E\|_\infty.
\]

Thus

\[
\boxed{
0\le G\le1.
}
\]

Small \(G\) quantifies cancellation in the cumulative centered discrepancy.

---

# Restrictions

This identity and inequality are elementary deterministic integration-by-parts mechanisms.

No novelty claim is made.

No asymptotic zero-counting bound is proved.

No estimate for \(\|F\|_\infty\) is proved.

No RH consequence follows.

