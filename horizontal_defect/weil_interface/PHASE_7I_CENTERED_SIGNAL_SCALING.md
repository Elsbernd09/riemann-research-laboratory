# Phase 7I — Centered Quartet Signal Scaling Law

## Purpose

Phase 7H built the centered finite-rank quartet matrix

\[
C_m(x,\gamma)
=
\sum_{\epsilon=\pm1}
\sum_{\eta=\pm1}
v_m(\rho_{\epsilon,\eta}(x))v_m(\rho_{\epsilon,\eta}(x))^*
-
2\sum_{\eta=\pm1}
v_m(\rho_{0,\eta})v_m(\rho_{0,\eta})^*.
\]

This phase proves the first scaling law:

\[
C_m(x,\gamma)=O(x^2)
\]

as \(x\to0\).

This is not a Weil theorem.

This is not an RH proof.

It is a finite-rank diagnostic scaling theorem.

---

# 1. Setup

Let

\[
\rho_{\epsilon,\eta}(x)
=
\frac12+\epsilon x+i\eta\gamma,
\]

where

\[
\epsilon,\eta\in\{-1,+1\}.
\]

Let

\[
w(\rho)=1-\frac1\rho
\]

and

\[
v_m(\rho)
=
(w(\rho),w(\rho)^2,\ldots,w(\rho)^m)^T.
\]

Define

\[
A_\eta(x)
=
v_m\left(\frac12+x+i\eta\gamma\right)
v_m\left(\frac12+x+i\eta\gamma\right)^*.
\]

Then

\[
C_m(x,\gamma)
=
\sum_{\eta=\pm1}
\left[
A_\eta(x)+A_\eta(-x)-2A_\eta(0)
\right].
\]

Thus \(C_m\) is a centered second difference.

---

# 2. Analyticity

For fixed \(\gamma\ne0\), the map

\[
x\mapsto
w\left(\frac12+x+i\eta\gamma\right)
\]

is real-analytic near \(x=0\), because the denominator

\[
\frac12+x+i\eta\gamma
\]

does not vanish near \(x=0\).

Therefore each matrix entry of \(A_\eta(x)\) is real-analytic near \(x=0\).

---

# 3. Centered second-difference expansion

Since each entry of \(A_\eta(x)\) is real-analytic, Taylor expansion gives

\[
A_\eta(x)
=
A_\eta(0)
+
xA_\eta'(0)
+
\frac{x^2}{2}A_\eta''(0)
+
O(x^3),
\]

and

\[
A_\eta(-x)
=
A_\eta(0)
-
xA_\eta'(0)
+
\frac{x^2}{2}A_\eta''(0)
+
O(x^3).
\]

Adding gives

\[
A_\eta(x)+A_\eta(-x)-2A_\eta(0)
=
x^2A_\eta''(0)+O(x^4).
\]

The odd powers cancel.

Therefore

\[
C_m(x,\gamma)
=
x^2
\sum_{\eta=\pm1}
A_\eta''(0)
+
O(x^4).
\]

---

# 4. Main theorem

## Theorem

For fixed degree \(m\) and fixed \(\gamma\ne0\),

\[
C_m(x,\gamma)
=
x^2B_m(\gamma)+O_{m,\gamma}(x^4),
\]

where

\[
B_m(\gamma)
=
\sum_{\eta=\pm1}
A_\eta''(0).
\]

In particular,

\[
\|C_m(x,\gamma)\|_F
=
O_{m,\gamma}(x^2).
\]

If

\[
B_m(\gamma)\ne0,
\]

then

\[
\|C_m(x,\gamma)\|_F
\asymp_{m,\gamma}
x^2
\]

as \(x\to0\).

---

# 5. Interpretation

The centered finite-rank testbed sees horizontal displacement at second order.

This agrees with the geometry of horizontal defect:

\[
\beta-\frac12=x.
\]

Because the quartet is symmetric under

\[
x\mapsto -x,
\]

the first-order term cancels.

The leading diagnostic signal is quadratic.

---

# 6. Boundary

This scaling law is a finite-rank analytic statement about the diagnostic testbed.

It does not prove RH.

It does not define a classical Weil quadratic form.

It does not prove arithmetic-side control.

The next problem is to identify whether the second-order coefficient matrix

\[
B_m(\gamma)
\]

has stable positive and negative Rayleigh directions.

