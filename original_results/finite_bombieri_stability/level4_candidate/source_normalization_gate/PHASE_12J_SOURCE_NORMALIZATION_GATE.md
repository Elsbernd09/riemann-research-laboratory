# Phase 12J — Source-Normalization / Sign-Convention Gate

## Purpose

Phase 12I decomposed the finite approximation error as

\[
E_N(g)=T_N(g)+P_N^{err}(g)+S_N(g)+C_N(g).
\]

The term

\[
S_N(g)
\]

records source-normalization, sign-convention, Haar-measure, and involution compatibility uncertainty.

Phase 12J attacks this term honestly.

---

# 1. Source-normalization term

The source-normalization/sign-convention error is:

\[
S_N(g).
\]

It absorbs uncertainty from:

1. whether the correct positivity form is \(T[g*g^*]\) or \(-T[g*g^*]\);
2. whether the star involution normalization matches the project’s \(T[f]\);
3. whether the multiplicative Haar measure convention matches the project’s \(T[f]\);
4. whether the project’s extracted \(T[f]\) uses the same Mellin transform convention as the provisional \(F_g=g*g^*\);
5. whether the zero-side identity has the same sign and normalization as the arithmetic-side functional.

---

# 2. Available provisional source information

The supplied source-summary text supports the following structure:

\[
g^*(x)=\frac1x\overline{g(1/x)},
\]

\[
F_g=g*g^*,
\]

and a positivity target of the form

\[
T[g*g^*]\ge0.
\]

It also states the Mellin-side identity

\[
\widehat{g*g^*}(s)
=
\widehat g(s)\overline{\widehat g(1-\bar s)}.
\]

This is enough for provisional development.

It is not enough for final primary-source validation.

---

# 3. Gate classification

We classify the source-normalization term as:

\[
\boxed{
S_N(g)=0
\text{ only after primary-source confirmation.}
}
\]

Before primary-source confirmation, the honest bound is:

\[
|S_N(g)|\le\sigma_N(g),
\]

where \(\sigma_N(g)\) is unresolved.

Thus Phase 12J cannot set

\[
\sigma_N(g)=0
\]

as a final theorem.

---

# 4. Provisional theorem

Under the provisional convention agreement:

1. \(Q_W(g)=T[g*g^*]\);
2. \(g^*(x)=x^{-1}\overline{g(1/x)}\);
3. \((a*b)(x)=\int_0^\infty a(y)b(x/y)\,dy/y\);
4. \(T[F]=\sum_\rho \widehat F(\rho)\);
5. the positivity sign is \(Q_W(g)\ge0\);

the source-normalization term is formally zero:

\[
S_N(g)=0.
\]

This is a conditional convention theorem, not a primary-source theorem.

---

# Theorem 12J.1 — Conditional source-normalization cancellation

Assume the project conventions exactly match the classical Weil/Bombieri conventions:

\[
Q_W(g)=T[g*g^*],
\]

\[
g^*(x)=x^{-1}\overline{g(1/x)},
\]

\[
(a*b)(x)=\int_0^\infty a(y)b(x/y)\frac{dy}{y},
\]

and

\[
T[F]=\sum_\rho \widehat F(\rho)
\]

with positivity condition

\[
Q_W(g)\ge0.
\]

Then the source-normalization/sign-convention error vanishes:

\[
S_N(g)=0.
\]

## Proof

The term \(S_N(g)\) was introduced only to account for possible mismatch between the project conventions and the true classical conventions.

If the project conventions exactly match the classical conventions, then there is no sign mismatch, no involution mismatch, no Haar-measure mismatch, no Mellin-transform mismatch, and no explicit-formula normalization mismatch.

Therefore the mismatch term is identically zero:

\[
S_N(g)=0.
\]

\[
\square
\]

---

# 5. What is actually proven

Phase 12J proves:

\[
\boxed{
\text{If the conventions are confirmed, then }S_N(g)=0.
}
\]

It does not prove:

\[
\boxed{
\text{The conventions are confirmed by a primary source.}
}
\]

Therefore, in the final error bound, there are two versions.

---

# 6. Provisional bound

Under provisional convention agreement:

\[
|Q_N(P_Ng)-Q_W(g)|
\le
\tau_N(g)+\pi_N(g)+\chi_N(g).
\]

For a finite test class:

\[
\sup_{g\in\mathcal F_R^{(m)}}|Q_N(P_Ng)-Q_W(g)|
\le
\tau_N(R,m)+\pi_N(R,m)+\chi_N(R,m).
\]

---

# 7. Fully rigorous bound before primary-source confirmation

Before primary-source confirmation:

\[
|Q_N(P_Ng)-Q_W(g)|
\le
\tau_N(g)+\pi_N(g)+\sigma_N(g)+\chi_N(g).
\]

For a finite test class:

\[
\sup_{g\in\mathcal F_R^{(m)}}|Q_N(P_Ng)-Q_W(g)|
\le
\tau_N(R,m)+\pi_N(R,m)+\sigma_N(R,m)+\chi_N(R,m).
\]

---

# 8. Gate verdict

The source-normalization term is conditionally eliminated:

\[
\boxed{
S_N(g)=0
\quad
\text{under exact convention agreement.}
}
\]

But it is not finally eliminated:

\[
\boxed{
\text{primary-source confirmation still required.}
}
\]

Therefore the Level 4 branch can proceed only in provisional mode.

---

# 9. Next target

Phase 12K should attack the next real mathematical object:

\[
P_N.
\]

The finite approximation map must be defined.

Without \(P_N\), there is no projection error theorem.

The next phase must define or honestly fail to define:

\[
P_N:\mathcal D_W\to V_N.
\]

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove finite approximation convergence.

This phase does not prove Level 4 contribution.

This phase does not establish novelty.

Exact audit strings:

SOURCE_NORMALIZATION_GATE_COMPLETE

SOURCE_NORMALIZATION_TERM_DEFINED

CONDITIONAL_SOURCE_NORMALIZATION_CANCELLATION_PROVED

S_N_ZERO_ONLY_UNDER_CONVENTION_AGREEMENT

PRIMARY_SOURCE_CONFIRMATION_STILL_REQUIRED

PROVISIONAL_THREE_ERROR_BOUND_RESTORED

RIGOROUS_FOUR_ERROR_BOUND_RETAINED

FINITE_APPROXIMATION_CONVERGENCE_STILL_MISSING

LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED

