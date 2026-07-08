# Phase 1C Local-to-Global Audit

## Original danger

The project initially analyzed the individual zero kernel

\[
f_n(\rho)
=
1-
\left(
1-\frac1\rho
\right)^n.
\]

A naive next step would have been to claim that the same kernel arises term-by-term from the Li derivative functional applied to a finite zero factor.

That claim is false.

---

# Failed termwise bridge

For

\[
F_\rho(s)
=
1-\frac{s}{\rho},
\]

the Li-type functional

\[
\mathscr L_n[F_\rho]
\]

produces

\[
1-
\left(
1-\frac1\rho
\right)^{-n},
\]

not

\[
1-
\left(
1-\frac1\rho
\right)^n.
\]

Thus the individual-zero derivative-side kernel and the project's zero-side kernel differ.

---

# Surviving orbit-level bridge

Define

\[
g_n(\rho)
=
1-
\left(
1-\frac1\rho
\right)^{-n}.
\]

Then

\[
g_n(\rho)
=
f_n(1-\rho).
\]

For a finite signed measure invariant under

\[
\rho\mapsto1-\rho,
\]

integration against \(g_n\) equals integration against \(f_n\).

The project's signed orbit-splitting measure has exactly this reflection invariance.

Therefore the orbit-level finite-factor derivative response agrees with the signed zero-kernel response.

---

# Research significance

The bridge between the two descriptions is not termwise.

It is symmetry mediated.

Reflection invariance is therefore structurally necessary for the present finite response formalism.

This observation sharpens the research program:

the laboratory should distinguish diagnostic identities that hold at individual zeros from identities that emerge only after symmetry-orbit aggregation.

---

# Remaining obstruction

The signed finite factor ratio is not automatically an admissible deformation of the actual Riemann xi-function.

The project has established a response identity for a finite rational factor and a reflection-invariant signed zero measure.

It has not constructed a new arithmetic zeta-like function.
