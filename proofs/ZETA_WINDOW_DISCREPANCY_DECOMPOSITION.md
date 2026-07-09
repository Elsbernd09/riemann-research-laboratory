# Exact Finite-Dataset Zeta-Window Response Discrepancy Decomposition

## Phase 5D

This phase separates the discrepancy between the finite discrete zeta-zero window response and the Phase 5C finite-height smooth-density profile into:

1. an empirical zero-counting remainder;
2. a Li-kernel asymptotic truncation remainder.

The Stieltjes decomposition is exact for the frozen finite computational dataset.

---

# 1. Empirical counting function

Let D denote the frozen finite zero-ordinate dataset.

Define

\[
N_D(T)
=
\#\{
\gamma_j\in D:
\gamma_j\le T
\}.
\]

Define the smooth counting model

\[
M(T)
=
\frac{T}{2\pi}
\log\left(
\frac{T}{2\pi}
\right)
-
\frac{T}{2\pi}
+
\frac78.
\]

Then

\[
M'(T)
=
\frac{1}{2\pi}
\log\left(
\frac{T}{2\pi}
\right).
\]

Define the empirical counting remainder

\[
\boxed{
E_D(T)
=
N_D(T)-M(T).
}
\]

This definition is exact for the finite data.

---

# 2. Discrete window response

Let

\[
f_n(t)
=
\chi_n^{\mathrm{Li}}(t).
\]

For

\[
B=(1+\eta)H,
\]

define

\[
\mathcal W_n(H,\eta)
=
\sum_{H\le\gamma_j\le B}
f_n(\gamma_j).
\]

Equivalently,

\[
\boxed{
\mathcal W_n(H,\eta)
=
\int_{[H,B]}
f_n(t)\,dN_D(t).
}
\]

---

# 3. Left-endpoint atom

The Phase 5C height anchors H are themselves dataset zero ordinates.

Therefore

\[
\Delta N_D(H)
=
N_D(H)-N_D(H^-)
\]

is nonzero.

Write

\[
\int_{[H,B]}f\,dN_D
=
f(H)\Delta N_D(H)
+
\int_{(H,B]}f\,dN_D.
\]

For the frozen indexed dataset anchors,

\[
\Delta N_D(H)=1.
\]

The derivation keeps the jump explicit.

---

# 4. Exact empirical counting-remainder identity

Since

\[
N_D=M+E_D,
\]

Stieltjes integration by parts on

\[
(H,B]
\]

gives

\[
\int_{(H,B]}f\,dE_D
=
f(B)E_D(B)
-
f(H)E_D(H)
-
\int_H^B E_D(t)f'(t)\,dt.
\]

Therefore

\[
\boxed{
\begin{aligned}
\mathcal W_n(H,\eta)
={}&
\int_H^B
f_n(t)M'(t)\,dt\\
&+
f_n(H)\Delta N_D(H)\\
&+
f_n(B)E_D(B)\\
&-
f_n(H)E_D(H)\\
&-
\int_H^B
E_D(t)f_n'(t)\,dt.
\end{aligned}
}
\]

Define

\[
\boxed{
S_{\mathrm{exact}}
=
\int_H^B
\chi_n^{\mathrm{Li}}(t)
M'(t)\,dt
}
\]

and

\[
\boxed{
R_{\mathrm{count}}
=
f_n(H)\Delta N_D(H)
+
f_n(B)E_D(B)
-
f_n(H)E_D(H)
-
\int_H^B E_D(t)f_n'(t)\,dt.
}
\]

Then

\[
\boxed{
\mathcal W_n
=
S_{\mathrm{exact}}
+
R_{\mathrm{count}}.
}
\]

This is an exact finite-dataset identity.

---

# 5. Leading-profile smooth benchmark

Define

\[
\boxed{
S_{\mathrm{profile}}
=
\int_H^B
t^{-2}
\Psi_{\mathrm{Li}}
\left(
\frac nt
\right)
M'(t)\,dt.
}
\]

Under

\[
c=n/H,
\]

the Phase 5C finite-height benchmark satisfies

\[
\boxed{
\frac H{\log H}
S_{\mathrm{profile}}
=
\Phi_{\eta,H}^{FH}(c).
}
\]

Define

