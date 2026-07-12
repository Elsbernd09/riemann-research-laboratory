# Phase 10AC — \(L_H(U,t)\) Constant Calculator

## Purpose

Phase 10AB defined concrete compact-domain majorants.

Phase 10AC implements a calculator for the symbolic \(H\)-kernel Lipschitz candidate:

\[
L_H(U,t)=L_x(U,t)+L_y(U,t).
\]

---

# 1. Inputs

The calculator receives compact-domain parameters:

\[
R,S,R_y,S_y,\Delta_Y,r,t.
\]

Here:

\[
\Delta_Y
\]

is the lower bound for

\[
|1/4+y^2|
\]

on the chosen \(y\)-domain, and \(r>0\) is the Cauchy buffer radius.

---

# 2. Computed constants

The calculator computes:

\[
A_0=e^{|t|S},
\]

\[
A_1=\frac{\exp(|t|(S+r))}{r},
\]

\[
B_0=\frac1{\Delta_Y},
\]

\[
B_1=\frac{2\rho_y}{\Delta_Y^2},
\]

\[
C_0=\frac12+\rho_y,
\]

where

\[
\rho_y=\sqrt{R_y^2+S_y^2}.
\]

It then computes:

\[
M_0=A_0+2|c_t|C_0A_0^2,
\]

\[
M_x=A_1+2|c_t|C_0A_0A_1,
\]

\[
M_y=A_1+2|c_t|(A_0^2+C_0A_0A_1).
\]

Finally:

\[
L_x=2|t|B_0M_x,
\]

\[
L_y=2|t|(B_1M_0+B_0M_y),
\]

and

\[
L_H=L_x+L_y.
\]

---

# 3. Status

This phase implements the calculator.

It does not yet complete the final explicit \(H\)-kernel Lipschitz theorem.

The next phase must state and prove the theorem connecting this computed \(L_H\) into the combined-radius certificate.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not use zeta zeros.

This phase does not verify the zeta case.

This phase does not claim novelty.

Exact audit strings:

LH_CONSTANT_CALCULATOR

COMPUTABLE_H_KERNEL_LIPSCHITZ_CONSTANT

CONCRETE_COMPACT_DOMAIN_MAJORANTS

NO_FULL_LIPSCHITZ_THEOREM_YET

