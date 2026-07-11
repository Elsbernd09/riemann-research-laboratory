# Phase 8B — Weil Object Definitions

## Purpose

Phase 8A started the classical Weil criterion reconstruction program.

Phase 8B defines the objects that future phases must handle carefully.

This is not a proof of RH.

This is not a new Weil criterion.

This is a notation and object-definition phase.

---

# 1. Why this phase matters

The Phase 7 toy models were useful but not canonical.

To move beyond toy models, the repository needs explicit definitions for:

1. test functions;
2. transforms;
3. zero-side terms;
4. prime-side terms;
5. quadratic forms;
6. positivity statements;
7. negative directions.

Without these definitions, later finite-rank experiments risk confusing diagnostics with the classical Weil criterion.

---

# 2. Zero-side object

Let

\[
\rho=\beta+i\gamma
\]

range over nontrivial zeros of the completed zeta function.

A generic zero-side linear statistic has the form

\[
Z(h)
=
\sum_\rho h(\rho),
\]

where \(h\) is an admissible test function or transformed test function.

The key RH-relevant fact is that the value of \(h(\rho)\) may depend on both

\[
\beta
\]

and

\[
\gamma.
\]

Therefore zero-side statistics can be horizontally sensitive if the test family is rich enough.

---

# 3. Test-function object

A test function is an allowed function chosen from a class suitable for the explicit formula.

The exact admissible class depends on the version of the Weil criterion being used.

For this repository, the placeholder notation is:

\[
f\in\mathcal A.
\]

The class \(\mathcal A\) must eventually be replaced by a literature-correct admissible test-function space.

Until that replacement is complete, all results involving \(\mathcal A\) are reconstruction scaffolding, not final theorems.

---

# 4. Transform object

Weil-type formulae usually involve a transform of the test function.

We write this schematically as

\[
\widehat f
\]

or

\[
\mathcal T f.
\]

The exact transform may be Fourier, Mellin, or a version adapted to the completed zeta function.

Phase 8 does not yet choose a final transform.

Future phases must record the exact convention before proving any theorem.

---

# 5. Quadratic form object

A Weil-type positivity statement has the schematic form

\[
\mathcal W(f)\ge0
\]

for every allowed test function \(f\).

The functional

\[
\mathcal W
\]

is not arbitrary.

It must arise from the classical explicit formula or an equivalent known formulation.

A toy finite-rank matrix is not a Weil quadratic form unless this connection is proved.

---

# 6. Negative direction object

A negative direction is an admissible test function \(f\) such that

\[
\mathcal W(f)<0.
\]

In Weil-type criteria, the existence of off-critical zeros is associated with the existence of such negative directions.

Future finite-rank work should approximate this mechanism only after the relevant classical quadratic form is fixed.

---

# 7. Finite-rank approximation object

A finite-rank approximation chooses a finite-dimensional subspace

\[
V_m\subset\mathcal A.
\]

Then one studies

\[
\mathcal W(f)
\]

for

\[
f\in V_m.
\]

Choosing \(V_m\) arbitrarily may produce diagnostic behavior but does not prove anything about the classical criterion unless:

1. \(V_m\subset\mathcal A\);
2. the restriction of \(\mathcal W\) is correctly computed;
3. convergence or density properties are understood.

---

# 8. Object dependency chain

The correct dependency chain is:

\[
\text{admissible test functions}
\Rightarrow
\text{transform}
\Rightarrow
\text{explicit formula}
\Rightarrow
\text{Weil quadratic form}
\Rightarrow
\text{negative-direction mechanism}
\Rightarrow
\text{finite-rank model}.
\]

Phase 7 toy models skipped most of this chain.

Phase 8 must rebuild it.

---

# 9. Phase conclusion

The central rule is:

\[
\boxed{
\text{No finite-rank object should be called Weil-compatible until the classical object map is fixed.}
}
\]

