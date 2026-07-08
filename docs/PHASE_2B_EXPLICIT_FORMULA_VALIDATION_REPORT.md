# Phase 2B Explicit-Formula Susceptibility Validation Report

## Objective

Independently validate the exact second derivative, quarter-turn susceptibility, native amplitude normalization, and mesoscopic scaling profile of the individual explicit-formula zero kernel

\[
p_L(z)
=
-\frac{e^{Lz}}{z}.
\]

---

# 1. Symbolic derivative validation

The kernel was independently differentiated using SymPy.

The symbolic second derivative agreed exactly with

\[
\boxed{
p_L''(z)
=
-e^{Lz}
\left(
\frac{L^2}{z}
-
\frac{2L}{z^2}
+
\frac2{z^3}
\right).
}
\]

Status:

VALIDATED.

---

# 2. Arbitrary-precision derivative validation

The manually derived second derivative was compared with direct numerical differentiation of the original kernel using mpmath at high working precision.

Multiple \(L\) and \(\gamma\) combinations were tested.

The implementation required relative agreement substantially beyond ordinary double-precision scale.

Status:

VALIDATED.

---

# 3. Quarter-turn directional contrast recovery

The degree-preserving horizontal-minus-vertical four-zero contrast was evaluated directly from the original explicit-formula kernel.

The normalized contrast

\[
\frac{
\mathcal A_{p_L}(\delta,\gamma)
}{
2\delta^2
}
\]

converged to

\[
\chi_L^{\mathrm{EF}}(\gamma)
=
2\Re p_L''
\left(
\frac12+i\gamma
\right).
\]

Status:

VALIDATED.

---

# 4. Exact critical-line amplitude normalization

On the critical line,

\[
e^{L\rho_\gamma}
=
e^{L/2}e^{iL\gamma}.
\]

Therefore the exact exponential modulus is

\[
e^{L/2}.
\]

The normalized susceptibility

\[
\widetilde\chi_L^{\mathrm{EF}}
=
e^{-L/2}
\chi_L^{\mathrm{EF}}
\]

removes this factor exactly.

The normalization audit directly reconstructed the phase-rational component after multiplying the complex second derivative by

\[
e^{-L/2}.
\]

Using an incorrect normalization exponent leaves a deterministic residual multiplicative scale.

Status:

VALIDATED.

---

# 5. Important normalization correction

An incorrect fixed amplitude exponent does not necessarily destroy the leading mesoscopic limit under

\[
L\gamma\to c,
\]

because this scaling implies

\[
L\to0.
\]

For fixed \(a\),

\[
e^{-aL}
e^{L/2}
=
e^{(1/2-a)L}
\to1.
\]

Therefore the exact normalization is analytically canonical at finite \(L\), but the leading phase-preserving scaling limit is insensitive to fixed normalization-exponent errors.

The project must not use the scaling collapse alone as evidence that the exact amplitude normalization is uniquely determined.

---

# 6. Mesoscopic scaling profile

For the amplitude-normalized susceptibility,

\[
\widetilde\chi_L^{\mathrm{EF}}(\gamma)
=
e^{-L/2}
\chi_L^{\mathrm{EF}}(\gamma),
\]

the project tested sequences satisfying

\[
L=\frac c\gamma.
\]

Thus

\[
L\gamma=c
\]

exactly.

The scaled response

\[
\gamma^3
\widetilde\chi_L^{\mathrm{EF}}(\gamma)
\]

converged toward

\[
\boxed{
\Psi_{\mathrm{EF}}(c)
=
-4c\cos c
+
2(2-c^2)\sin c.
}
\]

The campaign included multiple values of \(c\) and \(\gamma\) and recorded high-precision outputs, metadata, Git state, and output hashes.

Status:

VALIDATED.

---

# 7. Mathematical status

The project promotes the explicit-formula mesoscopic susceptibility scaling statement to PROVED IN PROJECT:

If

\[
\gamma_j\to\infty
\]

and

\[
L_j\gamma_j\to c>0,
\]

then

\[
\boxed{
\gamma_j^3
e^{-L_j/2}
\chi_{L_j}^{\mathrm{EF}}(\gamma_j)
\to
-4c\cos c
+
2(2-c^2)\sin c.
}
\]

The result concerns the individual analytic zero kernel

\[
-e^{Lz}/z.
\]

It is not a theorem about the complete explicit formula.

No originality claim is made.

---

# 8. Cross-diagnostic consequence

The project now has two independently validated susceptibility scaling families.

## Li kernel

Phase coordinate:

\[
\frac n\gamma.
\]

Height exponent:

\[
2.
\]

Profile:

\[
\Psi_{\mathrm{Li}}(c)
=
-2c(c\cos c+2\sin c).
\]

## Explicit-formula zero kernel

Phase coordinate:

\[
L\gamma.
\]

Height exponent:

\[
3.
\]

Profile:

\[
\Psi_{\mathrm{EF}}(c)
=
-4c\cos c
+
2(2-c^2)\sin c.
\]

This supports continued investigation of a susceptibility scaling taxonomy.

Two examples are insufficient to establish a general classification principle.

---

# 9. Remaining limitation

The project still studies individual zero kernels and finite four-zero contrasts.

It has not established a comparison of full RH-equivalent diagnostics under a shared resource or detection-cost model.

No implication for RH is claimed.
