# Phase B7 — Convention Reconciliation

## Purpose

Phase B6 extracted the Bombieri–Lagarias primary conventions.

Phase B7 reconciles those conventions with the project's earlier notation before any certified arithmetic matrix work continues.

This phase prevents a common research error:

\[
\boxed{
\text{building certified computations on mismatched definitions}
}
\]

---

# 1. Bombieri–Lagarias source conventions

Bombieri–Lagarias use the Mellin transform:

\[
f(s)=\int_0^\infty f(x)x^{s-1}\,dx.
\]

They define the involution:

\[
\widetilde f(x)=\frac1x f\left(\frac1x\right).
\]

They define multiplicative convolution:

\[
(f\vee g)(x)=\int_0^\infty f(xy)g(y)\frac{dy}{y}.
\]

They state that the Mellin transform of a convolution-square object has the spectral product:

\[
f(s)f(1-s).
\]

This is real and positive on the critical line.

---

# 2. Project conventions

The project previously used:

\[
\widehat f(s)=\int_0^\infty f(x)x^{s-1}\,dx.
\]

\[
f^*(x)=x^{-1}\overline{f(1/x)}.
\]

\[
(f*g)(x)=\int_0^\infty f(y)g(x/y)\frac{dy}{y}.
\]

Then:

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

# 3. Reconciliation map

Bombieri–Lagarias separate inversion and complex conjugation.

The project combines them into one star operation.

The reconciliation is:

\[
f^*=\widetilde{\bar f}.
\]

That is:

\[
f^*(x)=\frac1x\overline{f(1/x)}.
\]

So the project star convention is compatible with Bombieri–Lagarias after separating:

1. tilde inversion;
2. complex conjugation.

---

# 4. Convolution reconciliation

Bombieri–Lagarias use:

\[
(f\vee g)(x)=\int_0^\infty f(xy)g(y)\frac{dy}{y}.
\]

The project uses:

\[
(f*g)(x)=\int_0^\infty f(y)g(x/y)\frac{dy}{y}.
\]

These are different-looking but related by change of variables and ordering.

The safest rule is:

\[
\boxed{
\text{all future arithmetic entries must state which convention is used}
}
\]

and

\[
\boxed{
\text{do not freely replace } \vee \text{ by } * \text{ without checking order/involution.}
}
\]

---

# 5. Spectral product reconciliation

Bombieri–Lagarias source product:

\[
\mathcal M(f\vee\bar f)(s)=f(s)f(1-s).
\]

Project product:

\[
\widehat{f*f^*}(s)
=
\widehat f(s)\overline{\widehat f(1-\bar s)}.
\]

On the critical line both produce a nonnegative square-type object.

For real-valued \(f\), and after aligning tilde/conjugation conventions, these represent the same positivity mechanism.

For complex \(f\), the conjugation convention must be tracked explicitly.

---

# 6. Explicit formula constant correction

Bombieri–Lagarias displayed explicit formula includes:

\[
-(\log\pi+\gamma)f(1).
\]

Earlier project notes sometimes used:

\[
-(\log4\pi+\gamma)f(1).
\]

Therefore the project must not treat the constant as locked across normalizations.

Correction rule:

\[
\boxed{
\text{Arithmetic entries must carry a named normalization field.}
}
\]

Allowed labels:

1. `bombieri_lagarias_normalization`;
2. `earlier_project_normalization`;
3. `unreconciled_normalization`.

Until the exact transformation is documented, certified arithmetic entries must use:

\[
\boxed{
\text{bombieri\_lagarias\_normalization}
}
\]

when relying on the Bombieri–Lagarias source formula.

---

# 7. Pole constraints status

The project used:

\[
\widehat g(0)=0,
\qquad
\widehat g(1)=0.
\]

Bombieri–Lagarias confirm that the explicit formula contains pole/integral terms, but this extraction alone does not fully lock the finite-subspace constraints for \(g\).

Therefore status remains:

\[
\boxed{
\text{POLE\_CONSTRAINTS\_PLAUSIBLE\_BUT\_NOT\_FULLY\_LOCKED}
}
\]

Future certified matrices can include pole constraints as a cautious admissibility restriction, but must label them as source-plausible rather than fully source-locked.

---

# 8. Theorem B7.1 — compatibility of project star with Bombieri–Lagarias tilde plus conjugation

Let Bombieri–Lagarias define:

\[
\widetilde f(x)=x^{-1}f(1/x).
\]

Let the project define:

\[
f^*(x)=x^{-1}\overline{f(1/x)}.
\]

Then:

\[
f^*=\widetilde{\bar f}.
\]

## Proof

By definition:

\[
\widetilde{\bar f}(x)
=
x^{-1}\bar f(1/x)
=
x^{-1}\overline{f(1/x)}.
\]

This is exactly:

\[
f^*(x).
\]

Therefore:

\[
f^*=\widetilde{\bar f}.
\]

\[
\square
\]

---

# 9. Theorem B7.2 — normalization safety rule

Any arithmetic matrix entry derived from the Bombieri–Lagarias displayed explicit formula must use the constant:

\[
(\log\pi+\gamma)f(1)
\]

unless an explicit transformation to another normalization is proven.

## Proof

Phase B6 extracted the displayed Bombieri–Lagarias formula with the constant:

\[
(\log\pi+\gamma)f(1).
\]

Using a different constant changes the quadratic functional by a multiple of \(f(1)\).

Therefore changing the constant without proof changes the value of the arithmetic matrix entries.

Thus the Bombieri–Lagarias constant must be used under Bombieri–Lagarias normalization.

\[
\square
\]

---

# 10. Updated certified-entry target

Any future certified arithmetic entry must store:

1. source normalization;
2. Mellin convention;
3. involution convention;
4. convolution convention;
5. constant term convention;
6. pole constraint status;
7. whether complex conjugation is included.

This becomes the required metadata header for Phase B8.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a breakthrough.

This phase does not prove novelty.

This phase does not compute certified arithmetic entries.

Exact audit strings:

PHASE_B7_CONVENTION_RECONCILIATION_COMPLETE

PROJECT_STAR_EQUALS_TILDE_CONJUGATE

CONVOLUTION_CONVENTION_DIFFERENCE_TRACKED

SPECTRAL_PRODUCT_RECONCILED

EXPLICIT_FORMULA_CONSTANT_RECONCILED_TO_BOMBIERI_LAGARIAS

NORMALIZATION_METADATA_REQUIRED

POLE_CONSTRAINTS_PLAUSIBLE_NOT_FULLY_LOCKED

CERTIFIED_ENTRY_METADATA_SCHEMA_CREATED

BREAKTHROUGH_NOT_ACHIEVED

READY_FOR_PHASE_B8_CERTIFIED_ENTRY_METADATA

