# Explicit-Formula Zero-Kernel Susceptibility

## Phase 2A

This document derives the quarter-turn quadratic susceptibility of an individual zero kernel modeled on the zero contribution in the Riemann explicit formula.

---

# 1. Kernel

Let

\[
L>0.
\]

Define

\[
p_L(z)
=
-\frac{e^{Lz}}{z}.
\]

Equivalently, for

\[
x=e^L>1,
\]

one has

\[
p_L(z)
=
-\frac{x^z}{z}.
\]

This is the individual analytic zero kernel associated with the standard explicit-formula contribution

\[
-\frac{x^\rho}{\rho}.
\]

The present phase does not assert a result about the full explicit formula.

---

# 2. Second derivative

Starting from

\[
p_L(z)
=
-e^{Lz}z^{-1},
\]

one obtains

\[
p_L'(z)
=
-e^{Lz}
\left(
Lz^{-1}-z^{-2}
\right).
\]

Differentiating again gives

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

Equivalently,

\[
\boxed{
p_L''(z)
=
-e^{Lz}
\frac{
L^2z^2-2Lz+2
}{
z^3
}.
}
\]

---

# 3. Critical-line susceptibility

Let

\[
\rho_\gamma
=
\frac12+i\gamma.
\]

Define

\[
\chi_L^{\mathrm{EF}}(\gamma)
=
2\Re p_L''(\rho_\gamma).
\]

Then

\[
\boxed{
\chi_L^{\mathrm{EF}}(\gamma)
=
-2
\Re
\left[
e^{L\rho_\gamma}
\left(
\frac{L^2}{\rho_\gamma}
-
\frac{2L}{\rho_\gamma^2}
+
\frac2{\rho_\gamma^3}
\right)
\right].
}
\]

Since

\[
e^{L\rho_\gamma}
=
e^{L/2}e^{iL\gamma},
\]

one has

\[
\boxed{
\chi_L^{\mathrm{EF}}(\gamma)
=
-2e^{L/2}
\Re
\left[
e^{iL\gamma}
\left(
\frac{L^2}{\rho_\gamma}
-
\frac{2L}{\rho_\gamma^2}
+
\frac2{\rho_\gamma^3}
\right)
\right].
}
\]

---

# 4. Native amplitude normalization

On the critical line,

\[
|e^{L\rho_\gamma}|
=
e^{L/2}.
\]

Define the amplitude-normalized susceptibility

\[
\boxed{
\widetilde\chi_L^{\mathrm{EF}}(\gamma)
=
e^{-L/2}
\chi_L^{\mathrm{EF}}(\gamma).
}
\]

Thus

\[
\boxed{
\widetilde\chi_L^{\mathrm{EF}}(\gamma)
=
-2
\Re
\left[
e^{iL\gamma}
\left(
\frac{L^2}{\rho_\gamma}
-
\frac{2L}{\rho_\gamma^2}
+
\frac2{\rho_\gamma^3}
\right)
\right].
}
\]

This normalization removes the exact modulus of the exponential factor on the critical line.

---

# 5. Phase-preserving scaling regime

Suppose

\[
\gamma\to\infty
\]

and

\[
L=L(\gamma)>0
\]

satisfies

\[
L\gamma\to c
\]

for fixed

\[
c>0.
\]

Then

\[
e^{iL\gamma}\to e^{ic}.
\]

Also,

\[
\frac{\gamma}{\rho_\gamma}\to-i,
\]

\[
\frac{\gamma^2}{\rho_\gamma^2}\to-1,
\]

and

\[
\frac{\gamma^3}{\rho_\gamma^3}\to i.
\]

Therefore

\[
\gamma^3
\frac{L^2}{\rho_\gamma}
=
(L\gamma)^2
\frac{\gamma}{\rho_\gamma}
\to
-ic^2,
\]

\[
\gamma^3
\left(
-\frac{2L}{\rho_\gamma^2}
\right)
=
-2(L\gamma)
\frac{\gamma^2}{\rho_\gamma^2}
\to
2c,
\]

and

\[
\gamma^3
\frac2{\rho_\gamma^3}
\to
2i.
\]

Hence

\[
\boxed{
\gamma^3
\left(
\frac{L^2}{\rho_\gamma}
-
\frac{2L}{\rho_\gamma^2}
+
\frac2{\rho_\gamma^3}
\right)
\to
2c+i(2-c^2).
}
\]

---

# 6. Mesoscopic profile

It follows that

\[
\gamma^3
\widetilde\chi_L^{\mathrm{EF}}(\gamma)
\to
-2
\Re
\left[
e^{ic}
\left(
2c+i(2-c^2)
\right)
\right].
\]

Therefore

\[
\boxed{
\gamma^3
\widetilde\chi_L^{\mathrm{EF}}(\gamma)
\to
\Psi_{\mathrm{EF}}(c),
}
\]

where

\[
\boxed{
\Psi_{\mathrm{EF}}(c)
=
-4c\cos c
+
2(2-c^2)\sin c.
}
\]

---

# 7. Comparison with the Li kernel

For the individual Li kernel, the project proved a phase-preserving regime

\[
\frac n\gamma\to c
\]

and susceptibility scaling

\[
\gamma^2
\chi_n^{\mathrm{Li}}(\gamma)
\to
\Psi_{\mathrm{Li}}(c).
\]

For the explicit-formula zero kernel, after removal of the native critical-line exponential amplitude, the phase-preserving regime is

\[
L\gamma\to c
\]

and the candidate scaling is

\[
\gamma^3
\widetilde\chi_L^{\mathrm{EF}}(\gamma)
\to
\Psi_{\mathrm{EF}}(c).
\]

Thus the two kernel families exhibit different phase coordinates and different height-decay exponents.

---

# 8. Interpretation warning

The regime

\[
L\gamma\to c
\]

implies

\[
L\to0
\]

and

\[
x=e^L\to1^+.
\]

This is not asserted to be the standard large-\(x\) prime-counting regime of the explicit formula.

The result concerns the individual analytic zero kernel and its phase-preserving quarter-turn susceptibility.

No statement about prime detection power is currently made.

---

# 9. Candidate proposition status

The exact derivative and susceptibility formulas have been manually derived.

The phase-preserving scaling limit has a direct asymptotic derivation.

Neither is yet promoted to PROVED IN PROJECT.

Independent symbolic differentiation and arbitrary-precision scaling validation are required.

No originality claim is made.
