# Phase 12L — Truncation Error Gate

## Purpose

Phase 12K eliminated projection error on a chosen finite test class by taking the finite projection to be exact on that class.

The remaining main wall is truncation error:

\[
\tau_Y(R,m).
\]

Phase 12L defines a spectral truncation and proves a conditional finite-class tail bound.

---

# 1. Provisional infinite spectral form

From Phase 12G, the provisional infinite form is

\[
Q_W(g)
=
\sum_\rho
\widehat g(\rho)
\overline{\widehat g(1-\bar\rho)}.
\]

The sum runs over nontrivial zeros \(\rho\) of \(\zeta(s)\).

This remains provisional pending primary-source confirmation of conventions.

---

# 2. Spectral truncation

For a height cutoff \(Y>0\), define the finite spectral truncation

\[
Q_Y(g)
=
\sum_{|\operatorname{Im}\rho|\le Y}
\widehat g(\rho)
\overline{\widehat g(1-\bar\rho)}.
\]

Define the tail error

\[
T_Y(g)=Q_W(g)-Q_Y(g).
\]

Thus,

\[
T_Y(g)
=
\sum_{|\operatorname{Im}\rho|>Y}
\widehat g(\rho)
\overline{\widehat g(1-\bar\rho)}.
\]

The truncation problem is to prove

\[
|T_Y(g)|\to0
\]

as

\[
Y\to\infty.
\]

---

# 3. Finite test class

Let

\[
\mathcal F_R^{(m)}
=
\left\{
g=\sum_{j=1}^{m}a_j\phi_j:\|a\|_2\le R
\right\}.
\]

For each pair \(i,j\), define the tail Gram entry

\[
\mathcal R_{ij}(Y)
=
\sum_{|\operatorname{Im}\rho|>Y}
\widehat{\phi_i}(\rho)
\overline{\widehat{\phi_j}(1-\bar\rho)}.
\]

Then for

\[
g=\sum_{j=1}^{m}a_j\phi_j,
\]

the tail error becomes

\[
T_Y(g)
=
a^*\mathcal R(Y)a
\]

up to the convention of indexing the coefficient vector.

---

# Theorem 12L.1 — Finite-class truncation bound from tail Gram matrix

Assume the tail Gram matrix

\[
\mathcal R(Y)=(\mathcal R_{ij}(Y))_{i,j=1}^{m}
\]

is well-defined.

Then for every

\[
g\in\mathcal F_R^{(m)},
\]

\[
|T_Y(g)|
\le
R^2\|\mathcal R(Y)\|_2.
\]

## Proof

Write

\[
g=\sum_{j=1}^{m}a_j\phi_j
\]

with

\[
\|a\|_2\le R.
\]

By bilinearity of the spectral tail expression,

\[
T_Y(g)=a^*\mathcal R(Y)a.
\]

Therefore,

\[
|T_Y(g)|
=
|a^*\mathcal R(Y)a|
\le
\|a\|_2^2\|\mathcal R(Y)\|_2.
\]

Since

\[
\|a\|_2\le R,
\]

we get

\[
|T_Y(g)|
\le
R^2\|\mathcal R(Y)\|_2.
\]

\[
\square
\]

---

# Corollary 12L.2 — Entrywise truncation bound

If

\[
|\mathcal R_{ij}(Y)|\le \delta_Y^{(m)}
\]

for all

\[
1\le i,j\le m,
\]

then

\[
\sup_{g\in\mathcal F_R^{(m)}}|T_Y(g)|
\le
R^2m\delta_Y^{(m)}.
\]

## Proof

If every entry satisfies

\[
|\mathcal R_{ij}(Y)|\le\delta_Y^{(m)},
\]

then

\[
\|\mathcal R(Y)\|_2
\le
\|\mathcal R(Y)\|_F
\le
m\delta_Y^{(m)}.
\]

Apply Theorem 12L.1.

\[
\square
\]

---

# 4. Shell tail strategy

To bound \(\delta_Y^{(m)}\), divide the zero tail into height shells:

\[
k<|\operatorname{Im}\rho|\le k+1.
\]

Let

\[
Z(k)
\]

be an upper bound for the number of zeros in the shell

\[
k<|\operatorname{Im}\rho|\le k+1.
\]

Let

\[
A_{ij}(k)
\]

be an upper bound for

\[
\left|
\widehat{\phi_i}(\rho)
\overline{\widehat{\phi_j}(1-\bar\rho)}
\right|
\]

for zeros in that shell.

Then

\[
|\mathcal R_{ij}(Y)|
\le
\sum_{k>\lfloor Y\rfloor} Z(k)A_{ij}(k).
\]

---

# Theorem 12L.3 — Shell-count truncation bound

Assume that for every shell

\[
k<|\operatorname{Im}\rho|\le k+1,
\]

there are at most \(Z(k)\) zeros, and assume

\[
\left|
\widehat{\phi_i}(\rho)
\overline{\widehat{\phi_j}(1-\bar\rho)}
\right|
\le A_{ij}(k)
\]

for every zero in that shell.

Then

\[
|\mathcal R_{ij}(Y)|
\le
\sum_{k>\lfloor Y\rfloor}Z(k)A_{ij}(k).
\]

Therefore, if

\[
\delta_Y^{(m)}
=
\max_{1\le i,j\le m}
\sum_{k>\lfloor Y\rfloor}Z(k)A_{ij}(k),
\]

