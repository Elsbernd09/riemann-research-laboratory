# H-Matrix Lock Requirements

## Status update

The formula-level kernel extraction for

\[
H(\gamma,\gamma';t)
\]

has been completed at source-note level.

H_MATRIX_FORMULA_STATUS: PARTIAL_LOCKED.

H_MATRIX_IMPLEMENTATION_PERMISSION: DENIED.

EIGENVALUE_COMPUTATION_PERMISSION: DENIED.

---

# Locked

## 1. Base kernel

\[
K(x)=\frac{\sin x}{x}.
\]

Status: LOCKED.

## 2. Scaled kernel

\[
K_t(x)=K(tx).
\]

Status: LOCKED.

## 3. Corrected kernel

\[
K^*(x,y;t)
\]

Status: LOCKED at formula-note level.

## 4. H kernel

\[
H(x,y;t)=\frac{2tK^*(x,y;t)}{1/4+y^2}.
\]

Status: LOCKED at formula-note level.

---

# Still required before implementation

## 1. Exact finite matrix convention

Status: UNLOCKED.

## 2. Boundary-condition handling in finite matrix coordinates

Status: UNLOCKED.

## 3. Hermitian or real-symmetric normalization

Status: PARTIAL.

## 4. Multiplicity convention in matrix rows and columns

Status: PARTIAL.

## 5. Theorem 8 statement

Status: UNLOCKED.

## 6. Eigenvalue interpretation

Status: UNLOCKED.

---

# Current permission

SYMBOLIC H-KERNEL NOTES: ALLOWED.

H_MATRIX_IMPLEMENTATION_PERMISSION: DENIED.

EIGENVALUE_COMPUTATION_PERMISSION: DENIED.

