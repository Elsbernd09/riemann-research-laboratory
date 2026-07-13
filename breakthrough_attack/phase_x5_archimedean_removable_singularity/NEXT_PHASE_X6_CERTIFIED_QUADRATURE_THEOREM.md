# Next Phase X6 — Certified Quadrature Theorem

## Goal

Create the rigorous quadrature bound needed for certified entries.

For midpoint quadrature:

\[
Q_N(h)=\sum_{k=0}^{N-1}h(a+(k+1/2)\Delta)\Delta,
\qquad
\Delta=\frac{b-a}{N}.
\]

The target theorem is:

\[
\left|
\int_a^b h(x)\,dx-Q_N(h)
\right|
\le
\frac{(b-a)^3}{24N^2}
\sup_{x\in[a,b]}|h''(x)|.
\]

## Required after theorem

1. interval bound for \(h''\);
2. outward rounding;
3. certified interval enclosure;
4. application to the continuous archimedean extension.
