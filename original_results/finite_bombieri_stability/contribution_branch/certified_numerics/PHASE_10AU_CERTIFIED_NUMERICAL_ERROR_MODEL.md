# Phase 10AU — Certified Numerical Error Model

## Purpose

Phase 10AT proved the conditional transfer theorem using four error terms:

\[
T_{ij}^{(N)},\quad P_{ij}^{(N)},\quad K_{ij}^{(N)},\quad C_{ij}^{(N)}.
\]

Phase 10AU attacks the first project-controllable term:

\[
C_{ij}^{(N)}.
\]

This term represents computational error.

The goal is to create a rigorous numerical certification model proving a bound of the form

\[
|C_{ij}^{(N)}|\leq \chi_N^{(m)}.
\]

This does not prove RH.

This does not prove classical convergence.

But it is a serious project-controllable component of the larger transfer framework.

---

# 1. Computational error term

Recall the Gram-entry decomposition:

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

The computational error term is

\[
C_{ij}^{(N)}.
\]

It measures the difference between the exact finite entry and the computed finite entry.

Let

\[
G^{(N),exact}_{ij}
\]

be the exact finite Gram entry and

\[
\widetilde G^{(N)}_{ij}
\]

be the computed entry.

Then define

\[
C_{ij}^{(N)}
=
\widetilde G^{(N)}_{ij}-G^{(N),exact}_{ij}.
\]

The goal is to certify

\[
|C_{ij}^{(N)}|\leq \chi_N^{(m)}.
\]

---

# 2. Certified interval model

For each computed entry, instead of storing only a floating-point value, store an interval

\[
I_{ij}^{(N)}=[\ell_{ij}^{(N)},u_{ij}^{(N)}]
\]

such that

\[
G^{(N),exact}_{ij}\in I_{ij}^{(N)}.
\]

Let the computed midpoint be

\[
\widetilde G^{(N)}_{ij}
=
\frac{\ell_{ij}^{(N)}+u_{ij}^{(N)}}{2}.
\]

Let the interval radius be

\[
r_{ij}^{(N)}
=
\frac{u_{ij}^{(N)}-\ell_{ij}^{(N)}}{2}.
\]

Then

\[
|\widetilde G^{(N)}_{ij}-G^{(N),exact}_{ij}|
\leq r_{ij}^{(N)}.
\]

---

# 3. Global numerical error bound

Define

\[
\chi_N^{(m)}
=
\max_{1\leq i,j\leq m} r_{ij}^{(N)}.
\]

Then for all entries,

\[
|C_{ij}^{(N)}|
\leq
\chi_N^{(m)}.
\]

This is the certified numerical error bound.

---

# Theorem 10AU.1 — Interval certified computational error bound

Assume that for every \(1\leq i,j\leq m\), the exact finite Gram entry satisfies

\[
G^{(N),exact}_{ij}\in
[\ell_{ij}^{(N)},u_{ij}^{(N)}].
\]

Let

\[
\widetilde G^{(N)}_{ij}
=
\frac{\ell_{ij}^{(N)}+u_{ij}^{(N)}}{2}
\]

and

\[
r_{ij}^{(N)}
=
\frac{u_{ij}^{(N)}-\ell_{ij}^{(N)}}{2}.
\]

Define

\[
\chi_N^{(m)}
=
\max_{i,j}r_{ij}^{(N)}.
\]

Then

\[
|C_{ij}^{(N)}|
=
|\widetilde G^{(N)}_{ij}-G^{(N),exact}_{ij}|
\leq
\chi_N^{(m)}
\]

for all \(i,j\).

## Proof

Since

\[
G^{(N),exact}_{ij}\in
[\ell_{ij}^{(N)},u_{ij}^{(N)}],
\]

and

\[
\widetilde G^{(N)}_{ij}
\]

is the midpoint of this interval, the distance from the midpoint to any point in the interval is at most the radius

\[
r_{ij}^{(N)}.
\]

Thus

\[
|\widetilde G^{(N)}_{ij}-G^{(N),exact}_{ij}|
\leq
r_{ij}^{(N)}
\leq
\chi_N^{(m)}.
\]

\[
\square
\]

---

# 4. Matrix-level numerical error bound

Let

\[
\widetilde G^{(N)}
\]

be the computed Gram matrix and

\[
G^{(N),exact}
\]

the exact finite Gram matrix.

Define the numerical error matrix

\[
E_C^{(N)}
=
\widetilde G^{(N)}-G^{(N),exact}.
\]

If

\[
|E_{C,ij}^{(N)}|\leq \chi_N^{(m)}
\]

for all \(i,j\), then

\[
\|E_C^{(N)}\|_2
\leq
m\chi_N^{(m)}.
\]

---

# Theorem 10AU.2 — Matrix-level certified numerical error bound

If

\[
|C_{ij}^{(N)}|\leq \chi_N^{(m)}
\]

for all \(1\leq i,j\leq m\), then

\[
\|\widetilde G^{(N)}-G^{(N),exact}\|_2
\leq
m\chi_N^{(m)}.
\]

## Proof

The Frobenius norm satisfies

\[
\|E_C^{(N)}\|_F
=
\left(
\sum_{i,j}|E_{C,ij}^{(N)}|^2
\right)^{1/2}
\leq
\left(m^2(\chi_N^{(m)})^2\right)^{1/2}
=
m\chi_N^{(m)}.
\]

Since

\[
\|E_C^{(N)}\|_2\leq \|E_C^{(N)}\|_F,
\]

the result follows.

\[
\square
\]

---

# 5. Certified numerical workflow

A computation is certified only if it records:

1. exact formula used;
2. arithmetic precision;
3. rounding mode or interval enclosure rule;
4. interval lower bound \(\ell_{ij}^{(N)}\);
5. interval upper bound \(u_{ij}^{(N)}\);
6. midpoint \(\widetilde G^{(N)}_{ij}\);
7. radius \(r_{ij}^{(N)}\);
8. global bound \(\chi_N^{(m)}\);
9. reproducible script hash or commit hash.

Without these, the computation is not certified.

---

# 6. Certified numerics contribution

This phase controls one of the four error terms in the conditional transfer theorem:

\[
C_{ij}^{(N)}.
\]

The project still needs:

\[
T_{ij}^{(N)},\quad P_{ij}^{(N)},\quad K_{ij}^{(N)}
\]

to be controlled before classical convergence follows.

But now the computational term has a rigorous certification path.

---

# 7. Next target

Phase 10AV should implement a certified interval Gram-entry calculator prototype.

It should not claim to compute true classical \(G^{(N)}\) yet.

It should implement the certification structure:

\[
[\ell,u],\quad midpoint,\quad radius,\quad \chi_N^{(m)}.
\]

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove classical convergence.

This phase does not import the true Weil form.

This phase does not claim novelty.

Exact audit strings:

CERTIFIED_NUMERICAL_ERROR_MODEL

INTERVAL_CERTIFIED_COMPUTATIONAL_ERROR_BOUND

MATRIX_LEVEL_NUMERICAL_ERROR_BOUND

CHI_N_M_NUMERICAL_ERROR_CERTIFICATE

COMPUTATIONAL_ERROR_CONTROLLED_CONDITIONALLY

CERTIFIED_NUMERICS_WORKFLOW

NOT_RH_CONTRIBUTION_YET

