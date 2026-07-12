# Phase 8P — Fourier-Side Infinite Quadratic Form Extraction Worksheet

## Purpose

Phase 8O source-locked the roadmap for Bombieri's finite truncation program.

Phase 8P prepares the extraction of the Fourier-side infinite quadratic form from Bombieri Sections 5 and 6.

This phase does not implement a matrix.

This phase does not compute eigenvalues.

This phase does not prove RH.

This phase does not claim a new Weil criterion.

---

# 1. Why this phase comes before Section 8

Bombieri's Section 8 finite approximations approximate an earlier Fourier-side reformulation.

Therefore, before extracting finite matrices, the project must extract the infinite object being approximated.

The correct order is:

\[
\text{Weil functional}
\rightarrow
\text{Fourier-side infinite quadratic form}
\rightarrow
\text{finite approximation}
\rightarrow
\text{matrix entries}
\rightarrow
\text{eigenvalues}.
\]

Skipping the Fourier-side object would risk creating another toy matrix.

---

# 2. Extraction target

The next source target is Bombieri Sections 5 and 6.

The extraction must identify:

1. the Fourier transform convention;
2. the function space or Hilbert space;
3. the variables used in the infinite quadratic form;
4. the exact quadratic form;
5. the eigenvalue problem;
6. the symmetry decomposition, if any;
7. the relation between the Fourier-side form and \(T[f*f^*]\);
8. the notation used later in Section 8.

---

# 3. Required source fields

## Source location

Record:

- paper;
- section;
- page;
- displayed equation number if available;
- theorem/proposition/lemma number if available.

## Transform convention

Record:

- Fourier transform definition;
- inverse transform definition;
- signs;
- constants;
- real/complex convention.

## Function space

Record:

- domain;
- inner product;
- norm;
- support restrictions;
- parity restrictions;
- smoothness or decay assumptions.

## Infinite quadratic form

Record exact source formula.

Do not translate to project notation until the original source formula is recorded.

## Eigenvalue problem

Record:

- operator or quadratic form;
- eigenvalue parameter;
- variational formulation;
- odd/even decomposition if present.

## Link to finite approximation

Record the notation that Section 8 later truncates.

---

# 4. Current status

## LOCKED

Bombieri \(T[f]\) formula.

Bombieri positivity object:

\[
T[f*f^*].
\]

Hermitian positivity star convention.

Source roadmap for Sections 5–6 and Section 8.

## UNLOCKED

Fourier transform convention.

Infinite quadratic form.

Hilbert/function space.

Eigenvalue problem.

Section 8 truncation variables.

Matrix entries.

---

# 5. Worksheet

## Fourier transform convention

Original source formula:

UNFILLED.

Project notation translation:

BLOCKED.

Status:

UNLOCKED.

---

## Function space

Original source definition:

UNFILLED.

Project notation translation:

BLOCKED.

Status:

UNLOCKED.

---

## Infinite quadratic form

Original source formula:

UNFILLED.

Project notation translation:

BLOCKED.

Status:

UNLOCKED.

---

## Eigenvalue problem

Original source statement:

UNFILLED.

Project notation translation:

BLOCKED.

Status:

UNLOCKED.

---

## Link to Section 8 finite approximation

Original source notation:

UNFILLED.

Project notation translation:

BLOCKED.

Status:

UNLOCKED.

---

# 6. Permission status

FOURIER_SIDE_EXTRACTION_PERMISSION: GRANTED.

FOURIER_SIDE_SYMBOLIC_SUMMARY_PERMISSION: GRANTED.

FOURIER_SIDE_IMPLEMENTATION_PERMISSION: DENIED.

FINITE_MATRIX_IMPLEMENTATION_PERMISSION: DENIED.

EIGENVALUE_COMPUTATION_PERMISSION: DENIED.

---

# 7. Boundary

No matrix code.

No eigenvalue computation.

No finite-rank Weil implementation.

No RH proof.

No novelty claim.

