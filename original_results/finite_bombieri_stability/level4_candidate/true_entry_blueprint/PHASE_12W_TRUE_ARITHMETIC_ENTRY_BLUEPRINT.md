# Phase 12W — True Arithmetic Entry Blueprint

## Purpose

Phase 12V implemented interval matrix certificate infrastructure, but only with placeholder entries.

Phase 12W defines the true arithmetic entry blueprint for

\[
M_{ij}^{arith}=T[\phi_j*\phi_i^*].
\]

This phase does not yet compute certified numerical entries. It specifies the exact components that must be computed.

---

# 1. Arithmetic matrix entry

Use the coefficient-compatible convention:

\[
M_{ij}^{arith}=T[F_{ij}],
\]

where

\[
F_{ij}=\phi_j*\phi_i^*.
\]

The arithmetic functional is

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

---

# 2. Compact support cutoff

Assume every basis function is supported in

\[
[e^{-B},e^B].
\]

Then Phase 12Q proved

\[
\operatorname{supp}(F_{ij})\subset[e^{-2B},e^{2B}].
\]

Let

\[
M=e^{2B}.
\]

Then the prime sum is finite:

\[
\sum_{n=1}^{\infty}\Lambda(n)\{F_{ij}(n)+F_{ij}^*(n)\}
=
\sum_{1\le n\le M}\Lambda(n)\{F_{ij}(n)+F_{ij}^*(n)\}.
\]

---

# 3. Entry decomposition

Define:

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

Then

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

---

# Theorem 12W.1 — True arithmetic entry blueprint

For compactly supported basis functions with common support in \([e^{-B},e^B]\), every arithmetic matrix entry has the finite computable blueprint

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
A_{ij},
\]

where the prime component \(P_{ij}\) is finite and the archimedean component \(A_{ij}\) is reduced to a finite interval integral plus an explicit logarithmic term.

## Proof

This follows by combining:

1. the extracted formula for \(T[F]\);
2. Phase 12Q, which proves the prime sum has no terms beyond \(M=e^{2B}\);
3. Phase 12R, which reduces the archimedean integral to \([1,M]\) plus a logarithmic tail.

Substitute \(F=F_{ij}=\phi_j*\phi_i^*\).

\[
\square
\]

---

# 4. Certified interval blueprint

To certify an entry, compute intervals:

\[
I_{ij}^{0}\in \mathbf I_{ij}^{0},
\]

\[
I_{ij}^{*,0}\in \mathbf I_{ij}^{*,0},
\]

\[
P_{ij}\in \mathbf P_{ij},
\]

\[
C_{ij}\in \mathbf C_{ij},
\]

\[
A_{ij}\in \mathbf A_{ij}.
\]

Then

\[
M_{ij}^{arith}
\in
\mathbf I_{ij}^{0}
+
\mathbf I_{ij}^{*,0}
-
\mathbf P_{ij}
-
\mathbf C_{ij}
-
\mathbf A_{ij}.
\]

This is the exact interval entry formula needed by Phase 12V.

---

# 5. Required computational subroutines

A true arithmetic entry implementation needs:

1. basis evaluator \(\phi_j(x)\);
2. star evaluator \(\phi_i^*(x)\);
3. multiplicative convolution evaluator \(F_{ij}(x)\);
4. finite prime-sum evaluator;
5. von Mangoldt evaluator \(\Lambda(n)\);
6. central integral evaluator;
7. archimedean reduced integral evaluator;
8. removable-singularity handler near \(x=1\);
9. interval error propagation;
10. Hermitian residual verification.

---

# 6. Implementation status

Phase 12W creates a blueprint and a non-certified skeleton.

It does not claim:

1. true certified numerical entries;
2. full arithmetic-only certificate;
3. RH proof;
4. novelty.

---

# 7. Next target

Phase 12X should choose a simple explicit compactly supported toy basis that is computationally tractable.

The basis should be easy enough to evaluate numerically while preserving the structure of the theorem.

A piecewise polynomial bump is acceptable for a prototype, but the final theoretical \(C_c^\infty\) version remains the clean mathematical class.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove a complete arithmetic-only finite certificate.

This phase does not establish novelty.

Exact audit strings:

TRUE_ARITHMETIC_ENTRY_BLUEPRINT_COMPLETE

M_IJ_TRUE_ENTRY_DECOMPOSITION_DEFINED

FINITE_PRIME_COMPONENT_INCLUDED

REDUCED_ARCHIMEDEAN_COMPONENT_INCLUDED

INTERVAL_ENTRY_FORMULA_DEFINED

TRUE_CERTIFIED_NUMERICAL_ENTRIES_NOT_YET_COMPUTED

TOY_BASIS_REQUIRED_NEXT

ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE

LEVEL4_BRANCH_READY_FOR_TOY_ENTRY_PROTOTYPE

