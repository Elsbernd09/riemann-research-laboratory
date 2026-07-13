# Phase X5 — Archimedean Removable Singularity Theorem

## Purpose

Phase X4 closed the finite-prime-sum gate structurally.

Phase X5 attacks the next major blocker:

\[
\left(F(x)+\widetilde F(x)-2x^{-2}F(1)\right)\frac{x}{x^2-1}
\]

has an apparent singularity at:

\[
x=1.
\]

For certified interval quadrature, this singularity must be removed.

---

# 1. Locked Bombieri–Lagarias archimedean integrand

The locked archimedean integrand is:

\[
A_F(x)
=
\left(F(x)+\widetilde F(x)-2x^{-2}F(1)\right)\frac{x}{x^2-1}.
\]

The locked tilde involution is:

\[
\widetilde F(x)=x^{-1}F(1/x).
\]

Therefore:

\[
A_F(x)
=
\left(F(x)+x^{-1}F(1/x)-2x^{-2}F(1)\right)
\frac{x}{x^2-1}.
\]

---

# 2. Numerator cancellation at \(x=1\)

Define:

\[
N_F(x)=F(x)+x^{-1}F(1/x)-2x^{-2}F(1).
\]

Then:

\[
N_F(1)=F(1)+F(1)-2F(1)=0.
\]

Thus the numerator vanishes at \(x=1\).

The denominator also vanishes at \(x=1\), so the singularity is potentially removable.

---

# 3. Derivative of the numerator

Differentiate:

\[
N_F(x)=F(x)+x^{-1}F(1/x)-2x^{-2}F(1).
\]

The derivative is:

\[
N_F'(x)
=
F'(x)
-
x^{-2}F(1/x)
-
x^{-3}F'(1/x)
+
4x^{-3}F(1).
\]

At \(x=1\):

\[
N_F'(1)
=
F'(1)-F(1)-F'(1)+4F(1)
=
3F(1).
\]

---

# 4. Limit at \(x=1\)

Since:

\[
x^2-1=(x-1)(x+1),
\]

we have near \(x=1\):

\[
\frac{x}{x^2-1}
=
\frac{x}{(x-1)(x+1)}.
\]

Because \(N_F(1)=0\), the limit is:

\[
\lim_{x\to1}A_F(x)
=
\frac{N_F'(1)}{2}
=
\frac{3}{2}F(1).
\]

Thus the removable value is:

\[
\boxed{
A_F(1)=\frac32F(1).
}
\]

---

# Theorem X5.1 — archimedean numerator vanishes at \(x=1\)

Let \(F\) be continuous at \(1\), and define:

\[
\widetilde F(x)=x^{-1}F(1/x).
\]

Then:

\[
F(1)+\widetilde F(1)-2F(1)=0.
\]

## Proof

\[
\widetilde F(1)=1^{-1}F(1)=F(1).
\]

Therefore:

\[
F(1)+\widetilde F(1)-2F(1)
=
F(1)+F(1)-2F(1)
=
0.
\]

\[
\square
\]

---

# Theorem X5.2 — removable archimedean limit

Let \(F\) be differentiable near \(x=1\). Define:

\[
A_F(x)
=
\left(F(x)+x^{-1}F(1/x)-2x^{-2}F(1)\right)
\frac{x}{x^2-1}.
\]

Then \(A_F\) has the removable value:

\[
A_F(1)=\frac32F(1).
\]

## Proof

Let:

\[
N_F(x)=F(x)+x^{-1}F(1/x)-2x^{-2}F(1).
\]

From Theorem X5.1:

\[
N_F(1)=0.
\]

Differentiate:

\[
N_F'(x)
=
F'(x)
-
x^{-2}F(1/x)
-
x^{-3}F'(1/x)
+
4x^{-3}F(1).
\]

At \(x=1\):

\[
N_F'(1)=3F(1).
\]

Since:

\[
x^2-1=(x-1)(x+1),
\]

we compute:

\[
\lim_{x\to1}A_F(x)
=
\lim_{x\to1}
\frac{N_F(x)}{x-1}\cdot\frac{x}{x+1}
=
N_F'(1)\cdot\frac12
=
\frac32F(1).
\]

\[
\square
\]

---

# 5. Certified integration consequence

The archimedean integrand can now be replaced by the continuous extension:

\[
A_F^{\mathrm{cont}}(x)
=
\begin{cases}
A_F(x), & x\ne1,\\
\frac32F(1), & x=1.
\end{cases}
\]

This removes the singularity blocker for future interval quadrature.

---

# 6. Breakthrough relevance

This is a real mathematical blocker removal.

It does not prove RH.

It does not prove a breakthrough.

But it gives an exact closed-form singularity removal theorem needed for certified arithmetic matrix entries.

---

# 7. Next phase

Phase X6 should create the certified quadrature theorem:

\[
\left|
\int_a^b h(x)\,dx-Q_N(h)
\right|
\le
\frac{(b-a)^3}{24N^2}
\sup_{x\in[a,b]}|h''(x)|.
\]

Then we need interval or symbolic bounds for \(h''\).

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not compute a certified arithmetic entry.

It proves the removable archimedean singularity theorem needed for certified interval quadrature.

Exact audit strings:

PHASE_X5_ARCHIMEDEAN_REMOVABLE_SINGULARITY_COMPLETE

ARCHIMEDEAN_NUMERATOR_CANCELLATION_PROVED

ARCHIMEDEAN_REMOVABLE_LIMIT_PROVED

REMOVABLE_VALUE_THREE_HALVES_F_OF_ONE_PROVED

CONTINUOUS_ARCHIMEDEAN_EXTENSION_DEFINED

ARCHIMEDEAN_SINGULARITY_GATE_CLOSED_STRUCTURALLY

CERTIFIED_ENTRY_NOT_COMPUTED

READY_FOR_PHASE_X6_CERTIFIED_QUADRATURE_THEOREM

