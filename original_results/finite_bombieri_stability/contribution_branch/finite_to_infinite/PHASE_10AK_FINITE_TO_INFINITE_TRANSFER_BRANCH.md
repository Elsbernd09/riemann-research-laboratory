# Phase 10AK — Finite-to-Infinite Transfer Theorem Branch

## Purpose

The project currently has a real finite-dimensional result:

\[
\mathcal R_{\min}(L_H)<g_0(M(\Gamma,t))
\implies
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
\]

This is finite and certified.

But it is not yet an RH contribution.

The missing bridge is a theorem connecting finite certified matrix behavior to an infinite Weil/Bombieri-style positivity form.

Phase 10AK begins that bridge.

---

# 1. Main idea

Let \(\mathcal H\) be a complex Hilbert space or pre-Hilbert test-function space.

Let

\[
Q:\mathcal D\to\mathbb R
\]

be an infinite quadratic form on a dense domain \(\mathcal D\subset\mathcal H\).

Let

\[
Q_N:\mathcal D_N\to\mathbb R
\]

be finite-dimensional approximating quadratic forms.

The RH-relevant dream is:

\[
Q(f)\geq0\ \text{for all test functions }f
\]

is equivalent to RH or RH-like positivity.

The finite project can matter only if finite certificates tell us something rigorous about \(Q\).

---

# 2. Transfer problem

The central transfer question is:

When does certified finite positivity or certified finite negativity imply information about the infinite form?

There are two directions.

## Direction A — Positivity transfer

If finite forms are eventually nonnegative and converge to \(Q\), then can we prove

\[
Q(f)\geq0
\]

for all admissible \(f\)?

## Direction B — Negativity detection

If the infinite form has a negative direction,

\[
Q(f)<0,
\]

then must sufficiently accurate finite approximations eventually show a certified negative direction?

Direction B is especially important.

If RH fails and the Weil form has a negative test function, then a serious finite method should eventually detect certified finite negativity.

---

# 3. Theorem 10AK.1 — Abstract finite-to-infinite positivity transfer

Let \(\mathcal D\) be a test-function domain and \(Q:\mathcal D\to\mathbb R\) an infinite quadratic form.

Suppose there exist finite forms \(Q_N\) and approximation maps

\[
P_N:\mathcal D\to\mathcal D_N
\]

such that for every \(f\in\mathcal D\),

\[
Q_N(P_Nf)\to Q(f).
\]

If

\[
Q_N(g)\geq0
\]

for every \(g\in\mathcal D_N\) and every sufficiently large \(N\), then

\[
Q(f)\geq0
\]

for every \(f\in\mathcal D\).

## Proof

Fix \(f\in\mathcal D\).

By assumption,

\[
Q_N(P_Nf)\to Q(f).
\]

For all sufficiently large \(N\),

\[
Q_N(P_Nf)\geq0.
\]

The limit of nonnegative real numbers is nonnegative. Therefore,

\[
Q(f)\geq0.
\]

Since \(f\) was arbitrary,

\[
Q(f)\geq0
\]

for all \(f\in\mathcal D\).

\[
\square
\]

---

# 4. Theorem 10AK.2 — Negative direction detection under quantitative convergence

Let \(Q\), \(Q_N\), and \(P_N\) be as above.

Suppose \(f\in\mathcal D\) satisfies

\[
Q(f)\leq -\eta
\]

for some

\[
\eta>0.
\]

Suppose also that for all sufficiently large \(N\),

\[
|Q_N(P_Nf)-Q(f)|<\frac{\eta}{2}.
\]

Then for all sufficiently large \(N\),

\[
Q_N(P_Nf)<-\frac{\eta}{2}.
\]

## Proof

By the triangle inequality,

\[
Q_N(P_Nf)
\leq
Q(f)+|Q_N(P_Nf)-Q(f)|.
\]

Using the hypotheses,

\[
Q_N(P_Nf)
<
-\eta+\frac{\eta}{2}
=
-\frac{\eta}{2}.
\]

Thus the finite form detects a negative direction.

\[
\square
\]

---

# 5. Theorem 10AK.3 — Certified finite negativity from perturbation margin

Let \(Q_N\) be represented by a Hermitian matrix \(M_N\).

Suppose a computed finite approximation \(\widetilde M_N\) satisfies

\[
\|M_N-\widetilde M_N\|_2<\mu_N.
\]

If \(\widetilde M_N\) has a unit vector \(v_N\) with

\[
v_N^*\widetilde M_Nv_N<-\mu_N,
\]

then the exact finite form \(Q_N\) has a true negative direction:

\[
v_N^*M_Nv_N<0.
\]

## Proof

We have

\[
v_N^*M_Nv_N
=
v_N^*\widetilde M_Nv_N
+
v_N^*(M_N-\widetilde M_N)v_N.
\]

Since \(v_N\) is unit,

\[
|v_N^*(M_N-\widetilde M_N)v_N|
\leq
\|M_N-\widetilde M_N\|_2
<
\mu_N.
\]

Therefore,

\[
v_N^*M_Nv_N
<
-\mu_N+\mu_N
=
0.
\]

Thus \(Q_N\) has a true negative direction.

\[
\square
\]

---

# 6. Why this phase matters

This phase identifies the real RH-relevance bottleneck.

Finite computations matter only if we can prove:

1. finite forms approximate the infinite Weil/Bombieri form;
2. approximation errors are controlled;
3. finite certified negativity reflects true finite negativity;
4. true finite negativity transfers to the infinite setting or detects infinite negativity.

This is the first real bridge theorem layer.

It is still abstract.

It is not yet an RH contribution.

But it defines exactly what must be proven for the finite stability framework to become RH-relevant.

---

# 7. Contribution-track status

This phase contributes a clean abstract transfer framework:

\[
\text{infinite negativity}
\Rightarrow
\text{eventual finite negativity}
\Rightarrow
\text{certified finite detection}.
\]

The next serious target is to specialize \(Q\), \(Q_N\), and \(P_N\) to the Bombieri/Weil finite approximation setting.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not verify zeta zeros.

This phase does not claim novelty.

Exact audit strings:

FINITE_TO_INFINITE_TRANSFER_BRANCH

ABSTRACT_POSITIVITY_TRANSFER_THEOREM

NEGATIVE_DIRECTION_DETECTION_THEOREM

CERTIFIED_FINITE_NEGATIVITY_THEOREM

NOT_RH_CONTRIBUTION_YET

