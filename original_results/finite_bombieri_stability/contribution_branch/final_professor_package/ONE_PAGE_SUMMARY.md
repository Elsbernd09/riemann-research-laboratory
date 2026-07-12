# One-Page Summary

## Project

A Conditional Finite-to-Infinite Transfer Framework for Certified Gram-Matrix Approximations in Weil/Bombieri-Style Models

## Main idea

The project studies when finite certified matrix computations can be connected to an infinite Weil/Bombieri-style quadratic form.

## Main conditional theorem

For a finite test class

\[
\mathcal F_R^{(m)}
=
\left\{
\sum_{j=1}^{m}a_j\phi_j:\|a\|_2\leq R
\right\},
\]

if each Gram-entry error decomposes as

\[
G^{(N)}_{ij}-G^{(\infty)}_{ij}
=
T_{ij}^{(N)}
+
P_{ij}^{(N)}
+
K_{ij}^{(N)}
+
C_{ij}^{(N)}
\]

and the four terms satisfy

\[
|T_{ij}^{(N)}|\leq\tau_N^{(m)},
\quad
|P_{ij}^{(N)}|\leq\pi_N^{(m)},
\quad
|K_{ij}^{(N)}|\leq\kappa_N^{(m)},
\quad
|C_{ij}^{(N)}|\leq\chi_N^{(m)},
\]

then

\[
\sup_{f\in\mathcal F_R^{(m)}}
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
R^2m
\left(
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\kappa_N^{(m)}
+
\chi_N^{(m)}
\right).
\]

## Implemented component

The project implements a transfer-certificate calculator and a prototype certified numerical interval framework for the computational error term.

## Honest status

Professor-review-worthy as a conditional framework.

Not an RH proof.

Not an RH breakthrough.

Not an established RH contribution.

Novelty not established.

