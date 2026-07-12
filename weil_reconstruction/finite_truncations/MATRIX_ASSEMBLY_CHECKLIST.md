# Matrix Assembly Checklist

## Stage A — Synthetic Gamma data model

- [ ] Store full multiset values.
- [ ] Store distinct values.
- [ ] Store multiplicities.
- [ ] Count repeated-value zero-eigenvalue warning.
- [ ] Count distinct complex conjugate pairs.
- [ ] Explicitly reject zeta-zero input.

Status: NOT STARTED.

---

## Stage B — Full multiset matrix

- [ ] Assemble \(A_{jk}=H(\gamma_j,\gamma_k;t)\).
- [ ] Check matrix shape.
- [ ] Check all entries finite.
- [ ] Check repeated rows/columns when gamma values repeat.
- [ ] Do not compute eigenvalues.

Status: NOT STARTED.

---

## Stage C — Distinct weighted matrix

- [ ] Assemble \(B_{jk}=H(\gamma_j,\gamma_k;t)m(\gamma_k)\).
- [ ] Check matrix shape.
- [ ] Check all entries finite.
- [ ] Check column weights match multiplicity table.
- [ ] Do not compute eigenvalues.

Status: NOT STARTED.

---

## Stage D — Symmetry audit

- [ ] Inspect raw Hermitian residual.
- [ ] Inspect weighted Hermitian residual.
- [ ] Inspect similarity-symmetrized residual.
- [ ] Do not compute eigenvalues.

Status: NOT STARTED.

---

## Stage E — Next permission gate

- [ ] Only after Stages A-D pass, create eigenvalue-validation phase.
- [ ] Synthetic finite multisets only.
- [ ] No zeta-zero experiments until Sections 10 and 11 are source-extracted.

Status: BLOCKED.

