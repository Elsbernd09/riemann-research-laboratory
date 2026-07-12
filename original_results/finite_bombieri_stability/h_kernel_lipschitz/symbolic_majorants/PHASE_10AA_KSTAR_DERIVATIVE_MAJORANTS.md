# Phase 10AA — Symbolic Derivative Majorants for the \(K^*\)-Formula

## Purpose

Phase 10Z launched the explicit \(H\)-kernel Lipschitz branch.

Phase 10AA derives symbolic derivative majorants for the actual \(K^*\)-formula used in the finite Bombieri-style kernel.

This is still not the full final explicit theorem, but it is the first concrete symbolic step.

---

# 1. Kernel structure

Recall

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

The finite symbolic kernel has the form

\[
K^*(x,y;t)
=
K_t(x-y)
-
c_t\left(\frac12+iy\right)K_t(i/2-y)K_t(i/2+x)
-
c_t\left(\frac12-iy\right)K_t(i/2+y)K_t(i/2-x).
\]

The full kernel is

\[
H(x,y;t)
=
\frac{2t}{1/4+y^2}K^*(x,y;t).
\]

---

# 2. Majorant symbols

On a compact domain \(U\), define the following symbolic majorants.

For shifted \(K_t\)-arguments appearing in \(K^*\), let

\[
A_0(U,t)\geq \sup |K_t(z)|
\]

and

\[
A_1(U,t)\geq \sup |K_t'(z)|.
\]

For the rational factor, let

\[
B_0(U)\geq \sup_y \left|\frac{1}{1/4+y^2}\right|,
\]

and

\[
B_1(U)\geq \sup_y \left|\frac{d}{dy}\frac{1}{1/4+y^2}\right|.
\]

For the linear coefficients, let

\[
C_0(U)\geq
\sup_y
\max\left\{
\left|\frac12+iy\right|,
\left|\frac12-iy\right|
\right\}.
\]

Finally,

\[
|c_t|=\left|\frac{t}{\sinh t}\right|.
\]

---

# 3. Bound for \(K^*\)

Using the triangle inequality,

\[
|K^*(x,y;t)|
\leq
A_0+2|c_t|C_0A_0^2.
\]

Define

\[
M_0(U,t)
=
A_0+2|c_t|C_0A_0^2.
\]

Then

\[
|K^*(x,y;t)|\leq M_0(U,t).
\]

---

# 4. \(x\)-derivative majorant

Differentiate \(K^*\) with respect to \(x\).

The direct term gives

\[
\partial_xK_t(x-y)=K_t'(x-y).
\]

The product terms contribute one \(K_t'\)-factor in the \(x\)-shifted term.

Therefore,

\[
|\partial_xK^*(x,y;t)|
\leq
A_1+2|c_t|C_0A_0A_1.
\]

Define

\[
M_x(U,t)
=
A_1+2|c_t|C_0A_0A_1.
\]

Then

\[
|\partial_xK^*(x,y;t)|\leq M_x(U,t).
\]

---

# 5. \(y\)-derivative majorant

Differentiate \(K^*\) with respect to \(y\).

The direct term contributes

\[
|K_t'(x-y)|.
\]

Each product term contributes two types of pieces:

1. derivative of the linear coefficient \((1/2\pm iy)\);
2. derivative of the \(y\)-shifted \(K_t\)-factor.

Since

\[
\left|\frac{d}{dy}\left(\frac12\pm iy\right)\right|=1,
\]

each product term is bounded by

\[
|c_t|(A_0^2+C_0A_0A_1).
\]

There are two such product terms. Hence

\[
|\partial_yK^*(x,y;t)|
\leq
A_1+2|c_t|(A_0^2+C_0A_0A_1).
\]

Define

\[
M_y(U,t)
=
A_1+2|c_t|(A_0^2+C_0A_0A_1).
\]

Then

\[
|\partial_yK^*(x,y;t)|\leq M_y(U,t).
\]

---

# 6. Full \(H\)-kernel derivative majorants

Since

\[
H(x,y;t)=2tQ(y)K^*(x,y;t),
\]

where

\[
Q(y)=\frac{1}{1/4+y^2},
\]

we have

\[
\partial_xH(x,y;t)
=
2tQ(y)\partial_xK^*(x,y;t).
\]

Thus,

\[
|\partial_xH(x,y;t)|
\leq
2|t|B_0M_x.
\]

Define

\[
L_x(U,t)=2|t|B_0M_x.
\]

For the \(y\)-derivative,

\[
\partial_yH(x,y;t)
=
2tQ'(y)K^*(x,y;t)
+
2tQ(y)\partial_yK^*(x,y;t).
\]

Thus,

\[
|\partial_yH(x,y;t)|
\leq
2|t|(B_1M_0+B_0M_y).
\]

Define

\[
L_y(U,t)=2|t|(B_1M_0+B_0M_y).
\]

---

# 7. Symbolic Lipschitz candidate

The symbolic computable Lipschitz candidate is

\[
L_H(U,t)=L_x(U,t)+L_y(U,t).
\]

Therefore,

\[
L_H(U,t)
=
2|t|B_0M_x
+
2|t|(B_1M_0+B_0M_y).
\]

Substituting the definitions:

\[
M_0=A_0+2|c_t|C_0A_0^2,
\]

\[
M_x=A_1+2|c_t|C_0A_0A_1,
\]

\[
M_y=A_1+2|c_t|(A_0^2+C_0A_0A_1).
\]

This creates an explicit symbolic formula for the \(H\)-kernel Lipschitz candidate in terms of compact-domain majorants.

---

# 8. What remains

To complete the full theorem, the next phases must:

1. define a concrete compact domain model \(U\);
2. compute explicit \(A_0,A_1,B_0,B_1,C_0\);
3. prove these majorants really bound the required terms;
4. connect \(L_H(U,t)\) into the combined-radius stability certificate.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not use zeta zeros.

This phase does not verify the zeta case.

This phase does not claim novelty.

Exact audit strings:

KSTAR_DERIVATIVE_MAJORANTS

SYMBOLIC_H_KERNEL_LIPSCHITZ_CANDIDATE

COMPUTABLE_LIPSCHITZ_BOUND

NO_FULL_LIPSCHITZ_THEOREM_YET

