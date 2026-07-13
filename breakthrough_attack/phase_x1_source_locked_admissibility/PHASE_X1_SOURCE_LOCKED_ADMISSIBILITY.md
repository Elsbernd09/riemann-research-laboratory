# Phase X1 — Source-Locked Admissibility Attack

## Purpose

This phase starts the serious breakthrough attack.

The goal is no longer broad framework-building.

The goal is to lock the exact admissibility conditions needed for a finite arithmetic Weil/Bombieri matrix theorem.

---

# 1. User-provided live-search inputs

The user supplied live-search notes claiming the following objects:

\[
W(f\star f^\vee)\ge 0
\]

as a Weil positivity criterion.

The notes also claim admissible functions satisfy regularity, growth, Mellin-strip, and pole-cancellation constraints.

They further claim a pole cancellation implication:

\[
\widetilde g(0)=0,\qquad \widetilde g(1)=0
\Longrightarrow
\widetilde f(0)=\widetilde f(1)=0.
\]

However, these notes include several convention conflicts.

Therefore this phase is a source-locking attack, not a victory declaration.

---

# 2. Immediate conflicts detected

## Conflict 1 — star convention mismatch

One version says:

\[
g^*(x)=\overline{g(x^{-1})}.
\]

But Bombieri–Lagarias define the involution:

\[
\widetilde f(x)=x^{-1}f(1/x).
\]

The project convention has been:

\[
g^*(x)=x^{-1}\overline{g(1/x)}.
\]

These are not identical.

The missing factor \(x^{-1}\) changes Mellin transforms and therefore changes the spectral product.

Status:

\[
\boxed{\text{STAR\_CONVENTION\_CONFLICT\_DETECTED}}
\]

---

## Conflict 2 — growth conditions mismatch

The user notes state boundary growth like:

\[
f(x)=O(x^{1/2+\varepsilon})
\]

near \(0\), and

\[
f(x)=O(x^{-1/2-\varepsilon})
\]

near infinity.

Bombieri–Lagarias use a different-looking condition in the extracted paper:

\[
f(x)=O(x^\delta)
\]

as \(x\to0^+\), and

\[
f(x)=O(x^{-1-\delta})
\]

as \(x\to+\infty\).

These may be equivalent under a normalization or logarithmic change of variables, but this is not yet proved.

Status:

\[
\boxed{\text{GROWTH\_CONDITION\_CONFLICT\_DETECTED}}
\]

---

## Conflict 3 — explicit formula normalization mismatch

The user notes include an archimedean/global formula with a \(\log 4\pi+\gamma\) constant.

The Bombieri–Lagarias extraction used the displayed constant:

\[
\log \pi+\gamma.
\]

This may be due to a transformed normalization, but until proven, arithmetic matrix entries must use one locked normalization.

Status:

\[
\boxed{\text{EXPLICIT\_FORMULA\_NORMALIZATION\_CONFLICT\_DETECTED}}
\]

---

## Conflict 4 — pole cancellation target ambiguity

The key question is:

Are the pole constraints imposed on \(g\):

\[
\widehat g(0)=0,\qquad \widehat g(1)=0,
\]

or on \(f=g\vee\bar g\):

\[
\widehat f(0)=0,\qquad \widehat f(1)=0?
\]

If

\[
\widehat f(s)=\widehat g(s)\widehat g(1-s),
\]

then:

\[
\widehat f(0)=\widehat g(0)\widehat g(1),
\]

and

\[
\widehat f(1)=\widehat g(1)\widehat g(0).
\]

Thus it may be enough that one of \(\widehat g(0)\) or \(\widehat g(1)\) vanishes, not necessarily both.

But for a clean admissible subspace, imposing both is stronger and safer.

Status:

\[
\boxed{\text{POLE\_CANCELLATION\_TARGET\_AMBIGUITY\_DETECTED}}
\]

---

# 3. Theorem X1.1 — safe sufficient pole cancellation

Assume the convolution-square spectral identity:

\[
\widehat f(s)=\widehat g(s)\widehat g(1-s).
\]

If

\[
\widehat g(0)=0
\]

and

\[
\widehat g(1)=0,
\]

then