\[
\boxed{
R_{\mathrm{kernel}}
=
S_{\mathrm{exact}}
-
S_{\mathrm{profile}}.
}
\]

Therefore

\[
\boxed{
\mathcal W_n
-
S_{\mathrm{profile}}
=
R_{\mathrm{count}}
+
R_{\mathrm{kernel}}.
}
\]

After Phase 5C normalization,

\[
\boxed{
\frac H{\log H}
\mathcal W_n
-
\Phi_{\eta,H}^{FH}(n/H)
=
\frac H{\log H}
R_{\mathrm{count}}
+
\frac H{\log H}
R_{\mathrm{kernel}}.
}
\]

---

# 6. Kernel-remainder scale

For

\[
q=n/t
\]

in a fixed compact positive range, the validated individual susceptibility expansion is

\[
\chi_n^{\mathrm{Li}}(t)
=
t^{-2}\Psi_{\mathrm{Li}}(q)
+
t^{-4}K_{\mathrm{Li}}(q)
+
O(t^{-6}).
\]

Hence

\[
\chi_n^{\mathrm{Li}}(t)
-
t^{-2}\Psi_{\mathrm{Li}}(n/t)
=
O(t^{-4})
\]

uniformly on a fixed relative-height window under the compact-q hypothesis.

Because

\[
M'(t)
\asymp
\log H
\]

and the window length is

\[
O(H),
\]

one expects

\[
\boxed{
R_{\mathrm{kernel}}
=
O(H^{-3}\log H).
}
\]

Thus

\[
\boxed{
\frac H{\log H}
R_{\mathrm{kernel}}
=
O(H^{-2}).
}
\]

This scale follows from the project susceptibility expansion and fixed-window geometry.

---

# 7. Counting-remainder scale

At matched scale

\[
n\asymp H,
\]

the leading susceptibility form gives

\[
f_n(t)=O(H^{-2})
\]

on a fixed relative-height window.

Differentiating the leading profile form gives

\[
f_n'(t)
\approx
-t^{-3}
\left[
2\Psi_{\mathrm{Li}}(q)
+
q\Psi_{\mathrm{Li}}'(q)
\right],
\qquad
q=n/t.
\]

Thus

\[
f_n'(t)=O(H^{-3}).
\]

If the counting remainder is on a logarithmic scale,

\[
E_D(t)=O(\log H),
\]

then

\[
R_{\mathrm{count}}
=
O(H^{-2}\log H),
\]

and therefore

\[
\boxed{
\frac H{\log H}
R_{\mathrm{count}}
=
O(H^{-1}).
}
\]

The exact finite-dataset decomposition does not depend on this asymptotic scale assumption.

The scale comparison motivates the Phase 5E empirical test.

---

# 8. Computable counting-remainder certificate

Let

\[
\|E_D\|_{\infty,[H,B]}
=
\sup_{H\le t\le B}
|E_D(t)|.
\]

Then

\[
\boxed{
\begin{aligned}
|R_{\mathrm{count}}|
\le{}&
|f(H)|\Delta N_D(H)\\
&+
|f(B)||E_D(B)|\\
&+
|f(H)||E_D(H)|\\
&+
\|E_D\|_\infty
\int_H^B|f'(t)|dt.
\end{aligned}
}
\]

The right side is a computable finite-dataset discrepancy certificate.

---

# 9. Endpoint-atom diagnostic

For Phase 5C zero-anchored windows,

\[
\Delta N_D(H)=1.
\]

Therefore

\[
\boxed{
R_{\mathrm{atom}}
=
\chi_n^{\mathrm{Li}}(H).
}
\]

Its Phase 5C normalized contribution is

\[
\boxed{
\frac H{\log H}
R_{\mathrm{atom}}.
}
\]

Phase 5E must quantify whether the left-inclusive zero anchor materially contributes to the remaining finite-height residual.

---

# 10. Interpretation boundary

The exact Stieltjes decomposition is an identity for the frozen empirical counting function N_D.

A theorem transferring the decomposition to a globally complete zeta zero sequence requires a precisely defined full zero-counting measure and corresponding completeness assumptions.

This phase does not prove RH.

This phase does not prove a new bound for the classical zeta zero-counting remainder.

Originality remains unresolved.
