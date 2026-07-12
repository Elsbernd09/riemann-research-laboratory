# Representation Normalization Decision Rule

## Status values

### PRELIMINARY_SYNTHETIC_LOCK_POSSIBLE

Use only if:

1. every synthetic case passes the Hermitian gate;
2. every synthetic case matches the expected Theorem 8 negative-count target;
3. no blocked case occurs;
4. no mismatch occurs.

This is still only synthetic finite validation.

---

### REPRESENTATION_NOT_LOCKED

Use if:

1. any Hermitian gate blocks;
2. any expected count mismatches;
3. any numerical ambiguity invalidates the count;
4. any representation choice is inconsistent across cases.

---

# Boundary

Neither status proves RH.

Neither status applies to zeta zeros.

Neither status replaces Bombieri Sections 10 and 11.

