# Finite Truncation Lock Status

## Current status

FINITE_TRUNCATION_MODEL: UNLOCKED.

FINITE_MATRIX_ENTRIES: UNLOCKED.

NEGATIVE_EIGENVALUE_THEOREM_LOCATION: UNLOCKED.

EIGENVALUE_COMPUTATION_PERMISSION: DENIED.

CLASSICAL_WEIL_MATRIX_IMPLEMENTATION_PERMISSION: DENIED.

---

# What is known at statement level

Bombieri's framework studies finite truncations and negative eigenvalues of the associated quadratic form.

Under a finite off-critical zero hypothesis, sufficiently large truncations detect negative eigenvalues related to the number of zeros failing RH.

---

# What must be extracted next

1. exact section/page/theorem location;
2. infinite quadratic form notation;
3. finite truncation definition;
4. matrix entries;
5. eigenvalue theorem statement;
6. proof dependency;
7. assumptions on off-critical zeros;
8. relationship between negative eigenvalue count and zero count.

---

# Rule

No code may compute a matrix and call it a Bombieri-Weil truncation until all required finite-truncation rows are LOCKED.

