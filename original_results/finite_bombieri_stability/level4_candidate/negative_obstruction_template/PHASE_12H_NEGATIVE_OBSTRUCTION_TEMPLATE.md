# Phase 12H — Negative Obstruction Detection Template

## Purpose

Phase 12G derived the provisional spectral form

\[
Q_W(g)
=
\sum_\rho
\widehat g(\rho)
\overline{\widehat g(1-\bar\rho)}
\]

and showed that RH implies provisional positivity.

Phase 12H states the exact finite-detection theorem template needed for a Level 4 breakthrough candidate.

The target is:

\[
Q_W(g)<0
\Longrightarrow
Q_N(P_Ng)<0
\]

for sufficiently large \(N\), with explicit error control.

---

# 1. Infinite obstruction

An infinite Weil-form obstruction is a function \(g\) such that

\[
Q_W(g)<0.
\]

For quantitative detection, assume a margin:

\[
Q_W(g)\le -\eta
\]

for some

\[
\eta>0.
\]

---

# 2. Finite approximation target

Let \(Q_N\) be a finite approximating quadratic form.

Let

\[
P_Ng
\]

be the finite approximation of \(g\).

The hard theorem needed is an approximation bound:

\[
|Q_N(P_Ng)-Q_W(g)|\le\varepsilon_N(g).
\]

If

\[
\varepsilon_N(g)\to0,
\]

then sufficiently large finite approximations detect the infinite obstruction.

---

# Theorem 12H.1 — Negative obstruction detection template

Assume

\[
Q_W(g)\le -\eta
\]

for some

\[
\eta>0.
\]

Assume also that for some \(N\),

\[
|Q_N(P_Ng)-Q_W(g)|<\eta/2.
\]

Then

\[
Q_N(P_Ng)<-\eta/2.
\]

## Proof

By the triangle inequality,

\[
Q_N(P_Ng)
\le
Q_W(g)+|Q_N(P_Ng)-Q_W(g)|.
\]

Using

\[
Q_W(g)\le-\eta
\]

and

\[
|Q_N(P_Ng)-Q_W(g)|<\eta/2,
\]

we obtain

\[
Q_N(P_Ng)
<
-\eta+\eta/2
=
-\eta/2.
\]

Therefore,

\[
Q_N(P_Ng)<-\eta/2.
\]

\[
\square
\]

---

# Corollary 12H.2 — Eventual finite detection

Assume

\[
Q_W(g)\le-\eta
\]

and

\[
\varepsilon_N(g)\to0
\]

where

\[
|Q_N(P_Ng)-Q_W(g)|\le\varepsilon_N(g).
\]

Then there exists \(N_0\) such that for all

\[
N\ge N_0,
\]

we have

\[
Q_N(P_Ng)<-\eta/2.
\]

## Proof

Since

\[
\varepsilon_N(g)\to0,
\]

there exists \(N_0\) such that for all \(N\ge N_0\),

\[
\varepsilon_N(g)<\eta/2.
\]

Thus, for all \(N\ge N_0\),

\[
|Q_N(P_Ng)-Q_W(g)|<\eta/2.
\]

Apply Theorem 12H.1.

\[
\square
\]

---

# 3. Uniform finite-class version

Let

\[
\mathcal F_R^{(m)}
=
\left\{
g=\sum_{j=1}^{m}a_j\phi_j:\|a\|_2\le R
\right\}.
\]

Assume

\[
\sup_{g\in\mathcal F_R^{(m)}}
|Q_N(P_Ng)-Q_W(g)|
\le
\varepsilon_N(R,m).
\]

If

\[
\varepsilon_N(R,m)\to0,
\]

then every negative infinite obstruction in \(\mathcal F_R^{(m)}\) with margin \(\eta\) is eventually detected by finite forms.

---

# Theorem 12H.3 — Uniform finite-class negative detection

Assume

\[
\sup_{g\in\mathcal F_R^{(m)}}
|Q_N(P_Ng)-Q_W(g)|
\le
\varepsilon_N(R,m).
\]

Assume

\[
\varepsilon_N(R,m)<\eta/2.
\]

If

\[
g\in\mathcal F_R^{(m)}
\]

and

\[
Q_W(g)\le-\eta,
\]

then

\[
Q_N(P_Ng)<-\eta/2.
\]

## Proof

Since \(g\in\mathcal F_R^{(m)}\),

\[
|Q_N(P_Ng)-Q_W(g)|
\le
\sup_{h\in\mathcal F_R^{(m)}}
|Q_N(P_Nh)-Q_W(h)|
\le
\varepsilon_N(R,m).
\]

By assumption,

\[
\varepsilon_N(R,m)<\eta/2.
\]

Therefore,

\[
|Q_N(P_Ng)-Q_W(g)|<\eta/2.
\]

Apply Theorem 12H.1.

\[
\square
\]

---

# 4. What this proves

This phase proves the formal negative-detection implication:

\[
Q_W(g)\le-\eta
\quad\text{and}\quad
|Q_N(P_Ng)-Q_W(g)|<\eta/2
\Longrightarrow
Q_N(P_Ng)<-\eta/2.
\]

It also proves the uniform finite-class version.

---

# 5. What remains hard

The hard part is not Theorem 12H.1.

The hard part is proving the approximation theorem:

\[
|Q_N(P_Ng)-Q_W(g)|\le\varepsilon_N(g)
\]

with

\[
\varepsilon_N(g)\to0.
\]

For a finite test class, the needed theorem is:

\[
\sup_{g\in\mathcal F_R^{(m)}}
|Q_N(P_Ng)-Q_W(g)|
\le
\varepsilon_N(R,m)
\to0.
\]

This is the actual Level 4 breakthrough-candidate target.

---

# 6. Next target

Phase 12I must define the approximation error decomposition for the provisional \(Q_W(g)=T[g*g^*]\):

\[
Q_N(P_Ng)-Q_W(g).
\]

It must identify the exact terms:

1. truncation error;
2. projection error;
3. source-normalization/sign error;
4. computational error.

Then the branch can attack each bound.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove the finite approximation theorem.

This phase does not prove Level 4 contribution.

This phase does not establish novelty.

Exact audit strings:

NEGATIVE_OBSTRUCTION_TEMPLATE_COMPLETE

NEGATIVE_DETECTION_TEMPLATE_PROVED

EVENTUAL_FINITE_DETECTION_COROLLARY_PROVED

UNIFORM_FINITE_CLASS_DETECTION_PROVED

FINITE_APPROXIMATION_THEOREM_STILL_MISSING

EPSILON_N_CONVERGENCE_STILL_MISSING

LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED

