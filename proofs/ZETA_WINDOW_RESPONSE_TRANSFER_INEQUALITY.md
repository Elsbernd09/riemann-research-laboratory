# Deterministic Zeta-Window Response Transfer Inequality

## Phase 5F

This phase treats the empirical zero-counting remainder contribution as a linear response transform acting on a counting discrepancy.

The resulting stability inequalities are deterministic.

No probabilistic model for zeta zeros is required.

---

# 1. Counting-response transform

Let

\[
f_n(t)
=
\chi_n^{Li}(t).
\]

Let

\[
B=(1+\eta)H.
\]

For a counting discrepancy E on the window, define

\[
\boxed{
\mathcal T_{n,H,\eta}[E]
=
f_n(B)E(B)
-
f_n(H)E(H)
-
\int_H^B
E(t)f_n'(t)dt.
}
\]

For the empirical counting remainder

\[
E_D=N_D-M,
\]

the exact finite-dataset counting contribution is

\[
\boxed{
R_{\mathrm{count}}
=
f_n(H)\Delta N_D(H)
+
\mathcal T_{n,H,\eta}[E_D].
}
\]

---

# 2. Exact sup-norm stability inequality

By the triangle inequality,

\[
\boxed{
|\mathcal T_{n,H,\eta}[E]|
\le
\|E\|_{\infty,[H,B]}
\left[
|f_n(H)|
+
|f_n(B)|
+
\int_H^B|f_n'(t)|dt
\right].
}
\]

Define

\[
\boxed{
\Lambda_n(H,\eta)
=
|f_n(H)|
+
|f_n(B)|
+
\int_H^B|f_n'(t)|dt.
}
\]

Then

\[
\boxed{
|\mathcal T_{n,H,\eta}[E]|
\le
\Lambda_n(H,\eta)
\|E\|_\infty.
}
\]

For the empirical counting contribution,

\[
\boxed{
|R_{\mathrm{count}}|
\le
|f_n(H)|\Delta N_D(H)
+
\Lambda_n(H,\eta)
\|E_D\|_\infty.
}
\]

This inequality is deterministic.

---

# 3. Variation interpretation

Since \(f_n\) is continuously differentiable on a positive-height window,

\[
\operatorname{Var}_{[H,B]}(f_n)
=
\int_H^B|f_n'(t)|dt.
\]

Therefore

\[
\boxed{
\Lambda_n(H,\eta)
=
|f_n(H)|
+
|f_n(B)|
+
\operatorname{Var}_{[H,B]}(f_n).
}
\]

Thus the sup-norm response gain is controlled by endpoint magnitude and total variation of the susceptibility kernel.

---

# 4. Holder-family inequalities

For conjugate exponents

\[
1\le p,q\le\infty,
\qquad
1/p+1/q=1,
\]

Holder's inequality gives

\[
\boxed{
\begin{aligned}
|\mathcal T[E]|
\le{}&
|f(B)||E(B)|
+
|f(H)||E(H)|\\
&+
\|E\|_{L^p(H,B)}
\|f'\|_{L^q(H,B)}.
\end{aligned}
}
\]

In particular,

\[
\boxed{
|\mathcal T[E]|
\le
|f(B)||E(B)|
+
|f(H)||E(H)|
+
\|E\|_2\|f'\|_2.
}
\]

The L-infinity variation certificate and L2 Holder certificate may have different empirical tightness.

---

# 5. Leading derivative-response profile

The individual susceptibility profile is

\[
\Psi_{Li}(q)
=
-2q^2\cos q
-
4q\sin q.
\]

Its derivative is

\[
\Psi_{Li}'(q)
=
2q^2\sin q
-
8q\cos q
-
4\sin q.
\]

Define

\[
\boxed{
J_{Li}(q)
=
2\Psi_{Li}(q)
+
q\Psi_{Li}'(q).
}
\]

Then

\[
\boxed{
J_{Li}(q)
=
2q^3\sin q
-
12q^2\cos q
-
12q\sin q.
}
\]

Equivalently,

\[
\boxed{
J_{Li}(q)
=
2q
\left[
q^2\sin q
-
6q\cos q
-
6\sin q
\right].
}
\]

For matched scale \(n/t=q\),

\[
\frac d{dt}
\left[
t^{-2}\Psi_{Li}(n/t)
\right]
=
-t^{-3}J_{Li}(n/t).
\]

---

# 6. Continuum transfer envelope

Under

\[
n/H\to c
\]

with fixed positive eta, define

\[
\boxed{
\begin{aligned}
\mathcal L_\eta(c)
={}&
|\Psi_{Li}(c)|\\
&+
(1+\eta)^{-2}
\left|
\Psi_{Li}
\left(
\frac c{1+\eta}
\right)
\right|\\
&+
\int_1^{1+\eta}
u^{-3}
\left|
J_{Li}
\left(
\frac cu
\right)
\right|du.
\end{aligned}
}
\]

Using the compact-range susceptibility expansion,

\[
\boxed{
H^2\Lambda_n(H,\eta)
\to
\mathcal L_\eta(c)
}
\]

along matched-scale paths.

---

# 7. Normalized discrepancy scale

The exact deterministic bound is

\[
|R_{\mathrm{count}}|
\le
|f(H)|\Delta N(H)
+
\Lambda_n(H,\eta)
\|E\|_\infty.
\]

Under matched scale,

\[
|f(H)|
=
H^{-2}|\Psi(c)|
+
O(H^{-4})
\]

and

\[
\Lambda_n(H,\eta)
=
H^{-2}\mathcal L_\eta(c)
+
O(H^{-4}).
\]

Therefore

\[
\boxed{
\begin{aligned}
\frac H{\log H}
|R_{\mathrm{count}}|
\lesssim{}&
\frac{
|\Psi(c)|\Delta N(H)
}{
H\log H
}\\
&+
\frac{
\mathcal L_\eta(c)
}{
H\log H
}
\|E\|_\infty.
\end{aligned}
}
\]

If

\[
\|E\|_\infty=O(\log H),
\]

this gives candidate normalized scale

\[
O(H^{-1}).
\]

The transfer envelope isolates the coordinate-dependent response constant from the counting-remainder size.

---

# 8. Profile-to-transfer ratio

Define

\[
\boxed{
Q_\eta(c)
=
\frac{
|\Phi_\eta(c)|
}{
\mathcal L_\eta(c)
}
}
\]

when

\[
\mathcal L_\eta(c)>0.
\]

This compares smooth window-profile magnitude with worst-case sup-norm counting-discrepancy transfer.

At a smooth window-profile root,

\[
\Phi_\eta(c)=0,
\]

and therefore

\[
Q_\eta(c)=0.
\]

Thus a response-zero coordinate is not automatically a stability point.

The deterministic smooth signal vanishes while the counting-response transform need not.

---

# 9. Interpretation boundary

The transfer inequality is deterministic.

The continuum envelope relies on the project susceptibility asymptotic expansion under fixed compact similarity-coordinate and fixed relative-window assumptions.

The inequality does not establish a new bound for the classical zeta zero-counting remainder.

The profile-to-transfer ratio is a project-defined comparative quantity.

Originality remains unresolved.

No RH implication is established.
