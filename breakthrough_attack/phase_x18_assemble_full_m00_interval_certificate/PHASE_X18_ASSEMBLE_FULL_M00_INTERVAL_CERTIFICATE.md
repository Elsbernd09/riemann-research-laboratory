# Phase X18 — Assemble Full M00 Interval Certificate

## Purpose

Phase X18 assembles every term-level certificate for the single arithmetic entry:

\[
M_{00}=T_{BL}[F],
\qquad
F=\Phi_0*\Phi_0^*.
\]

The locked Bombieri–Lagarias functional is:

\[
T_{BL}[F]
=
\int_0^\infty F(x)\,dx
+
\int_0^\infty \widetilde F(x)\,dx
-
\sum_{n=1}^{\infty}\Lambda(n)(F(n)+\widetilde F(n))
-
(\log\pi+\gamma)F(1)
-
\int_1^\infty
\left(F(x)+\widetilde F(x)-2x^{-2}F(1)\right)
\frac{x}{x^2-1}\,dx.
\]

Earlier phases created term-level interval-certificate structures for:

1. central integral;
2. tilde integral;
3. finite prime side;
4. constant term;
5. archimedean integral.

This phase assembles them into one \(M_{00}\)-level interval object.

---

# 1. Sign structure

Let:

\[
I_c=\int F(x)\,dx,
\]

\[
I_t=\int \widetilde F(x)\,dx,
\]

\[
P=\sum_{n\le N}\Lambda(n)(F(n)+\widetilde F(n)),
\]

\[
C=-(\log\pi+\gamma)F(1),
\]

and:

\[
A=
\int_1^\infty
\left(F(x)+\widetilde F(x)-2x^{-2}F(1)\right)
\frac{x}{x^2-1}\,dx.
\]

Then:

\[
M_{00}=I_c+I_t-P+C-A.
\]

---

# 2. Interval assembly theorem

If:

\[
I_c\in \mathcal I_c,\quad
I_t\in \mathcal I_t,\quad
P\in \mathcal P,\quad
C\in \mathcal C,\quad
A\in \mathcal A,
\]

then interval arithmetic gives:

\[
M_{00}
\in
\mathcal I_c+\mathcal I_t-\mathcal P+\mathcal C-\mathcal A.
\]

---

# 3. Honest status

This phase assembles the full \(M_{00}\) interval object.

However, term-level gates remain incomplete:

1. prime-side pointwise convolution certificates;
2. constant-term pointwise convolution certificate for \(F(1)\);
3. archimedean derivative bound;
4. coefficient-solve certification;
5. outward-rounded arithmetic review.

Therefore the final status is:

\[
\boxed{
\texttt{FULL\_M00\_INTERVAL\_CERTIFICATE\_ASSEMBLED\_BUT\_NOT\_FULLY\_CERTIFIED}
}
\]

This is not yet:

\[
\texttt{CERTIFIED\_ARITHMETIC\_ENTRY}.
\]

---

# Theorem X18.1 — full M00 interval assembly

Assume every term interval is valid:

\[
I_c\in \mathcal I_c,\quad
I_t\in \mathcal I_t,\quad
P\in \mathcal P,\quad
C\in \mathcal C,\quad
A\in \mathcal A.
\]

Then:

\[
M_{00}=I_c+I_t-P+C-A
\]

is contained in:

\[
\mathcal I_c+\mathcal I_t-\mathcal P+\mathcal C-\mathcal A.
\]

## Proof

Interval addition, subtraction, and negation preserve containment.

Apply these operations in the exact sign structure of \(T_{BL}\).

\[
\square
\]

---

# Theorem X18.2 — assembled does not mean fully certified

If one or more term intervals is not fully certified, then the assembled \(M_{00}\) interval is not a fully certified arithmetic entry.

## Proof

The assembly theorem assumes all term intervals are valid.

If any term interval depends on an uncertified approximation or incomplete derivative bound, then the hypothesis is not fully established.

Therefore the assembled object is a certificate candidate, not a fully certified arithmetic entry.

\[
\square
\]

---

# 4. Breakthrough relevance

This is a serious checkpoint.

The project now has a complete single-entry Bombieri–Lagarias interval-certificate object.

But the object is still blocked by certification gates.

The next phases must harden the gates rather than merely add more structure.

---

# 5. Next phase

Phase X19 should certify the coefficient solve:

\[
\widehat\Phi(0)=\widehat\Phi(1)=0.
\]

This is critical because all later intervals depend on the corrected pole-cancelled basis.

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not compute a fully certified arithmetic entry.

It assembles the full \(M_{00}\) interval-certificate candidate.

Exact audit strings:

PHASE_X18_ASSEMBLE_FULL_M00_INTERVAL_CERTIFICATE_COMPLETE

CENTRAL_TERM_IMPORTED

TILDE_TERM_IMPORTED

PRIME_SIDE_TERM_IMPORTED

CONSTANT_TERM_IMPORTED

ARCHIMEDEAN_TERM_IMPORTED

FULL_M00_INTERVAL_ASSEMBLED

FULL_M00_INTERVAL_CERTIFICATE_ASSEMBLED_BUT_NOT_FULLY_CERTIFIED

CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED

READY_FOR_PHASE_X19_COEFFICIENT_SOLVE_CERTIFICATION

