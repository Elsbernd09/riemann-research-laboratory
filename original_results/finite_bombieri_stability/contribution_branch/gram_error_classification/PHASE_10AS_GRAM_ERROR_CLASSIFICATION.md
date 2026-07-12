# Phase 10AS — Gram Error Classification

## Purpose

Phase 10AR decomposed the Gram-entry error:

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

Phase 10AS classifies each term according to whether it is:

1. classical-source dependent;
2. project-controllable;
3. numerical;
4. unresolved.

This is important because a real contribution requires knowing exactly which pieces can be proven by this project and which pieces must be imported from established Weil/Bombieri theory.

---

# 1. Truncation error

The truncation error is

\[
T_{ij}^{(N)}.
\]

It measures the error from replacing the infinite Weil/Bombieri form with a finite approximation.

## Classification

\[
T_{ij}^{(N)}
=
\text{CLASSICAL-SOURCE DEPENDENT}
\]

## Why

This term depends on the true infinite form \(Q_W\), the true finite approximation \(Q_N^W\), and the classical limiting process.

The project cannot honestly bound this term until the exact classical form and finite truncation scheme are imported.

## Current status

TRUNCATION_ERROR_CLASSICAL_SOURCE_DEPENDENT

UNRESOLVED_UNTIL_CLASSICAL_IMPORT

---

# 2. Projection error

The projection error is

\[
P_{ij}^{(N)}.
\]

It measures the error caused by mapping test functions into the finite space:

\[
P_N^W:\mathcal D_W\to V_N^W.
\]

## Classification

\[
P_{ij}^{(N)}
=
\text{CLASSICAL + PROJECT DEPENDENT}
\]

## Why

If the projection map \(P_N^W\) is classical, the project must import it.

If the projection map is project-defined, the project must prove it approximates the relevant test functions correctly.

## Current status

PROJECTION_ERROR_CLASSICAL_OR_PROJECT_DEPENDENT

APPROXIMATION_MAP_STILL_MISSING

---

# 3. Kernel/model error

The kernel/model error is

\[
K_{ij}^{(N)}.
\]

It measures mismatch between the finite kernel used in the project and the true classical kernel/form.

## Classification

\[
K_{ij}^{(N)}
=
\text{PROJECT-CONTROLLABLE ONLY AFTER CLASSICAL VALIDATION}
\]

## Why

The project has developed an explicit finite \(H\)-kernel and Lipschitz constants. But this term can be controlled only after verifying that the finite \(H\)-kernel is exactly the correct classical object or after bounding the mismatch.

## Current status

KERNEL_MODEL_ERROR_REQUIRES_CLASSICAL_VALIDATION

FINITE_H_KERNEL_NOT_YET_CLASSICALLY_VALIDATED

---

# 4. Computational error

The computational error is

\[
C_{ij}^{(N)}.
\]

It measures floating-point, rounding, implementation, matrix assembly, and numerical approximation error.

## Classification

\[
C_{ij}^{(N)}
=
\text{PROJECT-CONTROLLABLE}
\]

## Why

This term can be controlled with:

1. interval arithmetic;
2. rational arithmetic where possible;
3. high precision arithmetic;
4. reproducible scripts;
5. matrix assembly audits;
6. independent verification.

## Current status

COMPUTATIONAL_ERROR_PROJECT_CONTROLLABLE

CERTIFIED_NUMERICS_POSSIBLE

---

# 5. Error classification table

| Error term | Meaning | Classification | Current status |
|---|---|---|---|
| \(T_{ij}^{(N)}\) | infinite-to-finite truncation error | classical-source dependent | unresolved |
| \(P_{ij}^{(N)}\) | approximation/projection error | classical or project dependent | unresolved |
| \(K_{ij}^{(N)}\) | kernel/model mismatch error | project-controllable after classical validation | unresolved |
| \(C_{ij}^{(N)}\) | numerical/computational error | project-controllable | controllable in principle |

---

# 6. What the project can attack first

The safest immediately attackable term is:

\[
C_{ij}^{(N)}.
\]

This means the project can build a certified numerical layer.

The second attackable term is:

\[
K_{ij}^{(N)}.
\]

But only after verifying whether the project \(H\)-kernel matches the classical finite kernel.

The hardest terms are:

\[
T_{ij}^{(N)}
\quad\text{and}\quad
P_{ij}^{(N)}.
\]

These require exact classical definitions.

---

# 7. Strategic consequence

The next contribution should not pretend to prove the full convergence theorem.

The next contribution should prove a conditional theorem:

If the classical truncation and projection errors satisfy bounds

\[
|T_{ij}^{(N)}|\leq\tau_N^{(m)}
\]

and

\[
|P_{ij}^{(N)}|\leq\pi_N^{(m)},
\]

and if kernel/model and computation errors satisfy

\[
|K_{ij}^{(N)}|\leq\kappa_N^{(m)}
\]

and

\[
|C_{ij}^{(N)}|\leq\chi_N^{(m)},
\]

then finite-class convergence follows with explicit bound:

\[
R^2m
\left(
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\kappa_N^{(m)}
+
\chi_N^{(m)}
\right).
\]

This conditional theorem is a real next contribution candidate.

---

# 8. Next target

Phase 10AT should prove the conditional Gram-error-to-transfer theorem.

This will combine:

1. Gram error decomposition;
2. finite-class convergence;
3. certified finite negativity;
4. explicit stability margins.

The result will still be conditional, but it will be a serious architecture theorem.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove classical convergence.

This phase does not claim novelty.

Exact audit strings:

GRAM_ERROR_CLASSIFICATION

TRUNCATION_ERROR_CLASSICAL_SOURCE_DEPENDENT

PROJECTION_ERROR_CLASSICAL_OR_PROJECT_DEPENDENT

KERNEL_MODEL_ERROR_REQUIRES_CLASSICAL_VALIDATION

COMPUTATIONAL_ERROR_PROJECT_CONTROLLABLE

CERTIFIED_NUMERICS_POSSIBLE

CONDITIONAL_TRANSFER_THEOREM_NEXT

NOT_RH_CONTRIBUTION_YET

