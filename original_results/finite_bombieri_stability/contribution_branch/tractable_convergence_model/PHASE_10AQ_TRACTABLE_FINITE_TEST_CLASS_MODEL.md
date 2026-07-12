# Phase 10AQ — Tractable Finite Test-Class Convergence Model

## Purpose

Phase 10AP identified the major convergence target:

\[
\sup_{f\in\mathcal F}
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
\varepsilon_N(\mathcal F),
\qquad
\varepsilon_N(\mathcal F)\to0.
\]

Phase 10AQ chooses the first tractable version of this target: a finite-dimensional bounded test-class model.

This phase still does not prove RH.

This phase still does not prove the classical convergence theorem.

But it creates a realistic theorem target that can be attacked.

---

# 1. Finite test class

Let

\[
\mathcal F_R^{(m)}
\subset
\mathcal D_W
\]

be a finite-dimensional bounded test class.

Think of \(\mathcal F_R^{(m)}\) as test functions controlled by \(m\) coefficients:

\[
f=\sum_{j=1}^{m} a_j\phi_j,
\]

where

\[
\|a\|_2\leq R.
\]

Here:

- \(\phi_1,\ldots,\phi_m\) are admissible basis/test functions;
- \(a=(a_1,\ldots,a_m)\in\mathbb C^m\);
- \(R>0\) controls the size of the class.

---

# 2. Infinite Gram matrix

Define the infinite Weil/Bombieri Gram matrix on this finite test family by

\[
G^{(\infty)}_{ij}
=
B_W(\phi_i,\phi_j),
\]

where \(B_W\) is the Hermitian form associated to \(Q_W\).

Then for

\[
f=\sum_{j=1}^{m}a_j\phi_j,
\]

we have

\[
Q_W(f)=a^*G^{(\infty)}a.
\]

---

# 3. Finite Gram matrix

Define the finite approximating Gram matrix

\[
G^{(N)}_{ij}
=
B_N^W(P_N^W\phi_i,P_N^W\phi_j).
\]

Then

\[
Q_N^W(P_N^W f)=a^*G^{(N)}a.
\]

---

# 4. Matrix convergence reduces function convergence

For the finite class \(\mathcal F_R^{(m)}\), the convergence problem reduces to bounding

\[
|a^*(G^{(N)}-G^{(\infty)})a|.
\]

Let

\[
\Delta_N^{(m)}=G^{(N)}-G^{(\infty)}.
\]

Then

\[
|Q_N^W(P_N^W f)-Q_W(f)|
=
|a^*\Delta_N^{(m)}a|.
\]

Using the spectral norm,

\[
|a^*\Delta_N^{(m)}a|
\leq
\|\Delta_N^{(m)}\|_2\|a\|_2^2.
\]

Since

\[
\|a\|_2\leq R,
\]

we get

\[
|Q_N^W(P_N^W f)-Q_W(f)|
\leq
R^2\|\Delta_N^{(m)}\|_2.
\]

---

# Theorem 10AQ.1 — Finite test-class convergence reduction

Let

\[
\mathcal F_R^{(m)}
=
\left\{
\sum_{j=1}^{m}a_j\phi_j:\|a\|_2\leq R
\right\}.
\]

Assume \(G^{(\infty)}\) and \(G^{(N)}\) are the infinite and finite Gram matrices defined above.

Then

\[
\sup_{f\in\mathcal F_R^{(m)}}
|Q_N^W(P_N^W f)-Q_W(f)|
\leq
R^2\|G^{(N)}-G^{(\infty)}\|_2.
\]

## Proof

Let

\[
f=\sum_{j=1}^{m}a_j\phi_j
\]

with

\[
\|a\|_2\leq R.
\]

Then

\[
Q_W(f)=a^*G^{(\infty)}a
\]

and

\[
Q_N^W(P_N^Wf)=a^*G^{(N)}a.
\]

Therefore,

