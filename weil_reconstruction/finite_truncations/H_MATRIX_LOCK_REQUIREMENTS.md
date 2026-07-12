# H-Matrix Lock Requirements

## Status update

The formula-level kernel extraction for

\[
H(\gamma,\gamma';t)
\]

has been completed at source-note level.

Bombieri Theorem 8 has also been extracted at statement level.

H_MATRIX_FORMULA_STATUS: PARTIAL_LOCKED.

THEOREM8_STATEMENT_STATUS: LOCKED.

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

## 5. Theorem 8 statement

The number of negative eigenvalues of \(H(\Gamma;t)\) equals the number of distinct complex conjugate pairs in \(\Gamma\).

Status: LOCKED at statement level.

---

# Still required before implementation

## 1. Code-normalization audit

Status: UNLOCKED.

## 2. Stable handling of \(K(0)=1\)

Status: UNLOCKED.

## 3. Complex arithmetic convention

Status: UNLOCKED.

## 4. Repeated-\(\gamma\) multiplicity handling

Status: PARTIAL.

## 5. Distinct weighted matrix implementation rule

Status: PARTIAL.

## 6. Hermitian or real-symmetric conversion

Status: UNLOCKED.

## 7. Validation test against Theorem 8 on synthetic finite multisets

Status: UNLOCKED.

---

# Current permission

SYMBOLIC H-KERNEL NOTES: ALLOWED.

THEOREM 8 STATEMENT NOTES: ALLOWED.

H_MATRIX_IMPLEMENTATION_PERMISSION: DENIED.

EIGENVALUE_COMPUTATION_PERMISSION: DENIED.

