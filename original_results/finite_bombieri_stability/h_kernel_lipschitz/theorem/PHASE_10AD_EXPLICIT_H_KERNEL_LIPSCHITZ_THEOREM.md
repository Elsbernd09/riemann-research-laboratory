# Phase 10AD — Explicit H-Kernel Lipschitz Theorem

## Purpose

Earlier phases developed:

1. symbolic derivative majorants for \(K^*\);
2. concrete compact-domain majorants;
3. an \(L_H(U,t)\) calculator.

Phase 10AD proves the explicit finite \(H\)-kernel Lipschitz theorem.

This replaces the abstract assumption

\[
L_t(U)
\]

with a computable constant

\[
L_H(U,t).
\]

---

# 1. Kernel recalled

Let

\[
K_t(z)=\frac{\sin(tz)}{tz},
\]

with removable value

\[
K_t(0)=1.
\]

Let

\[
c_t=\frac{t}{\sinh t}.
\]

Define

\[
K^*(x,y;t)
=
K_t(x-y)
-
c_t\left(\frac12+iy\right)K_t(i/2-y)K_t(i/2+x)
-
c_t\left(\frac12-iy\right)K_t(i/2+y)K_t(i/2-x).
\]

The finite kernel is

\[
H(x,y;t)
=
\frac{2t}{1/4+y^2}K^*(x,y;t).
\]

---

# 2. Compact-domain hypotheses

Let \(U\subset\mathbb C^2\) be a compact domain for \((x,y)\).

Assume:

1. all shifted \(K_t\)-arguments appearing in \(K^*\) lie in a compact box \(Z(R,S)\);
2. all \(y\)-values lie in \(Y(R_y,S_y)\);
3. the denominator avoids zero:
\[
\Delta_Y=\inf_{y\in Y(R_y,S_y)}|1/4+y^2|>0;
\]
4. \(r>0\) is a Cauchy buffer radius for the \(K_t\) derivative estimate.

---

# 3. Concrete majorants

Define

\[
\rho_y=\sqrt{R_y^2+S_y^2}.
\]

Use the compact-domain majorants:

\[
A_0=e^{|t|S},
\]

\[
A_1=\frac{\exp(|t|(S+r))}{r},
\]

\[
B_0=\frac{1}{\Delta_Y},
\]

\[
B_1=\frac{2\rho_y}{\Delta_Y^2},
\]

\[
C_0=\frac12+\rho_y.
\]

Then define

\[
M_0=A_0+2|c_t|C_0A_0^2,
\]

\[
M_x=A_1+2|c_t|C_0A_0A_1,
\]

\[
M_y=A_1+2|c_t|(A_0^2+C_0A_0A_1).
\]

Finally define

\[
L_x=2|t|B_0M_x,
\]

\[
L_y=2|t|(B_1M_0+B_0M_y),
\]

and

\[
L_H(U,t)=L_x+L_y.
\]

---

# Theorem 10AD.1 — Explicit finite \(H\)-kernel Lipschitz theorem

Under the compact-domain hypotheses above, for all

\[
(x,y),(x',y')\in U,
\]

the finite kernel \(H\) satisfies

\[
|H(x',y';t)-H(x,y;t)|
\leq
L_H(U,t)(|x'-x|+|y'-y|).
\]

---

# Proof

The symbolic derivative-majorant phase established the derivative bounds

\[
|\partial_xH(x,y;t)|
\leq
L_x,
\]

and

\[
|\partial_yH(x,y;t)|
\leq
L_y
\]

on the compact domain \(U\).

The concrete compact-domain majorants prove that \(L_x\) and \(L_y\) are computable finite quantities whenever

\[
\Delta_Y>0
\]

and

\[
r>0.
\]

For any two points \((x,y),(x',y')\in U\), connect them by the two-segment path

\[
(x,y)\to(x',y)\to(x',y').
\]

Along the first segment, the mean-value estimate gives

\[
|H(x',y;t)-H(x,y;t)|
\leq
L_x|x'-x|.
\]

Along the second segment,

\[
|H(x',y';t)-H(x',y;t)|
\leq
L_y|y'-y|.
\]

By the triangle inequality,

\[
|H(x',y';t)-H(x,y;t)|
\leq
L_x|x'-x|+L_y|y'-y|.
\]

Since

\[
L_H(U,t)=L_x+L_y,
\]

we also have

\[
L_x|x'-x|+L_y|y'-y|
\leq
L_H(U,t)(|x'-x|+|y'-y|).
\]

Therefore,

\[
|H(x',y';t)-H(x,y;t)|
\leq
L_H(U,t)(|x'-x|+|y'-y|).
\]

\[
\square
\]

---

# Corollary 10AD.2 — Explicit \(H\)-kernel stability insertion

In every earlier support-stability theorem, the abstract Lipschitz constant

\[
L_t(U)
\]

may be replaced by the computable finite \(H\)-kernel constant

\[
L_H(U,t).
\]

Therefore, the combined-radius certificate becomes:

\[
\mathcal R_{\min}(L_H(U,t))<g_0(M(\Gamma,t)).
\]

If this holds, then

\[
n_-(M(\widetilde\Gamma,t))
=
n_-(M(\Gamma,t)).
\]

---

# 4. Why this is stronger

The project no longer relies only on an abstract Lipschitz constant.

It now has a concrete computable finite constant for the actual symbolic \(H\)-kernel model:

\[
L_H(U,t)=2|t|B_0M_x+2|t|(B_1M_0+B_0M_y).
\]

This specializes the stability framework to the finite Bombieri-style \(H\)-kernel.

---

# 5. Limitations

This theorem is finite-dimensional.

It depends on the compact-domain hypotheses.

It uses safe, possibly crude majorants.

It does not optimize the constants.

It does not prove anything about the infinite zeta limit.

It does not verify actual zeta zeros.

It does not prove RH.

It does not establish novelty.

---

# Boundary

This theorem does not prove RH.

This theorem does not falsify RH.

This theorem does not use zeta zeros.

This theorem does not verify the zeta case.

This theorem does not claim novelty.

Exact audit strings:

EXPLICIT_H_KERNEL_LIPSCHITZ_THEOREM

COMPUTABLE_H_KERNEL_LIPSCHITZ_CONSTANT

H_KERNEL_STABILITY_INSERTION

THEOREM_10AD_1

COROLLARY_10AD_2

