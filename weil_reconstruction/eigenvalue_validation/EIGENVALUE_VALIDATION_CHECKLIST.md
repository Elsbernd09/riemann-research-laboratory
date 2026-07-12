# Eigenvalue Validation Checklist

## Stage A — Hermitian gate

- [ ] Assemble candidate raw full matrix.
- [ ] Assemble candidate distinct weighted matrix.
- [ ] Assemble candidate similarity-symmetrized matrix.
- [ ] Compute Hermitian residuals.
- [ ] Choose representation only if residual is acceptable.

Status: NOT STARTED.

---

## Stage B — Synthetic cases

- [ ] All real \(\gamma\)-values.
- [ ] One non-real conjugate pair.
- [ ] Two non-real conjugate pairs.
- [ ] Repeated real values.
- [ ] Repeated non-real conjugate pair.

Status: NOT STARTED.

---

## Stage C — Negative eigenvalue counting rule

- [ ] Set tolerance \(\tau\).
- [ ] Count \(\lambda<-\tau\) as negative.
- [ ] Count \(|\lambda|\le\tau\) as numerical zero.
- [ ] Record ambiguous cases.

Status: NOT STARTED.

---

## Stage D — Theorem 8 comparison

- [ ] Count expected distinct conjugate pairs.
- [ ] Count numerical negative eigenvalues.
- [ ] Compare case by case.
- [ ] Log failures honestly.

Status: NOT STARTED.

---

## Stage E — Boundary enforcement

- [ ] No zeta zeros.
- [ ] No RH claims.
- [ ] No novelty claims.
- [ ] No publication claims from synthetic tests.

Status: REQUIRED.

