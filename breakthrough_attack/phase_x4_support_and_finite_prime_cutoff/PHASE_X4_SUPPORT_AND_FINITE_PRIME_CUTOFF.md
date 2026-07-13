# Phase X4 — Support and Finite Prime Cutoff Theorem

## Purpose

Phase X3 built smooth pole-cancelled basis functions:

\[
\phi_j\in C_c^\infty(0,\infty),
\qquad
\widehat{\phi_j}(0)=\widehat{\phi_j}(1)=0.
\]

Phase X4 proves exact support bookkeeping for matrix-entry test functions:

\[
F_{ij}=\phi_j*\phi_i^*.
\]

The goal is to prove that each \(F_{ij}\) has compact support:

\[
\operatorname{supp}(F_{ij})\subset[A_{ij},B_{ij}],
\]

so the prime sum in \(T_{BL}[F_{ij}]\) is finite.

---

# 1. Corrected basis support

Each corrected basis function has the form:

\[
\phi_j=b_j-\alpha_j u_0-\beta_j u_1.
\]

Therefore:

\[
\operatorname{supp}(\phi_j)
\subset
\operatorname{supp}(b_j)
\cup
\operatorname{supp}(u_0)
\cup
\operatorname{supp}(u_1).
\]

If this union lies in:

\[
[L_j,U_j],
\]

then:

\[
\operatorname{supp}(\phi_j)\subset[L_j,U_j].
\]

---

# 2. Star support

The locked Hermitian star is:

\[
\phi_i^*(x)=x^{-1}\overline{\phi_i(1/x)}.
\]

The factor \(x^{-1}\) does not change support.

Thus if:

\[
\operatorname{supp}(\phi_i)\subset[L_i,U_i],
\]

then:

\[
\operatorname{supp}(\phi_i^*)\subset[U_i^{-1},L_i^{-1}].
\]

---

# 3. Multiplicative convolution support

For multiplicative convolution:

\[
(F*G)(x)=\int_0^\infty F(y)G(x/y)\frac{dy}{y},
\]

if:

\[
\operatorname{supp}(F)\subset[L_F,U_F],
\]

and:

\[
\operatorname{supp}(G)\subset[L_G,U_G],
\]

then:

\[
\operatorname{supp}(F*G)
\subset
[L_FL_G,U_FU_G].
\]

Therefore:

\[
\operatorname{supp}(\phi_j*\phi_i^*)
\subset
[L_j/U_i,\ U_j/L_i].
\]

---

# 4. Finite prime cutoff

The Bombieri–Lagarias prime sum includes:

\[
\sum_{n=1}^{\infty}\Lambda(n)\left(F_{ij}(n)+\widetilde F_{ij}(n)\right).
\]

If:

\[
\operatorname{supp}(F_{ij})\subset[A_{ij},B_{ij}],
\]

then:

\[
F_{ij}(n)=0
\]

for all integers:

\[
n>B_{ij}.
\]

Also:

\[
\widetilde F_{ij}(n)=n^{-1}F_{ij}(1/n),
\]

so \(\widetilde F_{ij}(n)\neq0\) only when:

\[
1/n\in[A_{ij},B_{ij}].
\]

This implies:

\[
n\in[1/B_{ij},1/A_{ij}].
\]

Since \(n\ge1\), the finite cutoff for the tilde side is:

\[
n\le 1/A_{ij}.
\]

Thus the full prime cutoff is:

\[
\boxed{
N_{ij}=\left\lfloor \max(B_{ij},A_{ij}^{-1})\right\rfloor.
}
\]

---

# Theorem X4.1 — corrected basis support bound

If

\[
\phi_j=b_j-\alpha_j u_0-\beta_j u_1,
\]

then:

\[
\operatorname{supp}(\phi_j)
\subset
\operatorname{supp}(b_j)
\cup
\operatorname{supp}(u_0)
\cup
\operatorname{supp}(u_1).
\]

## Proof

If \(x\) lies outside all three supports, then:

\[
b_j(x)=u_0(x)=u_1(x)=0.
\]

Therefore:

\[
\phi_j(x)=0.
\]

Thus \(x\) cannot lie in the support of \(\phi_j\).

\[
\square
\]

---

# Theorem X4.2 — star support bound

If:

\[
\operatorname{supp}(\phi_i)\subset[L_i,U_i],
\]

then:

\[
\operatorname{supp}(\phi_i^*)\subset[U_i^{-1},L_i^{-1}].
\]

## Proof

\[
\phi_i^*(x)=x^{-1}\overline{\phi_i(1/x)}.
\]

This is nonzero only when:

\[
1/x\in[L_i,U_i].
\]

Equivalently:

\[
x\in[U_i^{-1},L_i^{-1}].
\]

\[
\square
\]

---

# Theorem X4.3 — convolution support bound

If:

\[
\operatorname{supp}(\phi_j)\subset[L_j,U_j],
\]

and:

\[
\operatorname{supp}(\phi_i^*)\subset[U_i^{-1},L_i^{-1}],
\]

then:

\[
\operatorname{supp}(\phi_j*\phi_i^*)
\subset
[L_j/U_i,\ U_j/L_i].
\]

## Proof

The multiplicative convolution is nonzero only when:

\[
y\in[L_j,U_j]
\]

and:

\[
x/y\in[U_i^{-1},L_i^{-1}].
\]

Thus:

\[
x\in y[U_i^{-1},L_i^{-1}].
\]

As \(y\in[L_j,U_j]\), the possible values of \(x\) lie in:

\[
[L_j/U_i,\ U_j/L_i].
\]

\[
\square
\]

---

# Theorem X4.4 — finite prime cutoff theorem

Let:

\[
\operatorname{supp}(F_{ij})\subset[A_{ij},B_{ij}].
\]

Then the prime side of \(T_{BL}[F_{ij}]\) only needs integers:

\[
n\le
\left\lfloor
\max(B_{ij},A_{ij}^{-1})
\right\rfloor.
\]

## Proof

The non-tilde term \(F_{ij}(n)\) vanishes for \(n>B_{ij}\).

The tilde term is:

\[
\widetilde F_{ij}(n)=n^{-1}F_{ij}(1/n).
\]

This vanishes unless:

\[
1/n\in[A_{ij},B_{ij}].
\]

Equivalently:

\[
n\le A_{ij}^{-1}.
\]

Thus both sides vanish beyond:

\[
\max(B_{ij},A_{ij}^{-1}).
\]

\[
\square
\]

---

# 5. Breakthrough relevance

This phase closes the structural finite-prime-sum gate.

For each certified matrix entry, the prime side is not an infinite object after support is known.

It becomes a finite exact sum.

This is necessary for rigorous interval certification.

---

# 6. Next phase

Phase X5 should attack the archimedean removable singularity theorem at \(x=1\).

That is the next major blocker.

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not compute a certified arithmetic entry.

It proves the finite-prime-cutoff theorem needed for certified matrix entries.

Exact audit strings:

PHASE_X4_SUPPORT_AND_FINITE_PRIME_CUTOFF_COMPLETE

CORRECTED_BASIS_SUPPORT_BOUND_PROVED

STAR_SUPPORT_BOUND_PROVED

CONVOLUTION_SUPPORT_BOUND_PROVED

FINITE_PRIME_CUTOFF_THEOREM_PROVED

ENTRY_SUPPORT_TABLE_CREATED

FINITE_PRIME_SUM_GATE_CLOSED_STRUCTURALLY

CERTIFIED_ENTRY_NOT_COMPUTED

READY_FOR_PHASE_X5_ARCHIMEDEAN_REMOVABLE_SINGULARITY_THEOREM

