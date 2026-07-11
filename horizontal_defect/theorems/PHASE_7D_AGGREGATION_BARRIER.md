# Phase 7D — Aggregation Barrier for Radial Defect Energy

## Purpose

Phase 7C constructed the positive single-zero radial Li-coordinate defect

\[
D_{\mathrm{rad}}(\rho)
=
\left(\log |1-1/\rho|\right)^2.
\]

It is nonnegative and vanishes exactly on the critical line.

This phase studies aggregation over many zeros.

The key conclusion is:

\[
\boxed{
\text{Positive aggregation is easy. Arithmetic-side control is hard.}
}
\]

This phase does not prove RH.

It identifies the next major obstruction.

---

# 1. Positive weighted aggregation

Let \(\Omega\) be a finite multiset of zero candidates

\[
\rho_j=\beta_j+i\gamma_j
\]

with \(\gamma_j\ne0\).

Let \(w_j>0\) be positive weights.

Define

\[
\mathcal D_{\mathrm{rad}}(\Omega)
=
\sum_{\rho_j\in\Omega}
w_j
\left(\log |1-1/\rho_j|\right)^2.
\]

Then

\[
\mathcal D_{\mathrm{rad}}(\Omega)\ge0.
\]

Moreover,

\[
\mathcal D_{\mathrm{rad}}(\Omega)=0
\]

if and only if

\[
\Re(\rho_j)=\frac12
\]

for every \(\rho_j\in\Omega\).

Thus finite positive aggregation preserves faithful horizontal detection.

---

# 2. Proof

Each summand satisfies

\[
\left(\log |1-1/\rho_j|\right)^2\ge0.
\]

Since \(w_j>0\), every weighted summand is nonnegative.

Therefore the sum is nonnegative.

The sum is zero if and only if every summand is zero.

By Phase 7C, each summand vanishes if and only if

\[
\Re(\rho_j)=\frac12.
\]

This proves the claim.

---

# 3. Infinite aggregation warning

For an infinite zero set, the formal expression

\[
\sum_\rho
\phi(\gamma_\rho)
\left(\log |1-1/\rho|\right)^2
\]

requires a convergence rule.

If

\[
\phi(\gamma)>0
\]

and the sum converges absolutely, then vanishing of the sum still forces every included zero to lie on the critical line.

However, this is mostly tautological unless the sum can be evaluated, bounded, or transformed using independent information.

---

# 4. Why this does not prove RH

Define

\[
\mathcal D_\phi
=
\sum_\rho
\phi(\gamma_\rho)
\left(\log |1-1/\rho|\right)^2.
\]

If \(\phi>0\) and the sum is well-defined, then

\[
\mathcal D_\phi=0
\]

is equivalent to the assertion that all included zeros lie on the critical line.

But this does not prove RH because we have not shown

\[
\mathcal D_\phi=0.
\]

We have only defined a nonnegative quantity that would vanish if RH holds.

The difficult part is not positivity.

The difficult part is proving vanishing or deriving an arithmetic-side identity strong enough to force vanishing.

---

# 5. Aggregation barrier

The radial defect energy is nonlinear in zero position:

\[
\left(\log |1-1/\rho|\right)^2.
\]

Classical explicit formulae are naturally linear sums over zeros of test functions:

\[
\sum_\rho h(\rho).
\]

Quadratic or nonlinear defect energies do not automatically appear as a standard Weil/Guinand zero-side expression.

Therefore the barrier is:

\[
\boxed{
\text{Find an explicit-formula-compatible representation of a positive horizontal-defect energy.}
}
\]

Without this bridge, the radial defect energy remains diagnostic rather than arithmetic.

---

# 6. The actual next problem

The next research problem is not to define more positive energies.

The next research problem is:

\[
\boxed{
\text{Can a positive horizontal-defect energy be represented by, bounded by, or approximated through a Weil-positive test family?}
}
\]

This creates three possible paths:

1. Exact representation;
2. upper/lower comparison with a Weil quadratic form;
3. finite-rank approximation with convergence guarantees.

---

# 7. Phase conclusion

Positive aggregation of the radial defect energy is mathematically straightforward.

The obstruction is explicit-formula compatibility.

This phase records the aggregation barrier and prevents the project from mistaking a tautological RH-equivalent defect sum for a proof.

