# Phase 12U — \(T\)-Star Functional Audit

## Purpose

Phase 12T proved that the arithmetic matrix is Hermitian if the extracted arithmetic functional satisfies

\[
T[F^*]=\overline{T[F]}.
\]

Phase 12U audits this condition term by term.

---

# 1. Extracted functional

The project’s extracted arithmetic functional is

\[
T[F]
=
\int_0^\infty F(x)\,dx
+
\int_0^\infty F^*(x)\,dx
-
\sum_{n=1}^{\infty}\Lambda(n)\{F(n)+F^*(n)\}
-
(\log 4\pi+\gamma_E)F(1)
-
\int_1^\infty
\left(
F(x)+F^*(x)-\frac{2F(1)}{x}
\right)
\frac{x\,dx}{x^2-1}.
\]

The star operation is

\[
F^*(x)=x^{-1}\overline{F(1/x)}.
\]

---

# 2. Desired adjoint symmetry

The target identity is

\[
T[F^*]=\overline{T[F]}.
\]

This is stronger than merely saying \(T[F]=T[F^*]\) for real-valued test functions.

For complex-valued test functions, the conjugation matters.

---

# 3. Termwise obstacles

The functional contains five types of terms:

1. central integral:
   \[
   \int_0^\infty F(x)\,dx;
   \]

2. dual central integral:
   \[
   \int_0^\infty F^*(x)\,dx;
   \]

3. prime sum:
   \[
   \sum_n\Lambda(n)\{F(n)+F^*(n)\};
   \]

4. constant term:
   \[
   (\log4\pi+\gamma_E)F(1);
   \]

5. archimedean term:
   \[
   \int_1^\infty
   \left(
   F(x)+F^*(x)-\frac{2F(1)}x
   \right)
   \frac{x\,dx}{x^2-1}.
   \]

The first four terms are straightforward under conjugation and star if convergence/exchange is legal.

The archimedean term is the delicate one because it lives on \([1,\infty)\), not on the whole multiplicative line.

---

# 4. Formal real-structure hypothesis

Define the following hypothesis.

## Hypothesis 12U-H — Star-adjoint compatibility of the extracted \(T\)-functional

For every admissible test function \(F\),

\[
T[F^*]=\overline{T[F]}.
\]

This hypothesis is expected from the Weil/Bombieri Hermitian structure, but it still requires either:

1. primary-source confirmation; or
2. a complete termwise proof with all convergence and endpoint conditions checked.

Phase 12U does not claim this is fully source-confirmed.

---

# Theorem 12U.1 — Conditional \(T\)-star adjoint audit

Assume Hypothesis 12U-H:

\[
T[F^*]=\overline{T[F]}.
\]

Then the arithmetic matrix from Phase 12S is Hermitian:

\[
M_{ij}^{arith}=\overline{M_{ji}^{arith}}.
\]

## Proof

This is exactly the missing condition from Phase 12T.

Phase 12T proved that if

\[
T[F^*]=\overline{T[F]},
\]

then

\[
M^{arith}
\]

is Hermitian under the coefficient-compatible convention

\[
M_{ij}^{arith}=T[\phi_j*\phi_i^*].
\]

Therefore Hypothesis 12U-H implies

\[
M_{ij}^{arith}=\overline{M_{ji}^{arith}}.
\]

\[
\square
\]

---

# 5. Partial termwise audit

Although full source validation remains open, we can record a partial symbolic audit.

## 5.1 Central-pair terms

The pair

\[
\int_0^\infty F(x)\,dx+\int_0^\infty F^*(x)\,dx
\]

is formally stable under replacing \(F\) by \(F^*\), since the two terms swap.

With conjugation included, one needs the star integral identity

\[
\int_0^\infty F^*(x)\,dx
=
\overline{\int_0^\infty F(x)\,dx}
\]

under the correct measure/convention.

This is not automatic for \(dx\), so the exact functional normalization must be checked.

## 5.2 Prime terms

The prime term

\[
\sum_n\Lambda(n)\{F(n)+F^*(n)\}
\]

is formally stable under swapping \(F\) and \(F^*\).

But the conjugate-adjoint identity requires:

\[
\sum_n\Lambda(n)\{F^*(n)+(F^*)^*(n)\}
=
\overline{
\sum_n\Lambda(n)\{F(n)+F^*(n)\}
}.
\]

This is valid if \((F^*)^*=F\) and the star-values give the correct conjugate pairing under the chosen convention.

## 5.3 Constant term

The constant term changes from

\[
F(1)
\]

to

\[
F^*(1)=\overline{F(1)}.
\]

Since

\[
\log4\pi+\gamma_E
\]

is real, the constant term has the correct conjugation behavior.

## 5.4 Archimedean term

The archimedean term is the main unresolved audit point.

It must be shown that

\[
A[F^*]=\overline{A[F]}.
\]

This requires checking:

1. the \(F(x)\) term;
2. the \(F^*(x)\) term;
3. the subtraction term \(2F(1)/x\);
4. the kernel \(x/(x^2-1)\);
5. the endpoint \(x=1\);
6. convergence at infinity;
7. compatibility with the reduced finite-interval formula from Phase 12R.

This is not completed here.

---

# 6. Audit verdict

Phase 12U proves the following:

\[
\boxed{
\text{The Hermitian matrix theorem is valid if }T[F^*]=\overline{T[F]}.
}
\]

But Phase 12U does not prove the full termwise identity from first principles.

Therefore the status is:

\[
\boxed{
\text{T\_STAR\_ADJOINT\_SYMMETRY\_REMAINS\_A\_GATE}
}
\]

and

\[
\boxed{
\text{UNCONDITIONAL\_HERMITIAN\_STILL\_NOT\_PROVED}.
}
\]

---

# 7. Safe project status

The arithmetic matrix can now be used in one of two ways:

## Route A — Conditional Hermitian route

Proceed with:

\[
T[F^*]=\overline{T[F]}
\]

as an explicit hypothesis.

Then eigenvalue certification is conditional.

## Route B — Direct certified Hermitian route

Build arithmetic entries numerically and prove interval bounds for

\[
M_{ij}^{arith}-\overline{M_{ji}^{arith}}.
\]

If the interval contains only \(0\), Hermitian symmetry is certified for the computed finite matrix.

This is more computational but safer.

---

# 8. Next target

Phase 12V should build the certified interval implementation skeleton for arithmetic matrix entries.

It should not claim a completed arithmetic certificate yet.

It should produce:

1. interval object structure;
2. certified entry placeholder;
3. Hermitian residual interval;
4. Rayleigh quotient interval;
5. negative direction certificate logic.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove a complete arithmetic-only finite certificate.

This phase does not establish novelty.

Exact audit strings:

T_STAR_FUNCTIONAL_AUDIT_COMPLETE

T_STAR_ADJOINT_SYMMETRY_IDENTIFIED_AS_GATE

CONDITIONAL_T_STAR_TO_HERMITIAN_THEOREM_PROVED

PARTIAL_TERMWISE_AUDIT_RECORDED

ARCHIMEDEAN_TERM_REMAINS_MAIN_T_STAR_OBSTACLE

UNCONDITIONAL_HERMITIAN_STILL_NOT_PROVED

CONDITIONAL_HERMITIAN_ROUTE_AVAILABLE

DIRECT_CERTIFIED_HERMITIAN_ROUTE_AVAILABLE

ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE

