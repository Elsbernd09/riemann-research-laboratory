# Phase 10AR — Gram Convergence Problem

## Purpose

Phase 10AQ proved that uniform convergence on a finite test class reduces to Gram matrix convergence:

\[
\sup_{f\in\mathcal F_R^{(m)}}
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
R^2\|G^{(N)}-G^{(\infty)}\|_2.
\]

Phase 10AR defines the next exact problem:

\[
G^{(N)}_{ij}\to G^{(\infty)}_{ij}.
\]

This phase does not prove classical convergence.

This phase does not prove RH.

It isolates the next concrete mathematical target.

---

# 1. Finite test family

Let

\[
\Phi_m=\{\phi_1,\ldots,\phi_m\}
\subset
\mathcal D_W
\]

be a finite family of admissible test functions.

The finite test class is

\[
\mathcal F_R^{(m)}
=
\left\{
f=\sum_{j=1}^m a_j\phi_j:\|a\|_2\leq R
\right\}.
\]

---

# 2. Infinite Gram matrix

Let \(B_W\) be the Hermitian form associated with the infinite Weil/Bombieri quadratic form \(Q_W\).

Define

\[
G^{(\infty)}_{ij}
=
B_W(\phi_i,\phi_j).
\]

Then

\[
Q_W(f)=a^*G^{(\infty)}a.
\]

---

# 3. Finite Gram matrix

Let \(B_N^W\) be the finite Hermitian form represented by \(M_N^W\).

Let

\[
P_N^W:\mathcal D_W\to V_N^W
\]

be the approximation map.

Define

\[
G^{(N)}_{ij}
=
B_N^W(P_N^W\phi_i,P_N^W\phi_j).
\]

Then

\[
Q_N^W(P_N^Wf)=a^*G^{(N)}a.
\]

---

# 4. Gram convergence problem

The central finite-class convergence problem is:

\[
G^{(N)}_{ij}\to G^{(\infty)}_{ij}
\]

for every fixed pair

\[
1\leq i,j\leq m.
\]

A quantitative version is:

\[
|G^{(N)}_{ij}-G^{(\infty)}_{ij}|
\leq
\delta_N^{(m)}
\]

with

\[
\delta_N^{(m)}\to0.
\]

---

# 5. Theorem 10AR.1 — Gram convergence implies finite-class convergence

Assume that for a fixed finite test family \(\Phi_m\),

\[
\max_{1\leq i,j\leq m}
|G^{(N)}_{ij}-G^{(\infty)}_{ij}|
\leq
\delta_N^{(m)}.
\]

Then

\[
\sup_{f\in\mathcal F_R^{(m)}}
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
R^2m\delta_N^{(m)}.
\]

If

\[
\delta_N^{(m)}\to0,
\]

then

\[
Q_N^W(P_N^Wf)\to Q_W(f)
\]

uniformly for

\[
f\in\mathcal F_R^{(m)}.
\]

## Proof

This is exactly the entrywise Gram convergence certificate from Phase 10AQ.

Let

\[
\Delta_N^{(m)}=G^{(N)}-G^{(\infty)}.
\]

The entrywise bound gives

\[
\|\Delta_N^{(m)}\|_F
\leq
m\delta_N^{(m)}.
\]

Since

\[
\|\Delta_N^{(m)}\|_2
\leq
\|\Delta_N^{(m)}\|_F,
\]

we have

\[
\|\Delta_N^{(m)}\|_2
\leq
m\delta_N^{(m)}.
\]

For

\[
f=\sum_{j=1}^m a_j\phi_j
\]

with

\[
\|a\|_2\leq R,
\]

we get

\[
|Q_N^W(P_N^Wf)-Q_W(f)|
=
|a^*\Delta_N^{(m)}a|
\leq
\|\Delta_N^{(m)}\|_2\|a\|_2^2
\leq
R^2m\delta_N^{(m)}.
\]

Taking the supremum over \(\mathcal F_R^{(m)}\) gives the result.

\[
\square
\]

---

# 6. Decomposing the Gram error

The key object is

\[
G^{(N)}_{ij}-G^{(\infty)}_{ij}.
\]

This can be decomposed symbolically as:

\[
G^{(N)}_{ij}-G^{(\infty)}_{ij}
=
\text{finite truncation error}
+
\text{projection error}
+
\text{kernel/model error}
+
\text{numerical error}.
\]

More explicitly:

\[
G^{(N)}_{ij}-G^{(\infty)}_{ij}
=
T_{ij}^{(N)}
+
P_{ij}^{(N)}
+
K_{ij}^{(N)}
+
C_{ij}^{(N)}.
\]

Where:

1. \(T_{ij}^{(N)}\): truncation error from replacing the infinite form by a finite form;
2. \(P_{ij}^{(N)}\): projection error from \(P_N^W\);
3. \(K_{ij}^{(N)}\): kernel or model mismatch error;
4. \(C_{ij}^{(N)}\): computational or rounding error.

---

# 7. Theorem 10AR.2 — Error decomposition certificate

Assume that for all \(1\leq i,j\leq m\),

\[
|T_{ij}^{(N)}|\leq \tau_N^{(m)},
\]

\[
|P_{ij}^{(N)}|\leq \pi_N^{(m)},
\]

\[
|K_{ij}^{(N)}|\leq \kappa_N^{(m)},
\]

and

\[
|C_{ij}^{(N)}|\leq \chi_N^{(m)}.
\]

Then

\[
|G^{(N)}_{ij}-G^{(\infty)}_{ij}|
\leq
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\kappa_N^{(m)}
+
\chi_N^{(m)}.
\]

Therefore,

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

## Proof

Use the triangle inequality:

\[
|G^{(N)}_{ij}-G^{(\infty)}_{ij}|
\leq
|T_{ij}^{(N)}|
+
|P_{ij}^{(N)}|
+
|K_{ij}^{(N)}|
+
|C_{ij}^{(N)}|.
\]

Apply the assumed bounds and then apply Theorem 10AR.1.

\[
\square
\]

---

# 8. Contribution meaning

This phase creates a concrete route:

\[
\text{control individual Gram-entry errors}
\]

implies

\[
\text{uniform convergence on finite test classes}.
\]

This is not RH progress yet.

But it is a serious mathematical bridge target.

The next phase should identify which of the four error terms can be attacked first.

---

# 9. Next target

Phase 10AS should classify the four Gram error terms:

\[
T_{ij}^{(N)},\quad
P_{ij}^{(N)},\quad
K_{ij}^{(N)},\quad
C_{ij}^{(N)}.
\]

We should identify which are:

1. classical;
2. project-controlled;
3. numerical;
4. currently impossible without deeper theory.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not import the true Weil form.

This phase does not prove classical convergence.

This phase does not claim novelty.

Exact audit strings:

GRAM_CONVERGENCE_PROBLEM

GRAM_ENTRY_CONVERGENCE_TARGET

FINITE_CLASS_CONVERGENCE_FROM_GRAM_CONVERGENCE

GRAM_ERROR_DECOMPOSITION

TRUNCATION_PROJECTION_KERNEL_COMPUTATION_ERROR

CLASSICAL_CONVERGENCE_NOT_PROVEN

NOT_RH_CONTRIBUTION_YET

