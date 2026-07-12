# Phase 12G — Provisional Spectral \(Q_W\) Alignment

## Purpose

Phase 12F proved the formal Mellin identity

\[
\widehat{g*g^*}(s)
=
\widehat g(s)\overline{\widehat g(1-\bar s)}.
\]

Phase 12G combines this with the provisional explicit-formula identity

\[
T[F]=\sum_\rho \widehat F(\rho)
\]

to derive the provisional spectral expression for

\[
Q_W(g)=T[g*g^*].
\]

---

# 1. Provisional definitions

Let

\[
F_g=g*g^*.
\]

Define provisionally:

\[
Q_W(g)=T[F_g].
\]

The function \(T\) is the extracted Bombieri/Weil explicit-formula functional.

The spectral-side convention used in this phase is:

\[
T[F]=\sum_\rho \widehat F(\rho),
\]

where \(\rho\) ranges over the nontrivial zeros of \(\zeta(s)\).

---

# 2. Previously proved Mellin identity

From Phase 12F,

\[
\widehat{F_g}(s)
=
\widehat{g*g^*}(s)
=
\widehat g(s)\overline{\widehat g(1-\bar s)}.
\]

---

# Theorem 12G.1 — Provisional spectral form of \(Q_W\)

Under the provisional imported conventions,

\[
Q_W(g)
=
\sum_\rho
\widehat g(\rho)
\overline{\widehat g(1-\bar\rho)}.
\]

## Proof

By definition,

\[
Q_W(g)=T[F_g].
\]

By the spectral side of the explicit formula,

\[
T[F_g]=\sum_\rho \widehat{F_g}(\rho).
\]

By Phase 12F,

\[
\widehat{F_g}(s)
=
\widehat g(s)\overline{\widehat g(1-\bar s)}.
\]

Substituting \(s=\rho\),

\[
\widehat{F_g}(\rho)
=
\widehat g(\rho)\overline{\widehat g(1-\bar\rho)}.
\]

Therefore,

\[
Q_W(g)
=
\sum_\rho
\widehat g(\rho)
\overline{\widehat g(1-\bar\rho)}.
\]

\[
\square
\]

---

# Corollary 12G.2 — RH implies provisional positivity

Assume RH.

Then every nontrivial zero has the form

\[
\rho=\frac12+i\gamma.
\]

Hence

\[
1-\bar\rho=\rho.
\]

Therefore,

\[
\widehat g(\rho)\overline{\widehat g(1-\bar\rho)}
=
\widehat g(\rho)\overline{\widehat g(\rho)}
=
|\widehat g(\rho)|^2.
\]

Thus,

\[
Q_W(g)
=
\sum_\rho |\widehat g(\rho)|^2
\ge0.
\]

So, under the provisional framework,

\[
\mathrm{RH}
\Longrightarrow
Q_W(g)\ge0.
\]

---

# 3. What this proves

Phase 12G proves the forward positivity mechanism:

\[
\boxed{
\mathrm{RH}
\Longrightarrow
Q_W(g)\ge0
}
\]

under the provisional imported definitions and spectral convention.

It does not prove the converse.

It does not prove RH.

It does not prove that positivity implies RH.

It does not prove Level 4 finite obstruction detection.

---

# 4. Why this matters for Level 4

The Level 4 target is:

\[
Q_W(g)<0
\Longrightarrow
Q_N(P_Ng)<0
\]

for sufficiently large \(N\).

Phase 12G clarifies what a true infinite obstruction would be:

\[
Q_W(g)<0.
\]

If one could prove a finite approximation theorem

\[
|Q_N(P_Ng)-Q_W(g)|<\eta/2
\]

whenever

\[
Q_W(g)\le-\eta,
\]

then finite certified computation would detect the infinite obstruction.

That is still future work.

---

# 5. Remaining unresolved issues

The following remain unresolved:

1. primary-source confirmation of \(F_g=g*g^*\);
2. exact sign convention for \(T\) versus \(Q_W\);
3. exact admissible function domain \(\mathcal D_W\);
4. convergence of the zero sum;
5. finite approximation map \(P_N\);
6. truncation error bound;
7. projection error bound;
8. converse direction: positivity implies RH.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove Level 4 contribution.

This phase does not establish novelty.

Exact audit strings:

SPECTRAL_Q_W_ALIGNMENT_COMPLETE

PROVISIONAL_SPECTRAL_Q_W_FORM_PROVED

Q_W_EQUALS_ZERO_SUM_PRODUCT_FORM

RH_IMPLIES_PROVISIONAL_Q_W_POSITIVITY

CONVERSE_NOT_PROVED

PRIMARY_SOURCE_CONFIRMATION_STILL_REQUIRED

SIGN_CONVENTION_STILL_UNCONFIRMED

FINITE_APPROXIMATION_NOT_YET_PROVED

LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED

