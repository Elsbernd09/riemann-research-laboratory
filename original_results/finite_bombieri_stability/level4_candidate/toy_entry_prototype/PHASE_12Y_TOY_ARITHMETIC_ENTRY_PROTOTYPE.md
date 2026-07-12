# Phase 12Y — Toy Arithmetic Entry Prototype

## Purpose

Phase 12X implemented a computable compactly supported toy basis.

Phase 12Y uses that toy basis to compute a prototype arithmetic entry

\[
M_{ij}^{arith}=T[\phi_j*\phi_i^*].
\]

This is not certified interval arithmetic yet.

It is the first end-to-end arithmetic-entry prototype.

---

# 1. Entry formula

For

\[
F_{ij}=\phi_j*\phi_i^*,
\]

the arithmetic entry blueprint is

\[
M_{ij}^{arith}
=
I_{ij}^{0}
+
I_{ij}^{*,0}
-
P_{ij}
-
C_{ij}
-
A_{ij}.
\]

The components are:

\[
I_{ij}^{0}=\int_0^\infty F_{ij}(x)\,dx,
\]

\[
I_{ij}^{*,0}=\int_0^\infty F_{ij}^*(x)\,dx,
\]

\[
P_{ij}=\sum_{1\le n\le M}\Lambda(n)\{F_{ij}(n)+F_{ij}^*(n)\},
\]

\[
C_{ij}=(\log4\pi+\gamma_E)F_{ij}(1),
\]

and

\[
A_{ij}
=
\int_1^M
\left(
F_{ij}(x)+F_{ij}^*(x)-\frac{2F_{ij}(1)}{x}
\right)
\frac{x\,dx}{x^2-1}
-
F_{ij}(1)\log\left(\frac{M+1}{M-1}\right).
\]

---

# 2. Prototype status

The prototype computes approximate floating-point versions of:

1. central integral;
2. star central integral;
3. finite prime sum;
4. constant term;
5. reduced archimedean term;
6. final entry value.

It uses midpoint quadrature and finite summation.

It is not a rigorous certificate.

---

# 3. Why this matters

This phase proves that the arithmetic-entry blueprint is computationally executable.

It creates the bridge from theorem architecture to actual arithmetic matrix computation.

---

# 4. Main limitations

The current prototype:

1. uses a piecewise-smooth toy basis;
2. uses floating-point quadrature;
3. does not certify quadrature error;
4. does not handle complex entries;
5. does not prove Hermitian symmetry;
6. does not prove RH;
7. does not prove a complete arithmetic-only certificate.

---

# 5. Next target

Phase 12Z should assemble a small toy arithmetic matrix and run the interval matrix certificate logic from Phase 12V.

This will create a full toy pipeline:

\[
\text{basis}
\to
\text{entry prototype}
\to
\text{matrix}
\to
\text{Rayleigh test}.
\]

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove a complete arithmetic-only finite certificate.

This phase does not establish novelty.

Exact audit strings:

TOY_ARITHMETIC_ENTRY_PROTOTYPE_COMPLETE

TOY_CENTRAL_INTEGRAL_COMPUTED

TOY_STAR_CENTRAL_INTEGRAL_COMPUTED

TOY_FINITE_PRIME_SUM_COMPUTED

TOY_CONSTANT_TERM_COMPUTED

TOY_ARCHIMEDEAN_TERM_COMPUTED

TOY_ARITHMETIC_ENTRY_COMPUTED

FLOATING_POINT_PROTOTYPE_ONLY

CERTIFIED_INTERVAL_ENTRY_NOT_YET_PROVED

LEVEL4_READY_FOR_TOY_MATRIX_PROTOTYPE

