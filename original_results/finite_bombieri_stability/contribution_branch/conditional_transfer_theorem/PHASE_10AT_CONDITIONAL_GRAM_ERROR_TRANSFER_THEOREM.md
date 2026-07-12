# Phase 10AT — Conditional Gram-Error Transfer Theorem

## Purpose

Phase 10AS classified the Gram-entry error decomposition:

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

Phase 10AT proves the conditional transfer theorem:

if all four error terms are explicitly bounded, then uniform convergence on finite test classes follows with an explicit bound.

This is not RH progress yet.

It is a conditional finite-to-infinite transfer theorem.

---

# 1. Setup

Let

\[
\Phi_m=\{\phi_1,\ldots,\phi_m\}
\subset
\mathcal D_W
\]

be a finite test family.

Let

\[
\mathcal F_R^{(m)}
=
\left\{
f=\sum_{j=1}^m a_j\phi_j:\|a\|_2\leq R
\right\}.
\]

Let

\[
G^{(\infty)}_{ij}=B_W(\phi_i,\phi_j)
\]

and

\[
G^{(N)}_{ij}=B_N^W(P_N^W\phi_i,P_N^W\phi_j).
\]

Define

\[
\Delta_N^{(m)}
=
G^{(N)}-G^{(\infty)}.
\]

---

# 2. Error decomposition

Assume that each Gram-entry error decomposes as

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

The terms mean:

1. \(T_{ij}^{(N)}\): truncation error;
2. \(P_{ij}^{(N)}\): projection error;
3. \(K_{ij}^{(N)}\): kernel/model error;
4. \(C_{ij}^{(N)}\): computational error.

---

# 3. Error bounds

Assume that for all

\[
1\leq i,j\leq m,
\]

we have

\[
|T_{ij}^{(N)}|\leq\tau_N^{(m)},
\]

\[
|P_{ij}^{(N)}|\leq\pi_N^{(m)},
\]

\[
|K_{ij}^{(N)}|\leq\kappa_N^{(m)},
\]

and

\[
|C_{ij}^{(N)}|\leq\chi_N^{(m)}.
\]

Define the total entrywise error bound

\[
\delta_N^{(m)}
=
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\kappa_N^{(m)}
+
\chi_N^{(m)}.
\]

---

# Theorem 10AT.1 — Conditional Gram-error transfer theorem

Under the setup above,

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

Equivalently,

\[
\sup_{f\in\mathcal F_R^{(m)}}
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
R^2m\delta_N^{(m)}.
\]

## Proof

For each entry,

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

By the triangle inequality,

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

Using the assumed bounds,

\[
|G^{(N)}_{ij}-G^{(\infty)}_{ij}|
\leq
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\kappa_N^{(m)}
+
\chi_N^{(m)}
=
\delta_N^{(m)}.
\]

Thus

\[
\max_{i,j}|G^{(N)}_{ij}-G^{(\infty)}_{ij}|
\leq
\delta_N^{(m)}.
\]

By the finite test-class Gram convergence theorem from Phase 10AR,

\[
\sup_{f\in\mathcal F_R^{(m)}}
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
R^2m\delta_N^{(m)}.
\]

Substituting the definition of \(\delta_N^{(m)}\) gives

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

\[
\square
\]

---

# Theorem 10AT.2 — Conditional convergence corollary

Assume the hypotheses of Theorem 10AT.1.

If

\[
\tau_N^{(m)}\to0,
\]

\[
\pi_N^{(m)}\to0,
\]

\[
\kappa_N^{(m)}\to0,
\]

and

\[
\chi_N^{(m)}\to0,
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

By Theorem 10AT.1,

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

If all four terms tend to zero, then the right-hand side tends to zero.

Thus convergence is uniform on \(\mathcal F_R^{(m)}\).

\[
\square
\]

---

# Theorem 10AT.3 — Conditional certified negative-direction transfer

Assume the hypotheses of Theorem 10AT.1.

Suppose there exists

\[
f\in\mathcal F_R^{(m)}
\]

such that

\[
Q_W(f)\leq-\eta
\]

for some \(\eta>0\).

If

\[
R^2m
\left(
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\kappa_N^{(m)}
+
\chi_N^{(m)}
\right)
<
\eta/2,
\]

then

\[
Q_N^W(P_N^Wf)<-\eta/2.
\]

## Proof

From Theorem 10AT.1,

\[
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

By the assumed margin,

\[
|Q_N^W(P_N^Wf)-Q_W(f)|
<
\eta/2.
\]

Since

\[
Q_W(f)\leq-\eta,
\]

we get

\[
Q_N^W(P_N^Wf)
<
-\eta+\eta/2
=
-\eta/2.
\]

\[
\square
\]

---

# 4. Why this matters

This theorem is conditional, but it is a real architecture result.

It says that the finite-to-infinite bridge can be reduced to four explicit error controls:

\[
\tau_N^{(m)},\quad
\pi_N^{(m)},\quad
\kappa_N^{(m)},\quad
\chi_N^{(m)}.
\]

So the project no longer has one vague missing convergence theorem.

It has four precise subproblems.

---

# 5. Contribution-track status

This is not a breakthrough.

This is not an RH contribution yet.

But it is a stronger contribution candidate than the earlier abstract templates because it gives a clean conditional theorem with explicit finite-class bounds.

The next serious step is to attack the only immediately project-controllable term:

\[
\chi_N^{(m)}.
\]

That means certified numerics.

---

# 6. Next target

Phase 10AU should define a certified numerical error model for

\[
C_{ij}^{(N)}.
\]

This should include:

1. interval arithmetic;
2. matrix assembly verification;
3. rounding-error certificates;
4. reproducible computation logs;
5. independent recalculation checks.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove unconditional classical convergence.

This phase does not import the true Weil form.

This phase does not claim novelty.

Exact audit strings:

CONDITIONAL_GRAM_ERROR_TRANSFER_THEOREM

CONDITIONAL_CONVERGENCE_COROLLARY

CONDITIONAL_CERTIFIED_NEGATIVE_DIRECTION_TRANSFER

FOUR_ERROR_CONTROL_REDUCTION

TRUNCATION_PROJECTION_KERNEL_COMPUTATION_BOUND

UNCONDITIONAL_CLASSICAL_CONVERGENCE_NOT_PROVEN

NOT_RH_CONTRIBUTION_YET

