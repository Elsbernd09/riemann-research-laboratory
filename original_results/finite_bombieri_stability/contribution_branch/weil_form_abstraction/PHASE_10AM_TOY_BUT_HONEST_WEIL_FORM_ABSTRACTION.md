# Phase 10AM — Toy-but-Honest Weil-Form Abstraction

## Purpose

Phase 10AL identified the missing bridge:

\[
Q_N(P_Nf)\to Q_W(f).
\]

Phase 10AM defines a toy-but-honest abstraction of the Weil/Bombieri form so we can study transfer without falsely claiming the full classical theorem.

This is not RH.

This is not a new RH criterion.

This is a safe model for finite-to-infinite reasoning.

---

# 1. Abstract test-function space

Let \(\mathcal D\) be a complex vector space of admissible test functions.

We do not yet specify the full classical test-function space.

Instead, we require only that \(\mathcal D\) supports:

1. finite-dimensional projections;
2. quadratic evaluation;
3. a limiting quadratic form;
4. approximation maps.

---

# 2. Infinite quadratic form

Let

\[
Q_\infty:\mathcal D\to\mathbb R
\]

be a Hermitian quadratic form.

That means there is a Hermitian sesquilinear form

\[
B_\infty:\mathcal D\times\mathcal D\to\mathbb C
\]

such that

\[
Q_\infty(f)=B_\infty(f,f).
\]

This is a toy abstraction of a Weil/Bombieri-style form.

It is not asserted to equal the classical zeta Weil form.

---

# 3. Finite approximating forms

Let

\[
V_N\cong\mathbb C^{d_N}
\]

be finite-dimensional spaces.

Let

\[
M_N\in\mathbb C^{d_N\times d_N}
\]

be Hermitian matrices.

Define

\[
Q_N(v)=v^*M_Nv.
\]

---

# 4. Approximation maps

Let

\[
P_N:\mathcal D\to V_N
\]

be approximation maps.

The finite-to-infinite bridge requires:

\[
Q_N(P_Nf)\to Q_\infty(f)
\]

for every fixed

\[
f\in\mathcal D.
\]

This is the central convergence condition.

---

# 5. Error model

Define the finite approximation error

\[
E_N(f)=Q_N(P_Nf)-Q_\infty(f).
\]

A quantitative convergence theorem would prove:

\[
|E_N(f)|\leq \varepsilon_N(f)
\]

with

\[
\varepsilon_N(f)\to0.
\]

This phase does not prove such a theorem.

It makes the required object explicit.

---

# Theorem 10AM.1 — Positivity transfer in the toy Weil-form abstraction

Assume:

1. \(Q_\infty:\mathcal D\to\mathbb R\) is a Hermitian quadratic form;
2. \(Q_N(v)=v^*M_Nv\) are finite Hermitian quadratic forms;
3. \(P_N:\mathcal D\to V_N\);
4. for every \(f\in\mathcal D\),

\[
Q_N(P_Nf)\to Q_\infty(f);
\]

5. for all sufficiently large \(N\), \(Q_N(v)\geq0\) for every \(v\in V_N\).

Then

\[
Q_\infty(f)\geq0
\]

for every \(f\in\mathcal D\).

## Proof

Fix \(f\in\mathcal D\).

By convergence,

\[
Q_N(P_Nf)\to Q_\infty(f).
\]

For all sufficiently large \(N\),

\[
Q_N(P_Nf)\geq0.
\]

Therefore the limit is nonnegative:

\[
Q_\infty(f)\geq0.
\]

\[
\square
\]

---

# Theorem 10AM.2 — Quantitative negative-direction transfer

Assume:

1. \(Q_\infty(f)\leq-\eta\) for some \(f\in\mathcal D\) and \(\eta>0\);
2. the approximation error satisfies

\[
|E_N(f)|<\eta/2
\]

for all sufficiently large \(N\).

Then

\[
Q_N(P_Nf)<-\eta/2
\]

for all sufficiently large \(N\).

## Proof

Since

\[
Q_N(P_Nf)=Q_\infty(f)+E_N(f),
\]

we have

\[
Q_N(P_Nf)
\leq
-\eta+|E_N(f)|
<
-\eta+\eta/2
=
-\eta/2.
\]

\[
\square
\]

---

# Theorem 10AM.3 — Certified computed negativity in the toy abstraction

Let \(\widetilde M_N\) be a computed approximation to \(M_N\).

Assume

\[
\|M_N-\widetilde M_N\|_2<\mu_N.
\]

If a unit vector \(v_N\in V_N\) satisfies

\[
v_N^*\widetilde M_Nv_N<-\mu_N,
\]

then

\[
v_N^*M_Nv_N<0.
\]

## Proof

Since \(v_N\) is unit,

\[
|v_N^*(M_N-\widetilde M_N)v_N|
\leq
\|M_N-\widetilde M_N\|_2
<
\mu_N.
\]

Thus

\[
v_N^*M_Nv_N
<
-\mu_N+\mu_N
=
0.
\]

\[
\square
\]

---

# 6. Import obligations from classical theory

To turn this toy abstraction into a genuine Bombieri/Weil contribution, the following must be imported or proven from classical theory:

1. the correct \(\mathcal D\);
2. the true \(Q_W\);
3. the exact relation between \(Q_W\) and RH;
4. the correct finite subspaces \(V_N\);
5. the correct finite matrices \(M_N\);
6. the correct approximation maps \(P_N\);
7. convergence \(Q_N(P_Nf)\to Q_W(f)\);
8. quantitative bounds \(\varepsilon_N(f)\).

Without these, the abstraction remains useful but not RH-conclusive.

---

# 7. Contribution-track meaning

This phase is valuable because it separates:

\[
\text{finite certified computation}
\]

from

\[
\text{infinite RH-relevant positivity}.
\]

It gives a safe theorem template for future work.

But it is not yet an RH contribution.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not verify zeta zeros.

This phase does not claim novelty.

Exact audit strings:

TOY_BUT_HONEST_WEIL_FORM_ABSTRACTION

ABSTRACT_WEIL_FORM_MODEL

POSITIVITY_TRANSFER_IN_TOY_MODEL

QUANTITATIVE_NEGATIVE_DIRECTION_TRANSFER

CLASSICAL_THEORY_IMPORT_OBLIGATIONS

NOT_RH_CONTRIBUTION_YET

