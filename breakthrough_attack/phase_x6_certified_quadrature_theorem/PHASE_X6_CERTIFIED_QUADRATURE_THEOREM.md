# Phase X6 — Certified Quadrature Theorem

## Purpose

Phase X5 removed the archimedean singularity structurally.

Phase X6 proves the rigorous quadrature theorem needed for certified arithmetic entries.

The target is the midpoint rule error bound:

\[
\left|
\int_a^b h(x)\,dx-Q_N(h)
\right|
\le
\frac{(b-a)^3}{24N^2}
\sup_{x\in[a,b]}|h''(x)|.
\]

---

# 1. Midpoint quadrature

Let:

\[
\Delta=\frac{b-a}{N}.
\]

Let the midpoint nodes be:

\[
m_k=a+\left(k+\frac12\right)\Delta,
\qquad
k=0,\dots,N-1.
\]

Define:

\[
Q_N(h)=\Delta\sum_{k=0}^{N-1}h(m_k).
\]

---

# 2. Local error bound

On one subinterval:

\[
I_k=[x_k,x_{k+1}],
\]

with midpoint \(m_k\), Taylor's theorem gives:

\[
h(x)=h(m_k)+h'(m_k)(x-m_k)+\frac12h''(\xi_x)(x-m_k)^2.
\]

Integrating over the symmetric interval around \(m_k\), the first-order term vanishes.

Thus:

\[
\left|
\int_{x_k}^{x_{k+1}}h(x)\,dx-\Delta h(m_k)
\right|
\le
\frac12 M_k\int_{x_k}^{x_{k+1}}(x-m_k)^2dx,
\]

where:

\[
M_k=\sup_{x\in I_k}|h''(x)|.
\]

Since:

\[
\int_{-\Delta/2}^{\Delta/2}u^2du=\frac{\Delta^3}{12},
\]

the local bound is:

\[
\frac{M_k\Delta^3}{24}.
\]

---

# 3. Global error bound

Summing over all \(N\) subintervals:

\[
\left|
\int_a^b h(x)\,dx-Q_N(h)
\right|
\le
\sum_{k=0}^{N-1}\frac{M_k\Delta^3}{24}.
\]

Let:

\[
M=\sup_{x\in[a,b]}|h''(x)|.
\]

Then:

\[
\le
N\frac{M\Delta^3}{24}
=
\frac{M(b-a)^3}{24N^2}.
\]

---

# Theorem X6.1 — midpoint quadrature error theorem

Let \(h\in C^2([a,b])\), and let:

\[
M_2=\sup_{x\in[a,b]}|h''(x)|.
\]

Then:

\[
\left|
\int_a^b h(x)\,dx-Q_N(h)
\right|
\le
\frac{(b-a)^3}{24N^2}M_2.
\]

## Proof

Apply the local midpoint error bound on each subinterval and sum.

\[
\square
\]

---

# 4. Certified interval consequence

If we have:

\[
Q_N(h)\in[q_L,q_U]
\]

from outward-rounded arithmetic, and:

\[
M_2\le B_2,
\]

then:

\[
\int_a^b h(x)\,dx
\in
\left[
q_L-E,\ q_U+E
\right],
\]

where:

\[
E=\frac{(b-a)^3}{24N^2}B_2.
\]

This becomes a certified interval enclosure.

---

# Theorem X6.2 — certified integral enclosure

Assume:

\[
Q_N(h)\in[q_L,q_U]
\]

and:

\[
\sup_{x\in[a,b]}|h''(x)|\le B_2.
\]

Then:

\[
\int_a^b h(x)\,dx
\in
\left[
q_L-\frac{(b-a)^3B_2}{24N^2},
q_U+\frac{(b-a)^3B_2}{24N^2}
\right].
\]

## Proof

By Theorem X6.1:

\[
\left|\int_a^b h(x)\,dx-Q_N(h)\right|\le E.
\]

Since \(Q_N(h)\in[q_L,q_U]\), the true integral lies within distance \(E\) of some value in \([q_L,q_U]\).

Therefore the true integral lies in:

\[
[q_L-E,q_U+E].
\]

\[
\square
\]

---

# 5. What remains

This theorem is rigorous, but future phases still need:

1. interval arithmetic for \(Q_N(h)\);
2. interval or symbolic upper bounds for \(h''\);
3. application to convolution integrals;
4. application to the archimedean continuous extension;
5. certified arithmetic matrix entries.

---

# 6. Breakthrough relevance

This phase turns numerical integration from a heuristic into a certifiable proof pattern.

It is necessary for the certified finite matrix attack.

But it does not yet compute a certified entry.

---

# 7. Next phase

Phase X7 should create the first certified-looking single-entry pipeline:

\[
M_{00}=T_{BL}[\phi_0*\phi_0^*].
\]

It should include:

1. finite prime side;
2. central integral side;
3. archimedean continuous extension;
4. quadrature intervals;
5. explicit error fields.

The honest goal is an interval-candidate-with-proof-structure.

If derivative bounds are not yet rigorous, it must be labeled:

\[
\texttt{CERTIFICATION\_INCOMPLETE}.
\]

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not compute a certified arithmetic entry.

It proves the certified quadrature theorem needed for future certified arithmetic entries.

Exact audit strings:

PHASE_X6_CERTIFIED_QUADRATURE_THEOREM_COMPLETE

MIDPOINT_QUADRATURE_ERROR_THEOREM_PROVED

CERTIFIED_INTEGRAL_ENCLOSURE_THEOREM_PROVED

ERROR_BOUND_FORMULA_LOCKED

QUADRATURE_CERTIFICATION_PATTERN_CREATED

CERTIFIED_ENTRY_NOT_COMPUTED

READY_FOR_PHASE_X7_SINGLE_ENTRY_CERTIFICATION_PIPELINE

