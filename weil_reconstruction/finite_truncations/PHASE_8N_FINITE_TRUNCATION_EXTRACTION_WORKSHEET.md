# Phase 8N — Finite Truncation Extraction Worksheet

## Purpose

Phase 8M recorded the off-critical negative-direction mechanism at statement level.

Phase 8N prepares the source-grounded extraction of Bombieri's finite truncation construction.

This phase does not implement a matrix.

This phase does not compute eigenvalues.

This phase does not prove RH.

This phase does not claim a new Weil criterion.

---

# 1. Why this phase is necessary

The project now knows the symbolic Bombieri-Weil object:

\[
T[f*f^*].
\]

It also knows the high-level source claim that finite truncations and negative eigenvalues are studied in Bombieri's framework.

However, the project does not yet know the exact finite truncation construction.

Therefore, any code written now would risk being another toy model.

The purpose of this phase is to prevent that.

---

# 2. Extraction target

The next source-extraction target is Bombieri's finite-dimensional approximation to the Weil quadratic form.

The extraction must identify:

1. the infinite quadratic form;
2. the variable basis;
3. the indexing set;
4. the matrix entries;
5. the truncation parameter;
6. the finite matrix definition;
7. the eigenvalue theorem;
8. the relationship between negative eigenvalues and off-critical zeros;
9. assumptions such as finite off-critical zero count;
10. convergence or stabilization statements.

---

# 3. Required source fields

For each finite-truncation statement, record:

## Source identity

- author;
- paper;
- section;
- page;
- equation number;
- theorem/proposition number.

## Infinite object

Record the exact infinite quadratic form.

## Basis

Record the exact variables or basis elements used.

## Matrix entries

Record the exact formula for each entry.

## Truncation rule

Record whether truncation means:

- first \(N\) variables;
- bounded index set;
- finite principal minor;
- finite-rank projection;
- another construction.

## Eigenvalue theorem

Record the exact statement involving negative eigenvalues.

## Off-critical zero relation

Record the exact relationship between:

\[
\#\{\text{negative eigenvalues}\}
\]

and

\[
\#\{\text{zeros failing RH}\}.
\]

## Assumptions

Record whether the theorem assumes:

- RH false;
- finitely many off-critical zeros;
- simplicity;
- multiplicity conditions;
- sufficiently large truncation;
- symmetry of zero set;
- other analytic hypotheses.

---

# 4. Current status

## LOCKED

Bombieri \(T[f]\) functional.

Bombieri positivity object:

\[
T[f*f^*].
\]

Hermitian positivity mechanism.

Off-critical square-norm failure mechanism.

## UNLOCKED

Finite truncation model.

Infinite quadratic form variables.

Matrix entries.

Truncation parameter.

Eigenvalue theorem number.

Negative eigenvalue count theorem.

Implementation permission.

---

# 5. Worksheet

## Source location

Source:

Bombieri, Remarks on Weil's quadratic functional in the theory of prime numbers, I.

Section:

TBD.

Page:

TBD.

Theorem/proposition/equation:

TBD.

Status:

UNFILLED.

---

## Infinite quadratic form

Original source formula:

UNFILLED.

Project notation translation:

BLOCKED.

Status:

UNLOCKED.

---

## Finite truncation

Original source definition:

UNFILLED.

Project notation translation:

BLOCKED.

Status:

UNLOCKED.

---

## Matrix entries

Original source formula:

UNFILLED.

Project notation translation:

BLOCKED.

Status:

UNLOCKED.

---

## Eigenvalue statement

Original source statement:

UNFILLED.

Project notation translation:

BLOCKED.

Status:

UNLOCKED.

---

## Off-critical zero count relationship

Original source statement:

UNFILLED.

Project notation translation:

BLOCKED.

Status:

UNLOCKED.

---

# 6. Permission status

FINITE_TRUNCATION_EXTRACTION_PERMISSION: GRANTED.

SYMBOLIC SUMMARY_PERMISSION: GRANTED.

CLASSICAL_WEIL_MATRIX_IMPLEMENTATION_PERMISSION: DENIED.

EIGENVALUE_COMPUTATION_PERMISSION: DENIED.

TOY_MODEL_COMPARISON_PERMISSION: DENIED.

---

# 7. Next phase

The next phase must fill this worksheet from the Bombieri source.

No matrix code should be written before that extraction is complete.

