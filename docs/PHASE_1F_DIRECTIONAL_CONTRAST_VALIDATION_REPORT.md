# Phase 1F Directional Contrast Validation Report

## Objective

Validate the horizontal-versus-vertical finite four-zero contrast and determine the true leading error order in the susceptibility approximation.

---

# 1. Previous remainder estimate

Phase 1E established

\[
\mathcal A_f(\delta,\gamma)
=
2\delta^2\chi_f(\gamma)
+
O(\delta^4).
\]

This estimate was correct but not sharp.

---

# 2. Quarter-turn derivative filtering

Horizontal symmetric displacement contributes even Taylor derivatives with factors

\[
\delta^{2m}.
\]

Vertical symmetric displacement contributes factors

\[
(i\delta)^{2m}
=
(-1)^m\delta^{2m}.
\]

Therefore horizontal-minus-vertical contrast weights derivative order \(2m\) by

\[
1-(-1)^m.
\]

Terms with even \(m\) cancel.

Terms with odd \(m\) survive.

Thus only derivative orders

\[
4k+2
\]

remain.

For one center,

\[
A_f^{(\rho)}(\delta)
=
4
\sum_{k\ge0}
\frac{
\delta^{4k+2}
}{
(4k+2)!
}
f^{(4k+2)}(\rho).
\]

For the conjugate critical-line pair,

\[
\mathcal A_f(\delta,\gamma)
=
8
\sum_{k\ge0}
\frac{
\delta^{4k+2}
}{
(4k+2)!
}
\Re
f^{(4k+2)}
\left(
\frac12+i\gamma
\right).
\]

---

# 3. Sharpened local expansion

The first term is

\[
2\delta^2\chi_f(\gamma).
\]

The fourth-order term vanishes exactly.

The next surviving term is sixth order:

\[
\boxed{
\mathcal A_f(\delta,\gamma)
=
2\delta^2\chi_f(\gamma)
+
\frac{\delta^6}{90}
\Re
f^{(6)}
\left(
\frac12+i\gamma
\right)
+
O(\delta^{10}).
}
\]

Thus the susceptibility estimator

\[
\frac{
\mathcal A_f(\delta,\gamma)
}{
2\delta^2
}
\]

has leading error of order

\[
\delta^4,
\]

even though the contrast itself has leading residual of order

\[
\delta^6.
\]

---

# 4. Symbolic validation

A symbolic Taylor model was constructed with independent formal derivative symbols.

The horizontal-minus-vertical contrast was expanded through derivative order 14.

Only derivative orders

\[
2,\ 6,\ 10,\ 14
\]

survived.

Orders

\[
0,\ 4,\ 8,\ 12
\]

cancelled exactly.

Status:

VALIDATED.

---

# 5. Arbitrary-precision Li-kernel validation

The degree-preserving four-zero contrast

\[
\sum_{H_{\delta,\gamma}}f_n
-
\sum_{V_{\delta,\gamma}}f_n
\]

was evaluated using arbitrary-precision arithmetic.

After division by

\[
2\delta^2,
\]

the contrast converged to the exact Li-kernel susceptibility.

Status:

VALIDATED.

---

# 6. Sixth-order residual validation

The residual

\[
\mathcal A_{f_n}(\delta,\gamma)
-
2\delta^2\chi_n^{\mathrm{Li}}(\gamma)
\]

was divided by

\[
\delta^6.
\]

The scaled residual converged to

\[
\boxed{
\frac1{90}
\Re
f_n^{(6)}
\left(
\frac12+i\gamma
\right).
}
\]

This was tested across multiple \(n\) and \(\gamma\) cases using high working precision.

A reproducible campaign is stored in

`results/li_directional_contrast_sixth_order/`.

---

# 7. Mathematical status

The project promotes the quarter-turn directional contrast expansion to PROVED IN PROJECT.

The result is a local complex-analytic identity for the finite zero-configuration contrast defined by the project.

The root-of-unity filtering mechanism underlying the derivative cancellation is standard mathematics and is not asserted to be novel.

The application to the project's Li susceptibility architecture has not undergone a complete literature originality audit.

---

# 8. Research interpretation

The finite four-zero horizontal-versus-vertical contrast does more than preserve multiplicity.

It filters the local analytic derivative hierarchy.

Derivative orders congruent to

\[
0\pmod4
\]

cancel from the nonconstant even expansion.

Derivative orders congruent to

\[
2\pmod4
\]

survive.

The quadratic susceptibility is therefore the first coefficient in a structured sequence of quarter-turn contrast responses.

---

# 9. Remaining limitation

The contrast remains a finite-factor analytic construction.

It has not been promoted to an arithmetic deformation of the Riemann xi-function.

No implication for RH is claimed.