then

\[
\sup_{g\in\mathcal F_R^{(m)}}|T_Y(g)|
\le
R^2m\delta_Y^{(m)}.
\]

## Proof

For fixed \(i,j\),

\[
\mathcal R_{ij}(Y)
=
\sum_{|\operatorname{Im}\rho|>Y}
\widehat{\phi_i}(\rho)
\overline{\widehat{\phi_j}(1-\bar\rho)}.
\]

Partition the zeros into shells. In shell \(k\), there are at most \(Z(k)\) zeros, and each term has absolute value at most \(A_{ij}(k)\). Hence the total contribution of shell \(k\) is at most

\[
Z(k)A_{ij}(k).
\]

Summing over shells gives

\[
|\mathcal R_{ij}(Y)|
\le
\sum_{k>\lfloor Y\rfloor}Z(k)A_{ij}(k).
\]

The finite-class bound follows from Corollary 12L.2.

\[
\square
\]

---

# 5. Vanishing truncation criterion

If

\[
\delta_Y^{(m)}\to0,
\]

then

\[
\sup_{g\in\mathcal F_R^{(m)}}|T_Y(g)|\to0.
\]

This is the desired truncation convergence on the finite test class.

---

# Corollary 12L.4 — Truncation convergence criterion

If

\[
\delta_Y^{(m)}\to0
\]

as

\[
Y\to\infty,
\]

then

\[
\sup_{g\in\mathcal F_R^{(m)}}|Q_W(g)-Q_Y(g)|
\to0.
\]

## Proof

By Theorem 12L.3,

\[
\sup_{g\in\mathcal F_R^{(m)}}|Q_W(g)-Q_Y(g)|
=
\sup_{g\in\mathcal F_R^{(m)}}|T_Y(g)|
\le
R^2m\delta_Y^{(m)}.
\]

If

\[
\delta_Y^{(m)}\to0,
\]

then

\[
R^2m\delta_Y^{(m)}\to0.
\]

\[
\square
\]

---

# 6. Concrete sufficient decay condition

A standard sufficient shape is:

\[
Z(k)\le C(1+\log(k+2))
\]

and

\[
A_{ij}(k)\le C_{ij,A}(1+k)^{-A}
\]

for some

\[
A>2.
\]

Then

\[
\sum_{k>Y}Z(k)A_{ij}(k)
\le
C C_{ij,A}
\sum_{k>Y}(1+\log(k+2))(1+k)^{-A}
\to0.
\]

Thus, fast Mellin decay of the basis functions plus a zero-count shell bound gives truncation convergence.

This is not yet a fully source-imported theorem because the exact admissible function class and zero-count bound still require primary-source alignment.

But it gives the exact route.

---

# 7. What this achieves

Phase 12L proves:

\[
\boxed{
\sup_{g\in\mathcal F_R^{(m)}}|Q_W(g)-Q_Y(g)|
\le
R^2m\delta_Y^{(m)}
}
\]

and shows that if

\[
\delta_Y^{(m)}\to0,
\]

then finite-class spectral truncation converges.

This is a real truncation theorem template.

---

# 8. What remains unresolved

Still unresolved:

1. primary-source confirmation of \(Q_W\);
2. exact admissible function domain;
3. exact zero-count theorem import;
4. exact Mellin decay proof for chosen basis functions;
5. computational realization of \(Q_Y\);
6. arithmetic-side finite form compatibility;
7. whether this spectral truncation is the same \(Q_N\) needed for the final finite certificate.

---

# 9. Updated Level 4 status

On a finite test class, we now have:

\[
\pi_m(R,m)=0
\]

from Phase 12K.

We also have the truncation criterion:

\[
\tau_Y(R,m)\le R^2m\delta_Y^{(m)}.
\]

Therefore, under provisional convention agreement and certified computation,

\[
\sup_{g\in\mathcal F_R^{(m)}}
|Q_Y(g)-Q_W(g)|
\le
R^2m\delta_Y^{(m)}+\chi_Y(R,m).
\]

If

\[
\delta_Y^{(m)}\to0
\]

and

\[
\chi_Y(R,m)\to0,
\]

then the finite-class approximation theorem follows for spectral truncations.

This is a serious Level 4-candidate pathway.

It is still not a breakthrough because the required source imports and concrete basis estimates are not yet complete.

---

# 10. Next target

Phase 12M should choose a concrete finite basis class \(\{\phi_j\}\) and prove Mellin decay bounds:

\[
A_{ij}(k)\le C_{ij,A}(1+k)^{-A}.
\]

Without concrete basis estimates, \(\delta_Y^{(m)}\to0\) remains conditional.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove Level 4 contribution.

This phase does not establish novelty.

Exact audit strings:

TRUNCATION_ERROR_GATE_COMPLETE

SPECTRAL_TRUNCATION_Q_Y_DEFINED

TAIL_ERROR_T_Y_DEFINED

TAIL_GRAM_MATRIX_DEFINED

FINITE_CLASS_TRUNCATION_BOUND_PROVED

ENTRYWISE_TRUNCATION_BOUND_PROVED

SHELL_COUNT_TRUNCATION_BOUND_PROVED

TRUNCATION_CONVERGENCE_CRITERION_PROVED

DELTA_Y_TO_ZERO_STILL_NEEDS_BASIS_ESTIMATES

LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED

