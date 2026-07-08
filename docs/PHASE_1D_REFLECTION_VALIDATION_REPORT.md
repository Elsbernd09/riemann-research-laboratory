# Phase 1D Reflection Validation Report

## Objective

Adversarially validate the Phase 1C claim that reflection symmetry mediates the equality between the standard Li zero-kernel response and the finite-factor derivative-side response.

---

# 1. Symbolic reflection identity

The project defines

\[
f_n(z)
=
1-
\left(
1-\frac1z
\right)^n
\]

and

\[
g_n(z)
=
1-
\left(
1-\frac1z
\right)^{-n}.
\]

Symbolic simplification independently verified

\[
\boxed{
g_n(z)=f_n(1-z).
}
\]

Status:

VALIDATED.

---

# 2. Single-factor derivative-side kernel

For

\[
F_\rho(s)
=
1-\frac{s}{\rho},
\]

the finite Li-type functional

\[
\mathscr L_n[F_\rho]
=
\frac1{(n-1)!}
\left.
\frac{d^n}{ds^n}
\left[
s^{n-1}\log F_\rho(s)
\right]
\right|_{s=1}
\]

was evaluated independently with symbolic differentiation for fixed integers

\[
1\le n\le20.
\]

The derived values agreed with

\[
g_n(\rho)
=
1-
\left(
1-\frac1\rho
\right)^{-n}.
\]

These fixed-integer checks validate the implementation and the written general coefficient proof.

They are not substituted for the general proof.

Status:

VALIDATED.

---

# 3. Reflection-invariant orbit response

The standard zero-kernel response

\[
\int f_n\,d\nu_{\delta,\gamma}
\]

was compared with the inverse-phase derivative-side response

\[
\int g_n\,d\nu_{\delta,\gamma}
\]

at 120 decimal digits of working precision.

The signed orbit measure

\[
\nu_{\delta,\gamma}
\]

is invariant under

\[
z\mapsto1-z.
\]

The two responses agreed to the declared high-precision threshold across the tested parameter cases.

Status:

VALIDATED.

---

# 4. Negative control: reflection symmetry removed

The project deliberately evaluated the two kernel responses on finite signed measures that were not invariant under

\[
z\mapsto1-z.
\]

For example, the measure

\[
\mathfrak d_{0.5+h+i\gamma}
-
\mathfrak d_{0.5+i\gamma}
\]

does not contain the reflected partners required for reflection invariance.

The standard-kernel and inverse-phase-kernel responses generally differed.

This negative control supports the mechanism predicted by the Phase 1C proof:

the orbit-level bridge is symmetry mediated.

The experiment does not establish that reflection invariance is a necessary condition for equality in every isolated case.

It establishes that removing the symmetry can and generally does break the equality.

---

# 5. Mathematical status

The project promotes the following statement to PROVED IN PROJECT:

Let

\[
\nu
\]

be a finite signed point measure invariant under

\[
z\mapsto1-z
\]

and supported away from \(0\) and \(1\).

For

\[
f_n(z)
=
1-
\left(
1-\frac1z
\right)^n
\]

and

\[
g_n(z)
=
1-
\left(
1-\frac1z
\right)^{-n},
\]

one has

\[
g_n(z)=f_n(1-z)
\]

and therefore

\[
\boxed{
\int g_n\,d\nu
=
\int f_n\,d\nu.
}
\]

For integer-weight finite signed measures, the left side agrees with the Li-type derivative functional of the corresponding finite rational factor.

---

# 6. Interpretation

The standard Li zero kernel and the finite-factor derivative kernel do not agree term-by-term at the same point.

Their signed responses agree after aggregation over a reflection-invariant measure.

Thus the relevant compatibility is an orbit-level statement rather than an individual-zero statement.

---

# 7. Remaining limitation

The project has not shown that the rational factor associated with the signed orbit response is an admissible entire deformation of the Riemann xi-function.

No Euler product, Dirichlet series, arithmetic coefficients, or modified prime interpretation has been constructed.

No result in this phase proves or assumes the Riemann Hypothesis.
