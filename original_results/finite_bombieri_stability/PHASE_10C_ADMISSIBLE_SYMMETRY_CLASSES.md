# Phase 10C — Admissible Finite Symmetry Classes

## Purpose

Phase 10B locked the finite matrix object:

\[
\mathcal M(\Gamma,t)=D^{1/2}A(t)D^{1/2}.
\]

Phase 10C defines the admissible finite symmetry classes for \(\Gamma\).

The purpose is to state exactly when a finite multiset is allowed inside the original stability theorem.

---

# 1. Why symmetry is needed

Bombieri-style finite zero configurations are not arbitrary finite subsets of \(\mathbb C\).

They are motivated by zero symmetries.

A meaningful finite model should record which closure properties are assumed.

This branch will not claim these are zeta zeros.

This branch works with synthetic finite multisets satisfying explicitly defined symmetries.

---

# 2. Finite multiset

A finite multiset is a finite collection

\[
\Gamma=\{\gamma_1,\ldots,\gamma_n\}\subset\mathbb C
\]

where repeated values are allowed.

The distinct support is

\[
\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}.
\]

The multiplicity function is

\[
m:\Gamma_{\mathrm{dist}}\to\mathbb N.
\]

---

# 3. Conjugation closure

A finite multiset \(\Gamma\) is conjugation-closed if

\[
\gamma\in\Gamma
\implies
\overline{\gamma}\in\Gamma
\]

with the same multiplicity.

Equivalently,

\[
m(\gamma)=m(\overline{\gamma}).
\]

---

# 4. Reflection closure

A finite multiset \(\Gamma\) is reflection-closed if

\[
\gamma\in\Gamma
\implies
-\gamma\in\Gamma
\]

with the same multiplicity.

Equivalently,

\[
m(\gamma)=m(-\gamma).
\]

---

# 5. Quartet closure

A finite multiset \(\Gamma\) is quartet-closed if

\[
\gamma\in\Gamma
\implies
\gamma,\overline{\gamma},-\gamma,-\overline{\gamma}\in\Gamma
\]

with equal multiplicities across the quartet.

This is the strongest finite symmetry class used in the branch.

---

# 6. Real-axis cases

If

\[
\gamma\in\mathbb R,
\]

then

\[
\overline{\gamma}=\gamma.
\]

In this case conjugation closure is automatic, but reflection closure still requires \(-\gamma\) with matching multiplicity.

If \(\gamma=0\), both conjugation and reflection fix \(\gamma\).

---

# 7. Admissible classes

We define three admissible classes.

## Class C

\[
\mathcal C_N
\]

is the class of finite conjugation-closed multisets with \(N\) distinct support points.

## Class R

\[
\mathcal R_N
\]

is the class of finite reflection-closed multisets with \(N\) distinct support points.

## Class Q

\[
\mathcal Q_N
\]

is the class of finite quartet-closed multisets with \(N\) distinct support points.

The strongest theorem version will be stated for \(\mathcal Q_N\).

Weaker versions may be stated for \(\mathcal C_N\) or \(\mathcal R_N\) if the proof only requires one symmetry.

---

# 8. Negative pair count

Define the synthetic conjugate-pair count:

\[
q(\Gamma)
=
\#\{\{\gamma,\overline{\gamma}\}:\gamma\in\Gamma_{\mathrm{dist}},\ \gamma\neq\overline{\gamma}\}.
\]

This counts distinct non-real conjugate pairs in the support.

This is not an RH statement.

It is only a finite synthetic combinatorial statistic.

---

# 9. Stability theorem relationship

The eventual stability theorem will not require \(q(\Gamma)\) directly.

The theorem will stabilize

\[
n_-(\mathcal M(\Gamma,t)).
\]

However, the synthetic validation branch may compare this number against \(q(\Gamma)\) when appropriate.

---

# 10. Boundary

These are finite synthetic symmetry classes.

They do not contain zeta zeros.

They do not prove RH.

They do not falsify RH.

They do not claim novelty.


---

# Exact audit boundary phrases

This phase does not prove RH.

This phase does not falsify RH.

This phase does not use zeta zeros.

This phase does not claim novelty.

