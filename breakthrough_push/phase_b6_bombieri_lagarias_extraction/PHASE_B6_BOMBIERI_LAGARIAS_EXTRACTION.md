# Phase B6 — Bombieri–Lagarias Primary Extraction

## Purpose

Phase B6 extracts exact mathematical content from Bombieri and Lagarias,
"Complements to Li's Criterion for the Riemann Hypothesis," Journal of Number Theory 77, 274–287 (1999).

This is the first real primary-source extraction in the breakthrough-push branch.

---

# 1. Paper identity

Title:

\[
\text{Complements to Li's Criterion for the Riemann Hypothesis}
\]

Authors:

\[
\text{Enrico Bombieri and Jeffrey C. Lagarias}
\]

Journal:

\[
\text{Journal of Number Theory 77, 274–287 (1999)}
\]

Purpose of paper:

1. prove a general criterion for multisets of complex numbers;
2. recover Li's criterion for RH;
3. give an arithmetic formula for Li's numbers via the Guinand–Weil explicit formula;
4. relate Li's positivity to Weil's criterion.

---

# 2. Explicit formula test functions

Bombieri–Lagarias consider functions \(f(x)\) on \((0,\infty)\) satisfying:

## Condition (A)

\(f(x)\) is continuous and continuously differentiable except at finitely many points, where \(f\) and \(f'\) have at most first-kind discontinuities.

## Condition (B)

There exists \(\delta>0\) such that

\[
f(x)=O(x^\delta)
\quad\text{as }x\to0^+
\]

and

\[
f(x)=O(x^{-1-\delta})
\quad\text{as }x\to+\infty.
\]

This is broader than the earlier project’s \(C_c^\infty(0,\infty)\) working class.

---

# 3. Involution convention

Bombieri–Lagarias define an involution \(f\mapsto \widetilde f\) by:

\[
\widetilde f(x)=\frac1x f\left(\frac1x\right).
\]

This matches the project’s non-conjugated star convention for real-valued functions.

For complex-valued functions, the paper later uses complex conjugation separately.

Project convention:

\[
f^*(x)=x^{-1}\overline{f(1/x)}.
\]

Bombieri–Lagarias split this into:

\[
\widetilde f(x)=x^{-1}f(1/x)
\]

and conjugation \(\bar f\).

Thus the project convention is consistent if:

\[
f^*=\widetilde{\bar f}.
\]

---

# 4. Mellin transform convention

Bombieri–Lagarias define the Mellin transform as:

\[
f(s)=\int_0^\infty f(x)x^{s-1}\,dx.
\]

This matches the project convention:

\[
\widehat f(s)=\int_0^\infty f(x)x^{s-1}\,dx.
\]

---

# 5. Explicit formula

Bombieri–Lagarias state the explicit formula:

\[
\sum_{\rho} f(\rho)
=
\int_0^\infty f(x)\,dx
+
\int_0^\infty \widetilde f(x)\,dx
-
\sum_{n=1}^{\infty}\Lambda(n)\{f(n)+\widetilde f(n)\}
\]

\[
-(\log\pi+\gamma)f(1)
-
\int_1^\infty
\left\{
f(x)+\widetilde f(x)-\frac{2}{x^2}f(1)
\right\}
\frac{x\,dx}{x^2-1}.
\]

This source confirms the explicit-formula architecture used in the project, though the constant differs from one earlier project form that used \(\log 4\pi+\gamma\).

Important correction:

\[
\boxed{
\text{Bombieri–Lagarias source form uses }(\log\pi+\gamma)f(1)
}
\]

in the displayed explicit formula.

The project must keep separate convention records for:

1. Bombieri form;
2. Weil form;
3. any transformed normalization;
4. previous project formula using \(\log 4\pi+\gamma\).

---

# 6. Multiplicative convolution

In Section 4, Bombieri–Lagarias define multiplicative convolution of complex-valued functions:

\[
(f\vee g)(x)=\int_0^\infty f(xy)g(y)\frac{dy}{y}.
\]

This differs by a change of variable from the project convention

\[
(f*g)(x)=\int_0^\infty f(y)g(x/y)\frac{dy}{y}.
\]

These are equivalent up to the convention/order used, but must be tracked carefully.

---

# 7. Mellin transform of convolution

Bombieri–Lagarias state:

\[
\mathcal M(f\vee g)(s)=f(s)\widehat g(s)
\]

under their notation.

They then state that the Mellin transform of

\[
f\vee \bar f
\]

is:

\[
f(s)f(1-s).
\]

This is the central source-confirmed spectral product.

On the critical line:

\[
\Re(s)=\frac12,
\]

this is real and positive.

In project notation, with the appropriate involution/conjugation convention, this corresponds to:

\[
\widehat{f*f^*}(s)
=
\widehat f(s)\overline{\widehat f(1-\bar s)}.
\]

On the critical line:

\[
s=\frac12+it,
\]

this becomes:

\[
|\widehat f(1/2+it)|^2.
\]

---

# 8. Relation to Weil criterion

Bombieri–Lagarias state that positivity of the explicit formula on functions of the type

\[
f\vee\bar f
\]

is a necessary condition for RH.

They also state that, as shown by Weil, this condition is sufficient.

Thus the paper confirms the conceptual bridge:

\[
\text{RH}
\Longleftrightarrow
\text{positivity of explicit formula on convolution-square test functions}.
\]

---

# 9. Pole-removal status

Bombieri–Lagarias do not present the pole-removal constraints in the exact same finite-subspace language used in Phase B1/B2.

However, their explicit formula contains the two integral terms:

\[
\int_0^\infty f(x)\,dx,
\qquad
\int_0^\infty \widetilde f(x)\,dx.
\]

These correspond to pole terms.

The project’s constraints

\[
\widehat g(0)=0,
\qquad
\widehat g(1)=0
\]

remain plausible as a way to remove pole contributions, but must be cross-checked with Weil’s original admissible formulation and the exact \(f\vee\bar f\) construction.

Status:

\[
\boxed{
\text{POLE\_CONSTRAINTS\_PLAUSIBLE\_BUT\_NOT\_FULLY\_LOCKED\_BY\_BOMBIERI\_LAGARIAS}
}
\]

---

# 10. Collision with project

## Confirmed matches

Bombieri–Lagarias confirms:

1. Mellin transform convention;
2. involution \(f\mapsto \widetilde f\);
3. Guinand–Weil explicit formula structure;
4. multiplicative convolution;
5. spectral product positive on the critical line;
6. link between positivity and Weil’s criterion.

## Differences or corrections

1. Their convolution notation is \(f\vee g\), with \(f(xy)g(y)\,dy/y\).
2. Their explicit formula uses \((\log\pi+\gamma)f(1)\) in the displayed form.
3. Their complex-conjugation convention is not identical to the project’s \(f^*\), but is compatible after separating involution and conjugation.
4. Pole-removal constraints need more source validation.

## Novelty collision

The source confirms that the convolution-square positivity framework is classical.

Therefore the project cannot claim novelty for:

\[
f\vee\bar f
\]

or

\[
\widehat f(s)f(1-s)
\]

or the positivity connection to Weil’s criterion.

---

# 11. Updated project correction

The project should replace loose language:

\[
g*g^*
\]

with a source-aware convention table:

\[
\widetilde f(x)=x^{-1}f(1/x)
\]

\[
(f\vee g)(x)=\int_0^\infty f(xy)g(y)\frac{dy}{y}
\]

\[
\mathcal M(f\vee\bar f)(s)=f(s)f(1-s)
\]

and then explain how this maps to the project's alternate notation.

---

# 12. Breakthrough status after B6

B6 strengthens the project by validating core conventions.

But it also increases prior-art collision risk.

Current status:

\[
\boxed{
\text{SOURCE\_CORRECTNESS\_IMPROVED}
}
\]

\[
\boxed{
\text{NOVELTY\_RISK\_INCREASED}
}
\]

\[
\boxed{
\text{BREAKTHROUGH\_NOT\_ACHIEVED}
}
\]

---

# 13. Next target

Phase B7 should create a convention reconciliation layer:

1. Bombieri–Lagarias notation;
2. project notation;
3. exact map between \(f\vee\bar f\), \(\widetilde f\), and \(f^*\);
4. corrected explicit formula constants;
5. impact on arithmetic matrix entries.

This must happen before certified arithmetic entries.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a breakthrough.

This phase does not prove novelty.

This phase does not fully validate pole constraints.

Exact audit strings:

PHASE_B6_BOMBIERI_LAGARIAS_EXTRACTION_COMPLETE

BOMBIERI_LAGARIAS_PRIMARY_SOURCE_USED

MELLIN_TRANSFORM_CONVENTION_CONFIRMED

INVOLUTION_TILDE_CONVENTION_CONFIRMED

MULTIPLICATIVE_CONVOLUTION_CONFIRMED

CONVOLUTION_SPECTRAL_PRODUCT_CONFIRMED

WEIL_POSITIVITY_CONNECTION_CONFIRMED

EXPLICIT_FORMULA_CONSTANT_CORRECTION_IDENTIFIED

POLE_CONSTRAINTS_NOT_FULLY_LOCKED

CLASSICAL_CONVOLUTION_SQUARE_NOT_NOVEL

BREAKTHROUGH_NOT_ACHIEVED

READY_FOR_PHASE_B7_CONVENTION_RECONCILIATION

