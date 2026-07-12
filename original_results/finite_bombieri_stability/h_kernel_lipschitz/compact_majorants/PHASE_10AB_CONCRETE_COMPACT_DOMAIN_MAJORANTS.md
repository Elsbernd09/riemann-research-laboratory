# Phase 10AB — Concrete Compact-Domain Majorants

## Purpose

Phase 10AA derived symbolic majorants

\[
A_0,A_1,B_0,B_1,C_0
\]

for the \(H\)-kernel Lipschitz branch.

Phase 10AB defines concrete computable majorants on compact rectangular complex domains.

This moves the project from symbolic placeholders toward a fully explicit \(H\)-kernel Lipschitz certificate.

---

# 1. Compact box domain

Let the relevant shifted \(K_t\)-arguments lie in the complex box

\[
Z(R,S)=\{z\in\mathbb C: |\Re z|\leq R,\ |\Im z|\leq S\}.
\]

Let the \(y\)-variable lie in

\[
Y(R_y,S_y)=\{y\in\mathbb C: |\Re y|\leq R_y,\ |\Im y|\leq S_y\}.
\]

Assume the rational denominator stays away from zero:

\[
\Delta_Y
=
\inf_{y\in Y(R_y,S_y)} |1/4+y^2|
>
0.
\]

---

# 2. Majorant for \(K_t\)

Recall

\[
K_t(z)=\frac{\sin(tz)}{tz}.
\]

Using

\[
|\sin w|\leq e^{|\Im w|}
\]

and the removable value at \(z=0\), we use the safe compact-domain majorant

\[
A_0(R,S,t)=e^{|t|S}.
\]

This is crude but computable and valid as a safe upper bound for \(|K_t|\) on compact shifted domains when the removable value is included.

---

# 3. Majorant for \(K_t'\)

Using the power series

\[
K_t(z)=\sum_{n=0}^{\infty}(-1)^n\frac{(tz)^{2n}}{(2n+1)!},
\]

we have

\[
K_t'(z)=
t
\sum_{n=1}^{\infty}
(-1)^n
\frac{2n(tz)^{2n-1}}{(2n+1)!}.
\]

On \(|z|\leq \rho\), where

\[
\rho=\sqrt{R^2+S^2},
\]

a safe derivative majorant is

\[
A_1(R,S,t)
=
|t|
\sum_{n=1}^{\infty}
\frac{2n(|t|\rho)^{2n-1}}{(2n+1)!}.
\]

For implementation, this can be evaluated by truncation with a positive tail bound.

For a simpler closed-form safe majorant, use the Cauchy estimate on a radius buffer \(r>0\):

\[
A_1(R,S,t;r)
\leq
\frac{\exp(|t|(S+r))}{r}.
\]

This phase locks the Cauchy-style computable bound:

\[
A_1=\frac{\exp(|t|(S+r))}{r}.
\]

---

# 4. Rational factor majorants

For

\[
Q(y)=\frac{1}{1/4+y^2},
\]

define

\[
\Delta_Y
=
\inf_{y\in Y(R_y,S_y)} |1/4+y^2|.
\]

If

\[
\Delta_Y>0,
\]

then

\[
B_0=\frac{1}{\Delta_Y}.
\]

Since

\[
Q'(y)=\frac{-2y}{(1/4+y^2)^2},
\]

and

\[
|y|\leq \rho_y=\sqrt{R_y^2+S_y^2},
\]

we may take

\[
B_1=\frac{2\rho_y}{\Delta_Y^2}.
\]

---

# 5. Linear coefficient majorant

For

\[
\frac12\pm iy,
\]

we have

\[
\left|\frac12\pm iy\right|
\leq
\frac12+|y|.
\]

Thus

\[
C_0=\frac12+\rho_y.
\]

---

# 6. Computable majorant package

The concrete package is:

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

Together with

\[
c_t=\frac{t}{\sinh t},
\]

these feed the Phase 10AA formulas:

\[
M_0=A_0+2|c_t|C_0A_0^2,
\]

\[
M_x=A_1+2|c_t|C_0A_0A_1,
\]

\[
M_y=A_1+2|c_t|(A_0^2+C_0A_0A_1),
\]

and

\[
L_H(U,t)=2|t|B_0M_x+2|t|(B_1M_0+B_0M_y).
\]

---

# 7. What remains

This phase defines computable majorants but does not yet prove the final explicit \(H\)-kernel Lipschitz theorem.

The next phase should implement a calculator for these constants and test it on synthetic compact boxes.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not use zeta zeros.

This phase does not verify the zeta case.

This phase does not claim novelty.

Exact audit strings:

CONCRETE_COMPACT_DOMAIN_MAJORANTS

A0_EXP_MAJORANT

A1_CAUCHY_MAJORANT

RATIONAL_FACTOR_MAJORANTS

COMPUTABLE_H_KERNEL_MAJORANT_PACKAGE

NO_FULL_LIPSCHITZ_THEOREM_YET

