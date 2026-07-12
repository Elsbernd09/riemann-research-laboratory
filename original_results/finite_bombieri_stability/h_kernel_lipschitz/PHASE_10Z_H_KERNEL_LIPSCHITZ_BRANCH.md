# Phase 10Z — Explicit H-Kernel Lipschitz Branch

## Purpose

Earlier phases proved support-stability certificates assuming an abstract local Lipschitz constant

\[
L_t(U).
\]

Phase 10Z begins the explicit \(H\)-kernel Lipschitz branch.

The goal is to replace the abstract assumption

\[
L_t(U)
\]

with a computable bound for the Bombieri-style finite kernel.

This is a stronger direction because it specializes the stability framework to the actual finite matrix object.

---

# 1. Kernel recalled

The symbolic Bombieri-style finite kernel branch used

\[
K(x)=\frac{\sin x}{x}
\]

with the removable value

\[
K(0)=1.
\]

For \(t>0\),

\[
K_t(x)=K(tx)=\frac{\sin(tx)}{tx}.
\]

The finite kernel has the schematic form

\[
H(x,y;t)=\frac{2t}{1/4+y^2}K^*(x,y;t),
\]

where \(K^*(x,y;t)\) is built from finite sums and products of shifted \(K_t\)-terms.

---

# 2. Lipschitz strategy

To prove an explicit Lipschitz bound on a compact set \(U\subset\mathbb C^2\), it is enough to bound the partial derivatives:

\[
\left|\frac{\partial H}{\partial x}(x,y;t)\right|
\leq
L_x(U,t),
\]

and

\[
\left|\frac{\partial H}{\partial y}(x,y;t)\right|
\leq
L_y(U,t).
\]

Then

\[
|H(x',y';t)-H(x,y;t)|
\leq
(L_x(U,t)+L_y(U,t))(|x'-x|+|y'-y|)
\]

or, more sharply,

\[
|H(x',y';t)-H(x,y;t)|
\leq
L_x(U,t)|x'-x|+L_y(U,t)|y'-y|.
\]

The project will use the computable certificate

\[
L_H(U,t)=L_x(U,t)+L_y(U,t).
\]

---

# 3. Derivative of \(K_t\)

For

\[
K_t(z)=\frac{\sin(tz)}{tz},
\]

the derivative is

\[
K_t'(z)=
\frac{tz\cos(tz)-\sin(tz)}{tz^2}.
\]

Equivalently,

\[
K_t'(z)
=
t\frac{(tz)\cos(tz)-\sin(tz)}{(tz)^2}.
\]

At \(z=0\), the removable value is

\[
K_t'(0)=0.
\]

---

# 4. Compact-domain majorants

On a bounded compact domain avoiding poles of

\[
\frac{1}{1/4+y^2},
\]

the functions \(K_t\), \(K_t'\), and the rational factor are bounded.

Define symbolic majorants:

\[
A_0(U,t)\geq \sup_{z\in Z(U)} |K_t(z)|,
\]

\[
A_1(U,t)\geq \sup_{z\in Z(U)} |K_t'(z)|,
\]

\[
B_0(U)\geq \sup_{y\in Y(U)}\left|\frac{1}{1/4+y^2}\right|,
\]

\[
B_1(U)\geq \sup_{y\in Y(U)}\left|\frac{d}{dy}\frac{1}{1/4+y^2}\right|.
\]

Then partial derivative bounds for \(H\) can be expressed in terms of \(A_0,A_1,B_0,B_1,t\), and the finite algebraic structure of \(K^*\).

---

# 5. Main target theorem for this branch

The branch aims to prove:

## Target Theorem 10Z+

For a compact domain \(U\subset\mathbb C^2\) avoiding the poles \(y=\pm i/2\), there exists a computable finite expression

\[
L_H(U,t)
\]

such that for all \((x,y),(x',y')\in U\),

\[
|H(x',y';t)-H(x,y;t)|
\leq
L_H(U,t)(|x'-x|+|y'-y|).
\]

This will convert the earlier abstract certificate into an explicit \(H\)-kernel certificate:

\[
\mathcal R_{\min}(L_H(U,t))<g_0(M(\Gamma,t)).
\]

---

# 6. What Phase 10Z does and does not prove

Phase 10Z starts the explicit branch.

It locks the derivative strategy and majorant structure.

It does not yet complete the full explicit \(H\)-kernel Lipschitz theorem.

The next phase must compute and audit symbolic derivative bounds for the actual \(K^*\)-formula.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not use zeta zeros.

This phase does not verify the zeta case.

This phase does not claim novelty.

Exact audit strings:

H_KERNEL_LIPSCHITZ_BRANCH

EXPLICIT_H_KERNEL_LIPSCHITZ_TARGET

COMPUTABLE_LIPSCHITZ_BOUND

NO_FULL_LIPSCHITZ_THEOREM_YET

