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


---

# Adversarial correction: direct derivative asymptotic

## Reason for correction

An earlier proof dependency for the matched-scale transfer-envelope asymptotic was underjustified.

The susceptibility expansion

\[
\chi_n(\gamma)
=
\gamma^{-2}\Psi_{Li}(n/\gamma)
+
O(\gamma^{-4})
\]

does not, by itself, justify differentiation of the remainder inside the total-variation term.

In particular, an estimate

\[
f=g+O(h)
\]

does not automatically imply a corresponding derivative estimate.

Therefore the derivative asymptotic required for the variation term is derived directly from the exact formula for

\[
\chi_n'(\gamma).
\]

Numerical convergence observed in Phase 5G is validation only and does not repair a proof dependency.

## Exact derivative input

Let

\[
D=\gamma^2+\frac14,
\qquad
\theta=2\arctan\frac1{2\gamma},
\qquad
q=\frac n\gamma.
\]

The exact susceptibility derivative is

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

## Compact matched-scale reparameterization

Set

\[
x=\frac1\gamma,
\qquad
q=\frac n\gamma.
\]

Then

\[
\gamma=x^{-1},
\qquad
n=\frac qx,
\]

and

\[
D
=
x^{-2}
\left(
1+\frac{x^2}{4}
\right).
\]

Also,

\[
\theta
=
2\arctan\frac x2.
\]

For \(q\) in a compact positive set \(K\),

\[
n\theta
=
\frac qx
2\arctan\frac x2
=
q-\frac{q}{12}x^2+O_K(x^4)
\]

uniformly as \(x\to0\).

After substitution of

\[
\gamma=x^{-1},
\qquad
n=q/x
\]

into the exact derivative formula, the scaled derivative

\[
G(q,x)
:=
\gamma^3\chi_n'(\gamma)
\]

is a smooth function of \(q\) and \(x^2\) in a neighborhood of

\[
K\times\{0\}.
\]

In particular \(G\) is even in \(x\).

Direct evaluation at \(x=0\) gives

\[
G(q,0)
=
-J_{Li}(q),
\]

where

\[
J_{Li}(q)
=
2\Psi_{Li}(q)+q\Psi_{Li}'(q)
\]

and explicitly

\[
J_{Li}(q)
=
2q^3\sin q
-
12q^2\cos q
-
12q\sin q.
\]

By smoothness, evenness in \(x\), and compactness of \(K\),

\[
G(q,x)
+
J_{Li}(q)
=
O_K(x^2)
\]

uniformly for \(q\in K\).

Therefore

\[
\boxed{
\gamma^3\chi_n'(\gamma)
=
-J_{Li}(q)
+
O_K(\gamma^{-2}),
\qquad
q=n/\gamma,
}
\]

uniformly for \(q\) in compact positive sets.

## Transfer to the total-variation term

Fix

\[
\eta>0
\]

and suppose

\[
c_H=\frac nH
\]

lies in a compact positive interval

\[
K=[c_-,c_+].
\]

Set

\[
t=Hu,
\qquad
1\le u\le1+\eta.
\]

Then

\[
q=\frac nt=\frac{c_H}{u}
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
\chi_n'(Hu)
=
H^{-3}u^{-3}
\left[
-J_{Li}(c_H/u)
+
O_{K',\eta}(H^{-2})
\right]
\]

uniformly in \(u\in[1,1+\eta]\).

Hence

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
\right|
du.
\]

Use

\[
\big||a+r|-|a|\big|
\le|r|.
\]

The uniform derivative remainder therefore implies

\[
H^2
\int_H^{(1+\eta)H}
|\chi_n'(t)|dt
=
\int_1^{1+\eta}
u^{-3}
|J_{Li}(c_H/u)|du
+
O(H^{-2}).
\]

## Endpoint terms

The independently established uniform susceptibility asymptotic gives

\[
\gamma^2\chi_n(\gamma)
=
\Psi_{Li}(n/\gamma)
+
O_K(\gamma^{-2})
\]

on compact positive matched-scale sets.

Therefore

\[
H^2|\chi_n(H)|
=
|\Psi_{Li}(c_H)|
+
O(H^{-2}),
\]

using again

\[
\big||a+r|-|a|\big|\le|r|.
\]

For

\[
B=(1+\eta)H,
\]

we similarly obtain

\[
H^2|\chi_n(B)|
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

## Repaired transfer-envelope asymptotic

Recall

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

Combining the endpoint and variation estimates gives

\[
\boxed{
H^2\Lambda_n(H,\eta)
=
\mathcal L_\eta(c_H)
+
O(H^{-2}),
}
\]

uniformly for \(c_H=n/H\) in compact positive sets, where

\[
\mathcal L_\eta(c)
=
|\Psi_{Li}(c)|
+
(1+\eta)^{-2}
\left|
\Psi_{Li}
\left(
\frac{c}{1+\eta}
\right)
\right|
+
\int_1^{1+\eta}
u^{-3}
|J_{Li}(c/u)|du.
\]

If

\[
c_H\to c>0,
\]

continuity of \(\mathcal L_\eta\) implies

\[
H^2\Lambda_n(H,\eta)
\to
\mathcal L_\eta(c).
\]

This proof uses the exact susceptibility derivative formula and does not differentiate an asymptotic remainder.
