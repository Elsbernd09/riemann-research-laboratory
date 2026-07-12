# H-Kernel Implementation Audit Checklist

## Stage A — Kernel functions

- [ ] Implement stable \(K(z)=\sin z/z\).
- [ ] Implement \(K_t(z)=K(tz)\).
- [ ] Implement \(K^*(x,y;t)\).
- [ ] Implement \(H(x,y;t)=2tK^*(x,y;t)/(1/4+y^2)\).
- [ ] No eigenvalue computation.

Status: NOT STARTED.

---

## Stage B — Sanity checks

- [ ] Check \(K(0)=1\).
- [ ] Check evenness \(K(-z)=K(z)\).
- [ ] Check finite values for complex samples.
- [ ] Check diagonal finiteness.
- [ ] Inspect conjugate symmetry.

Status: NOT STARTED.

---

## Stage C — Multiplicity representation

- [ ] Full multiset representation documented.
- [ ] Distinct weighted representation documented.
- [ ] Repeated-\(\gamma\) zero-eigenvalue convention documented.

Status: NOT STARTED.

---

## Stage D — Hermitian conversion

- [ ] Raw matrix symmetry inspected.
- [ ] Weighted similarity transform considered.
- [ ] Hermitian matrix convention locked.

Status: NOT STARTED.

---

## Stage E — Synthetic Theorem 8 validation

- [ ] Synthetic \(\Gamma\) with all real entries.
- [ ] Synthetic \(\Gamma\) with one non-real conjugate pair.
- [ ] Synthetic \(\Gamma\) with multiple non-real conjugate pairs.
- [ ] Synthetic repeated-\(\gamma\) case.
- [ ] Validate negative eigenvalue count only after Hermitian convention is locked.

Status: BLOCKED UNTIL STAGES A-D PASS.

---

# Permission

H_KERNEL_SYMBOLIC_IMPLEMENTATION_NEXT_PHASE: ALLOWED.

EIGENVALUE_COMPUTATION: DENIED.

ZETA_ZERO_EXPERIMENTS: DENIED.