\[
|Q_N^W(P_N^Wf)-Q_W(f)|
=
|a^*(G^{(N)}-G^{(\infty)})a|.
\]

By the spectral norm bound,

\[
|a^*(G^{(N)}-G^{(\infty)})a|
\leq
\|G^{(N)}-G^{(\infty)}\|_2\|a\|_2^2.
\]

Since \(\|a\|_2\leq R\),

\[
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
R^2\|G^{(N)}-G^{(\infty)}\|_2.
\]

Taking the supremum over \(f\in\mathcal F_R^{(m)}\) gives the result.

\[
\square
\]

---

# 5. Entrywise version

If each entry satisfies

\[
|G^{(N)}_{ij}-G^{(\infty)}_{ij}|
\leq
\delta_N^{(m)},
\]

then

\[
\|G^{(N)}-G^{(\infty)}\|_2
\leq
m\delta_N^{(m)}.
\]

Therefore,

\[
\sup_{f\in\mathcal F_R^{(m)}}
|Q_N^W(P_N^W f)-Q_W(f)|
\leq
R^2m\delta_N^{(m)}.
\]

---

# Theorem 10AQ.2 — Entrywise finite test-class convergence certificate

Assume

\[
|G^{(N)}_{ij}-G^{(\infty)}_{ij}|
\leq
\delta_N^{(m)}
\]

for all

\[
1\leq i,j\leq m.
\]

Then

\[
\sup_{f\in\mathcal F_R^{(m)}}
|Q_N^W(P_N^W f)-Q_W(f)|
\leq
R^2m\delta_N^{(m)}.
\]

If

\[
\delta_N^{(m)}\to0
\]

for fixed \(m\), then

\[
Q_N^W(P_N^W f)\to Q_W(f)
\]

uniformly on \(\mathcal F_R^{(m)}\).

## Proof

The entrywise bound implies

\[
\|G^{(N)}-G^{(\infty)}\|_F
\leq
m\delta_N^{(m)}.
\]

Since

\[
\|A\|_2\leq \|A\|_F,
\]

we have

\[
\|G^{(N)}-G^{(\infty)}\|_2
\leq
m\delta_N^{(m)}.
\]

Apply Theorem 10AQ.1.

\[
\square
\]

---

# 6. Why this matters

This is the first genuinely tractable convergence reduction:

\[
\text{uniform convergence on finite test class}
\]

reduces to

\[
\text{finite Gram matrix convergence}.
\]

So instead of proving convergence for every test function at once, we can attack the matrix entries:

\[
G^{(N)}_{ij}\to G^{(\infty)}_{ij}.
\]

This is a serious simplification.

---

# 7. Contribution-track significance

If the classical Weil/Bombieri objects are imported and the Gram entries can be controlled, then this gives a clean contribution path:

\[
\text{entrywise Gram convergence}
\Rightarrow
\text{uniform finite-class convergence}
\Rightarrow
\text{certified finite negativity/positivity transfer}.
\]

This is still not RH progress yet.

But it is a more serious theorem architecture than the earlier abstract template.

---

# 8. Next target

Phase 10AR should define the finite Gram convergence problem:

\[
G^{(N)}_{ij}\to G^{(\infty)}_{ij}.
\]

The key will be to identify whether the finite \(H\)-kernel construction already gives those entries, or whether a different finite approximation is needed.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not import the true Weil form.

This phase does not prove classical convergence.

This phase does not claim novelty.

Exact audit strings:

TRACTABLE_FINITE_TEST_CLASS_MODEL

FINITE_TEST_CLASS_CONVERGENCE_REDUCTION

GRAM_MATRIX_CONVERGENCE_REDUCTION

ENTRYWISE_GRAM_CONVERGENCE_CERTIFICATE

UNIFORM_FINITE_CLASS_CONVERGENCE

CLASSICAL_CONVERGENCE_NOT_PROVEN

NOT_RH_CONTRIBUTION_YET

