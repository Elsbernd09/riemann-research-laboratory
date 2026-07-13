# Phase X2 — Exact Functional Lock

## Purpose

Phase X2 locks one exact functional for the breakthrough attack.

We now use the Bombieri–Lagarias normalization only.

No mixed conventions.

No switching between \(\log 4\pi+\gamma\) and \(\log\pi+\gamma\).

No switching between incompatible star conventions.

---

# 1. Locked functional

The locked functional is denoted:

\[
T_{BL}[f].
\]

It follows the Bombieri–Lagarias convention:

\[
\widetilde f(x)=x^{-1}f(1/x),
\]

\[
\widehat f(s)=\int_0^\infty f(x)x^{s-1}\,dx.
\]

The explicit formula functional has the structure:

\[
T_{BL}[f]
=
\int_0^\infty f(x)\,dx
+
\int_0^\infty \widetilde f(x)\,dx
-
\sum_{n=1}^{\infty}\Lambda(n)\left(f(n)+\widetilde f(n)\right)
-
(\log\pi+\gamma)f(1)
-
\int_1^\infty
\left(f(x)+\widetilde f(x)-2x^{-2}f(1)\right)
\frac{x\,dx}{x^2-1}.
\]

This is the only normalization allowed in the breakthrough attack branch.

---

# 2. Locked involution

The locked involution is:

\[
\widetilde f(x)=x^{-1}f(1/x).
\]

For complex-valued functions, the Hermitian star convention is:

\[
f^*(x)=x^{-1}\overline{f(1/x)}.
\]

Thus:

\[
f^*=\widetilde{\overline f}.
\]

---

# 3. Locked convolution-square object

The positivity test object is taken to be:

\[
f=g*g^*.
\]

In the locked convention:

\[
g^*(x)=x^{-1}\overline{g(1/x)}.
\]

The attack branch will not use the convention:

\[
g^*(x)=\overline{g(1/x)}
\]

unless a later source transformation explicitly proves equivalence.

---

# 4. Locked pole-removal target

The pole-removal condition is imposed on the test object \(f\):

\[
\widehat f(0)=0,
\qquad
\widehat f(1)=0.
\]

For finite linear construction, we may use the stronger sufficient condition:

\[
\widehat g(0)=0,
\qquad
\widehat g(1)=0,
\]

because it implies the locked \(f\)-pole cancellation under the convolution-square Mellin product identity.

But the official target is:

\[
\boxed{
\widehat f(0)=\widehat f(1)=0.
}
\]

---

# 5. Locked finite arithmetic matrix

For a finite admissible smooth basis:

\[
g_a=\sum_{j=1}^{m}a_j\phi_j,
\]

define:

\[
f_a=g_a*g_a^*.
\]

The finite arithmetic matrix is the Hermitian matrix satisfying:

\[
a^*M a = T_{BL}[g_a*g_a^*].
\]

Equivalently:

\[
M_{ij}=T_{BL}[\phi_j*\phi_i^*].
\]

The certified finite matrix goal is:

\[
M_{ij}\in [L_{ij},U_{ij}]
\]

with rigorous interval proof for every entry.

---

# 6. The breakthrough gap

Based on the current user-supplied source intelligence:

1. modern Connes-style papers build structural or numerical finite matrices;
2. they do not appear to provide fully certified interval arithmetic finite matrices;
3. therefore a possible gap remains:

\[
\boxed{
\text{certified finite arithmetic Weil/Bombieri matrix entries}
}
\]

This is not yet a novelty proof.

It is a target gap.

---

# Theorem X2.1 — locked functional removes normalization ambiguity

Once \(T_{BL}\) is fixed with the constant:

\[
\log\pi+\gamma,
\]

no later arithmetic matrix entry may use:

\[
\log 4\pi+\gamma
\]

unless a separate source-proven change of variables is recorded.

## Proof

The matrix entries are defined by:

\[
M_{ij}=T_{BL}[\phi_j*\phi_i^*].
\]

Changing the constant term changes \(T_{BL}\), hence changes \(M_{ij}\).

Therefore a matrix entry computed with \(\log 4\pi+\gamma\) is not an entry of the locked \(T_{BL}\) matrix.

\[
\square
\]

---

# Theorem X2.2 — official admissibility target is linear in \(f\), not necessarily in \(g\)

The locked pole-removal target is:

\[
\widehat f(0)=\widehat f(1)=0.
\]

If \(f=g*g^*\), then imposing:

\[
\widehat g(0)=\widehat g(1)=0
\]

is a sufficient finite-construction device, but it is not declared necessary.

## Proof

The official locked condition is stated on \(f\).

A stronger condition on \(g\) may imply the condition on \(f\), but implication does not establish equivalence.

Thus the \(g\)-constraints are sufficient construction constraints, not the official source-level target.

\[
\square
\]

---

# 7. Next phase

Phase X3 should build a smooth compactly supported basis with built-in stronger pole cancellation:

\[
\widehat \phi_j(0)=0,
\qquad
\widehat \phi_j(1)=0.
\]

This will create a finite admissible \(g\)-basis that automatically produces pole-cancelled \(f=g*g^*\).

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not create a certified matrix.

It locks the exact functional and removes convention ambiguity.

Exact audit strings:

PHASE_X2_EXACT_FUNCTIONAL_LOCK_COMPLETE

BOMBIERI_LAGARIAS_FUNCTIONAL_LOCKED

LOG_PI_GAMMA_CONSTANT_LOCKED

LOG_4PI_GAMMA_REJECTED_FOR_LOCKED_BRANCH

TILDE_INVOLUTION_LOCKED

HERMITIAN_STAR_DICTIONARY_LOCKED

F_POLE_REMOVAL_TARGET_LOCKED

G_POLE_CONSTRAINTS_MARKED_SUFFICIENT_NOT_NECESSARY

FINITE_ARITHMETIC_MATRIX_TARGET_DEFINED

CERTIFIED_MATRIX_GAP_TARGET_IDENTIFIED

READY_FOR_PHASE_X3_BUILT_IN_POLE_CANCELLED_SMOOTH_BASIS