\[
\widehat f(0)=0
\]

and

\[
\widehat f(1)=0.
\]

## Proof

Evaluate the product at \(s=0\):

\[
\widehat f(0)=\widehat g(0)\widehat g(1).
\]

Since both factors are zero under the stronger admissibility condition, the product is zero.

Evaluate the product at \(s=1\):

\[
\widehat f(1)=\widehat g(1)\widehat g(0).
\]

Again this product is zero.

Thus:

\[
\widehat f(0)=\widehat f(1)=0.
\]

\[
\square
\]

---

# 4. Theorem X1.2 — stronger-than-necessary constraint warning

If the only requirement is:

\[
\widehat f(0)=\widehat f(1)=0,
\]

and if:

\[
\widehat f(s)=\widehat g(s)\widehat g(1-s),
\]

then imposing both

\[
\widehat g(0)=0,\qquad \widehat g(1)=0
\]

is sufficient but may be stronger than necessary.

## Proof

The equations:

\[
\widehat f(0)=\widehat g(0)\widehat g(1)
\]

and

\[
\widehat f(1)=\widehat g(1)\widehat g(0)
\]

both vanish if either \(\widehat g(0)=0\) or \(\widehat g(1)=0\).

Thus requiring both constraints is sufficient, but possibly stronger than required.

\[
\square
\]

---

# 5. Breakthrough target after X1

The aggressive theorem target is now:

\[
\boxed{
\text{finite certified arithmetic matrix theorem on a source-locked admissible subspace}
}
\]

But the admissibility layer must be one of the following:

## Option A — stronger safe subspace

\[
\widehat g(0)=0,\qquad \widehat g(1)=0.
\]

Pros: safe pole cancellation.

Cons: may be unnecessarily restrictive.

## Option B — exact \(f\)-admissibility

\[
\widehat f(0)=0,\qquad \widehat f(1)=0.
\]

Pros: likely closer to explicit formula.

Cons: nonlinear in \(g\), harder for finite matrix construction.

## Option C — source-defined admissibility

Use exactly what Weil/Bombieri/Connes/Suzuki define.

Pros: most correct.

Cons: requires exact primary extraction.

---

# 6. X1 verdict

We cannot yet claim source-locked admissibility.

But we have identified the precise theorem gate:

\[
\boxed{
\text{decide whether admissibility lives on }g\text{ or }f=g\vee\bar g.
}
\]

Until that is solved:

\[
\boxed{\text{CERTIFIED\_FINITE\_WEIL\_MATRIX\_THEOREM\_BLOCKED}}
\]

---

# 7. Required next source target

The next source must answer:

1. In Weil's criterion, what is the exact domain of the positive-definite test object?
2. Does the positivity criterion require pole cancellation?
3. Are pole terms included or removed?
4. Are constraints imposed on \(g\), \(f\), or both?
5. In modern Galerkin matrix papers, how are pole terms handled?

---

# 8. Next phase

Phase X2 should create the exact functional lock:

\[
T_{BL}[f]
\]

with only one convention:

1. Bombieri–Lagarias tilde;
2. Bombieri–Lagarias convolution;
3. Bombieri–Lagarias constant;
4. explicit pole terms included or explicitly removed;
5. no mixed normalizations.

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not source-lock admissibility completely.

It identifies the exact admissibility theorem gate.

Exact audit strings:

PHASE_X1_SOURCE_LOCKED_ADMISSIBILITY_ATTACK_COMPLETE

STAR_CONVENTION_CONFLICT_DETECTED

GROWTH_CONDITION_CONFLICT_DETECTED

EXPLICIT_FORMULA_NORMALIZATION_CONFLICT_DETECTED

POLE_CANCELLATION_TARGET_AMBIGUITY_DETECTED

SAFE_SUFFICIENT_POLE_CANCELLATION_PROVED

STRONGER_THAN_NECESSARY_CONSTRAINT_WARNING_PROVED

CERTIFIED_FINITE_WEIL_MATRIX_THEOREM_BLOCKED

ADMISSIBILITY_GATE_IDENTIFIED

READY_FOR_PHASE_X2_EXACT_FUNCTIONAL_LOCK

