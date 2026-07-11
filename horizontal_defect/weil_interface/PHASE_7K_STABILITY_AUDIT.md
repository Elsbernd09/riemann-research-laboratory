# Phase 7K — Stability Audit Across Heights and Basis Choices

## Purpose

Phase 7J found that the second-order centered finite-rank signal

\[
B_m(\gamma)
=
\lim_{x\to0}
\frac{C_m(x,\gamma)}{x^2}
\]

shows both positive and negative Rayleigh directions in several tested configurations.

Phase 7K stress-tests whether that diagnostic behavior is stable across:

1. different heights \(\gamma\);
2. different finite degrees \(m\);
3. different feature bases.

This is not a Weil theorem.

This is not a proof of RH.

It is a diagnostic stability audit.

---

# 1. Feature bases tested

The audit tested four finite bases:

## Power basis

\[
\varphi_k(\rho)=w^k,
\qquad
w=1-\frac1\rho.
\]

## Shifted power basis

\[
\varphi_k(\rho)=(w-1)^k.
\]

## Reciprocal basis

\[
\varphi_k(\rho)=\rho^{-k}.
\]

## Hybrid basis

\[
\varphi_k(\rho)=w^k+\rho^{-k}.
\]

---

# 2. Audit outcome

The audit found a mixed result.

Some bases showed both positive and negative Rayleigh directions across the tested heights and degrees.

Other bases, especially the shifted basis, produced mostly one-sign behavior under the deterministic Rayleigh scan.

Thus the diagnostic indefiniteness observed in Phase 7J is not basis-universal in this toy finite-rank laboratory.

---

# 3. Correct conclusion

The correct conclusion is not:

\[
\text{indefiniteness is universally stable.}
\]

The correct conclusion is:

\[
\boxed{
\text{second-order sign behavior is strongly basis-dependent.}
}
\]

This is important because a genuine Weil-compatible construction cannot rely on arbitrary basis-dependent toy behavior.

---

# 4. Research meaning

The mixed outcome sharpens the next problem.

We must identify whether there is a mathematically canonical basis or quadratic form in which horizontal displacement creates a reliable negative direction.

Without a canonical Weil-compatible structure, the toy finite-rank signals remain diagnostic only.

---

# 5. Boundary

This audit does not prove:

1. global basis-independent indefiniteness;
2. convergence to a classical Weil quadratic form;
3. arithmetic-side control;
4. RH.

It records a basis-dependence obstruction.

---

# 6. Next target

The next phase should synthesize Phase 7A through Phase 7K and state the honest result:

- scalar counting is horizontally blind;
- linear Li filters are obstructed;
- radial defect is positive but not arithmetic-side compatible;
- quadratic Li filters give local positivity;
- finite-rank toy models detect horizontal displacement;
- second-order toy indefiniteness is basis-dependent.

